#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter",
# ]
# ///
"""Find tags that could potentially be merged based on patterns."""

from pathlib import Path
from collections import Counter, defaultdict
import frontmatter
import re

content_dir = Path(__file__).parent.parent / "hugo-site" / "content" / "circulars"
all_tags = Counter()

for f in content_dir.rglob("*.md"):
    try:
        post = frontmatter.load(f)
        tags = post.metadata.get("tags", [])
        for tag in tags:
            all_tags[tag.lower()] += 1
    except:
        pass

# Group tags by common stems/patterns
def get_stem(tag):
    """Get a rough stem by removing common suffixes."""
    tag = tag.lower()
    # Remove common suffixes
    for suffix in ['-listing', '-issue', '-allotment', '-redemption', '-payment',
                   '-securities', '-shares', '-fund', '-funds', '-market',
                   '-segment', '-trading', '-investors', '-investor', '-date',
                   '-announcement', '-notice', '-circular', '-update', '-change',
                   '-transfer', '-conversion', '-exercise', '-offer', '-period',
                   '-requirement', '-requirements', '-compliance', '-action',
                   '-actions', '-suspension', '-restrictions', '-settlement']:
        if tag.endswith(suffix):
            return tag[:-len(suffix)]
    return tag

# Group by stems
stem_groups = defaultdict(list)
for tag, count in all_tags.items():
    stem = get_stem(tag)
    stem_groups[stem].append((tag, count))

# Find groups with multiple tags
print("=" * 70)
print("POTENTIAL MERGE GROUPS (tags sharing common stems)")
print("=" * 70)
print()

# Sort by total count in group
groups_with_counts = []
for stem, tags in stem_groups.items():
    if len(tags) > 1:
        total = sum(c for t, c in tags)
        groups_with_counts.append((stem, tags, total))

groups_with_counts.sort(key=lambda x: -x[2])

for stem, tags, total in groups_with_counts[:50]:
    print(f"\n[{stem}] (total: {total})")
    for tag, count in sorted(tags, key=lambda x: -x[1]):
        print(f"    {count:5d}  {tag}")

# Also find plurals
print("\n" + "=" * 70)
print("SINGULAR/PLURAL PAIRS")
print("=" * 70)
print()

singular_plural = []
for tag in all_tags:
    if tag.endswith('s') and tag[:-1] in all_tags:
        singular_plural.append((tag[:-1], tag, all_tags[tag[:-1]], all_tags[tag]))

singular_plural.sort(key=lambda x: -(x[2] + x[3]))
for sing, plur, sc, pc in singular_plural[:30]:
    print(f"  {sing} ({sc}) / {plur} ({pc})")

# Find company name tags (often end with -ltd, -limited, -finance, -bank, etc)
print("\n" + "=" * 70)
print("COMPANY NAME TAGS (candidates for removal or separate field)")
print("=" * 70)
print()

company_patterns = ['-ltd', '-limited', '-finance', '-bank', '-capital',
                    '-securities', '-housing', '-industries', '-pharma',
                    '-infrastructure', '-power', '-energy', '-steel']
company_tags = []
for tag, count in all_tags.items():
    for pattern in company_patterns:
        if pattern in tag:
            company_tags.append((tag, count))
            break

company_tags.sort(key=lambda x: -x[1])
print(f"Found {len(company_tags)} company-like tags")
print("\nTop 30:")
for tag, count in company_tags[:30]:
    print(f"  {count:5d}  {tag}")

# Find tags with numbers (likely specific dates/amounts)
print("\n" + "=" * 70)
print("TAGS WITH NUMBERS (likely data, not categories)")
print("=" * 70)
print()

numeric_tags = [(t, c) for t, c in all_tags.items() if re.search(r'\d', t)]
numeric_tags.sort(key=lambda x: -x[1])
print(f"Found {len(numeric_tags)} tags with numbers")
print("\nTop 30:")
for tag, count in numeric_tags[:30]:
    print(f"  {count:5d}  {tag}")
