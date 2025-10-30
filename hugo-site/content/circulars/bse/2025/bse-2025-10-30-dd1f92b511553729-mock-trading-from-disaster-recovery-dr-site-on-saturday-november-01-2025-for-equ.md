---
category: market-operations
circular_id: dd1f92b511553729
date: '2025-10-30'
description: BSE announces mock trading session from Disaster Recovery site for Equity
  Derivatives segment on November 01, 2025 with detailed DR connection parameters
  for BOLT Plus and web-based systems.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={D1A20CEF-6EDC-41B5-9341-495C7F326CEE}&noticeno=20251030-52&dt=10/30/2025&icount=52&totcount=57&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Medium importance as this is a scheduled mock trading session for disaster
  recovery testing, requiring trading members to update technical connection parameters
  but not affecting live trading operations.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251030-52&attachedId=192bd5a0-6e8e-44ec-b3a5-45075e61cb6a
processing:
  attempts: 1
  content_hash: 0f721f5aaab3cfe9
  processed_at: '2025-10-30T15:34:29.186594'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-30T14:03:53+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={D1A20CEF-6EDC-41B5-9341-495C7F326CEE}&noticeno=20251030-52&dt=10/30/2025&icount=52&totcount=57&flag=0
severity: medium
source: bse
stocks: []
tags:
- mock-trading
- disaster-recovery
- equity-derivatives
- bolt-plus
- trading-system
- technical-connectivity
- eti-api
- rtrms
- market-infrastructure
title: Mock Trading from Disaster Recovery (DR) Site on Saturday, November 01, 2025
  for Equity Derivatives Segment
---

## Summary

BSE will conduct mock trading from its Disaster Recovery (DR) site on Saturday, November 01, 2025 for the Equity Derivatives segment. Trading members need to connect to the DR site using BOLT Plus trading system through BOLT TWS, third-party applications, or ETI APIs with specified DR connection parameters. The circular provides comprehensive technical details for connecting to both trading systems and web-based platforms during the mock session.

## Key Points

- Mock trading session scheduled for Saturday, November 01, 2025 for Equity Derivatives segment
- Trading members can connect via BOLT TWS or third-party applications using ETI APIs
- DR connection parameters provided for Primary DR (IP: 10.255.241.16; Port: 15910) and Secondary DR (IP: 10.255.241.17; Port: 15910)
- BOLT TWS users must change technical connection parameters in configuration settings using Shift+F12
- Web-based systems (RTRMS, CLASS Collateral, Extranet, EBOSS, LEIPS) accessible through specified DR URLs
- Updated BOLTPLUS Connectivity Manual version 1.16 dated October 6, 2025 included

## Regulatory Changes

No regulatory changes. This is a scheduled operational exercise for disaster recovery preparedness testing.

## Compliance Requirements

- Trading members must configure their systems with DR connection parameters before the mock session
- BOLT TWS users need to update configuration settings through scrip profile icon or Shift+F12 shortcut
- Third-party trading application users must update ETI API connection parameters to DR IP addresses and ports
- Members using web-based systems should access through provided DR URLs with existing credentials
- Online Trade File application users must modify setting.ini file with DR remote server IP (10.1.101.203) and port (9011)

## Important Dates

- **November 01, 2025**: Mock trading session from Disaster Recovery site for Equity Derivatives segment

## Impact Assessment

**Operational Impact**: Medium - Trading members need to temporarily reconfigure their trading systems to connect to DR site. This is a critical business continuity exercise to ensure trading can continue from backup infrastructure in case of primary site failure.

**Technical Requirements**: Members must update connection parameters across multiple systems including BOLT Plus (TWS and ETI), RTRMS, CLASS Collateral, Extranet, EBOSS, LEIPS, and other web-based platforms. Different connection methods require specific IP addresses, ports, and URLs for DR site access.

**Business Continuity**: This mock session validates the exchange's disaster recovery capabilities and ensures trading members are familiar with failover procedures, critical for maintaining market operations during emergencies.

**Member Preparation**: Trading members should test connectivity in advance and ensure technical teams are available during the mock session to troubleshoot any connection issues with the DR infrastructure.