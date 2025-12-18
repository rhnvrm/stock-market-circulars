---
category: market-operations
circular_id: 37ccdd6ca46a2a1d
date: '2025-12-18'
description: BSE announces mock trading session on Saturday, December 20, 2025 for
  the Equity Derivatives segment with DR site connectivity details for BOLT Plus trading
  system.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={E02DA54A-8420-4FF2-9FD4-C36EE7A5834A}&noticeno=20251218-52&dt=12/18/2025&icount=52&totcount=58&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Mock trading session for disaster recovery testing with no impact on
  regular trading operations; routine operational activity for system preparedness
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251218-52&attachedId=fe41a105-b9cf-4a8a-8c93-5a67ec626a81
processing:
  attempts: 1
  content_hash: f7ae80383bdeab83
  processed_at: '2025-12-18T18:40:56.055898'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-18T14:28:11+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={E02DA54A-8420-4FF2-9FD4-C36EE7A5834A}&noticeno=20251218-52&dt=12/18/2025&icount=52&totcount=58&flag=0
severity: low
source: bse
stocks: []
tags:
- mock-trading
- equity-derivatives
- disaster-recovery
- bolt-plus
- trading-system
- connectivity
- eti-api
- market-operations
title: Mock Trading on Saturday, December 20, 2025 for Equity Derivatives Segment
---

## Summary

BSE has scheduled a mock trading session on Saturday, December 20, 2025, for the Equity Derivatives segment using the Disaster Recovery (DR) site of the BOLT Plus trading system. Trading members can connect through BOLT TWS, third-party trading applications, or in-house developed systems via ETI APIs. The circular provides detailed technical connection parameters for DR site connectivity.

## Key Points

- Mock trading session scheduled for Saturday, December 20, 2025
- Applies to Equity Derivatives segment only
- Trading members must use DR site connection parameters
- Two connection methods available: BOLT TWS and ETI API-based applications
- DR Primary IP: 10.255.241.16, Port: 15910
- DR Secondary IP: 10.255.241.17, Port: 15910
- Access to web-based systems (RTRMS, CLASS, Extranet, etc.) through specific DR URLs provided
- Configuration changes required in trading applications to connect to DR environment

## Technical Connection Details

### BOLT TWS Users
- Must change technical connection parameters in configuration settings window at login
- Configuration settings accessible via scrip profile icon or "Shift+F12" shortcut keys

### ETI API Users (3rd Party/In-house Applications)
- Primary DR Connection: IP 10.255.241.16, Port 15910
- Secondary DR Connection: IP 10.255.241.17, Port 15910

### Web-Based Systems Access
- RTRMS: https://rtrms.bseindia.com (Internet) or http://10.1.101.197/stocks/jsp/rms/index.html (Leased Line)
- CLASS Collateral: https://classseg.bseindia.com/application/applogin/login.aspx
- EBOSS: https://eboss.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp
- Extranet: https://member.bseindia.com/Extranet_Login.aspx
- iBBS: https://ibbs.bseindia.com/
- Existing user IDs and passwords remain valid

## Compliance Requirements

- Trading members must update connection parameters in their trading systems before the mock trading session
- Members using BOLT TWS should modify configuration settings at login
- Members using ETI APIs must update IP and port settings in their trading applications
- Members using online trade file application must change remote server IP and port settings in setting.ini file
- DR Remote Server IP: 10.1.101.201, Port: 9001

## Important Dates

- **Mock Trading Date**: Saturday, December 20, 2025
- **Circular Issue Date**: December 18, 2025

## Impact Assessment

### Market Impact
- No impact on regular trading operations as this is a weekend mock session
- Non-trading day activity for disaster recovery preparedness

### Operational Impact
- Trading members need to prepare and test DR connectivity before the session
- Provides opportunity to validate disaster recovery systems and procedures
- Ensures business continuity preparedness for Equity Derivatives segment
- Routine system testing with minimal disruption to members