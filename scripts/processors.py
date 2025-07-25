"""File processing, text extraction, and Claude integration."""

import asyncio
import json
import re
import shlex
import subprocess
import tempfile
from pathlib import Path
from typing import Dict, Optional, Tuple

import httpx
from markitdown import MarkItDown


class FileDownloader:
    """Handles file downloads with validation"""
    
    def __init__(self, max_downloads: int = 3, logger=None):
        self.download_semaphore = asyncio.Semaphore(max_downloads)
        self.logger = logger or print
    
    def _log(self, message: str, level: str = "INFO", item_id: str = None):
        """Helper method for consistent logging"""
        if item_id and callable(self.logger):
            self.logger(message, level, item_id)
        else:
            print(message)
    
    async def download_temp_file(self, url: str, item_id: str = None) -> Tuple[Optional[Path], Optional[str]]:
        """Download file to temporary location with validation
        Returns: (file_path, error_type) where error_type can be '404', 'validation', or None
        """
        async with self.download_semaphore:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
            
            try:
                temp_file = tempfile.NamedTemporaryFile(suffix='.tmp', delete=False)
                temp_path = Path(temp_file.name)
                temp_file.close()
                
                async with httpx.AsyncClient(timeout=60) as client:
                    self._log(f"Downloading file temporarily: {url}", "INFO", item_id)
                    async with client.stream('GET', url, headers=headers) as response:
                        response.raise_for_status()
                        
                        with open(temp_path, 'wb') as f:
                            async for chunk in response.aiter_bytes():
                                f.write(chunk)
                
                is_valid, file_type = self._validate_file_type(temp_path)
                if is_valid:
                    self._log(f"File downloaded and validated ({file_type}): {temp_path}", "INFO", item_id)
                    return temp_path, None
                else:
                    # For debugging: log first 200 chars of failed file
                    try:
                        with open(temp_path, 'r', encoding='utf-8', errors='replace') as f:
                            sample = f.read(200)
                        self._log(f"File validation failed ({file_type}): {url} - Content sample: {sample[:100]}...", "ERROR", item_id)
                    except:
                        self._log(f"File validation failed ({file_type}): {url}", "ERROR", item_id)
                    temp_path.unlink()
                    return None, "validation"
                
            except Exception as e:
                self._log(f"Failed to download file {url}: {e}", "ERROR", item_id)
                if 'temp_path' in locals() and temp_path.exists():
                    temp_path.unlink()
                
                # Check if this is a BSE error that needs fallback (404 or 302 redirect to error page)
                error_str = str(e).lower()
                if "bseindia.com" in url and ("404" in error_str or ("302" in error_str and "error=500" in error_str)):
                    return None, "404"
                
                return None, "other"
    
    def _validate_file_type(self, file_path: Path) -> Tuple[bool, str]:
        """Validate file type by checking binary signatures"""
        try:
            with open(file_path, 'rb') as f:
                header = f.read(16)
            
            # PDF signature
            if header.startswith(b'%PDF'):
                return True, 'pdf'
            
            # ZIP/Office documents (DOCX, XLSX, etc.)
            elif header.startswith(b'PK\x03\x04'):
                return True, 'zip_office'
            
            # Legacy Office documents
            elif header.startswith(b'\\xd0\\xcf\\x11\\xe0\\xa1\\xb1\\x1a\\xe1'):
                return True, 'legacy_office'
            
            # HTML/text content (often error pages)
            elif header.startswith(b'<!DOCTYPE') or header.startswith(b'<html'):
                return False, 'html_error_page'
            
            # Generic binary check
            elif any(b > 127 for b in header[:8]):
                return True, 'unknown_binary'
            
            else:
                return False, 'unknown_text'
                
        except Exception as e:
            self._log(f"Error validating file type: {e}", "ERROR")
            return False, 'error'


