---
category: market-operations
circular_id: 30e59e97dd5bcfeb
date: '2026-03-27'
description: NSE Clearing introduces an optional facility for clearing members to
  set and monitor intraday uncrystallised Mark to Market (MTM) loss limits for their
  trading members via NMASS, effective April 1, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT73495.zip
impact: high
impact_ranking: high
importance_ranking: high
justification: Introduces a new risk management control mechanism that can automatically
  disable trading members when MTM losses breach set limits, directly affecting clearing
  and trading operations from April 1, 2026.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT73495.zip
processing:
  attempts: 1
  content_hash: e85a413b2e53293a
  processed_at: '2026-03-27T13:11:25.547492'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-03-27T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT73495.zip
severity: high
source: nse
stocks: []
tags:
- risk-management
- clearing-members
- trading-members
- mtm-limits
- futures
- nmass
- intraday-monitoring
- mark-to-market
title: Facility to Clearing Members to Monitor Intraday Uncrystallised Mark to Market
  Losses
---

## Summary

NSE Clearing Limited (NCL) is introducing an optional facility for clearing members to set intraday uncrystallised Mark to Market (MTM) loss limits for their trading members. The facility, available through NMASS, enables clearing members to monitor real-time MTM losses on futures positions and automatically disable trading members when losses breach 100% of the set limit. It goes live on **April 1, 2026**.

## Key Points

- Clearing members can optionally set MTM limits for trading members via NMASS (N-MASS system).
- MTM limits are used **solely** for monitoring intraday uncrystallised MTM losses — separate from margin monitoring against allocated/pledged collateral.
- Intraday uncrystallised MTM profits/losses are computed in **real time** for open positions in **futures contracts only**, based on the latest available price.
- Net MTM loss is computed across all clients and proprietary positions at the trading member level.
- If MTM losses breach **100% of the set limit**, the trading member is **disabled and placed in close-out mode**.
- Default MTM limit value is **zero** for all trading members; if no limit is set or it is zero, no MTM monitoring occurs.
- Limits can be set via the NMASS screen or via **file upload** (TXT or CSV format, 19-character filename).

## Regulatory Changes

- New optional risk control facility introduced under Circular Ref. No. 036/2026 (Download Ref No: NCL/CMPT/73495).
- Clearing members gain the ability to set trading member-level MTM limits independent of existing collateral-based margin monitoring.
- Automated disablement of trading members upon 100% MTM limit breach is a new enforcement mechanism.

## Compliance Requirements

- **Clearing Members**: May optionally configure MTM limits for their trading members in NMASS before April 1, 2026, if they wish to use the facility.
- **Limit Setup (Screen)**: Login to N-MASS → Limit and Enablement → FO Segment → TM Limit Setup → Set Limit → Select TM → Set IUMTM Limit (in Rs. Lakhs).
- **Limit Setup (File Upload)**: Navigate to Limits and Enablement → TM Limit Setup → Offline TM Limit Upload. File must be 19 characters (including extension), in `.txt` or `.csv` format, named `limit_ddmmyyyy_<nnnn>.txt/csv`.
- File fields: TM Code, CP Code, Set Limit (1 = eligible for auto approval, 0 = ineligible), Uncrystallised Set Limit (in Rs. Lakhs, e.g. `31.35` = Rs. 31.35 lakhs; `0` = unlimited).
- When TM code is provided, CP code field must contain one blank space, and vice versa.

## Important Dates

- **March 27, 2026**: Circular issued.
- **April 1, 2026**: Facility goes live; clearing members may begin setting MTM limits for trading members.

## Impact Assessment

This facility enhances intraday risk management for clearing members by providing a real-time automated safeguard against excessive uncrystallised MTM losses at the trading member level. Trading members operating with high intraday futures positions are at risk of automatic disablement if their clearing member sets MTM limits and losses breach those limits. Clearing members should proactively review whether to configure limits before April 1, 2026, and communicate any set limits to their trading members to avoid unexpected trading disruptions. The facility is limited to futures contracts and does not apply to options positions.