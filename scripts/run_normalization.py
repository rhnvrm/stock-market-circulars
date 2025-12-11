#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter",
#     "pyyaml",
# ]
# ///
"""
Main CLI runner for normalizing stocks and tags across all circulars.

Usage:
    uv run run_normalization.py --dry-run     # Preview changes
    uv run run_normalization.py               # Apply changes
    uv run run_normalization.py --stocks-only # Only normalize stocks
    uv run run_normalization.py --tags-only   # Only normalize tags
"""

import argparse
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import frontmatter

from normalize_stocks import InstrumentsLookup, normalize_stocks
from normalize_tags import TagRules, normalize_tags


def migrate_scrip_codes_to_stocks(tags: list[str], stocks: list[str]) -> tuple[list[str], list[str]]:
    """
    Migrate 5-6 digit numeric tags to stocks field (they're BSE scrip codes).

    Returns: (new_tags, new_stocks)
    """
    new_tags = []
    migrated = []

    for tag in tags:
        # Check if tag is a 5-6 digit number (BSE scrip code)
        if re.match(r'^\d{5,6}$', tag.strip()):
            migrated.append(tag.strip())
        else:
            new_tags.append(tag)

    # Add migrated scrip codes to stocks
    new_stocks = list(stocks) + migrated if migrated else stocks

    return new_tags, new_stocks


def extract_data_values_from_tags(tags: list[str], metadata: dict) -> tuple[list[str], dict]:
    """
    Extract data value tags to frontmatter fields.

    Patterns extracted:
    - Face Value: ... → face_value
    - Interest Rate: ... → interest_rate
    - Maturity Date: ... → maturity_date
    - ISIN: ... → securities_isin
    - Scrip Code: ... → scrip_code

    Returns: (new_tags, extracted_data)
    """
    new_tags = []
    extracted = {}

    for tag in tags:
        tag_stripped = tag.strip()

        # Check for data value patterns
        if tag_stripped.startswith("Face Value:"):
            extracted["face_value"] = tag_stripped.replace("Face Value:", "").strip()
        elif tag_stripped.startswith("Interest Rate:") or tag_stripped.startswith("Interest rate:"):
            extracted["interest_rate"] = tag_stripped.split(":", 1)[1].strip()
        elif tag_stripped.startswith("Maturity Date:"):
            extracted["maturity_date"] = tag_stripped.replace("Maturity Date:", "").strip()
        elif tag_stripped.startswith("ISIN:"):
            extracted["securities_isin"] = tag_stripped.replace("ISIN:", "").strip()
        elif tag_stripped.startswith("Scrip Code:") or tag_stripped.startswith("Scrip ID:"):
            extracted["scrip_code"] = tag_stripped.split(":", 1)[1].strip()
        else:
            # Keep non-data tags
            new_tags.append(tag)

    return new_tags, extracted


@dataclass
class NormalizationStats:
    """Aggregate statistics for normalization run."""

    total_files: int = 0
    modified_files: int = 0
    unchanged_files: int = 0
    error_files: int = 0

    # Stock stats
    stocks_original: int = 0
    stocks_normalized: int = 0
    stocks_isins_converted: int = 0
    stocks_duplicates_removed: int = 0
    unique_stocks_before: set = field(default_factory=set)
    unique_stocks_after: set = field(default_factory=set)

    # Tag stats
    tags_original: int = 0
    tags_normalized: int = 0
    tags_removed: int = 0
    tags_merged: int = 0
    tags_stock_duplicates_removed: int = 0
    unique_tags_before: set = field(default_factory=set)
    unique_tags_after: set = field(default_factory=set)

    errors: list = field(default_factory=list)

    def add_stock_stats(self, stats: dict) -> None:
        self.stocks_original += stats.get("original", 0)
        self.stocks_normalized += stats.get("normalized", 0)
        self.stocks_isins_converted += stats.get("isins_converted", 0)
        self.stocks_duplicates_removed += stats.get("duplicates_removed", 0)

    def add_tag_stats(self, stats: dict) -> None:
        self.tags_original += stats.get("original", 0)
        self.tags_normalized += stats.get("normalized", 0)
        self.tags_removed += stats.get("removed", 0)
        self.tags_merged += stats.get("merged", 0)
        self.tags_stock_duplicates_removed += stats.get("stock_duplicates_removed", 0)


