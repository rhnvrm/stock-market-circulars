"""Parse the latest India INX circulars listing (no ASP.NET postbacks)."""

import re
from datetime import datetime, timedelta, timezone
from urllib.parse import urljoin, urlsplit

from lxml import html

CIRCULARS_URL = "https://www.indiainx.com/markets/Circulars.aspx"
IST = timezone(timedelta(hours=5, minutes=30))


def parse_indiainx_circulars(content, page_url=CIRCULARS_URL):
    """Return pipeline items from six-column circular rows, skipping page chrome."""
    doc = html.fromstring(content)
    items = []
    seen = set()
    for row in doc.xpath('//tr'):
        cells = row.xpath('./td')
        if len(cells) < 6:
            continue
        circular_no = ' '.join(cells[1].text_content().split())
        if not re.fullmatch(r'\d{8}-\d+', circular_no):
            continue
        for anchor in cells[2].xpath('.//a[@href]'):
            url = urljoin(page_url, anchor.get('href').strip().replace('\\', '/'))
            parsed = urlsplit(url)
            if parsed.scheme not in ('http', 'https') or '/circulars/' not in parsed.path.lower() or not parsed.path.lower().endswith('.pdf'):
                continue
            title = ' '.join(anchor.text_content().split())
            if not title:
                continue
            date_text = ' '.join(cells[0].text_content().split())
            try:
                date = datetime.strptime(re.sub(r'\s*,\s*', ',', date_text), '%B %d,%Y').replace(tzinfo=IST)
            except ValueError:
                # A bad row must not discard the remaining circulars or get today's date.
                continue
            if circular_no in seen:
                break
            seen.add(circular_no)
            items.append({
                'title': title,
                'download_url': url,
                'guid': circular_no,
                'pubdate': date.isoformat(),
                'circular_no': circular_no,
                'segment': ' '.join(cells[3].text_content().split()),
                'exchange_category': ' '.join(cells[4].text_content().split()),
                'product': ' '.join(cells[5].text_content().split()),
            })
            break
    if not items:
        raise ValueError('No India INX circular rows found; the listing may be empty or its structure may have changed')
    return items
