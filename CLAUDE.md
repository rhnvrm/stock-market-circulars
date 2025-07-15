# Claude Instructions for Stock Market Circulars Project

## Project Context

This is a static site system for automatically collecting and displaying regulatory circulars from NSE, BSE, and SEBI. The system uses AI processing (Gemini + Claude) to generate summaries and structured content.

## Key Commands and Usage Patterns

### AI Processing Pipeline

#### Gemini for PDF Summary Extraction
```bash
gemini -p "@path/to/circular.pdf Extract a comprehensive summary of this regulatory circular including key points, regulatory changes, deadlines, and impact"
```

#### Claude for Structured Content Generation
```bash
claude -p "Based on this summary: [gemini output], generate frontmatter with title, description, tags (severity: high/medium/low, impact: high/medium/low, stock tickers if mentioned), and create markdown content" --allowedTools "Write"
```

### Project Structure
```
├── flake.nix              # Nix development environment
├── .envrc                 # direnv configuration
├── scripts/
│   ├── fetch-circulars.sh # RSS scraper
│   └── process-all.sh     # AI processing pipeline
├── hugo-site/             # Hugo static site
├── inbox/                 # Downloaded circulars
├── state/                 # Processing state files
└── docs/                  # Research and documentation
```

## Development Workflow

1. **RSS Scraping**: Run `./scripts/fetch-circulars.sh` to download new circulars
2. **AI Processing**: Run `./scripts/process-all.sh` to process downloaded files
3. **Site Generation**: Use Hugo to build static site
4. **Git Workflow**: Regular commits with descriptive messages including prompts used

## Design Guidelines

### Zerodha Design Language
- Primary Blue: #387ed1
- Background: #ffffff  
- Text: #424242
- Light Gray: #f9f9f9
- Border: #e0e0e0
- Font: Inter, system-ui, sans-serif

### Content Structure
- Frontmatter with comprehensive metadata
- Tags for severity, impact, categories, stock tickers
- Importance and impact rankings with justifications
- PDF embedding support

## AI Processing Instructions

When processing circulars with Claude:
1. Generate accurate, concise titles and descriptions
2. Extract relevant stock tickers when mentioned
3. Assign appropriate severity and impact ratings
4. Provide clear justification for rankings
5. Maintain consistent markdown formatting
6. Ensure all frontmatter fields are populated

## Common Patterns

### RSS Feed Sources
- NSE: https://nsearchives.nseindia.com/content/RSS/Circulars.xml
- BSE: https://www.bseindia.com/rss/bsecirculars.xml  
- SEBI: https://www.sebi.gov.in/sebirss.xml

### File Naming Convention
`{source}_{date}_{cleaned_title}.{extension}`

### Processing State
- Track processed GUIDs to avoid duplicates
- Maintain logs for debugging and monitoring
- Store metadata for incremental processing

## Testing and Validation

- Validate RSS XML structure before processing
- Error handling for malformed feeds and failed downloads
- Content validation for generated markdown
- Regular testing of AI processing pipeline

---

**Last Updated**: 2025-07-15  
**Current Focus**: AI processing pipeline implementation