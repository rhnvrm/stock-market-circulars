"""Main pipeline orchestration for processing RSS feeds and generating content."""

import asyncio
import hashlib
import json
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from config import load_config
from extractors import ContentScraper, PDFURLExtractor, RSSExtractor
from models import ItemProgress, PipelineStage, PipelineStats, SourceStats
from processors import ClaudeProcessor, FileDownloader, TextExtractor


class CircularsPipeline:
    """Main pipeline for processing stock market circulars"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or load_config()
        
        # Configuration
        general = self.config.get("general", {})
        self.request_delay = general.get("request_delay", 2.0)
        self.claude_delay = general.get("claude_delay", 3.0)
        self.timeout = general.get("timeout", 30)
        self.debug = general.get("debug", False)
        
        # Concurrency settings
        self.max_concurrent_items = general.get("max_concurrent_items", 5)
        self.max_concurrent_sources = general.get("max_concurrent_sources", 3)
        max_claude_calls = general.get("max_concurrent_claude_calls", 2)
        max_downloads = general.get("max_concurrent_downloads", 3)
        
        # Create semaphores for concurrency control
        self.item_semaphore = asyncio.Semaphore(self.max_concurrent_items)
        
        # Initialize components
        self.rss_extractor = RSSExtractor(self.timeout)
        self.pdf_extractor = PDFURLExtractor(self.timeout)
        self.content_scraper = ContentScraper(self.timeout)
        self.file_downloader = FileDownloader(max_downloads, logger=self.log)
        self.text_extractor = TextExtractor(logger=self.log)
        self.claude_processor = ClaudeProcessor(
            self.claude_delay, 
            max_claude_calls, 
            self.config.get("prompts", {}),
            logger=self.log
        )
        
        # Load RSS feeds from config
        self.rss_feeds = self.config.get("rss_feeds", {
            "nse": "https://nsearchives.nseindia.com/content/RSS/Circulars.xml",
            "bse": "https://www.bseindia.com/data/xml/notices.xml", 
            "sebi": "https://www.sebi.gov.in/sebirss.xml"
        })
        
        # Progress tracking
        self.state_dir = Path("state")
        self.state_dir.mkdir(exist_ok=True)
        (self.state_dir / "combined_progress").mkdir(exist_ok=True)
        (self.state_dir / "combined_errors").mkdir(exist_ok=True)
    
    def log(self, message: str, level: str = "INFO", item_id: str = None):
        """Log message with optional item ID for concurrent tracking"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if item_id:
            formatted_message = f"[{timestamp}] {level}: [{item_id}] {message}"
        else:
            formatted_message = f"[{timestamp}] {level}: {message}"
        
        print(formatted_message)
        
        # Also write to log file
        log_file = self.state_dir / "combined_pipeline.log"
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(formatted_message + "\n")
    
    async def process_sources(self, sources: List[str], max_items: Optional[int] = None) -> PipelineStats:
        """Process multiple RSS sources in parallel"""
        self.log(f"Processing {len(sources)} sources in parallel (max {self.max_concurrent_sources} concurrent)")
        
        start_time = datetime.now()
        
        # Create semaphore for source-level concurrency
        source_semaphore = asyncio.Semaphore(self.max_concurrent_sources)
        
        # Process sources concurrently
        tasks = []
        for source in sources:
            if source in self.rss_feeds:
                task = self.process_source_with_semaphore(source_semaphore, source, max_items)
                tasks.append(task)
        
        source_results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Calculate overall statistics
        total_items = sum(r.total_items for r in source_results if isinstance(r, SourceStats))
        completed_items = sum(r.completed_items for r in source_results if isinstance(r, SourceStats))
        failed_items = sum(r.failed_items for r in source_results if isinstance(r, SourceStats))
        
        processing_time = (datetime.now() - start_time).total_seconds()
        overall_success_rate = (completed_items / total_items * 100) if total_items > 0 else 0
        
        return PipelineStats(
            total_sources=len(sources),
            total_items=total_items,
            processed_items=total_items,
            completed_items=completed_items,
            failed_items=failed_items,
            overall_success_rate=overall_success_rate,
            sources=[r for r in source_results if isinstance(r, SourceStats)],
            processing_time=processing_time
        )
    
    async def process_source_with_semaphore(self, semaphore: asyncio.Semaphore, source: str, max_items: Optional[int] = None) -> SourceStats:
        """Process a single source with semaphore control"""
        async with semaphore:
            return await self.process_source(source, max_items)
    
    async def process_source(self, source: str, max_items: Optional[int] = None) -> SourceStats:
        """Process a single RSS source"""
        self.log(f"Processing {source.upper()} RSS feed")
        
        if source not in self.rss_feeds:
            self.log(f"Unknown source: {source}", "ERROR")
            return SourceStats(source=source, total_items=0, processed_items=0, completed_items=0, failed_items=0, success_rate=0)
        
        self.log(f"RSS URL for {source}: {self.rss_feeds[source]}", "DEBUG")
        
        # Download and parse RSS feed
        rss_content = await self.rss_extractor.download_rss_feed(source, self.rss_feeds[source])
        if not rss_content:
            return SourceStats(source=source, total_items=0, processed_items=0, completed_items=0, failed_items=0, success_rate=0)
        
        items = self.rss_extractor.parse_rss_feed(rss_content, source)
        if max_items:
            items = items[:max_items]
        
        if not items:
            return SourceStats(source=source, total_items=0, processed_items=0, completed_items=0, failed_items=0, success_rate=0)
        
        # Process items in parallel batches
        self.log(f"Processing {len(items)} items from {source.upper()} in parallel batches")
        
        completed_count = 0
        failed_count = 0
        errors = []
        
        # Process items with semaphore control
        tasks = []
        for i, item in enumerate(items, 1):
            task = self.process_item_with_semaphore(source, item, i, len(items))
            tasks.append(task)
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Count results
        for result in results:
            if isinstance(result, Exception):
                failed_count += 1
                errors.append(str(result))
            elif result:
                completed_count += 1
            else:
                failed_count += 1
        
        success_rate = (completed_count / len(items) * 100) if items else 0
        
        return SourceStats(
            source=source,
            total_items=len(items),
            processed_items=len(items),
            completed_items=completed_count,
            failed_items=failed_count,
            success_rate=success_rate,
            errors=errors[:10]  # Limit error list
        )
    
    async def process_item_with_semaphore(self, source: str, item: Dict[str, str], batch_num: int, total_batches: int) -> bool:
        """Process a single item with semaphore control"""
        async with self.item_semaphore:
            await asyncio.sleep(self.request_delay)  # Rate limiting
            self.log(f"Processing batch {batch_num}/{total_batches} (1 items)")
            return await self.process_item(source, item)
    
    async def process_item(self, source: str, item: Dict[str, str]) -> bool:
        """Process a single RSS item through the complete pipeline"""
        # Generate unique ID for this item
        item_id = hashlib.md5(f"{source}_{item['guid']}".encode()).hexdigest()[:16]
        
        # URL-based identifiers no longer needed - using consistent item_id throughout
        
        # Load or create progress
        progress = self.load_progress(item_id)
        if not progress:
            progress = ItemProgress(
                item_id=item_id,
                source=source,
                guid=item['guid'],
                title=item['title'],
                link=item['download_url'],
                stage=PipelineStage.STARTED,
                started_at=datetime.now(),
                last_updated=datetime.now(),
                metadata={}
            )
            self.save_progress(progress)
        
        # Check if already completed
        if progress.stage == PipelineStage.COMPLETED:
            self.log(f"Item already processed (GUID): {item['title'][:50]}...", "DEBUG")
            return True
        
        # Check if permanently failed
        if progress.attempts >= 3 and progress.stage != PipelineStage.COMPLETED:
            self.log(f"Item permanently failed after 3 attempts: {item['title'][:50]}...", "DEBUG")
            return False
        
        # Check if retry needed
        if progress.attempts > 1:
            self.log(f"Retrying failed item (attempt {progress.attempts}/3): {item['title'][:50]}...")
        
        self.log(f"Processing: {item['title'][:80]}... (stage: {progress.stage.value})", "INFO", item_id)
        self.log(f"Original RSS URL: {item['download_url']}", "DEBUG", item_id)
        
        try:
            # Stage 1: Extract PDF URL (for sources that need HTML parsing)
            if progress.stage == PipelineStage.STARTED:
                if source in ["nse", "bse", "sebi"]:
                    final_url = await self.pdf_extractor.extract_pdf_url(source, item['download_url'])
                    if final_url:
                        self.log(f"URL transformed: {item['download_url']} -> {final_url}", "DEBUG", item_id)
                    else:
                        final_url = item['download_url']  # Use original URL as fallback
                else:
                    final_url = item['download_url']  # Direct PDF URL
                
                progress.metadata['final_pdf_url'] = final_url
                progress.stage = PipelineStage.PDF_URL_EXTRACTED
                progress.last_updated = datetime.now()
                progress.stages[PipelineStage.PDF_URL_EXTRACTED.value] = datetime.now()
                self.save_progress(progress)
            
            # Stage 2: Download file temporarily
            if progress.stage == PipelineStage.PDF_URL_EXTRACTED:
                temp_file, error_type = await self.file_downloader.download_temp_file(progress.metadata['final_pdf_url'], item_id)
                
                # BSE fallback: if 404 error, try to scrape content directly from original URL
                if not temp_file and error_type == "404" and source == "bse":
                    self.log(f"BSE attachment not available (404/server error), falling back to scraping original page content", "INFO", item_id)
                    try:
                        # Scrape content directly from the original RSS URL
                        original_text = await self.content_scraper.scrape_bse_page_content(item['download_url'])
                        if original_text:
                            # Create a temporary text file instead
                            temp_file_obj = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8')
                            temp_file_obj.write(original_text)
                            temp_file_obj.close()
                            temp_file_path = Path(temp_file_obj.name)
                            self.log(f"BSE page content scraped successfully ({len(original_text)} chars)", "INFO", item_id)
                            progress.metadata['temp_pdf_path'] = str(temp_file_path)
                            progress.metadata['is_text_file'] = "true"  # Mark as text file, not PDF
                            progress.metadata['original_rss_url'] = item['download_url']  # Store original RSS URL
                            progress.metadata['file_type'] = "webpage"  # BSE fallback is webpage content
                            progress.metadata['download_url'] = ""  # No direct download for webpage content
                            progress.stage = PipelineStage.PDF_DOWNLOADED
                            progress.last_updated = datetime.now()
                            progress.stages[PipelineStage.PDF_DOWNLOADED.value] = datetime.now()
                            self.save_progress(progress)
                            # Text file is ready, proceed to text extraction stage
                            temp_file = temp_file_path  # Set temp_file so normal flow continues
                        else:
                            self.log(f"BSE page content scraping failed", "ERROR", item_id)
                    except Exception as e:
                        self.log(f"BSE fallback scraping error: {e}", "ERROR", item_id)
                
                if not temp_file:
                    self.record_error(item_id, "pdf_download", f"Failed to download file")
                    return False
                
                # Store metadata for regular file downloads
                if not progress.metadata.get('is_text_file'):
                    progress.metadata['temp_pdf_path'] = str(temp_file)
                    progress.metadata['original_rss_url'] = item['download_url']  # Store original RSS URL
                    progress.metadata['download_url'] = progress.metadata['final_pdf_url']  # Store direct download URL
                    
                    # Determine file type from validation
                    _, file_type = self.file_downloader._validate_file_type(temp_file)
                    progress.metadata['file_type'] = file_type  # Store actual file type
                    
                    progress.stage = PipelineStage.PDF_DOWNLOADED
                    progress.last_updated = datetime.now()
                    progress.stages[PipelineStage.PDF_DOWNLOADED.value] = datetime.now()
                    self.save_progress(progress)
            
            # Stage 3: Extract text
            if progress.stage == PipelineStage.PDF_DOWNLOADED:
                temp_pdf_path = Path(progress.metadata['temp_pdf_path'])
                if not temp_pdf_path.exists():
                    self.record_error(item_id, "text_extraction", "Temp file missing")
                    return False
                
                # Check if this is a text file from BSE fallback
                if progress.metadata.get('is_text_file') == "true":
                    # Direct text file - just read it
                    try:
                        with open(temp_pdf_path, 'r', encoding='utf-8') as f:
                            file_text = f.read().strip()
                        self.log(f"Successfully read text file ({len(file_text)} chars)", "INFO", item_id)
                    except Exception as e:
                        self.log(f"Failed to read text file: {e}", "ERROR", item_id)
                        file_text = None
                else:
                    # Regular file extraction with MarkItDown
                    file_text = self.text_extractor.extract_file_text(temp_pdf_path, item_id)
                
                if not file_text:
                    self.log("MarkItDown failed, trying Claude file fallback...", "INFO", item_id)
                    # Store file path for direct Claude processing instead of text
                    progress.metadata['pdf_path'] = str(temp_pdf_path)
                    progress.metadata['use_pdf_fallback'] = 'true'
                else:
                    progress.metadata['pdf_text'] = file_text
                    progress.metadata['use_pdf_fallback'] = 'false'
                progress.stage = PipelineStage.TEXT_EXTRACTED
                progress.last_updated = datetime.now()
                progress.stages[PipelineStage.TEXT_EXTRACTED.value] = datetime.now()
                self.save_progress(progress)
            
            # Stage 4: Generate markdown and save
            if progress.stage == PipelineStage.TEXT_EXTRACTED:
                metadata = {
                    "source": source, 
                    "title": item['title'], 
                    "pubdate": item.get('pubdate', ''),
                    "original_rss_url": progress.metadata.get('original_rss_url', ''),
                    "download_url": progress.metadata.get('download_url', ''),
                    "file_type": progress.metadata.get('file_type', 'unknown'),
                    "pdf_url": progress.metadata.get('final_pdf_url', progress.metadata.get('download_url', '')),
                    "circular_id": item_id,
                    "link": item.get('link', '')
                }
                
                # Use appropriate Claude method based on whether we have text or need PDF fallback
                if progress.metadata.get('use_pdf_fallback', 'false') == 'true':
                    pdf_path = Path(progress.metadata['pdf_path'])
                    markdown_content = await self.claude_processor.run_claude_with_pdf(pdf_path, metadata, item_id)
                else:
                    markdown_content = await self.claude_processor.run_claude(progress.metadata['pdf_text'], metadata, item_id)
                
                if not markdown_content:
                    self.record_error(item_id, "markdown_generation", "Failed to generate markdown")
                    return False
                
                # Save content
                content_file = self._save_hugo_content(source, item['title'], markdown_content, item_id)
                progress.metadata['content_file'] = str(content_file)
                progress.stage = PipelineStage.MARKDOWN_GENERATED
                progress.last_updated = datetime.now()
                progress.stages[PipelineStage.MARKDOWN_GENERATED.value] = datetime.now()
                self.save_progress(progress)
            
            # Stage 5: Complete
            if progress.stage == PipelineStage.MARKDOWN_GENERATED:
                progress.stage = PipelineStage.COMPLETED
                progress.last_updated = datetime.now()
                progress.stages[PipelineStage.COMPLETED.value] = datetime.now()
                self.save_progress(progress)
                self.log(f"✅ Successfully completed: {item['title'][:50]}...", "INFO", item_id)
                return True
                
        except Exception as e:
            self.record_error(item_id, progress.stage.value, str(e))
            return False
        
        return False
    
    def load_progress(self, item_id: str) -> Optional[ItemProgress]:
        """Load progress from JSON file"""
        progress_file = self.state_dir / "combined_progress" / f"{item_id}.json"
        try:
            if progress_file.exists():
                with open(progress_file, 'r') as f:
                    data = json.load(f)
                return ItemProgress(**data)
        except Exception as e:
            self.log(f"Error loading progress for {item_id}: {e}", "ERROR")
        return None
    
    def save_progress(self, progress: ItemProgress):
        """Save progress to JSON file"""
        progress_file = self.state_dir / "combined_progress" / f"{progress.item_id}.json"
        try:
            with open(progress_file, 'w') as f:
                # Use model_dump_json for proper serialization of datetime and enums
                json_str = progress.model_dump_json(indent=2)
                f.write(json_str)
            self.log(f"Updated progress to stage: {progress.stage.value}", "DEBUG", progress.item_id)
        except Exception as e:
            self.log(f"Error saving progress for {progress.item_id}: {e}", "ERROR")
    
    def record_error(self, item_id: str, stage: str, error: str):
        """Record error in progress and error file"""
        progress = self.load_progress(item_id)
        if progress:
            progress.attempts += 1
            progress.error_message = error
            progress.last_updated = datetime.now()
            self.save_progress(progress)
        
        # Also save to error file
        error_file = self.state_dir / "combined_errors" / f"{item_id}.json"
        error_data = {
            "item_id": item_id,
            "stage": stage,
            "error": error,
            "timestamp": datetime.now().isoformat(),
            "attempt": progress.attempts if progress else 1
        }
        with open(error_file, 'w') as f:
            json.dump(error_data, f, indent=2)
        
        self.log(f"Recorded error for {item_id} at stage {stage} (attempt {progress.attempts if progress else 1}): {error}", "ERROR")
    
    def _save_hugo_content(self, source: str, title: str, content: str, item_id: str) -> Path:
        """Save generated content to Hugo site structure"""
        # Create standardized filename: {source}-{date}-{item_id}-{clean-title}.md
        today = datetime.now().strftime("%Y-%m-%d")
        
        # Create kebab-case title (lowercase with hyphens)
        clean_title = title.lower()
        clean_title = "".join(c if c.isalnum() else '-' for c in clean_title)
        clean_title = '-'.join(word for word in clean_title.split('-') if word)  # Remove empty parts
        clean_title = clean_title[:30]  # Limit length since we're adding item_id
        
        filename = f"{source}-{today}-{item_id}-{clean_title}.md"
        
        # Create directory structure
        content_dir = Path("hugo-site/content/circulars") / source / "2025"
        content_dir.mkdir(parents=True, exist_ok=True)
        
        # Save content
        content_file = content_dir / filename
        
        with open(content_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        self.log(f"✅ Content saved: {filename}", "INFO", item_id)
        return content_file
    
    async def regenerate_item_markdown(self, item_id: str, source_filter: str = None) -> bool:
        """Regenerate markdown content for a specific item"""
        try:
            # Find the progress file  
            progress_file = self.state_dir / "combined_progress" / f"{item_id}.json"
            if not progress_file.exists():
                self.log(f"Progress file not found for item {item_id}", "ERROR", item_id)
                return False
            
            # Load progress
            progress = self.load_progress(item_id)
            if not progress:
                self.log(f"Failed to load progress for item {item_id}", "ERROR", item_id)
                return False
            
            # Check source filter
            if source_filter and progress.source != source_filter:
                self.log(f"Item {item_id} source {progress.source} doesn't match filter {source_filter}", "ERROR", item_id)
                return False
            
            # Reset to text_extracted stage to force regeneration
            if progress.stage.value not in ["text_extracted", "markdown_generated", "completed"]:
                self.log(f"Item {item_id} is in stage {progress.stage.value}, cannot regenerate markdown", "ERROR", item_id)
                return False
            
            progress.stage = PipelineStage.TEXT_EXTRACTED
            progress.last_updated = datetime.now()
            if PipelineStage.MARKDOWN_GENERATED.value in progress.stages:
                del progress.stages[PipelineStage.MARKDOWN_GENERATED.value]
            if PipelineStage.COMPLETED.value in progress.stages:
                del progress.stages[PipelineStage.COMPLETED.value]
            
            self.save_progress(progress)
            self.log(f"Reset item {item_id} to text_extracted stage for regeneration", "INFO", item_id)
            
            # Process markdown generation directly
            source = progress.source
            
            # Create metadata for Claude processing
            metadata = {
                "source": source, 
                "title": progress.title, 
                "pubdate": progress.metadata.get('pubdate', ''),
                "original_rss_url": progress.metadata.get('original_rss_url', ''),
                "download_url": progress.metadata.get('download_url', ''),
                "file_type": progress.metadata.get('file_type', 'unknown'),
                "pdf_url": progress.metadata.get('final_pdf_url', progress.metadata.get('download_url', '')),
                "circular_id": item_id,
                "link": progress.link
            }
            
            # Use appropriate Claude method based on whether we have text or need PDF fallback
            if progress.metadata.get('use_pdf_fallback', 'false') == 'true':
                pdf_path = Path(progress.metadata['pdf_path'])
                # Check if temp file still exists for regeneration
                if pdf_path.exists():
                    markdown_content = await self.claude_processor.run_claude_with_pdf(pdf_path, metadata, item_id)
                else:
                    # For regeneration, temp file may not exist - re-download if needed
                    self.log(f"Temp PDF file no longer exists, re-downloading for regeneration: {progress.metadata.get('final_pdf_url', '')}", "INFO", item_id)
                    
                    # Re-download the PDF
                    pdf_url = progress.metadata.get('final_pdf_url', progress.metadata.get('download_url', ''))
                    if pdf_url:
                        new_temp_path, error_type = await self.file_downloader.download_temp_file(pdf_url, item_id)
                        if new_temp_path and error_type is None:
                            markdown_content = await self.claude_processor.run_claude_with_pdf(new_temp_path, metadata, item_id)
                            # Clean up temp file after processing
                            new_temp_path.unlink()
                        else:
                            self.log(f"Failed to re-download PDF for regeneration, falling back to extracted text", "WARNING", item_id)
                            # Fallback to extracted text if available
                            if progress.metadata.get('pdf_text'):
                                markdown_content = await self.claude_processor.run_claude(progress.metadata['pdf_text'], metadata, item_id)
                            else:
                                self.record_error(item_id, "markdown_generation", "Cannot regenerate - no PDF access and no extracted text")
                                return False
                    else:
                        self.record_error(item_id, "markdown_generation", "Cannot regenerate - no PDF URL available")
                        return False
            else:
                markdown_content = await self.claude_processor.run_claude(progress.metadata['pdf_text'], metadata, item_id)
            
            if not markdown_content:
                self.record_error(item_id, "markdown_generation", "Failed to generate markdown")
                return False
            
            # Save content
            content_file = self._save_hugo_content(source, progress.title, markdown_content, item_id)
            progress.metadata['content_file'] = str(content_file)
            progress.stage = PipelineStage.MARKDOWN_GENERATED
            progress.last_updated = datetime.now()
            progress.stages[PipelineStage.MARKDOWN_GENERATED.value] = datetime.now()
            
            # Mark as completed
            progress.stage = PipelineStage.COMPLETED
            progress.stages[PipelineStage.COMPLETED.value] = datetime.now()
            self.save_progress(progress)
            
            self.log(f"Successfully regenerated markdown for {item_id}", "INFO", item_id)
            return True
            
        except Exception as e:
            self.log(f"Error regenerating item {item_id}: {e}", "ERROR", item_id)
            return False