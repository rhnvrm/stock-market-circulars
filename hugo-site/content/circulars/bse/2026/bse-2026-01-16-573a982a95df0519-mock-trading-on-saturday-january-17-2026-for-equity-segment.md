---
category: market-operations
circular_id: 573a982a95df0519
date: '2026-01-16'
description: BSE announces mock trading session for the equity segment on Saturday,
  January 17, 2026, with DR site connectivity parameters for BOLT Plus trading system.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={65E3D59A-C522-4018-98B9-E22EDD59AD71}&noticeno=20260116-15&dt=01/16/2026&icount=15&totcount=42&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for system testing with no impact on live
  trading or market participants beyond technical preparation
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260116-15&attachedId=6bafc780-3da6-4b40-b815-0c2a81ea9e0c
processing:
  attempts: 1
  content_hash: 1e516e2af743722e
  processed_at: '2026-01-16T13:02:00.623075'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-16T09:58:04+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={65E3D59A-C522-4018-98B9-E22EDD59AD71}&noticeno=20260116-15&dt=01/16/2026&icount=15&totcount=42&flag=0
severity: low
source: bse
stocks: []
tags:
- mock-trading
- equity-segment
- bolt-plus
- dr-site
- connectivity
- trading-members
- eti-api
- bolt-tws
title: Mock Trading on Saturday, January 17, 2026, for Equity Segment
---

## Summary

BSE has scheduled a mock trading session for the equity segment on Saturday, January 17, 2026. Trading members can connect to the Disaster Recovery (DR) site of the BOLT Plus trading system using either BOLT TWS or third-party trading applications through ETI APIs. The circular provides detailed technical connection parameters and web-based system access links for various BSE platforms.

## Key Points

- Mock trading session scheduled for Saturday, January 17, 2026, for equity segment
- Trading members can connect via BOLT TWS or third-party applications using ETI APIs
- DR site connectivity requires configuration changes to technical connection parameters
- ETI API Primary DR connection: IP 10.255.241.10, Port 18909
- ETI API Secondary DR connection: IP 10.255.241.11, Port 18909
- Access to web-based systems (RTRMS, CLASS collateral, Extranet, EBOSS, LEIPS) available through provided URLs
- BOLT TWS users must modify configuration settings using scrip profile icon or Shift+F12 shortcut

## Regulatory Changes

No regulatory changes introduced. This is a technical operational circular for mock trading connectivity.

## Compliance Requirements

- Trading members must update technical connection parameters in their trading applications to connect to DR site
- BOLT TWS users: Change configuration settings at login using scrip profile icon or Shift+F12
- Third-party application users: Update ETI API connection parameters with DR site IP addresses and ports
- Online Trade File users: Modify remote server IP and port settings in setting.ini file (IP: 10.1.101.203, Port: 9011)
- Members should use existing user IDs and passwords for web-based systems

## Important Dates

- **January 17, 2026 (Saturday)**: Mock trading session for equity segment

## Impact Assessment

**Market Impact**: No impact on live trading. This is a routine mock trading session for system testing and DR site connectivity verification.

**Operational Impact**: Trading members need to configure their systems with DR site parameters to participate in the mock trading session. This is a standard technical exercise to ensure system readiness and disaster recovery preparedness.

**Technical Requirements**: Members using various connectivity methods (BOLT TWS, ETI APIs, web-based systems) must adjust configuration parameters as specified. The circular provides comprehensive technical details including IP addresses, ports, and URLs for all BSE trading and support systems.