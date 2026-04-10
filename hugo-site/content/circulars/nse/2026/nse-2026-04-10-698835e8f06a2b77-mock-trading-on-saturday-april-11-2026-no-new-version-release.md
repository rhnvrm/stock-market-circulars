---
category: market-operations
circular_id: 698835e8f06a2b77
date: '2026-04-10'
description: NSE will conduct a mock trading session in the Futures & Options segment
  on Saturday, April 11, 2026, with no new version release. Functional changes for
  new encryption mechanism will be effective from April 13, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP73687.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session notification for F&O segment members;
  no new software version, no regulatory change, and no financial obligations arise
  from mock trades.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP73687.pdf
processing:
  attempts: 1
  content_hash: 5edff9a8062877d9
  processed_at: '2026-04-10T10:13:29.936028'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-04-10T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP73687.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- futures-options
- neat-plus
- trading-system
- bcp-site
- encryption
- neat-adapter
- market-operations
title: Mock Trading Session - Futures & Options Segment - April 11, 2026
---

## Summary

NSE is conducting a mock trading session in the Futures & Options (F&O) segment on Saturday, April 11, 2026. There is no new version release for this mock session. The circular references the upcoming new encryption mechanism for Interactive Messages and Immediate Order Acknowledgement, whose functional changes will go live on April 13, 2026. Members are required to use NEAT+ version 7.8.7 and the appropriate NEAT Adapter version and port combination.

## Key Points

- Mock trading session for F&O segment scheduled on Saturday, April 11, 2026
- No new version release for this mock session
- New encryption mechanism changes (per circular NSE/FAOP/72763 dated February 12, 2026) will be effective from April 13, 2026
- Two trading sessions: Session 1 from Primary Site, Session 2 from BCP Site
- NEAT+ version in use: 7.8.7 (path: `/faoftp/faocommon/NEATPlus787`)
- Old NEAT Adapter (v1.0.20) uses GR PORT 10827; New NEAT Adapter (v1.0.27) uses GR PORT 10833
- All outstanding orders will be cleared before each session
- Trades in mock sessions carry no financial obligation (no fund pay-in or pay-out)
- Only valid and compliant UCC/PAN uploaded and approved before cutoff will be allowed

## Regulatory Changes

No new regulatory changes are introduced by this circular. However, it references the upcoming enforcement of the new encryption mechanism for Interactive Messages and Immediate Order Acknowledgement (circular NSE/FAOP/72763 dated February 12, 2026), which becomes effective April 13, 2026.

## Compliance Requirements

- Members must use NEAT+ version 7.8.7 for the mock session
- Members must select the correct NEAT Adapter version and corresponding GR PORT (10827 for old adapter v1.0.20; 10833 for new adapter v1.0.27)
- Members using NNF software must manually clear outstanding orders before each session
- Members may use Mock Trading or Simulated Environment to meet SEBI regulatory requirements (per SEBI/HO/MRD1/DSAP/CIR/P/2020/234)
- Valid UCC/PAN must be uploaded and approved before the cutoff; queries to uci@nse.co.in

## Important Dates

- **April 11, 2026 (Saturday):** Mock trading session in F&O segment
  - Session 1 (Primary Site): Pre-Open opens 10:00, Normal Market 10:15–14:00
  - Session 2 (BCP Site): Pre-Open opens 14:45, Normal Market 15:00–16:00, Trade Modification ends 16:10
  - Live Re-login window: 17:00–18:00
- **April 13, 2026:** Functional changes for new encryption mechanism go live in production

## Impact Assessment

This circular has minimal market impact as it pertains to a routine Saturday mock trading session for F&O segment members. The mock session is intended to allow members to test connectivity and system readiness ahead of the April 13, 2026 encryption mechanism rollout. No new software is being released, and all mock trades carry zero financial obligation. Members should ensure they have the correct NEAT Adapter version installed and are using the appropriate GR PORT before the session.