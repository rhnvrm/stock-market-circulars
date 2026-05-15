---
category: market-operations
circular_id: 8c409899b189308d
date: '2026-05-15'
description: NSE will conduct a mock trading session in the Futures & Options segment
  on Saturday, May 16, 2026. No new software version is being released; members should
  use NEATPlus 7.8.7 or 7.8.8 and re-login to the live environment afterward.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP74258.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for F&O segment with no new version release;
  primarily operational guidance for members to test connectivity before the live
  week.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP74258.pdf
processing:
  attempts: 1
  content_hash: d3e1dbcd76f89ead
  processed_at: '2026-05-15T19:38:17.688446'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-15T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP74258.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- futures-and-options
- neat-plus
- neat-adapter
- trading-session
- saturday-mock
- f-and-o
title: Mock Trading Session - Futures & Options Segment, May 16, 2026 (No New Version
  Release)
---

## Summary

NSE will hold a mock trading session in the Futures & Options (F&O) segment on Saturday, May 16, 2026. No new software version is being released for this mock. Members are expected to participate using all trading software and re-login to the live environment afterward to ensure smooth connectivity for Monday, May 18, 2026.

## Key Points

- Mock trading is scheduled for May 16, 2026 in the Futures & Options segment
- No new version release accompanying this mock session
- Normal Market open: 12:45, Normal Market close: 15:15
- Pre-Open opens at 12:30, closes at 12:38 (random closure in last one minute)
- Trade Modification end time: 15:25
- Live Re-login window: 18:30–19:00
- NEATPlus 7.8.7 (compatible with existing broadcast parameters) and 7.8.8 (compatible with new broadcast parameters) are both supported
- NEATPlus 7.8.8 download path: `/faoftp/faocommon/NEATPlus788`; discontinuation date for 7.8.7: June 06, 2026 (mock)
- New NEAT Adapter (Version 1.0.27, Windows & Linux) must use GR PORT 10833 for F&O segment
- All outstanding orders will be purged before each session
- Trades during mock sessions carry no financial obligation (no fund pay-in/pay-out)

## Regulatory Changes

No regulatory changes introduced by this circular. Members are reminded of existing obligations under SEBI circular SEBI/HO/MRD1/DSAP/CIR/P/2020/234 and NSE/MSD/46441 regarding software testing using Mock Trading or Simulated Environments.

## Compliance Requirements

- Members must participate in the mock session using all trading software
- Members using NNF software must manually clear orders in their systems before each session
- Only valid and compliant UCC/PAN uploaded and approved before cutoff will be allowed; UCC validation is skipped during contingency time
- Members should refer to NSE/MSD/73993 (April 30, 2026) for interactive connectivity details
- NEAT Adapter version 1.0.27 (Windows/Linux) must be used with GR PORT 10833
- Members should re-login to the live environment after the mock session to ensure Monday readiness

## Important Dates

- **May 16, 2026**: Mock trading session date (F&O segment)
- **May 18, 2026**: Next live trading Monday — members should ensure connectivity post-mock
- **June 06, 2026**: NEATPlus 7.8.7 discontinuation (mock); members should migrate to 7.8.8
- **2:00 PM on mock day**: Connect2NSE and Extranet facility unavailable until end of mock session
- **2:00 PM – 3:00 PM on mock day**: Extranet API unavailable

## Impact Assessment

This is a routine operational circular with low market impact. It affects all F&O segment members who must test their trading infrastructure. No financial settlements result from mock trades. Members running older NEATPlus versions (7.8.7) should note the June 2026 discontinuation and plan migration to 7.8.8, which supports new broadcast parameters introduced via NSE/MSD/74133 dated May 08, 2026.