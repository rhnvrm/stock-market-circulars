#!/usr/bin/env python3
"""
Backfill NSE circulars for a date range.

Two strategies:
1. API-based: Uses /api/circulars endpoint (rolling window, ~7 days)
2. Enumeration: Scans sequential circular numbers when API doesn't cover the range

Usage:
    # API-based (for recent dates within the rolling window)
    python3 scripts/backfill_nse.py --from-date 2026-02-13 --to-date 2026-02-19

    # Enumeration (for older dates outside the API window)
    python3 scripts/backfill_nse.py --enumerate --start-num 72732 --end-num 72783 \
        --from-date 2026-02-11 --to-date 2026-02-12

    # Dry run
    python3 scripts/backfill_nse.py --from-date 2026-02-13 --to-date 2026-02-19 --dry-run
"""

import argparse
import hashlib
import json
import re
import time
import urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path

IST = timezone(timedelta(hours=5, minutes=30))
CONTENT_DIR = Path("hugo-site/content/circulars")

# NSE department prefix to name mapping
DEPT_NAMES = {
    "CML": "Capital Market Listing", "CMPT": "Clearing/F&O",
    "CMTR": "Capital Market Trade", "COM": "Commodity Derivatives",
    "COMP": "Inspection & Compliance", "CMPL": "Inspection & Compliance",
    "CD": "Currency Derivatives", "DS": "Debt Segment",
    "FAOP": "Futures & Options", "INVG": "Surveillance",
    "ISC": "Legal/ISC", "MSD": "Member Services",
    "MFSS": "Mutual Fund", "NMF": "Mutual Fund",
    "SLBS": "Securities Lending", "SURV": "Surveillance",
}

PREFIXES = list(DEPT_NAMES.keys())
EXTENSIONS = ["pdf", "zip"]


def slugify(text, max_len=80):
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text)
    text = re.sub(r'-+', '-', text).strip('-')
    return text[:max_len]


def write_stub(circular_id, title, published_date, guid, pdf_url):
    dt_str = published_date[:10]
    year = dt_str[:4]
    slug = slugify(title)
    filename = f'nse-{dt_str}-{circular_id}-{slug}.md'
    out_dir = CONTENT_DIR / "nse" / year
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / filename

    if out_path.exists():
        return False

    now = datetime.now(IST).isoformat()
    content = f'''---
circular_id: {circular_id}
draft: true
guid: "{guid}"
pdf_url: "{pdf_url}"
processing:
  attempts: 0
  content_hash: ''
  processed_at: '{now}'
  processor_version: '2.0'
  stage: backfill_stub
  status: failed
published_date: '{published_date}'
rss_url: "{guid}"
source: nse
title: "{title.replace(chr(34), chr(92)+chr(34))}"
---

Processing in progress...'''
    out_path.write_text(content)
    return True


def backfill_api(from_date, to_date, dry_run=False):
    """Fetch from NSE circulars API (rolling window of ~7 days)."""
    from_str = from_date.strftime("%d-%m-%Y")
    to_str = to_date.strftime("%d-%m-%Y")

    print(f"Fetching NSE API: {from_str} to {to_str}")
    url = f"https://www.nseindia.com/api/circulars?from={from_str}&to={to_str}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0", "Accept": "application/json"
    })

    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())

    items = data if isinstance(data, list) else data.get("data", [])
    print(f"API returned {len(items)} items")

    # Filter to requested date range
    created, skipped = 0, 0
    seen = set()

    for item in items:
        title = item.get("sub", "").strip()
        link = item.get("circFilelink", "")
        circ_date = item.get("cirDate", "")  # YYYYMMDD

        if not link or link in seen:
            skipped += 1
            continue
        seen.add(link)

        # Parse date and filter
        if len(circ_date) == 8:
            item_date = datetime.strptime(circ_date, "%Y%m%d").date()
            if item_date < from_date or item_date > to_date:
                skipped += 1
                continue
            pub_date = f"{circ_date[:4]}-{circ_date[4:6]}-{circ_date[6:8]}T00:00:00+05:30"
        else:
            skipped += 1
            continue

        circular_id = hashlib.md5(f"nse_{link}".encode()).hexdigest()[:16]

        if dry_run:
            print(f"  [DRY RUN] {circ_date} {title[:60]}")
            created += 1
        elif write_stub(circular_id, title, pub_date, link, link):
            created += 1
        else:
            skipped += 1

    print(f"Created: {created}, Skipped: {skipped}")
    return created


def backfill_enumerate(start_num, end_num, from_date, to_date, dry_run=False):
    """Enumerate sequential NSE circular numbers and probe URLs."""
    total_nums = end_num - start_num + 1
    mid_num = start_num + total_nums // 2

    print(f"Scanning NSE circular numbers {start_num}-{end_num}")
    print(f"  Assigning {start_num}-{mid_num - 1} to {from_date}, {mid_num}-{end_num} to {to_date}")

    found, created = [], 0

    for num in range(start_num, end_num + 1):
        for prefix in PREFIXES:
            for ext in EXTENSIONS:
                url = f"https://nsearchives.nseindia.com/content/circulars/{prefix}{num}.{ext}"
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                try:
                    with urllib.request.urlopen(req, timeout=5) as resp:
                        data = resp.read(100)
                        if len(data) > 0:
                            found.append((num, prefix, ext, url))
                            print(f"  Found: {prefix}{num}.{ext}")
                            break
                except:
                    pass
            if any(f[0] == num for f in found):
                break
        time.sleep(0.05)

    print(f"\nFound {len(found)} circulars")

    for num, prefix, ext, url in found:
        dept = DEPT_NAMES.get(prefix, prefix)
        title = f"NSE Circular {prefix}{num} - {dept}"

        if num < mid_num:
            pub_date = f"{from_date.isoformat()}T00:00:00+05:30"
        else:
            pub_date = f"{to_date.isoformat()}T00:00:00+05:30"

        circular_id = hashlib.md5(f"nse_{url}".encode()).hexdigest()[:16]

        if dry_run:
            print(f"  [DRY RUN] {prefix}{num}.{ext}")
        elif write_stub(circular_id, title, pub_date, url, url):
            created += 1

    print(f"Created: {created}")
    return created


def main():
    parser = argparse.ArgumentParser(description="Backfill NSE circulars")
    parser.add_argument("--from-date", required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--to-date", required=True, help="End date (YYYY-MM-DD)")
    parser.add_argument("--enumerate", action="store_true", help="Use URL enumeration instead of API")
    parser.add_argument("--start-num", type=int, help="First circular number (for --enumerate)")
    parser.add_argument("--end-num", type=int, help="Last circular number (for --enumerate)")
    parser.add_argument("--dry-run", action="store_true", help="Don't write files")
    args = parser.parse_args()

    from_date = datetime.strptime(args.from_date, "%Y-%m-%d").date()
    to_date = datetime.strptime(args.to_date, "%Y-%m-%d").date()

    if args.enumerate:
        if not args.start_num or not args.end_num:
            parser.error("--enumerate requires --start-num and --end-num")
        backfill_enumerate(args.start_num, args.end_num, from_date, to_date, args.dry_run)
    else:
        backfill_api(from_date, to_date, args.dry_run)


if __name__ == "__main__":
    main()
