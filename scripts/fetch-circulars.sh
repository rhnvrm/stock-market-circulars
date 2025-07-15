#!/bin/bash
set -euo pipefail

# Stock Market Circulars RSS Feed Scraper
# Downloads new circulars from NSE, BSE, and SEBI RSS feeds

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
INBOX_DIR="$PROJECT_DIR/inbox"
STATE_DIR="$PROJECT_DIR/state"

# RSS Feed URLs
declare -A RSS_FEEDS=(
    ["nse"]="https://nsearchives.nseindia.com/content/RSS/Circulars.xml"
    ["bse"]="https://www.bseindia.com/rss/bsecirculars.xml"
    ["sebi"]="https://www.sebi.gov.in/sebirss.xml"
)

# Ensure directories exist
mkdir -p "$INBOX_DIR" "$STATE_DIR"

log_info() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] INFO: $*"
}

log_error() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: $*" >&2
}

# Check if a GUID has been processed before
is_processed() {
    local source="$1"
    local guid="$2"
    local seen_file="$STATE_DIR/${source}_seen_guids.txt"
    
    [[ -f "$seen_file" ]] && grep -Fxq "$guid" "$seen_file"
}

# Mark a GUID as processed
mark_processed() {
    local source="$1"
    local guid="$2"
    local seen_file="$STATE_DIR/${source}_seen_guids.txt"
    
    echo "$guid" >> "$seen_file"
}

# Download file with proper naming
download_file() {
    local url="$1"
    local source="$2"
    local title="$3"
    local pubdate="$4"
    
    # Clean filename from title and add source prefix
    local clean_title=$(echo "$title" | sed 's/[^a-zA-Z0-9._-]/_/g' | cut -c1-100)
    local date_prefix=$(date -d "$pubdate" '+%Y%m%d' 2>/dev/null || date '+%Y%m%d')
    local filename="${source}_${date_prefix}_${clean_title}"
    
    # Detect file extension from URL
    local extension=""
    case "$url" in
        *.pdf|*.PDF) extension=".pdf" ;;
        *.doc|*.DOC) extension=".doc" ;;
        *.docx|*.DOCX) extension=".docx" ;;
        *) extension=".pdf" ;;  # Default to PDF
    esac
    
    local filepath="$INBOX_DIR/${filename}${extension}"
    
    # Skip if file already exists
    if [[ -f "$filepath" ]]; then
        log_info "File already exists: $filename$extension"
        return 0
    fi
    
    log_info "Downloading: $url -> $filename$extension"
    
    # Download with timeout and proper error handling
    if timeout 60 wget -q -O "$filepath" "$url"; then
        log_info "Successfully downloaded: $filename$extension"
        return 0
    else
        log_error "Failed to download: $url"
        [[ -f "$filepath" ]] && rm "$filepath"  # Clean up partial download
        return 1
    fi
}

# Process RSS feed for a specific source
process_feed() {
    local source="$1"
    local rss_url="$2"
    local temp_file=$(mktemp)
    
    log_info "Processing $source RSS feed: $rss_url"
    
    # Download RSS feed with timeout
    if ! timeout 30 curl -s -f -L "$rss_url" -o "$temp_file"; then
        log_error "Failed to download RSS feed for $source"
        rm "$temp_file"
        return 1
    fi
    
    # Validate XML structure
    if ! xmlstarlet val "$temp_file" 2>/dev/null; then
        log_error "Invalid XML structure for $source RSS feed"
        rm "$temp_file"
        return 1
    fi
    
    local new_items=0
    
    # Parse RSS feed and process each item
    xmlstarlet sel -t -m "/rss/channel/item" \
        -v "guid" -o "|" \
        -v "title" -o "|" \
        -v "link" -o "|" \
        -v "pubDate" -o "|" \
        -v "enclosure/@url" -n "$temp_file" 2>/dev/null | \
    while IFS='|' read -r guid title link pubdate enclosure_url; do
        # Skip empty lines
        [[ -z "$guid" && -z "$title" ]] && continue
        
        # Use link as fallback if no enclosure URL
        local download_url="${enclosure_url:-$link}"
        
        # Skip if we've already processed this item
        if is_processed "$source" "$guid"; then
            continue
        fi
        
        # Try to download the file
        if download_file "$download_url" "$source" "$title" "$pubdate"; then
            mark_processed "$source" "$guid"
            ((new_items++))
        fi
    done
    
    rm "$temp_file"
    log_info "Processed $source: $new_items new items downloaded"
    return 0
}

# Main execution
main() {
    log_info "Starting RSS feed processing..."
    
    local total_new=0
    
    for source in "${!RSS_FEEDS[@]}"; do
        if process_feed "$source" "${RSS_FEEDS[$source]}"; then
            log_info "Successfully processed $source feed"
        else
            log_error "Failed to process $source feed"
        fi
        echo  # Add spacing between sources
    done
    
    log_info "RSS feed processing completed"
    log_info "Check $INBOX_DIR for downloaded circulars"
}

# Run main function
main "$@"