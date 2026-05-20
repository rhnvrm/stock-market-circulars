# Development Guide

This guide covers local development workflow, code structure, and contribution guidelines.

## Prerequisites

- Go 1.21 or later
- Docker (optional, for Typesense search)
- Git

## Development Setup

### Using Nix (Recommended)

If you have Nix installed with flakes enabled:

```bash
# Enter development environment
nix develop

# This provides: Go, Python, uv, Claude CLI, Node.js
```

### Manual Setup

Install dependencies manually:
- Go: https://go.dev/dl/
- Just: https://github.com/casey/just
- Docker: https://docs.docker.com/get-docker/ (optional)

## Running the Server

### Quick Start

```bash
# Start development server on port 9999
just serve

# Or run directly
go run cmd/server/main.go
```

### With Search

```bash
# Start Typesense container
just typesense-up

# Start server with search enabled
just serve-with-search

# Stop Typesense when done
just typesense-down
```

### Custom Configuration

```bash
# Run on custom port
ADDR=:3000 BASE_URL=http://localhost:3000 go run cmd/server/main.go

# Disable auto-indexing
TYPESENSE_AUTO_INDEX=false just serve-with-search
```

See [Configuration](./configuration.md) for all environment variables.

## Building

```bash
# Build binary
just build

# Or directly
go build -o server.bin cmd/server/main.go

# Run binary
./server.bin
```

## Code Structure

```
stock-market-circulars/
├── cmd/
│   └── server/
│       └── main.go           # Main entry point, route setup
├── internal/
│   ├── content/              # Content loading and indexing
│   │   ├── loader.go         # Markdown file loader
│   │   ├── builder.go        # Index builder
│   │   └── index.go          # In-memory circular index
│   ├── handlers/             # HTTP handlers
│   │   └── rss.go            # RSS feed generation
│   ├── models/               # Data structures
│   │   └── circular.go       # Circular model
│   ├── render/               # Rendering utilities
│   │   └── markdown.go       # Markdown to HTML
│   ├── search/               # Search integration
│   │   └── typesense.go      # Typesense client
│   └── templates/            # HTML templates
│       ├── renderer.go       # Template engine
│       ├── page-home.html    # Home page
│       ├── page-source.html  # Source listings
│       ├── page-circular.html # Circular detail
│       └── page-search.html  # Search page
├── static/
│   └── css/
│       └── style.css         # Stylesheet
└── hugo-site/content/        # Markdown source data
    └── circulars/            # Circulars by source/year
```

## Adding Features

### Adding a New Route

1. Define handler in `cmd/server/main.go` or create new handler file in `internal/handlers/`
2. Register route in main.go router setup
3. Create template in `internal/templates/` if needed
4. Test manually

Example:
```go
r.Get("/new-route", func(w http.ResponseWriter, r *http.Request) {
    data := map[string]interface{}{
        "Title":   "New Page",
        "BaseURL": baseURL,
        "Path":    "/new-route",
    }
    tmplRenderer.Render(w, "page-new", data)
})
```

### Adding a Template

1. Create new template file in `internal/templates/page-*.html`
2. Use existing CSS classes from `static/css/style.css`
3. Include Alpine.js directives if needed for interactivity

### Modifying Search

1. Update schema in `internal/search/typesense.go` if needed
2. Modify indexing logic in `EnsureIndexed()` method
3. Test with Docker: `just typesense-up && just serve-with-search`

## Testing

Currently manual testing is performed. Future work will add automated tests.

### Manual Testing Checklist

- [ ] Home page loads (`http://localhost:9999/`)
- [ ] Source listings work (`/circulars/nse/`, `/circulars/bse/`, `/circulars/sebi/`)
- [ ] Individual circular pages render
- [ ] RSS feeds are valid XML (`/feed.xml`, `/circulars/nse/feed.xml`)
- [ ] Search works (if Typesense is running)
- [ ] Health check responds (`/health`)

## Running the Pipeline

The RSS scraping and AI processing pipeline is separate from the web server:

```bash
# Run pipeline to fetch and process new circulars
just pipeline

# Regenerate specific circulars
just regenerate CIRCULAR_ID_1 CIRCULAR_ID_2

# View pipeline logs
just logs

# Check processing statistics
just stats
```

## Available Commands

Run `just` to see all available commands:

```bash
just                    # List all commands
just serve              # Start development server
just serve-with-search  # Start with Typesense search
just build              # Build production binary
just pipeline           # Run RSS scraping pipeline
just typesense-up       # Start Typesense container
just typesense-down     # Stop Typesense container
just clean              # Clean build artifacts
just deps               # Check dependencies
```

## Contributing

### Workflow

1. Fork the repository
2. Create a feature branch: `git checkout -b feat-your-feature`
3. Make changes and test locally
4. Commit with descriptive messages
5. Push and create a pull request

### Commit Message Format

Use conventional commits:
- `feat: add new feature`
- `fix: fix bug in handler`
- `docs: update documentation`
- `chore: update dependencies`
- `refactor: restructure code`

### Code Style

- Follow standard Go formatting (`gofmt`)
- Use meaningful variable names
- Add comments for exported functions
- Keep functions focused and small

## Troubleshooting

### Port Already in Use

```bash
# Use a different port
ADDR=:3000 just serve
```

### Typesense Connection Failed

```bash
# Check if container is running
docker ps | grep typesense

# Start container
just typesense-up

# View logs
just typesense-logs
```

### Template Errors

Templates are embedded at compile time. After modifying templates:
```bash
# Rebuild to pick up changes
go build -o server.bin cmd/server/main.go
```

### Content Not Loading

Check that `CONTENT_DIR` points to the correct location:
```bash
# Default location
CONTENT_DIR=./hugo-site/content go run cmd/server/main.go
```

## Getting Help

- Open an issue: https://github.com/rhnvrm/stock-market-circulars/issues
- Check existing documentation in this directory
- Review the [Server Guide](./server.md) for usage details
- See the [Migration Roadmap](./migration-roadmap.md) for project status
