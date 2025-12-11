---
category: market-operations
circular_id: 9d3a7e7b65497f62
date: '2025-10-30'
description: BSE announces mock trading session from Disaster Recovery site on November
  01, 2025 for Equity Derivatives segment to test DR infrastructure and connectivity.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={D1A20CEF-6EDC-41B5-9341-495C7F326CEE}&noticeno=20251030-52&dt=10/30/2025&icount=52&totcount=63&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Scheduled DR mock trading session requires technical configuration
  changes by trading members but does not affect regular trading operations or market
  participants' positions
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251030-52&attachedId=192bd5a0-6e8e-44ec-b3a5-45075e61cb6a
processing:
  attempts: 1
  content_hash: 969c9699bf327a7d
  processed_at: '2025-10-30T18:38:27.806670'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-30T14:03:53+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={D1A20CEF-6EDC-41B5-9341-495C7F326CEE}&noticeno=20251030-52&dt=10/30/2025&icount=52&totcount=63&flag=0
severity: medium
source: bse
stocks: []
tags:
- connectivity
- derivatives
- disaster-recovery
- eti-api
- market-infrastructure
- mock-trading
- trading-platform
title: Mock Trading from Disaster Recovery (DR) Site on Saturday, November 01, 2025
  for Equity Derivatives Segment
---

## Summary

BSE has announced a mock trading session from the Disaster Recovery (DR) site on Saturday, November 01, 2025 for the Equity Derivatives segment. Trading members need to update their technical connection parameters to connect to the DR site using either BOLT TWS or third-party trading applications through ETI APIs. The circular provides detailed connectivity parameters and configuration instructions for various systems.

## Key Points

- Mock trading session scheduled for Saturday, November 01, 2025
- Applies to Equity Derivatives segment only
- Trading members must modify connection parameters to access DR site
- Two connection methods available: BOLT TWS and 3rd party applications via ETI APIs
- DR connection parameters provided for BOLT Plus trading system
- Web-based systems (RTRMS, CLASS collateral, Extranet, etc.) accessible through specific DR URLs
- Configuration changes required in trading applications before the mock session

## Technical Connection Parameters

### BOLT TWS Users
- Must change technical connection parameters in configuration settings window at login
- Access configuration via scrip profile icon or "Shift+F12" shortcut keys

### ETI API Users (3rd Party Applications)
- Primary DR: IP: 10.255.241.16; Port: 15910
- Secondary DR: IP: 10.255.241.17; Port: 15910

### Web-Based Systems DR Links
- RTRMS: https://rtrms.bseindia.com (Internet) / http://10.1.101.197/stocks/jsp/rms/index.html (Leased Line)
- CLASS Collateral: https://classseg.bseindia.com/application/applogin/login.aspx
- EBOSS: https://eboss.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp
- Extranet: https://member.bseindia.com/Extranet_Login.aspx
- LEIPS: https://leipsmm.bseindia.com/stocks/jsp/LEIPS/index.jsp
- iBBS: https://ibbs.bseindia.com/

### Online Trade File (OTD) DR Parameters
- Remote Server IP: 10.1.101.203
- Remote Server Port: 9011
- Settings must be updated in setting.ini file

## Compliance Requirements

- Trading members must update connection parameters in their trading systems before the mock session
- Members using BOLT TWS need to modify configuration settings at login
- Members using third-party applications must update ETI API connection parameters
- Online trade file users must modify remote server IP and port in setting.ini file
- Existing user IDs and passwords will work with DR site web-based systems
- BOLTPLUS Connectivity Manual V1.16 (dated October 6, 2025) provided for reference

## Important Dates

- **Mock Trading Date**: Saturday, November 01, 2025
- **Circular Date**: October 30, 2025

## Impact Assessment

### Operational Impact
- Trading members need to perform technical configuration changes
- Mock session tests DR infrastructure readiness and business continuity capabilities
- No impact on regular trading as session scheduled on non-trading day (Saturday)
- Ensures trading members can seamlessly switch to DR site during actual emergencies

### Technical Impact
- Requires temporary modification of connection parameters
- Tests connectivity for both interactive trading interfaces and market data streams
- Validates web-based system accessibility from DR site
- No impact on live trading positions or regular market operations

### Market Participant Impact
- Limited to trading members and broker-dealers
- No direct impact on retail investors or end clients
- Provides assurance of robust disaster recovery capabilities
- Medium impact as it requires technical coordination but enhances system reliability