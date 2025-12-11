---
category: market-operations
circular_id: a4b834414c641393
date: '2025-08-07'
description: BSE announces mock trading session from DR site for Equity Derivatives
  segment with connection parameters for BOLT Plus system.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={BF16FFBB-30E6-4B67-AA18-26BFDDD27DB8}&noticeno=20250807-3&dt=08/07/2025&icount=3&totcount=37&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Routine DR testing exercise important for business continuity but limited
  operational impact
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20250807-3&attachedId=c4169db5-b18b-496b-84fd-f1b22f3687e8
processing:
  attempts: 1
  content_hash: f38e95f1436b8b94
  processed_at: '2025-08-07T12:57:30.580978'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-08-07T07:10:55+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={BF16FFBB-30E6-4B67-AA18-26BFDDD27DB8}&noticeno=20250807-3&dt=08/07/2025&icount=3&totcount=37&flag=0
severity: medium
source: bse
stocks: []
tags:
- connectivity
- derivatives
- disaster-recovery
- market-infrastructure
- mock-trading
- trading-platform
title: Mock Trading from Disaster Recovery Site on Saturday, August 09, 2025 for Equity
  Derivatives Segment
---

## Summary

BSE has scheduled mock trading from its Disaster Recovery (DR) site on Saturday, August 09, 2025 for the Equity Derivatives segment. Trading members can connect using BOLT TWS or third-party applications through ETI APIs with specified DR connection parameters.

## Key Points

- Mock trading session scheduled for Saturday, August 09, 2025
- Applies to Equity Derivatives segment only
- Two connection methods available: BOLT TWS and ETI APIs
- DR site connectivity parameters provided for both primary and secondary connections
- Web-based systems accessible through alternate URLs during DR testing

## Connection Parameters

**BOLT TWS Users:**
- Change technical connection parameters in configuration settings
- Access via scrip profile icon or "Shift+F12" shortcut keys

**ETI API Users:**
- Primary DR: IP 10.255.241.16, Port 15910
- Secondary DR: IP 10.255.241.17, Port 15910

**Web-based Systems DR URLs:**
- RTRMS: http://10.1.101.197/stocks/jsp/rms/index.html
- Collateral & Early Pay In: http://10.1.101.100/
- EBOSS: Various DR URLs provided
- Extranet: Alternate access points specified

## Technical Requirements

- Trading members must update connection settings in their respective applications
- Online Trade File application requires changes to setting.ini file
- Remote server IP and port modifications needed for DR connectivity
- Existing user credentials remain valid for web-based system access

## Important Dates

- **Mock Trading Date:** Saturday, August 09, 2025

## Impact Assessment

This is a routine disaster recovery testing exercise to ensure business continuity capabilities. Trading members need to prepare their systems with alternate connection parameters but normal trading operations will not be affected as this occurs on a non-trading day.