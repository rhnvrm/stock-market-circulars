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

# Search Commands

# Start Typesense server for local development
search-start:
    @echo "🔍 Starting Typesense server..."
    docker compose up -d typesense
    @echo "⏳ Waiting for Typesense to be ready..."
    @sleep 5
    @curl -sf "http://localhost:8108/health" > /dev/null && echo "✅ Typesense is ready" || echo "⚠️ Typesense starting up..."

# Stop Typesense server
search-stop:
    @echo "🛑 Stopping Typesense server..."
    docker compose down

# Generate search data from Hugo content
search-build:
    @echo "📄 Generating search data..."
    cd hugo-site && hugo --minify --gc
    @echo "✅ Search data generated: hugo-site/public/search.json"

# Import search data into Typesense
search-import *args:
    @echo "📤 Importing search data into Typesense..."
    @cd scripts && uv run typesense_import.py --data-path ../hugo-site/public/search.json {{args}}

# Rebuild search index (delete and recreate)
search-rebuild:
    @echo "🔄 Rebuilding search index..."
    just search-build
    just search-import --rebuild

# Full search setup (start server, build, import)
search-setup:
    just search-start
    just search-build
    just search-import

# Development with search (build + import + serve)
dev-search:
    just search-build
    just search-import
    just serve

