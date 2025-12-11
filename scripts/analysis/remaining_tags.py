#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter",
#     "pyyaml",
# ]
# ///
"""Show remaining tags after normalization to find more merge opportunities."""

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

# Count tags
content_dir = Path(__file__).parent.parent / "hugo-site" / "content" / "circulars"
after_tags = Counter()

for f in content_dir.rglob("*.md"):
    try:
        post = frontmatter.load(f)
        tags = post.metadata.get("tags", [])
        stocks = set(s.upper() for s in post.metadata.get("stocks", []))

        for tag in tags:
            normalized = normalize_tag(tag)
            if normalized and normalized.upper() not in stocks:
                after_tags[normalized] += 1
    except:
        pass

# Show tags NOT in merge rules (remaining to consolidate)
already_canonical = set(config.get("merge_rules", {}).keys())
remaining = [(t, c) for t, c in after_tags.items() if t not in already_canonical]
remaining.sort(key=lambda x: -x[1])

print("=" * 70)
print("REMAINING TAGS NOT IN MERGE RULES (candidates for new rules)")
print("=" * 70)
print(f"\nTotal remaining unique tags: {len(remaining)}")
print(f"\nTags with 10+ occurrences (sorted by frequency):")
print()

for tag, count in remaining:
    if count >= 10:
        print(f"  {count:5d}  {tag}")

print("\n" + "=" * 70)
print("TAGS WITH 5-9 OCCURRENCES")
print("=" * 70)
for tag, count in remaining:
    if 5 <= count < 10:
        print(f"  {count:5d}  {tag}")
