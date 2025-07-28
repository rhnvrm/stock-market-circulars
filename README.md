# Stock Market Circulars Processing Pipeline

A modern Python-based system for automatically collecting, processing, and displaying regulatory circulars from NSE, BSE, and SEBI. Features Claude AI content generation, 100% semantic CSS architecture, and content-based state management for reliable processing and deployment.

## Quick Start

```bash
# Setup environment (Nix + direnv)
direnv allow

# Run complete pipeline
just pipeline

# Start development server
just serve
```

## Architecture

- **Unified Python Pipeline** (`scripts/combined_pipeline.py` - uv script format)
- **Claude AI Integration** (JSON output format for GitHub Actions compatibility)
- **Content-Based State Management** (markdown frontmatter instead of JSON files)
- **Hugo Static Site** with 100% semantic CSS architecture and Zerodha design system
- **Multi-Format Support** (PDF, ZIP archives, HTML fallback for BSE)

## Key Features

- **RSS Feed Processing**: Automated scraping from NSE, BSE, SEBI with intelligent PDF extraction
- **AI Content Generation**: Claude processes PDFs/HTML to generate structured markdown with YAML frontmatter
- **Hugo Site Generation**: Professional static site with 100% semantic CSS, filtering, search, and responsive design
- **Content-Based State**: Frontmatter-based state management with complete audit trails
- **Multi-Format Support**: PDF files, ZIP archives, and HTML fallback (BSE 404 handling)
- **Resume Functionality**: Automatically detects and skips completed items across runs
- **Content Regeneration**: Fix specific items with updated prompts without full pipeline re-run

## RSS Data Sources

| Source | Format | Method | Fallback |
|--------|--------|--------|----------|
| NSE | RSS 2.0 | Direct PDF/ZIP links | N/A |
| BSE | RSS 2.0 | HTML page extraction | HTML scraping on 404 |
| SEBI | RSS 2.0 | HTML page extraction with iframe detection | N/A |

## Commands

### Core Workflow
```bash
just pipeline        # Run RSS scraping and AI processing (all sources)
just regenerate <id> # Regenerate specific items with updated prompts

# Direct script usage (advanced)
uv run --script scripts/combined_pipeline.py main           # All sources
uv run --script scripts/combined_pipeline.py main nse bse  # Specific sources
uv run --script scripts/combined_pipeline.py main --debug  # Debug mode
```

### Development
```bash
just serve           # Start Hugo development server
just build           # Build static site for production
```

### Utilities
```bash
just deps            # Check dependencies and system status
just stats           # Show processing statistics
just logs            # View recent pipeline logs
just clean-state     # Reset pipeline state for fresh run
just validate        # Validate RSS feeds are accessible (CI/CD)
```

## Project Structure

```
├── flake.nix              # Modern Nix development environment
├── justfile               # Streamlined command runner
├── scripts/
│   ├── combined_pipeline.py # Main pipeline script (uv format)
│   ├── cli.py              # Command-line interface with regenerate support
│   ├── pipeline.py         # Core pipeline orchestration
│   ├── processors.py       # Claude integration, file processing, and HTML extraction
│   ├── extractors.py       # RSS parsing and PDF URL extraction
│   ├── frontmatter_manager.py # Content-based state management
│   ├── models.py           # Data models (simplified)
│   └── config.py           # Configuration loading
├── config/
│   └── config.toml         # Unified configuration (RSS feeds, prompts, settings)
├── hugo-site/             # Hugo static site with Zerodha design
├── combined_pipeline.log  # Pipeline execution logs
└── state/                 # Legacy state directory (unused)
```

## Development Environment

### Requirements
- **Nix** with flakes enabled
- **direnv** for automatic environment activation

### Setup
```bash
git clone <repo>
cd stock-market-circulars
direnv allow  # Automatically installs Python + uv + Claude Code + Hugo
```

### Dependencies (managed by uv)
- `rich` - CLI interface and progress display
- `typer` - Command-line argument parsing  
- `pydantic` - Data models and validation
- `httpx` - HTTP client for RSS/PDF downloading
- `lxml` - XML/HTML parsing
- `markitdown[pdf]` - PDF text extraction
- `tomli` - TOML configuration parsing

### External Tools
- `claude` CLI - AI content generation (auto-installed via npm)
- `hugo` - Static site generation

## Configuration

All configuration is centralized in `config/config.toml`:
- RSS feed URLs and processing settings
- Claude AI prompts for Hugo-compatible output
- Retry logic and concurrency limits
- Output formatting and directory structure

## Content Generation

### Frontmatter Schema
```yaml
---
title: "Clear descriptive title"
description: "Brief 1-2 sentence summary"
date: 2025-07-25
source: nse
circular_id: "16-character-hash"
pdf_url: "https://example.com/circular.pdf"
tags:
  - relevant-tag-1
  - stock-ticker-if-mentioned
severity: "high/medium/low"
impact: "high/medium/low"
category: "trading/listing/compliance/disclosure/market-operations"
stocks: ["TICKER1", "TICKER2"]
importance_ranking: "high/medium/low"
impact_ranking: "high/medium/low"
justification: "Brief reasoning for rankings"
---
```

### File Organization
```
hugo-site/content/circulars/
├── nse/2025/nse-2025-07-25-[16-char-id]-[title-slug].md
├── bse/2025/bse-2025-07-25-[16-char-id]-[title-slug].md
└── sebi/2025/sebi-2025-07-25-[16-char-id]-[title-slug].md
```

## Design System

Professional, responsive web interface built with Zerodha-inspired design:

- **Clean Interface**: Minimalist design focused on content readability
- **Fast Performance**: Lightweight CSS with no external framework dependencies  
- **Mobile-First**: Responsive design that works on all devices
- **Accessibility**: Proper semantic markup and keyboard navigation
- **Search & Filtering**: Advanced filtering by source, severity, tags, and content search
- **Professional Aesthetics**: Zerodha's signature blue (`#387ed1`) with Inter typography

## License

[Your License Here]