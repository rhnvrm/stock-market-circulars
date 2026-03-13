---
category: market-operations
circular_id: ff1346e13a5d9a9d
date: '2026-03-13'
description: BSE announces mock trading session for the Electronic Gold Receipts (EGR)
  segment on Saturday, March 14, 2026, providing DR connection parameters for BOLT
  Plus trading system.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={5D9C9339-CD6E-4181-A688-A8579CCAAAEE}&noticeno=20260313-3&dt=03/13/2026&icount=3&totcount=6&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading drill for EGR segment on a Saturday; affects only
  trading members testing DR connectivity and does not impact normal market operations
  or listed securities.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260313-3&attachedId=c844ca4c-4765-45f7-a620-6d2533af3124
processing:
  attempts: 1
  content_hash: 15d57db3bdae18ce
  processed_at: '2026-03-13T06:57:31.342682'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-03-13T06:42:30+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={5D9C9339-CD6E-4181-A688-A8579CCAAAEE}&noticeno=20260313-3&dt=03/13/2026&icount=3&totcount=6&flag=0
severity: low
source: bse
stocks: []
tags:
- mock-trading
- electronic-gold-receipts
- egr
- bolt-plus
- dr-site
- trading-members
- connectivity
- eti-api
- commodity-derivatives
title: Mock Trading on Saturday, March 14, 2026 for Electronic Gold Receipts Segment
---

## Summary

BSE has scheduled a mock trading session for the Electronic Gold Receipts (EGR) segment on Saturday, March 14, 2026. The circular provides technical connection parameters for trading members to connect to the Disaster Recovery (DR) site of the BOLT Plus trading system during this mock session. Members can connect via BOLT TWS, third-party trading applications through ETI APIs, or in-house developed systems.

## Key Points

- Mock trading session scheduled for Saturday, March 14, 2026 for the EGR segment
- Trading members must use DR site connection parameters during the mock session
- BOLT TWS users must update configuration settings via the scrip profile icon or Shift+F12 shortcut
- ETI API users must update their connection parameters to DR-specific IP addresses and ports
- Web-based systems (RTRMS, EBOSS, LEIPS, Extranet, iBBS, etc.) are accessible via provided URLs
- DR connection parameters differ from production parameters and must be set before login

## Regulatory Changes

No permanent regulatory changes. This is an operational circular providing technical parameters for a one-time mock trading drill on the DR site for the EGR segment.

## Compliance Requirements

- Trading members participating in the mock session must update their BOLT TWS or ETI API configuration to use DR site parameters before connecting
- BOLT TWS users: change configuration via scrip profile icon or Shift+F12 during login
- ETI API users must configure:
  - Primary DR – IP: 10.255.241.26; Port: 14910
  - Secondary DR – IP: 10.255.241.27; Port: 14910
- Members using Online Trade File (OTD) application must update remote server IP and port in the setting.ini file (IP: 10.1.101.203; Port: 9011 for leased line; IP: 103.47.196.143; Port: 8080 for internet)
- Members should revert to production parameters after the mock session

## Important Dates

- **March 14, 2026 (Saturday):** Mock trading session for the Electronic Gold Receipts (EGR) segment on BSE DR site

## Impact Assessment

Impact is limited to trading members of the EGR segment who choose to participate in the mock trading session. This is a technical drill to test DR site readiness and member connectivity. No impact on normal market operations, listed securities, or investors. Members not participating are unaffected. The session is confined to a Saturday when regular markets are closed.