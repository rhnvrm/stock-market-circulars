---
category: market-operations
circular_id: 70cf358d8a4f3aa9
date: '2026-04-06'
description: NSE outlines modalities for acting as an alternative trading venue for
  BSE during outages, including handling of BSE-exclusive equity derivatives contracts
  with specific symbol conventions and trading rules.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP73629.pdf
impact: high
impact_ranking: high
importance_ranking: high
justification: Mandated by SEBI circular; introduces structural changes to derivatives
  trading infrastructure including new contract identifiers, trading session rules,
  and file formats effective April 13, 2026.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP73629.pdf
processing:
  attempts: 1
  content_hash: 3f16eca9f70878d0
  processed_at: '2026-04-06T15:54:37.575629'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-04-06T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP73629.pdf
severity: high
source: nse
stocks: []
tags:
- business-continuity
- interoperability
- equity-derivatives
- futures-options
- alternative-trading-venue
- bse-exclusive-contracts
- market-operations
- sebi-directive
title: Business Continuity for Interoperable Segments of Stock Exchanges
---

## Summary

NSE has issued detailed modalities for the Equity Derivatives segment under the SEBI-mandated Business Continuity framework (SEBI/HO/MRD/TPD/P/CIR/2024/167 dated November 28, 2024). When BSE experiences an outage during trading hours, NSE will act as an alternative trading venue, enabling BSE-exclusive derivative contracts to be traded at NSE. This circular specifies the technical and operational requirements members must be aware of.

## Key Points

- NSE will serve as an alternative trading venue for BSE during outages, and vice versa, per SEBI directive
- BSE-exclusive contracts at NSE will have a `$` suffix in the contract symbol (e.g., `SYMBOLABC$`)
- A new `Admission type` value of `2` (BSE listed) will be introduced in contract master files (`contract.gz` field 13, `NSE_FO_contract_ddmmyyyy.csv.gz` field 30)
- Orders in BSE-exclusive contracts will be rejected with error code `16387` on normal trading days when alternative venue is not invoked
- Upon invocation, BSE-exclusive contracts are enabled and a broadcast message is sent to all trading terminals
- Spread contracts and LPP (Liquidity Provider Program) are not applicable for BSE-exclusive contracts
- Pre-open session will be conducted contingent on receiving invocation communication from BSE before market hours

## Regulatory Changes

- Implements SEBI circular SEBI/HO/MRD/TPD/P/CIR/2024/167 (November 28, 2024) requiring exchanges to establish alternative trading venue mechanisms
- Extends existing NSE circular NSE/MSD/67344 (March 28, 2025) with Equity Derivatives-specific modalities
- Introduces new contract master field value (`Admission type = 2`) to distinguish BSE-listed contracts hosted at NSE
- New contract files to be published on Exchange website from April 13, 2026 for market participants to identify BSE-exclusive contracts

## Compliance Requirements

- Members must update their systems to handle the `$`-suffixed BSE-exclusive contract symbols
- Trading systems must correctly handle error code `16387` rejections for BSE-exclusive contracts on non-invocation days
- Members should consume updated contract master files (`contract.gz`, `NSE_FO_contract_ddmmyyyy.csv.gz`) that include the new `Admission type` field value
- Members should be prepared for pre-open sessions that may be triggered on short notice upon BSE invocation
- From April 13, 2026, members should use new contract files available on the Exchange website and extranet paths for identifying and locating BSE-exclusive contracts

## Important Dates

- **April 06, 2026**: Circular issued; modalities effective
- **April 13, 2026**: New contract files to be made available on Exchange website and extranet for identifying BSE-exclusive contracts

## Impact Assessment

This circular has high operational impact for members trading in the Equity Derivatives (F&O) segment. Members and their technology teams need to update order management and risk systems to:
1. Recognize and handle the new `$`-suffixed contract symbols
2. Process the updated contract master field for BSE-listed contracts
3. Handle dynamic enablement/disablement of BSE-exclusive contracts based on invocation status
4. Accommodate potential pre-open sessions triggered by BSE outages

The framework enhances market resilience by ensuring continuity of trading for BSE-listed derivatives even during exchange-level outages, reducing systemic risk in the Indian equity derivatives market.