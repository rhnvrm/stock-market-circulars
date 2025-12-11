---
category: market-operations
circular_id: c2c3be9f34c18ab0
date: '2025-10-30'
description: BSE announces mock trading session from DR site on November 01, 2025
  for Electronic Gold Receipts segment to test business continuity preparedness.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={1FA4A633-BD64-47FC-9425-1F2B27E247FC}&noticeno=20251030-53&dt=10/30/2025&icount=53&totcount=63&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Scheduled DR mock trading for EGR segment is routine operational testing
  with medium importance for trading members to ensure connectivity preparedness,
  but does not affect live trading or have immediate market impact.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251030-53&attachedId=5a64e126-15c3-4ebe-9ba6-7cebdfc4991b
processing:
  attempts: 1
  content_hash: 534fb5ceb145bbaf
  processed_at: '2025-10-30T21:19:40.504385'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-30T14:03:54+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={1FA4A633-BD64-47FC-9425-1F2B27E247FC}&noticeno=20251030-53&dt=10/30/2025&icount=53&totcount=63&flag=0
severity: medium
source: bse
stocks: []
tags:
- derivatives
- disaster-recovery
- dr-site
- egr
- market-infrastructure
- mock-trading
- trading-platform
title: Mock Trading from Disaster Recovery (DR) Site on Saturday, November 01, 2025
  for Electronic Gold Receipts Segment
---

## Summary

BSE has scheduled a mock trading session from its Disaster Recovery (DR) site on Saturday, November 01, 2025, for the Electronic Gold Receipts (EGR) segment. Trading members need to configure their systems to connect to the DR site using modified technical connection parameters for BOLT Plus trading system. The circular provides detailed connectivity instructions for BOLT TWS users, third-party trading applications using ETI APIs, and web-based systems.

## Key Points

- Mock trading session scheduled for Electronic Gold Receipts segment on November 01, 2025 (Saturday)
- Trading members must connect to DR site using modified connection parameters
- Two connection methods available: BOLT TWS or third-party/in-house applications through ETI APIs
- DR connection parameters provided for Commodity Derivatives segment BOLT Plus system
- Web-based systems (RTRMS, CLASS collateral, Extranet, EBOSS, etc.) accessible through specific DR URLs and IP addresses
- Configuration changes required in trading applications to connect to DR site

## Regulatory Changes

No regulatory changes introduced. This is an operational circular for disaster recovery testing.

## Compliance Requirements

**For BOLT TWS Users:**
- Change technical connection parameters in configuration settings window at login
- Access configuration settings using scrip profile icon or "Shift+F12" shortcut keys

**For Third-Party Trading Applications (ETI API):**
- Update technical connection parameters in trading applications:
  - Primary DR: IP 10.255.241.26, Port 14910
  - Secondary DR: IP 10.255.241.27, Port 14910

**For Web-Based Systems:**
- Use provided DR weblinks and IP addresses for systems including:
  - RTRMS: https://rtrms.bseindia.com
  - CLASS Collateral: https://classseg.bseindia.com
  - EBOSS: https://ebossll.bseindia.com (Leased Line) or https://eboss.bseindia.com (Internet)
  - Extranet: https://memberll.bseindia.com/ or https://member.bseindia.com
  - LEIPS: https://leipsmmll.bseindia.com or https://leipsmm.bseindia.com

**For Online Trade File Application:**
- Modify setting.ini file with DR parameters:
  - REMOTE SERVER IP: 10.1.101.201
  - REMOTE SERVER PORT: 9001
  - SPECIAL REQUEST PORT: 9000

## Important Dates

- **November 01, 2025 (Saturday)**: Mock trading session from DR site for Electronic Gold Receipts segment

## Impact Assessment

**Operational Impact:**
- Trading members must prepare and test DR connectivity configurations
- No impact on regular trading activities as session scheduled for Saturday
- Testing ensures business continuity preparedness for EGR segment

**Market Impact:**
- Low immediate market impact as this is a mock trading exercise
- Strengthens market infrastructure resilience and disaster recovery capabilities

**Technical Impact:**
- Trading members need to configure systems with DR site parameters
- Both manual (BOLT TWS) and automated (API-based) trading setups must be tested
- Successful participation validates member readiness for actual DR scenarios