---
category: market-operations
circular_id: 56ec6db04e7389a9
date: '2026-03-13'
description: BSE announces mock trading session on Saturday, March 14, 2026 for the
  Currency Derivatives segment, providing DR connection parameters for BOLT Plus trading
  system via ETI APIs and web-based systems.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={3F47E931-1431-4C6A-BC13-592D4BEC248C}&noticeno=20260313-4&dt=03/13/2026&icount=4&totcount=6&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Routine mock trading exercise for Currency Derivatives segment; operationally
  significant for trading members who need to update DR connection parameters, but
  no regulatory or market structure changes involved.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260313-4&attachedId=dd3b6e0c-35a0-498c-a31e-70bef847a296
processing:
  attempts: 1
  content_hash: 32c81a66378d978f
  processed_at: '2026-03-13T06:57:08.179797'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-03-13T06:42:31+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={3F47E931-1431-4C6A-BC13-592D4BEC248C}&noticeno=20260313-4&dt=03/13/2026&icount=4&totcount=6&flag=0
severity: low
source: bse
stocks: []
tags:
- mock-trading
- currency-derivatives
- bolt-plus
- eti-api
- dr-site
- trading-members
- connectivity
title: Mock Trading on Saturday, March 14, 2026 for Currency Derivatives Segment
---

## Summary

BSE has scheduled a mock trading session on Saturday, March 14, 2026 for the Currency Derivatives (CDX) segment. The circular provides DR (Disaster Recovery) site connection parameters for the BOLT Plus trading system, enabling trading members to connect via BOLT TWS, third-party applications through ETI APIs, or web-based exchange systems.

## Key Points

- Mock trading session is scheduled for Saturday, March 14, 2026 on the Currency Derivatives segment
- Trading members must update DR connection parameters in their configuration settings
- BOLT TWS users can access configuration via the scrip profile icon or `Shift+F12` shortcut keys
- ETI API users must update IP and port settings in their respective trading applications
- Web-based systems (RTRMS, CLASS, EBOSS, LEIPS, Extranet, iBBS) remain accessible via existing credentials

## Regulatory Changes

No regulatory changes. This is an operational mock trading drill to test DR site connectivity for the Currency Derivatives segment.

## Compliance Requirements

- Trading members connecting via ETI APIs must update the following DR connection parameters:
  - **Primary DR:** IP: 10.255.241.26; Port: 13910
  - **Secondary DR:** IP: 10.255.241.27; Port: 13910
- BOLT TWS users must change technical connection parameters in the configuration settings window at login time
- Members using the Online Trade File (OTD) application must update `setting.ini` with DR parameters:
  - REMOTE SERVER IP: 10.1.101.201
  - REMOTE SERVER PORT: 9001
  - SPECIAL REQUEST PORT: 9000
- Extranet Plus DR connection: IP 10.1.101.196; Port 1000
- IML DR connection: IP 103.47.196.143; Port 8080

## Important Dates

- **Mock Trading Date:** Saturday, March 14, 2026 — Currency Derivatives segment

## Impact Assessment

This mock trading session is a routine DR readiness exercise with medium operational impact for Currency Derivatives segment participants. Trading members and their technology teams must ensure DR connectivity parameters are correctly configured before the session. No market-wide or regulatory impact is expected. The BOLTPLUS Connectivity Manual (v1.16, dated October 6, 2025) provides detailed guidance on ETI, MDI, and EMDI interface configurations.