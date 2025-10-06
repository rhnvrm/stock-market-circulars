---
category: market-operations
circular_id: 1659128615dba514
date: '2025-10-03'
description: NSE announces mock trading session on October 04, 2025 for Currency Derivatives
  segment with new NEAT version 3.5.4 release implementing new encryption mechanism
  and immediate order acknowledgement.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CD70605.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Mandatory mock trading session for Currency Derivatives members to
  test new NEAT 3.5.4 version with critical encryption updates. NEAT 3.5.3 will be
  discontinued on November 01, 2025, requiring member preparation and migration.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CD70605.pdf
processing:
  attempts: 1
  content_hash: 9d42a657ce446fac
  processed_at: '2025-10-06T06:36:50.866378'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-03T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CD70605.pdf
severity: medium
source: nse
stocks: []
tags:
- mock-trading
- currency-derivatives
- neat-upgrade
- system-testing
- encryption
- software-release
- disaster-recovery
- neat-adapter
title: Mock Trading Session - New NEAT Version 3.5.4 Release for Currency Derivatives
---

## Summary

NSE Currency Derivatives department has scheduled a mock trading session on Saturday, October 04, 2025 to test the new NEAT version 3.5.4. This release implements new encryption mechanism for interactive messages and immediate order acknowledgement as referenced in circular NSE/CD/70422 dated September 25, 2025. The mock session will test both primary site and disaster recovery (DR) site operations.

## Key Points

- New NEAT version 3.5.4 available from October 03, 2025 at 18:00 hrs
- Download path: /cdsftp/cdscommon/NEATCDS354 on NSE Extranet
- Mock trading includes primary site session (11:00-14:00) and DR site session (14:45-16:00)
- Contingency trading window: 12:00-13:30 on October 04, 2025
- Trade modification ends at 16:10, Live re-login available 18:00-18:30
- New NEAT Adapter Version 1.0.22 uses port 10879 (old version 1.0.20 uses port 10877)
- NEAT version 3.5.3 will be discontinued on November 01, 2025 (mock)
- All outstanding orders will be cleared before each session
- UCC validation will be skipped during contingency time for order entry

## Regulatory Changes

- Implementation of new encryption mechanism for interactive messages
- Introduction of immediate order acknowledgement feature
- Updated NEAT Adapter application (Version 1.0.22) with new port configuration (10879)
- Enhanced security protocols requiring version migration by November 01, 2025

## Compliance Requirements

- Members must download and install NEAT 3.5.4 from NSE Extranet
- Members using NNF software must manually clear orders in their systems
- Only valid and compliant UCC/PAN uploaded and approved before cutoff will be allowed
- Members must migrate from NEAT Adapter 1.0.20 to 1.0.22 per circular NSE/MSD/70421
- Members should refer to connectivity parameters in circular NSE/MSD/67674 dated April 24, 2025
- Members may use mock trading or simulated environment to meet SEBI regulatory requirements (SEBI/HO/MRD1/DSAP/CIR/P/2020/234)
- For UCC/PAN queries, contact uci@nse.co.in

## Important Dates

- **October 03, 2025, 18:00 hrs**: NEAT 3.5.4 version available for download
- **October 04, 2025, 11:00-14:00**: Mock trading session from primary site
  - Normal market open: 11:00
  - Contingency start: 12:00
  - Contingency close: 13:30
  - Normal market close: 14:00
- **October 04, 2025, 14:45-16:00**: Mock trading session from DR site
  - Session-2 open: 14:45
  - Session-2 close: 16:00
  - Trade modification end: 16:10
- **October 04, 2025, 18:00-18:30**: Live re-login window
- **November 01, 2025**: NEAT version 3.5.3 discontinuation date (mock)

## Impact Assessment

**Operational Impact**: Medium - Members must participate in mock trading to ensure readiness for new NEAT version deployment. The introduction of new encryption mechanism and immediate order acknowledgement requires system testing and validation. Members using older NEAT Adapter versions must upgrade to Version 1.0.22 and configure new port settings (10879).

**Technical Impact**: Members need to update their trading infrastructure, test connectivity with new ports, and ensure compatibility with the new encryption mechanism. The mandatory migration timeline (November 01, 2025 discontinuation of version 3.5.3) creates a clear deadline for members to complete testing and migration.

**Market Impact**: Low - This is a scheduled mock trading session with no financial obligations. No fund pay-in or pay-out will result from trades executed during the session. The session provides members opportunity to test disaster recovery procedures and contingency trading mechanisms.

**Member Action Required**: Immediate download and installation of NEAT 3.5.4, participation in mock trading session, testing of NEAT Adapter 1.0.22, and validation of connectivity through new port 10879.