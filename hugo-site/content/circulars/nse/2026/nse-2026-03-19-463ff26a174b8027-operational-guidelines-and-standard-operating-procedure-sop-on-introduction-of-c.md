---
category: market-operations
circular_id: 463ff26a174b8027
date: '2026-03-19'
description: NSE introduces Standard Operating Procedures for Settlement Price Computation
  under the new Closing Auction Session (CAS) in the Equity Segment, detailing how
  equilibrium prices replace VWAP-based settlement prices.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT73370.zip
impact: high
impact_ranking: high
importance_ranking: high
justification: Introduces a fundamental change to how closing prices are determined
  in the equity segment, affecting settlement prices for all CAS-applicable stocks
  across exchanges.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT73370.zip
processing:
  attempts: 1
  content_hash: 99af4534ea68e442
  processed_at: '2026-03-19T13:12:57.632472'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-03-19T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT73370.zip
severity: high
source: nse
stocks: []
tags:
- closing-auction-session
- cas
- settlement-price
- equity-segment
- vwap
- equilibrium-price
- market-operations
- sop
title: Operational Guidelines and SOP on Introduction of Closing Auction Session (CAS)
  in Equity Segment
---

## Summary

NSE has issued operational guidelines and a Standard Operating Procedure (SOP) for Settlement Price Computation in the Equity Segment following the introduction of the Closing Auction Session (CAS). The SOP establishes clear rules for determining settlement prices under CAS-applicable stocks versus non-CAS stocks, covering multiple scenarios based on trading activity during the session.

## Key Points

- For CAS-applicable stocks where an equilibrium price is determined, the equilibrium price replaces the VWAP of the last 30 minutes as the settlement price.
- If multiple stock exchanges provide equilibrium prices and quantities, a VWAP of those prices is used as the settlement price.
- If only one exchange provides an equilibrium price, that price is used directly.
- If no equilibrium price is determined in CAS but the stock traded during the day, the Reference Price is used as the close price (replacing Last Traded Price for non-CAS stocks).
- If no trading occurred at all during the day, the previous trading day's settlement price is used.
- Settlement prices with more than 2 decimal places are rounded using standard mathematical rounding.

## Regulatory Changes

- Introduction of the Closing Auction Session (CAS) in the Equity Segment changes the basis for settlement price computation.
- For CAS stocks: equilibrium price from CAS replaces the last-30-minute VWAP methodology.
- For CAS stocks with no CAS trade: Reference Price replaces Last Traded Price (LTP) as the fallback close price.
- Multi-exchange price aggregation rules now differentiate between CAS and non-CAS stock scenarios.

## Compliance Requirements

- Stock Exchanges must provide traded quantity and equilibrium price from the CAS session for applicable stocks.
- Exchanges must provide Reference Price as close price when no equilibrium price is established but intraday trading occurred.
- All settlement price computations must be rounded to 2 decimal places using simple mathematical rounding.
- Clearing corporations and market participants must update settlement price computation systems to incorporate the new CAS-based methodology.

## Important Dates

- Circular date: 2026-03-19
- Effective date of CAS and associated SOP: as per NSE implementation schedule (refer to accompanying circulars).

## Impact Assessment

This circular has high market-wide impact as it changes the foundational methodology for computing daily settlement prices in the equity segment. All CAS-applicable stocks will have their closing/settlement prices determined via the new auction equilibrium mechanism rather than VWAP of the last 30 minutes of continuous trading. This affects brokers, clearing members, custodians, index providers, and derivative markets that rely on equity closing prices for mark-to-market, margining, and expiry settlement. Market participants must update their systems and risk models to reflect the new price discovery mechanism at market close.