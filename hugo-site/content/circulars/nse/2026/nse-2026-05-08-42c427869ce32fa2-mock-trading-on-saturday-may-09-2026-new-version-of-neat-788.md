---
category: market-operations
circular_id: 42c427869ce32fa2
date: '2026-05-08'
description: NSE schedules a mock trading session in the Futures & Options segment
  on Saturday, May 09, 2026 to test the new NEAT+ version 7.8.8 with updated broadcast
  parameters. Members must upgrade from NEAT+ 7.8.7 before the June 06, 2026 discontinuation
  date.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP74134.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational circular requiring F&O segment members to upgrade trading
  software (NEAT+ 7.8.8) and participate in mock trading; no direct market or price
  impact, but mandatory compliance action needed before June 06, 2026 discontinuation.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP74134.pdf
processing:
  attempts: 1
  content_hash: c70d26b00c573461
  processed_at: '2026-05-08T13:59:24.013347'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-08T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP74134.pdf
severity: medium
source: nse
stocks: []
tags:
- mock-trading
- neat-plus
- futures-and-options
- system-upgrade
- neat-adapter
- disaster-recovery
- rtcm
- broadcast-parameters
title: Mock Trading Session on May 09, 2026 - NEAT+ Version 7.8.8 for Futures & Options
  Segment
---

## Summary

NSE is conducting a mock trading session in the Futures & Options (F&O) segment on Saturday, May 09, 2026. The session introduces NEAT+ version 7.8.8, which is compatible with new broadcast parameters announced in circular NSE/MSD/74133 dated May 08, 2026. Members must transition from NEAT+ 7.8.7 (compatible only with existing parameters) to NEAT+ 7.8.8 (compatible with new parameters) before the discontinuation date of June 06, 2026.

## Key Points

- Mock trading session scheduled for Saturday, May 09, 2026 in the F&O segment
- Two trading sessions: Session-1 from Primary Site and Session-2 from DR (Disaster Recovery) Site
- NEAT+ 7.8.8 introduces compatibility with new broadcast parameters per circular NSE/MSD/74133
- NEAT+ 7.8.7 will be discontinued on June 06, 2026 (mock date)
- New NEAT Adapter Version 1.0.27 (Windows and Linux) is required, using GR PORT 10833
- Reversal Trade Cancellation Mechanism (RTCM) in Equity & Equity Derivatives will be available in this mock and goes live from May 11, 2026
- All outstanding orders will be cleared before each mock session
- Trades during mock sessions carry no financial obligation

## Regulatory Changes

- New broadcast parameters introduced for the F&O segment (detailed in circular NSE/MSD/74133 dated May 08, 2026)
- Reversal Trade Cancellation Mechanism (RTCM) — covering a five trading days horizon — is being activated for Equity & Equity Derivatives, effective May 11, 2026 (per circular NSE/SURV/74022 dated April 30, 2026)

## Compliance Requirements

- Members must download and install NEAT+ 7.8.8 from `/faoftp/faocommon/NEATPlus788` on NSE Extranet before June 06, 2026
- Members must upgrade to NEAT Adapter Version 1.0.27 (Windows/Linux) and use GR PORT 10833 for F&O segment login
- Members using NNF software must manually clear outstanding orders before each mock session
- Members should refer to connectivity parameters in circular NSE/MSD/73993 dated April 30, 2026
- Software testing compliance: refer to NSE/MSD/46441 and SEBI circular SEBI/HO/MRD1/DSAP/CIR/P/2020/234

## Important Dates

| Event | Date |
|---|---|
| Mock Trading Session | May 09, 2026 |
| RTCM goes live | May 11, 2026 |
| NEAT+ 7.8.7 Discontinuation (mock) | June 06, 2026 |

**Mock Session Schedule (May 09, 2026):**

| Particulars | Time (Hrs) |
|---|---|
| Session-1 (Primary): Pre-Open Open | 10:00 |
| Session-1 (Primary): Pre-Open Close* | 10:08 |
| Session-1 (Primary): Normal Market Open | 10:15 |
| Session-1 (Primary): Contingency Start | 12:45 |
| Session-1 (Primary): Contingency Close | 14:00 |
| Session-1 (Primary): Normal Market Close | 14:00 |
| Session-2 (DR): Pre-Open Open | 14:45 |
| Session-2 (DR): Pre-Open Close* | 14:53 |
| Session-2 (DR): Normal Market Open | 15:00 |
| Session-2 (DR): Normal Market Close | 16:00 |
| Trade Modification End | 16:10 |
| Live Re-login Start | 18:30 |
| Live Re-login Close | 19:00 |

*Random closure in last one minute

## Impact Assessment

This circular primarily impacts F&O segment members and technology/infrastructure teams. Members running NEAT+ 7.8.7 must plan an upgrade to 7.8.8 ahead of the June 06, 2026 discontinuation; failure to do so will result in incompatibility with the new broadcast parameters. The introduction of RTCM from May 11, 2026 adds a new surveillance mechanism that could affect order cancellation workflows for members active in the Equity and Equity Derivatives segments. No direct impact on underlying securities or market prices is expected from this operational change.