class CircularNormalizer:
    """Normalizes stocks and tags in Hugo circular markdown files."""

    def __init__(
        self,
        content_dir: Path,
        instruments_path: Optional[Path] = None,
        tag_rules_path: Optional[Path] = None,
        dry_run: bool = False,
        stocks_only: bool = False,
        tags_only: bool = False,
    ):
        self.content_dir = content_dir
        self.dry_run = dry_run
        self.stocks_only = stocks_only
        self.tags_only = tags_only

        # Load instruments lookup
        self.instruments: Optional[InstrumentsLookup] = None
        if instruments_path and instruments_path.exists() and not tags_only:
            self.instruments = InstrumentsLookup(instruments_path)

        # Load tag rules
        self.tag_rules: Optional[TagRules] = None
        if tag_rules_path and tag_rules_path.exists() and not stocks_only:
            self.tag_rules = TagRules(tag_rules_path)

        self.stats = NormalizationStats()

    def process_file(self, file_path: Path) -> dict:
        """
        Process a single markdown file.

        Returns dict with 'modified' bool and 'changes' list.
        """
        result = {"modified": False, "changes": [], "file": str(file_path)}

        try:
            # Read file
            post = frontmatter.load(file_path)
            metadata = post.metadata

            # Track if anything changed
            changed = False

            # PHASE 1: Extract data values from tags and migrate scrip codes
            original_tags = metadata.get("tags", [])
            original_stocks = metadata.get("stocks", [])

            if original_tags and not self.stocks_only:
                # Extract data values (Face Value, Interest Rate, etc.) to frontmatter
                cleaned_tags, extracted_data = extract_data_values_from_tags(
                    original_tags, metadata
                )

                # Add extracted data to metadata
                if extracted_data:
                    for key, value in extracted_data.items():
                        metadata[key] = value
                        changed = True
                    # Update tags to cleaned version (without data values)
                    original_tags = cleaned_tags

                # Migrate numeric tags (scrip codes) to stocks
                cleaned_tags, migrated_stocks = migrate_scrip_codes_to_stocks(
                    original_tags, original_stocks
                )

                # Update if scrip codes were migrated
                if len(migrated_stocks) > len(original_stocks):
                    metadata["tags"] = cleaned_tags
                    metadata["stocks"] = migrated_stocks
                    original_stocks = migrated_stocks  # For stock normalization
                    changed = True

            # PHASE 2: Normalize stocks
            if not self.tags_only and original_stocks:
                # Track unique stocks before
                for stock in original_stocks:
                    if stock:
                        self.stats.unique_stocks_before.add(stock.upper())

                normalized_stocks, stock_stats = normalize_stocks(
                    original_stocks, self.instruments
                )
                self.stats.add_stock_stats(stock_stats)

                # Track unique stocks after
                for stock in normalized_stocks:
                    if stock:
                        self.stats.unique_stocks_after.add(stock.upper())

                if normalized_stocks != original_stocks:
                    result["changes"].append(
                        {
                            "field": "stocks",
                            "before": original_stocks,
                            "after": normalized_stocks,
                        }
                    )
                    metadata["stocks"] = normalized_stocks
                    changed = True

            # Normalize tags
            if not self.stocks_only:
                original_tags = metadata.get("tags", [])
                stocks_for_filter = metadata.get("stocks", [])
                if original_tags:
                    # Track unique tags before
                    for tag in original_tags:
                        if tag:
                            self.stats.unique_tags_before.add(tag.lower())

                    normalized_tags, tag_stats = normalize_tags(
                        original_tags, stocks_for_filter, self.tag_rules
                    )
                    self.stats.add_tag_stats(tag_stats)

                    # Track unique tags after
                    for tag in normalized_tags:
                        if tag:
                            self.stats.unique_tags_after.add(tag.lower())

                    if normalized_tags != original_tags:
                        result["changes"].append(
                            {
                                "field": "tags",
                                "before": original_tags,
                                "after": normalized_tags,
                            }
                        )
                        metadata["tags"] = normalized_tags
                        changed = True

            result["modified"] = changed

            # Write file if modified and not dry-run
            if changed and not self.dry_run:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(frontmatter.dumps(post))

        except Exception as e:
            result["error"] = str(e)
            self.stats.errors.append({"file": str(file_path), "error": str(e)})

        return result

    def process_all(self, max_workers: int = 8) -> NormalizationStats:
        """Process all markdown files with parallel execution."""
        md_files = list(self.content_dir.rglob("*.md"))
        self.stats.total_files = len(md_files)

        print(f"\nProcessing {len(md_files)} files...")
        print(f"Mode: {'DRY RUN' if self.dry_run else 'LIVE'}")
        if self.stocks_only:
            print("Scope: Stocks only")
        elif self.tags_only:
            print("Scope: Tags only")
        else:
            print("Scope: Stocks and Tags")
        print()

        processed = 0
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self.process_file, f): f for f in md_files}

            for future in as_completed(futures):
                file_path = futures[future]
                try:
                    result = future.result()
                    if result.get("error"):
                        self.stats.error_files += 1
                    elif result["modified"]:
                        self.stats.modified_files += 1
                    else:
                        self.stats.unchanged_files += 1
                except Exception as e:
                    self.stats.error_files += 1
                    self.stats.errors.append({"file": str(file_path), "error": str(e)})

                processed += 1
                if processed % 1000 == 0:
                    print(f"  Processed {processed}/{len(md_files)} files...")

        return self.stats


