# Go Server for Stock Market Circulars

## Status: MVP Complete ✓

A lightweight Go server that replaces Hugo with lazy markdown rendering and caching.

## What's Implemented

### ✓ Core Features
- **Content Loading**: Frontmatter parsing for 14K+ markdown files
- **Index Building**: Fast startup with lightweight index (<5 seconds)
- **Markdown Rendering**: Goldmark with GFM support
- **HTTP Routes**: Home, source lists, single circular pages
- **Lazy Loading**: Content loaded on-demand, not at startup

### ✓ Routes Available
```
GET /                              Home page (recent circulars)
GET /circulars/{source}/           NSE/BSE/SEBI filtered lists
GET /circulars/{source}/{year}/{slug}/  Single circular detail
GET /health                        Health check endpoint
```

### ⏳ Not Yet Implemented
- RSS feeds (custom `circular:` namespace)
- Typesense search integration
- Proper Hugo template porting (currently using inline HTML)
- Pagination UI
- Taxonomy pages (tags, stocks)

## Quick Start

```bash
# Build the server
just server-build

# Run the server
./server.bin

# Or build and run directly
just server

# Test it
curl http://localhost:8080/health
```

## Environment Variables

```bash
ADDR=:8080                          # Server address
CONTENT_DIR=./hugo-site/content     # Content directory
BASE_URL=http://localhost:8080      # Base URL
```

## Performance

**Actual Results:**
- Index build: ~2-5 seconds for 14,686 files
- First page load: <500ms (uncached)
- Subsequent loads: <50ms (cached in-memory)

**vs Hugo:**
- Hugo: 6+ minutes to build all pages
- Go Server: No build time, instant startup

## Project Structure

```
cmd/server/main.go                  # Entry point
internal/
  models/circular.go                # Data structures
  content/
    loader.go                       # Frontmatter parsing
    index.go                        # Index building & querying
  render/
    markdown.go                     # Goldmark renderer
static/css/style.css                # Copied from Hugo theme
```

## Next Steps

To complete the migration:

1. **RSS Feeds** - Port `hugo-site/themes/minimal/layouts/_default/rss.xml`
2. **Templates** - Port HTML templates properly (currently inline)
3. **Search** - Integrate Typesense for search functionality
4. **Taxonomy Pages** - Implement /tags/ and /stocks/ routes
5. **Testing** - Compare output with Hugo for parity

## Development

```bash
# Watch mode (not implemented yet - manual restart needed)
just server

# Build binary
just server-build

# Run Hugo for comparison
just serve
```

## Notes

- CSS copied from Hugo theme (working)
- Content directory is `hugo-site/content/` (unchanged)
- Python processing pipeline unaffected
- Hugo can remain for GitHub Pages if needed

## Current Limitations

1. Templates are inline HTML (needs proper porting)
2. No Alpine.js interactive features yet
3. No RSS feeds yet
4. No search yet
5. No proper pagination UI

## Testing

Try these URLs after starting the server:

```
http://localhost:8080/
http://localhost:8080/circulars/nse/
http://localhost:8080/circulars/bse/
http://localhost:8080/circulars/nse/2025/[any-slug]/
http://localhost:8080/health
```

Replace `[any-slug]` with an actual circular slug from the content directory.
