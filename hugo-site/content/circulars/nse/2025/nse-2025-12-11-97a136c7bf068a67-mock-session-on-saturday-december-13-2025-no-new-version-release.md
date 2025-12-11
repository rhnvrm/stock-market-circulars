---
category: market-operations
circular_id: 97a136c7bf068a67
date: '2025-12-11'
description: NSE announces mock trading session for Commodity Derivatives segment
  on December 13, 2025 to test new encryption mechanism for interactive messages and
  immediate order acknowledgement.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/COM71770.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Important for members to test new encryption mechanism before December
  15, 2025 implementation. Mandatory participation evidence required for algorithmic
  trading compliance.
pdf_url: https://nsearchives.nseindia.com/content/circulars/COM71770.pdf
processing:
  attempts: 1
  content_hash: d32a41151c1cbf00
  processed_at: '2025-12-11T19:11:46.953924'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-11T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/COM71770.pdf
severity: medium
source: nse
stocks: []
tags:
- algo-trading
- derivatives
- encryption
- mock-trading
- retail-investor
- trading-platform
title: Mock Session on Saturday, December 13, 2025 - No New Version Release
---

## Summary

NSE will conduct a mock trading session in the Commodity Derivatives segment on Saturday, December 13, 2025. This session is intended to test the new encryption mechanism for interactive messages and immediate order acknowledgement that will be effective from December 15, 2025. Members must participate and provide evidence of participation for compliance with SEBI's algorithmic trading requirements.

## Key Points

- Mock session scheduled for December 13, 2025
- Testing new encryption mechanism referenced in circular NSE/COM/71599 dated December 02, 2025
- Functional changes in trading platform effective from December 15, 2025
- Two trading sessions planned: Session-1 from Primary Site (12:00-13:45) and Session-2 from DR Site (14:45-15:30)
- NEAT version 1.5.3 to be used for the mock session
- New NEAT Adapter versions available: 1.0.23 for Windows and Linux (Port 10859)
- Old NEAT Adapter versions 1.0.20 will use Port 10857
- Members required to test algorithmic trading functionality for retail investors
- Evidence of participation must be submitted to NNFREG@nse.co.in

## Regulatory Changes

- New encryption mechanism for interactive messages and immediate order acknowledgement becoming effective December 15, 2025
- Implementation of SEBI requirements for safer participation of retail investors in algorithmic trading per SEBI circular SEBI/HO/MIRSD/MIRSD-PoD/P/CIR/2025/132 dated September 30, 2025
- Members must provide evidence of participation in mock or simulation sessions

## Compliance Requirements

**For All Members:**
- Participate in mock trading session on December 13, 2025
- Download and use NEAT version 1.5.3 from path /comtftp/comtcommon/NEATCO153
- Update to new NEAT Adapter version 1.0.23 if required

**For Algorithmic Trading:**
- Test functionality related to safer participation of retail investors in algorithmic trading
- Submit evidence of participation via email to NNFREG@nse.co.in with following details:
  - Trading Member Name
  - Trading Member code
  - User ID
  - Participation in session (Mock/simulation environment)
  - Date(s) of participation
  - Segment

**Reference Circulars:**
- SEBI/HO/MIRSD/MIRSD-PoD/P/CIR/2025/0000013 dated February 4, 2025
- NSE/INVG/67858 dated May 05, 2025 (Implementation standards)
- NSE/INVG/69255 dated July 22, 2025 (Operational modalities)
- NSE/INVG/69289 dated July 24, 2025 (Corrigendum)
- NSE/INVG/70309 dated September 19, 2025 (Corrigendum)
- NSE/MSD/71601 dated December 02, 2025 (NEAT Adapter)
- NSE/MSD/67731 dated April 28, 2025 (Simulated trading sessions)

## Important Dates

- **December 13, 2025**: Mock trading session
  - Trading Session-1: 12:00 - 13:45 (Primary Site)
  - Trading Session-2: 14:45 - 15:30 (DR Site)
  - Position Limit/Collateral setup cutoff: 15:40
  - Trade Modification end: 15:50
  - Live Re-login window: 16:30 - 17:00
- **December 15, 2025**: New encryption mechanism becomes effective

## Impact Assessment

**Operational Impact:**
- Members must allocate resources for mock session participation on Saturday
- IT teams need to update NEAT trading platform to version 1.5.3
- Members using NEAT Adapter must upgrade to version 1.0.23 and configure new port 10859
- Trading operations will be affected if members fail to test and prepare for new encryption mechanism

**Compliance Impact:**
- Mandatory evidence submission for algorithmic trading participants creates additional compliance burden
- Members must demonstrate readiness for SEBI's retail investor protection framework in algorithmic trading
- Non-participation may affect ability to operate algorithmic trading services for retail clients

**Technical Impact:**
- Two-day window between mock session and live implementation requires quick resolution of any issues identified
- Members using old NEAT Adapter can continue on different port, providing transition flexibility
- Dual trading sessions (Primary and DR sites) allow comprehensive disaster recovery testing