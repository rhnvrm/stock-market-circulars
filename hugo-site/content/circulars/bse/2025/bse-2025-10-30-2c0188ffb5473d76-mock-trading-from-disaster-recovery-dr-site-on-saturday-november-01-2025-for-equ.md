---
category: market-operations
circular_id: 2c0188ffb5473d76
date: '2025-10-30'
description: BSE announces mock trading session from Disaster Recovery site on November
  01, 2025 for equity segment to test DR infrastructure and member connectivity.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={B77F02B1-F32A-4A81-A7B1-5FAE346F9A0F}&noticeno=20251030-51&dt=10/30/2025&icount=51&totcount=63&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Mandatory participation in DR mock trading session affects all trading
  members but is routine infrastructure testing with no market impact
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251030-51&attachedId=aa0fb875-45e7-4690-9ef6-0ec5777d1afb
processing:
  attempts: 1
  content_hash: e322595e4b5b7a25
  processed_at: '2025-10-30T18:37:57.029254'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-30T14:03:52+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={B77F02B1-F32A-4A81-A7B1-5FAE346F9A0F}&noticeno=20251030-51&dt=10/30/2025&icount=51&totcount=63&flag=0
severity: medium
source: bse
stocks: []
tags:
- connectivity
- disaster-recovery
- dr-site
- equity
- market-infrastructure
- mock-trading
- trading-platform
title: Mock Trading from Disaster Recovery (DR) Site on Saturday, November 01, 2025
  for Equity Segment
---

## Summary

BSE has scheduled a mock trading session from its Disaster Recovery (DR) site on Saturday, November 01, 2025 for the equity segment. Trading members must connect to the DR site using modified technical parameters for BOLT Plus trading system, either through BOLT TWS or third-party trading applications via ETI APIs. The circular provides detailed connection parameters and configuration settings for both leased line and internet connectivity.

## Key Points

- Mock trading session scheduled for Saturday, November 01, 2025 from DR site
- Applicable to equity segment trading members
- Members can connect via BOLT TWS or third-party trading applications using ETI APIs
- Configuration changes required in technical connection parameters
- Primary DR connection: IP 10.255.241.10, Port 18909
- Secondary DR connection: IP 10.255.241.11, Port 18909
- Web-based systems (RTRMS, CLASS, EBOSS, LEIPS, Extranet) accessible through alternate URLs
- BOLT TWS users must modify configuration settings at login using Shift+F12 or scrip profile icon

## Regulatory Changes

No regulatory changes introduced. This is a routine disaster recovery testing exercise.

## Compliance Requirements

- Trading members must ensure their systems are configured to connect to DR site parameters
- BOLT TWS users must change technical connection parameters in configuration settings window
- Third-party application users must update ETI API connection parameters (Primary DR: IP 10.255.241.10, Port 18909; Secondary DR: IP 10.255.241.11, Port 18909)
- Members using web-based systems must access through DR URLs provided for RTRMS, CLASS collateral, EBOSS, LEIPS, Extranet, and other applications
- Online Trade File users must modify setting.ini file with DR remote server IP (10.1.101.201) and port (9001)
- Members must test connectivity using existing user IDs and passwords

## Important Dates

- **November 01, 2025 (Saturday)**: Mock trading session from DR site for equity segment

## Impact Assessment

**Operational Impact**: Medium - All equity trading members must participate and configure systems for DR connectivity. Requires technical preparation and testing of backup infrastructure.

**Market Impact**: Low - Mock trading session on Saturday (non-trading day) with no impact on regular market operations.

**Technical Requirements**: Trading members must have technical teams available to modify connection parameters across multiple systems including BOLT TWS, third-party applications, and web-based platforms. Members using leased line and internet connectivity both need to update configurations.

**Business Continuity**: This exercise validates BSE's disaster recovery capabilities and ensures trading members can seamlessly switch to DR infrastructure in case of primary site failure, strengthening overall market resilience.