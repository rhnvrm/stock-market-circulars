---
category: trading
circular_id: c63e5668e7fd628b
date: '2026-02-27'
description: NSE revises quantity freeze limits for derivatives contracts on five
  major indices including NIFTY, BANKNIFTY, FINNIFTY, MIDCPNIFTY, and NIFTYNXT50,
  effective March 02, 2026. Members must update contract files before trading on the
  effective date.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP73039.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Routine periodic update to quantity freeze limits for index derivatives;
  operationally significant for large F&O traders and members but does not represent
  a major regulatory or structural change.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP73039.pdf
processing:
  attempts: 1
  content_hash: c645bbc8368bb576
  processed_at: '2026-02-27T16:02:36.286881'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-02-27T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP73039.pdf
severity: medium
source: nse
stocks:
- BANKNIFTY
- NIFTY
- FINNIFTY
- MIDCPNIFTY
- NIFTYNXT50
tags:
- futures-options
- quantity-freeze
- derivatives
- indices
- banknifty
- nifty
- finnifty
- midcpnifty
- niftynxt50
- f-and-o
- contract-specifications
title: Quantity Freeze Limits for Indices Effective March 2, 2026
---

## Summary

NSE has revised the quantity freeze limits for futures and options contracts on five major indices under the provisions of Chapter 1.8 of the F&O Consolidated Circular (NSE/FAOP/67775, dated April 30, 2025). The updated limits will come into effect from **March 02, 2026**. Members are required to load updated contract files into their trading systems before the effective date.

## Key Points

- Quantity freeze limits revised for five index derivatives: BANKNIFTY, NIFTY, FINNIFTY, MIDCPNIFTY, and NIFTYNXT50
- Effective date: **March 02, 2026**
- Members must update `contract.gz` and `NSE_FO_contract_ddmmyyyy.csv.gz` files prior to trading on the effective date
- Contract files are available on the NSE Extranet server at `faoftp/faocommon`
- Updated contract files also accessible via the NSE website at the All Reports – Derivatives section

## Regulatory Changes

Updated quantity freeze limits as per the computation methodology in F&O Consolidated Circular NSE/FAOP/67775 (April 30, 2025):

| Index Symbol | Quantity Freeze Limit |
|---|---|
| BANKNIFTY | 600 |
| NIFTY | 1800 |
| FINNIFTY | 1200 |
| MIDCPNIFTY | 2800 |
| NIFTYNXT50 | 600 |

## Compliance Requirements

- **All trading members** must load the updated `contract.gz` and `NSE_FO_contract_ddmmyyyy.csv.gz` file into their trading applications **before** trading commences on March 02, 2026
- Contract files can be obtained from the Extranet server directory `faoftp/faocommon`
- Members can alternatively download the contract file from the NSE website: [https://www.nseindia.com/all-reports-derivatives](https://www.nseindia.com/all-reports-derivatives)
- Details of quantity freeze limits per underlying are also available at: [https://www.nseindia.com/products-services/equity-derivatives-contract-information](https://www.nseindia.com/products-services/equity-derivatives-contract-information)

## Important Dates

- **February 27, 2026**: Circular issued
- **March 02, 2026**: New quantity freeze limits become effective; updated contract files must be loaded before trading begins

## Impact Assessment

This circular affects all NSE members who trade index futures and options. Orders exceeding the specified quantity freeze limits will be rejected by the exchange systems. Members with automated or algorithmic trading strategies that involve large lot sizes must ensure their systems are configured to respect the new limits before March 02, 2026. Failure to update contract files may result in order rejection or trading disruptions on the effective date. The limits apply specifically to BANKNIFTY, NIFTY, FINNIFTY, MIDCPNIFTY, and NIFTYNXT50 derivatives.