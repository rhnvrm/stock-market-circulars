#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter",
# ]
# ///
"""Analyze stock distribution."""

from pathlib import Path
from collections import Counter
import frontmatter
import json
import re

# Load instruments to check validity
instruments_path = Path("/tmp/instruments.json")
valid_tickers = set()

if instruments_path.exists():
    with open(instruments_path) as f:
        for line in f:
            try:
                record = json.loads(line.strip())
                if record.get("instrument_type") == "EQ":
                    ticker = record.get("tradingsymbol", "").upper()
                    if ticker:
                        valid_tickers.add(ticker)
            except:
                pass

print(f"Loaded {len(valid_tickers)} valid tickers from instruments.json\n")

content_dir = Path(__file__).parent.parent / "hugo-site" / "content" / "circulars"
all_stocks = Counter()
valid_stocks = Counter()
invalid_stocks = Counter()
isin_stocks = Counter()

for f in content_dir.rglob("*.md"):
    try:
        post = frontmatter.load(f)
        stocks = post.metadata.get("stocks", [])
        for stock in stocks:
            if stock:
                stock = stock.strip()
                all_stocks[stock] += 1

                # Categorize
                if re.match(r'^INE[A-Z0-9]{10}$', stock.upper()):
                    isin_stocks[stock] += 1
                elif stock.upper() in valid_tickers:
                    valid_stocks[stock] += 1
                else:
                    invalid_stocks[stock] += 1
    except:
        pass

print("=" * 70)
print("STOCK ANALYSIS")
print("=" * 70)
print(f"\nTotal unique stocks: {len(all_stocks):,}")
print(f"Total stock instances: {sum(all_stocks.values()):,}")
print()
print(f"Breakdown:")
print(f"  Valid tickers (in instruments.json): {len(valid_stocks):,} ({100*len(valid_stocks)/len(all_stocks):.1f}%)")
print(f"  ISINs: {len(isin_stocks):,} ({100*len(isin_stocks)/len(all_stocks):.1f}%)")
print(f"  Invalid/Other: {len(invalid_stocks):,} ({100*len(invalid_stocks)/len(all_stocks):.1f}%)")

print('\n' + "=" * 70)
print('Top 50 stocks by frequency:')
print("=" * 70)
for stock, count in all_stocks.most_common(50):
    status = "VALID" if stock.upper() in valid_tickers else "ISIN" if re.match(r'^INE[A-Z0-9]{10}$', stock.upper()) else "INVALID"
    print(f'  {count:5d}  {stock:30s} [{status}]')

print('\n' + "=" * 70)
print('INVALID/OTHER stocks (top 100):')
print("=" * 70)
for stock, count in invalid_stocks.most_common(100):
    print(f'  {count:5d}  {stock}')

print('\n' + "=" * 70)
print('Stocks appearing only ONCE:')
print("=" * 70)
once = [s for s, c in all_stocks.items() if c == 1]
print(f"Total: {len(once):,} stocks ({100*len(once)/len(all_stocks):.1f}%)")
print("\nFirst 50:")
for stock in sorted(once)[:50]:
    status = "VALID" if stock.upper() in valid_tickers else "ISIN" if re.match(r'^INE[A-Z0-9]{10}$', stock.upper()) else "INVALID"
    print(f'  {stock:30s} [{status}]')
