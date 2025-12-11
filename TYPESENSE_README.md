# Typesense Search Setup

## Starting Typesense

```bash
# Start Typesense with Docker
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f typesense
```

## Environment Variables

```bash
export TYPESENSE_HOST=localhost:8108
export TYPESENSE_API_KEY=stock-circulars-dev-key
```

## Indexing Circulars

```bash
# Index all circulars (run after starting the server)
curl -X POST http://localhost:8080/admin/index
```

## Testing Search

```bash
# Search via JSON API
curl "http://localhost:8080/api/search?q=listing"

# Search with source filter
curl "http://localhost:8080/api/search?q=ipo&source=nse"

# HTML search page
open http://localhost:8080/search?q=trading
```

## Stopping Typesense

```bash
# Stop container
docker-compose down

# Stop and remove data
docker-compose down -v
```

## Typesense Admin

Access Typesense admin at: http://localhost:8108/health

API Key: `stock-circulars-dev-key`
