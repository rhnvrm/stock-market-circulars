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

# Start Hugo development server
serve:
    @echo "🌐 Starting Hugo development server..."
    cd hugo-site && hugo server --buildDrafts --watch --bind 0.0.0.0

# Build static site for production
build:
    @echo "🏗️ Building static site..."
    cd hugo-site && hugo --minify --gc

# Essential Utilities

# Check dependencies and system status
deps:
    @echo "🔧 Checking dependencies..."
    @which curl > /dev/null && echo "✅ curl" || echo "❌ curl"
    @which hugo > /dev/null && echo "✅ hugo" || echo "❌ hugo"  
    @which claude > /dev/null && echo "✅ claude" || echo "❌ claude"
    @cd scripts && uv run combined_pipeline.py --help > /dev/null && echo "✅ Python dependencies" || echo "❌ Missing Python dependencies"

# Show processing statistics and status
stats:
    @cd scripts && uv run analyze_stats.py

# View recent logs
logs:
    @tail -20 combined_pipeline.log 2>/dev/null || echo "No logs found - run 'just pipeline' first"

# Cleaning Commands

# Clean Hugo build artifacts
clean:
    rm -rf hugo-site/public/ hugo-site/resources/

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

# Go Server Commands

# Run Go server (local development)
server:
    @echo "🚀 Starting Go server..."
    go run cmd/server/main.go

# Build Go server binary
server-build:
    @echo "🏗️ Building Go server..."
    go build -o server.bin cmd/server/main.go
    @echo "✅ Binary created: server.bin"

# Run built Go server
server-run: server-build
    @echo "🚀 Running Go server..."
    ./server.bin

