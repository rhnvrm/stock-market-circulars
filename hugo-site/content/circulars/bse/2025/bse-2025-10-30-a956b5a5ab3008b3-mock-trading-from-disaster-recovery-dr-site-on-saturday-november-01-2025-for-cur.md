---
category: market-operations
circular_id: a956b5a5ab3008b3
date: '2025-10-30'
description: BSE announces mock trading session from Disaster Recovery site on November
  01, 2025 for Currency Derivatives segment to test DR connectivity and systems.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={9AE1D6EC-9E3B-4223-8DCF-373909257E22}&noticeno=20251030-54&dt=10/30/2025&icount=54&totcount=57&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Routine DR mock trading exercise for currency derivatives segment requiring
  trading members to test connectivity parameters but not affecting live trading operations
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251030-54&attachedId=d2d2da23-a33c-45ee-99fd-b9b854b3ce1d
processing:
  attempts: 1
  content_hash: 5730595a30ad870f
  processed_at: '2025-10-30T15:34:07.657385'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-30T14:03:55+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={9AE1D6EC-9E3B-4223-8DCF-373909257E22}&noticeno=20251030-54&dt=10/30/2025&icount=54&totcount=57&flag=0
severity: medium
source: bse
stocks: []
tags:
- mock-trading
- disaster-recovery
- currency-derivatives
- bolt-plus
- eti-api
- system-testing
- dr-site
title: Mock Trading from Disaster Recovery (DR) Site on Saturday, November 01, 2025
  for Currency Derivative Segment
---

## Summary

BSE has scheduled a mock trading session from its Disaster Recovery (DR) site on Saturday, November 01, 2025, for the Currency Derivatives segment. Trading members are required to connect to the DR site using BOLT TWS or third-party trading applications through ETI APIs with specified DR connection parameters. This exercise ensures business continuity preparedness and validates DR infrastructure.

## Key Points

- Mock trading session scheduled for Currency Derivatives segment on November 01, 2025
- Trading members can connect via BOLT TWS or third-party applications using ETI APIs
- Specific DR connection parameters provided for Primary and Secondary DR sites
- BOLT TWS users must modify technical connection parameters in configuration settings (Shift+F12)
- ETI API users must update IP and port settings in their trading applications
- Web-based systems (RTRMS, CLASS Collateral, Extranet, etc.) accessible through DR weblinks

## Technical Connection Parameters

### BOLT TWS Configuration
- Access configuration settings using scrip profile icon or Shift+F12 shortcut
- Modify technical connection parameters in configuration settings window at login

### ETI API Connection Parameters
- **Primary DR**: IP: 10.255.241.26; Port: 13910
- **Secondary DR**: IP: 10.255.241.27; Port: 13910

### Web-Based Systems DR Access
- RTRMS: Leased Line - http://10.1.101.197/stocks/jsp/rms/index.html
- CLASS Collateral: https://classseg.bseindia.com/application/applogin/login.aspx
- EBOSS: https://eboss.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp
- Extranet: https://member.bseindia.com/Extranet_Login.aspx
- All systems accessible with existing user ID and password

## Compliance Requirements

- Trading members must ensure their systems are configured with DR connection parameters before the mock session
- Members using BOLT TWS must update configuration settings at login time
- Members using third-party trading applications must modify ETI API connection parameters
- Members using Online Trade File application must update remote server IP and port in setting.ini file
- Testing of all connectivity options (BOLT TWS, ETI APIs, web-based systems) during mock session

## Important Dates

- **Mock Trading Date**: Saturday, November 01, 2025
- **Segment**: Currency Derivatives (CDX)

## Impact Assessment

**Operational Impact**: Medium - Trading members need to reconfigure systems temporarily for DR testing. This is a planned exercise with no impact on regular trading operations as it occurs on Saturday.

**Market Impact**: Low - Mock session does not affect live markets or actual trading positions.

**Technical Impact**: Medium - Requires IT teams to update connection parameters and validate DR connectivity across multiple systems including trading terminals, APIs, and web applications.

**Business Continuity**: High importance for ensuring preparedness in case of primary site failure, validating that all trading members can seamlessly switch to DR infrastructure.