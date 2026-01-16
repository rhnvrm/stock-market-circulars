---
category: market-operations
circular_id: ea4b86fd567a38c1
date: '2026-01-16'
description: BSE announces mock trading session for Electronic Gold Receipts (EGR)
  segment on January 17, 2026, with DR connectivity parameters for BOLT Plus trading
  system.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={7202D826-0650-47C2-AD1D-D20637731D3E}&noticeno=20260116-17&dt=01/16/2026&icount=17&totcount=63&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for system testing purposes with no impact
  on regular trading or market participants beyond technical preparation
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260116-17&attachedId=7e18151b-2603-4e16-b3aa-d2a3bdb64db1
processing:
  attempts: 1
  content_hash: d028fae285d5b4b7
  processed_at: '2026-01-16T15:51:13.888517'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-16T09:58:06+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={7202D826-0650-47C2-AD1D-D20637731D3E}&noticeno=20260116-17&dt=01/16/2026&icount=17&totcount=63&flag=0
severity: low
source: bse
stocks: []
tags:
- mock-trading
- electronic-gold-receipts
- egr
- bolt-plus
- disaster-recovery
- trading-system
- connectivity
- technical
title: Mock Trading on Saturday, January 17, 2026 for Electronic Gold Receipts Segment
---

## Summary

BSE has scheduled a mock trading session for the Electronic Gold Receipts (EGR) segment on Saturday, January 17, 2026. The circular provides technical connection parameters for trading members to connect to the Disaster Recovery (DR) site of the BOLT Plus trading system. Members can connect using BOLT TWS, third-party trading applications, or in-house developed systems through ETI APIs.

## Key Points

- Mock trading session scheduled for Electronic Gold Receipts segment on January 17, 2026
- Trading members must configure DR site connection parameters for BOLT Plus system
- Two connection methods available: BOLT TWS users and ETI API integration
- DR connectivity parameters provided for commodity derivatives segment
- Web-based systems (RTRMS, CLASS, Extranet, etc.) accessible through specified URLs

## Technical Configuration

### BOLT TWS Users
- Members must change technical connection parameters in configuration settings window at login
- Configuration settings accessible via scrip profile icon or "Shift+F12" shortcut keys

### ETI API Users (3rd Party Applications)
- Primary DR: IP 10.255.241.26, Port 14910
- Secondary DR: IP 10.255.241.27, Port 14910

### Web-Based Systems Access
- RTRMS: https://rtrms.bseindia.com
- CLASS Collateral: https://classseg.bseindia.com/application/applogin/login.aspx
- EBOSS: https://eboss.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp
- Extranet: https://member.bseindia.com/Extranet_Login.aspx
- iBBS: https://ibbs.bseindia.com/

## Compliance Requirements

- Trading members participating in EGR segment must configure their systems with DR connection parameters
- Members using BOLT TWS must update configuration settings before mock trading session
- Members using third-party applications must update IP and port settings in their trading applications
- Existing user IDs and passwords to be used for web-based system access

## Important Dates

- **January 17, 2026 (Saturday)**: Mock trading session for Electronic Gold Receipts segment

## Impact Assessment

This is a routine mock trading exercise with minimal market impact. The session is designed to test disaster recovery systems and ensure trading members can successfully connect to backup infrastructure. No impact on regular trading activities. Only members participating in the EGR segment need to take action. The mock session helps ensure business continuity preparedness and system resilience for the Electronic Gold Receipts trading segment.