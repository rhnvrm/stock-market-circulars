---
category: market-operations
circular_id: 31b08812525d5fab
date: '2026-01-09'
description: NSE announces mock trading session in Commodity Derivatives segment on
  January 10, 2026 for testing new NEAT version 1.5.4 with enhanced encryption mechanism.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/COM72200.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Mandatory mock trading session for system upgrade affecting all commodity
  derivatives members; requires software update and active participation but no financial
  impact
pdf_url: https://nsearchives.nseindia.com/content/circulars/COM72200.pdf
processing:
  attempts: 1
  content_hash: e627e352d9fcafec
  processed_at: '2026-01-09T09:30:19.132321'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-09T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/COM72200.pdf
severity: medium
source: nse
stocks: []
tags:
- mock-trading
- neat-upgrade
- commodity-derivatives
- encryption
- system-testing
- dr-site
- neat-adapter
title: Mock session on Saturday, January 10, 2026 - New version of NEAT 1.5.4
---

## Summary

NSE will conduct a mock trading session in the Commodity Derivatives segment on Saturday, January 10, 2026 to test the new NEAT version 1.5.4. This upgrade implements enhanced encryption mechanism for interactive messages and immediate order acknowledgement. Members must download the new version available from January 09, 2026 at 18:00 hrs and participate in two trading sessions conducted from DR Site and Primary Site.

## Key Points

- Mock trading session scheduled for January 10, 2026 with two trading sessions
- Trading Session-1 from DR Site: 13:15 to 13:45
- Trading Session-2 from Primary Site: 15:00 to 16:45
- Orders and trades from Session 1 will not be available in Session 2
- New NEAT version 1.5.4 available for download from January 09, 2026, 18:00 hrs
- Download path: /comtftp/comtcommon/NEATCO154 on NSE Extranet
- NEAT Adapter updated to version 1.0.23 for both Windows and Linux
- New GR PORT: 10859 (Old port: 10857)
- Live re-login window: 19:00 to 19:30
- No financial obligations from mock trading transactions

## Regulatory Changes

New encryption mechanism for interactive messages and immediate order acknowledgement being implemented through NEAT 1.5.4, as referenced in circular NSE/COM/71599 dated December 02, 2025. This represents a security enhancement to the trading platform.

## Compliance Requirements

- Members must download and install NEAT version 1.5.4 before the mock session
- Members must update NEAT Adapter to version 1.0.23 (for Windows or Linux)
- Members must configure systems to use new GR PORT 10859
- Active participation required in all trading sessions
- Members using NNF software must manually clear orders in their systems between sessions
- Only valid and compliant UCC/PAN uploaded and approved before cutoff will be allowed
- Members should refer to circular NSE/MSD/46441 and SEBI circular SEBI/HO/MRD1/DSAP/CIR/P/2020/234 for software testing requirements

## Important Dates

- **January 09, 2026, 18:00 hrs**: NEAT 1.5.4 available for download
- **January 10, 2026**: Mock trading session
  - 13:15-13:45: Trading Session-1 from DR Site
  - 15:00-16:45: Trading Session-2 from Primary Site
  - 16:55: Position Limit/Collateral value setup cutoff and Trade Modification end time
  - 19:00-19:30: Live re-login window
- **February 07, 2026**: Discontinuation date for NEAT version 1.5.3

## Impact Assessment

**Market Impact**: No direct market impact as this is a mock session with no financial obligations. However, successful testing is critical for smooth transition to the new system.

**Operational Impact**: Medium - All commodity derivatives members must upgrade their systems and participate in testing. The upgrade involves:
- New NEAT version installation
- NEAT Adapter update to version 1.0.23
- Port configuration change (10857 to 10859)
- Testing across two separate trading sessions from different sites

**Technical Requirements**: Members need to ensure compatibility with new encryption mechanism and updated connectivity parameters. Members using custom NNF software must implement manual order clearing procedures.

**Benefits**: Enhanced security through improved encryption, immediate order acknowledgement functionality, and validated disaster recovery capabilities through DR site testing.