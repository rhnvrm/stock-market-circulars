# Stock Market Circulars - Living Dataset

A living dataset of regulatory circulars from NSE, BSE, and SEBI, continuously updated through automated RSS feed processing and LLM-powered content extraction.

## Data Sources

Regulatory circulars from official RSS feeds:

- **NSE** - Trading circulars, market updates, regulatory changes
- **BSE** - Listing requirements, compliance notices, market rules  
- **SEBI** - Policy changes, investor guidelines, regulatory frameworks

## How the Living Dataset Works

The dataset updates automatically every 3 hours via GitHub Actions:

1. **Scheduled Execution** - GitHub Actions runs `update-circulars.yml` every 3 hours (or on manual trigger)
2. **Environment Setup** - Nix development environment provides Python, uv, Claude CLI, and Go
3. **Pipeline Execution** - `just pipeline` command runs the complete RSS monitoring and processing pipeline
4. **Content Processing** - Python scripts download PDFs, extract text, and use Claude AI for analysis
5. **Dataset Updates** - New circulars are committed as structured markdown files with timestamps

All processing happens in the cloud using GitHub's infrastructure - no local setup required for the dataset to stay current.

Each circular is stored as a markdown file with YAML frontmatter containing source, date, impact level, affected stocks, and AI-generated categorization.

## Repository Structure

```
├── cmd/server/             # Go web server (main application)
├── internal/               # Go server internals
│   ├── content/           # Content loading and indexing
│   ├── handlers/          # HTTP handlers (RSS, etc.)
│   ├── search/            # Typesense search integration
│   └── templates/         # HTML templates
├── scripts/                # Python processing pipeline
├── config/                 # Configuration files
├── hugo-site/content/      # Processed dataset (markdown files)
│   └── circulars/
│       ├── nse/           # NSE circulars by year
│       ├── bse/           # BSE circulars by year
│       └── sebi/          # SEBI circulars by year
├── static/css/             # Stylesheets
└── .github/workflows/      # GitHub Actions for automation
```

## Development

**Quick start:**
```bash
just serve              # Start development server
just serve-with-search  # Start server with Typesense search
just build              # Build production binary
```

See `justfile` for all available commands.

## Contributing

Contributions welcome! You can:

- Improve the processing pipeline (RSS parsing, document extraction, LLM prompts)
- Fix data issues or incorrectly processed circulars
- Enhance the website design or functionality  
- Add new features (search, filtering, analysis)
- Improve documentation

See [Technical Reference](.local/docs/technical-reference.md) for development setup.

**Issues**: [GitHub Issues](https://github.com/rhnvrm/stock-market-circulars/issues)

## License

[Your License Here]