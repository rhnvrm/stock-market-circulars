#!/usr/bin/env python3
"""
Tag normalization module for stock market circulars.

Normalizes tags by:
- Lowercasing
- Merging similar tags using rules
- Removing invalid/numeric tags
- Removing tags that duplicate stock entries
"""

import re
from pathlib import Path
from typing import Optional

import yaml


class TagRules:
    """Tag normalization rules loaded from YAML config."""

    def __init__(self, rules_path: Path):
        self.remove_patterns: list[re.Pattern] = []
        self.merge_map: dict[str, str] = {}  # alias -> canonical
        self.lowercase: bool = True
        self.remove_stock_duplicates: bool = True
        self._load_rules(rules_path)

    def _load_rules(self, path: Path) -> None:
        """Load rules from YAML file."""
        if not path.exists():
            print(f"Warning: tag rules file not found at {path}")
            return

        with open(path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)

        # Load remove patterns
        for pattern in config.get("remove_patterns", []):
            try:
                self.remove_patterns.append(re.compile(pattern, re.IGNORECASE))
            except re.error as e:
                print(f"Invalid regex pattern '{pattern}': {e}")

        # Load merge rules (canonical -> [aliases])
        # Build reverse map (alias -> canonical)
        for canonical, aliases in config.get("merge_rules", {}).items():
            # Canonical maps to itself
            self.merge_map[canonical.lower()] = canonical.lower()
            # Each alias maps to canonical
            for alias in aliases:
                self.merge_map[alias.lower()] = canonical.lower()

        self.lowercase = config.get("lowercase", True)
        self.remove_stock_duplicates = config.get("remove_stock_duplicates", True)

        print(f"Loaded {len(self.remove_patterns)} remove patterns")
        print(f"Loaded {len(self.merge_map)} tag merge mappings")

    def should_remove(self, tag: str) -> bool:
        """Check if tag should be removed based on patterns."""
        for pattern in self.remove_patterns:
            if pattern.match(tag):
                return True
        return False

    def get_canonical(self, tag: str) -> str:
        """Get canonical form of a tag."""
        tag_lower = tag.lower().strip()
        return self.merge_map.get(tag_lower, tag_lower)


def _is_tag_stock_duplicate(tag: str, stock_set: set[str], stock_simplified: set[str]) -> bool:
    """
    Check if a tag duplicates a stock entry.

    Uses fuzzy matching for company names:
    - Exact match: tag "RELIANCE" matches stock "RELIANCE"
    - Simplified match: tag "icici-bank" matches stock "ICICIBANK"
    - Company suffix match: tag "tata-power" matches stock "TATAPOWER"
    """
    tag_upper = tag.upper()

    # Exact match
    if tag_upper in stock_set:
        return True

    # Simplified match (remove hyphens, spaces, etc.)
    tag_simplified = re.sub(r'[^A-Z0-9]', '', tag_upper)
    if tag_simplified in stock_simplified:
        return True

    # Check if tag is contained in any stock or vice versa (for partial matches)
    # e.g., "manappuram-finance" -> "MANAPPURAMFIN"
    # INCREASED threshold from 5 to 8 to reduce false positives
    # (prevents "india" matching "INDIAMART", "power" matching "TATAPOWER", etc.)
    if len(tag_simplified) >= 8:  # Only for reasonably long tags
        for stock_simp in stock_simplified:
            # Tag contains stock or stock contains tag
            if len(stock_simp) >= 8:
                if tag_simplified in stock_simp or stock_simp in tag_simplified:
                    return True

    return False


def normalize_tags(
    tags: list[str],
    stocks: Optional[list[str]] = None,
    rules: Optional[TagRules] = None,
) -> tuple[list[str], dict]:
    """
    Normalize a list of tags.

    Args:
        tags: List of tag entries
        stocks: Optional list of stock entries (to remove duplicates)
        rules: Optional TagRules instance

    Returns:
        Tuple of (normalized_tags, stats_dict)
    """
    if not tags:
        return [], {"original": 0, "normalized": 0, "removed": 0, "merged": 0}

    stats = {
        "original": len(tags),
        "normalized": 0,
        "removed": 0,
        "merged": 0,
        "stock_duplicates_removed": 0,
    }

    # Build stock sets for duplicate checking
    stock_set: set[str] = set()
    stock_simplified: set[str] = set()
    if stocks:
        for s in stocks:
            if s:
                stock_set.add(s.upper())
                # Also add simplified version (no special chars)
                stock_simplified.add(re.sub(r'[^A-Z0-9]', '', s.upper()))

    seen: set[str] = set()
    normalized: list[str] = []

    for tag in tags:
        if not tag:
            continue

        tag = tag.strip()
        original_tag = tag

        # Lowercase if enabled
        if rules and rules.lowercase:
            tag = tag.lower()
        else:
            tag = tag.lower()  # Always lowercase tags

        # Check if tag should be removed
        if rules and rules.should_remove(tag):
            stats["removed"] += 1
            continue

        # Check if tag is a stock duplicate (with fuzzy matching)
        if rules and rules.remove_stock_duplicates:
            if _is_tag_stock_duplicate(tag, stock_set, stock_simplified):
                stats["stock_duplicates_removed"] += 1
                continue

        # Apply merge rules
        if rules:
            canonical = rules.get_canonical(tag)
            if canonical != tag:
                stats["merged"] += 1
            tag = canonical

        # Deduplicate
        if tag and tag not in seen:
            seen.add(tag)
            normalized.append(tag)

    stats["normalized"] = len(normalized)
    return sorted(normalized), stats


# For standalone testing
if __name__ == "__main__":
    import sys

    rules_path = Path(__file__).parent / "tag_rules.yaml"

    if rules_path.exists():
        rules = TagRules(rules_path)

        # Test cases
        test_tags = [
            "listing",
            "ncds",  # Should merge to ncd
            "non-convertible-debentures",  # Should merge to ncd
            "532310",  # Should be removed (numeric)
            "RELIANCE",  # Should be removed (stock duplicate)
            "corporate-actions",  # Should merge to corporate-action
            "ipo",
            "IPO",  # Case variation, should dedupe
        ]

        test_stocks = ["RELIANCE", "TCS"]

        print("\nTest normalization:")
        normalized, stats = normalize_tags(test_tags, test_stocks, rules)
        print(f"Input tags: {test_tags}")
        print(f"Input stocks: {test_stocks}")
        print(f"Output: {normalized}")
        print(f"Stats: {stats}")
    else:
        print(f"Tag rules file not found at {rules_path}")
        sys.exit(1)
