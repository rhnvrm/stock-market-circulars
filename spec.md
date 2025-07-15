# Stock Market Circulars Static Site - Technical Specification

## Project Overview

A static site system for automatically collecting, processing, and displaying regulatory circulars from NSE, BSE, and SEBI. The system uses AI-powered processing to generate summaries, tags, and structured content for easy browsing and filtering.

## Architecture

### Core Components

1. **RSS Feed Scraper** (`scripts/fetch-circulars.sh`)
2. **AI Processing Pipeline** (`scripts/process-all.sh`)
3. **Hugo Static Site Generator** (`hugo-site/`)
4. **Interactive Frontend** (Alpine.js + DaisyUI)

### Data Flow

```
RSS Feeds → Download PDFs → AI Processing → Markdown Generation → Hugo Build → Static Site
```

## RSS Data Sources

| Source | URL | Format |
|--------|-----|--------|
| NSE | `https://nsearchives.nseindia.com/content/RSS/Circulars.xml` | RSS 2.0 |
| BSE | `https://www.bseindia.com/rss/bsecirculars.xml` | RSS 2.0 |
| SEBI | `https://www.sebi.gov.in/sebirss.xml` | RSS 2.0 |

## AI Processing Pipeline

### Stage 1: Summary Extraction (Gemini)
```bash
gemini -p "@path/to/circular.pdf Extract a comprehensive summary of this regulatory circular including key points, regulatory changes, deadlines, and impact"
```

### Stage 2: Structured Content Generation (Claude)
```bash
claude -p "Based on this summary: [gemini output], generate frontmatter with title, description, tags (severity: high/medium/low, impact: high/medium/low, stock tickers if mentioned), and create markdown content" --allowedTools "Write"
```

## Content Structure

### File Organization
```
content/circulars/
├── nse/
│   └── 2025/
│       └── 20250715_circular_name.md
├── bse/
│   └── 2025/
│       └── 20250715_circular_name.md
└── sebi/
    └── 2025/
        └── 20250715_circular_name.md
```

### Frontmatter Schema
```yaml
---
title: "Circular Title"
description: "Brief description of the circular"
date: 2025-07-15T10:00:00Z
source: "nse|bse|sebi"
circular_id: "unique_identifier"
pdf_url: "/pdfs/filename.pdf"
tags:
  - severity: "high|medium|low"
  - impact: "high|medium|low"
  - category: "trading|listing|compliance|disclosure"
  - stocks: ["TICKER1", "TICKER2"]  # if applicable
importance_ranking: "high|medium|low"
impact_ranking: "high|medium|low"
justification: "Explanation of ranking"
---
```

## Design System (Zerodha Inspired)

### Color Palette
- Primary Blue: `#387ed1`
- Background: `#ffffff`
- Text: `#424242`
- Light Gray: `#f9f9f9`
- Border: `#e0e0e0`

### Typography
- Font Family: Inter, system-ui, sans-serif
- Base Font Size: 16px
- Headings: H1: 2rem, H2: 1.5rem, H3: 1.25rem

## Features

### Core Features
- [x] RSS feed scraping with duplicate detection
- [x] PDF download and organization
- [ ] AI-powered summary generation
- [ ] Automated tagging and categorization
- [ ] Static site generation with Hugo
- [ ] PDF embedding and viewing

### Interactive Features
- [ ] Source filtering (NSE/BSE/SEBI)
- [ ] Tag-based filtering
- [ ] Search functionality
- [ ] Importance/impact ranking display
- [ ] Responsive design

### Future Enhancements
- [ ] Automated scheduling (cron/systemd)
- [ ] Email notifications for high-importance circulars
- [ ] API endpoint for external integrations
- [ ] Analytics and usage tracking

## Technical Requirements

### Development Environment
- Nix flake with direnv support
- Node.js 20+ for npm packages
- Hugo (via npm initially, migrate to Nix later)

### Dependencies
- `xmlstarlet` - RSS XML parsing
- `curl`/`wget` - File downloading
- `jq` - JSON processing
- `gemini` CLI - AI summary generation
- `claude` CLI - Structured content generation

### Browser Support
- Modern browsers supporting ES6+
- Alpine.js 3.x compatibility
- Tailwind CSS + DaisyUI components

## Security Considerations

- Input validation for RSS feed data
- Safe file downloading with timeout limits
- Sanitization of generated content
- No sensitive data storage
- Read-only static site deployment

## Performance Targets

- RSS processing: < 5 minutes for all feeds
- AI processing: < 2 minutes per circular
- Site build time: < 30 seconds
- Page load time: < 2 seconds
- Mobile responsiveness: 95+ Lighthouse score

## Testing Strategy

- Unit tests for RSS parsing functions
- Integration tests for AI processing pipeline
- End-to-end tests for complete workflow
- Manual testing for UI/UX validation
- Performance benchmarking