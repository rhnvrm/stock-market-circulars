---
category: market-operations
circular_id: 0cab604a56907ac8
date: '2025-08-07'
description: BSE announces mock trading session from DR site for equity derivatives
  segment with technical connection parameters and system access details.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={BF16FFBB-30E6-4B67-AA18-26BFDDD27DB8}&noticeno=20250807-3&dt=08/07/2025&icount=3&totcount=10&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Routine DR testing with specific technical requirements for trading
  members
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20250807-3&attachedId=c4169db5-b18b-496b-84fd-f1b22f3687e8
processing:
  attempts: 1
  content_hash: 67eaa2cf8983635d
  processed_at: '2025-08-07T09:30:04.952477'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-08-07T07:10:55+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={BF16FFBB-30E6-4B67-AA18-26BFDDD27DB8}&noticeno=20250807-3&dt=08/07/2025&icount=3&totcount=10&flag=0
severity: medium
source: bse
stocks: []
tags:
- mock-trading
- disaster-recovery
- equity-derivatives
- bolt-plus
- trading-system
- dr-testing
title: Mock Trading from Disaster Recovery Site on Saturday, August 09, 2025 for Equity
  Derivatives Segment
---

## Summary

BSE has scheduled mock trading from its Disaster Recovery (DR) site on Saturday, August 09, 2025 for the Equity Derivatives segment. Trading members need to update their technical connection parameters to participate in the DR testing exercise.

## Key Points

- Mock trading session scheduled for Saturday, August 09, 2025
- Applies specifically to Equity Derivatives segment
- Trading members can connect via BOLT TWS or third-party applications through ETI APIs
- Configuration changes required for DR site connectivity
- Web-based systems accessible through provided URLs with existing credentials

## Technical Connection Parameters

### BOLT TWS Users
- Change technical connection parameters in configuration settings window
- Access via scrip profile icon or "Shift+F12" shortcut keys

### Third-party Applications (ETI APIs)
- Primary DR: IP 10.255.241.16, Port 15910
- Secondary DR: IP 10.255.241.17, Port 15910

### Web-based Systems Access
- RTRMS: https://rtrms.bseindia.com
- Collateral & Early Pay In: https://classseg.bseindia.com/application/applogin/login.aspx
- EBOSS: https://eboss.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp
- LEIPS: https://leipsmm.bseindia.com/stocks/jsp/LEIPS/index.jsp
- Extranet: https://member.bseindia.com/Extranet_Login.aspx

## Compliance Requirements

- Trading members must update connection parameters before DR testing
- Use existing user IDs and passwords for web-based systems
- Ensure proper configuration of trading applications
- Update setting.ini files for online trade file applications with DR parameters

## Important Dates

- **Mock Trading Date**: Saturday, August 09, 2025
- **Segment**: Equity Derivatives only

## Impact Assessment

Routine disaster recovery testing with minimal market impact as it occurs on non-trading day. Trading members need to allocate technical resources for parameter updates and testing participation.