---
category: trading
circular_id: 78935e699c2e5bd9
date: '2026-06-17'
description: BSE announces phased live rollout of updated NFCAST API (v6.2) and MDI/EMDI
  API (v1.4.5) in the Equity segment, with go-live dates in July and August 2026 following
  availability in test environment from June 11, 2026.
draft: false
guid: https://www.bseindia.com/downloads/UploadDocs/Notices/20260617-33/20260617-33.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Affects trading members and front-end application vendors who use BSE's
  Market Data APIs; requires system testing and upgrades but does not impact all market
  participants broadly.
pdf_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260617-33/20260617-33.pdf
processing:
  attempts: 1
  content_hash: 58cafde424d84457
  processed_at: '2026-06-17T15:40:00.623446'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-17T13:34:02+00:00'
rss_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260617-33/20260617-33.pdf
severity: medium
source: bse
stocks: []
tags:
- market-data-api
- nfcast
- mdi-emdi
- mock-trading
- closing-auction
- trading-technology
- equity-segment
title: Release of New Version of Market Data API in Equity Segment - Update
---

## Summary

BSE has announced the phased live rollout of updated Market Data Stream APIs in the Equity segment, continuing from earlier circulars dated March 30, 2026, May 15, 2026, and June 10, 2026. The changes, which support Closing Auction Session functionality, have been available in the test environment since June 11, 2026, and will now be progressively deployed to the live environment.

## Key Points

- NFCAST API will be upgraded from Version 5.0 to Version 6.2, with go-live on August 3, 2026 (Mock Trading: August 1, 2026)
- MDI/EMDI API will be upgraded from Version 1.4.4 to Version 1.4.5, with go-live on July 13, 2026 (Mock Trading: July 11, 2026)
- EOBI (Version 1.4) will remain unchanged
- Test environment has been available since June 11, 2026
- This is a continuation of changes related to the Closing Auction Session rollout

## Regulatory Changes

The API structure changes are part of BSE's broader initiative to support Closing Auction Session (CAS) related changes in the Equity segment, as introduced in previous circulars. The new versions incorporate structural modifications to the Market Data Streams to accommodate these changes.

## Compliance Requirements

- Trading members must complete necessary testing of updated APIs in the test environment before go-live dates
- Front-end trading application vendors must update and test their applications to ensure compatibility with the new API versions
- Members should use the test environment to validate their systems ahead of each phased rollout

## Important Dates

| API | Mock Trading | Go-Live |
|---|---|---|
| MDI/EMDI API (v1.4.4 → v1.4.5) | July 11, 2026 | July 13, 2026 |
| NFCAST API (v5.0 → v6.2) | August 1, 2026 | August 3, 2026 |
| EOBI (v1.4) | No change | No change |

Test environment available from: June 11, 2026

## Impact Assessment

This circular directly impacts trading members and front-end trading application vendors who consume BSE's Market Data APIs in the Equity segment. Vendors and members must upgrade their integrations to the new API versions by the respective go-live dates to avoid disruption. The phased rollout (MDI/EMDI in July, NFCAST in August) allows members adequate time for testing. Failure to upgrade could result in loss of market data feed access post go-live. Contact: bse.tech@bseindia.com / 022-2272 8053.