---
category: trading
circular_id: 16a05917dfae7735
date: '2026-05-27'
description: NSE announces adjustment of Futures and Options contracts for Life Insurance
  Corporation of India (LICI) due to a 1:1 bonus issue, effective 29-May-2026, with
  an adjustment factor of 2 and revised market lot of 1400.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP74446.pdf
impact: high
impact_ranking: high
importance_ranking: high
justification: Direct impact on all active F&O traders in LICI — strike prices are
  halved, lot size doubles to 1400, and freeze limits change. Members must reload
  contract files before trading on ex-date to avoid errors.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP74446.pdf
processing:
  attempts: 1
  content_hash: 876ec760b78f4adb
  processed_at: '2026-05-27T16:07:14.999220'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-27T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP74446.pdf
severity: high
source: nse
stocks:
- LICI
tags:
- bonus
- adjustment-of-futures-and-options-contracts
- price-adjustment
- lot-size-change
- ex-date
- lici
- futures-and-options
- freeze-quantity
title: 'BONUS: Adjustment of Futures and Options Contracts in LICI (1:1 Bonus, Ex-Date
  29-May-2026)'
---

## Summary

NSE has announced the adjustment of Futures and Options contracts for **Life Insurance Corporation of India (LICI)** on account of a **1:1 bonus issue**. The ex-date and effective date is **29-May-2026**. All existing F&O contracts will be adjusted using an adjustment factor of 2, which halves all option strike prices and doubles the market lot size.

## Key Points

- **Symbol:** LICI (Life Insurance Corporation of India)
- **Corporate Action:** Bonus issue in ratio 1:1
- **Face Value:** Rs 10/-
- **Ex-Date / Effective Date:** 29-May-2026
- **Adjustment Factor:** 2
- **Revised Market Lot:** 1,400 (doubled from existing)
- **Revised Quantity Freeze Limit:** 56,000
- **Option Strike Prices:** All existing strikes halved (e.g., 660.00 → 330.00, 800.00 → 400.00)
- Members must load updated `contract.gz` / MII contract and spread files before trading on the ex-date
- Revised strike scheme (new strikes added post-bonus) is effective from the trade date **after** the ex-date

## Regulatory Changes

In pursuance of SEBI guidelines for adjustments to F&O contracts on announcement of corporate actions, NSE is adjusting all LICI derivative contracts. Strike prices and base prices may appear in decimal places and will be rounded to the nearest tick size; lot sizes will be rounded to the nearest integer.

## Compliance Requirements

- **All trading members** must load the updated contract files (`NSE_FO_contract_ddmmyyyy.csv.gz`) and spread files (`NSE_FO_spdcontract_ddmmyyyy.csv.gz`) from the Extranet server (`faoftp/faocommon`) onto their trading applications **before trading on 29-May-2026**.
- Files are also available on the NSE website under the derivatives reports section.
- Position adjustment methodology will be separately communicated by the respective Clearing Corporation.

## Important Dates

| Event | Date |
|---|---|
| Circular Date | 27-May-2026 |
| Ex-Date / Effective Date for F&O Adjustment | 29-May-2026 |
| Revised Strike Scheme Effective | Trade date after 29-May-2026 |
| JUN-2026 Options Expiry | 30-Jun-2026 |

## Impact Assessment

**High impact** for all participants holding LICI F&O positions. The 1:1 bonus with an adjustment factor of 2 means:

- All existing option strike prices are **halved** (24 strikes listed for JUN-2026 expiry, ranging from new strikes of 330.00 to 402.50)
- Market lot **doubles to 1,400**, increasing the nominal contract value per lot
- Quantity freeze limit increases to **56,000 units**
- Traders and risk systems must update their models and position limits to reflect the new lot size and strike prices
- Failure to load updated contract files before ex-date will result in trading on stale contract specifications, posing operational risk