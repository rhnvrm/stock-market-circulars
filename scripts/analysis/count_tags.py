#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter",
# ]
# ///
"""Count unique tags and show stats."""

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

print(f"Total unique tags: {len(all_tags)}")
print(f"Total tag instances: {sum(all_tags.values())}")
print()
print("Top 50 tags:")
for tag, count in all_tags.most_common(50):
    print(f"  {count:5d} {tag}")
