---
category: market-operations
circular_id: 9689d7fe4a23ae21
date: '2026-01-02'
description: NSE announces mock trading session for Currency Derivatives segment on
  January 03, 2026 with no new version release, using NEAT 3.5.4 and new encryption
  mechanism.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CD72133.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for testing purposes with no financial
  obligations or market impact
pdf_url: https://nsearchives.nseindia.com/content/circulars/CD72133.pdf
processing:
  attempts: 1
  content_hash: b7c3b08f66724ea5
  processed_at: '2026-01-02T12:54:48.262346'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-02T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CD72133.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- currency-derivatives
- testing
- neat-adapter
- encryption
- disaster-recovery
title: Mock Trading Session for Currency Derivatives Segment - January 03, 2026
---

## Summary

NSE will conduct a mock trading session for the Currency Derivatives segment on Saturday, January 03, 2026. The session will test the new encryption mechanism for interactive messages and immediate order acknowledgement using NEAT version 3.5.4. No new version will be released. The mock session includes two trading sessions from primary and DR sites, with specific timings for trading, contingency operations, and re-login periods.

## Key Points

- Mock trading scheduled for January 03, 2026 in Currency Derivatives segment
- NEAT version 3.5.4 to be used (no new version release)
- Two trading sessions: Session-1 from Primary Site (11:00-14:00) and Session-2 from DR Site (14:45-15:30)
- Contingency operations scheduled from 12:00-13:30
- Live re-login window from 17:00-18:00
- New NEAT Adapter version 1.0.23 required for port connectivity
- All outstanding orders will be cleared before each session
- No financial obligations - trades will not result in fund pay-in or pay-out
- NOTIS application accessible from 11:15 AM to 12:30 PM and 2:45 PM till market close
- UCC validation will be skipped during contingency time for order entry

## Regulatory Changes

No regulatory changes introduced. This circular implements previously announced changes:
- New encryption mechanism for interactive messages (reference: NSE/CD/70422 dated September 25, 2025)
- Immediate order acknowledgement update (reference: circular 71999 dated December 24, 2025)
- NEAT Adapter version updates (references: NSE/MSD/70421 and NSE/MSD/71601)

## Compliance Requirements

- Members must use NEAT version 3.5.4 available at /cdsftp/cdscommon/NEATCDS354
- Members must use appropriate NEAT Adapter version (1.0.23 recommended for new application)
- Port selection based on adapter version: Old versions use ports 10877/10879, new version 1.0.23 uses standard ports
- Members using NNF software must manually clear orders in their systems
- Only valid and compliant UCC/PAN uploaded and approved before cutoff will be allowed
- Members may use mock trading session to meet SEBI regulatory requirements per SEBI/HO/MRD1/DSAP/CIR/P/2020/234

## Important Dates

- **January 03, 2026**: Mock trading session
  - 11:00: Trading Session-1 starts (Primary Site)
  - 12:00: Contingency operations start
  - 13:30: Contingency operations close
  - 14:00: Trading Session-1 closes
  - 14:45: Trading Session-2 starts (DR Site)
  - 15:30: Trading Session-2 closes
  - 15:40: Trade modification end time
  - 17:00-18:00: Live re-login window

## Impact Assessment

**Market Impact**: None. This is a testing session with no financial obligations.

**Operational Impact**: Low. Members need to participate in mock session to test connectivity and ensure readiness for the new encryption mechanism and NEAT Adapter versions. This provides opportunity to test disaster recovery site switchover procedures.

**Member Requirements**: Members should ensure proper NEAT version installation, appropriate NEAT Adapter version deployment, and test connectivity parameters. Optional participation for testing software as per SEBI requirements.