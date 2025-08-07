---
category: market-operations
circular_id: e4bb5a3e596fa160
date: '2025-08-07'
description: BSE announces mock trading session from DR site for commodity derivatives
  segment with connection parameters and system access details.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={429B2B66-79AC-457E-89F1-738CAF24F6C9}&noticeno=20250807-6&dt=08/07/2025&icount=6&totcount=37&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Routine DR testing for commodity derivatives segment requiring technical
  configuration changes
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20250807-6&attachedId=79fd323a-a3eb-4967-b2cf-9f67800ce5f5
processing:
  attempts: 1
  content_hash: e9cdd02fa67c33ef
  processed_at: '2025-08-07T12:56:13.866700'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-08-07T07:10:58+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={429B2B66-79AC-457E-89F1-738CAF24F6C9}&noticeno=20250807-6&dt=08/07/2025&icount=6&totcount=37&flag=0
severity: medium
source: bse
stocks: []
tags:
- mock-trading
- disaster-recovery
- commodity-derivatives
- bolt-plus
- trading-system
- dr-testing
title: Mock Trading from Disaster Recovery Site on Saturday, August 09, 2025 for Commodity
  Derivatives Segment
---

## Summary

BSE has scheduled mock trading from its Disaster Recovery (DR) site on Saturday, August 09, 2025, specifically for the Commodity Derivatives segment. Trading members need to update their technical connection parameters to connect to the DR site using either BOLT TWS or third-party trading applications through ETI APIs.

## Key Points

- Mock trading session scheduled for Saturday, August 09, 2025
- Applies to Commodity Derivatives segment only
- Members can connect via BOLT TWS or third-party applications through ETI APIs
- Technical connection parameters must be changed for DR site access
- Web-based systems accessible through provided DR URLs

## Technical Connection Parameters

**For BOLT TWS Users:**
- Change technical connection parameters in configuration settings window
- Access via scrip profile icon or "Shift+F12" shortcut keys

**For ETI API Users:**
- Primary DR: IP 10.255.241.26, Port 14910
- Secondary DR: IP 10.255.241.27, Port 14910

## Web-Based System Access

**Available Systems with DR URLs:**
- RTRMS: https://rtrms.bseindia.com
- Collateral & Early Pay In: https://classseg.bseindia.com/application/applogin/login.aspx
- EBOSS: https://eboss.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp
- LEIPS: https://leipsmm.bseindia.com/stocks/jsp/LEIPS/index.jsp
- Extranet: https://member.bseindia.com/Extranet_Login.aspx
- iBBS: https://ibbs.bseindia.com/

## Important Dates

- **Mock Trading Date:** Saturday, August 09, 2025
- **Segment:** Commodity Derivatives only

## Impact Assessment

This is a routine disaster recovery testing exercise that requires trading members to temporarily reconfigure their systems. The mock trading session helps ensure business continuity preparedness for the commodity derivatives segment. Members must update technical parameters to participate in the DR testing.