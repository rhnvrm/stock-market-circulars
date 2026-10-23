#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx", "curl_cffi", "lxml", "markitdown", "pydantic", "python-frontmatter", "tomli"]
# ///

import tempfile
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

from config import load_config
from extractors import RSSExtractor
from pipeline import CircularsPipeline, parse_rss_date
from processors import FileDownloader
from tlsfetch import needs_impersonation

from mcx import FEED_URLS, parse_mcx_feed

SOURCE = 'mcx'
SLUGS = ['ctcl', 'membership-and-compliance', 'ddr', 'c-s', 'legal', 'general', 'tech', 't-s']
FEED = """<?xml version="1.0" encoding="utf-8"?><rss version="2.0"><channel><title>MCX Exchange Circular (T&amp;amp;S)</title><link>http://mcxindia.com</link><description>x</description>
<item><title>MCX Exchange Circular (T&amp;amp;S) : Availability of New KRA reports on MRS Portal</title><link>/docs/default-source/circulars/english/2026/october/circular---594---2026.pdf</link><description>Tuesday, October 20, 2026</description><pubDate>Tuesday, October 20, 2026</pubDate></item>
<item><title>MCX Exchange Circular (LEGAL) : Reminder Submission Of Annual Returns</title><link>/docs/default-source/circulars/english/2013/november/circular384-2013-zip6fd68a4f.zip</link><description>Saturday, November 16, 2013</description><pubDate>Saturday, November 16, 2013</pubDate></item>
</channel></rss>"""


class ParserTests(unittest.TestCase):
    def test_all_circular_feeds_configured(self):
        feeds = load_config()['rss_feeds'][SOURCE]
        self.assertEqual(feeds, [f'https://www.mcxindia.com/en/rssfeed/circulars/{s}' for s in SLUGS])
        self.assertEqual(feeds, FEED_URLS)

    def test_relative_pdf_link_without_guid(self):
        item = RSSExtractor().parse_rss_feed(FEED, SOURCE)[0]
        self.assertEqual(item['download_url'], 'https://www.mcxindia.com/docs/default-source/circulars/english/2026/october/circular---594---2026.pdf')
        self.assertEqual(item['guid'], item['download_url'])
        self.assertEqual(parse_rss_date(item['pubdate']), '2026-10-20T00:00:00+05:30')

    def test_double_escaped_ampersand(self):
        self.assertIn('(T&S)', parse_mcx_feed(FEED)[0]['title'])

    def test_zip_item_is_kept(self):
        item = parse_mcx_feed(FEED)[1]
        self.assertTrue(item['download_url'].endswith('.zip'))
        self.assertEqual(parse_rss_date(item['pubdate']), '2013-11-16T00:00:00+05:30')

    def test_duplicate_and_incomplete_items(self):
        entry = '<item><title>A</title><link>/docs/a.pdf</link><pubDate>Monday, October 05, 2026</pubDate></item>'
        items = parse_mcx_feed('<rss><channel>' + entry + entry + '<item><title>No link</title><link/></item></channel></rss>')
        self.assertEqual(len(items), 1)

    def test_blocked_and_malformed_feed(self):
        self.assertEqual(RSSExtractor().parse_rss_feed('<html>Access Denied</html>', SOURCE), [])
        self.assertEqual(RSSExtractor().parse_rss_feed('broken', SOURCE), [])


class FetchRoutingTests(unittest.IsolatedAsyncioTestCase):
    def test_only_mcx_uses_browser_tls(self):
        self.assertTrue(needs_impersonation('https://www.mcxindia.com/en/rssfeed/circulars/ctcl'))
        self.assertFalse(needs_impersonation('https://www.msei.in/rss/rss?type=circular'))
        self.assertFalse(needs_impersonation('https://notmcxindia.com/x.pdf'))

    async def test_feed_fetch_uses_curl_cffi(self):
        with patch('extractors.fetch_text', new=AsyncMock(return_value=FEED)) as fetch:
            content = await RSSExtractor()._fetch_with_retry('https://www.mcxindia.com/en/rssfeed/circulars/tech', {})
        self.assertEqual(content, FEED)
        fetch.assert_awaited_once()

    async def test_document_download_uses_curl_cffi(self):
        async def fake_download(url, path, timeout):
            Path(path).write_bytes(b'%PDF-1.4 test')
            return ''
        with tempfile.TemporaryDirectory() as tmp, patch('processors.download_file', new=fake_download), \
                patch('processors.httpx.AsyncClient', side_effect=AssertionError('httpx must not be used for MCX')):
            path, error = await FileDownloader(attachment_dir=tmp).download_temp_file('https://www.mcxindia.com/docs/a.pdf', 'id')
            self.assertIsNone(error)
            self.assertTrue(path.read_bytes().startswith(b'%PDF'))


class PipelineTests(unittest.IsolatedAsyncioTestCase):
    async def test_categories_deduplicate_by_document_url(self):
        pipeline = object.__new__(CircularsPipeline)
        pipeline.rss_feeds = {SOURCE: FEED_URLS}
        pipeline.rss_extractor = RSSExtractor()
        pipeline.rss_extractor.download_rss_feed = AsyncMock(return_value=FEED)
        pipeline.log = MagicMock()
        items = await pipeline._fetch_source_items(SOURCE)
        self.assertEqual(len(items), 2)
        self.assertEqual(pipeline.rss_extractor.download_rss_feed.await_count, 8)

    async def test_pdf_reaches_published_state(self):
        from test_msei_parser import PipelineTests as MSEIPipelineTests
        with tempfile.TemporaryDirectory() as tmp:
            pipeline = MSEIPipelineTests().make_pipeline(tmp)
            item = parse_mcx_feed(FEED)[0]
            self.assertTrue(await pipeline.process_item_content_based(SOURCE, item))
            pipeline.pdf_extractor.extract_pdf_url.assert_not_awaited()
            metadata = pipeline.frontmatter_manager.parse_frontmatter(next(Path(tmp).rglob('*.md')))
            self.assertEqual(metadata['source'], SOURCE)
            self.assertEqual(metadata['guid'], item['download_url'])
            self.assertEqual(metadata['processing']['status'], 'published')


if __name__ == '__main__':
    unittest.main()
