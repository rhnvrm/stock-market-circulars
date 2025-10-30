---
category: market-operations
circular_id: 625d8e830d6688c4
date: '2025-10-30'
description: BSE announces mock trading session from Disaster Recovery site on November
  01, 2025 for Commodity Derivatives segment to test business continuity systems.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={7301E078-E1B5-41E4-92E3-EA7F9383D457}&noticeno=20251030-55&dt=10/30/2025&icount=55&totcount=57&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Routine DR drill for commodity segment requiring trading members to
  test backup connectivity parameters but not affecting live trading operations
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251030-55&attachedId=91be77fe-2191-4ea8-a122-9d7eca49b6af
processing:
  attempts: 1
  content_hash: 26450990f2b0b095
  processed_at: '2025-10-30T15:32:40.717319'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-30T14:03:56+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={7301E078-E1B5-41E4-92E3-EA7F9383D457}&noticeno=20251030-55&dt=10/30/2025&icount=55&totcount=57&flag=0
severity: medium
source: bse
stocks: []
tags:
- mock-trading
- disaster-recovery
- commodity-derivatives
- business-continuity
- bolt-plus
- trading-systems
- technical-connectivity
title: Mock Trading from Disaster Recovery (DR) Site on Saturday, November 01, 2025
  for Commodity Derivatives Segment
---

## Summary

BSE has scheduled a mock trading session from its Disaster Recovery (DR) site on Saturday, November 01, 2025, for the Commodity Derivatives segment. Trading members must connect to the DR site using modified technical parameters for BOLT Plus trading system through either BOLT TWS or third-party trading applications via ETI APIs. The exercise tests business continuity preparedness and backup systems connectivity.

## Key Points

- Mock trading session scheduled for November 01, 2025 (Saturday)
- Applies to Commodity Derivatives segment only
- Trading members must use DR-specific connection parameters
- BOLT TWS users need to change configuration settings at login using Shift+F12
- Third-party applications via ETI APIs must update IP addresses and ports
- Primary DR connection: IP 10.255.241.26, Port 14910
- Secondary DR connection: IP 10.255.241.27, Port 14910
- Web-based systems (RTRMS, CLASS, EBOSS, LEIPS, Extranet) accessible via specific DR URLs
- Online Trade File application requires setting.ini file modifications

## Regulatory Changes

No regulatory changes introduced. This is a technical drill to ensure trading members can seamlessly switch to backup infrastructure during disruptions.

## Compliance Requirements

- Trading members must configure their trading systems with DR connection parameters before the mock session
- BOLT TWS users must invoke configuration settings window using scrip profile icon or Shift+F12 shortcut
- Members using third-party applications must update ETI API connection parameters (Primary and Secondary DR IPs and Ports)
- Members using web-based systems should access via DR-specific URLs provided
- Online Trade File users must modify remote server IP and port settings in setting.ini file
- Existing user IDs and passwords remain valid for DR systems

## Important Dates

- **November 01, 2025 (Saturday)**: Mock trading session from DR site for Commodity Derivatives segment

## Impact Assessment

**Operational Impact**: Medium - Trading members need to reconfigure technical systems temporarily for the DR drill. This requires technical resources and coordination but occurs on a non-trading day (Saturday) to minimize disruption.

**Market Impact**: Low - No impact on live trading as the exercise is conducted on a weekend. This is a routine business continuity test.

**Technical Requirements**: Trading members must ensure their technical teams are available to:
- Update connection parameters in BOLT TWS configuration
- Modify ETI API settings for third-party applications
- Test connectivity to DR web-based systems
- Verify all backup systems function correctly

**Preparedness Benefit**: High - Regular DR drills ensure trading members can quickly switch to backup infrastructure during actual disasters, maintaining market continuity and protecting investor interests.