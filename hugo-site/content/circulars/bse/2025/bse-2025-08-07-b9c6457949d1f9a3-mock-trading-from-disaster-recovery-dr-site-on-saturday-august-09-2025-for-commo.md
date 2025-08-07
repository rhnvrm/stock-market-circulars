---
category: trading
circular_id: b9c6457949d1f9a3
date: '2025-08-07'
description: BSE announces mock trading session from DR site for commodity derivatives
  segment with technical connection parameters for trading members.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={429B2B66-79AC-457E-89F1-738CAF24F6C9}&noticeno=20250807-6&dt=08/07/2025&icount=6&totcount=10&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Scheduled mock trading session for DR testing - important for operational
  continuity but not market-moving
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20250807-6&attachedId=79fd323a-a3eb-4967-b2cf-9f67800ce5f5
processing:
  attempts: 1
  content_hash: 7b7c515c9fd55acf
  processed_at: '2025-08-07T09:28:31.132327'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-08-07T07:10:58+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={429B2B66-79AC-457E-89F1-738CAF24F6C9}&noticeno=20250807-6&dt=08/07/2025&icount=6&totcount=10&flag=0
severity: medium
source: bse
stocks: []
tags:
- mock-trading
- disaster-recovery
- commodity-derivatives
- technical-parameters
- bolt-plus
- eti-api
- trading-systems
title: Mock Trading from Disaster Recovery (DR) site on Saturday, August 09, 2025
  for Commodity Derivatives segment
---

## Summary

BSE announces mock trading from Disaster Recovery (DR) site scheduled for Saturday, August 09, 2025 for the Commodity Derivatives segment. Trading members must use specific technical connection parameters to connect to the DR site through BOLT TWS or third-party trading applications.

## Key Points

- Mock trading session from DR site for Commodity Derivatives segment
- Two connection methods available: BOLT TWS and third-party applications via ETI APIs
- Specific IP addresses and ports provided for DR connectivity
- Web-based systems accessible through provided URLs with existing credentials

## Technical Connection Parameters

### BOLT TWS Users
- Change technical connection parameters in configuration settings window
- Access via scrip profile icon or "Shift+F12" shortcut keys

### ETI API Users
- Primary DR: IP 10.255.241.26, Port 14910
- Secondary DR: IP 10.255.241.27, Port 14910

### Web-based Systems URLs
- RTRMS: https://rtrms.bseindia.com
- Collateral & Early Pay In: https://classseg.bseindia.com/application/applogin/login.aspx
- EBOSS: https://ebossll.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp
- LEIPS: https://leipsmmll.bseindia.com/stocks/jsp/LEIPS/index.jsp
- Extranet: https://memberll.bseindia.com/

## Compliance Requirements

- Trading members must configure their systems with DR connection parameters
- Existing user IDs and passwords to be used for web-based systems
- Members using online trade file application must update setting.ini file with DR IP and port settings

## Important Dates

- **Mock Trading Date**: Saturday, August 09, 2025
- **Segment**: Commodity Derivatives only

## Impact Assessment

Operational impact for trading members who need to reconfigure their trading systems for DR connectivity testing. Essential for ensuring business continuity and disaster recovery preparedness in commodity derivatives trading.