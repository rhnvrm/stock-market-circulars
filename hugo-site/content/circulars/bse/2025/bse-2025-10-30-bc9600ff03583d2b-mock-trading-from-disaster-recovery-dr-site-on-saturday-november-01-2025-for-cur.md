---
category: market-operations
circular_id: bc9600ff03583d2b
date: '2025-10-30'
description: BSE announces mock trading session from Disaster Recovery site for Currency
  Derivatives segment on November 01, 2025 to test DR infrastructure and connectivity.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={9AE1D6EC-9E3B-4223-8DCF-373909257E22}&noticeno=20251030-54&dt=10/30/2025&icount=54&totcount=63&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational circular for DR testing affecting trading members in Currency
  Derivatives segment. Requires technical configuration changes but is a routine mock
  session with no live trading impact.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251030-54&attachedId=d2d2da23-a33c-45ee-99fd-b9b854b3ce1d
processing:
  attempts: 1
  content_hash: aaef7b207ef99d9d
  processed_at: '2025-10-30T18:36:59.106188'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-30T14:03:55+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={9AE1D6EC-9E3B-4223-8DCF-373909257E22}&noticeno=20251030-54&dt=10/30/2025&icount=54&totcount=63&flag=0
severity: medium
source: bse
stocks: []
tags:
- cdx
- derivatives
- disaster-recovery
- mock-trading
- trading-platform
title: Mock Trading from Disaster Recovery (DR) Site on Saturday, November 01, 2025
  for Currency Derivative Segment
---

## Summary

BSE has announced a mock trading session from its Disaster Recovery (DR) site scheduled for Saturday, November 01, 2025 for the Currency Derivatives segment. Trading members need to connect to the DR site using modified connection parameters for BOLT Plus trading system, either through BOLT TWS or third-party trading applications via ETI APIs. The exercise tests business continuity infrastructure and member connectivity to DR systems.

## Key Points

- Mock trading session scheduled for November 01, 2025 (Saturday)
- Applies to Currency Derivatives (CDX) segment only
- Trading members must modify technical connection parameters
- Two connection methods available: BOLT TWS or ETI APIs through third-party applications
- DR connection parameters provided for primary and secondary servers
- Members can also access web-based systems (RTRMS, CLASS, EBOSS, etc.) through DR URLs
- Testing ensures preparedness for actual DR scenarios

## Technical Connection Details

### BOLT TWS Users
- Members must change technical connection parameters in configuration settings window at login
- Configuration accessible via scrip profile icon or "Shift+F12" shortcut keys

### ETI API Users (Third-party Applications)
- Primary DR: IP 10.255.241.26, Port 13910
- Secondary DR: IP 10.255.241.27, Port 13910

### Web-based Systems Access
Members can connect to DR versions of:
- RTRMS (Risk and Trade Reporting Management System)
- CLASS Collateral
- EBOSS (Exchange Back Office Support System)
- LEIPS (Leased Line Interface for Primary Segment)
- Extranet and Extranet Plus
- iBBS
- Online Trade File (OTD)

Specific DR IP addresses and URLs provided for both leased line and internet connectivity.

## Compliance Requirements

- Trading members must configure their systems with DR connection parameters before the mock session
- Members using BOLT TWS need to update configuration settings
- Members using third-party trading applications must update IP and port settings in their systems
- Testing participation ensures compliance with business continuity requirements
- Members should verify connectivity to all required systems (trading and back-office)

## Important Dates

- **Mock Trading Date**: Saturday, November 01, 2025
- **Circular Date**: October 30, 2025

## Impact Assessment

**Operational Impact**: Medium - Trading members in Currency Derivatives segment must reconfigure systems for the mock session. This is a planned activity on a weekend (Saturday) to minimize disruption to regular trading.

**Market Impact**: Low - No impact on live trading as this is a mock session conducted on a non-trading day.

**Technical Impact**: Medium - Requires technical teams to modify connection parameters and verify DR connectivity across multiple systems including trading platforms and back-office applications.

**Business Continuity**: High importance for preparedness - Regular DR testing is critical for ensuring seamless failover capability in case of actual disasters or primary site failures. This exercise validates that trading members can successfully connect and operate from the DR infrastructure.