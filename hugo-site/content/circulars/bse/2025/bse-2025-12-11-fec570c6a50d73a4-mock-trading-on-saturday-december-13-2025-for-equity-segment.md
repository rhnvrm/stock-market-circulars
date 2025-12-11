---
category: market-operations
circular_id: fec570c6a50d73a4
date: '2025-12-11'
description: BSE announces mock trading session on Saturday, December 13, 2025, for
  the Equity segment to test disaster recovery (DR) site connectivity and systems.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={CE54B4DF-CF73-4CFF-A58A-88677E0C39F2}&noticeno=20251211-53&dt=12/11/2025&icount=53&totcount=88&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Mock trading session for disaster recovery testing is operationally
  important for trading members to ensure business continuity preparedness but does
  not affect regular market operations or trading.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251211-53&attachedId=761903c9-52e3-4901-8fec-c14cda78483c
processing:
  attempts: 1
  content_hash: bb87a8db57753865
  processed_at: '2025-12-11T15:45:23.990561'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-11T14:01:56+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={CE54B4DF-CF73-4CFF-A58A-88677E0C39F2}&noticeno=20251211-53&dt=12/11/2025&icount=53&totcount=88&flag=0
severity: medium
source: bse
stocks: []
tags:
- mock-trading
- disaster-recovery
- equity-segment
- bolt-plus
- trading-system
- business-continuity
- testing
title: Mock Trading on Saturday, December 13, 2025, for Equity Segment
---

## Summary

BSE has scheduled a mock trading session on Saturday, December 13, 2025, for the Equity segment to test disaster recovery (DR) site connectivity. Trading members are required to connect to the DR site of BOLT Plus trading system using modified technical connection parameters. The mock session will test various systems including BOLT TWS, ETI APIs, and web-based applications like RTRMS, CLASS collateral, and Extranet.

## Key Points

- Mock trading session scheduled for Saturday, December 13, 2025, for Equity segment
- Trading members must connect to DR site of BOLT Plus trading system
- Two connection methods available: BOLT TWS and 3rd party trading applications via ETI APIs
- DR site connection parameters provided for both primary and secondary connections
- ETI API Primary DR: IP 10.255.241.10, Port 18909
- ETI API Secondary DR: IP 10.255.241.11, Port 18909
- Web-based systems (RTRMS, EBOSS, LEIPS, Extranet) accessible through specific DR URLs
- Configuration changes required in trading applications to connect to DR site

## Regulatory Changes

No regulatory changes introduced. This is a scheduled mock trading session for disaster recovery testing purposes.

## Compliance Requirements

- Trading members must participate in the mock trading session
- Members using BOLT TWS must change technical connection parameters in configuration settings (accessible via scrip profile icon or Shift+F12 shortcut)
- Members using 3rd party trading applications must update ETI API connection parameters to DR site IPs and ports
- Members must test connectivity to all relevant web-based systems during the mock session
- Members using Online Trade File application must update remote server IP and port settings in the setting.ini file

## Important Dates

- **December 13, 2025 (Saturday)**: Mock trading session for Equity segment at disaster recovery site

## Impact Assessment

**Operational Impact**: Medium - Trading members need to prepare by understanding and implementing DR connection parameters. This requires technical configuration changes in their trading systems.

**Market Impact**: Low - This is a mock session on a non-trading day (Saturday) and will not affect regular market operations.

**Business Continuity Impact**: High - This exercise is critical for ensuring trading members can seamlessly switch to DR site during actual disaster scenarios, ensuring market continuity.

**Technical Requirements**: Trading members must have technical teams ready to:
- Modify BOLT TWS configuration settings
- Update ETI API parameters in 3rd party applications
- Test web-based system connectivity through DR URLs
- Verify both leased line and internet connectivity options