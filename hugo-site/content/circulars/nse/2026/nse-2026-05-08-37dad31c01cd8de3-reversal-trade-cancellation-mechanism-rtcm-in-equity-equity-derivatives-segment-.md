---
category: trading
circular_id: 37dad31c01cd8de3
date: '2026-05-08'
description: NSE announces that the 5-Day Reversal Trade Cancellation Mechanism (RTCM)
  will go live on May 11, 2026, clarifying that intraday cancellations apply only
  to eligible reversal trades with no cancellation of previous day trades.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/SURV74137.pdf
impact: high
impact_ranking: high
importance_ranking: high
justification: RTCM going live on May 11, 2026 directly affects all NSE trading members
  in equity and equity derivatives segments by introducing automatic trade cancellations
  for reversal trades, requiring immediate operational awareness and system readiness.
pdf_url: https://nsearchives.nseindia.com/content/circulars/SURV74137.pdf
processing:
  attempts: 1
  content_hash: fadaf611a32b91ec
  processed_at: '2026-05-08T16:22:30.212322'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-08T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/SURV74137.pdf
severity: high
source: nse
stocks: []
tags:
- rtcm
- reversal-trade-cancellation
- surveillance
- equity
- equity-derivatives
- trade-cancellation
- market-surveillance
- pan-based-monitoring
title: Reversal Trade Cancellation Mechanism (RTCM) Goes Live May 11, 2026 - Equity
  & Equity Derivatives Segment
---

## Summary

NSE Surveillance has issued a follow-up circular to NSE/SURV/74022 (April 30, 2026) confirming that the 5-Day Reversal Trade Cancellation Mechanism (RTCM) will go live on May 11, 2026. The circular provides critical clarifications on the scope of intraday trade cancellations and reiterates that trading members retain full compliance obligations under existing surveillance circulars.

## Key Points

- The 5-Day RTCM mechanism becomes operational on **May 11, 2026**
- Automatic intraday trade cancellations will apply only to eligible reversal trades within the same trading day
- No trades from previous days will be cancelled — the cancellation date and trade date must be the same
- Upon cancellation, trading terminals will display: `Trade CXL: <Trade details> Trade Cancelled by Exchange User Id (Dealer ID)`
- RTCM targets reversal trades between two PANs where specific thresholds are breached
- The mechanism covers both Equity and Equity Derivatives segments
- RTCM does not replace or reduce trading members' existing compliance obligations

## Regulatory Changes

This circular amends point 6 of NSE/SURV/74022 (April 30, 2026) to explicitly clarify that intraday cancellations are strictly limited to eligible reversal trades identified on the same day. The clarification removes any ambiguity about whether prior-day trades could be retroactively cancelled under RTCM — they cannot.

RTCM builds upon earlier surveillance mechanisms introduced via:
- NSE/SURV/62493 dated June 18, 2024
- NSE/SURV/65645 dated December 17, 2024

## Compliance Requirements

- Trading members must ensure their trading terminals and systems are ready to receive and process RTCM cancellation messages from May 11, 2026
- Members must continue to monitor client transactions and take necessary steps per **NSE/SURV/48818 dated July 1, 2021**, regardless of RTCM being active
- Full compliance with **NSE/INVG/46662 dated December 16, 2020** obligations remains mandatory — RTCM does not absolve members of these duties
- Members with queries should contact surveillance@nse.co.in

## Important Dates

| Date | Event |
|------|-------|
| April 30, 2026 | Original RTCM circular NSE/SURV/74022 issued |
| May 08, 2026 | This clarification circular (NSE/SURV/74137) issued |
| **May 11, 2026** | **5-Day RTCM mechanism goes LIVE** |

## Impact Assessment

**For Trading Members:** High operational impact. All NSE members trading in equity and equity derivatives segments must be aware that from May 11, 2026, the exchange will automatically cancel trades identified as eligible reversal trades on an intraday basis. Members need to brief their dealers about the new cancellation message format and ensure back-office systems can handle auto-cancellation events.

**For Dealers/Traders:** Trades flagged as reversal trades between two PANs exceeding defined thresholds will be cancelled without manual intervention. Dealers will receive real-time terminal alerts upon cancellation.

**Market Integrity:** This mechanism strengthens NSE's automated surveillance capabilities by removing the need for manual intervention to cancel suspicious reversal trades, reducing the window for potential market manipulation. The intraday-only scope limits disruption to settlement cycles.

**Compliance Risk:** Trading members who rely solely on RTCM for reversal trade monitoring face regulatory risk — the circular explicitly states that RTCM is a supplementary facility, not a substitute for member-level surveillance obligations.