---
category: trading
circular_id: 0840cf7155688f08
date: '2026-03-30'
description: NSE revises market lots for derivatives contracts on 50 individual stocks
  effective April 29, 2026, pursuant to SEBI guidelines for periodic lot size revision
  (SEBI circular dated December 30, 2024).
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP73549.zip
impact: high
impact_ranking: high
importance_ranking: high
justification: Affects derivatives contracts across 50 underlying stocks covering
  major indices constituents; requires members to update trading systems before April
  29, 2026. Lot size changes directly impact margin requirements, position limits,
  and trading strategies for a large number of widely-traded F&O stocks.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP73549.zip
processing:
  attempts: 1
  content_hash: 7d3eb44838763faa
  processed_at: '2026-03-30T16:19:21.418823'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-03-30T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP73549.zip
severity: high
source: nse
stocks:
- FEDERALBNK
- NATIONALUM
- POWERINDIA
- TATASTEEL
- TORNTPHARM
- AMBUJACEM
- BAJAJFINSV
- BAJAJHLDNG
- BDL
- CAMS
- CIPLA
- COFORGE
- COLPAL
- CROMPTON
- DLF
- GAIL
- GODREJPROP
- HCLTECH
- HDFCBANK
- IEX
- INOXWIND
- IREDA
- IRFC
- ITC
tags:
- derivatives
- futures-options
- market-lot
- lot-size-revision
- sebi-guidelines
- FEDERALBNK
- NATIONALUM
- POWERINDIA
- TATASTEEL
- TORNTPHARM
- AMBUJACEM
- BAJAJFINSV
- BAJAJHLDNG
- BDL
- CAMS
- CIPLA
- COFORGE
- COLPAL
- CROMPTON
- DLF
- GAIL
- GODREJPROP
- HCLTECH
- HDFCBANK
- IEX
- INOXWIND
- IREDA
- IRFC
- ITC
title: Revision in Market Lot of Derivative Contracts on Individual Stocks
---

## Summary

NSE has revised the market lots of derivative contracts on 50 individual stocks effective April 29, 2026, in pursuance of SEBI circular SEBI/HO/MRD-PoD2/CIR/P/2024/00181 dated December 30, 2024, which mandates periodic revision of lot sizes. Lot sizes have been revised downwards for 5 stocks, upwards for 43 stocks, left unchanged for 151 stocks, and downwards (with new lot size not a multiple of old lot size) for 2 stocks. The computation is based on the average closing price of underlyings for the period March 2–30, 2026.

## Key Points

- **5 stocks revised downwards (Annexure 1):** FEDERALBNK (5000→2500), NATIONALUM (3750→1875), POWERINDIA (50→25), TATASTEEL (5500→2750), TORNTPHARM (250→125). Effective for May 2026 and later expiries.
- **43 stocks revised upwards (Annexure 2):** Includes AMBUJACEM (1050→1200), BAJAJFINSV (250→300), BAJAJHLDNG (50→75), BDL (350→425), CAMS (750→825), CIPLA (375→425), COFORGE (375→475), COLPAL (225→275), CROMPTON (1800→2150), DLF (825→950), GAIL (3150→3550), GODREJPROP (275→325), HCLTECH (350→400), HDFCBANK (550→650), IEX (3750→4350), INOXWIND (3575→6400), IREDA (3450→4525), IRFC (4250→5425), ITC (1600→revised), and others. Effective for July 2026 and later expiries.
- **151 stocks unchanged** — no action required for those contracts.
- **2 stocks revised downwards** but new lot size is not a multiple of old lot size (Annexure 4) — effective for July 2026 and later expiries.
- HUDCO, PPLPHARMA, TATATECH, and TORNTPOWER were excluded from review as they are being removed from the F&O segment effective April 29, 2026.

## Regulatory Changes

This revision is mandated under SEBI circular SEBI/HO/MRD-PoD2/CIR/P/2024/00181 dated December 30, 2024, which requires periodic review and revision of lot sizes for equity derivative contracts to align contract values with SEBI-prescribed thresholds. Lot sizes are recalculated based on the one-month average closing price of the underlying (March 2–30, 2026).

## Compliance Requirements

- Members must load the updated contract files — `contract.gz`, `spd_contract.gz`, `NSE_FO_contract_ddmmyyyy.csv.gz`, and `NSE_FO_spdcontract_ddmmyyyy.csv.gz` — into their trading applications **before trading on April 29, 2026**.
- These files are available from the directory `faoftp/faocommon` on the Extranet server.
- For Annexure 2 and 4 stocks (revised upwards or non-multiple downward revision), only the far-month July 2026 expiry contracts will carry the revised lot sizes; May 2026 and June 2026 contracts retain existing lot sizes.
- The day spread order book will **not** be available for June 2026 – July 2026 expiry combination contracts for Annexure 2 and 4 stocks.

## Important Dates

- **March 2–30, 2026:** Reference period for average closing price computation.
- **April 29, 2026:** Effective date for all lot size revisions. Members must update trading systems before market open on this date.
  - Annexure 1 (revised downwards): Effective for **May 2026 and later** expiries.
  - Annexure 2 (revised upwards) and Annexure 4 (non-multiple downward): Effective for **July 2026 and later** expiries.

## Impact Assessment

This revision has significant operational and financial impact across F&O market participants:

- **Margin impact:** Downward lot size revisions (Annexure 1) reduce per-contract margin requirements, lowering barriers for retail participants in stocks like TATASTEEL and FEDERALBNK. Upward revisions (Annexure 43) increase margin requirements, potentially reducing retail participation in those contracts.
- **Position limits:** All MWPL and participant-level position limits will need to be recalculated based on new lot sizes.
- **Spread contracts:** The unavailability of the June–July 2026 day spread order book for Annexure 2 and 4 stocks introduces a temporary operational constraint for calendar spread traders.
- **Technology/systems:** Brokers, proprietary traders, and algo systems must update contract master files by April 29, 2026, or face operational disruptions.
- **F&O exclusions:** HUDCO, PPLPHARMA, TATATECH, and TORNTPOWER will cease to have derivatives contracts from April 29, 2026, requiring open positions to be wound down ahead of that date.