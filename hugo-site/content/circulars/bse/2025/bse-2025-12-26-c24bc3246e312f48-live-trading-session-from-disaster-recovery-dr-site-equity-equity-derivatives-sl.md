---
category: market-operations
circular_id: c24bc3246e312f48
date: '2025-12-26'
description: BSE notification regarding live trading session operations from Disaster
  Recovery site with connection parameters for BOLT Plus trading system and web-based
  systems.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={20B980F9-1726-4AA7-976C-1567A6B04399}&noticeno=20251226-1&dt=12/26/2025&icount=1&totcount=23&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Critical infrastructure change affecting all trading members across
  multiple segments requiring immediate technical reconfiguration to connect to DR
  site
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251226-1&attachedId=9b59dfbb-9520-412a-aa1a-242d868beb9e
processing:
  attempts: 1
  content_hash: b339ab60a506b413
  processed_at: '2025-12-26T12:53:10.075010'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-26T02:30:13+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={20B980F9-1726-4AA7-976C-1567A6B04399}&noticeno=20251226-1&dt=12/26/2025&icount=1&totcount=23&flag=0
severity: high
source: bse
stocks: []
tags:
- disaster-recovery
- dr-site
- bolt-plus
- trading-system
- connectivity
- equity
- derivatives
- commodity
- currency
- slb
- egr
- technical-configuration
title: Live Trading Session from Disaster Recovery (DR) Site – Equity, Equity Derivatives,
  SLB, Currency Derivatives, Commodity Derivatives, Electronic Gold Receipts Segment
---

## Summary

BSE is conducting live trading sessions from its Disaster Recovery (DR) site for all major segments including Equity, Equity Derivatives, SLB, Currency Derivatives, Commodity Derivatives, and Electronic Gold Receipts. Trading members must update their connection parameters to connect to the DR site using BOLT Plus trading system and other web-based platforms. The circular provides detailed technical connection parameters for both BOLT TWS users and third-party trading applications.

## Key Points

- Live trading will operate from BSE's Disaster Recovery site across all major trading segments
- Trading members must reconfigure connection parameters for BOLT Plus and web-based systems
- BOLT TWS users need to change technical parameters in configuration settings using scrip profile icon or Shift+F12
- Third-party trading applications using ETI APIs must update to DR IP addresses and ports
- Primary DR connection: IP 10.255.241.26, Port 14910; Secondary DR: IP 10.255.241.27, Port 14910
- Web-based systems like RTRMS, CLASS collateral, Extranet accessible through provided DR URLs
- Existing user IDs and passwords remain valid for web-based system access

## Technical Configuration Details

### BOLT Plus Trading System - Commodity Derivatives

**For BOLT TWS Users:**
- Access configuration settings window using scrip profile icon or Shift+F12 shortcut
- Update technical connection parameters at login

**For 3rd Party Trading Applications (ETI APIs):**
- Primary DR: IP 10.255.241.26, Port 14910
- Secondary DR: IP 10.255.241.27, Port 14910

### Web-Based Systems DR Connection Parameters

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

**Extranet:**
- Internet: https://member.bseindia.com/Extranet_Login.aspx
- Leased Line: https://memberll.bseindia.com/

**Extranet Plus DR Settings:**
- Remote Server IP: 10.1.101.201
- Remote Server Port: 9001
- Special Request Port: 9000

**iBBS:**
- Internet: https://ibbs.bseindia.com/
- Leased Line: IP 10.1.101.196, Port 1000

**Online Trade File (OTD):**
- IP: 10.1.101.203, Port 9011
- Alternative: IP 103.47.196.143, Port 8080

## Compliance Requirements

- All trading members must immediately update connection parameters in their trading systems to connect to DR site
- Members using BOLT TWS must modify configuration settings before login
- Members using third-party trading applications must update ETI API connection parameters
- Online trade file application users must change remote server IP and port settings in setting.ini file
- Existing authentication credentials (user IDs and passwords) should be used without changes

## Important Dates

- Effective Date: December 26, 2025 (immediate implementation)

## Impact Assessment

**Market Impact:**
- All trading segments affected: Equity, Equity Derivatives, SLB, Currency Derivatives, Commodity Derivatives, and Electronic Gold Receipts
- Continuous market operations maintained through DR site infrastructure
- No interruption to trading activities expected if members configure systems correctly

**Operational Impact:**
- Critical requirement for all trading members to reconfigure systems immediately
- Technical teams must update connection parameters across multiple platforms
- Failure to update parameters will result in inability to connect and trade
- Members using multiple connectivity methods (TWS, ETI APIs, web-based) need comprehensive updates
- System administrators must update setting.ini files for automated trading applications

**Technical Impact:**
- Infrastructure shift from primary to disaster recovery site
- Network connectivity changes for both leased line and internet users
- Multiple IP addresses and ports require updating across different applications
- Critical for business continuity and system resilience testing