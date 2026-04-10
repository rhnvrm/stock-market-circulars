---
category: market-operations
circular_id: ed1ab49a01e79adf
date: '2026-04-10'
description: NSE will conduct a mock trading session in the Commodity Derivatives
  segment on Saturday, April 11, 2026. No new version release; NEAT version 1.5.5
  is mandatory.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/COM73691.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for commodity derivatives members; no
  regulatory changes or market-wide impact. Relevant only to members participating
  in connectivity testing.
pdf_url: https://nsearchives.nseindia.com/content/circulars/COM73691.pdf
processing:
  attempts: 1
  content_hash: 7c11eed3e128642c
  processed_at: '2026-04-10T10:12:23.321341'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-04-10T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/COM73691.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- commodity-derivatives
- neat
- trading-session
- disaster-recovery
- market-operations
title: Mock Session on Saturday, April 11, 2026 - Commodity Derivatives Segment
---

## Summary

NSE will conduct a mock trading session in the Commodity Derivatives segment on Saturday, April 11, 2026. The session involves two trading sessions — one from the Primary Site and one from the DR (Disaster Recovery) Site. There is no new software version release; members must use NEAT version 1.5.5 (mandatory).

## Key Points

- Mock trading date: Saturday, April 11, 2026
- Segment: Commodity Derivatives
- No new NEAT version release; mandatory version is 1.5.5
- Download path: `/comtftp/comtcommon/NEATCO155`
- Two trading sessions: Session-1 from Primary Site and Session-2 from DR Site
- Old NEAT Adapter (v1.0.20) uses GR PORT 10857; New NEAT Adapter (v1.0.27) uses GR PORT 10859
- All outstanding orders will be purged before each session
- No financial obligations arise from mock session trades
- Members should re-login to the live environment after mock to ensure smooth connectivity for Monday, April 13, 2026

## Regulatory Changes

No regulatory changes. This circular is a continuation of circular (download no. 71999) dated December 24, 2025, governing periodic mock trading sessions.

## Compliance Requirements

- Members must use NEAT version 1.5.5 (mandatory)
- Members using NNF software must manually clear orders in their systems before each session
- Only valid and compliant UCC/PAN uploaded and approved before cutoff will be allowed during the mock session
- UCC validation will be skipped during contingency time for order entry
- Members should participate using all trading software and re-login to the live environment post-mock
- For NEAT Adapter details, refer to circular NSE/MSD/73674 dated April 09, 2025

## Important Dates

- Mock session date: April 11, 2026 (Saturday)
- Trading Session-1 (Primary Site): Normal Market open 10:00, Contingency Start 12:00, Contingency End 13:30, Normal Market close 14:00
- Trading Session-2 (DR Site): Normal Market open 14:45, Normal Market close 15:30
- Position Limit/Collateral value setup cutoff: 15:40
- Trade Modification end time: 15:40
- Live Re-login: 17:00–18:00
- Connect2NSE and Extranet not available: 12:30–17:30 and 18:00–21:30
- Extranet API not available: 12:30–14:00 and 17:30–18:30
- Live trading resumes: Monday, April 13, 2026

## Impact Assessment

Minimal market impact. This is a routine operational mock session for Commodity Derivatives segment members to test connectivity, software, and disaster recovery switchover procedures. No fund pay-in or pay-out will result from trades during the mock session. Members should ensure they complete re-login to the live environment before Monday, April 13, 2026 to avoid any disruption to live trading.