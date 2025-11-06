---
category: trading
circular_id: 5e2f75af7d7b0991
date: '2025-11-06'
description: NSE announces dividend adjustment for BPCL F&O contracts with Rs 7.5
  dividend per share, effective November 7, 2025. Strike prices revised downward by
  dividend amount.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP71148.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Routine dividend adjustment affecting active F&O contracts in BPCL.
  Medium impact as it requires position adjustments and updated contract files for
  all members trading BPCL derivatives.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP71148.pdf
processing:
  attempts: 1
  content_hash: 111f1f4f9245b514
  processed_at: '2025-11-06T12:55:35.199962'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-11-06T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP71148.pdf
severity: medium
source: nse
stocks:
- BPCL
tags:
- dividend
- futures-and-options
- corporate-action
- derivatives
- strike-price-adjustment
title: Dividend Adjustment of Futures and Options Contracts in BPCL
---

## Summary

NSE has announced the adjustment of Futures and Options contracts for Bharat Petroleum Corporation Limited (BPCL) following a dividend declaration of Rs 7.5 per share (face value Rs 10). All existing option strike prices will be revised downward by the dividend amount, effective from the ex-date of November 7, 2025. Members must update their trading systems with new contract files before trading on the ex-date.

## Key Points

- Company: Bharat Petroleum Corporation Limited (BPCL)
- Corporate Action: Dividend payment
- Dividend Amount: Rs 7.5 per share
- Face Value: Rs 10
- Ex-Date and Effective Date: November 7, 2025
- All existing option strike prices reduced by Rs 7.5
- Contract files (contract.gz and MII files) must be updated before trading
- Position adjustment methodology to be communicated separately by Clearing Corporation

## Regulatory Changes

No new regulatory changes. This circular implements existing SEBI guidelines for adjustments to futures and options contracts upon announcement of corporate actions.

## Compliance Requirements

- **Trading Members**: Must load updated contract.gz/MII contract files (NSE_FO_contract_ddmmyyyy.csv.gz) and spread files (NSE_FO_spdcontract_ddmmyyyy.csv.gz) on trading applications before trading on November 7, 2025
- **File Location**: Files available in faoftp/faocommon directory on Extranet server
- **Alternative Source**: MII contract and spread files also available on NSE website at https://www.nseindia.com/all-reports-derivatives
- **Strike Price Adjustments**: Revised strike prices in decimal format rounded to nearest tick size; lot sizes rounded to nearest integer
- **Position Adjustments**: Await separate intimation from respective Clearing Corporation

## Important Dates

- **Circular Date**: November 6, 2025
- **Ex-Date**: November 7, 2025
- **Effective Date**: November 7, 2025
- **Affected Expiries**: November 25, 2025 and December 30, 2025 contracts listed in Annexure 1

## Impact Assessment

**Market Impact**: Medium - affects all active BPCL futures and options positions across November and December expiries. The Rs 7.5 dividend adjustment will shift all strike prices downward, requiring recalibration of trading strategies and risk management systems.

**Operational Impact**: Members must ensure timely system updates to avoid trading disruptions. Failure to load updated contract files may result in incorrect pricing and execution errors. Position holders will see automatic adjustments to their open positions as per Clearing Corporation methodology.

**Trading Impact**: Over 59 option strike prices listed in the circular (27 for November expiry, 32+ for December expiry) will be adjusted. Example adjustments: 280 → 272.50, 300 → 292.50, 350 → 342.50, 400 → 392.50, 420 → 412.50.