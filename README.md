# Stock Market Circulars Processing Pipeline

A modern Python-based system for automatically collecting, processing, and displaying regulatory circulars from NSE, BSE, and SEBI. Uses Claude AI to generate Hugo-compatible markdown with proper frontmatter and structured content.

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
- **Claude AI Integration** (text extraction + content generation with Hugo-compatible output)
- **Hugo Static Site** with Zerodha-inspired design
- **State Management** with retry logic and progress tracking

## Key Features

- **RSS Feed Processing**: Automated scraping from NSE, BSE, SEBI with intelligent PDF extraction
- **AI Content Generation**: Claude processes PDFs to generate structured markdown with YAML frontmatter
- **Hugo Site Generation**: Professional static site with filtering, search, and responsive design
- **Retry Logic**: 3-attempt system with state preservation for reliable processing
- **Content Regeneration**: Fix specific items with updated prompts without full pipeline re-run

## RSS Data Sources

| Source | Format | Method |
|--------|--------|--------|
| NSE | RSS 2.0 | Direct PDF links |
| BSE | RSS 2.0 | HTML page extraction |
| SEBI | RSS 2.0 | HTML page extraction with iframe detection |

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
│   ├── processors.py       # Claude integration and file processing
│   ├── extractors.py       # RSS parsing and PDF URL extraction
│   ├── models.py           # Data models and enums
│   └── config.py           # Configuration loading
├── config/
│   └── config.toml         # Unified configuration (RSS feeds, prompts, settings)
├── hugo-site/             # Hugo static site with Zerodha design
└── state/                 # Processing state files and logs
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

Built with Zerodha-inspired design language:
- **Primary Blue**: `#387ed1`
- **Typography**: Inter, system-ui, sans-serif
- **Framework**: Hugo + Alpine.js + DaisyUI
- **Features**: Source filtering, tag-based filtering, search, responsive design

## License

[Your License Here]