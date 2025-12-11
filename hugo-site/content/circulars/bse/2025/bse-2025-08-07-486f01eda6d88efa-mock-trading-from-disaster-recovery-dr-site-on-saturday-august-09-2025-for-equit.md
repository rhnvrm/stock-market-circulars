---
category: market-operations
circular_id: 486f01eda6d88efa
date: '2025-08-07'
description: BSE announces mock trading session from disaster recovery site for equity
  segment with connection parameters and system access details.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={8C171ED7-E3EA-4F76-BB03-5360D0A1F41D}&noticeno=20250807-2&dt=08/07/2025&icount=2&totcount=77&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Mock trading session for DR testing is important for business continuity
  but has no direct market impact
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20250807-2&attachedId=a3006d47-77bf-4799-b578-5a095593b1be
processing:
  attempts: 1
  content_hash: f4aa4a9045c170c5
  processed_at: '2025-08-07T18:55:21.891504'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-08-07T07:10:54+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={8C171ED7-E3EA-4F76-BB03-5360D0A1F41D}&noticeno=20250807-2&dt=08/07/2025&icount=2&totcount=77&flag=0
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

BSE will conduct mock trading from its Disaster Recovery (DR) site on Saturday, August 09, 2025 for the equity segment. Trading members can connect using BOLT TWS or third-party applications through ETI APIs with specific DR connection parameters.

## Key Points

- Mock trading session scheduled for Saturday, August 09, 2025
- Testing covers equity segment only
- Two connection methods available: BOLT TWS and ETI APIs
- Specific DR IP addresses and ports provided for connectivity
- Web-based systems accessible through alternate URLs

## Connection Parameters

**BOLT TWS Users:**
- Change technical connection parameters in configuration settings
- Access settings via scrip profile icon or Shift+F12 shortcut

**ETI API Users:**
- Primary DR: IP 10.255.241.10, Port 18909
- Secondary DR: IP 10.255.241.11, Port 18909

**Web-based Systems DR URLs:**
- RTRMS: http://10.1.101.197/stocks/jsp/rms/index.html
- Collateral & Early Pay In: http://10.1.101.100/
- EBOSS: https://ebossll.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp
- LEIPS: https://leipsmmll.bseindia.com/stocks/jsp/LEIPS/index.jsp
- Extranet: https://memberll.bseindia.com/

## Technical Requirements

- Trading members must update connection parameters before the mock session
- Existing user IDs and passwords remain valid for DR site access
- Online Trade File application requires setting.ini file modifications
- DR server settings: IP 10.1.101.201, Port 9001, Special Request Port 9000

## Important Dates

- **Mock Trading Date:** Saturday, August 09, 2025
- **Preparation Required:** Prior to session start

## Impact Assessment

This mock trading session is part of BSE's business continuity planning to ensure seamless operations during system failures. Trading members should participate to validate their DR connectivity and procedures. No impact on regular trading operations as this occurs on a non-trading day.