---
category: market-operations
circular_id: dd7cac39a57aac00
date: '2026-05-22'
description: NSE will conduct a mock trading session in the Electronic Gold Receipts
  (EGR) segment on May 23, 2026, covering two trading sessions from Primary and DR
  sites. No new software version is being released.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/EGR74355.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for EGR segment with no new software version;
  no financial obligations arise from trades executed during the session.
pdf_url: https://nsearchives.nseindia.com/content/circulars/EGR74355.pdf
processing:
  attempts: 1
  content_hash: 8cb8141f0dd4a5ab
  processed_at: '2026-05-22T20:03:48.703614'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-22T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/EGR74355.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- egr
- electronic-gold-receipts
- neat
- disaster-recovery
- market-operations
title: Mock Trading Session in EGR Segment - Saturday, May 23, 2026 (No New Version
  Release)
---

## Summary

NSE is conducting a mock trading session in the Electronic Gold Receipts (EGR) segment on Saturday, May 23, 2026. No new NEAT+ version is being released in conjunction with this session. The mock covers two trading sessions — one from the Primary (BKC) site and one from the Disaster Recovery (DR) site — to test system readiness and member connectivity.

## Key Points

- Mock trading is scheduled for Saturday, May 23, 2026 in the EGR segment
- No new version release; NEAT EGR version in use remains **1.0.0**
- Two sessions: Trading Session-1 from Primary Site (BKC) and Trading Session-2 from DR Site
- NEAT Adapter version applicable: **1.0.25** (Windows and Linux); GR PORT: **11887**
- Default login password for mock session: `Neat@EG1`
- Trades executed during mock sessions carry **no financial obligation** (no fund pay-in or pay-out)
- Members should refer to NEAT Adapter circular NSE/MSD/74225 dated May 14, 2026 for adapter setup

## Regulatory Changes

No regulatory changes. This is an operational mock exercise to validate trading infrastructure including Primary-to-DR switchover procedures.

## Compliance Requirements

- Members must download NEAT EGR Version 1.0.0 from NSE Extranet path `/egftp/egcommon/NEATPlus100` if not already installed
- NEAT Adapter executable (`NA_1.0.25_Setup.exe`) available at `/egftp/egcommon/NeatAdapter/`
- Security and participant master files (`security_eg.gz`, `participant_eg.gz`) available at `egftp/egcommon/ntneat`
- Application supports OS up to Windows 10; Microsoft redistributable package (VS 2015) must be pre-installed
- Members must use the correct GR PORT (11887) with the new NEAT Adapter for EGR segment login
- Refer to Annexures 1–5 in the circular for detailed instructions on login parameters, market data broadcast, installation, and DR switchover guidelines

## Important Dates

| Event | Date/Time |
|---|---|
| Mock Trading Date | Saturday, May 23, 2026 |
| Session-1 Pre-open Open (Primary) | 08:45 hrs |
| Session-1 Pre-open Close (Primary) | 08:53 hrs |
| Session-1 Normal Market Open (Primary) | 09:00 hrs |
| Session-1 Normal Market Close (Primary) | 10:05 hrs |
| Session-2 Pre-open Open (DR) | 10:45 hrs |
| Session-2 Pre-open Close (DR) | 10:53 hrs |
| Session-2 Normal Market Open (DR) | 11:00 hrs |
| Session-2 Normal Market Close (DR) | 11:30 hrs |
| Trade Modification End Time | 11:10 hrs |
| Live Re-login Start | 13:00 hrs |
| Live Re-login Close | 13:30 hrs |

## Impact Assessment

Minimal market impact. This is a routine technical drill for the EGR segment. Members using the EGR platform must ensure connectivity and software readiness before the session. No trades from the mock session result in any financial settlement. The inclusion of a DR site session tests business continuity preparedness.