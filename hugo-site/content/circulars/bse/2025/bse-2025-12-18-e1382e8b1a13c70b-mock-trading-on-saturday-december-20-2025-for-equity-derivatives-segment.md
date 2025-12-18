---
category: market-operations
circular_id: e1382e8b1a13c70b
date: '2025-12-18'
description: BSE announces mock trading session for Equity Derivatives segment on
  Saturday, December 20, 2025, with DR site connection parameters for trading members.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={E02DA54A-8420-4FF2-9FD4-C36EE7A5834A}&noticeno=20251218-52&dt=12/18/2025&icount=52&totcount=56&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for testing disaster recovery systems;
  no impact on regular trading or specific securities.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251218-52&attachedId=fe41a105-b9cf-4a8a-8c93-5a67ec626a81
processing:
  attempts: 1
  content_hash: 9820e91fa8cf37cb
  processed_at: '2025-12-18T15:37:26.629531'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-18T14:28:11+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={E02DA54A-8420-4FF2-9FD4-C36EE7A5834A}&noticeno=20251218-52&dt=12/18/2025&icount=52&totcount=56&flag=0
severity: low
source: bse
stocks: []
tags:
- mock-trading
- equity-derivatives
- dr-site
- testing
- bolt-plus
- technical-connectivity
title: Mock Trading on Saturday, December 20, 2025 for Equity Derivatives Segment
---

## Summary

BSE has announced a mock trading session for the Equity Derivatives segment scheduled for Saturday, December 20, 2025. The circular provides detailed technical connection parameters for trading members to connect to the DR (Disaster Recovery) site of the BOLT Plus trading system. Trading members can connect using BOLT TWS, third-party trading applications, or in-house developed systems through ETI APIs.

## Key Points

- Mock trading session scheduled for Saturday, December 20, 2025
- Applies to Equity Derivatives segment only
- Trading members must use DR site connection parameters
- Multiple connectivity options available: BOLT TWS, third-party applications via ETI APIs, and web-based systems
- DR site technical parameters provided for both BOLT TWS users and ETI API users

## Technical Connection Details

### BOLT TWS Users
- Members must change technical connection parameters in configuration settings window at login
- Configuration settings can be accessed via scrip profile icon or "Shift+F12" shortcut keys

### ETI API Users (Third-party/In-house Systems)
- Primary DR IP: 10.255.241.16, Port: 15910
- Secondary DR IP: 10.255.241.17, Port: 15910

### Web-based Systems Access
- RTRMS: https://rtrms.bseindia.com
- Collateral & Early Pay In: https://classseg.bseindia.com/application/applogin/login.aspx
- EBOSS: https://eboss.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp
- LEIPS: https://leipsmm.bseindia.com/stocks/jsp/LEIPS/index.jsp
- Extranet: https://member.bseindia.com/Extranet_Login.aspx
- iBBS: https://ibbs.bseindia.com/

### Leased Line Connection Parameters
- RTRMS: http://10.1.101.197/stocks/jsp/rms/index.html or http://10.1.101.100/
- Extranet DR IP: 10.1.101.201, Port: 9001
- Special Request Port: 9000
- Online Trade File: IP 10.1.101.203, Port 9011

## Compliance Requirements

- Trading members participating in mock trading must configure their systems with the specified DR site parameters
- Members using BOLT TWS must update configuration settings before login
- Members using third-party or in-house trading applications must update ETI API connection parameters
- Existing user IDs and passwords can be used for web-based systems

## Important Dates

- **Mock Trading Date**: Saturday, December 20, 2025

## Impact Assessment

### Market Impact
- No impact on regular trading operations as this is a weekend testing session
- Mock trading is for testing and validation purposes only

### Operational Impact
- Trading members need to configure systems with DR site parameters for the mock session
- Testing helps ensure business continuity and disaster recovery preparedness
- Provides opportunity for members to validate their connectivity to backup systems
- No disruption to normal weekday trading activities