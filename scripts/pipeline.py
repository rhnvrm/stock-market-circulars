"""Main pipeline orchestration for processing RSS feeds and generating content."""

import asyncio
import hashlib
import json
import re
import tempfile
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from config import load_config
from extractors import ContentScraper, PDFURLExtractor, RSSExtractor
from frontmatter_manager import FrontmatterManager
from models import PipelineStats, SourceStats
from processors import ClaudeProcessor, FileDownloader, TextExtractor

# Pre-compiled regex for SEBI date format parsing
SEBI_DATE_PATTERN = re.compile(r'(\d{1,2})\s+(\w{3}),?\s+(\d{4})\s+([+-]\d{4})')

# Month name to number mapping
MONTH_NAMES = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}


def parse_rss_date(pubdate: str) -> str:
    """Convert RSS pubDate format to ISO format"""
    if not pubdate:
        raise ValueError("pubDate is missing from RSS feed item")
    
    try:
        # Try RFC 2822 format first (standard RSS format)
        dt = parsedate_to_datetime(pubdate)
        return dt.isoformat()
    except Exception:
        # Handle SEBI's non-standard format: "25 Jul, 2025 +0530"
        try:
            # Extract components using pre-compiled regex
            match = SEBI_DATE_PATTERN.match(pubdate.strip())
            if match:
                day, month_str, year, tz = match.groups()
                
                # Convert month name to number using constant
                month = MONTH_NAMES.get(month_str)
                if not month:
                    raise ValueError(f"Unknown month: {month_str}")
                
                # Parse timezone offset
                tz_sign = 1 if tz[0] == '+' else -1
                tz_hours = int(tz[1:3])
                tz_minutes = int(tz[3:5])
                
                # Create datetime with timezone
                tz_offset = timezone(timedelta(hours=tz_sign*tz_hours, minutes=tz_sign*tz_minutes))
                dt = datetime(int(year), month, int(day), tzinfo=tz_offset)
                
                return dt.isoformat()
            else:
                raise ValueError(f"Unrecognized date format: {pubdate}")
                
        except Exception as e:
            raise ValueError(f"Failed to parse pubDate '{pubdate}': {e}")


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
        self.rss_extractor = RSSExtractor(self.timeout, self.config.get('processing', {}).get('retry_delays', [5, 15, 30]))
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
        
        # Logging directory (no longer using JSON state files)
        self.state_dir = Path("state")
        self.state_dir.mkdir(exist_ok=True)
        
        # Content-based state management
        content_dir = Path(self.config.get("directories", {}).get("content_dir", "hugo-site/content/circulars"))
        self.frontmatter_manager = FrontmatterManager(content_dir, logger=self.log)
    
    def log(self, message: str, level: str = "INFO", item_id: str = None):
        """Log message with optional item ID for concurrent tracking"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if item_id:
            formatted_message = f"[{timestamp}] {level}: [{item_id}] {message}"
        else:
            formatted_message = f"[{timestamp}] {level}: {message}"
        
        print(formatted_message)
        
        # Also write to log file
        log_file = Path("combined_pipeline.log")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(formatted_message + "\n")

    async def process_sources(self, sources: List[str], max_items: Optional[int] = None) -> PipelineStats:
        """Process multiple RSS sources in parallel"""
        start_time = datetime.now()
        
        # Create semaphore for source concurrency
        source_semaphore = asyncio.Semaphore(self.max_concurrent_sources)
        
        # Process all sources concurrently
        tasks = []
        for source in sources:
            task = self.process_source_with_semaphore(source_semaphore, source, max_items)
            tasks.append(task)
        
        # Wait for all sources to complete
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Aggregate results
        total_items = 0
        processed_items = 0 
        completed_items = 0
        failed_items = 0
        source_results = {}
        
        for i, result in enumerate(results):
            source = sources[i]
            if isinstance(result, Exception):
                self.log(f"Source {source} failed with error: {result}", "ERROR")
                source_results[source] = SourceStats(source=source, total_items=0, processed_items=0, completed_items=0, failed_items=0, success_rate=0)
            else:
                total_items += result.total_items
                processed_items += result.processed_items
                completed_items += result.completed_items
                failed_items += result.failed_items
                source_results[source] = result
        
        # Calculate overall success rate
        success_rate = (completed_items / processed_items * 100) if processed_items > 0 else 0
        
        elapsed_time = datetime.now() - start_time
        
        return PipelineStats(
            total_sources=len(sources),
            total_items=total_items,
            processed_items=processed_items,
            completed_items=completed_items,
            failed_items=failed_items,
            success_rate=success_rate,
            source_results=source_results,
            elapsed_time=elapsed_time
        )

    async def process_source_with_semaphore(self, semaphore: asyncio.Semaphore, source: str, max_items: Optional[int] = None) -> SourceStats:
        """Process a single source with semaphore control"""
        async with semaphore:
            return await self.process_source(source, max_items)

    async def process_source(self, source: str, max_items: Optional[int] = None) -> SourceStats:
        """Process a single RSS source"""
        self.log(f"Processing {source.upper()} RSS feed")
        self.log(f"RSS URL for {source}: {self.rss_feeds.get(source)}", "DEBUG")
        
        # Download RSS feed
        rss_url = self.rss_feeds.get(source)
        if not rss_url:
            self.log(f"No RSS URL configured for source: {source}", "ERROR")
            return SourceStats(source=source, total_items=0, processed_items=0, completed_items=0, failed_items=0, success_rate=0)
        
        rss_content = await self.content_scraper.fetch_content(rss_url)
        if not rss_content:
            self.log(f"Failed to download RSS feed for {source}", "ERROR")
            return SourceStats(source=source, total_items=0, processed_items=0, completed_items=0, failed_items=0, success_rate=0)
        
        items = self.rss_extractor.parse_rss_feed(rss_content, source)
        if max_items:
            items = items[:max_items]
        
        if not items:
            return SourceStats(source=source, total_items=0, processed_items=0, completed_items=0, failed_items=0, success_rate=0)
        
        # Process items in parallel batches
        self.log(f"Processing {len(items)} items from {source.upper()} in parallel batches")
        
        # Check processing status and filter out completed items
        self.log(f"Checking processing status for {len(items)} items...")
        original_count = len(items)
        items_to_process = []
        
        for item in items:
            try:
                # Generate circular ID
                circular_id = hashlib.md5(f"{source}_{item['guid']}".encode()).hexdigest()[:16]
                
                # Check if already processed
                if self.frontmatter_manager.is_processed(circular_id, source):
                    self.log(f"Item already processed: {item['title'][:50]}...", "DEBUG", circular_id)
                    continue
                
                # Add to processing queue
                items_to_process.append(item)
                
                # Basic metadata for state tracking including original RSS URL
                base_metadata = {
                    'source': source,
                    'title': item['title'],
                    'circular_id': circular_id,
                    'published_date': parse_rss_date(item.get('pubdate', '')),
                    'guid': item['guid'],
                    'rss_url': item['download_url']  # Original URL from RSS feed
                }
                
                # Generate content path
                content_path = self.frontmatter_manager.generate_content_path(
                    source, 
                    base_metadata['published_date'], 
                    circular_id, 
                    item['title']
                )
                
                # Write initial state file only if not already exists
                if not content_path.exists():
                    self.frontmatter_manager.write_state_file(content_path, base_metadata, "discovered", "processing")
                
            except Exception as e:
                self.log(f"Failed to create initial state file for {item.get('title', 'unknown')}: {e}", "ERROR")
        
        # Update items list to only include items that need processing
        items = items_to_process
        skipped_count = original_count - len(items)
        
        if not items:
            self.log(f"All {original_count} items already processed for {source}")
            return SourceStats(source=source, total_items=original_count, processed_items=0, completed_items=original_count, failed_items=0, success_rate=100.0, errors=[])
        
        self.log(f"Found {len(items)} items to process (skipped {skipped_count} already completed)")
        
        completed_count = 0
        failed_count = 0
        errors = []
        
        # Process items with semaphore control
        tasks = []
        for i, item in enumerate(items, 1):
            task = self.process_item_with_semaphore(source, item, i, len(items))
            tasks.append(task)
        
        # Wait for all items to complete and collect results
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for result in results:
            if isinstance(result, Exception):
                failed_count += 1
                errors.append(str(result))
            elif result:
                completed_count += 1
            else:
                failed_count += 1
        
        success_rate = (completed_count / len(items) * 100) if len(items) > 0 else 0
        
        self.log(f"Completed {source.upper()}: {completed_count}/{len(items)} successful ({success_rate:.1f}%)")
        
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
            return await self.process_item_content_based(source, item)
    
    async def process_item_content_based(self, source: str, item: Dict[str, str]) -> bool:
        """Process a single RSS item using content-based state management"""
        # Generate unique circular ID from GUID
        circular_id = hashlib.md5(f"{source}_{item['guid']}".encode()).hexdigest()[:16]
        
        self.log(f"Processing: {item['title'][:80]}...", "INFO", circular_id)
        self.log(f"Original RSS URL: {item['download_url']}", "DEBUG", circular_id)
        
        try:
            # Basic metadata for state tracking including original RSS URL
            base_metadata = {
                'source': source,
                'title': item['title'],
                'circular_id': circular_id,
                'published_date': parse_rss_date(item.get('pubdate', '')),
                'guid': item['guid'],
                'rss_url': item['download_url']  # Original URL from RSS feed
            }
            
            # Generate content path early for state tracking
            content_path = self.frontmatter_manager.generate_content_path(
                source, 
                base_metadata['published_date'], 
                circular_id, 
                item['title']
            )
            
            # Stage 1: Extract PDF URL (for sources that need HTML parsing) 
            self.frontmatter_manager.write_state_file(content_path, base_metadata, "url_extraction", "processing")
            
            final_url = item['download_url']
            if source in ["bse", "sebi"]:  # NSE has direct PDF URLs
                extracted_url = await self.pdf_extractor.extract_pdf_url(source, item['download_url'])
                if extracted_url:
                    final_url = extracted_url
                    self.log(f"URL extracted: {item['download_url']} -> {final_url}", "DEBUG", circular_id)
            
            # Update metadata with final URL
            base_metadata['pdf_url'] = final_url
            
            # Stage 2: Download file temporarily
            self.frontmatter_manager.write_state_file(content_path, base_metadata, "downloading", "processing")
            
            temp_file, error_type = await self.file_downloader.download_temp_file(final_url, circular_id)
            if not temp_file:
                self.log(f"Failed to download file: {error_type}", "ERROR", circular_id)
                
                # BSE fallback: if 404 error, try scraping the original notice page HTML
                if error_type == "404" and source == "bse" and item['guid']:
                    self.log(f"Attempting BSE HTML fallback for 404 error", "INFO", circular_id)
                    self.frontmatter_manager.write_state_file(content_path, base_metadata, "html_fallback", "processing")
                    
                    try:
                        # Extract text from the original BSE notice page
                        html_text = await self.text_extractor.extract_html_text(item['guid'], circular_id)
                        if html_text and len(html_text) > 100:
                            self.log(f"Successfully extracted {len(html_text)} characters from BSE HTML", "INFO", circular_id)
                            
                            # Process the HTML content with Claude
                            self.frontmatter_manager.write_state_file(content_path, base_metadata, "claude_processing", "processing")
                            claude_content = await self.claude_processor.run_claude(html_text, base_metadata, circular_id)
                            
                            if claude_content:
                                # Stage 5: Finalize and write content
                                self.frontmatter_manager.write_state_file(content_path, base_metadata, "finalizing", "processing")
                                
                                processing_state = self.frontmatter_manager.create_processing_state(
                                    status="published",
                                    stage="completed",
                                    content_hash=hashlib.md5(claude_content.encode()).hexdigest()[:16]
                                )
                                
                                success = self.frontmatter_manager.write_content_file(
                                    content_path, 
                                    claude_content, 
                                    base_metadata, 
                                    processing_state
                                )
                                
                                if success:
                                    self.log(f"Successfully processed BSE HTML fallback: {content_path.name}", "INFO", circular_id)
                                    return True
                                else:
                                    self.log(f"Failed to write BSE HTML fallback content", "ERROR", circular_id)
                                    
                        else:
                            self.log(f"BSE HTML extraction insufficient ({len(html_text) if html_text else 0} chars)", "WARNING", circular_id)
                            
                    except Exception as e:
                        self.log(f"BSE HTML fallback failed: {e}", "ERROR", circular_id)
                
                # Write failure state
                self.frontmatter_manager.write_state_file(content_path, base_metadata, "download_failed", "failed")
                return False
            
            # Stage 3: Extract text content
            self.frontmatter_manager.write_state_file(content_path, base_metadata, "text_extraction", "processing")
            
            extracted_text = self.text_extractor.extract_file_text(temp_file, circular_id)
            
            # Stage 4: Generate content with Claude
            self.frontmatter_manager.write_state_file(content_path, base_metadata, "claude_processing", "processing")
            
            # Try text-based approach first, fallback to PDF direct processing
            if extracted_text and len(extracted_text) > 50:
                claude_content = await self.claude_processor.run_claude(extracted_text, base_metadata, circular_id)
            else:
                self.log(f"Text extraction failed/insufficient, trying direct PDF processing", "WARNING", circular_id)
                claude_content = await self.claude_processor.run_claude_with_pdf(temp_file, base_metadata, circular_id)
            
            # Clean up temp file
            if temp_file and temp_file.exists():
                temp_file.unlink()
            
            if not claude_content:
                self.log(f"Claude processing failed", "ERROR", circular_id)
                # Write failure state
                self.frontmatter_manager.write_state_file(content_path, base_metadata, "claude_failed", "failed")
                return False
            
            # Stage 5: Write final content file with processing state
            self.frontmatter_manager.write_state_file(content_path, base_metadata, "finalizing", "processing")
            
            # Create processing state
            processing_state = self.frontmatter_manager.create_processing_state(
                status="published",
                stage="completed", 
                content_hash=self.frontmatter_manager.get_content_hash(claude_content)
            )
            
            # Write the final content file
            success = self.frontmatter_manager.write_content_file(
                content_path, 
                claude_content, 
                base_metadata, 
                processing_state
            )
            
            if success:
                self.log(f"Successfully processed and saved: {content_path.name}", "INFO", circular_id)
                return True
            else:
                self.log(f"Failed to write content file", "ERROR", circular_id)
                
                # Mark as failed to prevent infinite reprocessing
                try:
                    self.frontmatter_manager.write_state_file(content_path, base_metadata, "write_failed", "failed")
                    self.log(f"Marked item as failed due to write failure", "INFO", circular_id)
                except Exception as state_error:
                    self.log(f"Failed to update state after write failure: {state_error}", "ERROR", circular_id)
                
                return False
                
        except Exception as e:
            self.log(f"Processing error: {e}", "ERROR", circular_id)
            return False
    
    async def process_item(self, source: str, item: Dict[str, str]) -> bool:
        """Legacy method - redirects to content-based processing"""
        return await self.process_item_content_based(source, item)
    
    async def regenerate_item_markdown(self, item_id: str, source: str) -> bool:
        """Regenerate a specific item by reprocessing it from scratch"""
        try:
            # Find the existing content file
            content_path = None
            content_dir = Path(f"hugo-site/content/circulars/{source}")
            
            for year_dir in content_dir.glob("*"):
                if year_dir.is_dir():
                    for file_path in year_dir.glob(f"*{item_id}*.md"):
                        content_path = file_path
                        break
                if content_path:
                    break
            
            if not content_path or not content_path.exists():
                self.log(f"Content file not found for item {item_id}", "ERROR", item_id)
                return False
            
            # Parse existing frontmatter to get original RSS data
            try:
                existing_metadata = self.frontmatter_manager.parse_frontmatter(content_path)
                if not existing_metadata:
                    self.log(f"Could not parse frontmatter from {content_path}", "ERROR", item_id)
                    return False
                
                # Reconstruct item data for reprocessing
                item_data = {
                    'guid': existing_metadata.get('guid', ''),
                    'title': existing_metadata.get('title', ''),
                    'download_url': existing_metadata.get('rss_url', existing_metadata.get('pdf_url', ''))
                }
                
                self.log(f"Regenerating item {item_id}: {item_data['title']}", "INFO", item_id)
                
                # Delete existing file and reprocess
                content_path.unlink()
                return await self.process_item_content_based(source, item_data)
                
            except Exception as e:
                self.log(f"Failed to parse existing metadata: {e}", "ERROR", item_id)
                return False
                
        except Exception as e:
            self.log(f"Regeneration error: {e}", "ERROR", item_id)
            return False