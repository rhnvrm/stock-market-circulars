---
category: trading
circular_id: 76e891307c5586d1
date: '2026-06-09'
description: NSE announces adjustment of Futures and Options contracts for Infosys
  Limited (INFY) due to a dividend of Rs 25 per share, effective June 10, 2026. Option
  strike prices are revised downward by Rs 25 across all expiries.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP74629.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Routine F&O strike price adjustment for a large-cap stock (Infosys)
  due to a significant dividend of Rs 25 per share. Affects active derivatives traders
  who must reload updated contract files before trading on the ex-date.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP74629.pdf
processing:
  attempts: 1
  content_hash: 8381d82b50964c01
  processed_at: '2026-06-09T14:55:09.053851'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-09T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP74629.pdf
severity: medium
source: nse
stocks:
- INFY
tags:
- dividend
- adjustment-of-futures-and-options-contracts
- price-adjustment
- ex-date
- ex-dividend
- futures-and-options
- infy
- infosys
title: Dividend Adjustment of Futures and Options Contracts for INFY (Infosys Limited)
---

## Summary

NSE's Futures & Options department (Circular Ref. No. 83/2026, Ref No: NSE/FAOP/74629) advises all members of the adjustment to Futures and Options contracts on Infosys Limited (INFY) in accordance with SEBI guidelines for corporate action adjustments. The adjustment is triggered by a dividend of Rs 25 per share (face value Rs 5) with an ex-date and effective date of June 10, 2026.

## Key Points

- **Symbol:** INFY (Infosys Limited)
- **Corporate Action:** Dividend — Rs 25 per share (Face Value: Rs 5)
- **Ex-Date / Effective Date:** June 10, 2026
- All option strike prices for INFY contracts are revised downward by Rs 25 across June 2026 expiry (e.g., 920.00 → 895.00, 1000.00 → 975.00, etc.)
- Revised strike/futures base prices and lot sizes may appear in decimal form and will be rounded to the nearest tick size and nearest integer respectively
- Updated contract details will be reflected in the latest `contract.gz` file

## Regulatory Changes

Pursuant to SEBI guidelines on adjustments to futures and options contracts upon announcement of corporate actions, strike prices for INFY OPTSTK contracts expiring June 30, 2026 are revised. The adjustment reduces all affected strike prices by Rs 25 (equal to the dividend amount). A representative sample of revisions from Annexure 1:

| Old Strike Price | Revised Strike Price |
|-----------------|---------------------|
| 920.00 | 895.00 |
| 960.00 | 935.00 |
| 1000.00 | 975.00 |
| 1040.00 | 1015.00 |
| 1060.00 | 1035.00 |
| 1080.00 | 1055.00 |

Full revised strike price details are available in Annexure 1 of the circular and at the NSE corporate actions adjustments page.

## Compliance Requirements

- Members must load the updated `contract.gz` / MII contract file (`NSE_FO_contract_ddmmyyyy.csv.gz`) and spread file (`NSE_FO_spdcontract_ddmmyyyy.csv.gz`) on their trading applications **before trading on the ex-date (June 10, 2026)**
- These files are available from the `faoftp/faocommon` directory on the Extranet server and on the NSE website under All Reports – Derivatives
- Position adjustment methodology will be separately communicated by the respective Clearing Corporation

## Important Dates

- **Circular Date:** June 9, 2026
- **Ex-Date / Effective Date:** June 10, 2026 (adjustments become effective from this date)
- **Affected Expiry:** June 30, 2026 (OPTSTK contracts)

## Impact Assessment

This is a standard dividend-driven F&O contract adjustment for Infosys Limited, one of India's largest IT companies and a heavily traded derivatives counter. The Rs 25 dividend is substantial relative to the stock price, warranting a 25-point downward revision in all option strike prices to prevent arbitrage opportunities. Traders and members must update contract master files before the market opens on June 10, 2026 to avoid order placement errors or mismatched contract data. Open positions will be adjusted automatically per Clearing Corporation guidelines.