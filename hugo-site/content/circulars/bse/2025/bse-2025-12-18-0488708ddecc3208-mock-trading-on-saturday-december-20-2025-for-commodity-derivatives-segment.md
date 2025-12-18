---
category: market-operations
circular_id: 0488708ddecc3208
date: '2025-12-18'
description: BSE announces mock trading session for Commodity Derivatives segment
  on December 20, 2025, with disaster recovery site connection parameters for BOLT
  Plus trading system.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={9B9C2103-D67E-4D00-957B-1EAA26FB9CDC}&noticeno=20251218-54&dt=12/18/2025&icount=54&totcount=56&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for testing disaster recovery connectivity;
  no operational or regulatory impact on regular trading
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251218-54&attachedId=811ffd6a-7121-4fd5-9e35-311bcf826580
processing:
  attempts: 1
  content_hash: f88ae0e36228aa2d
  processed_at: '2025-12-18T15:36:58.702910'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-18T14:28:15+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={9B9C2103-D67E-4D00-957B-1EAA26FB9CDC}&noticeno=20251218-54&dt=12/18/2025&icount=54&totcount=56&flag=0
severity: low
source: bse
stocks: []
tags:
- mock-trading
- commodity-derivatives
- disaster-recovery
- bolt-plus
- trading-system
- eti-api
- connectivity
title: Mock Trading on Saturday, December 20, 2025 for Commodity Derivatives Segment
---

## Summary

BSE has scheduled a mock trading session for the Commodity Derivatives segment on Saturday, December 20, 2025. The circular provides technical connection parameters for trading members to connect to the Disaster Recovery (DR) site of the BOLT Plus trading system using either BOLT TWS or third-party trading applications through ETI APIs.

## Key Points

- Mock trading session scheduled for Commodity Derivatives segment on December 20, 2025
- Trading members can connect using BOLT TWS or third-party applications via ETI APIs
- DR connection parameters provided for primary and secondary sites
- Configuration changes required in trading system settings
- Access details provided for web-based systems (RTRMS, CLASS, Extranet, etc.)

## Technical Connection Parameters

### BOLT TWS Users
- Members must change technical connection parameters in configuration settings window at login
- Configuration settings accessible via scrip profile icon or "Shift+F12" shortcut keys

### ETI API Users (3rd Party Applications)
- **Primary DR**: IP: 10.255.241.26; Port: 14910
- **Secondary DR**: IP: 10.255.241.27; Port: 14910

### Web-Based Systems Access
- **RTRMS**: https://rtrms.bseindia.com
- **Collateral & Early Pay In**: https://classseg.bseindia.com/application/applogin/login.aspx
- **EBOSS**: https://eboss.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp
- **LEIPS**: https://leipsmm.bseindia.com/stocks/jsp/LEIPS/index.jsp
- **Extranet**: https://member.bseindia.com/Extranet_Login.aspx
- **iBBS**: https://ibbs.bseindia.com/

## Compliance Requirements

- Trading members must update connection parameters in their trading applications before the mock session
- Members using BOLT TWS must modify configuration settings at login
- Members using third-party applications must update ETI API connection parameters to DR site IPs and ports
- Existing user IDs and passwords to be used for web-based systems

## Important Dates

- **Mock Trading Date**: Saturday, December 20, 2025
- **Segment**: Commodity Derivatives

## Impact Assessment

This is a routine disaster recovery testing exercise with minimal operational impact. Trading members need to temporarily update their system configurations to connect to the DR site during the mock session. Regular trading operations are not affected as the mock session is scheduled on a Saturday. The exercise ensures business continuity preparedness and validates DR infrastructure for the Commodity Derivatives segment.