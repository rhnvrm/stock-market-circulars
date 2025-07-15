# Hugo Static Site Generator Research

## Hugo Overview

Hugo is a fast, modern static site generator written in Go, ideal for building content-heavy sites with complex taxonomies and filtering requirements.

## Key Findings for Our Use Case

### Site Initialization
```bash
hugo new site circulars-site
cd circulars-site
hugo new theme zerodha-theme
```

### Content Organization Strategy
```
content/circulars/
├── nse/
│   └── 2025/
│       └── _index.md          # NSE 2025 section page
│       └── circular-name.md   # Individual circulars
├── bse/
└── sebi/
```

### Taxonomy Configuration
```yaml
# config.yaml
taxonomies:
  source: sources      # nse, bse, sebi
  tag: tags           # severity, impact, categories
  severity: severities # high, medium, low
  impact: impacts     # high, medium, low
  category: categories # trading, listing, compliance
  stock: stocks       # individual stock tickers
```

## Theme Structure for Zerodha Design

### Layout Hierarchy
```
themes/zerodha/
├── layouts/
│   ├── _default/
│   │   ├── baseof.html     # Base template
│   │   ├── single.html     # Individual circular
│   │   └── list.html       # Circular listings
│   ├── partials/
│   │   ├── header.html
│   │   ├── footer.html
│   │   ├── circular-card.html
│   │   └── filters.html
│   └── index.html          # Homepage
├── static/
│   ├── css/
│   ├── js/
│   └── pdfs/              # PDF files
└── assets/                # Source assets for processing
```

### Template Variables for Circulars
```go-html-template
{{ .Title }}                    # Circular title
{{ .Date }}                     # Publication date
{{ .Params.source }}            # nse/bse/sebi
{{ .Params.circular_id }}       # Unique identifier
{{ .Params.pdf_url }}           # PDF file path
{{ .Params.severity }}          # high/medium/low
{{ .Params.impact }}            # high/medium/low
{{ .Params.importance_ranking }} # Overall importance
{{ .Params.justification }}     # Ranking explanation
```

## Content Processing Pipeline

### Frontmatter Schema
```yaml
---
title: "Trading Halt for XYZ Company"
description: "Trading suspended due to regulatory review"
date: 2025-07-15T14:30:00Z
source: "nse"
circular_id: "NSE/INSP/45123/2025"
pdf_url: "/pdfs/nse_20250715_trading_halt_xyz.pdf"
tags:
  - trading
  - suspension
  - regulatory
severity: "high"
impact: "medium"
stocks:
  - "XYZ"
importance_ranking: "high"
impact_ranking: "medium"
justification: "Trading suspension affects immediate liquidity"
---
```

### Automated Content Generation
- Use Hugo's `hugo new` command with archetypes
- Custom archetype for circular content type
- Pre-populated frontmatter templates

## Filtering and Search Implementation

### Taxonomy Pages
- Automatic generation of tag/category pages
- Custom list templates for each taxonomy
- Cross-referencing between taxonomies

### JavaScript Integration
- Alpine.js for client-side filtering
- JSON data generation for search indices
- Real-time filtering without page reloads

### Hugo's Built-in Features
```go-html-template
<!-- Filter by source -->
{{ range .Site.Taxonomies.sources }}
  <a href="{{ .Page.Permalink }}">{{ .Page.Title }}</a>
{{ end }}

<!-- Filter by severity -->
{{ range .Site.Taxonomies.severities }}
  <button data-severity="{{ .Page.Title }}">{{ .Page.Title }}</button>
{{ end }}
```

## PDF Handling Strategy

### Static File Management
- Store PDFs in `static/pdfs/` directory
- Maintain original filename structure
- Hugo copies static files without processing

### PDF Embedding Options
1. **Inline Embedding**: Use `<embed>` or `<iframe>` tags
2. **Modal Viewers**: JavaScript-based PDF viewers
3. **External Links**: Link to PDF files directly

### Example PDF Integration
```go-html-template
{{ if .Params.pdf_url }}
  <div class="pdf-viewer">
    <embed src="{{ .Params.pdf_url }}" type="application/pdf" width="100%" height="600px">
    <p><a href="{{ .Params.pdf_url }}" target="_blank">Download PDF</a></p>
  </div>
{{ end }}
```

## Performance Optimization

### Build Optimization
- Use Hugo's built-in minification
- Optimize images and assets
- Enable gzip compression
- Leverage browser caching

### Content Organization
- Paginated listings for large datasets
- Lazy loading for PDF embeds
- Efficient taxonomy querying

## Development Workflow

### Local Development
```bash
hugo server --watch --buildDrafts
```

### Build Process
```bash
hugo --minify --gc
```

### Deployment Considerations
- Static file hosting (Netlify, Vercel, GitHub Pages)
- CDN integration for PDF files
- Automated builds on content updates

## Integration with AI Pipeline

### Content Generation Flow
1. AI processing generates markdown files
2. Files placed in appropriate content directories
3. Hugo rebuilds site automatically
4. New content appears in filtered views

### Metadata Synchronization
- Ensure AI-generated frontmatter matches Hugo schema
- Validate required fields before site build
- Error handling for malformed content

## Future Enhancements

### Advanced Features
- Full-text search with lunr.js
- Real-time content updates
- Analytics integration
- Comment system for circulars
- Email subscription management

### Performance Scaling
- Incremental builds for large content volumes
- Content delivery network integration
- Database backend for complex queries
- API endpoints for external integrations

---

**Research Date**: 2025-07-15  
**Implementation Status**: 📋 Planned  
**Next Steps**: Theme development and content structure setup