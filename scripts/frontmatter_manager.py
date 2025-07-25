"""Content-based state management using markdown frontmatter."""

import hashlib
import os
import re
import tempfile
import threading
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import frontmatter
import yaml


class FrontmatterManager:
    """Manages processing state using markdown frontmatter"""
    
    def __init__(self, content_dir: Path, logger=None):
        self.content_dir = Path(content_dir)
        self.content_dir.mkdir(parents=True, exist_ok=True)
        self.logger = logger or print
        
        # Thread-safe file operations
        self._file_locks = {}
        self._locks_lock = threading.Lock()
    
    def _log(self, message: str, level: str = "INFO", item_id: str = None):
        """Helper method for consistent logging"""
        if item_id and callable(self.logger):
            self.logger(message, level, item_id)
        else:
            print(message)
    
    def _get_file_lock(self, file_path: Path) -> threading.Lock:
        """Get or create a lock for a specific file path"""
        str_path = str(file_path.resolve())
        with self._locks_lock:
            if str_path not in self._file_locks:
                self._file_locks[str_path] = threading.Lock()
            return self._file_locks[str_path]
    
    def _atomic_write(self, file_path: Path, content: str) -> bool:
        """Atomically write content to file using temporary file"""
        try:
            # Ensure parent directory exists
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Write to temporary file first
            with tempfile.NamedTemporaryFile(
                mode='w', 
                encoding='utf-8', 
                dir=file_path.parent,
                prefix=f".{file_path.name}.",
                suffix=".tmp",
                delete=False
            ) as tmp_file:
                tmp_file.write(content)
                tmp_path = Path(tmp_file.name)
            
            # Atomic move to final location
            tmp_path.replace(file_path)
            return True
            
        except Exception as e:
            self._log(f"Atomic write failed for {file_path}: {e}", "ERROR")
            # Clean up temp file if it exists
            if 'tmp_path' in locals() and tmp_path.exists():
                try:
                    tmp_path.unlink()
                except:
                    pass
            return False
    
    def read_content_file(self, file_path: Path) -> Optional[frontmatter.Post]:
        """Read markdown file with frontmatter"""
        try:
            if not file_path.exists():
                return None
            
            with open(file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            return post
        except Exception as e:
            self._log(f"Error reading content file {file_path}: {e}", "ERROR")
            return None
    
    def write_content_file(self, file_path: Path, content: str, metadata: Dict, processing_state: Dict = None) -> bool:
        """Write markdown file with frontmatter and processing state using atomic operations"""
        file_lock = self._get_file_lock(file_path)
        
        with file_lock:
            try:
                # Check if content already has frontmatter (from Claude)
                if content.strip().startswith('---'):
                    # Parse existing frontmatter from Claude's output
                    post = frontmatter.loads(content)
                    self._log(f"Parsed existing frontmatter from Claude output", "DEBUG")
                else:
                    # Create new post with content (no frontmatter from Claude)
                    post = frontmatter.Post(content)
                    self._log(f"Created new post from content without frontmatter", "DEBUG")
                
                # Add/update pipeline metadata (don't overwrite Claude's metadata)
                pipeline_metadata = {
                    'circular_id': metadata.get('circular_id'),
                    'source': metadata.get('source'),
                    'published_date': metadata.get('published_date'),
                    'pdf_url': metadata.get('pdf_url'),
                    'rss_url': metadata.get('rss_url'),  # Original RSS URL
                    'guid': metadata.get('guid')
                }
                
                # Only add pipeline metadata if not already present from Claude
                for key, value in pipeline_metadata.items():
                    if key not in post.metadata and value is not None:
                        post.metadata[key] = value
                
                # Always add processing state
                if processing_state:
                    post.metadata['processing'] = processing_state
                
                # Use atomic write
                final_content = frontmatter.dumps(post)
                success = self._atomic_write(file_path, final_content)
                
                if success:
                    self._log(f"Successfully wrote content file: {file_path}", "INFO")
                    return True
                else:
                    self._log(f"Atomic write failed for: {file_path}", "ERROR")
                    return False
                    
            except Exception as e:
                self._log(f"Error writing content file {file_path}: {e}", "ERROR")
                return False
    
    def create_processing_state(self, status: str = "draft", stage: str = "discovered", 
                              processor_version: str = "2.0", content_hash: str = None) -> Dict:
        """Create processing state metadata"""
        return {
            "status": status,
            "stage": stage,
            "processed_at": datetime.now().isoformat(),
            "processor_version": processor_version,
            "content_hash": content_hash or "",
            "attempts": 1
        }
    
    def update_processing_state(self, file_path: Path, updates: Dict) -> bool:
        """Update processing state in existing file"""
        try:
            post = self.read_content_file(file_path)
            if not post:
                return False
            
            # Update processing state
            processing = post.metadata.get('processing', {})
            processing.update(updates)
            processing['last_updated'] = datetime.now().isoformat()
            post.metadata['processing'] = processing
            
            # Write updated file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(frontmatter.dumps(post))
            
            return True
            
        except Exception as e:
            self._log(f"Error updating processing state for {file_path}: {e}", "ERROR")
            return False
    
    def get_content_hash(self, content: str) -> str:
        """Generate SHA256 hash of content"""
        return hashlib.sha256(content.encode('utf-8')).hexdigest()[:16]
    
    def find_files_by_status(self, status: str) -> List[Path]:
        """Find all content files with specific processing status"""
        matching_files = []
        
        for file_path in self.content_dir.rglob("*.md"):
            post = self.read_content_file(file_path)
            if post and post.metadata.get('processing', {}).get('status') == status:
                matching_files.append(file_path)
        
        return matching_files
    
    def find_files_by_circular_id(self, circular_id: str) -> List[Path]:
        """Find content files by circular_id"""
        matching_files = []
        
        for file_path in self.content_dir.rglob("*.md"):
            post = self.read_content_file(file_path)
            if post and post.metadata.get('circular_id') == circular_id:
                matching_files.append(file_path)
        
        return matching_files
    
    def is_processed(self, circular_id: str, source: str = None) -> bool:
        """Check if circular has already been processed"""
        for file_path in self.content_dir.rglob("*.md"):
            post = self.read_content_file(file_path)
            if post and post.metadata.get('circular_id') == circular_id:
                if source and post.metadata.get('source') != source:
                    continue
                processing_status = post.metadata.get('processing', {}).get('status', '')
                return processing_status in ['published', 'completed']
        
        return False
    
    def write_state_file(self, file_path: Path, metadata: Dict, stage: str, status: str = "processing") -> bool:
        """Write a state-only file during intermediate processing stages"""
        file_lock = self._get_file_lock(file_path)
        
        with file_lock:
            try:
                # Create minimal content for state tracking
                post = frontmatter.Post("Processing in progress...")
                
                # Add metadata
                post.metadata.update(metadata)
                
                # Add processing state
                processing_state = self.create_processing_state(
                    status=status,
                    stage=stage,
                    content_hash=None  # No content hash for state-only files
                )
                post.metadata['processing'] = processing_state
                
                # Use atomic write
                final_content = frontmatter.dumps(post)
                success = self._atomic_write(file_path, final_content)
                
                if success:
                    self._log(f"Wrote state file at stage '{stage}': {file_path.name}", "DEBUG")
                    return True
                else:
                    self._log(f"Failed to write state file: {file_path}", "ERROR")
                    return False
                    
            except Exception as e:
                self._log(f"Error writing state file {file_path}: {e}", "ERROR")
                return False
    
    def get_processing_stats(self) -> Dict:
        """Get processing statistics from content files"""
        stats = {
            'total': 0,
            'published': 0,
            'draft': 0,
            'failed': 0,
            'processing': 0,
            'by_source': {}
        }
        
        for file_path in self.content_dir.rglob("*.md"):
            post = self.read_content_file(file_path)
            if not post:
                continue
                
            stats['total'] += 1
            
            # Count by status
            status = post.metadata.get('processing', {}).get('status', 'unknown')
            if status in stats:
                stats[status] += 1
            
            # Count by source
            source = post.metadata.get('source', 'unknown')
            if source not in stats['by_source']:
                stats['by_source'][source] = 0
            stats['by_source'][source] += 1
        
        return stats
    
    def clean_filename(self, text: str, max_length: int = 80) -> str:
        """Clean text for use in filename"""
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', '', text)
        # Replace special characters with hyphens
        text = re.sub(r'[^\w\s-]', '', text)
        # Replace whitespace with hyphens
        text = re.sub(r'[-\s]+', '-', text)
        # Remove leading/trailing hyphens
        text = text.strip('-').lower()
        # Truncate to max length
        return text[:max_length]
    
    def generate_content_path(self, source: str, date: str, circular_id: str, title: str = "") -> Path:
        """Generate content file path with input validation"""
        # Input validation
        if not source or not isinstance(source, str):
            raise ValueError("Source must be a non-empty string")
        if not date or not isinstance(date, str):
            raise ValueError("Date must be a non-empty string")
        if not circular_id or not isinstance(circular_id, str):
            raise ValueError("Circular ID must be a non-empty string")
        
        # Validate source against allowed values
        allowed_sources = ["nse", "bse", "sebi"]
        if source not in allowed_sources:
            raise ValueError(f"Source must be one of: {allowed_sources}")
        
        # Validate circular_id format (hexadecimal, max 16 chars)
        if not re.match(r'^[a-f0-9]{1,16}$', circular_id):
            raise ValueError("Circular ID must be hexadecimal string, max 16 characters")
        
        # Extract year from date
        try:
            year = datetime.fromisoformat(date.replace('Z', '+00:00')).year
            if year < 2000 or year > 2100:  # Reasonable year range
                raise ValueError(f"Year {year} is outside valid range")
        except Exception as e:
            raise ValueError(f"Invalid date format: {date} - {e}")
        
        # Clean and validate title for filename
        cleaned_title = ""
        if title:
            cleaned_title = self.clean_filename(title)
            if len(cleaned_title) > 100:  # Limit filename length
                cleaned_title = cleaned_title[:100]
        
        # Construct filename with length limits
        if cleaned_title:
            filename = f"{source}-{date[:10]}-{circular_id}-{cleaned_title}.md"
        else:
            filename = f"{source}-{date[:10]}-{circular_id}.md"
        
        # Final filename length check
        if len(filename) > 255:  # Filesystem limit
            self._log(f"Filename too long, truncating: {filename}", "WARNING")
            filename = filename[:251] + ".md"
        
        # Ensure path is within content directory (prevent path traversal)
        content_path = self.content_dir / source / str(year) / filename
        if not str(content_path.resolve()).startswith(str(self.content_dir.resolve())):
            raise ValueError("Generated path is outside content directory")
        
        return content_path
    
    def parse_frontmatter(self, file_path: Path) -> Optional[Dict]:
        """Parse YAML frontmatter from markdown file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if file starts with frontmatter
            if not content.startswith('---'):
                return None
            
            # Find end of frontmatter
            end_marker = content.find('---', 3)
            if end_marker == -1:
                return None
            
            # Extract and parse YAML
            frontmatter_content = content[3:end_marker].strip()
            return yaml.safe_load(frontmatter_content)
            
        except Exception as e:
            self._log(f"Failed to parse frontmatter from {file_path}: {e}", "ERROR")
            return None