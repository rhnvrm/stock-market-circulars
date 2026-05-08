---
category: market-operations
circular_id: 2ff18c64e987a355
date: '2026-05-08'
description: NSE will conduct a mock trading session in the Capital Market Segment
  on May 09, 2026, introducing NEAT+ version 7.8.8 with updated session timings and
  Reversal Trade Cancellation Mechanism (RTCM).
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMTR74121.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for system testing purposes; limited to
  technology and operational readiness for members, no direct market or stock-level
  impact.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMTR74121.pdf
processing:
  attempts: 1
  content_hash: cb9daa35a75032dd
  processed_at: '2026-05-08T10:28:32.198515'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-08T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMTR74121.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- neat-plus
- capital-market
- trading-system
- disaster-recovery
- rtcm
- block-deal
- pre-open-session
title: Mock Trading on Saturday, May 09, 2026 - New Version of NEAT+ 7.8.8
---

## Summary

NSE will conduct a mock trading session in the Capital Market Segment on Saturday, May 09, 2026. The session introduces NEAT+ version 7.8.8, available for download at `/common/NEATPlus788`. Members are expected to test the new version ahead of the discontinuation of version 7.8.7 on June 06, 2026 (mock). The session also includes a test of the Reversal Trade Cancellation Mechanism (RTCM), which will go live from May 11, 2026.

## Key Points

- Mock trading session scheduled for Saturday, May 09, 2026 in the Capital Market Segment
- New NEAT+ version 7.8.8 introduced; download path: `/common/NEATPlus788`
- NEAT+ version 7.8.7 discontinuation date: June 06, 2026 (mock)
- NEAT Adapter version 1.0.27 (Windows and Linux) with GR PORT 10823 required
- Reversal Trade Cancellation Mechanism (RTCM) will be tested in this mock session and go live May 11, 2026
- Two trading sessions: Primary Site (Session-1) and DR Site (Session-2)

## Regulatory Changes

- Introduction of NEAT+ 7.8.8 replacing 7.8.7 (discontinuation scheduled June 06, 2026)
- Reversal Trade Cancellation Mechanism (RTCM) in Equity & Equity Derivatives Segment (five trading days horizon) to be made effective from May 11, 2026, per circular NSE/SURV/74022 dated April 30, 2026

## Compliance Requirements

- Members must download and test NEAT+ version 7.8.8 from NSE Extranet at `/common/NEATPlus788`
- Members must use NEAT Adapter version 1.0.27 with GR PORT 10823 for Capital Market segment logins
- Members should refer to NEAT Adapter circular NSE/MSD/73674 dated April 09, 2026 for full adapter details
- Members must participate in mock session to validate system readiness before RTCM goes live

## Important Dates

- **May 09, 2026**: Mock trading session (Primary Site Session-1 and DR Site Session-2)
- **May 11, 2026**: RTCM goes live in Equity & Equity Derivatives Segment
- **June 06, 2026**: NEAT+ version 7.8.7 discontinuation (mock)

### Session Timings (May 09, 2026 - Primary Site)

| Event | Time |
|---|---|
| Morning Block Deal Window Session-1 Open | 09:45 |
| Morning Block Deal Window Session-1 Close | 10:00 |
| Pre-Open Open | 10:00 |
| Pre-Open Close (random last 1 min) | 10:08 |
| Special Pre-Open Open (IPO & Relisted) | 10:00 |
| Special Pre-Open Close (random last 10 min) | 10:45 |
| Normal Market Open | 10:15 |
| T+0 Market Open | 10:15 |
| Call Auction Illiquid Session Open | 10:30 |
| T+0 Market Close | 12:30 |
| T+0 Trade Modification End | 12:40 |
| Normal Market Open (Special Pre-Open stocks) | 11:00 |
| Auction Market Open | 11:30 |
| Auction Market Close | 12:15 |
| Afternoon Block Deal Window Session-2 Open | 12:05 |
| Afternoon Block Deal Window Session-2 Close | 12:20 |
| Contingency Start | 12:45 |
| Contingency Close / Normal Market Close | 14:00 |

### Session Timings (May 09, 2026 - DR Site Session-2)

| Event | Time |
|---|---|
| Pre-Open Open | 14:45 |
| Pre-Open Close | 14:53 |
| Normal Market Open | 15:00 |
| Call Auction Illiquid Session Open | 15:00 |
| Normal Market Close | 16:00 |
| Closing Session Open | 16:10 |
| Closing Session Close | 16:20 |
| Trade Modification End | 16:30 |
| Live Re-login Start | 17:30 |
| Live Re-login Close | 18:00 |

## Impact Assessment

This is a routine operational mock session with no direct market impact. Members (trading terminals) must upgrade to NEAT+ 7.8.8 and validate connectivity ahead of the June 2026 discontinuation deadline for version 7.8.7. The inclusion of RTCM testing is notable as the mechanism goes live on May 11, 2026, making participation in this mock session important for members trading in Equity and Equity Derivatives segments.