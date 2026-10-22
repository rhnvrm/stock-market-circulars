"""MSEI circular RSS normalization for the document processing pipeline."""

from datetime import datetime, timedelta, timezone
from html import unescape
from urllib.parse import urljoin, urlsplit

from lxml import etree, html

FEED_URL = "https://www.msei.in/rss/rss?type=circular"
IST = timezone(timedelta(hours=5, minutes=30))


def normalize_date(value):
    """Accept the date-only forms used by MSEI; leave standard RSS dates intact."""
    value = value.strip()
    for fmt in ("%d-%b-%Y", "%d %b %Y", "%d/%m/%Y", "%B %d, %Y", "%b %d, %Y"):
        try:
            return datetime.strptime(value, fmt).replace(tzinfo=IST).isoformat()
        except ValueError:
            continue
    return value


def parse_msei_feed(content):
    """Normalize PDF links, keeping the publisher's GUID as the stable identity."""
    root = etree.fromstring(content.encode(), parser=etree.XMLParser(resolve_entities=False, no_network=True))
    items = []
    seen = set()
    for entry in root.xpath('.//item'):
        title = unescape((entry.findtext('title') or '').strip())
        link = (entry.findtext('link') or '').strip()
        description = entry.findtext('description') or ''
        candidates = [link]
        candidates += [e.get('url', '') for e in entry.findall('enclosure')]
        if description:
            try:
                fragment = html.fragment_fromstring(description, create_parent='div')
                candidates += fragment.xpath('.//a/@href')
            except (etree.ParserError, ValueError):
                pass
        urls = [urljoin(FEED_URL, value.strip().replace('\\', '/')) for value in candidates if value.strip()]
        urls = [url for url in urls if urlsplit(url).scheme in ('http', 'https')]
        pdf_urls = [url for url in urls if urlsplit(url).path.lower().endswith('.pdf')]
        download_url = next(iter(pdf_urls or urls), '')
        if not title or not download_url:
            continue
        guid = (entry.findtext('guid') or '').strip()
        if not guid:
            guid = urljoin(FEED_URL, link.replace('\\', '/')) if link else download_url
        if guid in seen:
            continue
        seen.add(guid)
        items.append({
            'title': title,
            'download_url': download_url,
            'guid': guid,
            'pubdate': normalize_date(entry.findtext('pubDate') or ''),
        })
    return items
