#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx", "lxml", "markitdown", "pydantic", "python-frontmatter", "tomli"]
# ///

import tempfile
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

from config import load_config
from extractors import RSSExtractor, PDFURLExtractor
from frontmatter_manager import FrontmatterManager
from pipeline import CircularsPipeline, parse_rss_date

from msei import parse_msei_feed

SOURCE = 'msei'
FEED = """<rss><channel><item>
<title><![CDATA[Trading &amp; settlement]]></title>
<link>https://www.msei.in/SX-Content/Circulars/2026/October/Circular-19806.pdf</link>
<pubDate>05-Oct-2026</pubDate>
</item></channel></rss>"""


def sample_item():
    return RSSExtractor().parse_rss_feed(FEED, SOURCE)[0]


class ParserTests(unittest.TestCase):
    def test_official_feed_configured(self):
        self.assertEqual(load_config()['rss_feeds'][SOURCE], 'https://www.msei.in/rss/rss?type=circular')

    def test_direct_pdf_without_guid(self):
        item = sample_item()
        self.assertEqual(item['title'], 'Trading & settlement')
        self.assertEqual(item['guid'], item['download_url'])
        self.assertEqual(parse_rss_date(item['pubdate']), '2026-10-05T00:00:00+05:30')

    def test_enclosure_and_duplicate_guids(self):
        entry = '<item><title>Update</title><link>/downloads/circular?id=1</link><guid>notice-1</guid><enclosure url="/SX-Content/Circulars/Circular-1.PDF?download=1"/><pubDate>Mon, 05 Oct 2026 09:00:00 +0530</pubDate></item>'
        items = parse_msei_feed('<rss><channel>'+entry+entry+'</channel></rss>')
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['guid'], 'notice-1')
        self.assertEqual(items[0]['download_url'], 'https://www.msei.in/SX-Content/Circulars/Circular-1.PDF?download=1')
        self.assertEqual(parse_rss_date(items[0]['pubdate']), '2026-10-05T09:00:00+05:30')

    def test_description_pdf_and_missing_link(self):
        items = parse_msei_feed('<rss><channel><item><title>Update</title><description><![CDATA[<a href="/circulars/file.pdf">Download</a>]]></description></item><item><title>Incomplete</title><link/></item></channel></rss>')
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['download_url'], 'https://www.msei.in/circulars/file.pdf')

    def test_empty_and_malformed_feed(self):
        self.assertEqual(RSSExtractor().parse_rss_feed('<html>Blocked</html>', SOURCE), [])
        self.assertEqual(RSSExtractor().parse_rss_feed('broken', SOURCE), [])



class DetailPageTests(unittest.IsolatedAsyncioTestCase):
    async def test_resolves_relative_pdf_on_detail_page(self):
        import httpx
        response = httpx.Response(200, text='<a href="/SX-Content/Circulars/Circular-1.PDF">Circular</a>', request=httpx.Request('GET', 'https://www.msei.in/downloads/notice'))
        client = AsyncMock()
        client.get.return_value = response
        with patch('extractors.httpx.AsyncClient') as factory:
            factory.return_value.__aenter__.return_value = client
            result = await PDFURLExtractor().extract_pdf_url('msei', 'https://www.msei.in/downloads/notice')
        self.assertEqual(result, 'https://www.msei.in/SX-Content/Circulars/Circular-1.PDF')


class PipelineTests(unittest.IsolatedAsyncioTestCase):
    def make_pipeline(self, temp_dir):
        pipeline = object.__new__(CircularsPipeline)
        pipeline.log = MagicMock()
        pipeline.max_concurrent_items = 2
        pipeline.frontmatter_manager = FrontmatterManager(Path(temp_dir), logger=MagicMock())
        pipeline.pdf_extractor = MagicMock()
        pipeline.pdf_extractor.extract_pdf_url = AsyncMock()
        pipeline.file_downloader = MagicMock()
        pdf = Path(temp_dir) / 'download.pdf'
        pdf.write_bytes(b'%PDF-test')
        pipeline.file_downloader.download_temp_file = AsyncMock(return_value=(pdf, None))
        pipeline.text_extractor = MagicMock()
        pipeline.text_extractor.extract_file_text.return_value = 'Circular requirements for regulated members. ' * 5
        pipeline.gemini_processor = MagicMock()
        pipeline.gemini_processor.run_gemini = AsyncMock(return_value='---\ntitle: Summary\ncategory: guessed\n---\nSummary')
        return pipeline

    async def test_downloads_pdf_and_publishes_state(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            pipeline = self.make_pipeline(temp_dir)
            item = sample_item()
            self.assertTrue(await pipeline.process_item_content_based(SOURCE, item))
            pipeline.file_downloader.download_temp_file.assert_awaited_once()
            self.assertEqual(pipeline.file_downloader.download_temp_file.await_args.args[0], item['download_url'])
            pipeline.pdf_extractor.extract_pdf_url.assert_not_awaited()
            files = list(Path(temp_dir).rglob('*.md'))
            self.assertEqual(len(files), 1)
            metadata = pipeline.frontmatter_manager.parse_frontmatter(files[0])
            self.assertEqual(metadata['source'], SOURCE)
            self.assertEqual(metadata['guid'], item['guid'])
            self.assertFalse(metadata['draft'])
            self.assertEqual(metadata['processing']['status'], 'published')
            for key in ('circular_no', 'segment', 'category', 'product'):
                if key in item:
                    self.assertEqual(metadata[key], item[key])
            self.assertTrue(pipeline.frontmatter_manager.is_processed(metadata['circular_id'], SOURCE))

    async def test_pdf_download_failure_does_not_publish(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            pipeline = self.make_pipeline(temp_dir)
            pipeline.file_downloader.download_temp_file.return_value = (None, '404')
            self.assertFalse(await pipeline.process_item_content_based(SOURCE, sample_item()))
            pipeline.gemini_processor.run_gemini.assert_not_awaited()
            files = list(Path(temp_dir).rglob('*.md'))
            metadata = pipeline.frontmatter_manager.parse_frontmatter(files[0])
            self.assertTrue(metadata['draft'])
            self.assertEqual(metadata['processing']['stage'], 'download_failed')


if __name__ == "__main__":
    unittest.main()
