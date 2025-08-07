---
category: market-operations
circular_id: 60945deea6cea933
date: '2025-08-07'
description: BSE announces mock trading session from DR site for equity derivatives
  segment with connection parameters and system access details.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={BF16FFBB-30E6-4B67-AA18-26BFDDD27DB8}&noticeno=20250807-3&dt=08/07/2025&icount=3&totcount=77&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Routine DR testing for trading members to ensure business continuity
  preparedness
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20250807-3&attachedId=c4169db5-b18b-496b-84fd-f1b22f3687e8
processing:
  attempts: 1
  content_hash: b8fb015352ef4ac7
  processed_at: '2025-08-07T18:54:53.645692'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-08-07T07:10:55+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={BF16FFBB-30E6-4B67-AA18-26BFDDD27DB8}&noticeno=20250807-3&dt=08/07/2025&icount=3&totcount=77&flag=0
severity: medium
source: bse
stocks: []
tags:
- disaster-recovery
- mock-trading
- equity-derivatives
- bolt-plus
- trading-systems
- dr-testing
title: Mock Trading from Disaster Recovery Site - Equity Derivatives Segment - August
  09, 2025
---

## Summary

BSE has announced mock trading from its Disaster Recovery (DR) site on Saturday, August 09, 2025, for the Equity Derivatives segment. Trading members can connect using BOLT TWS or third-party applications through ETI APIs with specific DR connection parameters.

## Key Points

- Mock trading session scheduled for August 09, 2025 (Saturday)
- Covers Equity Derivatives segment only
- Two connection methods available: BOLT TWS and ETI APIs
- DR connection parameters provided for both primary and secondary sites
- Web-based systems accessible through alternate URLs during DR testing

## Connection Parameters

**BOLT TWS Users:**
- Change technical connection parameters in configuration settings window
- Access via scrip profile icon or "Shift+F12" shortcut keys

**ETI API Users:**
- Primary DR: IP 10.255.241.16, Port 15910
- Secondary DR: IP 10.255.241.17, Port 15910

## Web-Based Systems Access

- RTRMS: https://rtrms.bseindia.com
- Collateral & Early Pay In: https://classseg.bseindia.com/application/applogin/login.aspx
- EBOSS: https://ebossll.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp
- LEIPS: https://leipsmmll.bseindia.com/stocks/jsp/LEIPS/index.jsp
- Extranet: https://memberll.bseindia.com/
- Extranet Plus: Specific DR IP settings provided

## Technical Requirements

**Online Trade File (OTD):**
- Remote Server IP: 10.1.101.201
- Remote Server Port: 9001
- Special Request Port: 9000

**iBBS Connection:**
- IP: 10.1.101.203, Port: 9011
- Alternative: IP 103.47.196.143, Port: 8080

## Compliance Requirements

- Trading members must test DR connectivity using provided parameters
- Existing user IDs and passwords remain valid for web-based systems
- Members should update configuration settings as specified
- Testing ensures business continuity preparedness

## Important Dates

- **Mock Trading Date:** Saturday, August 09, 2025
- **Segment:** Equity Derivatives only

## Impact Assessment

This DR testing ensures trading members can maintain operations during actual disaster scenarios. Regular DR testing is crucial for market stability and business continuity. Members should participate to validate their backup connectivity and systems integration.