---
category: market-operations
circular_id: b94f723ddb323251
date: '2025-12-18'
description: BSE announces mock trading session for Equity segment on Saturday, December
  20, 2025, with DR site connection parameters and system access details for trading
  members.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={AAE368ED-0B23-4FD5-8935-DFFC82627CF6}&noticeno=20251218-51&dt=12/18/2025&icount=51&totcount=58&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for disaster recovery testing with no
  impact on regular market operations or trading
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251218-51&attachedId=54b31359-a178-4e1e-89ed-ff7e918f96b9
processing:
  attempts: 1
  content_hash: d744e8a115ea9905
  processed_at: '2025-12-18T18:41:18.136273'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-18T14:28:09+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={AAE368ED-0B23-4FD5-8935-DFFC82627CF6}&noticeno=20251218-51&dt=12/18/2025&icount=51&totcount=58&flag=0
severity: low
source: bse
stocks: []
tags:
- mock-trading
- equity-segment
- disaster-recovery
- bolt-plus
- trading-system
- eti-api
- market-operations
title: Mock Trading on Saturday, December 20, 2025 for Equity Segment
---

## Summary

BSE has scheduled a mock trading session for the Equity segment on Saturday, December 20, 2025. The circular provides technical connection parameters for trading members to connect to the DR (Disaster Recovery) site of the BOLT Plus trading system. Trading members can connect using BOLT TWS, third-party trading applications from empanelled vendors, or in-house developed systems through ETI APIs.

## Key Points

- Mock trading session scheduled for Saturday, December 20, 2025 for Equity segment
- Trading members can connect to DR site using BOLT TWS or ETI APIs
- DR connection parameters provided for both primary and secondary sites
- Primary DR: IP 10.255.241.10, Port 18909
- Secondary DR: IP 10.255.241.11, Port 18909
- Configuration changes required in BOLT TWS using Shift+F12 shortcut
- Web-based systems (RTRMS, CLASS, Extranet, EBOSS, LEIPS) accessible through provided URLs
- Both leased line and internet connectivity options available

## Regulatory Changes

No regulatory changes. This is a routine operational communication for mock trading session.

## Compliance Requirements

- Trading members must update technical connection parameters in their trading applications to connect to DR site
- BOLT TWS users must change configuration settings at login using scrip profile icon or Shift+F12
- Third-party application users must update ETI connection parameters with provided DR IP addresses and ports
- Online Trade File users must update setting.ini file with DR remote server IP (10.1.101.201) and port (9001)

## Important Dates

- **December 20, 2025 (Saturday)**: Mock trading session for Equity segment

## Impact Assessment

This is a routine mock trading session with minimal operational impact. Regular trading is not affected as the session occurs on a non-trading day (Saturday). The exercise allows trading members to test their disaster recovery connectivity and ensures business continuity preparedness. Trading members need to perform technical configuration changes only for the mock session. No impact on investors or market participants beyond testing infrastructure readiness.