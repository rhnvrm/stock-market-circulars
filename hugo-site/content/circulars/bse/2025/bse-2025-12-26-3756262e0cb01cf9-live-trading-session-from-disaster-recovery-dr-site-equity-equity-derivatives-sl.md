---
category: market-operations
circular_id: 3756262e0cb01cf9
date: '2025-12-26'
description: BSE notification regarding live trading session operations from the Disaster
  Recovery (DR) site for all segments including connection parameters and system access
  details.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={20B980F9-1726-4AA7-976C-1567A6B04399}&noticeno=20251226-1&dt=12/26/2025&icount=1&totcount=9&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Critical infrastructure notification affecting all trading members
  across all market segments. Requires immediate technical configuration changes for
  DR site connectivity.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251226-1&attachedId=9b59dfbb-9520-412a-aa1a-242d868beb9e
processing:
  attempts: 1
  content_hash: 713b97365fc18e69
  processed_at: '2025-12-26T09:27:16.419961'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-26T02:30:13+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={20B980F9-1726-4AA7-976C-1567A6B04399}&noticeno=20251226-1&dt=12/26/2025&icount=1&totcount=9&flag=0
severity: high
source: bse
stocks: []
tags:
- disaster-recovery
- trading-systems
- connectivity
- bolt-plus
- market-operations
- infrastructure
- equity
- derivatives
- slb
- currency-derivatives
- commodity-derivatives
- electronic-gold-receipts
title: Live Trading Session from Disaster Recovery (DR) Site – Equity, Equity Derivatives,
  SLB, Currency Derivatives, Commodity Derivatives, Electronic Gold Receipts Segment
---

## Summary

BSE has issued technical parameters and connection details for trading members to connect to the Disaster Recovery (DR) site for live trading sessions across all segments - Equity, Equity Derivatives, Securities Lending and Borrowing (SLB), Currency Derivatives, Commodity Derivatives, and Electronic Gold Receipts. The circular provides comprehensive connection parameters for BOLT Plus trading system and various web-based exchange systems.

## Key Points

- Trading members can connect to DR site using BOLT TWS or 3rd party trading applications through ETI APIs
- DR connection parameters provided for Commodity Derivatives segment via BOLT Plus
- Primary DR IP: 10.255.241.26, Port: 14910
- Secondary DR IP: 10.255.241.27, Port: 14910
- Configuration changes required in technical connection parameters at login
- Web-based systems (RTRMS, CLASS collateral, Extranet, etc.) accessible through specific DR URLs
- Online Trade File application requires remote server IP & port settings modification

## Regulatory Changes

No regulatory changes. This is an operational notification for disaster recovery procedures.

## Compliance Requirements

- Trading members must update technical connection parameters in BOLT TWS configuration settings window (accessible via scrip profile icon or Shift+F12)
- Members using 3rd party trading applications must change connection parameters to specified DR IP addresses and ports
- Online Trade File users must modify setting.ini file with DR connection parameters (Remote Server IP: 10.1.101.201, Port: 9001, Special Request Port: 9000)
- Members must use existing user IDs and passwords for web-based system access through DR site URLs

## Important Dates

Circular Date: December 26, 2025
No specific implementation deadline mentioned - appears to be effective immediately for DR operations.

## Impact Assessment

**Market Impact:** High - Affects all trading members across all market segments (Equity, Equity Derivatives, SLB, Currency Derivatives, Commodity Derivatives, and Electronic Gold Receipts).

**Operational Impact:** High - Requires immediate technical reconfiguration by all trading members to ensure business continuity. Members must be prepared to switch to DR site connectivity parameters when necessary.

**Technical Impact:** Critical infrastructure failover notification. Members need to:
- Update BOLT Plus/BOLT TWS configuration settings
- Reconfigure 3rd party trading applications with new DR IP addresses and ports
- Update setting.ini files for Online Trade File applications
- Test connectivity to DR site URLs for web-based systems (RTRMS, EBOSS, LEIPS, Extranet, etc.)

**Systems Affected:**
- BOLT Plus Trading System
- RTRMS (Risk & Trade Risk Management System)
- CLASS Collateral System
- EBOSS (Electronic Back Office Settlement System)
- LEIPS (Late Entry of Institutional Placement System)
- SME Market Making Compliance System
- Extranet/Extranet Plus
- iBBS
- Online Trade File (OTD)