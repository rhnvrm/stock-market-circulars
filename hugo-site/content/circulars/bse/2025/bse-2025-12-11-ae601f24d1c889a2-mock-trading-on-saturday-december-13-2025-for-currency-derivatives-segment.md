---
category: market-operations
circular_id: ae601f24d1c889a2
date: '2025-12-11'
description: BSE announces mock trading session on Saturday, December 13, 2025 for
  Currency Derivatives segment with DR site connectivity details for BOLT Plus trading
  system.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={D0BC3F24-3409-4746-A156-B2D89263867E}&noticeno=20251211-55&dt=12/11/2025&icount=55&totcount=90&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for testing DR site connectivity with
  no impact on live trading operations
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251211-55&attachedId=75cc48f2-0e16-4cae-ba91-d86cde432ae3
processing:
  attempts: 1
  content_hash: 375e8926d6e48414
  processed_at: '2025-12-11T18:54:36.921629'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-11T14:04:05+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={D0BC3F24-3409-4746-A156-B2D89263867E}&noticeno=20251211-55&dt=12/11/2025&icount=55&totcount=90&flag=0
severity: low
source: bse
stocks: []
tags:
- cdx
- connectivity
- derivatives
- disaster-recovery
- market-infrastructure
- mock-trading
- trading-platform
title: Mock Trading on Saturday, December 13, 2025 for Currency Derivatives Segment
---

## Summary

BSE has scheduled a mock trading session for the Currency Derivatives segment on Saturday, December 13, 2025. The circular provides technical connection parameters for trading members to connect to the Disaster Recovery (DR) site of the BOLT Plus trading system using either BOLT TWS or third-party trading applications through ETI APIs.

## Key Points

- Mock trading session scheduled for Currency Derivatives segment on December 13, 2025 (Saturday)
- Trading members can connect using BOLT TWS or third-party trading applications via ETI APIs
- DR site connection parameters provided for both BOLT TWS users and ETI API users
- Primary DR IP: 10.255.241.26, Port: 13910
- Secondary DR IP: 10.255.241.27, Port: 13910
- Web-based systems (RTRMS, CLASS, EBOSS, Extranet) accessible through provided URLs
- BOLT Plus Connectivity Manual Version 1.16 dated October 6, 2025 included as reference

## Regulatory Changes

No regulatory changes introduced. This is a routine mock trading session for testing disaster recovery infrastructure.

## Compliance Requirements

- Trading members must update technical connection parameters in their configuration settings to connect to DR site
- BOLT TWS users need to change parameters in configuration settings window (accessible via scrip profile icon or Shift+F12)
- Members using third-party applications must update ETI API connection parameters with provided DR IP addresses and ports
- Members using Online Trade File application must update remote server IP and port settings in setting.ini file

## Important Dates

- **December 13, 2025 (Saturday)**: Mock trading session for Currency Derivatives segment

## Impact Assessment

**Market Impact**: None. This is a mock trading session with no effect on live market operations.

**Operational Impact**: Low. Trading members need to make temporary configuration changes to participate in the DR mock session. This is a routine exercise to test business continuity and disaster recovery preparedness for the Currency Derivatives segment.

**Technical Requirements**: Members must configure their trading systems with DR site parameters. Web-based systems remain accessible through both leased line and internet URLs provided in the annexure.