def print_stats(stats: NormalizationStats, dry_run: bool) -> None:
    """Print summary statistics."""
    print("\n" + "=" * 60)
    print("NORMALIZATION SUMMARY")
    print("=" * 60)

    if dry_run:
        print("\n*** DRY RUN - No files were modified ***\n")

    print(f"\nFiles:")
    print(f"  Total:     {stats.total_files:,}")
    print(f"  Modified:  {stats.modified_files:,}")
    print(f"  Unchanged: {stats.unchanged_files:,}")
    print(f"  Errors:    {stats.error_files:,}")

    print(f"\nStocks:")
    unique_before = len(stats.unique_stocks_before)
    unique_after = len(stats.unique_stocks_after)
    unique_reduction = unique_before - unique_after if unique_before > 0 else 0
    unique_pct = (100 * unique_reduction / unique_before) if unique_before > 0 else 0

    print(f"  Unique (before):       {unique_before:,}")
    print(f"  Unique (after):        {unique_after:,}")
    if unique_reduction > 0:
        print(f"  Unique reduced:        {unique_reduction:,} ({unique_pct:.1f}%)")
    print(f"  Total entries:         {stats.stocks_original:,} → {stats.stocks_normalized:,}")
    print(f"  ISINs converted:       {stats.stocks_isins_converted:,}")
    print(f"  Duplicates removed:    {stats.stocks_duplicates_removed:,}")

    print(f"\nTags:")
    unique_tags_before = len(stats.unique_tags_before)
    unique_tags_after = len(stats.unique_tags_after)
    unique_tags_reduction = unique_tags_before - unique_tags_after if unique_tags_before > 0 else 0
    unique_tags_pct = (100 * unique_tags_reduction / unique_tags_before) if unique_tags_before > 0 else 0

    print(f"  Unique (before):       {unique_tags_before:,}")
    print(f"  Unique (after):        {unique_tags_after:,}")
    if unique_tags_reduction > 0:
        print(f"  Unique reduced:        {unique_tags_reduction:,} ({unique_tags_pct:.1f}%)")
    print(f"  Total entries:         {stats.tags_original:,} → {stats.tags_normalized:,}")
    print(f"  Invalid removed:       {stats.tags_removed:,}")
    print(f"  Merged to canonical:   {stats.tags_merged:,}")
    print(f"  Stock dupes removed:   {stats.tags_stock_duplicates_removed:,}")

    if stats.errors:
        print(f"\nFirst 10 errors:")
        for err in stats.errors[:10]:
            print(f"  {err['file']}: {err['error']}")

    print("\n" + "=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Normalize stocks and tags in Hugo circulars"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without modifying files",
    )
    parser.add_argument(
        "--stocks-only",
        action="store_true",
        help="Only normalize stocks",
    )
    parser.add_argument(
        "--tags-only",
        action="store_true",
        help="Only normalize tags",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=8,
        help="Number of parallel workers (default: 8)",
    )
    parser.add_argument(
        "--content-dir",
        type=Path,
        default=Path(__file__).parent.parent / "hugo-site" / "content" / "circulars",
        help="Path to circulars content directory",
    )
    parser.add_argument(
        "--instruments",
        type=Path,
        default=Path("/tmp/instruments.json"),
        help="Path to instruments.json file",
    )
    parser.add_argument(
        "--tag-rules",
        type=Path,
        default=Path(__file__).parent / "tag_rules.yaml",
        help="Path to tag rules YAML file",
    )

    args = parser.parse_args()

    if args.stocks_only and args.tags_only:
        print("Error: Cannot specify both --stocks-only and --tags-only")
        sys.exit(1)

    if not args.content_dir.exists():
        print(f"Error: Content directory not found: {args.content_dir}")
        sys.exit(1)

    normalizer = CircularNormalizer(
        content_dir=args.content_dir,
        instruments_path=args.instruments,
        tag_rules_path=args.tag_rules,
        dry_run=args.dry_run,
        stocks_only=args.stocks_only,
        tags_only=args.tags_only,
    )

    stats = normalizer.process_all(max_workers=args.workers)
    print_stats(stats, args.dry_run)

    # Exit with error code if there were errors
    if stats.error_files > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
