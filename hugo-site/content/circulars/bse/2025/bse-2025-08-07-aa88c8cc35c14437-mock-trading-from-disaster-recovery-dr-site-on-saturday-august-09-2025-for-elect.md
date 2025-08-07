---
category: market-operations
circular_id: aa88c8cc35c14437
date: '2025-08-07'
description: BSE announces mock trading session from DR site for Electronic Gold Receipts
  segment with connection parameters for BOLT Plus trading system.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={9CD090FB-7701-4A11-BD50-A57BD551720D}&noticeno=20250807-4&dt=08/07/2025&icount=4&totcount=37&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Scheduled mock trading session for DR testing - important for operational
  continuity but no immediate market impact
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20250807-4&attachedId=99e787ca-a2f2-410c-8838-fbd681e90617
processing:
  attempts: 1
  content_hash: 13ef65e777611627
  processed_at: '2025-08-07T12:56:29.911346'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-08-07T07:10:56+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={9CD090FB-7701-4A11-BD50-A57BD551720D}&noticeno=20250807-4&dt=08/07/2025&icount=4&totcount=37&flag=0
severity: medium
source: bse
stocks: []
tags:
- mock-trading
- disaster-recovery
- electronic-gold-receipts
- bolt-plus
- eti-api
- trading-system
title: Mock Trading from Disaster Recovery Site on Saturday, August 09, 2025 for Electronic
  Gold Receipts Segment
---

## Summary

BSE has announced a mock trading session from the Disaster Recovery (DR) site on Saturday, August 09, 2025, specifically for the Electronic Gold Receipts segment. The circular provides detailed technical connection parameters for trading members to connect to the DR site using BOLT Plus trading system.

## Key Points

- Mock trading session scheduled for Electronic Gold Receipts segment from DR site
- Trading members can connect via BOLT TWS or third-party applications through ETI APIs
- Configuration changes required in trading applications for DR connectivity
- Multiple web-based systems accessible through provided DR URLs
- Comprehensive connectivity manual (Version 1.13) included for reference

## Technical Connection Details

### BOLT Plus ETI API Parameters
- Primary DR IP: 10.255.241.26, Port: 14910
- Secondary DR IP: 10.255.241.27, Port: 14910

### Web-Based Systems DR Access
- RTRMS, CLASS Collateral, EBOSS, LEIPS, and other systems accessible via specific DR URLs
- Existing user credentials remain valid for DR site access

## Compliance Requirements

- Trading members must update technical connection parameters in their trading applications
- BOLT TWS users need to modify configuration settings using Shift+F12 or scrip profile icon
- Third-party application users must update ETI API connection parameters
- Online Trade File application users must modify setting.ini file with DR parameters

## Important Dates

- **Mock Trading Date**: Saturday, August 09, 2025
- **Segment**: Electronic Gold Receipts only

## Impact Assessment

**Operational Impact**: Medium - Ensures trading members can effectively connect to and operate from the disaster recovery site, maintaining market continuity in case of primary system failures. The mock session allows testing of DR procedures without affecting regular trading operations.

**Market Impact**: Low - Being a mock session on Saturday, there is no direct impact on regular market operations or pricing.