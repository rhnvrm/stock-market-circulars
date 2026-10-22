# Go Server for exchangecirculars.com

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
GET /circulars/{source}/           NSE/BSE/SEBI/RBI/MSEI/India INX filtered lists
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

## Published Docker image

The `Publish serving app image` workflow builds the root `Dockerfile` and pushes
the Go server image to `ghcr.io/rhnvrm/exchange-circulars` for Linux amd64.
It authenticates with the repository's automatic `GITHUB_TOKEN`; no registry
secret is required.

To publish a release after the workflow is merged, tag the desired commit:

```bash
git tag v1.0.0
git push origin v1.0.0
```

Choose a new version for each release. A stable tag such as `v1.0.0` publishes
`:1.0.0`, `:1.0`, `:latest`, and `:sha-<full-commit-sha>`. A prerelease such as
`v1.1.0-rc.1` publishes `:1.1.0-rc.1` and the commit tag without updating
`:latest` or the minor version alias. Publishing an older stable release also
moves `:latest` to that release. The version is embedded in the server through
the Dockerfile's `BUILD_VERSION` argument.

You can also run the workflow manually from GitHub Actions for a selected branch
or tag. Branch builds publish only the commit tag.

The image excludes the circular dataset. Mount a content directory to run it:

```bash
docker run --rm -p 8080:8080 \
  -e BASE_URL=http://localhost:8080 \
  -v "$PWD/hugo-site/content:/data/content:ro" \
  ghcr.io/rhnvrm/exchange-circulars:1.0.0
```

The mounted files must be readable by the image's non-root `app` user. For
anonymous pulls, set the package visibility to public in its GitHub package
settings after the first publish; otherwise authenticate with `docker login ghcr.io`.

For production, set `BASE_URL=https://exchangecirculars.com` so canonical URLs
and feed links use the public domain.

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
