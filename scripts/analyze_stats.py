#!/usr/bin/env python3
"""
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "pyyaml",
#     "pathlib",
# ]
# ///

Analyze circular processing statistics with status grouping.
"""

import yaml
from pathlib import Path
from collections import defaultdict, Counter
import sys

def extract_frontmatter(file_path):
    """Extract YAML frontmatter from markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('---'):
            return None
            
        # Find the end of frontmatter
        end_marker = content.find('\n---\n', 3)
        if end_marker == -1:
            return None
            
        frontmatter_content = content[3:end_marker]
        return yaml.safe_load(frontmatter_content)
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        return None

def analyze_circulars():
    """Analyze all circulars and group by status/stage."""
    base_path = Path("hugo-site/content/circulars")
    
    if not base_path.exists():
        print("❌ No circulars directory found")
        return
    
    stats = defaultdict(lambda: defaultdict(int))
    stage_counts = defaultdict(Counter)
    total_counts = defaultdict(int)
    
    sources = ['nse', 'bse', 'sebi']
    
    for source in sources:
        source_path = base_path / source
        if not source_path.exists():
            continue
            
        # Find all markdown files
        md_files = list(source_path.rglob("*.md"))
        total_counts[source] = len(md_files)
        
        for md_file in md_files:
            frontmatter = extract_frontmatter(md_file)
            if not frontmatter:
                continue
                
            # Extract processing stage/status
            processing = frontmatter.get('processing', {})
            stage = processing.get('stage', 'unknown')
            status = processing.get('status', 'unknown')
            
            # Count by stage
            stage_counts[source][stage] += 1
            
            # Store both stage and status info
            stats[source][f"{stage}"] += 1
    
    return stats, stage_counts, total_counts

def print_stats():
    """Print formatted statistics."""
    stats, stage_counts, total_counts = analyze_circulars()
    
    print("📊 Processing Statistics")
    print("=" * 50)
    
    # Overall counts
    for source in ['nse', 'bse', 'sebi']:
        count = total_counts.get(source, 0)
        print(f"{source.upper()}: {count} circulars")
    
    print()
    print("📈 Status Breakdown")
    print("-" * 30)
    
    # Status breakdown by source
    for source in ['nse', 'bse', 'sebi']:
        if source not in stage_counts:
            continue
            
        print(f"\n{source.upper()}:")
        stages = stage_counts[source]
        
        # Sort stages by priority
        stage_order = ['completed', 'claude_processing', 'text_extraction', 'downloading', 
                      'url_extraction', 'discovered', 'html_fallback', 'download_failed', 
                      'claude_failed', 'unknown']
        
        for stage in stage_order:
            if stage in stages:
                count = stages[stage]
                percentage = (count / total_counts[source] * 100) if total_counts[source] > 0 else 0
                
                # Add emoji for status
                emoji = {
                    'completed': '✅',
                    'claude_processing': '🤖',
                    'text_extraction': '📄',
                    'downloading': '⬇️',
                    'url_extraction': '🔗',
                    'discovered': '🔍',
                    'html_fallback': '🌐',
                    'download_failed': '❌',
                    'claude_failed': '🚫',
                    'unknown': '❓'
                }.get(stage, '📋')
                
                print(f"  {emoji} {stage:15} {count:3d} ({percentage:5.1f}%)")
    
    # Summary
    print("\n" + "=" * 50)
    total_all = sum(total_counts.values())
    total_completed = sum(stage_counts[source].get('completed', 0) for source in stage_counts)
    total_failed = sum(stage_counts[source].get('download_failed', 0) + 
                      stage_counts[source].get('claude_failed', 0) for source in stage_counts)
    
    if total_all > 0:
        completion_rate = (total_completed / total_all * 100)
        failure_rate = (total_failed / total_all * 100)
        print(f"📊 Overall: {total_all} total, {total_completed} completed ({completion_rate:.1f}%), {total_failed} failed ({failure_rate:.1f}%)")

if __name__ == "__main__":
    print_stats()