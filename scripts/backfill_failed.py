#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter",
#     "typer",
# ]
# ///

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import List, Optional, Tuple

import frontmatter
import typer

app = typer.Typer()

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "hugo-site" / "content" / "circulars"
VALID_STAGES = {"claude_failed", "ai_failed"}
VALID_SOURCES = {"nse", "bse", "sebi"}


def extract_sort_key(post, md_file: Path) -> Tuple[str, str]:
    published_date = post.metadata.get("published_date") or ""
    try:
        normalized = datetime.fromisoformat(str(published_date).replace("Z", "+00:00")).isoformat()
    except Exception:
        normalized = ""
    return (normalized, md_file.name)


def collect_failed_items(source: Optional[str], stages: List[str]) -> List[str]:
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

        stage = post.metadata.get("processing", {}).get("stage")
        if stage not in chosen_stages:
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
    limit: int = typer.Option(50, "--limit", min=1),
):
    if source and source not in VALID_SOURCES:
        raise typer.BadParameter(f"Invalid source: {source}")
    if any(s not in VALID_STAGES for s in stage):
        raise typer.BadParameter(f"Invalid stage filter: {stage}")

    items = collect_failed_items(source, stage)
    selected = items[offset: offset + limit]
    for item in selected:
        print(item)


@app.command()
def count(
    source: Optional[str] = typer.Option(None, "--source", help="Filter source: nse, bse, sebi"),
    stage: List[str] = typer.Option([], "--stage", help="Failure stages to include: claude_failed, ai_failed"),
):
    if source and source not in VALID_SOURCES:
        raise typer.BadParameter(f"Invalid source: {source}")
    if any(s not in VALID_STAGES for s in stage):
        raise typer.BadParameter(f"Invalid stage filter: {stage}")

    items = collect_failed_items(source, stage)
    print(len(items))


if __name__ == "__main__":
    app()
