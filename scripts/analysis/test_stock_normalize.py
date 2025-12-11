#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Test stock normalization logic."""

from pathlib import Path
from normalize_stocks import InstrumentsLookup

instruments_path = Path("/tmp/instruments.json")
lookup = InstrumentsLookup(instruments_path)

# Test cases
test_cases = [
    "500209",  # BSE scrip for INFY
    "500052",  # BSE scrip for BEPL
    "INFY",    # Already valid
    "infy",    # Case variation
    "TATAMOTORS",  # Invalid
    "INFOSYS",  # Company name
    "360ONE",  # Valid
    "360 ONE WAM",  # Invalid format
]

print("\nStock Normalization Test:")
print("=" * 60)
for test in test_cases:
    result = lookup.normalize(test)
    print(f"  {test:20s} -> {result}")

# Check specific scrip mappings
print("\n\nBSE Scrip Code Samples:")
print("=" * 60)
sample_scrips = ["500209", "500052", "532540", "500325"]
for scrip in sample_scrips:
    if scrip in lookup.bse_scrip_to_ticker:
        print(f"  {scrip} -> {lookup.bse_scrip_to_ticker[scrip]}")
    else:
        print(f"  {scrip} -> NOT FOUND")
