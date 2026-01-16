---
category: market-operations
circular_id: 9f61d3b632bea0e0
date: '2026-01-16'
description: BSE announces mock trading session for Currency Derivatives segment on
  Saturday, January 17, 2026, with DR site connectivity details for BOLT Plus trading
  system.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={0593291F-2287-438B-A12F-097ED7A0A5F2}&noticeno=20260116-18&dt=01/16/2026&icount=18&totcount=42&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for testing purposes with no impact on
  live trading or market operations. Only affects technical connectivity parameters
  for DR site access during mock session.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260116-18&attachedId=3d4b4af9-7302-452b-841d-502b28849faf
processing:
  attempts: 1
  content_hash: 65a0108cf7760f99
  processed_at: '2026-01-16T13:00:51.118290'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-16T09:58:07+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={0593291F-2287-438B-A12F-097ED7A0A5F2}&noticeno=20260116-18&dt=01/16/2026&icount=18&totcount=42&flag=0
severity: low
source: bse
stocks: []
tags:
- mock-trading
- currency-derivatives
- bolt-plus
- dr-connectivity
- trading-system
- technical-configuration
title: Mock Trading on Saturday, January 17, 2026 for Currency Derivatives Segment
---

## Summary

BSE has announced a mock trading session for the Currency Derivatives (CDX) segment scheduled for Saturday, January 17, 2026. The circular provides detailed technical connection parameters for trading members to connect to the Disaster Recovery (DR) site of the BOLT Plus trading system during the mock session. Members can connect using BOLT TWS, third-party trading applications from empanelled vendors, or in-house developed systems through ETI APIs.

## Key Points

- Mock trading session scheduled for Saturday, January 17, 2026 for Currency Derivatives segment
- Trading members must use DR site connection parameters for BOLT Plus trading system
- Two connection methods available: BOLT TWS users and 3rd party trading applications through ETI APIs
- DR site connectivity details provided for Primary DR (IP: 10.255.241.26; Port: 13910) and Secondary DR (IP: 10.255.241.27; Port: 13910)
- Web-based systems like RTRMS, CLASS collateral, Extranet remain accessible through specified URLs
- Configuration changes required in technical connection parameters during login

## Regulatory Changes

No regulatory changes introduced. This is a technical circular for mock trading session connectivity.

## Compliance Requirements

**For BOLT TWS Users:**
- Change technical connection parameters in configuration settings window at time of login
- Configuration settings window can be invoked using scrip profile icon or "Shift+F12" shortcut keys

**For 3rd Party Trading Application Users:**
- Update technical connection parameters in respective trading applications
- Configure Primary DR: IP 10.255.241.26, Port 13910
- Configure Secondary DR: IP 10.255.241.27, Port 13910

**Web-Based Systems Access:**
- Connect to RTRMS, RTRMS-ZT, CLASS collateral, Extranet using provided weblinks with existing credentials
- Specific IP addresses and ports provided for leased line and internet connectivity

## Important Dates

- **January 17, 2026 (Saturday)**: Mock trading session for Currency Derivatives segment

## Impact Assessment

**Market Impact:** Minimal. This is a mock trading session for testing purposes only and does not affect live market operations.

**Operational Impact:** Low. Trading members need to temporarily modify their technical connection parameters to connect to the DR site during the mock session. The changes are reversible and only applicable for the mock trading period.

**Technical Impact:** Trading members using BOLT TWS or third-party applications must ensure proper configuration of DR site parameters. Web-based system users can continue using existing credentials with DR-specific URLs provided in the circular.

**Segment Affected:** Currency Derivatives segment only. No impact on equity, equity derivatives, debt, or commodity segments.