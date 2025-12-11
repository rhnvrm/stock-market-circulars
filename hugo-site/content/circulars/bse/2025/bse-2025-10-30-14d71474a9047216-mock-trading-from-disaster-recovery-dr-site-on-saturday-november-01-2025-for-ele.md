---
category: market-operations
circular_id: 14d71474a9047216
date: '2025-10-30'
description: BSE announces mock trading session from Disaster Recovery site for Electronic
  Gold Receipts segment on November 01, 2025, including connection parameters for
  BOLT Plus trading system and web-based applications.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={1FA4A633-BD64-47FC-9425-1F2B27E247FC}&noticeno=20251030-53&dt=10/30/2025&icount=53&totcount=57&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for disaster recovery testing with no
  impact on live trading or market participants beyond participation in the drill
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251030-53&attachedId=5a64e126-15c3-4ebe-9ba6-7cebdfc4991b
processing:
  attempts: 1
  content_hash: 488a2201f54da6d5
  processed_at: '2025-10-30T15:33:45.825868'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-30T14:03:54+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={1FA4A633-BD64-47FC-9425-1F2B27E247FC}&noticeno=20251030-53&dt=10/30/2025&icount=53&totcount=57&flag=0
severity: medium
source: bse
stocks: []
tags:
- connectivity
- disaster-recovery
- egr
- market-infrastructure
- mock-trading
- technical-parameters
- trading-platform
title: Mock Trading from Disaster Recovery (DR) Site on Saturday, November 01, 2025
  for Electronic Gold Receipts Segment
---

## Summary

BSE has scheduled a mock trading session from its Disaster Recovery (DR) site on Saturday, November 01, 2025, for the Electronic Gold Receipts segment. Trading members can connect to the DR site using BOLT TWS, third-party trading applications, or in-house developed systems through ETI APIs. The circular provides detailed technical connection parameters for BOLT Plus trading system and web-based applications including RTRMS, CLASS collateral, Extranet, and other member platforms.

## Key Points

- Mock trading session scheduled for November 01, 2025 (Saturday)
- Testing covers Electronic Gold Receipts (EGR) segment
- Members can connect via BOLT TWS or third-party trading applications
- DR connection parameters provided for Commodity Derivatives segment BOLT Plus system
- Primary DR IP: 10.255.241.26, Port: 14910
- Secondary DR IP: 10.255.241.27, Port: 14910
- Web-based systems accessible through specific URLs for leased line and internet connections
- Configuration changes required in trading applications for DR connectivity

## Regulatory Changes

No regulatory changes. This is a routine disaster recovery testing exercise.

## Compliance Requirements

- Trading members must update technical connection parameters in BOLT TWS configuration settings or third-party trading applications
- BOLT TWS users need to access configuration settings window using scrip profile icon or "Shift+F12" shortcut keys
- Members using ETI APIs must change connection parameters to DR site IP addresses and ports
- Online Trade File application users must modify remote server IP and port settings in setting.ini file
- Members should use existing user IDs and passwords for web-based systems during DR testing

## Important Dates

- **November 01, 2025 (Saturday)**: Mock trading session from Disaster Recovery site for Electronic Gold Receipts segment

## Impact Assessment

**Market Impact**: Minimal - This is a mock trading session with no impact on live markets or actual trading activities.

**Operational Impact**: Low - Trading members participating in the DR drill will need to temporarily reconfigure their trading systems with DR connection parameters. The exercise is voluntary and designed to test business continuity capabilities.

**Member Impact**: Members choosing to participate need to update connection settings in their trading applications. Web-based applications (RTRMS, EBOSS, LEIPS, Extranet, etc.) will be accessible through alternate URLs provided in the circular.

**Technical Requirements**: Members using BOLT TWS, third-party trading software, or in-house systems must implement the specified IP addresses and port configurations for the DR environment. The circular includes detailed connectivity manuals and parameters for various applications including BOLT Plus Connectivity Manual Version 1.16.