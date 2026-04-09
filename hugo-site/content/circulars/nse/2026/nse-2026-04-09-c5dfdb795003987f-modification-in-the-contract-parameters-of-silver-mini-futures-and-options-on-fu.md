---
category: market-operations
circular_id: c5dfdb795003987f
date: '2026-04-09'
description: NSE revises trading unit, symbol, and quotation parameters for Silver
  Mini Futures and Options on Futures, reducing the trading unit from 5 Kg to 100
  Grams with effect from May 4, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/COM73673.pdf
impact: high
impact_ranking: high
importance_ranking: high
justification: Significant structural change to Silver Mini derivatives — symbol rename,
  unit reduction from 5 Kg to 100 Grams, and revised strike intervals affect all trading
  members dealing in silver commodity derivatives. Members must update contract files
  before May 4, 2026 to avoid disruption.
pdf_url: https://nsearchives.nseindia.com/content/circulars/COM73673.pdf
processing:
  attempts: 1
  content_hash: 132817fd02059e68
  processed_at: '2026-04-09T10:16:48.760852'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-04-09T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/COM73673.pdf
severity: high
source: nse
stocks:
- SILVERM
- SILVER100
tags:
- silver-mini
- commodity-derivatives
- contract-parameters
- futures
- options-on-futures
- SILVER100
- SILVERM
- contract-modification
title: NSE Modifies Silver Mini Futures and Options Contract Parameters Effective
  May 2026
---

## Summary

NSE's Commodity Derivatives department has announced a revision to the contract parameters of Silver Mini Futures and Silver Mini Options on Futures. The trading and delivery unit is being reduced from 5 Kg to 100 Grams, the symbol is changing from SILVERM to SILVER100, and the quotation/base value is shifting from Rs/1Kg to Rs/100 grams. These changes apply to contracts expiring in May 2026 and beyond, effective May 4, 2026.

## Key Points

- Silver Mini Futures trading unit reduced from 5 Kg to 100 Grams
- Symbol changed from SILVERM to SILVER100
- Quotation base revised from Rs/1Kg to Rs/100 grams
- Silver Mini Options on Futures underlying updated to Silver100 Futures
- Strike interval for Options reduced from Rs 250 to Rs 25
- Changes effective May 4, 2026 for May 2026 expiry contracts onwards
- Trading members must upload updated co_contract.gz file before trading on May 4, 2026

## Regulatory Changes

| Parameter | Existing (SILVERM) | Modified (SILVER100) |
|---|---|---|
| Trading & Delivery Unit | 5 Kg | 100 Grams |
| Symbol | SILVERM | SILVER100 |
| Quotation/Base Value | Rs/1Kg | Rs/100 grams |
| Options Strike Interval | Rs 250 | Rs 25 |

The Silver Mini Options on Futures underlying asset is correspondingly updated from SILVERM to SILVER100 Futures.

## Compliance Requirements

- All trading members must download and upload the latest **co_contract.gz** file from NSE Extranet (path: `/comtftp/comtcommon`) **before commencing trading on May 4, 2026**.
- Members must ensure their systems and strategies reflect the new symbol (SILVER100), reduced lot size (100 Grams), revised quotation base (Rs/100 grams), and new strike interval (Rs 25) for options.
- Existing open positions in SILVERM contracts expiring before May 2026 will continue under existing parameters until expiry.

## Important Dates

- **April 9, 2026** — Circular issued by NSE
- **May 4, 2026** — Effective date for revised contract parameters; new symbol SILVER100 goes live
- **May 2026 expiry contracts onwards** — All Silver Mini Futures and Options trade under revised parameters

## Impact Assessment

This is a high-impact change for commodity derivatives participants. Reducing the lot size from 5 Kg to 100 Grams significantly lowers the minimum contract value, potentially improving accessibility and liquidity for retail participants in silver derivatives. The corresponding reduction in the options strike interval from Rs 250 to Rs 25 enables finer hedging granularity. Trading members with automated systems, algo strategies, or risk management frameworks referencing the SILVERM symbol must update all references to SILVER100 and recalibrate position sizing and margin calculations before May 4, 2026. Failure to upload the updated contract file could result in trading disruptions.