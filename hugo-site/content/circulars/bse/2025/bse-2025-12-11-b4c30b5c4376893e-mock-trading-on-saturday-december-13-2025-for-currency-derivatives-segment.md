---
category: market-operations
circular_id: b4c30b5c4376893e
date: '2025-12-11'
description: BSE announces mock trading session on Saturday, December 13, 2025 for
  Currency Derivatives segment with DR site connectivity parameters.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={D0BC3F24-3409-4746-A156-B2D89263867E}&noticeno=20251211-55&dt=12/11/2025&icount=55&totcount=88&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for disaster recovery testing with no
  impact on regular trading operations
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251211-55&attachedId=75cc48f2-0e16-4cae-ba91-d86cde432ae3
processing:
  attempts: 1
  content_hash: 3976b3d685e12f12
  processed_at: '2025-12-11T15:44:42.218226'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-11T14:04:05+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={D0BC3F24-3409-4746-A156-B2D89263867E}&noticeno=20251211-55&dt=12/11/2025&icount=55&totcount=88&flag=0
severity: low
source: bse
stocks: []
tags:
- connectivity
- derivatives
- disaster-recovery
- market-infrastructure
- mock-trading
- trading-platform
title: Mock Trading on Saturday, December 13, 2025 for Currency Derivatives Segment
---

## Summary

BSE has scheduled a mock trading session on Saturday, December 13, 2025 for the Currency Derivatives segment to test disaster recovery (DR) site connectivity. Trading members can connect to the DR site using BOLT TWS or third-party trading applications through ETI APIs with specified connection parameters.

## Key Points

- Mock trading session scheduled for Saturday, December 13, 2025
- Applies to Currency Derivatives segment only
- DR site connectivity testing for BOLT Plus trading system
- Two connection methods available: BOLT TWS and third-party applications via ETI APIs
- DR connection parameters provided for Primary and Secondary DR sites
- Web-based systems (RTRMS, CLASS, Extranet, etc.) accessible through specified URLs

## Connectivity Details

### BOLT TWS Users
- Change technical connection parameters in configuration settings window at login
- Access via scrip profile icon or "Shift+F12" shortcut keys

### Third-Party Trading Applications (ETI APIs)
- Primary DR: IP 10.255.241.26, Port 13910
- Secondary DR: IP 10.255.241.27, Port 13910

### Web-Based Systems Access
- RTRMS: https://rtrms.bseindia.com
- CLASS Collateral: https://classseg.bseindia.com
- EBOSS: https://eboss.bseindia.com
- LEIPS: https://leipsmm.bseindia.com
- Extranet: https://member.bseindia.com
- iBBS: https://ibbs.bseindia.com
- All accessible using existing user ID and password

## Regulatory Changes

No regulatory changes announced. This is a routine operational testing exercise.

## Compliance Requirements

- Trading members should configure DR connection parameters for mock trading session
- Members using BOLT TWS must update configuration settings
- Members using third-party applications must update ETI API connection parameters
- Testing participation recommended to ensure business continuity preparedness

## Important Dates

- **Mock Trading Date**: Saturday, December 13, 2025
- **Segment**: Currency Derivatives

## Impact Assessment

**Market Impact**: None - mock trading session on non-trading day

**Operational Impact**: Low - routine DR testing exercise to ensure business continuity

**Member Impact**: Minimal - optional participation for testing DR connectivity and familiarization with disaster recovery procedures

**Purpose**: Validates disaster recovery infrastructure and ensures trading members can seamlessly connect to backup systems in case of primary site failure