# Stock Market Circulars Project Commands

# Default: show available commands
default:
    @just --list

# Core Commands

# Run RSS scraping and AI processing pipeline
pipeline:
    @echo "🚀 Running RSS scraping & AI processing pipeline..."
    cd scripts && uv run combined_pipeline.py main

# Regenerate specific items with updated prompts
regenerate *args:
    @echo "🔄 Regenerating items: {{args}}"
    cd scripts && uv run combined_pipeline.py regenerate {{args}}

# Development Commands

# Start Go development server (port 9999 by default to avoid conflicts)
serve:
    @echo "🌐 Starting Go development server on :9999..."
    ADDR=:9999 BASE_URL=http://localhost:9999 go run cmd/server/main.go

# Build Go server binary for production
build:
    @echo "🏗️ Building Go server binary..."
    go build -o server.bin cmd/server/main.go
    @echo "✅ Binary created: server.bin"

# Essential Utilities

# Check dependencies and system status
deps:
    @echo "🔧 Checking dependencies..."
    @which curl > /dev/null && echo "✅ curl" || echo "❌ curl"
    @which go > /dev/null && echo "✅ go" || echo "❌ go"
    @which claude > /dev/null && echo "✅ claude" || echo "❌ claude"
    @cd scripts && uv run combined_pipeline.py --help > /dev/null && echo "✅ Python dependencies" || echo "❌ Missing Python dependencies"

# Show processing statistics and status
stats:
    @cd scripts && uv run analyze_stats.py

# View recent logs
logs:
    @tail -20 combined_pipeline.log 2>/dev/null || echo "No logs found - run 'just pipeline' first"

# Cleaning Commands

# Clean build artifacts
clean:
    @echo "🧹 Cleaning build artifacts..."
    rm -f server.bin
    @echo "✅ Build artifacts cleaned"

# Reset pipeline state for fresh run
clean-state:
    @echo "🧹 Cleaning pipeline state..."
    rm -f combined_pipeline.log
    @echo "✅ State cleaned"

# CI/CD Commands (for GitHub Actions)

# Trigger GitHub Actions workflow manually
trigger-workflow:
    @echo "🚀 Triggering GitHub Actions workflow..."
    @gh workflow run update-circulars.yml

# Validate RSS feeds are accessible
validate:
    @echo "🔍 Validating RSS feeds..."
    @curl -sf "https://nsearchives.nseindia.com/content/RSS/Circulars.xml" > /dev/null && echo "✅ NSE RSS" || echo "❌ NSE RSS"
    @curl -sf "https://www.bseindia.com/data/xml/notices.xml" > /dev/null && echo "✅ BSE RSS" || echo "❌ BSE RSS"
    @curl -sf "https://www.sebi.gov.in/sebirss.xml" > /dev/null && echo "✅ SEBI RSS" || echo "❌ SEBI RSS"

# Setup for CI/CD or fresh development
setup:
    mkdir -p hugo-site/content/circulars/{nse,bse,sebi}/2025

# Normalization Commands

# Dry-run normalization to preview changes
normalize-dry:
    @echo "🔍 Running normalization dry-run..."
    cd scripts && uv run run_normalization.py --dry-run

# Apply normalization to all circulars
normalize:
    @echo "🔄 Normalizing stocks and tags..."
    cd scripts && uv run run_normalization.py

# Normalize only stocks
normalize-stocks:
    @echo "🔄 Normalizing stocks only..."
    cd scripts && uv run run_normalization.py --stocks-only

# Normalize only tags
normalize-tags:
    @echo "🔄 Normalizing tags only..."
    cd scripts && uv run run_normalization.py --tags-only

# Docker Commands

# Start Typesense container
typesense-up:
    @echo "🐳 Starting Typesense container..."
    docker-compose up -d
    @echo "✅ Typesense running on localhost:8108"

# Stop Typesense container
typesense-down:
    @echo "🛑 Stopping Typesense container..."
    docker-compose down

# View Typesense logs
typesense-logs:
    docker-compose logs -f typesense

# Run Go server with Typesense
serve-with-search:
    @echo "🌐 Starting Go server with Typesense search on :9999..."
    ADDR=:9999 BASE_URL=http://localhost:9999 TYPESENSE_API_KEY=stock-circulars-dev-key TYPESENSE_HOST=localhost:8108 go run cmd/server/main.go

# UAT Deployment Commands
# Environment variables required (set in .env.local):
# - S3_ENDPOINT: MinIO/S3 endpoint URL
# - S3_BUCKET: Target bucket name
# - INFRA_PATH: Path to nomad infra repo
# - NOMAD_LOGIN_SCRIPT: Path to nomad login script
# - NOMAD_LOGS_SCRIPT: Path to logs script
# - NOMAD_DEPLOYMENT: Deployment directory name

# Version string for builds
last_commit := `git rev-parse --short HEAD`
last_commit_date := `git show -s --format=%ci`
buildstr := "UAT (" + last_commit + " " + last_commit_date + ")"

# Build static binary for UAT deployment
build-uat:
    @echo "🏗️ Building UAT binary..."
    mkdir -p bin
    CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w -extldflags '-static' -X 'main.buildString={{buildstr}}'" -o bin/circulars.bin cmd/server/main.go
    @echo "✅ Binary created: bin/circulars.bin"

# Upload binary to S3/MinIO
upload-uat:
    just build-uat
    @echo "📤 Uploading to S3..."
    aws s3 cp bin/circulars.bin s3://$S3_BUCKET/ --endpoint-url $S3_ENDPOINT
    @echo "✅ Binary uploaded to s3://$S3_BUCKET/circulars.bin"

# Deploy to UAT Nomad
deploy-uat:
    just upload-uat
    @echo "🚀 Deploying to UAT..."
    eval $($NOMAD_LOGIN_SCRIPT) && \
    cd $INFRA_PATH/deployments/$NOMAD_DEPLOYMENT/ && \
    nomad run deployment.nomad
    @echo "✅ Deployed to UAT. Check Nomad UI for status."

# View UAT logs
logs-uat:
    @echo "📋 Fetching UAT logs..."
    eval $($NOMAD_LOGIN_SCRIPT) && \
    $NOMAD_LOGS_SCRIPT logs $NOMAD_DEPLOYMENT server

# Test git sync locally
serve-with-git-sync:
    @echo "🌐 Starting server with git sync mode..."
    GIT_REPO_URL=https://github.com/rhnvrm/stock-market-circulars.git \
    GIT_DATA_PATH=/tmp/stock-market-circulars-data \
    SYNC_INTERVAL="@every 5m" \
    ADDR=:9999 \
    BASE_URL=http://localhost:9999 \
    go run cmd/server/main.go

