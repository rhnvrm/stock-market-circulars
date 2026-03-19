---
category: market-operations
circular_id: d26984ae0e14762b
date: '2026-03-19'
description: NSE introduces Standard Operating Procedure for Settlement Price Computation
  under the new Closing Auction Session (CAS) in the Equity Segment, detailing price
  determination rules for CAS-applicable and non-applicable stocks.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT73373.zip
impact: high
impact_ranking: high
importance_ranking: high
justification: Introduces a structural change to how settlement prices are computed
  in the equity segment via a new Closing Auction Session, affecting all listed equity
  stocks and market participants.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT73373.zip
processing:
  attempts: 1
  content_hash: 4dfd4c215a64b1ff
  processed_at: '2026-03-19T13:11:31.393978'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-03-19T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT73373.zip
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
- trading-operations
- sop
title: Operational Guidelines and SOP on Introduction of Closing Auction Session (CAS)
  in Equity Segment
---

## Summary

NSE has issued operational guidelines and a Standard Operating Procedure (SOP) for the introduction of the Closing Auction Session (CAS) in the Equity Segment. The circular details how settlement prices will be computed differently depending on whether a stock is subject to CAS or not, replacing or supplementing the existing last-30-minutes VWAP methodology.

## Key Points

- Settlement price computation rules differ for CAS-applicable and non-CAS stocks
- For CAS-applicable stocks, the Equilibrium Price determined during CAS replaces the last-30-minutes VWAP as the settlement price
- If multiple stock exchanges provide equilibrium price and quantity, a VWAP of those prices is used as the settlement price
- If only one stock exchange provides the equilibrium price, that price is used directly
- For non-CAS stocks, the existing last-30-minutes VWAP methodology continues to apply
- Settlement prices with more than 2 decimal places are rounded using standard mathematical rounding
- If a stock does not trade during CAS and no equilibrium price is determined but traded during the day, the Reference Price is used as the close price
- If a stock has not traded at all during the day, the previous trading day's settlement price is used

## Regulatory Changes

- Introduction of Closing Auction Session (CAS) as a new post-market trading session in the Equity Segment
- New settlement price computation framework for CAS-applicable stocks using Equilibrium Price instead of VWAP of last 30 minutes
- Reference Price replaces Last Traded Price (LTP) as the fallback close price for CAS stocks that traded during the day but not in CAS
- Three-tiered fallback hierarchy for CAS stocks: (1) CAS Equilibrium Price, (2) Reference Price (if traded intraday), (3) Previous day's settlement price

## Compliance Requirements

- Stock Exchanges must provide traded quantity and equilibrium price for CAS stocks where equilibrium price is determined
- Stock Exchanges must provide Reference Price as close price for CAS stocks that did not trade in CAS but traded during the day
- Where multiple exchanges provide settlement data, exchanges must coordinate to compute VWAP across provided prices
- All settlement prices must be rounded to 2 decimal places using simple mathematical rounding

## Important Dates

- Circular date: 2026-03-19
- Effective date: Not explicitly stated in the available content; refer to the full circular for implementation timeline

## Impact Assessment

- **Broad Market Impact**: Affects all equity segment participants including brokers, clearing members, custodians, and investors as settlement prices for CAS-applicable stocks will now be determined via auction equilibrium rather than VWAP
- **Price Discovery**: CAS is expected to improve end-of-day price discovery by concentrating liquidity into an auction mechanism, potentially reducing price manipulation in the closing minutes
- **Operational Impact**: Trading and risk systems will need to be updated to handle the new settlement price computation logic, including the distinction between CAS and non-CAS stocks
- **Multi-Exchange Coordination**: Requires coordination between stock exchanges (NSE, BSE) for cross-exchange VWAP computation when both provide equilibrium prices
- **Derivatives Settlement**: Settlement prices from the equity segment feed into derivatives settlement, so this change will have downstream impact on F&O settlement as well