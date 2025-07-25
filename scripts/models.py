"""Data models and enums for the stock market circulars pipeline."""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class PipelineStage(Enum):
    """Pipeline stages for tracking progress"""
    STARTED = "started"
    PDF_URL_EXTRACTED = "pdf_url_extracted"
    PDF_DOWNLOADED = "pdf_downloaded"
    TEXT_EXTRACTED = "text_extracted"
    MARKDOWN_GENERATED = "markdown_generated"
    COMPLETED = "completed"


class ItemProgress(BaseModel):
    """Progress tracking for individual items"""
    item_id: str
    source: str
    guid: str
    title: str
    link: str
    stage: PipelineStage
    started_at: datetime
    last_updated: datetime
    attempts: int = 1
    metadata: Dict[str, str] = {}
    stages: Dict[str, datetime] = {}
    error_message: Optional[str] = None


class SourceStats(BaseModel):
    """Statistics for a source"""
    source: str
    total_items: int
    processed_items: int
    completed_items: int
    failed_items: int
    success_rate: float
    errors: List[str] = []


class PipelineStats(BaseModel):
    """Overall pipeline statistics"""
    total_sources: int
    total_items: int
    processed_items: int
    completed_items: int
    failed_items: int
    overall_success_rate: float
    sources: List[SourceStats]
    processing_time: float