"""Data models for the stock market circulars pipeline."""

from datetime import timedelta
from typing import Dict, List

from pydantic import BaseModel


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
    success_rate: float
    source_results: Dict[str, SourceStats]
    elapsed_time: timedelta