---
category: market-operations
circular_id: bd8079e1980fcecf
date: '2026-01-16'
description: BSE announces mock trading session for commodity derivatives segment
  on Saturday, January 17, 2026, with DR connection parameters for BOLT Plus trading
  system.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={ABC1BFBA-36EC-47C4-8BD4-8F9A849E6A88}&noticeno=20260116-19&dt=01/16/2026&icount=19&totcount=42&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for testing DR systems with no impact
  on live trading operations
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260116-19&attachedId=adf32dbd-6aa5-4373-b215-fcd706a96bff
processing:
  attempts: 1
  content_hash: 437a6492aa3ca9dd
  processed_at: '2026-01-16T13:00:31.648759'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-16T09:58:08+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={ABC1BFBA-36EC-47C4-8BD4-8F9A849E6A88}&noticeno=20260116-19&dt=01/16/2026&icount=19&totcount=42&flag=0
severity: low
source: bse
stocks: []
tags:
- mock-trading
- commodity-derivatives
- disaster-recovery
- bolt-plus
- trading-system
- technical-parameters
title: Mock Trading on Saturday, January 17, 2026 for Commodity Derivatives Segment
---

## Summary

BSE has scheduled a mock trading session for the Commodity Derivatives segment on Saturday, January 17, 2026. The circular provides disaster recovery (DR) connection parameters for trading members using BOLT Plus trading system, including configurations for BOLT TWS users and third-party trading applications through ETI APIs.

## Key Points

- Mock trading session scheduled for Saturday, January 17, 2026
- Applicable to Commodity Derivatives segment only
- DR site connection parameters provided for BOLT Plus trading system
- Two connection methods available: BOLT TWS and third-party applications via ETI APIs
- DR connection parameters for web-based systems (RTRMS, CLASS, Extranet, etc.) included

## Technical Connection Parameters

### BOLT TWS Users
- Members must change technical connection parameters in configuration settings window at login
- Configuration accessible via scrip profile icon or "Shift+F12" shortcut keys

### ETI API Users (Third-party applications)
- Primary DR IP: 10.255.241.26, Port: 14910
- Secondary DR IP: 10.255.241.27, Port: 14910

### Web-based Systems DR Parameters
- RTRMS: http://10.1.101.197/stocks/jsp/rms/index.html (Leased Line)
- CLASS Collateral: https://classseg.bseindia.com/application/applogin/login.aspx
- EBOSS: https://ebossll.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp
- Extranet: https://memberll.bseindia.com/
- Online Trade File DR: IP 10.1.101.203, Port 9011

## Compliance Requirements

- Trading members using BOLT TWS must update configuration settings before connecting to DR site
- Members using third-party trading applications must modify connection parameters to DR IP addresses and ports
- Existing user IDs and passwords can be used for web-based systems
- Members using Online Trade File application must update setting.ini file with DR server IP and port

## Important Dates

- **Mock Trading Date**: Saturday, January 17, 2026

## Impact Assessment

This is a routine mock trading exercise with minimal operational impact. The session is designed to test disaster recovery systems and ensure business continuity preparedness. No impact on regular trading operations as the session is scheduled on a Saturday. Trading members need to be aware of the DR connection parameters for testing purposes only.