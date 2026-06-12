---
category: market-operations
circular_id: 3abddc2145a961fc
date: '2026-06-12'
description: NSE will conduct mock trading sessions from Primary and BCP/DR sites
  on June 13, 2026, covering three sessions including a re-login session to ensure
  connectivity for Monday, June 15, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/SLBS74683.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading exercise for BCP/DR site testing; no financial
  obligations, no regulatory changes, affects only member connectivity testing for
  the securities lending and borrowing segment.
pdf_url: https://nsearchives.nseindia.com/content/circulars/SLBS74683.pdf
processing:
  attempts: 1
  content_hash: db1bb8b3d41ead08
  processed_at: '2026-06-12T15:13:35.284785'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-12T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/SLBS74683.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- bcp
- disaster-recovery
- slbs
- securities-lending
- neat
- settlement-calendar
title: Mock Trading from BCP/DR Site on Saturday, June 13, 2026 - Securities Lending
  and Borrowing Market
---

## Summary

NSE will conduct a mock trading session on Saturday, June 13, 2026 for the Securities Lending and Borrowing (SLB) market segment, running sessions from both Primary and BCP/DR sites. A re-login session from the Primary site is scheduled to ensure members can connect smoothly for the live trading day on Monday, June 15, 2026.

## Key Points

- Three sessions scheduled: Primary site mock (09:15–11:00 hrs), BCP site mock (12:00–17:00 hrs), and Re-login session (18:30–19:00 hrs)
- Exchange will perform a non-graceful shutdown from the Primary site when switching to DR site during Session 2
- No changes to NEAT Adapter settings are required; settings from Friday June 12, 2026 live session will be retained
- All outstanding orders will be purged before each session starts
- Members using NNF software must manually clear outstanding orders from Session 1 before trading from BCP site
- NEAT version 1.3.3 and NEAT Adapter version 1.0.28 are applicable
- Connect2NSE and Extranet facility will not be available from 10:00–11:00 am and 06:00–09:00 pm
- Trades during mock sessions carry no financial obligation (no fund pay-in or pay-out)
- UCC validation will be skipped during contingency time for order entry
- NOTIS application will be accessible during the mock session

## Regulatory Changes

No regulatory changes. This is a routine operational mock trading exercise.

## Compliance Requirements

- Members must participate using all trading software and re-login into the live environment after the mock to ensure smooth connectivity for Monday, June 15, 2026
- Members should handle non-graceful shutdown scenarios per circular NSE/MSD/48662 dated June 18, 2021
- Connectivity parameters: refer to circular NSE/MSD/74511 dated June 02, 2026 for interactive connectivity details
- Installation procedure available on NSE Extranet at /slbftp/slbcommon/Installation_Procedure
- Only valid and compliant UCC/PAN uploaded and approved before cutoff will be allowed during the mock; queries to uci@nse.co.in
- Software testing requirements per circulars NSE/MSD/46441 and SEBI/HO/MRD1/DSAP/CIR/P/2020/234

## Important Dates

- **June 12, 2026 (Friday):** Retain NEAT Adapter settings from live session for use in mock
- **June 13, 2026 (Saturday):**
  - Session 1 (Primary Site): 09:15–11:00 hrs
  - Session 2 (BCP Site): 12:00–17:00 hrs
  - Re-login Session (Primary Site): 18:30–19:00 hrs
- **June 15, 2026 (Monday):** Live trading resumes; re-login session ensures smooth connectivity

## Impact Assessment

Minimal market impact. This is a scheduled disaster recovery drill for the SLB segment with no financial consequences for participants. Members must participate to validate connectivity before Monday's live session. The non-graceful shutdown during the Primary-to-DR switchover requires member-side preparedness per existing circulars. No changes to trading rules, margins, or settlement obligations are introduced.