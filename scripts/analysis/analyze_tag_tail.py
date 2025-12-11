#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter",
# ]
# ///
"""Analyze the long tail of tags - tags that appear only once or twice."""

from pathlib import Path
from collections import Counter
import frontmatter

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

# Analyze distribution
once = sum(1 for t, c in all_tags.items() if c == 1)
twice = sum(1 for t, c in all_tags.items() if c == 2)
rare = sum(1 for t, c in all_tags.items() if c <= 5)
common = sum(1 for t, c in all_tags.items() if c > 10)

print("=" * 60)
print("TAG FREQUENCY DISTRIBUTION")
print("=" * 60)
print()
print(f"Total unique tags: {len(all_tags):,}")
print()
print(f"Tags appearing ONCE:     {once:,} ({100*once/len(all_tags):.1f}%)")
print(f"Tags appearing TWICE:    {twice:,} ({100*twice/len(all_tags):.1f}%)")
print(f"Tags appearing <= 5x:    {rare:,} ({100*rare/len(all_tags):.1f}%)")
print(f"Tags appearing > 10x:    {common:,} ({100*common/len(all_tags):.1f}%)")
print()
print("Sample of tags appearing only ONCE (first 30):")
once_tags = [t for t, c in all_tags.items() if c == 1][:30]
for t in sorted(once_tags):
    print(f"  - {t}")
print()
print("Tags appearing 2-5 times (first 30):")
rare_tags = [(t, c) for t, c in all_tags.items() if 2 <= c <= 5][:30]
for t, c in sorted(rare_tags, key=lambda x: x[1]):
    print(f"  {c}x {t}")
