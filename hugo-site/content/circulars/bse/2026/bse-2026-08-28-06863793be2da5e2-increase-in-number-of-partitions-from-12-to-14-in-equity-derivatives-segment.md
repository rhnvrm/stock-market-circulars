---
category: market-operations
circular_id: 06863793be2da5e2
date: '2026-08-28'
description: BSE announces the increase in the number of partitions in the Equity
  Derivatives segment from 14 to 16, effective September 7, 2026, with mock trading
  scheduled for September 5, 2026.
draft: false
guid: https://www.bseindia.com/downloads/UploadDocs/Notices/20260828-12/20260828-12.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Involves technical infrastructure updates for trading members regarding
  partition expansion in the equity derivatives segment, requiring ETI and EOBI/EMDI
  application changes.
pdf_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260828-12/20260828-12.pdf
processing:
  attempts: 1
  content_hash: 54ef6b659841903f
  processed_at: '2026-08-28T15:13:50.219497'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-08-28T12:03:20+00:00'
rss_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260828-12/20260828-12.pdf
severity: medium
source: bse
stocks: []
tags:
- derivatives
- equity-derivatives
- trading-operations
- mock-trading
- market-data
title: Increase in Number of Partitions from 14 to 16 in Equity Derivatives Segment
---

## Summary

BSE has announced an increase in the number of partitions in the Equity Derivatives segment from 14 to 16, effective September 7, 2026. Trading members must update their ETI, EMDI, and EOBI applications to support the new partition structure.

## Key Points

- Number of partitions in the Equity Derivatives segment increases from 14 to 16.
- Effective date for the 16-partition setup is September 7, 2026.
- Partition details are available in the EQD master file (EQD_CODDMMYY.csv) under column 13.
- Partitions 15 and 16 are already available in the Simulation environment for testing.
- A mock trading session will be held on September 5, 2026.

## Regulatory Changes

- Expansion of equity derivatives trading infrastructure from 14 to 16 partitions to accommodate product distribution and multicast data streams.

## Compliance Requirements

- Trading members must update ETI applications utilizing Partition ID to query for 16 partitions instead of 14.
- Members must modify EMDI and EOBI applications to handle partition-wise multicast streams for products moved to partitions 15 and 16.

## Important Dates

- Simulation Testing: August 2026 onwards
- Mock Trading Session: September 5, 2026
- Effective Date: September 7, 2026

## Impact Assessment

- Requires technical changes by trading members for order routing, trade retransmission, and market data (EMDI/EOBI) streaming applications.