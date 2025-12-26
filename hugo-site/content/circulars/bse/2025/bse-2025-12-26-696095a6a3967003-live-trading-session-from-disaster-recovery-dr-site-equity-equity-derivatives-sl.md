---
category: market-operations
circular_id: 696095a6a3967003
date: '2025-12-26'
description: BSE announces live trading session from Disaster Recovery (DR) site with
  detailed connection parameters and technical specifications for all trading segments
  including BOLT Plus, ETI APIs, and web-based systems.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={20B980F9-1726-4AA7-976C-1567A6B04399}&noticeno=20251226-1&dt=12/26/2025&icount=1&totcount=45&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Critical infrastructure notice affecting all trading members across
  multiple segments requiring immediate technical configuration changes to connect
  to DR site
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251226-1&attachedId=9b59dfbb-9520-412a-aa1a-242d868beb9e
processing:
  attempts: 1
  content_hash: 8129fa485dba893a
  processed_at: '2025-12-26T18:54:15.761569'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-26T02:30:13+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={20B980F9-1726-4AA7-976C-1567A6B04399}&noticeno=20251226-1&dt=12/26/2025&icount=1&totcount=45&flag=0
severity: high
source: bse
stocks: []
tags:
- disaster-recovery
- trading-system
- bolt-plus
- commodity-derivatives
- equity-derivatives
- slb
- currency-derivatives
- egr
- technical-connectivity
- dr-site
- eti-api
- rtrms
- market-operations
title: Live Trading Session from Disaster Recovery (DR) Site – Equity, Equity Derivatives,
  SLB, Currency Derivatives, Commodity Derivatives, Electronic Gold Receipts Segment
---

## Summary

BSE has issued technical specifications for connecting to the Disaster Recovery (DR) site for live trading sessions across all segments including Equity, Equity Derivatives, SLB, Currency Derivatives, Commodity Derivatives, and Electronic Gold Receipts. Trading members must update their connection parameters for BOLT Plus TWS, third-party trading applications using ETI APIs, and web-based systems like RTRMS, CLASS collateral, and Extranet.

## Key Points

- Trading members can connect to DR site using BOLT TWS or third-party trading applications through ETI APIs
- Configuration changes required in technical connection parameters at login
- Primary DR IP: 10.255.241.26; Port: 14910 for ETI connections
- Secondary DR IP: 10.255.241.27; Port: 14910 for ETI connections
- DR site supports all trading segments: Equity, Equity Derivatives, SLB, Currency Derivatives, Commodity Derivatives, and EGR
- Web-based systems accessible through specific URLs for leased line and internet connections
- Existing user IDs and passwords remain valid for DR site access

## Technical Connection Parameters

### BOLT TWS Users
- Change technical connection parameters in configuration settings window at login
- Access configuration using scrip profile icon or "Shift+F12" shortcut keys

### ETI API Users (3rd Party Trading Applications)
- Primary DR: IP 10.255.241.26, Port 14910
- Secondary DR: IP 10.255.241.27, Port 14910

### Web-Based Systems DR URLs

**RTRMS:**
- Internet: https://rtrms.bseindia.com
- Leased Line: http://10.1.101.197/stocks/jsp/rms/index.html or http://10.1.101.100/

**Collateral & Early Pay In (CLASS):**
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

**Extranet Plus (Client Setting.ini):**
- REMOTE SERVER IP: 10.1.101.201
- REMOTE SERVER PORT: 9001
- SPECIAL REQUEST PORT: 9000

**iBBS:**
- Internet: https://ibbs.bseindia.com/
- Leased Line: IP 10.1.101.196, Port 1000

**Online Trade File (OTD):**
- IP: 10.1.101.203, Port 9011
- Alternative: IP 103.47.196.143, Port 8080

## Compliance Requirements

- Trading members must update connection parameters in their trading systems before connecting to DR site
- Members using BOLT TWS must modify configuration settings at login
- Members using third-party applications must update ETI API connection parameters
- Members using online trade file application must change remote server IP and port settings in setting.ini file
- Use existing user IDs and passwords for authentication

## Important Dates

- Effective immediately for DR site connectivity

## Impact Assessment

This circular has high operational impact as it affects all trading members across all BSE segments. The DR site activation is critical for business continuity and disaster recovery preparedness. Members must ensure their technical teams are aware of the connection parameters to maintain uninterrupted trading capabilities. Failure to configure systems correctly could result in inability to trade during DR site operations. The circular provides comprehensive technical specifications for multiple connectivity methods ensuring all member types can connect appropriately.