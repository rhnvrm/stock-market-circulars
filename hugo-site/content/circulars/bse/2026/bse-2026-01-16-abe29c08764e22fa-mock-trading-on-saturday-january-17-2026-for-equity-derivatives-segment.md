---
category: market-operations
circular_id: abe29c08764e22fa
date: '2026-01-16'
description: BSE announces mock trading session on Saturday, January 17, 2026, for
  the Equity Derivatives segment with DR site connectivity parameters for BOLT Plus
  trading system.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={B49E1159-88C3-4427-A2B5-40B3D86C116A}&noticeno=20260116-16&dt=01/16/2026&icount=16&totcount=64&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for disaster recovery testing with no
  impact on regular trading operations
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260116-16&attachedId=39a37400-dd23-4cbc-948a-1fcbf3e9ebc5
processing:
  attempts: 1
  content_hash: 75fcf85d23941626
  processed_at: '2026-01-16T19:00:25.931356'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-16T09:58:05+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={B49E1159-88C3-4427-A2B5-40B3D86C116A}&noticeno=20260116-16&dt=01/16/2026&icount=16&totcount=64&flag=0
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
- technical-parameters
title: Mock Trading on Saturday, January 17, 2026, for Equity Derivatives Segment
---

## Summary

BSE has announced a mock trading session scheduled for Saturday, January 17, 2026, for the Equity Derivatives segment. The circular provides detailed disaster recovery (DR) connection parameters for trading members to connect to the BOLT Plus trading system using either BOLT TWS or third-party trading applications through ETI APIs. Trading members can also access various Exchange web-based systems including RTRMS, CLASS collateral, and Extranet through specified weblinks.

## Key Points

- Mock trading session scheduled for Saturday, January 17, 2026, for Equity Derivatives segment
- Trading members can connect to DR site using BOLT TWS or third-party applications
- Primary DR connection: IP 10.255.241.16, Port 15910
- Secondary DR connection: IP 10.255.241.17, Port 15910
- Configuration changes required in BOLT TWS using Shift+F12 shortcut
- Web-based systems accessible through both leased line and internet connections
- Existing user IDs and passwords to be used for web-based systems

## Technical Connection Details

### BOLT TWS Users
- Trading members must change technical connection parameters in configuration settings window at login
- Configuration settings invoked using scrip profile icon or Shift+F12 shortcut keys

### Third-Party Trading Applications (ETI APIs)
- Primary DR: IP 10.255.241.16, Port 15910
- Secondary DR: IP 10.255.241.17, Port 15910

### Web-Based Systems Access
- RTRMS: https://rtrms.bseindia.com
- Collateral & Early Pay In: https://classseg.bseindia.com
- EBOSS: https://eboss.bseindia.com
- LEIPS: https://leipsmm.bseindia.com
- Extranet: https://member.bseindia.com
- iBBS: https://ibbs.bseindia.com

## Compliance Requirements

- Trading members must update their DR connection parameters before the mock trading session
- For BOLT TWS users: Update configuration settings at login
- For third-party application users: Update technical connection parameters in respective trading applications
- Online Trade File application users: Change remote server IP and port settings in setting.ini file

## Important Dates

- Mock Trading Session: Saturday, January 17, 2026
- Circular Date: January 16, 2026

## Impact Assessment

This is a routine disaster recovery testing exercise with minimal operational impact. The mock trading session is conducted on a non-trading day (Saturday) to test the resilience of the DR infrastructure without disrupting normal market operations. Trading members need to ensure their systems are configured correctly to participate in the mock session, which helps validate business continuity preparedness. No impact on regular trading activities or market participants who choose not to participate.