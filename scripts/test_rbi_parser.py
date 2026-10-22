#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "httpx",
#     "lxml",
#     "markitdown",
#     "pydantic",
#     "python-frontmatter",
#     "tomli",
# ]
# ///

"""Focused regression tests for RBI RSS ingestion."""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

from config import load_config
from extractors import RSSExtractor
from pipeline import CircularsPipeline


PRESS_RELEASE_FEED = """<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0">
  <channel>
    <title>PRESS RELEASES FROM RBI</title>
    <item>
      <title><![CDATA[Policy update]]></title>
      <description><![CDATA[<p>Policy &amp; liquidity update with operational guidance for regulated entities.</p><table><tr><td>Amount</td><td>2,000 crore</td></tr></table>]]></description>
      <link>https://www.rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid=1</link>
      <pubDate>Mon, 28 Sep 2026 19:05:00</pubDate>
    </item>
  </channel>
</rss>
"""

NOTIFICATION_FEED = """<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0">
  <channel>
    <title>NOTIFICATIONS FROM RBI</title>
    <item>
      <title>Regulatory notification</title>
      <description><![CDATA[<p>This notification contains enough regulatory content for processing by the pipeline.</p>]]></description>
      <link>https://www.rbi.org.in/scripts/NotificationUser.aspx?Id=2&amp;Mode=0</link>
      <pubDate>Mon, 28 Sep 2026 18:05:00</pubDate>
    </item>
  </channel>
</rss>
"""


class RBIExtractorTests(unittest.TestCase):
    def test_configures_both_official_feeds(self):
        self.assertEqual(
            load_config()["rss_feeds"]["rbi"],
            [
                "https://rbi.org.in/pressreleases_rss.xml",
                "https://rbi.org.in/notifications_rss.xml",
            ],
        )

    def test_parses_embedded_press_release_content(self):
        item = RSSExtractor().parse_rss_feed(PRESS_RELEASE_FEED, "rbi")[0]

        self.assertEqual(item["feed_type"], "press-release")
        self.assertEqual(item["guid"], item["download_url"])
        self.assertIn("Policy & liquidity update", item["content"])
        self.assertIn("Amount 2,000 crore", item["content"])

    def test_classifies_notification_feed(self):
        item = RSSExtractor().parse_rss_feed(NOTIFICATION_FEED, "rbi")[0]

        self.assertEqual(item["feed_type"], "notification")
        self.assertIn("regulatory content", item["content"])


class RBIPipelineTests(unittest.IsolatedAsyncioTestCase):
    async def test_aggregates_both_rbi_feeds(self):
        pipeline = object.__new__(CircularsPipeline)
        pipeline.rss_feeds = {"rbi": ["press", "notifications"]}
        pipeline.log = MagicMock()
        pipeline.rss_extractor = MagicMock()
        pipeline.rss_extractor.download_rss_feed = AsyncMock(
            side_effect=[PRESS_RELEASE_FEED, NOTIFICATION_FEED]
        )
        real_extractor = RSSExtractor()
        pipeline.rss_extractor.parse_rss_feed.side_effect = real_extractor.parse_rss_feed
        pipeline.frontmatter_manager = MagicMock()
        pipeline.frontmatter_manager.is_processed.return_value = False

        with tempfile.TemporaryDirectory() as temp_dir:
            pipeline.frontmatter_manager.generate_content_path.return_value = Path(temp_dir) / "item.md"
            pipeline.process_item_with_semaphore = AsyncMock(return_value=True)

            stats = await pipeline.process_source("rbi")

        self.assertEqual(stats.total_items, 2)
        self.assertEqual(stats.completed_items, 2)
        self.assertEqual(pipeline.rss_extractor.download_rss_feed.await_count, 2)
        feed_types = {
            call.args[1]["feed_type"]
            for call in pipeline.process_item_with_semaphore.await_args_list
        }
        self.assertEqual(feed_types, {"press-release", "notification"})

    async def test_processes_embedded_content_without_downloading_page(self):
        pipeline = object.__new__(CircularsPipeline)
        pipeline.log = MagicMock()
        pipeline.frontmatter_manager = MagicMock()
        pipeline.frontmatter_manager.generate_content_path.return_value = Path("/tmp/rbi-item.md")
        pipeline.frontmatter_manager.get_content_hash.return_value = "content-hash"
        pipeline.frontmatter_manager.create_processing_state.return_value = {
            "status": "published",
            "stage": "completed",
        }
        pipeline.frontmatter_manager.write_content_file.return_value = True
        pipeline.gemini_processor = MagicMock()
        pipeline.gemini_processor.run_gemini = AsyncMock(return_value="---\ntitle: RBI item\n---\nSummary")
        pipeline.text_extractor = MagicMock()
        pipeline.text_extractor.extract_html_text = AsyncMock()
        pipeline.file_downloader = MagicMock()
        pipeline.file_downloader.download_temp_file = AsyncMock()

        item = RSSExtractor().parse_rss_feed(PRESS_RELEASE_FEED, "rbi")[0]
        success = await pipeline.process_item_content_based("rbi", item)

        self.assertTrue(success)
        pipeline.file_downloader.download_temp_file.assert_not_awaited()
        pipeline.text_extractor.extract_html_text.assert_not_awaited()
        gemini_content, metadata, _ = pipeline.gemini_processor.run_gemini.await_args.args
        self.assertIn("Policy & liquidity update", gemini_content)
        self.assertEqual(metadata["feed_type"], "press-release")
        self.assertNotIn("pdf_url", metadata)
        self.assertEqual(metadata["rss_url"], item["download_url"])


if __name__ == "__main__":
    unittest.main()
