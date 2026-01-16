---
category: market-operations
circular_id: 1a428a5929c8479f
date: '2026-01-16'
description: BSE announces mock trading session for Commodity Derivatives segment
  on Saturday, January 17, 2026, with DR site connectivity details and connection
  parameters for trading members.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={ABC1BFBA-36EC-47C4-8BD4-8F9A849E6A88}&noticeno=20260116-19&dt=01/16/2026&icount=19&totcount=63&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for testing DR infrastructure with no
  impact on live trading or market participants' obligations
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260116-19&attachedId=adf32dbd-6aa5-4373-b215-fcd706a96bff
processing:
  attempts: 1
  content_hash: 7341b0773b5728c6
  processed_at: '2026-01-16T15:50:36.080760'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-16T09:58:08+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={ABC1BFBA-36EC-47C4-8BD4-8F9A849E6A88}&noticeno=20260116-19&dt=01/16/2026&icount=19&totcount=63&flag=0
severity: low
source: bse
stocks: []
tags:
- mock-trading
- commodity-derivatives
- disaster-recovery
- bolt-plus
- trading-system
- eti-api
- market-infrastructure
title: Mock Trading on Saturday, January 17, 2026 for Commodity Derivatives Segment
---

## Summary

BSE has scheduled a mock trading session for the Commodity Derivatives segment on Saturday, January 17, 2026. This session will utilize the Disaster Recovery (DR) site of the BOLT Plus trading system. Trading members can connect using BOLT TWS, third-party trading applications from empanelled vendors, or in-house developed systems through ETI APIs. The circular provides detailed technical connection parameters for both BOLT TWS users and ETI API users.

## Key Points

- Mock trading session scheduled for Commodity Derivatives segment on January 17, 2026
- Session will be conducted on DR site of BOLT Plus trading system
- Three connection methods available: BOLT TWS, third-party applications, or in-house systems via ETI APIs
- Primary DR connection: IP 10.255.241.26, Port 14910
- Secondary DR connection: IP 10.255.241.27, Port 14910
- BOLT TWS users must change technical parameters via configuration settings (Shift+F12)
- Web-based systems (RTRMS, CLASS, Extranet, etc.) accessible through provided URLs

## Regulatory Changes

No regulatory changes introduced. This is a routine operational exercise.

## Compliance Requirements

- Trading members must configure their systems with correct DR site connection parameters
- BOLT TWS users: Update configuration settings at login using scrip profile icon or Shift+F12
- ETI API users: Update technical connection parameters in trading applications
- Members should ensure connectivity to web-based systems using existing credentials

## Important Dates

- **January 17, 2026 (Saturday)**: Mock trading session for Commodity Derivatives segment

## Impact Assessment

**Operational Impact**: Minimal. This is a scheduled mock trading session for testing disaster recovery infrastructure. No impact on live trading operations.

**Market Impact**: None. Mock trading does not affect actual market transactions or positions.

**Technical Impact**: Trading members need to temporarily reconfigure connection parameters to participate in the mock session. This is a routine exercise to ensure business continuity preparedness.

**Scope**: Limited to Commodity Derivatives segment participants who wish to test their DR connectivity.

## Technical Connection Details

**For BOLT TWS Users:**
- Access configuration settings via scrip profile icon or Shift+F12 shortcut
- Update connection parameters as per DR site specifications

**For ETI API Users:**
- Primary DR: IP 10.255.241.26, Port 14910
- Secondary DR: IP 10.255.241.27, Port 14910

**Web-Based Systems Access:**
- RTRMS: https://rtrms.bseindia.com
- CLASS Collateral: https://classseg.bseindia.com
- Extranet: https://memberll.bseindia.com
- EBOSS: https://eboss.bseindia.com
- Other systems accessible via provided leased line and internet URLs