class TextExtractor:
    """Extracts text from various file formats"""
    
    def __init__(self, logger=None):
        self.logger = logger or print
    
    def _log(self, message: str, level: str = "INFO", item_id: str = None):
        """Helper method for consistent logging"""
        if item_id and callable(self.logger):
            self.logger(message, level, item_id)
        else:
            print(message)
    
    def extract_file_text(self, file_path: Path, item_id: str = None) -> Optional[str]:
        """Extract text from file using MarkItDown (supports PDF, Office docs, ZIP)"""
        try:
            is_valid, file_type = FileDownloader()._validate_file_type(file_path)
            if not is_valid:
                self._log(f"File type validation failed: {file_type}", "ERROR", item_id)
                return None
                
            self._log(f"Extracting text from {file_type} file using MarkItDown...", "INFO", item_id)
            markitdown = MarkItDown()
            result = markitdown.convert(str(file_path))
            
            if not result or not result.text_content:
                self._log(f"MarkItDown failed to extract text from {file_type} file", "ERROR", item_id)
                return None
            
            content = result.text_content.strip()
            if len(content) < 50:
                self._log(f"File content too short ({len(content)} chars)", "WARNING", item_id)
                return None
            
            self._log(f"Successfully extracted {len(content)} characters from {file_type} file", "INFO", item_id)
            return content
            
        except Exception as e:
            self._log(f"Text extraction failed: {e}", "ERROR", item_id)
            return None
    
    async def extract_html_text(self, url: str, item_id: str = None) -> Optional[str]:
        """Extract text content from HTML page (BSE fallback)"""
        try:
            import httpx
            from bs4 import BeautifulSoup
            
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
            
            async with httpx.AsyncClient(timeout=30) as client:
                self._log(f"Fetching HTML content from: {url}", "INFO", item_id)
                response = await client.get(url, headers=headers)
                response.raise_for_status()
                
                # Parse HTML and extract text content
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Remove script and style elements
                for script in soup(["script", "style"]):
                    script.decompose()
                
                # Look for main content areas (BSE-specific selectors)
                content_selectors = [
                    'div.content',
                    'div.main-content', 
                    'div#content',
                    'table.tbldata',
                    'div.notice-content',
                    'td.normalText'  # Common BSE notice text class
                ]
                
                text_content = ""
                for selector in content_selectors:
                    elements = soup.select(selector)
                    if elements:
                        for element in elements:
                            text_content += element.get_text(separator=" ", strip=True) + "\n"
                        break
                
                # Fallback to body text if no specific content found
                if not text_content or len(text_content.strip()) < 100:
                    body = soup.find('body')
                    if body:
                        text_content = body.get_text(separator=" ", strip=True)
                
                # Clean up text
                text_content = text_content.strip()
                
                if len(text_content) < 100:
                    self._log(f"HTML text content too short ({len(text_content)} chars)", "WARNING", item_id)
                    return None
                
                self._log(f"Successfully extracted {len(text_content)} characters from HTML", "INFO", item_id)
                return text_content
                
        except Exception as e:
            self._log(f"HTML text extraction failed: {e}", "ERROR", item_id)
            return None


