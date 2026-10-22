#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx", "lxml", "markitdown", "pydantic", "python-frontmatter", "tomli"]
# ///

import tempfile
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

from config import load_config
from extractors import RSSExtractor, PDFURLExtractor
from frontmatter_manager import FrontmatterManager
from pipeline import CircularsPipeline, parse_rss_date

from indiainx import CIRCULARS_URL, parse_indiainx_circulars

SOURCE = 'indiainx'
ROW = """<tr><td>October 01,2026</td><td>20261001-6</td>
<td><a href="../circulars/20261001-6/20261001-6.pdf"> Fund <b>balance</b> &amp; confirmation </a></td>
<td>ALL</td><td>Regulatory and Compliance</td><td>ALL</td></tr>"""
PAGE = '<html><table><tr><th>Date</th><th>Circular</th></tr>'+ROW+'</table></html>'


def sample_item():
    return parse_indiainx_circulars(PAGE)[0]


class ParserTests(unittest.TestCase):
    def test_html_source_configured(self):
        self.assertEqual(load_config()['html_sources'][SOURCE], CIRCULARS_URL)
        self.assertNotIn(SOURCE, load_config()['rss_feeds'])

    def test_row_fields_and_date(self):
        item = sample_item()
        self.assertEqual(item['title'], 'Fund balance & confirmation')
        self.assertEqual(item['guid'], '20261001-6')
        self.assertEqual(item['download_url'], 'https://www.indiainx.com/circulars/20261001-6/20261001-6.pdf')
        self.assertEqual(parse_rss_date(item['pubdate']), '2026-10-01T00:00:00+05:30')
        self.assertEqual(item['segment'], 'ALL')
        self.assertEqual(item['exchange_category'], 'Regulatory and Compliance')
        self.assertEqual(item['product'], 'ALL')

    def test_windows_paths_and_spaced_comma(self):
        page = PAGE.replace('../circulars/', '..\\circulars\\').replace('01,2026', '01, 2026')
        self.assertEqual(parse_indiainx_circulars(page)[0]['download_url'], sample_item()['download_url'])

    def test_duplicates_and_bad_rows_do_not_discard_valid_rows(self):
        bad = ROW.replace('October 01,2026', 'bad date').replace('20261001-6', '20261001-7')
        items = parse_indiainx_circulars('<table>'+bad+ROW+ROW+'</table>')
        self.assertEqual(len(items), 1)

    def test_block_page_and_empty_listing_report_failure(self):
        for page in ('<html>Access denied</html>', '<table><tr><td>No records</td></tr></table>', PAGE.replace('../circulars/20261001-6/20261001-6.pdf', 'javascript:void(0)')):
            with self.subTest(page=page):
                with self.assertRaises(ValueError):
                    parse_indiainx_circulars(page)


class ListingTests(unittest.IsolatedAsyncioTestCase):
    async def test_listing_uses_html_and_honors_max_items(self):
        pipeline = object.__new__(CircularsPipeline)
        pipeline.html_sources = {SOURCE: CIRCULARS_URL}
        pipeline.rss_feeds = {}
        pipeline.log = MagicMock()
        pipeline.rss_extractor = MagicMock()
        pipeline.rss_extractor._fetch_with_retry = AsyncMock(return_value=PAGE.replace('</table>', ROW.replace('20261001-6','20261001-5')+'</table>'))
        pipeline.frontmatter_manager = MagicMock()
        pipeline.frontmatter_manager.is_processed.return_value = False
        pipeline.frontmatter_manager.generate_content_path.return_value = Path('/tmp/nonexistent-inx-test.md')
        pipeline.process_item_with_semaphore = AsyncMock(return_value=True)
        stats = await pipeline.process_source(SOURCE, max_items=1)
        self.assertEqual(stats.completed_items, 1)
        pipeline.rss_extractor.download_rss_feed.assert_not_called()
        pipeline.rss_extractor.parse_rss_feed.assert_not_called()
        self.assertEqual(pipeline.rss_extractor._fetch_with_retry.await_args.args[0], CIRCULARS_URL)
        metadata = pipeline.frontmatter_manager.write_state_file.call_args.args[1]
        self.assertEqual(metadata['circular_no'], '20261001-6')


    async def test_download_failure_is_reported(self):
        pipeline = object.__new__(CircularsPipeline)
        pipeline.html_sources = {SOURCE: CIRCULARS_URL}
        pipeline.rss_feeds = {}
        pipeline.log = MagicMock()
        pipeline.rss_extractor = MagicMock()
        pipeline.rss_extractor._fetch_with_retry = AsyncMock(return_value=None)
        with self.assertRaisesRegex(ValueError, 'Failed to download'):
            await pipeline.process_source(SOURCE)


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
            for key in ('circular_no', 'segment', 'exchange_category', 'product'):
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


    async def test_regenerates_from_stored_pdf_after_listing_has_changed(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            pipeline = self.make_pipeline(temp_dir)
            self.assertTrue(await pipeline.process_item_content_based(SOURCE, sample_item()))
            original = list(Path(temp_dir).rglob('*.md'))[0]
            metadata = pipeline.frontmatter_manager.parse_frontmatter(original)
            pdf = Path(temp_dir) / 'retry.pdf'
            pdf.write_bytes(b'%PDF-retry')
            pipeline.file_downloader.download_temp_file.return_value = (pdf, None)
            self.assertTrue(await pipeline.regenerate_item_markdown(metadata['circular_id'], SOURCE))
            regenerated = list(Path(temp_dir).rglob('*.md'))
            self.assertEqual(len(regenerated), 1)
            result = pipeline.frontmatter_manager.parse_frontmatter(regenerated[0])
            self.assertEqual(result['circular_no'], '20261001-6')
            self.assertEqual(result['exchange_category'], 'Regulatory and Compliance')
            self.assertEqual(result['category'], 'guessed')
            self.assertEqual(result['guid'], metadata['guid'])


if __name__ == "__main__":
    unittest.main()
