---
category: market-operations
circular_id: 8b6e52610101ec84
date: '2025-12-11'
description: BSE announces mock trading session on December 13, 2025 for Equity Derivatives
  segment with disaster recovery site connection parameters for BOLT Plus trading
  system.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={725AA372-8991-4B3A-96E3-94A0EA537CC1}&noticeno=20251211-54&dt=12/11/2025&icount=54&totcount=90&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for testing disaster recovery connectivity;
  no impact on regular trading operations or market participants beyond voluntary
  participation in testing
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251211-54&attachedId=ea804e2e-4a98-4780-ad62-90b3b9b5a30f
processing:
  attempts: 1
  content_hash: 048fbac0b6b92c46
  processed_at: '2025-12-11T18:55:14.522360'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-11T14:03:39+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={725AA372-8991-4B3A-96E3-94A0EA537CC1}&noticeno=20251211-54&dt=12/11/2025&icount=54&totcount=90&flag=0
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
title: Mock Trading on Saturday, December 13, 2025, for Equity Derivatives Segment
---

## Summary

BSE has announced a mock trading session scheduled for Saturday, December 13, 2025, for the Equity Derivatives segment. The circular provides detailed technical connection parameters for trading members to connect to the Disaster Recovery (DR) site of the BOLT Plus trading system. Trading members can connect using BOLT TWS, third-party trading applications from empanelled vendors, or in-house developed systems through ETI APIs.

## Key Points

- Mock trading session scheduled for Saturday, December 13, 2025
- Applies to Equity Derivatives segment only
- Trading members must use DR site connection parameters
- Two connection methods available: BOLT TWS and ETI APIs
- DR connection parameters provided for primary and secondary servers
- Web-based systems accessible through specific URLs for leased line and internet connections

## Technical Connection Details

### BOLT TWS Users
- Trading members need to change technical connection parameters in configuration settings window at login
- Configuration settings can be invoked using scrip profile icon or "Shift+F12" shortcut keys

### ETI API Users (3rd Party Applications)
- Primary DR: IP 10.255.241.16, Port 15910
- Secondary DR: IP 10.255.241.17, Port 15910

### Web-Based Systems Access
- RTRMS: https://rtrms.bseindia.com
- Collateral & Early Pay In: https://classseg.bseindia.com/application/applogin/login.aspx
- EBOSS: https://eboss.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp
- LEIPS: https://leipsmm.bseindia.com/stocks/jsp/LEIPS/index.jsp
- Extranet: https://member.bseindia.com/Extranet_Login.aspx
- iBBS: https://ibbs.bseindia.com/

### Leased Line Connection Parameters
- RTRMS: http://10.1.101.197/stocks/jsp/rms/index.html
- Remote Server IP: 10.1.101.201, Port: 9001
- Special Request Port: 9000

## Compliance Requirements

- Trading members participating in the mock session must configure their systems with the provided DR connection parameters
- Members using BOLT TWS should update configuration settings before login
- Members using third-party or in-house applications must update IP addresses and ports in their trading applications
- Existing user IDs and passwords can be used for web-based system access

## Important Dates

- **Mock Trading Date**: Saturday, December 13, 2025
- No specific timings mentioned in the circular

## Impact Assessment

### Market Impact
- **Minimal**: Mock trading session does not affect regular market operations
- Scheduled on Saturday (non-trading day) to avoid disruption

### Operational Impact
- **Low to Medium**: Trading members choosing to participate need to reconfigure systems with DR parameters
- Provides opportunity to test disaster recovery connectivity and failover procedures
- Helps ensure business continuity preparedness

### Trading Member Action Required
- Optional participation in mock session
- Technical staff should be available to configure and test DR connectivity
- IT teams should verify connectivity parameters and test systems before the mock session