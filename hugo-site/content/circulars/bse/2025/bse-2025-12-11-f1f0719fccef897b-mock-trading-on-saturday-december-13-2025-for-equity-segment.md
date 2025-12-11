---
category: market-operations
circular_id: f1f0719fccef897b
date: '2025-12-11'
description: BSE announces mock trading session on Saturday, December 13, 2025, for
  the Equity segment with details on disaster recovery site connection parameters
  and web-based system access.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={CE54B4DF-CF73-4CFF-A58A-88677E0C39F2}&noticeno=20251211-53&dt=12/11/2025&icount=53&totcount=90&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for testing disaster recovery systems,
  no market impact or compliance requirements
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251211-53&attachedId=761903c9-52e3-4901-8fec-c14cda78483c
processing:
  attempts: 1
  content_hash: 41f3f8c18b356c70
  processed_at: '2025-12-11T18:54:11.057432'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-11T14:01:56+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={CE54B4DF-CF73-4CFF-A58A-88677E0C39F2}&noticeno=20251211-53&dt=12/11/2025&icount=53&totcount=90&flag=0
severity: low
source: bse
stocks: []
tags:
- disaster-recovery
- equity
- market-infrastructure
- mock-trading
- trading-platform
title: Mock Trading on Saturday, December 13, 2025, for Equity Segment
---

## Summary

BSE has scheduled a mock trading session for Saturday, December 13, 2025, for the Equity segment. The circular provides technical connection parameters for trading members to connect to the Disaster Recovery (DR) site of the BOLT Plus trading system. Members can connect using BOLT TWS, third-party trading applications from empanelled vendors, or in-house developed systems through ETI APIs.

## Key Points

- Mock trading session scheduled for December 13, 2025 (Saturday) for Equity segment
- Trading members need to change technical connection parameters to connect to DR site
- BOLT TWS users must update configuration settings at login using scrip profile icon or Shift+F12 shortcut keys
- Third-party application users connecting through ETI must use specified DR IP addresses and ports
- Primary DR connection: IP 10.255.241.10, Port 18909
- Secondary DR connection: IP 10.255.241.11, Port 18909
- Web-based systems (RTRMS, CLASS, EBOSS, LEIPS, Extranet) accessible through provided URLs
- Existing user IDs and passwords can be used for web-based systems

## Regulatory Changes

No regulatory changes introduced. This is a routine business continuity and disaster recovery testing exercise.

## Compliance Requirements

- Trading members should ensure their systems are configured to connect to DR site parameters
- Members using BOLT TWS should update configuration settings window with DR connection parameters
- Members using third-party trading applications should update ETI connection parameters (Primary DR: IP 10.255.241.10, Port 18909; Secondary DR: IP 10.255.241.11, Port 18909)
- Members using Online Trade File application should update setting.ini file with remote server IP 10.1.101.203 and Port 9011

## Important Dates

- Mock Trading Session: Saturday, December 13, 2025

## Impact Assessment

This is a routine mock trading session designed to test disaster recovery capabilities and business continuity preparedness. There is no impact on regular market operations or trading activities. The session allows trading members to verify their ability to connect to and operate from the DR site in case of an actual disaster scenario. No market disruption is expected as this occurs on a non-trading day (Saturday).