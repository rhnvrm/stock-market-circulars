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
from processors import FileDownloader, GeminiProcessor


PRESS_RELEASE_FEED = """<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0">
  <channel>
    <title>PRESS RELEASES FROM RBI</title>
    <item>
      <title><![CDATA[Policy update]]></title>
      <description><![CDATA[
        <h2>Operational details</h2>
        <p>Policy &amp; liquidity update with operational guidance for regulated entities. See the <a href="/rules/vrrr">VRRR rules</a>.</p>
        <table><tr><th>Metric</th><th>Value</th></tr><tr><td>Amount</td><td>2,000 crore</td></tr></table>
        <img src="/images/formula.png" alt="Auction formula">
      ]]></description>
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
        self.assertIn("## Operational details", item["content"])
        self.assertIn("| Metric | Value |", item["content"])
        self.assertIn("| Amount | 2,000 crore |", item["content"])
        self.assertIn("[VRRR rules](https://www.rbi.org.in/rules/vrrr)", item["content"])
        self.assertIn("![Auction formula](https://www.rbi.org.in/images/formula.png)", item["content"])
        self.assertEqual(item["image_urls"], ["https://www.rbi.org.in/images/formula.png"])

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

            stats = await pipeline.process_source("rbi", max_items=1)

        self.assertEqual(stats.total_items, 2)
        self.assertEqual(stats.completed_items, 2)
        self.assertEqual(pipeline.rss_extractor.download_rss_feed.await_count, 2)
        feed_types = {
            call.args[1]["feed_type"]
            for call in pipeline.process_item_with_semaphore.await_args_list
        }
        self.assertEqual(feed_types, {"press-release", "notification"})

    async def test_processes_embedded_content_and_attaches_images(self):
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
        image_path = Path("/tmp/nonexistent-rbi-formula.png")
        pipeline.file_downloader.download_temp_file = AsyncMock(return_value=(image_path, None))

        item = RSSExtractor().parse_rss_feed(PRESS_RELEASE_FEED, "rbi")[0]
        success = await pipeline.process_item_content_based("rbi", item)

        self.assertTrue(success)
        pipeline.text_extractor.extract_html_text.assert_not_awaited()
        pipeline.file_downloader.download_temp_file.assert_awaited_once()
        image_url = pipeline.file_downloader.download_temp_file.await_args.args[0]
        self.assertEqual(image_url, "https://www.rbi.org.in/images/formula.png")
        self.assertEqual(
            pipeline.file_downloader.download_temp_file.await_args.kwargs["referer"],
            item["download_url"],
        )
        gemini_content, metadata, _ = pipeline.gemini_processor.run_gemini.await_args.args
        self.assertIn("Policy & liquidity update", gemini_content)
        self.assertEqual(metadata["feed_type"], "press-release")
        self.assertNotIn("pdf_url", metadata)
        self.assertEqual(metadata["rss_url"], item["download_url"])
        self.assertIsNone(pipeline.gemini_processor.run_gemini.await_args.kwargs["content_limit"])
        self.assertEqual(pipeline.gemini_processor.run_gemini.await_args.kwargs["attachments"], [image_path])

    async def test_regeneration_refreshes_rbi_feed_content_and_type(self):
        pipeline = object.__new__(CircularsPipeline)
        pipeline.log = MagicMock()
        pipeline.frontmatter_manager = MagicMock()
        pipeline._find_rss_item = AsyncMock()
        pipeline.process_item_content_based = AsyncMock(return_value=True)

        refreshed_item = RSSExtractor().parse_rss_feed(NOTIFICATION_FEED, "rbi")[0]
        pipeline._find_rss_item.return_value = refreshed_item

        with tempfile.TemporaryDirectory() as temp_dir:
            content_path = Path(temp_dir) / "rbi-item.md"
            content_path.write_text("existing content", encoding="utf-8")
            pipeline.frontmatter_manager.find_files_by_circular_id.side_effect = [
                [content_path],
                [],
            ]
            pipeline.frontmatter_manager.parse_frontmatter.return_value = {
                "source": "rbi",
                "guid": refreshed_item["guid"],
                "title": "Old title",
                "rss_url": refreshed_item["download_url"],
                "published_date": refreshed_item["pubdate"],
                "feed_type": "notification",
                "processing": {"stage": "ai_failed"},
            }

            success = await pipeline.regenerate_item_markdown("circular-id", "rbi")

        self.assertTrue(success)
        pipeline._find_rss_item.assert_awaited_once_with("rbi", refreshed_item["guid"])
        source, regenerated_item = pipeline.process_item_content_based.await_args.args
        self.assertEqual(source, "rbi")
        self.assertEqual(regenerated_item["content"], refreshed_item["content"])
        self.assertEqual(regenerated_item["feed_type"], "notification")


class GeminiProcessorTests(unittest.IsolatedAsyncioTestCase):
    async def test_unlimited_content_keeps_the_full_rbi_notification(self):
        processor = GeminiProcessor(
            gemini_delay=0,
            max_gemini_calls=1,
            prompts={"gemini_analysis": "CONTENT:\n$content"},
        )
        captured = {}

        async def capture_attachment(prompt, item_id):
            attachment_path = Path(prompt.splitlines()[0].removeprefix("@"))
            captured["path"] = attachment_path
            captured["content"] = attachment_path.read_text(encoding="utf-8")
            captured["prompt"] = prompt
            return None

        processor._run_gemini_with_retry = AsyncMock(side_effect=capture_attachment)
        long_content = "start\n" + ("regulatory requirement\n" * 3_000) + "final operative clause"

        await processor.run_gemini(
            long_content,
            {"source": "rbi", "title": "Long notification"},
            "item-id",
            content_limit=None,
        )

        self.assertEqual(captured["content"], long_content)
        self.assertIn("The complete source document is attached", captured["prompt"])
        self.assertNotIn("final operative clause", captured["prompt"])
        self.assertLess(len(captured["prompt"]), 4000)
        self.assertFalse(captured["path"].exists())


class FileDownloaderTests(unittest.TestCase):
    def test_accepts_png_image_attachments(self):
        with tempfile.NamedTemporaryFile() as image_file:
            image_file.write(b"\x89PNG\r\n\x1a\n" + (b"\x00" * 16))
            image_file.flush()

            self.assertEqual(
                FileDownloader()._validate_file_type(Path(image_file.name)),
                (True, "png"),
            )


if __name__ == "__main__":
    unittest.main()
