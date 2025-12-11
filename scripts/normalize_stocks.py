#!/usr/bin/env python3
"""
Stock normalization module for stock market circulars.

Normalizes stocks by:
- Converting to uppercase
- Converting ISINs to tickers using instruments.json
- Removing duplicates
"""

import json
import re
from pathlib import Path
from typing import Optional


class InstrumentsLookup:
    """Lookup table for instruments data from Zerodha/Kite."""

    def __init__(self, instruments_path: Path):
        self.isin_to_ticker: dict[str, str] = {}
        self.ticker_set: set[str] = set()
        self.name_to_ticker: dict[str, str] = {}  # Simplified name -> ticker
        self.ticker_to_name: dict[str, str] = {}  # ticker -> full name
        self.bse_scrip_to_ticker: dict[str, str] = {}  # BSE exchange_token -> ticker
        self._load_instruments(instruments_path)

    def _load_instruments(self, path: Path) -> None:
        """Load instruments from NDJSON file."""
        if not path.exists():
            print(f"Warning: instruments file not found at {path}")
            return

        nse_tickers: dict[str, str] = {}  # ISIN -> NSE ticker
        bse_tickers: dict[str, str] = {}  # ISIN -> BSE ticker

        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)

                    # Only process equities
                    if record.get("instrument_type") != "EQ":
                        continue

                    exchange = record.get("exchange", "")
                    ticker = record.get("tradingsymbol", "")
                    isin = record.get("isin", "").strip()
                    name = record.get("name", "").strip()
                    exchange_token = record.get("exchange_token")

                    if not ticker:
                        continue

                    ticker_upper = ticker.upper()

                    # Add to ticker set
                    self.ticker_set.add(ticker_upper)

                    # Build BSE scrip code mapping (exchange_token is the scrip code)
                    if exchange == "BSE" and exchange_token:
                        self.bse_scrip_to_ticker[str(exchange_token)] = ticker_upper

                    # Build name mappings (simplified for fuzzy matching)
                    if name:
                        self.ticker_to_name[ticker_upper] = name
                        # Simplify name: remove Ltd, Limited, special chars
                        simple_name = re.sub(r'\b(LTD|LIMITED|PVT|PRIVATE)\b\.?', '', name.upper())
                        simple_name = re.sub(r'[^A-Z0-9]', '', simple_name)
                        if simple_name and len(simple_name) >= 3:
                            # Prefer NSE tickers for name mapping too
                            if exchange == "NSE" or simple_name not in self.name_to_ticker:
                                self.name_to_ticker[simple_name] = ticker_upper

                    # Build ISIN mappings (prefer NSE over BSE)
                    if isin and not isin.startswith("DUMMY"):
                        if exchange == "NSE":
                            nse_tickers[isin] = ticker_upper
                        elif exchange == "BSE":
                            bse_tickers[isin] = ticker_upper

                except json.JSONDecodeError:
                    continue

        # Merge: prefer NSE ticker, fall back to BSE
        for isin, ticker in nse_tickers.items():
            self.isin_to_ticker[isin] = ticker
        for isin, ticker in bse_tickers.items():
            if isin not in self.isin_to_ticker:
                self.isin_to_ticker[isin] = ticker

        print(f"Loaded {len(self.ticker_set)} unique tickers")
        print(f"Loaded {len(self.isin_to_ticker)} ISIN mappings")
        print(f"Loaded {len(self.name_to_ticker)} name mappings")
        print(f"Loaded {len(self.bse_scrip_to_ticker)} BSE scrip codes")

    def normalize(self, stock: str) -> Optional[str]:
        """
        Normalize a stock entry.

        Args:
            stock: Stock ticker, ISIN, or company name

        Returns:
            Normalized stock string (uppercase) or None if it's invalid
        """
        if not stock:
            return None

        stock = stock.strip()
        stock_upper = stock.upper()

        # Check if it's already a valid ticker FIRST (handles 360ONE, 3MINDIA, etc.)
        if stock_upper in self.ticker_set:
            return stock_upper

        # Check if it's a BSE scrip code (6-digit number) and convert to ticker
        if re.match(r"^\d{6}$", stock):
            if stock in self.bse_scrip_to_ticker:
                return self.bse_scrip_to_ticker[stock]
            # Remove scrip codes that don't map to tickers
            return None

        # Skip other pure numeric patterns that look like codes
        if re.match(r"^\d+[A-Z]{2,}\d+$", stock_upper):  # e.g., 10NFL25, 1215DHPL27
            return None

        # Check if it's an ISIN (INE + 10 alphanumeric chars)
        if re.match(r"^INE[A-Z0-9]{10}$", stock_upper):
            isin = stock_upper
            if isin in self.isin_to_ticker:
                return self.isin_to_ticker[isin]
            # Keep ISIN if not found in mapping
            return isin

        # Try fuzzy matching for common misspellings/variations
        # e.g., TATAMOTORS -> TATAMOTORS (if exists) or TATAMTRDVR
        stock_simplified = re.sub(r"[^A-Z0-9]", "", stock_upper)

        # Check if simplified version exists
        if stock_simplified in self.ticker_set:
            return stock_simplified

        # Try name-based matching
        if stock_simplified in self.name_to_ticker:
            return self.name_to_ticker[stock_simplified]

        # DISABLED: Fuzzy matching causes data loss (POWER → TATAPOWER, HDFC → HDFCBANK, etc.)
        # See TAG_STOCK_CONSOLIDATION_STRATEGY.md for analysis
        # # Check for partial matches (contains or is contained)
        # # Useful for: INFOSYS -> INFY, TATAMOTORS -> TATAMTRDVR
        # for ticker in self.ticker_set:
        #     # Only match if reasonably similar length
        #     if len(stock_simplified) >= 5 and len(ticker) >= 5:
        #         if stock_simplified in ticker or ticker in stock_simplified:
        #             return ticker

        # If no match found, keep as uppercase (preserves information)
        return stock_upper

    def is_valid_ticker(self, ticker: str) -> bool:
        """Check if ticker exists in instruments."""
        return ticker.upper() in self.ticker_set


