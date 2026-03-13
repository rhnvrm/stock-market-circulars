---
category: market-operations
circular_id: 88891ecda08f5a3e
date: '2026-03-13'
description: BSE circular providing technical connection parameters for BOLT Plus
  trading system DR site for the Equity Derivatives segment mock trading session on
  March 14, 2026.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={288B16CB-596B-487E-A60E-CA5A32B353C7}&noticeno=20260313-2&dt=03/13/2026&icount=2&totcount=6&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session notice with technical connectivity parameters
  for DR site; no regulatory changes or market-wide impact, limited to trading members
  needing to update connection settings.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260313-2&attachedId=6da44460-d739-441e-9130-adc84f8b6a56
processing:
  attempts: 1
  content_hash: c52d29dbfcb42d87
  processed_at: '2026-03-13T06:56:20.969104'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-03-13T06:42:29+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={288B16CB-596B-487E-A60E-CA5A32B353C7}&noticeno=20260313-2&dt=03/13/2026&icount=2&totcount=6&flag=0
severity: low
source: bse
stocks: []
tags:
- mock-trading
- equity-derivatives
- bolt-plus
- dr-site
- eti
- connectivity
- trading-system
title: Mock Trading on Saturday, March 14, 2026, for Equity Derivatives Segment
---

## Summary

BSE has issued technical guidance for trading members participating in the mock trading session on Saturday, March 14, 2026, for the Equity Derivatives (EQD) segment. The circular provides DR (Disaster Recovery) site connection parameters for the BOLT Plus trading system and other exchange web-based systems.

## Key Points

- Mock trading session scheduled for Saturday, March 14, 2026, for the Equity Derivatives segment
- Trading members must update connection parameters to use the DR site of BOLT Plus
- DR site accessible via BOLT TWS, third-party ETI API applications, or in-house developed systems
- BOLT TWS users must change technical connection parameters in the configuration settings window (accessible via scrip profile icon or Shift+F12)
- ETI API users must update IP and port settings in their trading applications

## Regulatory Changes

No regulatory changes. This is an operational circular for a scheduled mock trading drill.

## Compliance Requirements

- Trading members using BOLT TWS must update configuration settings at login using the scrip profile icon or Shift+F12 shortcut
- Members using third-party applications via ETI must update connection parameters:
  - Primary DR: IP 10.255.241.16, Port 15910
  - Secondary DR: IP 10.255.241.17, Port 15910
- Members using web-based systems (RTRMS, EBOSS, LEIPS, Extranet, etc.) should use the DR URLs and IP/port details provided
- Online Trade File (OTD) users must update the remote server IP and port in their setting.ini file (IP: 10.1.101.203, Port: 9011)

## Important Dates

- Mock trading session date: Saturday, March 14, 2026

## Impact Assessment

Limited operational impact. Only trading members in the Equity Derivatives segment who participate in the mock trading session need to act. They must temporarily update their connection parameters to DR site settings. No market-wide or investor impact. Normal trading is unaffected as this is a scheduled drill on a non-trading day.