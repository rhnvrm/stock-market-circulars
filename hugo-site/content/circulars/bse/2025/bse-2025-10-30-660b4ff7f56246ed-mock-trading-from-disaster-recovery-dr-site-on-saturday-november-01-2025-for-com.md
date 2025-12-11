---
category: market-operations
circular_id: 660b4ff7f56246ed
date: '2025-10-30'
description: BSE announces mock trading session from Disaster Recovery site for Commodity
  Derivatives segment on November 01, 2025 to test DR infrastructure and connectivity.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={7301E078-E1B5-41E4-92E3-EA7F9383D457}&noticeno=20251030-55&dt=10/30/2025&icount=55&totcount=63&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational testing exercise for DR infrastructure; requires trading
  members to test connectivity but does not affect live trading or have regulatory
  compliance impact
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251030-55&attachedId=91be77fe-2191-4ea8-a122-9d7eca49b6af
processing:
  attempts: 1
  content_hash: d914b4e1022a897c
  processed_at: '2025-10-30T18:37:33.175461'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-30T14:03:56+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={7301E078-E1B5-41E4-92E3-EA7F9383D457}&noticeno=20251030-55&dt=10/30/2025&icount=55&totcount=63&flag=0
severity: medium
source: bse
stocks: []
tags:
- connectivity
- derivatives
- disaster-recovery
- market-infrastructure
- mock-trading
- trading-platform
title: Mock Trading from Disaster Recovery (DR) Site on Saturday, November 01, 2025
  for Commodity Derivatives Segment
---

## Summary

BSE has scheduled a mock trading session from its Disaster Recovery (DR) site on Saturday, November 01, 2025 for the Commodity Derivatives segment. This exercise is designed to test the DR infrastructure and ensure trading members can successfully connect to backup systems using BOLT Plus trading platform through various connectivity methods including BOLT TWS, third-party applications, and ETI APIs.

## Key Points

- Mock trading session scheduled for November 01, 2025 (Saturday) for Commodity Derivatives segment
- Trading members must connect to DR site using modified technical connection parameters
- Multiple connectivity options available: BOLT TWS, third-party trading applications via ETI APIs, or in-house developed systems
- DR site connectivity parameters differ from production environment
- Web-based systems (RTRMS, CLASS, EBOSS, Extranet) accessible through dedicated DR URLs
- Both leased line and internet connectivity options provided

## Technical Configuration Requirements

### BOLT TWS Users
- Must change technical connection parameters in configuration settings window at login
- Configuration accessible via scrip profile icon or "Shift+F12" shortcut keys

### ETI API Users (3rd Party Applications)
- Primary DR connection: IP 10.255.241.26, Port 14910
- Secondary DR connection: IP 10.255.241.27, Port 14910

### Web-Based Systems DR URLs
- RTRMS: https://rtrms.bseindia.com (Leased Line: http://10.1.101.197/stocks/jsp/rms/index.html)
- CLASS Collateral: https://classseg.bseindia.com/application/applogin/login.aspx
- EBOSS: https://eboss.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp
- Extranet: https://member.bseindia.com/Extranet_Login.aspx
- LEIPS: https://leipsmm.bseindia.com/stocks/jsp/LEIPS/index.jsp
- iBBS: https://ibbs.bseindia.com/

### Online Trade File (OTD) Settings
- Remote Server IP: 10.1.101.201
- Remote Server Port: 9001
- Special Request Port: 9000
- Members must modify settings.ini file with DR connection parameters

## Compliance Requirements

- Trading members must test DR connectivity during the scheduled mock trading session
- Members must configure their trading systems with DR-specific connection parameters
- Existing user IDs and passwords can be used for web-based systems
- Members using third-party or in-house systems must update ETI API connection settings
- Configuration changes are temporary for the DR test and should be reverted post-exercise

## Important Dates

- **Mock Trading Date**: Saturday, November 01, 2025
- **Circular Date**: October 30, 2025

## Impact Assessment

### Market Impact
- No impact on live trading as this is a mock session on a non-trading day (Saturday)
- No effect on actual positions, settlements, or market operations

### Operational Impact
- Trading members must allocate technical resources to participate in DR testing
- Requires temporary reconfiguration of trading systems and applications
- Tests business continuity preparedness and DR infrastructure reliability
- Validates member connectivity to backup systems in disaster scenarios
- Ensures operational resilience of Commodity Derivatives segment

### Technical Impact
- Members must maintain documentation of DR connection parameters
- IT teams need to test both primary and secondary DR connections
- Validates compatibility of third-party applications with DR infrastructure
- Tests web-based system accessibility through DR URLs