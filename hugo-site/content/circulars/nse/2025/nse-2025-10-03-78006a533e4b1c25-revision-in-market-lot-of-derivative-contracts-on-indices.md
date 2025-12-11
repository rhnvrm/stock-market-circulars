---
category: trading
circular_id: 78006a533e4b1c25
date: '2025-10-03'
description: SEBI mandated revision in market lot sizes for derivative contracts on
  Nifty 50, Bank Nifty, Nifty Financial Services, and Nifty Mid Select indices effective
  October 28, 2025.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP70616.pdf
impact: high
impact_ranking: high
importance_ranking: high
justification: Significant change to derivative contract specifications affecting
  all F&O traders with positions in major indices. Requires system updates and repositioning
  strategies for existing positions.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP70616.pdf
processing:
  attempts: 1
  content_hash: 37acf691de9f3bdd
  processed_at: '2025-10-06T06:31:58.711279'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-03T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP70616.pdf
severity: high
source: nse
stocks: []
tags:
- banknifty
- derivatives
- finnifty
- futures-options
- lot-size-revision
- market-lot
- midcpnifty
- nifty
- sebi-guidelines
title: Revision in Market Lot of Derivative Contracts on Indices
---

## Summary

NSE announces revision in market lot sizes for derivative contracts on four major indices in compliance with SEBI circular SEBI/HO/MRD-PoD2/CIR/P/2024/00181 dated December 30, 2024. The revised lot sizes will reduce contract sizes for Nifty 50 (75→65), Bank Nifty (35→30), Nifty Financial Services (65→60), and Nifty Mid Select (140→120). Nifty Next 50 remains unchanged at 25 lots. The changes follow a phased implementation with different effective dates for weekly, monthly, quarterly, and half-yearly contracts.

## Key Points

- Nifty 50 market lot reduced from 75 to 65 (13.3% reduction)
- Bank Nifty market lot reduced from 35 to 30 (14.3% reduction)
- Nifty Financial Services market lot reduced from 65 to 60 (7.7% reduction)
- Nifty Mid Select market lot reduced from 140 to 120 (14.3% reduction)
- Nifty Next 50 market lot remains unchanged at 25
- Contract values computed using average closing prices for September 2025
- Members must inform clients with existing positions about the upcoming revisions
- Trading system file updates required before effective dates

## Regulatory Changes

This revision is mandated under SEBI's periodic review framework for derivative contract lot sizes as specified in SEBI circular SEBI/HO/MRD-PoD2/CIR/P/2024/00181 dated December 30, 2024. The revision aims to maintain appropriate contract values based on current market conditions.

## Compliance Requirements

- Members must download and load updated contract files (contract.gz, NSE_FO_contract_ddmmyyyy.csv.gz, spd_contract.gz, NSE_FO_spdcontract_ddmmyyyy.csv.gz) from faoftp/faocommon directory on Extranet server before respective effective dates
- Members must inform all clients holding positions or planning to take positions in quarterly and half-yearly contracts about the lot size revision
- Trading applications must be updated with new contract specifications before trading on effective dates

## Important Dates

- **October 28, 2025 (EOD)**: Circular comes into effect
- **December 23, 2025**: Last weekly expiry with existing lot size
- **December 30, 2025**: Last monthly expiry with existing lot size; lot size revision for all existing quarterly and half-yearly contracts (EOD)
- **January 6, 2026**: First weekly expiry with revised lot size
- **January 27, 2026**: First monthly expiry with revised lot size
- **March 31, 2026**: Expiry date for quarterly and half-yearly contracts affected by lot size revision

## Important Restrictions

- Day spread order book will NOT be available for the following combination contracts:
  - November 2025 – January 2026
  - December 2025 – January 2026
  - December 2025 – February 2026

## Impact Assessment

**Market Impact**: High. The reduction in lot sizes will lower the minimum capital required to trade index derivatives, potentially increasing retail participation. Existing position holders in quarterly and half-yearly contracts must adjust their risk management strategies as their position values will change on December 30, 2025.

**Operational Impact**: Members need to update trading systems, modify risk management systems, and communicate changes to all affected clients. The phased implementation for different expiry cycles adds complexity to position management during the transition period.

**Trading Impact**: Traders with spread positions involving contracts spanning the revision date may face challenges due to unavailability of certain spread order book combinations. The March 2026 quarterly contract will transition to a regular monthly contract after December 2025 expiry.