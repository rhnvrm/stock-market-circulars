#!/usr/bin/env python3
"""
Backfill SEBI circulars/orders for a date range.

Two strategies:
1. RSS-based: Fetches from SEBI RSS feed (rolling window of ~4 days)
2. Listing-based: Scrapes paginated listing pages across SEBI sections

SEBI items have sequential IDs in URLs (e.g., _99700.html). When using
listing-based backfill, dates are estimated from the ID range since SEBI
listing pages don't expose dates directly.

Usage:
    # RSS-based (recent dates only)
    python3 scripts/backfill_sebi.py --from-date 2026-02-17 --to-date 2026-02-19 --rss

    # Listing-based (for older dates)
    python3 scripts/backfill_sebi.py --from-date 2026-02-10 --to-date 2026-02-16 \
        --start-id 99646 --end-id 99832

    # Dry run
    python3 scripts/backfill_sebi.py --from-date 2026-02-10 --to-date 2026-02-16 \
        --start-id 99646 --end-id 99832 --dry-run

Figuring out the ID range:
    Look at existing SEBI content files around your gap dates. The guid field
    contains the SEBI URL with the ID: .../some-title_99645.html
    Use the last ID before your gap as start-id and the first ID after as end-id.
"""

import argparse
import hashlib
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime, timezone, timedelta
from pathlib import Path

IST = timezone(timedelta(hours=5, minutes=30))
CONTENT_DIR = Path("hugo-site/content/circulars")

MONTH_NAMES = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12,
}

# SEBI website section IDs for listing pages
# (sid, ssid) pairs that cover different content types
SEBI_SECTIONS = [
    (1, 0),   # Legal - all
    (1, 7),   # Legal - circulars
    (2, 0),   # Media - all
    (2, 9),   # Media - enforcement/recovery (bulk of items)
    (3, 0),   # Filings - all
    (4, 0),   # Reports - all
    (5, 0),   # Enforcement - all
]


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
    filename = f'sebi-{dt_str}-{circular_id}-{slug}.md'
    out_dir = CONTENT_DIR / "sebi" / year
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
source: sebi
title: "{title.replace(chr(34), chr(92)+chr(34))}"
---

