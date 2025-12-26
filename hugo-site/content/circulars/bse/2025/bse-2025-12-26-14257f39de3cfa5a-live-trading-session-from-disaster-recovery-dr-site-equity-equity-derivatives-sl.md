---
category: market-operations
circular_id: 14257f39de3cfa5a
date: '2025-12-26'
description: BSE announces live trading session from Disaster Recovery (DR) site for
  all segments including Equity, Derivatives, SLB, Currency, Commodity, and EGR with
  updated connection parameters for trading members.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={20B980F9-1726-4AA7-976C-1567A6B04399}&noticeno=20251226-1&dt=12/26/2025&icount=1&totcount=43&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Critical infrastructure change requiring immediate action from all
  trading members to update connection parameters for DR site access across all trading
  segments
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251226-1&attachedId=9b59dfbb-9520-412a-aa1a-242d868beb9e
processing:
  attempts: 1
  content_hash: 65f597bdbf59d02c
  processed_at: '2025-12-26T15:49:18.103667'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-26T02:30:13+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={20B980F9-1726-4AA7-976C-1567A6B04399}&noticeno=20251226-1&dt=12/26/2025&icount=1&totcount=43&flag=0
severity: high
source: bse
stocks: []
tags:
- disaster-recovery
- trading-infrastructure
- connectivity
- technical-parameters
- equity
- derivatives
- currency
- commodity
- slb
- egr
- bolt-plus
- eti-api
- market-operations
title: Live Trading Session from Disaster Recovery (DR) Site – Equity, Equity Derivatives,
  SLB, Currency Derivatives, Commodity Derivatives, Electronic Gold Receipts Segment
---

## Summary

BSE has announced a live trading session from its Disaster Recovery (DR) site covering all segments: Equity, Equity Derivatives, SLB, Currency Derivatives, Commodity Derivatives, and Electronic Gold Receipts. Trading members must update their connection parameters to access the DR site through BOLT Plus trading system, either via BOLT TWS or third-party trading applications using ETI APIs.

## Key Points

- DR site trading session applies to all BSE segments: Equity, Equity Derivatives, SLB, Currency Derivatives, Commodity Derivatives, and EGR
- Trading members can connect via BOLT TWS or third-party applications through ETI APIs
- Connection parameters must be updated in configuration settings for successful DR site access
- Web-based systems (RTRMS, CLASS, EBOSS, etc.) accessible through updated URLs
- Both leased line and internet connectivity options available

## Technical Connection Parameters

### Commodity Derivatives Segment (ETI API)
- Primary DR: IP 10.255.241.26, Port 14910
- Secondary DR: IP 10.255.241.27, Port 14910

### BOLT TWS Users
- Configuration changes required in settings window
- Access via scrip profile icon or "Shift+F12" shortcut keys

### Web-Based Systems DR URLs

**RTRMS:**
- Internet: https://rtrms.bseindia.com
- Leased Line: http://10.1.101.197/stocks/jsp/rms/index.html or http://10.1.101.100/

**CLASS Collateral:**
- Internet: https://classseg.bseindia.com/application/applogin/login.aspx

**EBOSS:**
- Internet: https://eboss.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp
- Leased Line: https://ebossll.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp

**LEIPS:**
- Internet: https://leipsmm.bseindia.com/stocks/jsp/LEIPS/index.jsp
- Leased Line: https://leipsmmll.bseindia.com/stocks/jsp/LEIPS/index.jsp

**Extranet:**
- Internet: https://member.bseindia.com/Extranet_Login.aspx
- Leased Line: https://memberll.bseindia.com/

**Extranet Plus DR Settings:**
- Remote Server IP: 10.1.101.201
- Remote Server Port: 9001
- Special Request Port: 9000

**Online Trade File (OTD):**
- IP: 10.1.101.203, Port: 9011

**iBBS:**
- Internet: https://ibbs.bseindia.com/
- IP: 10.1.101.196, Port: 1000

## Compliance Requirements

- Trading members must update connection parameters in their trading systems before accessing DR site
- BOLT TWS users: Update technical connection parameters in configuration settings window
- Third-party application users: Modify ETI API connection parameters as specified
- Online Trade File users: Update setting.ini file with DR remote server IP and port settings
- Use existing user ID and password for web-based system access

## Important Dates

- Circular Date: December 26, 2025
- Immediate implementation for DR site connectivity

## Impact Assessment

### Operational Impact
- **High**: All trading members across all segments must update connectivity parameters
- Critical for business continuity and disaster recovery preparedness
- Affects trading through BOLT Plus, ETI APIs, and all web-based member systems
- Ensures seamless transition to DR site during primary site unavailability

### Market Impact
- **High**: Covers all trading segments - equity, derivatives, currency, commodity, SLB, and EGR
- Trading continuity depends on proper implementation of DR connectivity
- Failure to update parameters may result in inability to trade during DR site operations

### Technical Impact
- Requires configuration changes across multiple systems and applications
- Members using in-house developed systems must update ETI API parameters
- Web-based system users must use updated URLs for DR site access