---
category: market-operations
circular_id: c32f17f37a025d0e
date: '2025-12-11'
description: BSE announces mock trading session on Saturday, December 13, 2025 for
  Commodity Derivatives segment with disaster recovery site connectivity details.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={526AFB1E-FFA4-400A-BA70-80374D7A23BF}&noticeno=20251211-56&dt=12/11/2025&icount=56&totcount=90&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for disaster recovery testing with no
  impact on regular trading operations
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251211-56&attachedId=c48e9277-522f-4e56-96ba-b6a861d2ff6d
processing:
  attempts: 1
  content_hash: 555b7b7da4107ac4
  processed_at: '2025-12-11T18:53:49.494565'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-11T14:04:25+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={526AFB1E-FFA4-400A-BA70-80374D7A23BF}&noticeno=20251211-56&dt=12/11/2025&icount=56&totcount=90&flag=0
severity: low
source: bse
stocks: []
tags:
- mock-trading
- commodity-derivatives
- disaster-recovery
- trading-systems
- bolt-plus
- business-continuity
title: Mock Trading on Saturday, December 13, 2025 for Commodity Derivatives Segment
---

## Summary

BSE has scheduled a mock trading session on Saturday, December 13, 2025 for the Commodity Derivatives segment. This session will be conducted from the Disaster Recovery (DR) site to test business continuity systems. Trading members can connect using BOLT TWS, third-party trading applications, or in-house developed systems through ETI APIs.

## Key Points

- Mock trading session scheduled for Saturday, December 13, 2025
- Session will operate from BSE's Disaster Recovery (DR) site
- Applies to Commodity Derivatives segment only
- Trading members must update technical connection parameters to connect to DR site
- Multiple connectivity options available: BOLT TWS, third-party applications via ETI APIs
- Web-based systems (RTRMS, CLASS, Extranet, EBOSS, LEIPS) accessible through DR site URLs

## Technical Connection Details

**BOLT TWS Users:**
- Change technical connection parameters in configuration settings window at login
- Access configuration via scrip profile icon or Shift+F12 shortcut keys

**Third-Party Applications via ETI APIs:**
- Primary DR IP: 10.255.241.26, Port: 14910
- Secondary DR IP: 10.255.241.27, Port: 14910

**Web-Based Systems DR Connectivity:**
- RTRMS: Leased Line - http://10.1.101.197/stocks/jsp/rms/index.html
- RTRMS: Internet - http://10.1.101.100/
- CLASS Collateral: https://classseg.bseindia.com/application/applogin/login.aspx
- EBOSS: https://ebossll.bseindia.com/stocks/jsp/SURVEILLANCE/index.jsp
- LEIPS: https://leipsmmll.bseindia.com/stocks/jsp/LEIPS/index.jsp
- Extranet: https://memberll.bseindia.com/
- Online Trade File - Remote Server IP: 10.1.101.201, Port: 9001

## Compliance Requirements

- Trading members must configure their systems with DR site connection parameters before the mock session
- Members using BOLT TWS need to update configuration settings
- Members using third-party or in-house applications must update ETI API connection parameters
- Existing user IDs and passwords will be used for web-based systems

## Important Dates

- **Mock Trading Session Date:** Saturday, December 13, 2025
- No specific timings mentioned in the circular

## Impact Assessment

**Operational Impact:** Minimal - This is a routine disaster recovery test with no impact on regular weekday trading operations.

**Member Impact:** Low - Trading members need to temporarily reconfigure connection parameters for the mock session only. No changes to regular production systems required.

**Purpose:** Business continuity testing to ensure DR site readiness and member connectivity in case of primary site failure.