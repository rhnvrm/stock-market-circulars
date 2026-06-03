---
category: trading
circular_id: f45f183b299ac6be
date: '2026-06-03'
description: NSE notifies adjustment of F&O contracts for TRENT LIMITED on account
  of a 1:2 bonus issue effective 04-June-2026, with an adjustment factor of 1.5, revised
  lot sizes, strike prices, and quantity freeze limits.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP74527.pdf
impact: high
impact_ranking: high
importance_ranking: high
justification: Directly affects all open F&O positions in TRENT; traders must reload
  contract files before ex-date to avoid trading on stale lot sizes and strike prices.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP74527.pdf
processing:
  attempts: 1
  content_hash: ec200360901f2095
  processed_at: '2026-06-03T17:10:35.784921'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-03T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP74527.pdf
severity: high
source: nse
stocks:
- TRENT
tags:
- bonus
- adjustment-of-futures-and-options-contracts
- price-adjustment
- ex-date
- lot-size-change
- freeze-quantity
- trent
title: 'BONUS: Adjustment of Futures and Options Contracts in TRENT (Ratio 1:2, Ex-Date
  04-Jun-2026)'
---

## Summary

NSE has announced adjustments to Futures and Options contracts for **TRENT LIMITED (TRENT)** pursuant to a **1:2 bonus issue** (1 bonus share for every 2 shares held). The ex-date and effective date is **04-June-2026**. An adjustment factor of **1.5** will be applied, resulting in revised lot sizes and option strike prices across all open contracts.

## Key Points

- **Symbol:** TRENT | **Company:** TRENT LIMITED
- **Corporate Action:** Bonus Issue in ratio **1:2**
- **Face Value:** Re 1/-
- **Ex-date / Effective date:** 04-June-2026
- **Adjustment Factor:** 1.5
- **Revised Market Lot:** June Expiry — **150**; July Expiry Onwards — **225** (as per circular 73549 dated 30-Mar-2026)
- **Revised Quantity Freeze Limit:** **9,000**
- All existing option strike prices are adjusted by dividing by the adjustment factor of 1.5 (e.g., ₹3,500 → ₹2,333.35, ₹4,500 → ₹3,000.00)
- Revised strike scheme (Annexure 2) is effective from the **trade date after the ex-date**
- Adjusted strike/futures base prices and lot sizes may appear in decimal places and will be rounded to the nearest tick size / integer

## Regulatory Changes

In line with SEBI guidelines on corporate action adjustments to derivatives contracts, NSE has revised:
1. Market lot sizes for all TRENT F&O contracts
2. Option strike prices across all June 2026 expiry contracts (see Annexure 1 for full mapping)
3. Quantity freeze limits
4. Strike scheme (Annexure 2) effective post ex-date trade date

## Compliance Requirements

- **Members must load updated contract files** — `NSE_FO_contract_ddmmyyyy.csv.gz` and `NSE_FO_spdcontract_ddmmyyyy.csv.gz` — from the Extranet server (`faoftp/faocommon`) onto their trading applications **before trading on the ex-date (04-June-2026)**.
- Updated MII contract and spread files are also available on the NSE website at: https://www.nseindia.com/all-reports-derivatives
- Position adjustment methodology will be separately communicated by the respective Clearing Corporation.

## Important Dates

| Event | Date |
|---|---|
| Circular Date | 03-June-2026 |
| Ex-date / Effective Date (lot size & strike price changes) | 04-June-2026 |
| Revised Strike Scheme effective | Trade date after 04-June-2026 |
| June Expiry | 30-June-2026 |

## Impact Assessment

All participants holding open positions in TRENT Futures or Options contracts are directly impacted. The adjustment factor of 1.5 reduces all strike prices proportionally (e.g., ₹4,500 becomes ₹3,000) and increases lot sizes (June: 150; July+: 225), reflecting the increased share count post-bonus. Traders who fail to update contract files before market open on 04-June-2026 risk order rejections or incorrect position sizing. The quantity freeze limit increases to 9,000 units, providing greater flexibility for large trades post-adjustment.