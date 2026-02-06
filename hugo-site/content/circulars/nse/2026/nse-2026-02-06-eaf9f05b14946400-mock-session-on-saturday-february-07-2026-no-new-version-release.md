---
category: market-operations
circular_id: eaf9f05b14946400
date: '2026-02-06'
description: NSE will conduct a mock trading session in the Commodity Derivatives
  segment on February 07, 2026, with NEAT version 1.5.3 discontinuation and testing
  of version 1.5.4.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/COM72666.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Routine mock trading session for system testing and version transition,
  important for member preparedness but no direct market impact
pdf_url: https://nsearchives.nseindia.com/content/circulars/COM72666.pdf
processing:
  attempts: 1
  content_hash: 6e297af1b07a1200
  processed_at: '2026-02-06T06:57:28.019457'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-02-06T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/COM72666.pdf
severity: medium
source: nse
stocks: []
tags:
- mock-trading
- commodity-derivatives
- neat-version-update
- system-testing
- dr-site-testing
title: Mock Trading Session on Saturday, February 07, 2026 - No New Version Release
---

## Summary

NSE will conduct a mock trading session in the Commodity Derivatives segment on Saturday, February 07, 2026. The session will test NEAT version 1.5.4 and discontinue version 1.5.3. Two trading sessions will be conducted - one from the Primary Site (11:00-14:00) and one from the DR Site (14:45-15:30), including contingency procedures and member re-login testing.

## Key Points

- Mock trading session scheduled for February 07, 2026 in Commodity Derivatives segment
- NEAT version 1.5.3 will be discontinued after this mock session
- NEAT version 1.5.4 to be used going forward (download path: /comtftp/comtcommon/NEATCO154)
- Trading Session-1 from Primary Site: 11:00 to 14:00 (includes contingency testing 12:00-13:30)
- Trading Session-2 from DR Site: 14:45 to 15:30
- New NEAT Adapter versions required: 1.0.23 for Windows and Linux (using port 10859)
- Old NEAT Adapter version 1.0.20 will use port 10857
- Connect2NSE and Extranet facility unavailable from 12:00 PM till end of mock session
- Extranet API unavailable from 12:00 PM to 01:00 PM
- Live re-login window: 17:00 to 18:00
- No financial obligations from mock trading
- All outstanding orders will be cleared before each session

## Regulatory Changes

NEAT version 1.5.3 will be discontinued effective February 07, 2026 (mock session date). Members must transition to NEAT version 1.5.4.

NEAT Adapter application updated to version 1.0.23 for both Windows and Linux platforms, with new port assignment (10859) as per circular NSE/MSD/71601 dated December 02, 2025.

## Compliance Requirements

- Members must download and install NEAT version 1.5.4 from /comtftp/comtcommon/NEATCO154
- Members must upgrade to NEAT Adapter version 1.0.23 and use port 10859
- Members must participate using all trading software to ensure connectivity
- Members must perform re-login into live environment after mock session
- Only valid and compliant UCC/PAN uploaded and approved before cutoff will be allowed
- Members using NNF software must manually clear orders in their systems
- Members should refer to connectivity parameters in circulars NSE/MSD/67674 (April 24, 2025) and NSE/COM/71599 (December 2, 2025)
- UCC validation will be skipped during contingency time for order entry

## Important Dates

- **February 06, 2026**: Circular issue date
- **February 07, 2026**: Mock trading session date
  - 11:00: Trading Session-1 start (Primary Site)
  - 12:00: Contingency start time
  - 13:30: Contingency end time
  - 14:00: Trading Session-1 close
  - 14:45: Trading Session-2 start (DR Site)
  - 15:30: Trading Session-2 close
  - 15:40: Position Limit/Collateral value setup cutoff and Trade Modification end time
  - 17:00: Live re-login start time
  - 18:00: Live re-login close time
- **February 07, 2026**: NEAT version 1.5.3 discontinuation date

## Impact Assessment

**Operational Impact**: Medium - Members must prepare systems for mock trading and ensure NEAT version upgrade. Testing of both primary and DR site operations requires member participation and system readiness.

**Technical Impact**: Members need to upgrade NEAT software to version 1.5.4 and NEAT Adapter to version 1.0.23, configure new port settings (10859), and test connectivity during the mock session.

**Member Preparedness**: Mock session provides opportunity to test disaster recovery procedures, contingency operations, and new software versions before live implementation. Members must allocate resources for Saturday testing.

**Service Disruption**: Connect2NSE and Extranet services will be unavailable during portions of the mock session (12:00 PM onwards), with Extranet API specifically unavailable from 12:00 PM to 01:00 PM.

**Financial Impact**: None - trades during mock session will not result in any fund pay-in or pay-out obligations.