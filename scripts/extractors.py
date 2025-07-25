"""RSS feed parsing and PDF URL extraction."""

import asyncio
import re
from typing import Dict, List, Optional
from urllib.parse import urljoin

import httpx
from lxml import etree, html


class RSSExtractor:
    """Handles RSS feed downloading and parsing"""
    
    def __init__(self, timeout: int = 30, retry_delays: List[int] = None):
        self.timeout = timeout
        self.retry_delays = retry_delays or [5, 15, 30]
    
    async def download_rss_feed(self, source: str, url: str) -> Optional[str]:
        """Download RSS feed with validation"""
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        
        print(f"Downloading RSS feed for {source}: {url}")
        content = await self._fetch_with_retry(url, headers)
        
        if content:
            try:
                etree.fromstring(content.encode())  # Validate XML
                print(f"Successfully downloaded and validated RSS for {source}")
                return content
            except Exception as e:
                print(f"RSS validation failed for {source}: {e}")
                return None
        return None
    
    async def _fetch_with_retry(self, url: str, headers: Dict[str, str]) -> Optional[str]:
        """Generic HTTP fetch with retry logic and exponential backoff"""
        last_error = None
        
        for attempt in range(len(self.retry_delays) + 1):  # +1 for initial attempt
            try:
                async with httpx.AsyncClient(timeout=self.timeout) as client:
                    print(f"HTTP fetch attempt {attempt + 1}/{len(self.retry_delays) + 1} for {url}")
                    response = await client.get(url, headers=headers)
                    response.raise_for_status()
                    return response.text
                    
            except Exception as e:
                last_error = e
                print(f"HTTP fetch attempt {attempt + 1} failed for {url}: {e}")
                
                # If this isn't the last attempt, wait before retrying
                if attempt < len(self.retry_delays):
                    delay = self.retry_delays[attempt]
                    print(f"Retrying in {delay} seconds...")
                    await asyncio.sleep(delay)
                else:
                    print(f"All retry attempts exhausted for {url}")
        
        print(f"HTTP fetch failed after all retries for {url}: {last_error}")
        return None
    
    def parse_rss_feed(self, content: str, source: str) -> List[Dict[str, str]]:
        """Parse RSS feed content and extract items"""
        try:
            root = etree.fromstring(content.encode())
            items = []
            
            for item in root.xpath('.//item'):
                title_elem = item.find('title')
                link_elem = item.find('link')
                guid_elem = item.find('guid')
                pubdate_elem = item.find('pubDate')
                
                if title_elem is not None and link_elem is not None:
                    download_url = link_elem.text.strip()
                    
                    # Fix SEBI URL duplication bug
                    if source == "sebi" and "https://www.sebi.gov.in/https://www.sebi.gov.in/" in download_url:
                        download_url = download_url.replace('https://www.sebi.gov.in/https://www.sebi.gov.in/', 'https://www.sebi.gov.in/')
                    
                    items.append({
                        'title': title_elem.text.strip() if title_elem.text else 'Untitled',
                        'download_url': download_url,
                        'guid': guid_elem.text.strip() if guid_elem is not None and guid_elem.text else download_url,
                        'pubdate': pubdate_elem.text.strip() if pubdate_elem is not None and pubdate_elem.text else ''
                    })
            
            print(f"Parsed {len(items)} items from RSS feed")
            return items
            
        except Exception as e:
            print(f"Failed to parse RSS for {source}: {e}")
            return []


