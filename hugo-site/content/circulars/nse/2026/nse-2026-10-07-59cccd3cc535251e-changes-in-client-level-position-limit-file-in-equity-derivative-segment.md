---
category: market-operations
circular_id: 59cccd3cc535251e
date: '2026-10-07'
description: NSE Clearing Limited announces that effective November 02, 2026, the
  client-level position limit file (oi_cli_limit) will contain limit information for
  stocks only.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT76766.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Modifies the contents of the client-level position limit file in the
  equity derivative segment, removing index data and retaining stock limits only,
  affecting member trading and risk management systems.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT76766.pdf
processing:
  attempts: 1
  content_hash: b86628efcb25f87d
  processed_at: '2026-10-07T18:55:40.688644'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-10-07T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT76766.pdf
severity: low
source: nse
stocks: []
tags:
- futures-and-options
- market-operations
- position-limit
title: Changes in Client level position limit file in Equity Derivative Segment
---

## Summary

NSE Clearing Limited has announced modifications to the client-level position limit file (`oi_cli_limit_DD-MMM-YYYY.lst`) in the Equity Derivative Segment. Effective November 02, 2026, this file will exclusively contain limit information for stocks, omitting index limit data.

## Key Points

- Reference to NCL consolidated circular NCL/CMPT/73997 dated April 30, 2026.
- The nomenclature of the file remains `oi_cli_limit_DD-MMM-YYYY.lst`.
- Effective date: November 02, 2026.
- Scope change: File will contain limit information for stocks only (index limits removed).

## Regulatory Changes

- Discontinuation of index position limit data within the `oi_cli_limit` file provided by NSE Clearing Limited.

## Compliance Requirements

- Trading and clearing members must update their internal automated systems, risk management software, and data ingestion pipelines to account for the exclusion of index limits from the `oi_cli_limit` file starting November 02, 2026.

## Important Dates

- Date of Circular: October 07, 2026
- Effective Date: November 02, 2026

## Impact Assessment

- Operational impact on members who parse the `oi_cli_limit` file for index position limits, requiring adjustments to data fetching and processing mechanisms.