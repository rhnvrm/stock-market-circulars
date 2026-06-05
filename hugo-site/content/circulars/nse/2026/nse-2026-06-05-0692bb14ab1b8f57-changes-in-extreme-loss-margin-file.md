---
category: market-operations
circular_id: 0692bb14ab1b8f57
date: '2026-06-05'
description: NSE Clearing Limited modifies the F_AEL_OPT_CONTRACTS_DDMMYYYY.CSV file
  to include all futures and options contracts (not just options strikes) along with
  applicable ELM percentages, effective June 9, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT74569.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational change to ELM data file affecting all F&O members who consume
  the file for risk management; naming convention and format remain unchanged, limiting
  disruption.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT74569.pdf
processing:
  attempts: 1
  content_hash: 29c5650915820c25
  processed_at: '2026-06-05T20:07:37.960807'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-05T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT74569.pdf
severity: medium
source: nse
stocks: []
tags:
- margins
- extreme-loss-margin
- futures-and-options
- elm
- risk-management
- market-operations
- f-and-o-segment
title: 'NSE Clearing: Extreme Loss Margin File to Include All F&O Contracts from June
  9, 2026'
---

## Summary

NSE Clearing Limited has announced a modification to the Extreme Loss Margin (ELM) file `F_AEL_OPT_CONTRACTS_DDMMYYYY.CSV`. Currently, this file lists only options strikes (index and stock). From June 9, 2026, it will be expanded to include all F&O contracts — both futures and options strikes — for indices and stocks, along with the applicable ELM percentage for the date.

## Key Points

- The ELM file `F_AEL_OPT_CONTRACTS_DDMMYYYY.CSV` will be updated to cover all futures and options contracts, not just options strikes.
- The file will include the ELM percentage applicable for each contract on a given date.
- The naming convention (`F_AEL_OPT_CONTRACTS_DDMMYYYY.CSV`) and file format remain unchanged.
- This is a partial modification to NCL Circular Ref. No. 125/2024 (dated October 21, 2024) and Point 40 "Extreme Loss Margin File (AEL)" of the NCL Consolidated Circular Ref. No. 050/2026 (dated April 30, 2026).

## Regulatory Changes

The scope of data published in the Extreme Loss Margin file is being expanded. Previously, only option strikes (index and stocks) were listed. Going forward, the file will provide a comprehensive list of all contracts — futures and options — for both indices and individual stocks, along with the respective ELM percentage.

## Compliance Requirements

- Members should update their systems to process the expanded ELM file, which will now contain futures contracts in addition to options strikes.
- No changes are required to file naming or parsing logic related to format, as the file name and format remain the same.
- Members should validate their risk management and margin calculation workflows to account for the additional contract data.

## Important Dates

- **June 9, 2026**: Changes to the ELM file (`F_AEL_OPT_CONTRACTS_DDMMYYYY.CSV`) take effect.

## Impact Assessment

This change has a moderate operational impact on F&O segment members who consume the ELM file for risk and margin management. The addition of futures contracts to the file provides a more complete picture of ELM obligations across all F&O instruments. Since the file name and format are unchanged, integration disruption is minimal, but members must ensure their downstream systems handle the increased data volume and the inclusion of futures contract records. Risk teams should review ELM-based margin calculations to ensure futures data is correctly processed post-change.