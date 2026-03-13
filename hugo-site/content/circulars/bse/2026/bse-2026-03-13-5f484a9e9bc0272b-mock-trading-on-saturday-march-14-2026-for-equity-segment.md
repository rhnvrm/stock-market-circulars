---
category: market-operations
circular_id: 5f484a9e9bc0272b
date: '2026-03-13'
description: BSE announces mock trading session on March 14, 2026 for the Equity segment,
  providing DR connection parameters for BOLT Plus trading system and web-based systems.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={C70EEAE6-AD35-4A78-B32B-30C5957C0AF8}&noticeno=20260313-1&dt=03/13/2026&icount=1&totcount=60&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for DR connectivity testing; affects trading
  members' technical setup only and has no direct market or stock-level impact.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260313-1&attachedId=2c90a573-8e8b-4eb3-81fa-7a28d0d04a72
processing:
  attempts: 1
  content_hash: bf9cea59abd52d99
  processed_at: '2026-03-13T21:38:19.395833'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-03-13T06:42:28+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={C70EEAE6-AD35-4A78-B32B-30C5957C0AF8}&noticeno=20260313-1&dt=03/13/2026&icount=1&totcount=60&flag=0
severity: low
source: bse
stocks: []
tags:
- mock-trading
- equity-segment
- bolt-plus
- dr-site
- eti-api
- connectivity
- trading-members
title: Mock Trading on Saturday, March 14, 2026, for Equity Segment
---

## Summary

BSE has scheduled a mock trading session on Saturday, March 14, 2026, for the Equity segment. The circular provides technical DR (Disaster Recovery) connection parameters for trading members to connect to the BOLT Plus trading system and various BSE web-based systems during the mock session.

## Key Points

- Mock trading is scheduled for Saturday, March 14, 2026, for the Equity segment.
- Trading members must update DR connection parameters in their systems prior to the mock session.
- BOLT TWS users must change technical connection parameters via the configuration settings window (accessible via scrip profile icon or Shift+F12).
- Third-party trading applications using ETI APIs must update to DR IP/Port: Primary DR – 10.255.241.10:18909; Secondary DR – 10.255.241.11:18909.
- Web-based systems (RTRMS, EBOSS, LEIPS, Extranet, iBBS, etc.) have dedicated DR URLs and IPs provided.

## Regulatory Changes

No regulatory changes. This is an operational/technical circular for a scheduled mock trading exercise.

## Compliance Requirements

- Trading members participating in the mock session must reconfigure their systems to use the DR connection parameters specified in the annexures.
- BOLT TWS users: Update configuration settings window at login.
- ETI API users: Update remote server IP and port in trading application settings.
- Online Trade File (OTD) users: Update remote server IP and port in the setting.ini file (IP: 10.1.101.203, Port: 9011).

## Important Dates

- **Mock Trading Date:** Saturday, March 14, 2026 (Equity segment)

## Impact Assessment

Low operational impact. This is a routine DR mock trading exercise requiring trading members to temporarily switch to DR connection parameters. It does not affect regular market operations, stock prices, or investor activity. Only technically relevant to trading members who need to validate their DR connectivity.