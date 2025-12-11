#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter",
#     "pyyaml",
# ]
# ///
"""Simulate tag normalization and show before/after stats."""

from pathlib import Path
from collections import Counter
import frontmatter
import yaml
import re

# Load tag rules
rules_path = Path(__file__).parent / "tag_rules.yaml"
with open(rules_path) as f:
    config = yaml.safe_load(f)

# Build remove patterns
remove_patterns = []
for pattern in config.get("remove_patterns", []):
    try:
        remove_patterns.append(re.compile(pattern, re.IGNORECASE))
    except:
        pass

# Build merge map
merge_map = {}
for canonical, aliases in config.get("merge_rules", {}).items():
    merge_map[canonical.lower()] = canonical.lower()
    for alias in aliases:
        merge_map[alias.lower()] = canonical.lower()

def should_remove(tag):
    for pattern in remove_patterns:
        if pattern.match(tag):
            return True
    return False

def normalize_tag(tag):
    tag = tag.lower().strip()
    if should_remove(tag):
        return None
    return merge_map.get(tag, tag)

def is_tag_stock_duplicate(tag, stocks_simplified):
    """Check if tag matches any stock (fuzzy)."""
    tag_simplified = re.sub(r'[^a-z0-9]', '', tag.lower())
    if tag_simplified in stocks_simplified:
        return True
    # Partial match for company names
    if len(tag_simplified) >= 5:
        for stock_simp in stocks_simplified:
            if len(stock_simp) >= 5:
                if tag_simplified in stock_simp or stock_simp in tag_simplified:
                    return True
    return False

# Count tags
content_dir = Path(__file__).parent.parent / "hugo-site" / "content" / "circulars"
before_tags = Counter()
after_tags = Counter()

for f in content_dir.rglob("*.md"):
    try:
        post = frontmatter.load(f)
        tags = post.metadata.get("tags", [])
        stocks = post.metadata.get("stocks", [])
        stocks_upper = set(s.upper() for s in stocks if s)
        stocks_simplified = set(re.sub(r'[^A-Z0-9]', '', s.upper()) for s in stocks if s)

        for tag in tags:
            before_tags[tag.lower()] += 1

            normalized = normalize_tag(tag)
            if normalized and not is_tag_stock_duplicate(normalized, stocks_simplified):
                after_tags[normalized] += 1
    except:
        pass

print("=" * 60)
print("TAG NORMALIZATION SIMULATION")
print("=" * 60)
print()
print(f"BEFORE:")
print(f"  Unique tags: {len(before_tags):,}")
print(f"  Total instances: {sum(before_tags.values()):,}")
print()
print(f"AFTER:")
print(f"  Unique tags: {len(after_tags):,}")
print(f"  Total instances: {sum(after_tags.values()):,}")
print()
print(f"REDUCTION:")
print(f"  Unique tags: {len(before_tags) - len(after_tags):,} ({100 * (len(before_tags) - len(after_tags)) / len(before_tags):.1f}%)")
print(f"  Instances: {sum(before_tags.values()) - sum(after_tags.values()):,}")
print()
print("Top 30 tags AFTER normalization:")
for tag, count in after_tags.most_common(30):
    print(f"  {count:5d} {tag}")
