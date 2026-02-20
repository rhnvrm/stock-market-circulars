#!/usr/bin/env python3
"""
Backfill BSE notices/circulars for a date range.

Scrapes individual notice pages from BSE's DispNoticesNCirculars.aspx endpoint.
Uses binary search to find total notice count per day, then fetches each notice.

Usage:
    python3 scripts/backfill_bse.py --from-date 2026-02-11 --to-date 2026-02-19
    python3 scripts/backfill_bse.py --from-date 2026-02-11 --to-date 2026-02-19 --dry-run
"""

import argparse
import hashlib
import re
import time
import urllib.request
from datetime import date, datetime, timezone, timedelta
from pathlib import Path

IST = timezone(timedelta(hours=5, minutes=30))
CONTENT_DIR = Path("hugo-site/content/circulars")
REQUEST_DELAY = 0.2  # seconds between requests


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
    filename = f'bse-{dt_str}-{circular_id}-{slug}.md'
    out_dir = CONTENT_DIR / "bse" / year
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
source: bse
title: "{title.replace(chr(34), chr(92)+chr(34))}"
---

Processing in progress...'''
    out_path.write_text(content)
    return True


def fetch_bse_notice(date_str, n, totcount=100):
    """Fetch a single BSE notice page and extract metadata."""
    mm, dd, yyyy = date_str[4:6], date_str[6:8], date_str[:4]
    dt = f"{mm}/{dd}/{yyyy}"
    url = (
        f"https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx"
        f"?noticeno={date_str}-{n}&dt={dt}&icount={n}&totcount={totcount}&flag=0"
    )
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

    with urllib.request.urlopen(req, timeout=15) as resp:
        content = resp.read().decode('utf-8', errors='ignore')

    # Extract subject
    subj_match = re.search(
        r'id="ContentPlaceHolder1_tc31"[^>]*>(.*?)</td>', content, re.DOTALL
    )
    subject = re.sub(r'<[^>]+>', '', subj_match.group(1)).strip() if subj_match else ""

    # Extract attachment link
    attach = re.search(
        r'id="ContentPlaceHolder1_lnkAttchment"[^>]*href="([^"]*)"', content
    )

    guid_url = (
        f"https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx"
        f"?noticeno={date_str}-{n}&dt={dt}"
    )

    return {
        'subject': subject,
        'attachment': attach.group(1) if attach else guid_url,
        'guid': guid_url,
        'has_content': bool(subject),
    }


def find_notice_count(date_str):
    """Binary search for total number of notices on a given date."""
    lo, hi = 1, 200
    while lo < hi:
        mid = (lo + hi + 1) // 2
        try:
            info = fetch_bse_notice(date_str, mid)
            if info['has_content']:
                lo = mid
            else:
                hi = mid - 1
        except Exception:
            hi = mid - 1

    # Verify lo=1 has content
    if lo == 1:
        try:
            info = fetch_bse_notice(date_str, 1)
            if not info['has_content']:
                return 0
        except Exception:
            return 0
    return lo


def backfill(from_date, to_date, dry_run=False):
    """Backfill BSE notices for a date range."""
    total_created = 0
    current = from_date

    while current <= to_date:
        # Skip weekends
        if current.weekday() >= 5:
            print(f"  {current} ({current.strftime('%A')}): skipped (weekend)")
            current += timedelta(days=1)
            continue

        date_str = current.strftime("%Y%m%d")
        count = find_notice_count(date_str)
        print(f"  {current} ({current.strftime('%A')}): {count} notices", end="", flush=True)

        day_created = 0
        for n in range(1, count + 1):
            try:
                info = fetch_bse_notice(date_str, n, count)
                if not info['has_content']:
                    continue

                pub_date = f"{current.isoformat()}T00:00:00+05:30"
                circular_id = hashlib.md5(f"bse_{info['guid']}".encode()).hexdigest()[:16]

                if dry_run:
                    day_created += 1
                elif write_stub(circular_id, info['subject'], pub_date, info['guid'], info['attachment']):
                    day_created += 1

                time.sleep(REQUEST_DELAY)
            except Exception as e:
                print(f" (error on #{n}: {e})", end="")

        total_created += day_created
        print(f" -> {day_created} {'would be ' if dry_run else ''}created")
        current += timedelta(days=1)

    print(f"\nTotal: {total_created}")
    return total_created


def main():
    parser = argparse.ArgumentParser(description="Backfill BSE notices")
    parser.add_argument("--from-date", required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--to-date", required=True, help="End date (YYYY-MM-DD)")
    parser.add_argument("--dry-run", action="store_true", help="Don't write files")
    args = parser.parse_args()

    from_date = datetime.strptime(args.from_date, "%Y-%m-%d").date()
    to_date = datetime.strptime(args.to_date, "%Y-%m-%d").date()

    backfill(from_date, to_date, args.dry_run)


if __name__ == "__main__":
    main()