def normalize_stocks(
    stocks: list[str], instruments: Optional[InstrumentsLookup] = None
) -> tuple[list[str], dict]:
    """
    Normalize a list of stocks.

    Args:
        stocks: List of stock entries
        instruments: Optional InstrumentsLookup instance

    Returns:
        Tuple of (normalized_stocks, stats_dict)
    """
    if not stocks:
        return [], {"original": 0, "normalized": 0, "isins_converted": 0}

    stats = {
        "original": len(stocks),
        "normalized": 0,
        "isins_converted": 0,
        "duplicates_removed": 0,
        "invalid_removed": 0,
        "fuzzy_matched": 0,
    }

    seen: set[str] = set()
    normalized: list[str] = []

    for stock in stocks:
        if not stock:
            continue

        original = stock.strip()
        original_upper = original.upper()

        # Normalize using instruments lookup if available
        if instruments:
            norm = instruments.normalize(stock)

            # Track what happened
            if norm is None:
                stats["invalid_removed"] += 1
                continue
            elif norm != original_upper:
                if re.match(r"^INE[A-Z0-9]{10}$", original_upper):
                    stats["isins_converted"] += 1
                elif norm != original_upper:
                    stats["fuzzy_matched"] += 1
        else:
            norm = original_upper

        # Deduplicate
        if norm and norm not in seen:
            seen.add(norm)
            normalized.append(norm)
        elif norm in seen:
            stats["duplicates_removed"] += 1

    stats["normalized"] = len(normalized)
    return normalized, stats


# For standalone testing
if __name__ == "__main__":
    import sys

    instruments_path = Path("/tmp/instruments.json")

    if instruments_path.exists():
        lookup = InstrumentsLookup(instruments_path)

        # Test cases
        test_stocks = [
            "RELIANCE",
            "reliance",  # Case variation
            "INE002A01018",  # ISIN for Reliance
            "HINDzinc",  # Mixed case
            "HINDZINC",  # Should merge with above
            "TATAMOTORS",  # Unmatched
        ]

        print("\nTest normalization:")
        normalized, stats = normalize_stocks(test_stocks, lookup)
        print(f"Input: {test_stocks}")
        print(f"Output: {normalized}")
        print(f"Stats: {stats}")
    else:
        print(f"Instruments file not found at {instruments_path}")
        sys.exit(1)
