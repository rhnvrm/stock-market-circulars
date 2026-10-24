"""MCX circular RSS normalization for the document processing pipeline."""

from datetime import datetime, timedelta, timezone
from html import unescape
from urllib.parse import urljoin, urlsplit

from lxml import etree, html

SITE_URL = "https://www.mcxindia.com/"
FEED_BASE = SITE_URL + "en/rssfeed/circulars/"
CIRCULAR_CATEGORIES = ("ctcl", "membership-and-compliance", "ddr", "c-s", "legal", "general", "tech", "t-s")
FEED_URLS = [FEED_BASE + category for category in CIRCULAR_CATEGORIES]  # mirrored in config/config.toml
IST = timezone(timedelta(hours=5, minutes=30))

# MCX pubDate is "Wednesday, October 14, 2026" (not RFC 822). The feeds carry no
# guid and the <link> is a relative path to the PDF (one 2013 legal item is a .zip).
DATE_FORMATS = ("%A, %B %d, %Y", "%d-%b-%Y", "%d %b %Y", "%d/%m/%Y", "%B %d, %Y", "%b %d, %Y")


def normalize_date(value):
    """Accept MCX's weekday-prefixed date; leave standard RSS dates intact."""
    value = value.strip()
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(value, fmt).replace(tzinfo=IST).isoformat()
        except ValueError:
            continue
    return value


def parse_mcx_feed(content):
    """Resolve relative document links; the absolute link is the stable identity."""
    if isinstance(content, str):
        content = content.encode()
    root = etree.fromstring(content, parser=etree.XMLParser(resolve_entities=False, no_network=True))
    items = []
    seen = set()
    for entry in root.xpath('.//item'):
        # c-s and t-s feeds double-escape ampersands (&amp;amp;), so unescape once more.
        title = unescape((entry.findtext('title') or '').strip())
        link = (entry.findtext('link') or '').strip()
        description = entry.findtext('description') or ''
        candidates = [link]
        candidates += [e.get('url', '') for e in entry.findall('enclosure')]
        if description:
            try:
                fragment = html.fragment_fromstring(unescape(description), create_parent='div')
                candidates += fragment.xpath('.//a/@href')
            except (etree.ParserError, ValueError):
                pass
        urls = [urljoin(SITE_URL, value.strip().replace('\\', '/')) for value in candidates if value.strip()]
        urls = [url for url in urls if urlsplit(url).scheme in ('http', 'https')]
        pdf_urls = [url for url in urls if urlsplit(url).path.lower().endswith('.pdf')]
        download_url = next(iter(pdf_urls or urls), '')
        if not title or not download_url:
            continue
        guid = (entry.findtext('guid') or '').strip() or download_url
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
