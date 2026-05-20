# Go Server Configuration

The server is configured via environment variables. Copy `.env.example` to `.env` and customize as needed.

## Environment Variables

### Server Settings

| Variable | Default | Description |
|----------|---------|-------------|
| `ADDR` | `:8080` | Server listen address (e.g., `:9999`, `localhost:3000`) |
| `BASE_URL` | `http://localhost:8080` | Base URL for RSS feeds and links |
| `CONTENT_DIR` | `./hugo-site/content` | Directory containing markdown circulars |

### Search Settings (Optional)

| Variable | Default | Description |
|----------|---------|-------------|
| `TYPESENSE_HOST` | `localhost:8108` | Typesense server address |
| `TYPESENSE_API_KEY` | _(none)_ | Typesense API key (search disabled if empty) |
| `TYPESENSE_COLLECTION` | `circulars` | Collection name in Typesense |
| `TYPESENSE_AUTO_INDEX` | `true` | Auto-index circulars on server startup |

## Quick Start

```bash
# Default (port 9999)
just serve

# With Typesense search
just serve-with-search

# Custom port
ADDR=:3000 BASE_URL=http://localhost:3000 just serve

# Production mode
just build
ADDR=:8080 ./server.bin
```

## Examples

### Local development on different port
```bash
ADDR=:3000 BASE_URL=http://localhost:3000 go run cmd/server/main.go
```

### Production with Typesense
```bash
export ADDR=:80
export BASE_URL=https://example.com
export TYPESENSE_API_KEY=your-api-key
export TYPESENSE_HOST=typesense.example.com:443
./server.bin
```

### Disable auto-indexing
```bash
TYPESENSE_AUTO_INDEX=false just serve-with-search
```
