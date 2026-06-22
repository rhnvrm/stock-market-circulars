---
category: market-operations
circular_id: 29cf0f48c88ca488
date: '2026-06-22'
description: BSE will conduct live trading sessions from its Hyderabad Disaster Recovery
  site for Equity, Equity Derivatives, SLB, Currency Derivatives, Commodity Derivatives,
  and Electronic Gold Receipts segments on June 22-23, 2026, during normal market
  timings.
draft: false
guid: https://www.bseindia.com/downloads/UploadDocs/Notices/20260622-1/20260622-1.pdf
impact: high
impact_ranking: high
importance_ranking: high
justification: This circular affects all trading members across all major segments
  requiring immediate technical configuration changes for DR site connectivity on
  June 22-23, 2026.
pdf_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260622-1/20260622-1.pdf
processing:
  attempts: 1
  content_hash: 7f7b1cfb8bf6f810
  processed_at: '2026-06-22T04:16:04.603137'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-22T02:30:47+00:00'
rss_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260622-1/20260622-1.pdf
severity: high
source: bse
stocks: []
tags:
- live-activities-schedule
- mock-trading
- settlement-calendar
- bse
- special-trading
title: Live Trading Session from BSE Disaster Recovery (DR) Site – All Segments
---

## Summary

BSE will conduct live trading sessions from its Hyderabad Disaster Recovery (DR) site for Equity, Equity Derivatives, SLB, Currency Derivatives, Commodity Derivatives, and Electronic Gold Receipts segments on Monday 22nd June and Tuesday 23rd June 2026. Trading will proceed at normal market timings. All trading members are required to configure DR site connection parameters in their trading applications before the sessions.

## Key Points

- Live trading from BSE's Disaster Recovery (DR) site is scheduled for June 22–23, 2026 during normal market timings
- Applicable segments: Equity, Equity Derivatives, SLB, Currency Derivatives, Commodity Derivatives, and Electronic Gold Receipts
- All leased line terminal users must add a secondary DNS entry (Alternate DNS server IP: 10.1.22.162) in addition to the existing primary DNS (10.1.125.122) — this is a one-time change
- Trading members must configure Hyderabad DR site technical connection parameters (Annexure 1) in their trading applications if not already done
- BOLT TWS users can update settings via the configuration setting window; ETI users must configure DR connection parameters in their ETI-based trading application
- Web-based exchange systems (RTRMS, ZT, CLASS collateral, Extranet, etc.) are accessible via DR site URLs provided in Annexure 2 using existing credentials
- Online trade file application users must update the remote server IP and port settings in setting.ini as per Annexure 2

## Regulatory Changes

No permanent regulatory changes. This is an operational notice for a scheduled live DR site trading exercise requiring temporary technical reconfiguration by all trading members.

## Compliance Requirements

- **All leased line terminal users**: Add secondary DNS IP 10.1.22.162 as the Alternate DNS server entry (one-time change)
- **BOLT TWS users**: Update DR connection parameters in the configuration setting window using Hyderabad DR site parameters from Annexure 1
- **ETI-based system users**: Configure DR connection parameters in their ETI trading application as per Annexure 1
- **Online trade file application users**: Update remote server IP and port in setting.ini per Annexure 2
- It is recommended to maintain DR site connection parameters in trading applications on an ongoing basis for future DR sessions
- For queries: BSE Tech Support at 022-22728053 / bse.tech@bseindia.com; BSE Helpdesk at 022-45720400/600 & 022-69158500 / bsehelp@bseindia.com

## Important Dates

- **June 22, 2026 (Monday)**: Live trading from DR site begins, normal market timings
- **June 23, 2026 (Tuesday)**: Live trading from DR site continues, normal market timings

## Impact Assessment

This circular has high operational impact for all BSE trading members. All members using leased line connections must make a one-time DNS configuration change to ensure seamless connectivity during both primary and DR site operations. Members who fail to configure DR parameters risk connectivity disruptions during the June 22–23 live DR trading sessions. The exercise spans all major market segments, meaning any misconfiguration could affect trading across equities, derivatives, currency, commodity, and EGR markets simultaneously. Members are advised to complete technical setup prior to market open on June 22, 2026.