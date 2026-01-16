---
category: market-operations
circular_id: 9addd6615c73bc48
date: '2026-01-16'
description: BSE announces mock trading session for Currency Derivatives segment on
  January 17, 2026, with DR site connectivity parameters for BOLT Plus trading system.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={0593291F-2287-438B-A12F-097ED7A0A5F2}&noticeno=20260116-18&dt=01/16/2026&icount=18&totcount=63&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for testing DR infrastructure; no impact
  on regular trading or market participants' operations
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260116-18&attachedId=3d4b4af9-7302-452b-841d-502b28849faf
processing:
  attempts: 1
  content_hash: e2f4681a0793e2a9
  processed_at: '2026-01-16T15:50:56.568275'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-16T09:58:07+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={0593291F-2287-438B-A12F-097ED7A0A5F2}&noticeno=20260116-18&dt=01/16/2026&icount=18&totcount=63&flag=0
severity: low
source: bse
stocks: []
tags:
- mock-trading
- currency-derivatives
- CDX
- BOLT-Plus
- disaster-recovery
- trading-system
- connectivity-parameters
title: Mock Trading on Saturday, January 17, 2026 for Currency Derivatives Segment
---

## Summary

BSE has scheduled a mock trading session for the Currency Derivatives segment on Saturday, January 17, 2026. The circular provides detailed technical connection parameters for trading members to connect to the Disaster Recovery (DR) site of the BOLT Plus trading system. Trading members can connect using BOLT TWS, third-party trading applications from empanelled vendors, or in-house developed systems through ETI APIs.

## Key Points

- Mock trading session scheduled for Currency Derivatives segment on January 17, 2026
- Trading members must use DR site connection parameters for the mock session
- Two connectivity options available: BOLT TWS and third-party applications via ETI APIs
- DR Primary IP: 10.255.241.26, Port: 13910
- DR Secondary IP: 10.255.241.27, Port: 13910
- Web-based systems (RTRMS, CLASS, EBOSS, Extranet) accessible through specified URLs
- Configuration changes required in trading applications for DR connectivity

## Regulatory Changes

No regulatory changes introduced. This is a scheduled mock trading session for testing disaster recovery infrastructure.

## Compliance Requirements

- Trading members participating in the mock session must configure their trading systems with DR site connection parameters
- BOLT TWS users must change technical connection parameters in configuration settings window (accessible via scrip profile icon or Shift+F12)
- Third-party application users must update ETI API connection parameters to DR site IPs and ports
- Members should test connectivity to web-based systems using provided DR URLs

## Important Dates

- **January 17, 2026 (Saturday)**: Mock trading session for Currency Derivatives segment

## Impact Assessment

**Market Impact**: None. This is a mock trading session with no impact on regular market operations.

**Operational Impact**: Low. Trading members need to temporarily reconfigure their systems to connect to DR infrastructure for testing purposes. This is routine testing to ensure business continuity preparedness.

**Technical Requirements**: Trading members must update connection parameters in their trading applications, including primary and secondary DR IPs, ports, and web-based system URLs for the mock session.