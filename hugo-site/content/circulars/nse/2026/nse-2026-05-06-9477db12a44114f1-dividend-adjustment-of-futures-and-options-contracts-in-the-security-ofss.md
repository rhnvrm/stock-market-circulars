---
category: trading
circular_id: 9477db12a44114f1
date: '2026-05-06'
description: NSE adjusts futures and options contracts for Oracle Financial Services
  Software Limited (OFSS) due to a dividend of Rs 270 per share, effective ex-date
  May 7, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP74089.pdf
impact: high
impact_ranking: high
importance_ranking: high
justification: A large dividend of Rs 270 (vs face value of Rs 5) triggers mandatory
  strike price revisions across all OFSS options contracts expiring May 26, 2026.
  Traders holding positions must load updated contract files before ex-date to avoid
  mispricing.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP74089.pdf
processing:
  attempts: 1
  content_hash: bfda4a48998ad895
  processed_at: '2026-05-06T14:18:04.160931'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-06T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP74089.pdf
severity: high
source: nse
stocks:
- OFSS
tags:
- futures-and-options
- dividend-adjustment
- strike-price-revision
- ofss
- corporate-action
- derivatives
- oracle-financial-services
title: OFSS Futures & Options Strike Price Adjustment for Rs 270 Dividend
---

## Summary

NSE has announced the adjustment of Futures and Options contracts for Oracle Financial Services Software Limited (Symbol: OFSS) in accordance with SEBI guidelines on corporate action adjustments. A dividend of Rs 270 per share (face value Rs 5) has been declared, with an ex-date of May 7, 2026. All option strike prices for the May 26, 2026 expiry are being revised downward by Rs 270 to reflect the dividend payout.

## Key Points

- **Symbol:** OFSS (Oracle Financial Services Software Limited)
- **Corporate Action:** Dividend of Rs 270/- per share (Face Value: Rs 5/-)
- **Ex-date / Effective Date:** May 7, 2026
- Strike prices for OPTSTK contracts expiring May 26, 2026 are revised downward by Rs 270
- Updated contract files (contract.gz / MII contract and spread files) must be loaded before trading on the ex-date
- Revised strike/futures base prices may appear in decimal places and will be rounded to the nearest tick size; lot sizes rounded to nearest integer
- Position adjustment methodology will be separately communicated by the respective Clearing Corporation

## Regulatory Changes

Pursuant to SEBI guidelines for adjustments to futures and options contracts on announcement of corporate actions, option strike prices are revised to neutralize the economic impact of the dividend. The adjustment reduces each strike price by the dividend amount of Rs 270.

## Compliance Requirements

- Members must load the updated contract.gz / MII contract file (`NSE_FO_contract_ddmmyyyy.csv.gz`) and spread file (`NSE_FO_spdcontract_ddmmyyyy.csv.gz`) on their trading applications **before trading on May 7, 2026**
- Files are available from the directory `faoftp/faocommon` on the Extranet server and also on the NSE website at https://www.nseindia.com/all-reports-derivatives
- Members should refer to https://www.nseindia.com/products-services/equity-derivatives-corporate-actions-adjustments for full adjustment details (Annexure 1)

## Important Dates

- **Circular Date:** May 6, 2026
- **Ex-date / Effective Date:** May 7, 2026 (strike revisions take effect)
- **Options Expiry Affected:** May 26, 2026

## Impact Assessment

The Rs 270 dividend represents a very large payout relative to the face value of Rs 5, indicating a substantial cash return to shareholders. This triggers significant strike price revisions across all listed OFSS option contracts for the May 2026 expiry. Traders with open positions in OFSS derivatives must be aware of the revised strikes to avoid mispricing or settlement errors. The reduction in strike prices by Rs 270 across the board (e.g., 5200 → 4930, 6000 → 5730, 7000 → 6730) directly impacts the moneyness of existing option positions. Failure to load updated contract files before the ex-date could result in trading errors.

### Revised Strike Prices (Annexure 1 — OPTSTK, Expiry: 26-MAY-2026)

| Sr. No. | Old Strike | Revised Strike |
|---------|------------|----------------|
| 1 | 5200.00 | 4930.00 |
| 2 | 6000.00 | 5730.00 |
| 3 | 6200.00 | 5930.00 |
| 4 | 6300.00 | 6030.00 |
| 5 | 6400.00 | 6130.00 |
| 6 | 6500.00 | 6230.00 |
| 7 | 6600.00 | 6330.00 |
| 8 | 6700.00 | 6430.00 |
| 9 | 6800.00 | 6530.00 |
| 10 | 6900.00 | 6630.00 |
| 11 | 7000.00 | 6730.00 |