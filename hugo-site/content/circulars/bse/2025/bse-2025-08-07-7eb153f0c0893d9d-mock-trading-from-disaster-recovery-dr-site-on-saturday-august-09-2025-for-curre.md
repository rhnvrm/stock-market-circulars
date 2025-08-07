---
category: market-operations
circular_id: 7eb153f0c0893d9d
date: '2025-08-07'
description: BSE announces mock trading session from disaster recovery site for currency
  derivatives segment with connection parameters and system access details.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={55B4AF47-F4EF-46E7-8460-E609B25C82AA}&noticeno=20250807-5&dt=08/07/2025&icount=5&totcount=68&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Scheduled DR testing for currency derivatives segment affecting trading
  member connectivity
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20250807-5&attachedId=61a2b049-f2e3-4f04-96ee-f804f1db5e40
processing:
  attempts: 1
  content_hash: bbf1cbe7e9ec5bf2
  processed_at: '2025-08-07T15:46:17.889849'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-08-07T07:10:57+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={55B4AF47-F4EF-46E7-8460-E609B25C82AA}&noticeno=20250807-5&dt=08/07/2025&icount=5&totcount=68&flag=0
severity: medium
source: bse
stocks: []
tags:
- mock-trading
- disaster-recovery
- currency-derivatives
- bolt-plus
- trading-system
- connectivity
- dr-testing
title: Mock Trading from Disaster Recovery (DR) Site on Saturday, August 09, 2025
  for Currency Derivative Segment
---

## Summary

BSE will conduct mock trading from its Disaster Recovery (DR) site on Saturday, August 09, 2025 for the Currency Derivatives segment. Trading members need to use specific DR connection parameters to access BOLT Plus trading system and other web-based systems during the test.

## Key Points

- Mock trading session scheduled for Currency Derivatives segment on August 09, 2025
- Trading members can connect via BOLT TWS or 3rd party trading applications through ETI APIs
- Specific DR IP addresses and ports provided for connectivity
- Access to web-based systems like RTRMS, CLASS collateral, Extranet available through DR URLs
- Both leased line and internet connectivity options provided

## Technical Connection Parameters

**BOLT Plus DR Connection (ETI APIs):**
- Primary DR: IP 10.255.241.26, Port 13910
- Secondary DR: IP 10.255.241.27, Port 13910

**Web-based Systems DR URLs:**
- RTRMS: https://rtrms.bseindia.com
- CLASS Collateral: https://classseg.bseindia.com/application/applogin/login.aspx
- EBOSS: https://eboss.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp
- Extranet: https://member.bseindia.com/Extranet_Login.aspx

## Compliance Requirements

- Trading members must configure DR connection parameters in their trading systems
- BOLT TWS users need to change technical connection parameters in configuration settings
- 3rd party application users must update ETI API connection parameters
- Existing user IDs and passwords remain valid for web-based system access

## Important Dates

- **Mock Trading Date:** Saturday, August 09, 2025
- **Segment:** Currency Derivatives only

## Impact Assessment

This DR mock trading session ensures business continuity preparedness for the currency derivatives segment. Trading members need to test their connectivity and systems using the provided DR parameters to ensure seamless operations during actual DR scenarios.