class ClaudeProcessor:
    """Handles Claude API interactions"""
    
    def __init__(self, claude_delay: float = 3.0, max_claude_calls: int = 2, prompts: Dict[str, str] = None, logger=None):
        self.claude_delay = claude_delay
        self.claude_semaphore = asyncio.Semaphore(max_claude_calls)
        self.prompts = prompts or {"claude_analysis": "Analyze this regulatory circular and generate markdown content with YAML frontmatter."}
        self.logger = logger or print  # Fallback to print if no logger provided
    
    def _log(self, message: str, level: str = "INFO", item_id: str = None):
        """Helper method for consistent logging"""
        if item_id and callable(self.logger):
            self.logger(message, level, item_id)
        else:
            print(message)
    
    async def run_claude_with_pdf(self, pdf_path: Path, metadata: Dict[str, str], item_id: str = None) -> Optional[str]:
        """Run Claude with PDF file directly using @filepath syntax"""
        # Build metadata string for prompt
        metadata_str = "\\n".join([f"- {k}: {v}" for k, v in metadata.items() if v])
        
        claude_prompt = self.prompts["claude_analysis"].format(
            source=metadata.get("source", "unknown"),
            title=metadata.get("title", "Untitled"),
            pdf_url=metadata.get("pdf_url", ""),
            circular_id=metadata.get("circular_id", ""),
            metadata=metadata_str,
            content="[Content will be read from PDF file]"
        )
        
        # Use @filepath syntax for direct PDF processing
        full_prompt = f"@{pdf_path} {claude_prompt}"
        
        response = await self._run_claude_with_retry(full_prompt, item_id)
        return response.get("result") if response else None
    
    async def run_claude(self, pdf_content: str, metadata: Dict[str, str], item_id: str = None) -> Optional[str]:
        """Run Claude with extracted text content"""
        # Build metadata string for prompt
        metadata_str = "\\n".join([f"- {k}: {v}" for k, v in metadata.items() if v])
        
        claude_prompt = self.prompts["claude_analysis"].format(
            source=metadata.get("source", "unknown"),
            title=metadata.get("title", "Untitled"),
            pdf_url=metadata.get("pdf_url", ""),
            circular_id=metadata.get("circular_id", ""),
            metadata=metadata_str,
            content=pdf_content[:4000]  # Limit content length
        )
        
        response = await self._run_claude_with_retry(claude_prompt, item_id)
        return response.get("result") if response else None
    
    def _sanitize_prompt(self, prompt: str) -> str:
        """Sanitize prompt input to prevent command injection"""
        if not isinstance(prompt, str):
            raise ValueError("Prompt must be a string")
        
        # Length validation
        if len(prompt) > 100000:  # 100KB limit
            raise ValueError("Prompt exceeds maximum length")
        
        # Remove null bytes and control characters
        prompt = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', prompt)
        
        # Basic validation - no shell metacharacters in critical parts
        if any(char in prompt[:200] for char in ['`', '$', '&&', '||', ';']):
            self._log("Potentially dangerous characters detected in prompt start", "WARNING")
        
        return prompt.strip()
    
    async def _run_claude_with_retry(self, prompt: str, item_id: str = None, max_retries: int = 3) -> Optional[Dict]:
        """Run Claude command with retry logic and concurrency control, returns JSON response"""
        # Sanitize input
        try:
            sanitized_prompt = self._sanitize_prompt(prompt)
        except ValueError as e:
            self._log(f"Prompt validation failed: {e}", "ERROR", item_id)
            return None
        
        async with self.claude_semaphore:
            for attempt in range(1, max_retries + 1):
                try:
                    if attempt > 1:
                        await asyncio.sleep(self.claude_delay * (attempt + 1))
                    else:
                        await asyncio.sleep(self.claude_delay)
                    
                    self._log(f"Running Claude (attempt {attempt}/{max_retries})", "INFO", item_id)
                    
                    # Use list format to prevent shell injection
                    cmd = [
                        "claude", 
                        "-p", sanitized_prompt,
                        "--output-format", "json",
                        "--allowedTools", "Read"
                    ]
                    
                    result = subprocess.run(
                        cmd,
                        capture_output=True,
                        text=True,
                        timeout=120,
                        check=False  # Don't raise on non-zero exit
                    )
                    
                    if result.returncode == 0 and result.stdout.strip():
                        try:
                            response_data = json.loads(result.stdout.strip())
                            if response_data.get("type") == "result" and not response_data.get("is_error", False):
                                content = response_data.get("result", "")
                                self._log(f"Successfully generated content ({len(content)} chars)", "INFO", item_id)
                                return response_data
                            else:
                                self._log(f"Claude returned error response: {response_data.get('result', 'Unknown error')}", "ERROR", item_id)
                        except json.JSONDecodeError as e:
                            self._log(f"Failed to parse Claude JSON response: {e}", "ERROR", item_id)
                    else:
                        self._log(f"Claude attempt {attempt} failed: {result.stderr}", "ERROR", item_id)
                        
                except subprocess.TimeoutExpired:
                    self._log(f"Claude attempt {attempt} timed out", "ERROR", item_id)
                except Exception as e:
                    self._log(f"Claude attempt {attempt} error: {e}", "ERROR", item_id)
                    
            self._log(f"All Claude attempts failed after {max_retries} tries", "ERROR", item_id)
            return None