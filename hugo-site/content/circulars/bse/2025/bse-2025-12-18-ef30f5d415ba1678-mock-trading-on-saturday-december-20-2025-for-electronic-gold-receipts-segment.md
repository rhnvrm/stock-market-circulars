---
category: market-operations
circular_id: ef30f5d415ba1678
date: '2025-12-18'
description: BSE announces mock trading session for Electronic Gold Receipts segment
  on December 20, 2025 with DR connectivity parameters for trading members.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={41BD1324-B0F7-4AA4-A1F9-5A5A97E94C82}&noticeno=20251218-55&dt=12/18/2025&icount=55&totcount=56&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for disaster recovery testing with no
  impact on regular trading operations
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251218-55&attachedId=ab87aee9-6373-485f-8993-5a36c89cd4e8
processing:
  attempts: 1
  content_hash: 62c3c3d00ecaf893
  processed_at: '2025-12-18T15:36:09.980528'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-18T14:28:16+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={41BD1324-B0F7-4AA4-A1F9-5A5A97E94C82}&noticeno=20251218-55&dt=12/18/2025&icount=55&totcount=56&flag=0
severity: low
source: bse
stocks: []
tags:
- mock-trading
- electronic-gold-receipts
- egr
- disaster-recovery
- connectivity
- bolt-plus
- trading-system
title: Mock Trading on Saturday, December 20, 2025 for Electronic Gold Receipts Segment
---

## Summary

BSE has announced a mock trading session for the Electronic Gold Receipts (EGR) segment scheduled for Saturday, December 20, 2025. This is a disaster recovery (DR) drill to test the BOLT Plus trading system's backup infrastructure. Trading members can participate using BOLT TWS or third-party trading applications through ETI APIs with specified DR connection parameters.

## Key Points

- Mock trading session for Electronic Gold Receipts segment on December 20, 2025 (Saturday)
- Disaster recovery connection testing for BOLT Plus trading system
- Trading members must use DR site connection parameters
- Two connectivity options: BOLT TWS or third-party applications via ETI APIs
- DR connection parameters provided for both primary and secondary servers
- Web-based systems (RTRMS, CLASS, EBOSS, etc.) accessible through DR URLs

## Technical Connection Parameters

### BOLT TWS Users
- Change technical connection parameters in configuration settings window at login
- Configuration settings accessible via scrip profile icon or "Shift+F12" shortcut keys

### ETI API Users (Third-party applications)
- Primary DR: IP 10.255.241.26, Port 14910
- Secondary DR: IP 10.255.241.27, Port 14910

### Web-based Systems DR URLs
- RTRMS: http://10.1.101.197/stocks/jsp/rms/index.html (Leased Line)
- CLASS Collateral: http://10.1.101.100/ (Leased Line)
- EBOSS: https://ebossll.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp (Leased Line)
- LEIPS: https://leipsmmll.bseindia.com/stocks/jsp/LEIPS/index.jsp (Leased Line)
- Extranet: https://memberll.bseindia.com/ (Leased Line)
- Extranet Plus: IP 10.1.101.196, Port settings in setting.ini file

## Compliance Requirements

- Trading members must configure their systems with DR connection parameters
- Members using BOLT TWS must update configuration settings before login
- Members using third-party applications must update ETI API connection parameters
- Existing user IDs and passwords can be used for web-based systems
- Online Trade File application users must update remote server IP and port in setting.ini file

## Important Dates

- Mock Trading Date: Saturday, December 20, 2025
- Circular Issue Date: December 18, 2025

## Impact Assessment

This is a routine disaster recovery drill with minimal operational impact. Regular trading is not affected as the mock session is scheduled on a Saturday. Trading members need to temporarily reconfigure their systems to connect to DR infrastructure for testing purposes. The drill ensures business continuity preparedness and validates backup system functionality for the Electronic Gold Receipts segment.