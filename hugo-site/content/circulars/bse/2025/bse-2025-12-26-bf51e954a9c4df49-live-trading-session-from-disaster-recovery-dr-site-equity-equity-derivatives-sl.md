---
category: market-operations
circular_id: bf51e954a9c4df49
date: '2025-12-26'
description: BSE announces live trading session from Disaster Recovery site with detailed
  connectivity parameters for all trading segments including BOLT Plus system, web-based
  applications, and market data interfaces.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={20B980F9-1726-4AA7-976C-1567A6B04399}&noticeno=20251226-1&dt=12/26/2025&icount=1&totcount=2&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Critical operational circular requiring immediate action by all trading
  members to reconfigure systems for DR site connectivity across all segments
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251226-1&attachedId=9b59dfbb-9520-412a-aa1a-242d868beb9e
processing:
  attempts: 1
  content_hash: 021b765ba63b3c50
  processed_at: '2025-12-26T04:01:15.541698'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-26T02:30:13+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={20B980F9-1726-4AA7-976C-1567A6B04399}&noticeno=20251226-1&dt=12/26/2025&icount=1&totcount=2&flag=0
severity: high
source: bse
stocks: []
tags:
- disaster-recovery
- trading-connectivity
- bolt-plus
- eti-api
- market-data
- system-migration
- technical-parameters
- rtrms
- equity
- derivatives
- commodity
- currency
- slb
- egr
title: Live Trading Session from Disaster Recovery (DR) Site – Equity, Equity Derivatives,
  SLB, Currency Derivatives, Commodity Derivatives, Electronic Gold Receipts Segment
---

## Summary

BSE has initiated a live trading session from its Disaster Recovery (DR) site for all trading segments including Equity, Equity Derivatives, SLB, Currency Derivatives, Commodity Derivatives, and Electronic Gold Receipts. Trading members must update their technical connection parameters to connect to the DR site infrastructure. The circular provides comprehensive connectivity details for BOLT Plus trading system, web-based applications (RTRMS, CLASS, EBOSS, etc.), and market data interfaces.

## Key Points

- Live trading from DR site activated for all BSE segments
- Trading members must update connection parameters in BOLT TWS or third-party trading applications
- DR connectivity available for both BOLT TWS users and ETI API users
- Web-based systems (RTRMS, Collateral, Extranet, EBOSS, LEIPS) accessible through specific DR URLs
- Separate IP addresses and ports provided for leased line and internet connectivity
- Market data interfaces (MDI, NFCAST, EMDI) connection parameters updated for DR site
- Both interactive interfaces and market data streams affected

## Technical Configuration Changes

### BOLT Plus Trading System - Commodity Derivatives

**BOLT TWS Users:**
- Members must change technical connection parameters in configuration settings window
- Access settings via scrip profile icon or Shift+F12 shortcut keys

**ETI API Users (3rd party/in-house applications):**
- Primary DR: IP 10.255.241.26, Port 14910
- Secondary DR: IP 10.255.241.27, Port 14910

### Web-Based Systems Connectivity

**RTRMS:**
- Internet: https://rtrms.bseindia.com
- Leased Line: http://10.1.101.197/stocks/jsp/rms/index.html or http://10.1.101.100/

**CLASS Collateral & Early Pay In:**
- Internet: https://classseg.bseindia.com/application/applogin/login.aspx

**EBOSS:**
- Internet: https://eboss.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp
- Leased Line: https://ebossll.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp

**LEIPS:**
- Internet: https://leipsmm.bseindia.com/stocks/jsp/LEIPS/index.jsp
- Leased Line: https://leipsmmll.bseindia.com/stocks/jsp/LEIPS/index.jsp

**SME Market Making Compliance System:**
- https://mmcs.bsesme.com/stocks/jsp/sme/index.jsp

**Extranet:**
- Leased Line: https://memberll.bseindia.com/
- Internet: https://member.bseindia.com/Extranet_Login.aspx

**Extranet Plus DR Configuration:**
- REMOTE SERVER IP: 10.1.101.201
- REMOTE SERVER PORT: 9001
- SPECIAL REQUEST PORT: 9000
- DR Path: C://HYDBSESMELWEB.BSEAPPS.COM/BSEExtranet_Data_Files/FTPDIR/EQ/Transaction/

**iBBS:**
- Internet: https://ibbs.bseindia.com/
- Leased Line: http://10.1.101.196/index.aspx
- IP: 10.1.101.196, Port: 1000

**Online Trade File (OTD):**
- Members must update setting.ini file with DR parameters
- IP: 10.1.101.203, Port: 9011
- Alternative: IP 103.47.196.143, Port 8080

## Market Data Interfaces

The circular references BOLTPLUS Connectivity Manual Version 1.16 (dated October 6, 2025) which provides detailed information on:

**Low Bandwidth Interfaces:**
- BSE Market Data Interface (MDI)
- BSE Direct NFCAST

**High Bandwidth Interfaces:**
- BSE Enhanced Market Data Interface (EMDI)
- BSE Enhanced Order Book

**Interactive Interface:**
- BSE Enhanced Trading Interface (BSE ETI)

## Compliance Requirements

- Trading members must immediately reconfigure all trading systems with DR site parameters
- BOLT TWS users must update configuration settings before login
- Members using third-party or in-house trading applications must modify ETI API connection parameters
- Web-based system users must access applications through DR-specific URLs
- Online Trade File users must update setting.ini file with new remote server IP and port details
- All existing user IDs and passwords remain valid for DR site access

## Important Dates

- Circular Date: December 26, 2025
- Effective Immediately: Trading from DR site is live
- Connectivity Manual Version: 1.16 (October 6, 2025)

## Impact Assessment

**Operational Impact:** High - All trading members across all segments must reconfigure their systems to maintain trading operations. Failure to update connection parameters will result in inability to trade.

**Segments Affected:** Complete market coverage including Equity, Equity Derivatives, SLB, Currency Derivatives, Commodity Derivatives, and Electronic Gold Receipts.

**System Coverage:** Both primary trading systems (BOLT Plus, ETI APIs) and auxiliary systems (RTRMS, collateral management, surveillance, reporting) require reconfiguration.

**Member Action Required:** Immediate technical implementation by IT teams to update connection parameters across multiple systems and applications.

**Business Continuity:** This DR activation demonstrates BSE's disaster recovery preparedness and ensures uninterrupted market operations during primary site unavailability.