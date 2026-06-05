---
category: market-operations
circular_id: 6350952f960a1d8d
date: '2026-06-05'
description: NSE extends the deadline for discontinuing Order Snapshot Recovery through
  Solace API for CM, FO, and CD segments, with CM segment mock date set to June 20,
  2026 and FO/CD to July 04, 2026. Members are advised to migrate to TCP/IP method
  on priority with no further extensions expected.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD74567.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical migration circular affecting members using Solace API for
  order snapshot recovery; no further extensions will be granted, making compliance
  time-sensitive for affected members.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD74567.pdf
processing:
  attempts: 1
  content_hash: 2a5b7844b145b07a
  processed_at: '2026-06-05T09:57:37.215601'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-05T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD74567.pdf
severity: medium
source: nse
stocks: []
tags:
- market-data
- order-snapshot
- solace-api
- tcp-ip
- mock-trading
- discontinuation
- member-advisory
title: Extension of Timeline for Discontinuation of Order Snapshot Recovery via Solace
  API for MTBT Broadcast in CM, FO and CD Segments
---

## Summary

NSE has extended the timeline for discontinuing Order Snapshot Recovery via Solace API for MTBT broadcast in the Capital Market (CM), Futures & Options (FO), and Currency Derivatives (CD) segments. This extension follows member feedback on the original circular NSE/MSD/73425 dated March 23, 2026. Members still using the Solace API must migrate to the TCP/IP method immediately as no further extensions will be granted.

## Key Points

- The discontinuation of Order Snapshot Recovery through Solace API has been extended for CM, FO, and CD segments
- CM segment mock discontinuation date: June 20, 2026
- FO and CD segments mock discontinuation date: July 04, 2026
- Migration to TCP/IP method is mandatory; no further extensions will be provided
- TCP/IP connection parameters are provided in the annexure for all three segments
- All other details from circular NSE/MSD/73425 dated March 23, 2026 remain unchanged

## Regulatory Changes

Revision to the discontinuation timeline originally announced in NSE/MSD/73425 (March 23, 2026):

| Functionality | Segment | Revised Mock Discontinuation Date |
|---|---|---|
| Order Snapshot Recovery via Solace API | CM | June 20, 2026 |
| Order Snapshot Recovery via Solace API | FO, CD | July 04, 2026 |

## Compliance Requirements

- Members currently using the Solace API for order book snapshot recovery must migrate to the TCP/IP method on priority
- TCP/IP parameters for migration:
  - **Capital Market (CM):** IP 172.28.124.54, Port 11984
  - **Futures & Options (FO):** IP 172.28.124.54, Port 11989
  - **Currency Derivatives (CD):** IP 172.28.124.54, Port 11985
- Members must monitor and adequately size their infrastructure for market data feeds
- Members are solely responsible for implementing and maintaining redundancy for market data broadcast subscribed from NSEIL
- Members should refer to circulars NSE/MSD/64333 (October 03, 2024), NSE/COMP/56426 (April 20, 2023), and NSE/MEM/26958 (June 19, 2014) regarding use of Exchange data

## Important Dates

- **June 20, 2026 (Mock):** Discontinuation of Order Snapshot Recovery via Solace API for CM segment
- **July 04, 2026 (Mock):** Discontinuation of Order Snapshot Recovery via Solace API for FO and CD segments
- No further extensions will be granted beyond these revised dates

## Impact Assessment

This circular has a moderate operational impact on NSE members who rely on the Solace API for order book snapshot recovery in the CM, FO, and CD segments. Affected members must complete migration to TCP/IP before the mock discontinuation dates or risk disruption to their market data recovery capabilities. NSE has made clear that no further extensions will be provided, making the TCP/IP migration a firm compliance deadline. Members should prioritize testing the TCP/IP connection parameters in the mock environment ahead of the live discontinuation dates.