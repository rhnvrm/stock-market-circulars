#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter",
# ]
# ///
"""Analyze company-name tags that could be cross-referenced with stocks."""

from pathlib import Path
from collections import Counter, defaultdict
import frontmatter
import json
import re

# Load instruments to get company names
instruments_path = Path("/tmp/instruments.json")
ticker_to_name = {}
name_to_ticker = {}

if instruments_path.exists():
    with open(instruments_path) as f:
        for line in f:
            try:
                record = json.loads(line.strip())
                if record.get("instrument_type") == "EQ":
                    ticker = record.get("tradingsymbol", "").upper()
                    name = record.get("name", "").lower()
                    if ticker and name:
                        ticker_to_name[ticker] = name
                        # Create simplified name for matching
                        simple_name = re.sub(r'[^a-z0-9]', '', name)
                        name_to_ticker[simple_name] = ticker
            except:
                pass

print(f"Loaded {len(ticker_to_name)} ticker->name mappings")

# Analyze tags
content_dir = Path(__file__).parent.parent / "hugo-site" / "content" / "circulars"

# Count how often a tag appears WITH a corresponding stock
tag_with_stock = Counter()  # tag appears AND stock is present
tag_without_stock = Counter()  # tag appears but stock NOT present
company_tags = set()

# Common company suffixes in tags
company_suffixes = ['-ltd', '-limited', '-finance', '-bank', '-capital',
                   '-securities', '-housing', '-industries', '-pharma',
                   '-infrastructure', '-power', '-energy', '-steel',
                   '-mutual-fund', '-fincorp', '-finserv']

for f in content_dir.rglob("*.md"):
    try:
        post = frontmatter.load(f)
        tags = [t.lower() for t in post.metadata.get("tags", [])]
        stocks = set(s.upper() for s in post.metadata.get("stocks", []))

        for tag in tags:
            # Check if tag looks like a company name
            is_company_tag = any(tag.endswith(suffix) for suffix in company_suffixes)

            if is_company_tag:
                company_tags.add(tag)

                # Try to match tag to a stock
                # Method 1: Direct tag->ticker conversion (e.g., "icici-bank" -> "ICICIBANK")
                tag_as_ticker = re.sub(r'[^a-z0-9]', '', tag).upper()

                # Method 2: Check if any stock in the file matches
                matched = False
                for stock in stocks:
                    stock_simple = re.sub(r'[^A-Z0-9]', '', stock)
                    if tag_as_ticker == stock_simple or tag_as_ticker in stock_simple or stock_simple in tag_as_ticker:
                        matched = True
                        break

                if matched:
                    tag_with_stock[tag] += 1
                else:
                    tag_without_stock[tag] += 1
    except:
        pass

print(f"\nFound {len(company_tags)} company-like tags")
print()

# Show tags that ALWAYS appear with corresponding stock (safe to remove)
print("=" * 70)
print("COMPANY TAGS THAT ALWAYS APPEAR WITH MATCHING STOCK (safe to remove)")
print("=" * 70)
always_with_stock = [(t, tag_with_stock[t]) for t in company_tags
                     if tag_with_stock[t] > 0 and tag_without_stock[t] == 0]
always_with_stock.sort(key=lambda x: -x[1])
print(f"\nTotal: {len(always_with_stock)} tags")
print("\nTop 50:")
for tag, count in always_with_stock[:50]:
    print(f"  {count:5d}  {tag}")

print()
print("=" * 70)
print("COMPANY TAGS THAT MOSTLY APPEAR WITH STOCK (>80% overlap)")
print("=" * 70)
mostly_with_stock = []
for t in company_tags:
    total = tag_with_stock[t] + tag_without_stock[t]
    if total >= 5 and tag_with_stock[t] / total >= 0.8:
        mostly_with_stock.append((t, tag_with_stock[t], tag_without_stock[t], total))
mostly_with_stock.sort(key=lambda x: -x[3])
print(f"\nTotal: {len(mostly_with_stock)} tags")
print("\nTag | With Stock | Without | Total | %")
for tag, with_s, without_s, total in mostly_with_stock[:30]:
    pct = 100 * with_s / total
    print(f"  {tag:40s} {with_s:5d} {without_s:5d} {total:5d} {pct:.0f}%")

print()
print("=" * 70)
print("COMPANY TAGS THAT RARELY APPEAR WITH STOCK (keep these)")
print("=" * 70)
rarely_with_stock = []
for t in company_tags:
    total = tag_with_stock[t] + tag_without_stock[t]
    if total >= 5 and (tag_with_stock[t] == 0 or tag_with_stock[t] / total < 0.2):
        rarely_with_stock.append((t, tag_with_stock[t], tag_without_stock[t], total))
rarely_with_stock.sort(key=lambda x: -x[3])
print(f"\nTotal: {len(rarely_with_stock)} tags (these are used independently)")
print("\nTop 30:")
for tag, with_s, without_s, total in rarely_with_stock[:30]:
    print(f"  {tag:40s} with:{with_s:3d} without:{without_s:3d}")
