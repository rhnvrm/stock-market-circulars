---
category: market-operations
circular_id: 788ab3bd9d92f2a7
date: '2026-10-14'
description: NSE updates closing price broadcast transaction codes and extends the
  discontinuation date for legacy Extranet and NNF API Bhavcopy reports to December
  07, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD76877.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Provides revised transition timelines and transaction codes for EOD
  information dissemination and Bhavcopy reports across multiple segments.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD76877.pdf
processing:
  attempts: 1
  content_hash: e7c4011dfcf0e2dd
  processed_at: '2026-10-14T14:37:25.474699'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-10-14T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD76877.pdf
severity: medium
source: nse
stocks: []
tags:
- bhavcopy
- market-operations
- trading-apis
- extranet
- nnf-api
title: Streamlining EOD information dissemination related to Bhavcopy - Update
---

## Summary

National Stock Exchange (NSE) has issued an update regarding the streamlining of End-of-Day (EOD) information dissemination related to Bhavcopy. The circular provides revised discontinuation dates for legacy Bhavcopy reports on Extranet and NNF API broadcast, and outlines transaction codes for broadcasting closing prices across various segments.

## Key Points

- Closing price broadcast transaction codes updated for COM, FO, and CD segments effective November 16, 2026 (`BCAST_ONLY_MBP` (7208) and `BCAST_ENHNCD_ONLY_MBP` (17208)).
- CM and EGR segments currently disseminate closing prices via `BCAST_ONLY_MBP` (7208).
- Discontinuation date for Mode 1 (Bhavcopy reports on Extranet) extended from November 16, 2026, to December 07, 2026.
- Discontinuation date for Mode 2 (Bhavcopy .MS & .MD via NNF API broadcast for CM, FO, CD, COM, EG and Index) extended from November 16, 2026, to December 07, 2026.

## Regulatory Changes

- Extension of transition timelines for members to adapt to new EOD dissemination mechanisms and discontinuation of legacy Extranet and NNF API Bhavcopy formats.

## Compliance Requirements

- Members must update their trading systems and API integrations to process closing prices via the specified transaction codes and prepare for the discontinuation of legacy Bhavcopy reports by December 07, 2026.

## Important Dates

- November 16, 2026: Effective date for closing price broadcasts in COM, FO, and CD segments via trading APIs.
- December 07, 2026: Revised discontinuation date for Mode 1 (Extranet Bhavcopy reports) and Mode 2 (NNF API broadcast Bhavcopy .MS & .MD files).

## Impact Assessment

- Operational impact on trading members and vendors relying on legacy Extranet and NNF API Bhavcopy formats, requiring updates to automated data ingestion pipelines before December 07, 2026.