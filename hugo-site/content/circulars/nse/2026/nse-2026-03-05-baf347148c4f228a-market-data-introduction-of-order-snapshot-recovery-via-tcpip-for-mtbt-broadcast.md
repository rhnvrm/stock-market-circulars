---
category: market-operations
circular_id: baf347148c4f228a
date: '2026-03-05'
description: NSE introduces Order Snapshot Recovery via TCP/IP for Multicast Tick
  by Tick (MTBT) broadcast in Futures & Options and Currency Derivatives segments,
  effective March 9, 2026, with existing Solace API support discontinued from June
  6, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD73149.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical infrastructure change affecting market data access for members
  using MTBT broadcast; requires member action before June 2026 to migrate from Solace
  API to TCP/IP, but no immediate trading restrictions or regulatory compliance obligations.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD73149.pdf
processing:
  attempts: 1
  content_hash: 266c2b95510a7385
  processed_at: '2026-03-05T13:16:51.548924'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-03-05T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD73149.pdf
severity: medium
source: nse
stocks: []
tags:
- market-data
- mtbt
- tcp-ip
- order-snapshot-recovery
- futures-options
- currency-derivatives
- solace-api
- technology
- member-services
title: Market Data - Introduction of Order Snapshot Recovery via TCP/IP for MTBT Broadcast
  in FO and CD Segments
---

## Summary

NSE is introducing Order Snapshot Recovery via TCP/IP for Multicast Tick by Tick (MTBT) broadcast in the Futures & Options (FO) and Currency Derivatives (CD) segments. This supplements and will eventually replace the existing Solace API-based snapshot recovery introduced in February 2021. The new TCP/IP method goes live in the March 7, 2026 mock session and in the production environment from March 9, 2026.

## Key Points

- Order Snapshot Recovery via TCP/IP is being added for MTBT broadcast in FO and CD segments
- FO segment: IP 172.28.124.54, Port 11989
- CD segment: IP 172.28.124.54, Port 11985
- Both TCP/IP and Solace API will coexist during a transition period
- Existing Solace API-based snapshot recovery will be discontinued on June 6, 2026
- Members should use snapshot recovery when large numbers of ticks are missed or when joining the MTBT feed late
- After receiving a snapshot message, client applications must disconnect; reconnection is allowed if disconnected mid-recovery

## Regulatory Changes

No new regulatory mandates. This is a technical enhancement to existing market data infrastructure. The circular references consolidated circular NSE/MSD/67677 dated April 25, 2025, which remains otherwise unchanged.

## Compliance Requirements

- Members using MTBT Order Book Snapshot Recovery must migrate from Solace API to TCP/IP before June 6, 2026
- Members should review and implement updated specifications available on the NSE website under trading system protocols (Order snapshot recovery for MTBT, Version 6.8)
- Client applications must disconnect after receiving snapshot messages and may reconnect if disconnected during recovery

## Important Dates

- **March 7, 2026**: TCP/IP Order Snapshot Recovery available in mock environment
- **March 9, 2026**: TCP/IP Order Snapshot Recovery live in production environment
- **June 6, 2026**: Discontinuation of existing Solace API-based Order Snapshot Recovery

## Impact Assessment

This change primarily impacts members and trading participants who subscribe to MTBT broadcast feeds in FO and CD segments and rely on the Order Book Snapshot Recovery functionality. The coexistence period (March 9 – June 6, 2026) provides approximately three months for members to migrate their client applications from Solace API to TCP/IP. Members who do not migrate before June 6, 2026 will lose snapshot recovery capability. The change is expected to enhance trading experience by enabling greater customization and improving efficiency through the use of standard TCP/IP connectivity.