class PDFURLExtractor:
    """Extracts PDF URLs from HTML pages"""
    
    def __init__(self, timeout: int = 30):
        self.timeout = timeout
    
    async def extract_pdf_url(self, source: str, url: str) -> Optional[str]:
        """Extract PDF URL from HTML page based on source type"""
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(url, headers=headers)
                response.raise_for_status()
                content = response.text
                
                doc = html.fromstring(content)
                
                if source == "nse":
                    return self._extract_nse_pdf_url(doc)
                elif source == "bse":
                    return self._extract_bse_pdf_url(doc, url)
                elif source == "sebi":
                    return self._extract_sebi_pdf_url(doc)
                
        except Exception as e:
            print(f"Failed to extract PDF URL from {url}: {e}")
            return None
        
        return None
    
    def _extract_nse_pdf_url(self, doc) -> Optional[str]:
        """Extract NSE PDF URL from HTML document"""
        for element in doc.xpath('.//a[contains(@href, ".pdf")]'):
            href = element.get('href')
            if href:
                return urljoin("https://nsearchives.nseindia.com/", href)
        return None
    
    def _extract_bse_pdf_url(self, doc, original_url: str = None) -> Optional[str]:
        """Extract BSE PDF URL from HTML document with fallback for empty attachedId"""
        for element in doc.xpath('.//a[contains(@href, "DownloadAttach.aspx")]'):
            href = element.get('href')
            if href:
                full_url = urljoin("https://www.bseindia.com/markets/MarketInfo/", href)
                
                # Check if attachedId is empty and try to fix it
                if 'attachedId=' in full_url and full_url.endswith('attachedId='):
                    if original_url and 'Noticeid=' in original_url:
                        # Extract Noticeid GUID from original URL
                        try:
                            notice_match = re.search(r'Noticeid=\\{([^}]+)\\}', original_url)
                            if notice_match:
                                notice_guid = notice_match.group(1)
                                # Replace empty attachedId with notice GUID
                                full_url = full_url.replace('attachedId=', f'attachedId={notice_guid}')
                                print(f"Fixed BSE URL with Noticeid GUID: {full_url}")
                        except Exception as e:
                            print(f"Error extracting Noticeid from URL: {e}")
                
                return full_url
        return None
    
    def _extract_sebi_pdf_url(self, doc) -> Optional[str]:
        """Extract SEBI PDF URL from HTML document"""
        # Check for iframe embedded PDFs first
        for element in doc.xpath('.//iframe[contains(@src, "attachdocs")]'):
            src = element.get('src')
            if src and 'file=' in src:
                # Extract file parameter from iframe src
                try:
                    file_param = src.split('file=')[1].split('&')[0]
                    if file_param:
                        return urljoin("https://www.sebi.gov.in/", file_param)
                except Exception:
                    continue
        
        # Fallback to direct PDF links
        for element in doc.xpath('.//a[contains(@href, ".pdf")]'):
            href = element.get('href')
            if href:
                return urljoin("https://www.sebi.gov.in/", href)
        return None


class ContentScraper:
    """Scrapes content from web pages when no PDF is available"""
    
    def __init__(self, timeout: int = 30):
        self.timeout = timeout
    
    async def fetch_content(self, url: str) -> Optional[str]:
        """Generic method to fetch content from any URL"""
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(url, headers=headers)
                response.raise_for_status()
                return response.text
        except Exception as e:
            print(f"Error fetching content from {url}: {e}")
            return None
    
    async def scrape_bse_page_content(self, url: str) -> Optional[str]:
        """Scrape content directly from BSE page when no attachment is available"""
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
            
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(url, headers=headers)
                response.raise_for_status()
                content = response.text
            
            if not content:
                return None
            
            # Parse HTML and extract meaningful content
            doc = html.fromstring(content)
            
            # Look for main content areas in BSE pages
            content_selectors = [
                './/div[contains(@class, "content")]//text()',
                './/div[contains(@class, "notice")]//text()',
                './/div[contains(@class, "circular")]//text()',
                './/table//text()',
                './/p//text()',
                './/div//text()'
            ]
            
            extracted_text = []
            for selector in content_selectors:
                texts = doc.xpath(selector)
                for text in texts:
                    text = text.strip()
                    if len(text) > 10 and not text.startswith('(') and 'javascript' not in text.lower():
                        extracted_text.append(text)
                
                # If we found substantial content, break
                if len(' '.join(extracted_text)) > 500:
                    break
            
            result = ' '.join(extracted_text).strip()
            
            # Clean up the text
            result = ' '.join(result.split())  # Normalize whitespace
            
            if len(result) < 100:
                print(f"BSE page content too short ({len(result)} chars), might not be a content page")
                return None
                
            return result
            
        except Exception as e:
            print(f"Error scraping BSE page content: {e}")
            return None