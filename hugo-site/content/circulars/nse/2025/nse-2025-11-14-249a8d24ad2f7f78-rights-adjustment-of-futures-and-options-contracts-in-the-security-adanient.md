---
category: trading
circular_id: 249a8d24ad2f7f78
date: '2025-11-14'
description: NSE announces adjustments to ADANIENT futures and options contracts due
  to rights issue at 3:25 ratio and Rs 1800 issue price, effective November 17, 2025.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP71315.pdf
impact: high
impact_ranking: high
importance_ranking: high
justification: Critical adjustment to all active F&O contracts for ADANIENT affecting
  market lot, strike prices, and trading parameters due to rights issue. Requires
  immediate system updates before ex-date.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP71315.pdf
processing:
  attempts: 1
  content_hash: 8a21f7ac0dcba8ae
  processed_at: '2025-11-14T15:41:36.966430'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-11-14T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP71315.pdf
severity: high
source: nse
stocks:
- ADANIENT
tags:
- futures-and-options
- derivatives
- corporate-action
- rights-issue
- contract-adjustment
- adani-enterprises
title: 'RIGHTS: Adjustment of Futures and Options contracts in ADANIENT'
---

## Summary

NSE has announced adjustments to Futures and Options contracts for Adani Enterprises Limited (ADANIENT) following the announcement of a rights issue. The adjustments will be effective from November 17, 2025 (ex-date). The rights issue is in the ratio of 3:25 at an issue price of Rs 1800 per share with face value of Re 1. The adjustment factor is 0.969485, resulting in revised market lot of 309 units and quantity freeze limit of 9270 units.

## Key Points

- **Symbol**: ADANIENT (Adani Enterprises Limited)
- **Corporate Action**: Rights Issue
- **Rights Ratio**: 3:25 (3 new shares for every 25 existing shares)
- **Issue Price**: Rs 1800 per share
- **Face Value**: Re 1/-
- **Adjustment Factor**: 0.969485
- **Revised Market Lot**: 309 units (adjusted from existing lot size)
- **Revised Quantity Freeze Limit**: 9270 units
- **Underlying Close Price (Last Cum Date)**: Rs 2516.80
- **Benefit per Share**: Rs 76.80

## Regulatory Changes

All futures and options contracts in ADANIENT will undergo adjustments in accordance with SEBI guidelines for corporate actions. The adjustments include:

- Modified strike prices for all outstanding option contracts (rounded to nearest tick size)
- Adjusted futures base prices
- Revised lot sizes (rounded to nearest integer)
- Updated quantity freeze limits

Members must load updated contract.gz and MII contract files (NSE_FO_contract_ddmmyyyy.csv.gz and NSE_FO_spdcontract_ddmmyyyy.csv.gz) before trading on the ex-date.

## Compliance Requirements

- **Trading Members**: Must load updated contract and spread files from faoftp/faocommon directory on Extranet server before November 17, 2025
- **System Updates**: Trading applications must be updated with revised contract specifications before ex-date
- **File Sources**: 
  - Files available on Extranet server at faoftp/faocommon directory
  - Also available on NSE website at https://www.nseindia.com/all-reports-derivatives
- **Position Adjustments**: Methodology will be separately communicated by respective Clearing Corporation
- **Reference Documentation**: Full adjustment details available at https://www.nseindia.com/products-services/equity-derivatives-corporate-actions-adjustments

## Important Dates

- **Circular Date**: November 14, 2025
- **Ex-Date / Effective Date**: November 17, 2025
- **Affected Expiry Dates**: November 25, 2025 contracts (sample strike prices provided in annexure)

## Impact Assessment

**High Impact on Derivatives Trading:**

- All existing ADANIENT futures and options positions will be adjusted proportionately
- Strike prices will change to decimal values (e.g., 2000 becomes 1938.95, 2100 becomes 2035.90)
- Market lot size changes from standard lot to 309 units, affecting order placement and margin calculations
- Traders must recalibrate strategies based on new strike prices and lot sizes
- System failures to update contract files will result in trading disruptions on ex-date
- Options traders need to be aware of revised strike prices for existing positions
- The adjustment factor of 0.969485 indicates approximately 3.05% adjustment to contract values

**Sample Strike Price Adjustments** (November 25, 2025 expiry):
- Old Strike 2000 → New Strike 1938.95
- Old Strike 2100 → New Strike 2035.90
- Old Strike 2140 → New Strike 2074.70

**Operational Impact:**
- Risk management systems must be updated for new lot sizes and freeze limits
- Margin calculations will be affected by revised contract parameters
- All algorithmic trading systems require recalibration before ex-date