Processing in progress...'''
    out_path.write_text(content)
    return True


def parse_sebi_date(pubdate):
    """Parse SEBI's non-standard date format: '20 Feb, 2026 +0530'."""
    m = re.match(r'(\d+)\s+(\w+),?\s+(\d{4})\s+([+-]\d{4})', pubdate.strip())
    if m:
        day, month_str, year, _ = m.groups()
        month = MONTH_NAMES.get(month_str, 1)
        return f'{year}-{month:02d}-{int(day):02d}T00:00:00+05:30'
    return None


def backfill_rss(from_date, to_date, dry_run=False):
    """Fetch from SEBI RSS feed (rolling window of ~4 days)."""
    print("Fetching SEBI RSS feed...")
    req = urllib.request.Request(
        "https://www.sebi.gov.in/sebirss.xml",
        headers={"User-Agent": "Mozilla/5.0"}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        xml_content = resp.read().decode()

    root = ET.fromstring(xml_content)
    items = root.findall('.//item')
    print(f"RSS has {len(items)} items")

    created, skipped = 0, 0
    for item in items:
        title = item.findtext('title', '').strip()
        link = item.findtext('link', '').strip()
        pubdate = item.findtext('pubDate', '').strip()

        pub_date = parse_sebi_date(pubdate)
        if not pub_date:
            skipped += 1
            continue

        item_date = datetime.strptime(pub_date[:10], "%Y-%m-%d").date()
        if item_date < from_date or item_date > to_date:
            skipped += 1
            continue

        circular_id = hashlib.md5(f"sebi_{link}".encode()).hexdigest()[:16]

        if dry_run:
            print(f"  [DRY RUN] {pub_date[:10]} {title[:60]}")
            created += 1
        elif write_stub(circular_id, title, pub_date, link, link):
            created += 1
        else:
            skipped += 1

    print(f"Created: {created}, Skipped: {skipped}")
    return created


def backfill_listings(from_date, to_date, start_id, end_id, dry_run=False):
    """Scrape SEBI paginated listing pages to find items in the ID range."""
    print(f"Scanning SEBI listings for IDs {start_id}-{end_id}")

    all_items = {}

    for sid, ssid in SEBI_SECTIONS:
        for page in range(1, 100):
            url = (
                f"https://www.sebi.gov.in/sebiweb/home/HomeAction.do"
                f"?doListing=yes&sid={sid}&ssid={ssid}&smession=No"
            )
            if page > 1:
                url += f"&page={page}"

            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            try:
                with urllib.request.urlopen(req, timeout=15) as resp:
                    content = resp.read().decode('utf-8', errors='ignore')

                links = re.findall(
                    r'href="(https://www.sebi.gov.in/[^"]*_(\d+)\.html)"', content
                )
                if not links:
                    break

                min_page_id = min(int(i) for _, i in links)

                for full_url, item_id in links:
                    iid = int(item_id)
                    if start_id <= iid <= end_id and iid not in all_items:
                        # Extract title from URL path
                        path_part = full_url.split('/')[-1].replace('.html', '')
                        path_part = path_part.rsplit('_', 1)[0]
                        title = path_part.replace('-', ' ').strip()
                        title = ' '.join(
                            w.capitalize() if len(w) > 3 else w
                            for w in title.split()
                        )
                        all_items[iid] = {'url': full_url, 'title': title[:150]}

                # Stop if we're past the range
                if min_page_id < start_id - 100:
                    break
            except Exception:
                break

    print(f"Found {len(all_items)} unique items")

    # Distribute dates proportionally across the ID range
    total_days = (to_date - from_date).days + 1
    # Only count weekdays
    weekdays = []
    current = from_date
    while current <= to_date:
        if current.weekday() < 5:
            weekdays.append(current)
        current += timedelta(days=1)

    id_range = end_id - start_id + 1
    ids_per_day = id_range / len(weekdays) if weekdays else id_range

    created = 0
    for iid in sorted(all_items.keys()):
        item = all_items[iid]

        # Assign date proportionally
        day_index = min(int((iid - start_id) / ids_per_day), len(weekdays) - 1)
        assigned_date = weekdays[day_index] if weekdays else from_date
        pub_date = f"{assigned_date.isoformat()}T00:00:00+05:30"

        circular_id = hashlib.md5(f"sebi_{item['url']}".encode()).hexdigest()[:16]

        if dry_run:
            print(f"  [DRY RUN] ID {iid} -> {assigned_date} {item['title'][:50]}")
            created += 1
        elif write_stub(circular_id, item['title'], pub_date, item['url'], item['url']):
            created += 1

    print(f"Created: {created}")
    return created


def main():
    parser = argparse.ArgumentParser(description="Backfill SEBI circulars")
    parser.add_argument("--from-date", required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--to-date", required=True, help="End date (YYYY-MM-DD)")
    parser.add_argument("--rss", action="store_true", help="Use RSS feed (recent dates only)")
    parser.add_argument("--start-id", type=int, help="First SEBI item ID (for listing mode)")
    parser.add_argument("--end-id", type=int, help="Last SEBI item ID (for listing mode)")
    parser.add_argument("--dry-run", action="store_true", help="Don't write files")
    args = parser.parse_args()

    from_date = datetime.strptime(args.from_date, "%Y-%m-%d").date()
    to_date = datetime.strptime(args.to_date, "%Y-%m-%d").date()

    if args.rss:
        backfill_rss(from_date, to_date, args.dry_run)
    else:
        if not args.start_id or not args.end_id:
            parser.error("Listing mode requires --start-id and --end-id")
        backfill_listings(from_date, to_date, args.start_id, args.end_id, args.dry_run)


if __name__ == "__main__":
    main()
