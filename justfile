# Stock Market Circulars Project Commands

# Default: show available commands
default:
    @just --list

# Core Commands

# Run RSS scraping and AI processing pipeline
pipeline:
    @echo "🚀 Running RSS scraping & AI processing pipeline..."
    uv run --script scripts/combined_pipeline.py main

# Regenerate specific items with updated prompts
regenerate *args:
    @echo "🔄 Regenerating items: {{args}}"
    uv run --script scripts/combined_pipeline.py regenerate {{args}}

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
    @uv run --script scripts/combined_pipeline.py --help > /dev/null && echo "✅ Python dependencies" || echo "❌ Missing Python dependencies"

# Show processing statistics and status
stats:
    @echo "📊 Processing Statistics"
    @echo "NSE: $(find hugo-site/content/circulars/nse -name "*.md" 2>/dev/null | wc -l) circulars"
    @echo "BSE: $(find hugo-site/content/circulars/bse -name "*.md" 2>/dev/null | wc -l) circulars" 
    @echo "SEBI: $(find hugo-site/content/circulars/sebi -name "*.md" 2>/dev/null | wc -l) circulars"
    @echo "Progress files: $(find state/combined_progress -name "*.json" 2>/dev/null | wc -l)"

# View recent logs
logs:
    @tail -20 state/combined_pipeline.log 2>/dev/null || echo "No logs found - run 'just pipeline' first"

# Cleaning Commands

# Clean Hugo build artifacts
clean:
    rm -rf hugo-site/public/ hugo-site/resources/

# Reset pipeline state for fresh run
clean-state:
    @echo "🧹 Cleaning pipeline state..."
    rm -rf state/combined_progress/* state/combined_errors/*
    rm -f state/*_combined_seen_guids.txt state/combined_pipeline.log
    @echo "✅ State cleaned"

# CI/CD Commands (for GitHub Actions)

# Validate RSS feeds are accessible
validate:
    @echo "🔍 Validating RSS feeds..."
    @curl -sf "https://nsearchives.nseindia.com/content/RSS/Circulars.xml" > /dev/null && echo "✅ NSE RSS" || echo "❌ NSE RSS"
    @curl -sf "https://www.bseindia.com/data/xml/notices.xml" > /dev/null && echo "✅ BSE RSS" || echo "❌ BSE RSS"
    @curl -sf "https://www.sebi.gov.in/sebirss.xml" > /dev/null && echo "✅ SEBI RSS" || echo "❌ SEBI RSS"

# Setup for CI/CD or fresh development
setup:
    mkdir -p state state/combined_progress state/combined_errors hugo-site/content/circulars/{nse,bse,sebi}/2025

