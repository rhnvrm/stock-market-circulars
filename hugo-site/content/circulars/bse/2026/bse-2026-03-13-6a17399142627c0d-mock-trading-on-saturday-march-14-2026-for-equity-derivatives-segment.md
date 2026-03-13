---
category: market-operations
circular_id: 6a17399142627c0d
date: '2026-03-13'
description: BSE announces mock trading session for the Equity Derivatives segment
  on Saturday, March 14, 2026, using the DR site of BOLT Plus trading system. Provides
  technical connection parameters for trading members.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={288B16CB-596B-487E-A60E-CA5A32B353C7}&noticeno=20260313-2&dt=03/13/2026&icount=2&totcount=60&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for system readiness testing; affects
  only trading members connecting to the Equity Derivatives segment DR site and does
  not impact live markets or securities.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260313-2&attachedId=6da44460-d739-441e-9130-adc84f8b6a56
processing:
  attempts: 1
  content_hash: e9c8348d705f680a
  processed_at: '2026-03-13T19:24:13.754954'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-03-13T06:42:29+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={288B16CB-596B-487E-A60E-CA5A32B353C7}&noticeno=20260313-2&dt=03/13/2026&icount=2&totcount=60&flag=0
severity: low
source: bse
stocks: []
tags:
- mock-trading
- equity-derivatives
- bolt-plus
- dr-site
- eti-api
- trading-members
- technical-connectivity
title: Mock Trading on Saturday, March 14, 2026, for Equity Derivatives Segment
---

## Summary

BSE has announced a mock trading session for the Equity Derivatives (EQD) segment on Saturday, March 14, 2026. The session will use the Disaster Recovery (DR) site of the BOLT Plus trading system. Trading members are required to update their technical connection parameters to participate in the mock session.

## Key Points

- Mock trading scheduled for Saturday, March 14, 2026, for the Equity Derivatives segment
- Session will use the DR site of the BOLT Plus trading system
- BOLT TWS users must update configuration settings via the scrip profile icon or `Shift+F12` shortcut keys
- Third-party/ETI API users must update DR connection parameters in their trading applications
- Primary DR: IP `10.255.241.16`, Port `15910`
- Secondary DR: IP `10.255.241.17`, Port `15910`
- Web-based systems (RTRMS, CLASS, EBOSS, LEIPS, Extranet, etc.) are accessible via provided URLs during the mock session

## Regulatory Changes

No regulatory changes. This is an operational mock trading exercise to test DR site connectivity and system readiness.

## Compliance Requirements

- Trading members intending to participate must reconfigure their BOLT TWS or third-party trading applications with the specified DR site IP and port parameters before the mock session
- Members using ETI APIs must update `Primary DR – IP: 10.255.241.16; Port: 15910` and `Secondary DR – IP: 10.255.241.17; Port: 15910` in their systems
- Members using web-based systems should use the provided DR URLs with existing credentials

## Important Dates

- **Mock Trading Date:** Saturday, March 14, 2026 (Equity Derivatives segment)

## Impact Assessment

Minimal market impact. This is a routine DR mock trading exercise affecting only trading members in the Equity Derivatives segment. No live trading occurs; the session is purely for technical readiness and connectivity testing of the BSE BOLT Plus DR infrastructure. Members who fail to update connection parameters will be unable to participate in the mock session.