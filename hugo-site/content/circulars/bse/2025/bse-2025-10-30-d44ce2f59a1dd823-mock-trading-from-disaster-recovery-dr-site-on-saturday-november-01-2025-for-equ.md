---
category: market-operations
circular_id: d44ce2f59a1dd823
date: '2025-10-30'
description: BSE announces mock trading session from Disaster Recovery site on November
  01, 2025 for Equity segment to test DR infrastructure and connectivity.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={B77F02B1-F32A-4A81-A7B1-5FAE346F9A0F}&noticeno=20251030-51&dt=10/30/2025&icount=51&totcount=57&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Regular DR mock trading exercise affecting all trading members but
  with medium impact as it's a scheduled test session on Saturday with no real trading
  impact
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251030-51&attachedId=aa0fb875-45e7-4690-9ef6-0ec5777d1afb
processing:
  attempts: 1
  content_hash: fd6df71207b92a75
  processed_at: '2025-10-30T15:34:59.261503'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-30T14:03:52+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={B77F02B1-F32A-4A81-A7B1-5FAE346F9A0F}&noticeno=20251030-51&dt=10/30/2025&icount=51&totcount=57&flag=0
severity: medium
source: bse
stocks: []
tags:
- mock-trading
- disaster-recovery
- equity-segment
- trading-systems
- bolt-plus
- connectivity
- business-continuity
title: Mock Trading from Disaster Recovery (DR) Site on Saturday, November 01, 2025
  for Equity Segment
---

## Summary

BSE will conduct a mock trading session from its Disaster Recovery (DR) site on Saturday, November 01, 2025 for the Equity segment. Trading members will need to connect to the DR infrastructure using modified technical connection parameters for BOLT Plus trading system, either through BOLT TWS or third-party trading applications. The exercise tests business continuity infrastructure and ensures member readiness for disaster scenarios.

## Key Points

- Mock trading session scheduled for Saturday, November 01, 2025 from DR site
- Applies to Equity segment only
- Trading members must use DR-specific connection parameters
- Two connection methods available: BOLT TWS and ETI APIs (third-party/in-house systems)
- DR primary IP: 10.255.241.10, Port: 18909
- DR secondary IP: 10.255.241.11, Port: 18909
- Web-based systems (RTRMS, CLASS, Extranet, EBOSS, LEIPS) accessible via alternate URLs
- Configuration changes required in BOLT TWS using Shift+F12 or scrip profile icon

## Technical Connection Parameters

### BOLT TWS Users
- Change connection parameters in configuration settings window at login
- Access via scrip profile icon or Shift+F12 shortcut keys

### ETI API Users (Third-party/In-house Systems)
- Primary DR: IP 10.255.241.10, Port 18909
- Secondary DR: IP 10.255.241.11, Port 18909

### Web-Based Systems DR Access
- RTRMS: http://10.1.101.197/stocks/jsp/rms/index.html (Leased Line)
- Collateral: http://10.1.101.100/ (Leased Line)
- EBOSS: https://ebossll.bseindia.com (Leased Line)
- LEIPS: https://leipsmmll.bseindia.com (Leased Line)
- Extranet: https://memberll.bseindia.com/ (Leased Line)
- CLASS: https://classseg.bseindia.com (Internet)

### Online Trade File (OTD) Settings
- Remote Server IP: 10.1.101.201
- Remote Server Port: 9001
- Special Request Port: 9000
- Connection IP: 10.1.101.203, Port: 9011

## Compliance Requirements

- All trading members must participate in the DR mock trading session
- Members must ensure their systems can connect using DR parameters
- Technical teams should update configuration settings in trading applications
- Test connectivity for both BOLT TWS and any third-party trading systems used
- Verify access to all web-based systems through DR URLs
- Update setting.ini files for Online Trade File application with DR parameters

## Important Dates

- **Mock Trading Date**: Saturday, November 01, 2025
- **Circular Issue Date**: October 30, 2025

## Impact Assessment

### Operational Impact
- Medium impact on trading members requiring pre-session technical preparation
- No impact on live trading as session scheduled on Saturday (non-trading day)
- Ensures business continuity readiness across all equity trading members
- Tests failover capabilities and alternate connectivity infrastructure

### Member Preparation Required
- Technical staff must be available on Saturday for mock session
- Configuration changes needed in trading systems
- Testing of backup connectivity parameters
- Validation of web-based system access through DR infrastructure

### Business Continuity Benefits
- Validates DR infrastructure functionality
- Ensures member preparedness for actual disaster scenarios
- Tests end-to-end connectivity and trading capabilities from backup site
- Identifies potential issues in controlled environment before actual emergency