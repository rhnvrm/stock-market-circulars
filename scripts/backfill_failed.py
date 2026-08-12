#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter",
#     "typer",
# ]
# ///

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import List, Optional, Tuple

import frontmatter
import typer

app = typer.Typer()

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "hugo-site" / "content" / "circulars"
VALID_STAGES = {"claude_failed", "ai_failed"}
VALID_SOURCES = {"nse", "bse", "sebi"}
BACKFILL_COOLDOWN_DAYS = 7


def parse_timestamp(value: str) -> Optional[datetime]:
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except Exception:
        return None


def extract_sort_key(post, md_file: Path) -> Tuple[str, str]:
    published_date = post.metadata.get("published_date") or ""
    parsed = parse_timestamp(str(published_date))
    normalized = parsed.isoformat() if parsed else ""
    return (normalized, md_file.name)


def should_skip_for_cooldown(processing: dict) -> tuple[bool, str]:
    retry_source = processing.get("retry_source")
    if retry_source != "backfill":
        return False, ""

    last_updated = parse_timestamp(str(processing.get("last_updated") or processing.get("processed_at") or ""))
    if not last_updated:
        return False, ""

    if last_updated.tzinfo is None:
        last_updated = last_updated.replace(tzinfo=timezone.utc)

    cutoff = datetime.now(timezone.utc) - timedelta(days=BACKFILL_COOLDOWN_DAYS)
    if last_updated >= cutoff:
        return True, (
            f"skip cooldown: retried via backfill at {last_updated.isoformat()} "
            f"which is newer than {BACKFILL_COOLDOWN_DAYS} days"
        )

    return False, ""


def collect_failed_items(source: Optional[str], stages: List[str], verbose: bool = False) -> List[str]:
    items: List[Tuple[Tuple[str, str], str]] = []
    chosen_stages = set(stages) if stages else VALID_STAGES

    for md_file in CONTENT_DIR.rglob("*.md"):
        try:
            post = frontmatter.load(md_file)
        except Exception:
            continue

        post_source = post.metadata.get("source")
        if source and post_source != source:
            continue

        processing = post.metadata.get("processing", {})
        stage = processing.get("stage")
        if stage not in chosen_stages:
            continue

        skip, reason = should_skip_for_cooldown(processing)
        if skip:
            if verbose:
                circular_id = post.metadata.get("circular_id") or md_file.name
                print(f"SKIP {circular_id} - {reason}")
            continue

        circular_id = post.metadata.get("circular_id")
        if not circular_id:
            continue

        items.append((extract_sort_key(post, md_file), circular_id))

    items.sort(reverse=True)
    return [circular_id for _, circular_id in items]


@app.command()
def list_ids(
    source: Optional[str] = typer.Option(None, "--source", help="Filter source: nse, bse, sebi"),
    stage: List[str] = typer.Option([], "--stage", help="Failure stages to include: claude_failed, ai_failed"),
    offset: int = typer.Option(0, "--offset", min=0),
    limit: Optional[int] = typer.Option(None, "--limit", min=1, help="Max items to return. Omit to return all eligible items."),
    verbose: bool = typer.Option(False, "--verbose", help="Log skipped items and selection decisions"),
):
    if source and source not in VALID_SOURCES:
        raise typer.BadParameter(f"Invalid source: {source}")
    if any(s not in VALID_STAGES for s in stage):
        raise typer.BadParameter(f"Invalid stage filter: {stage}")

    items = collect_failed_items(source, stage, verbose=verbose)
    selected = items[offset:] if limit is None else items[offset: offset + limit]
    for item in selected:
        print(item)


@app.command()
def count(
    source: Optional[str] = typer.Option(None, "--source", help="Filter source: nse, bse, sebi"),
    stage: List[str] = typer.Option([], "--stage", help="Failure stages to include: claude_failed, ai_failed"),
    verbose: bool = typer.Option(False, "--verbose", help="Log skipped items and selection decisions"),
):
    if source and source not in VALID_SOURCES:
        raise typer.BadParameter(f"Invalid source: {source}")
    if any(s not in VALID_STAGES for s in stage):
        raise typer.BadParameter(f"Invalid stage filter: {stage}")

    items = collect_failed_items(source, stage, verbose=verbose)
    print(len(items))


if __name__ == "__main__":
    app()
