---
category: market-operations
circular_id: c9a8e82ef404c5ff
date: '2026-03-13'
description: BSE announces mock trading session for the Currency Derivatives segment
  on Saturday, March 14, 2026, providing DR connection parameters for BOLT Plus trading
  system and web-based applications.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={3F47E931-1431-4C6A-BC13-592D4BEC248C}&noticeno=20260313-4&dt=03/13/2026&icount=4&totcount=60&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading drill for Currency Derivatives segment; operational/technical
  in nature with no regulatory changes or market-wide impact beyond member connectivity
  preparation.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260313-4&attachedId=dd3b6e0c-35a0-498c-a31e-70bef847a296
processing:
  attempts: 1
  content_hash: 1f2d3c7841acb8e8
  processed_at: '2026-03-13T21:38:05.740777'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-03-13T06:42:31+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={3F47E931-1431-4C6A-BC13-592D4BEC248C}&noticeno=20260313-4&dt=03/13/2026&icount=4&totcount=60&flag=0
severity: low
source: bse
stocks: []
tags:
- mock-trading
- currency-derivatives
- bolt-plus
- eti
- dr-site
- technical
- trading-members
title: Mock Trading on Saturday, March 14, 2026 for Currency Derivatives Segment
---

## Summary

BSE has announced a mock trading session for the Currency Derivatives (CDX) segment on Saturday, March 14, 2026. The circular provides technical connection parameters for trading members to connect to the Disaster Recovery (DR) site of the BOLT Plus trading system during the mock session.

## Key Points

- Mock trading will be conducted on Saturday, March 14, 2026 for the Currency Derivatives segment
- Trading members must use DR site connection parameters during the session
- BOLT TWS users need to update configuration settings via the scrip profile icon or `Shift+F12` shortcut
- ETI API users must update connection parameters in their trading applications
- DR Primary IP: `10.255.241.26`, Port: `13910`
- DR Secondary IP: `10.255.241.27`, Port: `13910`
- Web-based BSE systems (RTRMS, EBOSS, LEIPS, Extranet, etc.) accessible via provided URLs using existing credentials

## Regulatory Changes

No regulatory changes. This is a routine operational drill to test DR site connectivity for the Currency Derivatives segment.

## Compliance Requirements

- Trading members participating in mock trading must reconfigure their BOLT TWS or third-party/in-house ETI API applications to use the DR site IP addresses and ports prior to the session
- Members using web-based systems should use the DR URLs/IPs provided for RTRMS, Collateral & Early Pay-In, EBOSS, LEIPS, SME Market Making Compliance System, Extranet, Extranet Plus, iBBS, IML, and Online Trade File (OTD) applications
- Online Trade File users must update `REMOTE SERVER IP` and port in their `setting.ini` file (DR IP: `10.1.101.201`, Port: `9001`; Special Request Port: `9000`)

## Important Dates

- **Mock Trading Date:** Saturday, March 14, 2026 — Currency Derivatives segment

## Impact Assessment

Impact is limited to trading members active in the Currency Derivatives segment who need to participate in the mock session. No market-wide disruption is expected. Members must ensure technical readiness by updating DR connection parameters before the session. This is a standard business continuity preparedness exercise with no effect on live trading or settlement.