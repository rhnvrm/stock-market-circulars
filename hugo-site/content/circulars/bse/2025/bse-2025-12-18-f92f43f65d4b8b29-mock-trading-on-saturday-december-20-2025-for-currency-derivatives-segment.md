---
category: market-operations
circular_id: f92f43f65d4b8b29
date: '2025-12-18'
description: BSE announces mock trading session for Currency Derivatives segment on
  Saturday, December 20, 2025, with DR site connection parameters for BOLT Plus trading
  system.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={8B6DDE84-C923-4EF6-99C8-B6A9CAE7569C}&noticeno=20251218-53&dt=12/18/2025&icount=53&totcount=56&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for disaster recovery testing with no
  impact on regular trading operations or market participants beyond technical teams
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251218-53&attachedId=44701604-8207-4d0d-85c4-9e8aa3fa7134
processing:
  attempts: 1
  content_hash: 93548ff8a78e8ffc
  processed_at: '2025-12-18T15:37:49.508978'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-18T14:28:13+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={8B6DDE84-C923-4EF6-99C8-B6A9CAE7569C}&noticeno=20251218-53&dt=12/18/2025&icount=53&totcount=56&flag=0
severity: low
source: bse
stocks: []
tags:
- mock-trading
- currency-derivatives
- cdx
- disaster-recovery
- bolt-plus
- trading-system
- technical-connectivity
title: Mock Trading on Saturday, December 20, 2025 for Currency Derivatives Segment
---

## Summary

BSE will conduct a mock trading session on Saturday, December 20, 2025, for the Currency Derivatives (CDX) segment. The circular provides technical connection parameters for trading members to connect to the Disaster Recovery (DR) site of the BOLT Plus trading system using either BOLT TWS or third-party trading applications through ETI APIs.

## Key Points

- Mock trading session scheduled for Saturday, December 20, 2025
- Applies to Currency Derivatives segment only
- Trading members must use DR site connection parameters
- Two connectivity options available: BOLT TWS and 3rd party applications via ETI APIs
- Configuration changes required in trading systems to connect to DR site
- DR site connection available through both Primary and Secondary servers

## Technical Connection Parameters

### BOLT TWS Users
- Members must change technical connection parameters in configuration settings window at login
- Configuration settings can be accessed via scrip profile icon or "Shift+F12" shortcut keys

### ETI API Users (3rd Party Applications)
- Primary DR: IP 10.255.241.26, Port 13910
- Secondary DR: IP 10.255.241.27, Port 13910

### Web-Based Systems Access
- RTRMS: https://rtrms.bseindia.com
- Collateral & CLASS: https://classseg.bseindia.com/application/applogin/login.aspx
- EBOSS: https://eboss.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp
- LEIPS: https://leipsmm.bseindia.com/stocks/jsp/LEIPS/index.jsp
- Extranet: https://member.bseindia.com/Extranet_Login.aspx
- iBBS: https://ibbs.bseindia.com/

### Leased Line Connection Parameters
- RTRMS: http://10.1.101.197/stocks/jsp/rms/index.html or http://10.1.101.100/
- EBOSS: https://ebossll.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp
- LEIPS: https://leipsmmll.bseindia.com/stocks/jsp/LEIPS/index.jsp
- Extranet: https://memberll.bseindia.com/

### Online Trade File (OTD) Settings
- Remote Server IP: 10.1.101.203
- Remote Server Port: 9011
- Members must update setting.ini file with DR connection parameters

## Compliance Requirements

- Trading members participating in mock trading must configure their systems with DR site parameters
- Technical teams should update connection settings in BOLT TWS or third-party trading applications
- Members using online trade file application must modify setting.ini file with DR remote server IP and port
- Existing user IDs and passwords can be used for web-based system access

## Important Dates

- Mock Trading Date: Saturday, December 20, 2025
- Circular Issue Date: December 18, 2025

## Impact Assessment

### Market Impact
- No impact on regular trading operations as mock trading occurs on Saturday
- No impact on actual market prices or positions
- Testing exercise for disaster recovery preparedness

### Operational Impact
- Trading members' technical teams need to temporarily reconfigure systems
- Mock session helps validate DR site connectivity and functionality
- Ensures business continuity preparedness for Currency Derivatives segment
- Minimal operational disruption as conducted outside regular trading hours

### Participant Impact
- Limited to trading members who choose to participate in mock trading
- Voluntary participation for testing purposes
- No mandatory compliance requirements beyond those who opt to participate