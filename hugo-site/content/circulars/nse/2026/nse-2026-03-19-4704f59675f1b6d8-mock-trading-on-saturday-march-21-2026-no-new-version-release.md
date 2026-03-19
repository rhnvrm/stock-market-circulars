---
category: market-operations
circular_id: 4704f59675f1b6d8
date: '2026-03-19'
description: NSE will conduct a mock trading session in the Currency Derivatives Segment
  on March 21, 2026, with two sessions from Primary and BCP sites. No new NEAT version
  will be released; version 3.5.4 remains current.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CD73369.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for operational readiness; no regulatory
  changes, no new software version, and no financial obligations arise from mock trades.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CD73369.pdf
processing:
  attempts: 1
  content_hash: b36b6a6a3242920d
  processed_at: '2026-03-19T13:13:20.046444'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-03-19T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CD73369.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- currency-derivatives
- neat
- bcp
- disaster-recovery
- trading-session
- market-operations
title: Mock Trading on Saturday, March 21, 2026 - Currency Derivatives Segment (No
  New Version Release)
---

## Summary

NSE will conduct a mock trading session in the Currency Derivatives (CD) Segment on Saturday, March 21, 2026. The session consists of two parts: Trading Session-1 from the Primary Site and Trading Session-2 from the BCP (Business Continuity Planning) Site. No new NEAT version is being released; members should continue using NEAT version 3.5.4.

## Key Points

- Mock trading date: Saturday, March 21, 2026
- Two sessions: Primary Site (11:00–14:00) and BCP Site (14:45–15:30)
- No new NEAT version release; current version is 3.5.4 (download path: `/cdsftp/cdscommon/NEATCDS354`)
- All outstanding orders will be purged before each session
- Trades during mock sessions carry no financial obligation (no fund pay-in or pay-out)
- Members must re-login to live environment after mock session to ensure connectivity for Monday, March 23, 2026
- NOTIS application will be accessible during the mock session
- UCC/PAN validation applies; only compliant UCC/PAN uploaded before cutoff will be allowed

## Regulatory Changes

No regulatory changes. This is a routine operational mock trading exercise.

## Compliance Requirements

- All CD segment members are automatically eligible; participation uses existing User IDs, IPs, and Box ID mappings
- Members using NNF (Non-NEAT Frontend) software must manually clear orders in their systems before each session
- NNF users must ensure: dealer-type User ID, conversion for NNF, and IP mapping
- Members should set appropriate branch and user limits
- Members must telnet-verify Exchange host connectivity from intended IP addresses
- Members should confirm Box ID is created with appropriate segment messages
- Refer to circulars NSE/MSD/67674 (April 24, 2025) and NSE/CD/70422 (September 25, 2025) for interactive connectivity details
- Software testing requirements per NSE/MSD/46441 and SEBI circular SEBI/HO/MRD1/DSAP/CIR/P/2020/234

## Important Dates

- **March 21, 2026**: Mock trading session
  - Session-1 (Primary Site): 11:00–14:00
  - Session-2 (BCP Site): 14:45–15:30
  - Trade Modification end time: 15:40
  - Live Re-login window: 16:30–17:00
- **March 23, 2026**: Next live trading day (Monday); members must ensure connectivity via re-login on mock day

## Impact Assessment

Minimal market impact. This is a standard mock/DR drill for Currency Derivatives Segment members to verify operational readiness, connectivity, and software compatibility. No financial settlements occur. Members are advised to participate fully to ensure smooth live trading on Monday, March 23, 2026.