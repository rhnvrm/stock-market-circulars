---
category: market-operations
circular_id: f2ff051142b14815
date: '2026-06-12'
description: NSE will conduct a mock trading session on June 13, 2026 from both Primary
  and BCP/DR sites, followed by a re-login session from Primary site to ensure smooth
  operations on Monday, June 15, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP74689.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for BCP/DR preparedness; no financial
  obligations, no regulatory changes, and no impact on live trading or specific securities.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP74689.pdf
processing:
  attempts: 1
  content_hash: 9603d1930ed529b7
  processed_at: '2026-06-12T15:11:31.868483'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-12T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP74689.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- bcp
- disaster-recovery
- futures-and-options
- settlement-calendar
- live-activities-schedule
title: Mock Trading from BCP/DR Site on Saturday, June 13, 2026
---

## Summary

NSE will conduct a mock trading session on Saturday, June 13, 2026, covering both the Primary site (Trading Session-1) and BCP/DR site (Trading Session-2) for the Futures & Options segment. A re-login session from the Primary site will follow in the evening to prevent login issues on Monday, June 15, 2026.

## Key Points

- Two mock trading sessions scheduled: Session-1 from Primary site (09:00–11:00) and Session-2 from BCP site (11:45–15:30)
- Re-login session from Primary site: 18:30–19:00
- No changes required in NEAT Adapter settings; live settings from June 12, 2026 will be retained
- Exchange will perform a non-graceful shutdown from Primary site when shifting to DR site
- All outstanding orders will be purged before trading starts from BCP site
- Multicast TBT sequence numbers will reset to '1' when trading starts from BCP site
- Colo Participants should expect different latencies on DR/BCP day compared to normal trading days
- Trades during mock sessions carry no financial obligation (no fund pay-in or pay-out)

## Regulatory Changes

No regulatory changes. This is an operational mock/drill exercise to test BCP/DR readiness.

## Compliance Requirements

- Members using NNF software must manually clear outstanding orders from Session-1 before connecting to the BCP site session
- Only valid and compliant UCC/PAN uploaded and approved before cutoff are permitted during mock trading
- Members should refer to circular NSE/MSD/48662 dated June 18, 2021 for actions required during a non-graceful shutdown event
- Connectivity details available in circular NSE/MSD/74511 dated June 02, 2026
- Software testing requirements per circulars NSE/MSD/46441 and SEBI/HO/MRD1/DSAP/CIR/P/2020/234

## Important Dates

- **June 13, 2026 (Saturday):** Mock trading day
  - Session-1 (Primary): Pre-Open 09:00, Normal Open 09:15, Close 11:00
  - Session-2 (BCP): Pre-Open 11:45, Normal Open 12:00, Close 15:30, Trade modification end 16:15
  - Re-login (Primary): 18:30–19:00
- **June 15, 2026 (Monday):** Live trading resumes; re-login session on June 13 is intended to avoid login issues on this date

## Impact Assessment

This is a routine operational drill with no impact on live trading, market participants' positions, or financial settlements. Members should ensure their systems are prepared for non-graceful shutdown scenarios and BCP connectivity. Colo Participants should be aware of latency differences during DR operations.