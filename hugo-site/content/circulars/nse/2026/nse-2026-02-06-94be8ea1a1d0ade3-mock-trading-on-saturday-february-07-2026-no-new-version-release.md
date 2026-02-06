---
category: market-operations
circular_id: 94be8ea1a1d0ade3
date: '2026-02-06'
description: NSE will conduct a mock trading session in the Currency Derivatives Segment
  on February 07, 2026, with two trading sessions from Primary Site and DR Site.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CD72660.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for testing purposes with no financial
  obligations or operational changes. No new version release required.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CD72660.pdf
processing:
  attempts: 1
  content_hash: 1ffa5f2b9d7fc2d2
  processed_at: '2026-02-06T06:56:58.705450'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-02-06T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CD72660.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- currency-derivatives
- testing
- neat-version-3.5.4
- disaster-recovery
- adapter-version
- ucc-validation
title: Mock Trading on Saturday, February 07, 2026 - No New Version Release
---

## Summary

NSE will conduct a mock trading session in the Currency Derivatives Segment on Saturday, February 07, 2026. The session will include two trading sessions - one from the Primary Site (11:00 to 14:00) and another from the DR Site (14:45 to 15:30). Members will use existing NEAT version 3.5.4 with no new version release. Trades during the mock session will not result in any financial obligations.

## Key Points

- Mock trading date: February 07, 2026
- Trading Session-1 from Primary Site: 11:00 to 14:00 (including contingency testing from 12:00 to 13:30)
- Trading Session-2 from DR Site: 14:45 to 15:30
- Trade modification end time: 15:40
- Live re-login window: 17:00 to 18:00
- NEAT version to be used: 3.5.4 (available at /cdsftp/cdscommon/NEATCDS354)
- NEAT Adapter versions supported: 1.0.20, 1.0.22, and 1.0.23 for both Windows and Linux
- Applicable GR ports: 10877 (old adapters), 10879 (new adapter version 1.0.23)
- All outstanding orders will be purged before each session
- UCC validation will be skipped during contingency time for order entry
- NOTIS application will be accessible during the mock session

## Regulatory Changes

No regulatory changes introduced. This is a routine mock trading session for testing purposes.

## Compliance Requirements

- Members must participate in the mock trading session using all their trading software
- Members must re-login into live environment to ensure smooth connectivity
- Only valid and compliant UCC/PAN uploaded and approved before cutoff will be allowed (except during contingency time)
- Members using NNF software must manually clear orders in their systems
- Members may use either Mock Trading or Simulated Environment to meet SEBI regulatory requirements per circular SEBI/HO/MRD1/DSAP/CIR/P/2020/234
- For UCC/PAN queries, contact uci@nse.co.in

## Important Dates

- **February 07, 2026**: Mock trading session
  - Trading Session-1 (Primary Site): 11:00 - 14:00
  - Contingency testing: 12:00 - 13:30
  - Trading Session-2 (DR Site): 14:45 - 15:30
  - Trade modification end: 15:40
  - Live re-login: 17:00 - 18:00

## Impact Assessment

**Market Impact**: None. This is a mock trading session with no real financial transactions.

**Operational Impact**: Low. Members need to allocate resources for testing on Saturday. Connect2NSE and Extranet facility will be unavailable from 12:00 PM until end of mock session. Extranet API will be unavailable from 12:00 PM to 01:00 PM.

**Member Requirements**: Members must test their trading infrastructure, including connectivity to both Primary and DR sites, and ensure their systems can handle the switchover between sites. This is an opportunity to validate disaster recovery procedures and adapter configurations without financial risk.