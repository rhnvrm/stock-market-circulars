---
category: trading
circular_id: 5fa97368ba35aebd
date: '2025-08-07'
description: BSE announces mock trading session from DR site on August 9, 2025 for
  equity segment with specific connection parameters for trading members.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={8C171ED7-E3EA-4F76-BB03-5360D0A1F41D}&noticeno=20250807-2&dt=08/07/2025&icount=2&totcount=37&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Mock trading session for DR testing - important for operational continuity
  but not market impacting
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20250807-2&attachedId=a3006d47-77bf-4799-b578-5a095593b1be
processing:
  attempts: 1
  content_hash: 8a3a253c5eba8b8c
  processed_at: '2025-08-07T12:58:03.877155'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-08-07T07:10:54+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={8C171ED7-E3EA-4F76-BB03-5360D0A1F41D}&noticeno=20250807-2&dt=08/07/2025&icount=2&totcount=37&flag=0
severity: medium
source: bse
stocks: []
tags:
- connectivity
- disaster-recovery
- equity
- market-infrastructure
- mock-trading
- trading-platform
title: Mock Trading from Disaster Recovery Site on Saturday, August 09, 2025 for Equity
  Segment
---

## Summary

BSE will conduct mock trading from its Disaster Recovery (DR) site on Saturday, August 9, 2025 for the equity segment. Trading members need to update their connection parameters to participate in this DR testing exercise using either BOLT TWS or third-party trading applications.

## Key Points

- Mock trading session scheduled for Saturday, August 9, 2025
- Covers equity segment operations from DR site
- Two connection methods available: BOLT TWS and third-party applications via ETI APIs
- Specific IP addresses and ports provided for DR connectivity
- Web-based systems accessible through dedicated DR URLs

## Connection Parameters

### BOLT TWS Users
- Change technical connection parameters in configuration settings
- Access via scrip profile icon or "Shift+F12" shortcut keys

### Third-Party Applications (ETI APIs)
- Primary DR: IP 10.255.241.10, Port 18909
- Secondary DR: IP 10.255.241.11, Port 18909

### Web-Based Systems DR URLs
- RTRMS: https://rtrms.bseindia.com
- CLASS Collateral: https://classseg.bseindia.com/application/applogin/login.aspx
- EBOSS: https://eboss.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp
- LEIPS: https://leipsmm.bseindia.com/stocks/jsp/LEIPS/index.jsp
- Extranet: https://member.bseindia.com/Extranet_Login.aspx
- iBBS: https://ibbs.bseindia.com/

## Important Dates

- **Mock Trading Date**: Saturday, August 9, 2025
- **Segment**: Equity

## Impact Assessment

This is a routine DR testing exercise to ensure business continuity capabilities. Trading members must update their system configurations to participate. No impact on regular trading operations as this occurs on a non-trading day.