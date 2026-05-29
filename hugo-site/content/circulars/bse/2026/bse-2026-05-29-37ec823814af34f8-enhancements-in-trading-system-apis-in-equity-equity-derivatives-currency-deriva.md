---
category: trading
circular_id: 37ec823814af34f8
date: '2026-05-29'
description: BSE updates the rollout schedule for mandatory ETI API v1.6.14 enhancements
  including Algo ID field, new error codes, and revised Location ID. Equity segment
  go-live deferred to July 6, 2026; EGR segment added to scope.
draft: false
guid: https://www.bseindia.com/downloads/UploadDocs/Notices/20260529-13/20260529-13.pdf
impact: high
impact_ranking: high
importance_ranking: high
justification: Mandatory API changes affect all third-party and in-house trading application
  vendors across five segments; non-compliance would prevent trading. Updated go-live
  dates require immediate action from technology teams.
pdf_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260529-13/20260529-13.pdf
processing:
  attempts: 1
  content_hash: 21e6229f332e4b26
  processed_at: '2026-05-29T15:53:20.565904'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-29T09:59:33+00:00'
rss_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260529-13/20260529-13.pdf
severity: high
source: bse
stocks: []
tags:
- trading-system
- api
- mock-trading
- equity-derivatives
- currency-derivatives
- commodity-derivatives
- egr
- live-activities-schedule
title: BSE Trading System API Enhancements – Mandatory Release Update (Equity, F&O,
  Currency, Commodity & EGR Segments)
---

## Summary

BSE has issued an update to circular 20260515-36, revising the go-live schedule for mandatory ETI API v1.6.14 enhancements across Equity, Equity Derivatives, Currency Derivatives, Commodity Derivatives, and EGR segments. The Equity segment go-live has been deferred from June 22, 2026 to July 6, 2026, and EGR segment has been added to the mandatory release scope.

## Key Points

- This is a continuation of circular no. 20260515-36 dated May 15, 2026
- Three API enhancements are included: new Algo ID field in order & quote mass cancellation messages, new error code for debarred clients, and revised identification for Location ID
- EGR segment is now included in the mandatory ETI API v1.6.14 changes
- Test (simulation) environment changes for Equity Derivatives, Currency Derivatives, Commodity Derivatives, and EGR segments were made available from May 26, 2026
- Test environment changes for Equity segment will be available from June 3, 2026
- All third-party vendors and in-house trading application developers must update their systems

## Regulatory Changes

- ETI API version 1.6.14 is now mandatory across all five segments: Equity, Equity Derivatives, Currency Derivatives, Commodity Derivatives, and EGR
- New field: Algo ID added to order and quote mass cancellation messages
- New error code introduced for debarred clients
- Revised identification methodology for Location ID
- EGR segment added to mandatory release scope (previously not included in circular 20260515-36)

## Compliance Requirements

- All third-party trading application vendors must implement the API v1.6.14 changes in their systems before the respective go-live dates
- Members with in-house developed trading applications must also ensure necessary system development
- Testing in the simulation environment is available and should be completed prior to go-live
- For clarifications or technical assistance, contact: bse.tech@bseindia.com or telephone 022-2272-8053

## Important Dates

- May 26, 2026: Test environment changes available for Equity Derivatives, Currency Derivatives, Commodity Derivatives, and EGR segments
- June 3, 2026: Test environment changes available for Equity segment
- June 27, 2026 (Saturday): Mock trading for Equity Derivatives, Currency Derivatives, Commodity Derivatives & EGR segments
- June 29, 2026 (Monday): Live trading go-live for Equity Derivatives, Currency Derivatives, Commodity Derivatives & EGR segments
- July 4, 2026 (Saturday): Mock trading for Equity segment
- July 6, 2026 (Monday): Live trading go-live for Equity segment (deferred from previously announced June 22, 2026)

## Impact Assessment

This update has high operational impact on all market participants using BSE trading APIs. The deferral of the Equity segment go-live by two weeks (from June 22 to July 6, 2026) provides additional time for technology teams but also means a split rollout — derivatives and EGR segments go live first on June 29, followed by Equity on July 6. Firms operating across multiple segments will need to manage a staggered migration. The addition of EGR segment to the mandatory release scope expands the compliance burden for participants active in that segment. Failure to implement changes by go-live dates could result in trading disruptions.