#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "rich",
#     "typer", 
#     "pydantic",
#     "httpx",
#     "lxml",
#     "beautifulsoup4",
#     "markitdown[pdf,docx,xlsx,xls]",
#     "tomli",
#     "python-frontmatter",
# ]
# ///

"""
Stock Market Circulars Pipeline - Modular Version

This is the main entry point for the refactored pipeline.
The functionality has been split into multiple modules:

- models.py: Data models and enums
- config.py: Configuration handling  
- extractors.py: RSS parsing and PDF URL extraction
- processors.py: File processing and Claude integration
- pipeline.py: Main pipeline orchestration
- cli.py: Command-line interface

Usage:
    uv run scripts/combined_pipeline.py nse bse sebi
    uv run scripts/combined_pipeline.py bse --max-items 5 --debug
"""

if __name__ == "__main__":
    from cli import app
    app()