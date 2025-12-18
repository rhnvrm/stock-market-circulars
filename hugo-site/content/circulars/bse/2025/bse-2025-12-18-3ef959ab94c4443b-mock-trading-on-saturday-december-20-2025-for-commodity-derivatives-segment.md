---
category: market-operations
circular_id: 3ef959ab94c4443b
date: '2025-12-18'
description: BSE announces mock trading session for commodity derivatives segment
  on December 20, 2025, with disaster recovery (DR) site connection parameters for
  BOLT Plus trading system.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={9B9C2103-D67E-4D00-957B-1EAA26FB9CDC}&noticeno=20251218-54&dt=12/18/2025&icount=54&totcount=58&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading exercise for disaster recovery testing with no
  impact on actual trading or market participants
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251218-54&attachedId=811ffd6a-7121-4fd5-9e35-311bcf826580
processing:
  attempts: 1
  content_hash: 5938d47a01e25712
  processed_at: '2025-12-18T18:39:41.003978'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-18T14:28:15+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={9B9C2103-D67E-4D00-957B-1EAA26FB9CDC}&noticeno=20251218-54&dt=12/18/2025&icount=54&totcount=58&flag=0
severity: low
source: bse
stocks: []
tags:
- mock-trading
- commodity-derivatives
- disaster-recovery
- bolt-plus
- trading-system
- business-continuity
title: Mock Trading on Saturday, December 20, 2025 for Commodity Derivatives Segment
---

## Summary

BSE has scheduled a mock trading session for the Commodity Derivatives segment on Saturday, December 20, 2025. The circular provides technical connection parameters for trading members to connect to the Disaster Recovery (DR) site of the BOLT Plus trading system during the mock trading exercise.

## Key Points

- Mock trading session scheduled for Saturday, December 20, 2025
- Applies to Commodity Derivatives segment only
- Trading members must use DR site connection parameters
- Two connection methods available: BOLT TWS and third-party trading applications via ETI APIs
- Configuration changes required for both connection methods
- DR connectivity details provided for web-based systems (RTRMS, CLASS, Extranet, etc.)

## Technical Connection Parameters

### BOLT TWS Users
- Must change technical connection parameters in configuration settings window at login
- Configuration settings accessible via scrip profile icon or "Shift+F12" shortcut keys

### Third-Party Trading Applications (ETI APIs)
- Primary DR: IP 10.255.241.26, Port 14910
- Secondary DR: IP 10.255.241.27, Port 14910

### Web-Based Systems DR Access
- RTRMS: https://rtrms.bseindia.com
- CLASS Collateral: https://classseg.bseindia.com/application/applogin/login.aspx
- EBOSS: https://eboss.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp
- Extranet: https://member.bseindia.com/Extranet_Login.aspx
- Other systems accessible through specified leased line and internet URLs

## Compliance Requirements

- Trading members must configure their systems to connect to DR site parameters
- Existing user IDs and passwords remain valid for web-based systems
- Members using third-party applications must update IP and port settings
- Online Trade File application users must update setting.ini file with DR connection parameters

## Important Dates

- Mock Trading Date: Saturday, December 20, 2025

## Impact Assessment

This is a routine business continuity exercise with minimal operational impact. No actual trading will occur, and the exercise is designed to test disaster recovery infrastructure readiness. Trading members need to temporarily reconfigure their systems to participate in the mock session. Regular trading operations are unaffected.