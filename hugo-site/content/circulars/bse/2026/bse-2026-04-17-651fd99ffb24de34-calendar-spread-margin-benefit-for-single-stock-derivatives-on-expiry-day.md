---
category: trading
circular_id: 651fd99ffb24de34
date: '2026-04-17'
description: ICCL implements changes to calendar spread margin benefit for Single
  Stock Derivatives (SSDs) on expiry day, effective May 4, 2026, in compliance with
  SEBI Circular dated February 5, 2026.
draft: false
guid: https://www.bseindia.com/downloads/UploadDocs/Notices/20260417-19/20260417-19.pdf
impact: high
impact_ranking: high
importance_ranking: high
justification: Mandatory margin framework change affecting all derivative members
  trading Single Stock Derivatives; removes calendar spread benefit on expiry day
  under both SPAN and Extreme Loss Margin, requiring system-level preparedness by
  May 4, 2026.
pdf_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260417-19/20260417-19.pdf
processing:
  attempts: 1
  content_hash: d34821aedbdcb9fe
  processed_at: '2026-04-17T13:30:51.745887'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-04-17T11:14:15+00:00'
rss_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260417-19/20260417-19.pdf
severity: high
source: bse
stocks: []
tags:
- calendar-spread
- single-stock-derivatives
- margin
- span-margin
- extreme-loss-margin
- expiry-day
- iccl
- derivatives
- sebi-circular
- risk-management
title: Calendar Spread Margin Benefit for Single Stock Derivatives on Expiry Day
---

## Summary

Pursuant to SEBI Circular no. HO/47/15/11(2)2025-MRD-TPD1/I/4226/2026 dated February 5, 2026, and ICCL Circular no. 20260210-46 dated February 10, 2026, the Indian Clearing Corporation Limited (ICCL) is implementing changes to the calendar spread margin benefit for Single Stock Derivatives (SSDs) on the expiry day. The key change eliminates the benefit of offsetting positions across different expiries for contracts expiring on that day.

## Key Points

- Calendar spread margin benefit for Single Stock Derivatives will no longer be available on the expiry day for contracts expiring on that day
- Changes affect both SPAN Margin (via scanTiers and dspread tags in .spn files) and Extreme Loss Margin (ELM)
- On expiry day, two scan tiers will be configured: Tier 1 covering nearest expiry (T Date) only, and Tier 2 covering all subsequent expiries
- On non-expiry days, only one tier will be configured covering the nearest expiry
- The dspread tag will exclude any expiry combinations involving the nearest expiry (T Date) on expiry day
- ELM calendar spread benefit will not be available for expiry-day contracts from the start of that day
- A sample SPAN file illustrating the changes has been enclosed with the notice

## Regulatory Changes

**SPAN Margin Changes:**
- Two tiers under scanTiers tag on expiry day:
  - Tier 1: Starting and Ending Period = Nearest expiry (T Date)
  - Tier 2: Starting Period = Expiry next to T-day Expiry; Ending Period = Farthest expiry
- One tier under scanTiers tag on non-expiry days (nearest expiry only)
- dspread tag on expiry day will not include any combinations involving the nearest expiry (T Date)

**Extreme Loss Margin Changes:**
- Positions in expiry-day stock futures contracts will not be eligible for calendar spread treatment on the day of expiry
- No ELM calendar spread benefit available for contracts expiring on that day, effective from Begin of Day (BOD)

## Compliance Requirements

- All members must take note of the above changes
- Members must ensure necessary system-level preparedness before May 4, 2026
- Risk and technology teams should update margin calculation systems to reflect new SPAN file structure (scanTiers and dspread tag handling)
- Members should review the sample SPAN file (BSERISK20260416-00) enclosed with the notice

## Important Dates

- **February 5, 2026**: SEBI Circular no. HO/47/15/11(2)2025-MRD-TPD1/I/4226/2026 issued
- **February 10, 2026**: ICCL Circular no. 20260210-46 issued
- **April 17, 2026**: This notice issued
- **May 4, 2026 (Monday)**: Changes effective from Begin of Day (BOD)

## Impact Assessment

This change has significant operational and risk impact for members trading Single Stock Derivatives:

- **Increased Margin Requirements on Expiry Day**: Members holding calendar spread positions in SSDs will face higher margin requirements on expiry day as the offsetting benefit is removed, potentially requiring additional capital deployment
- **System Changes Required**: Clearing members and their technology vendors must update margin calculation engines to handle the new two-tier SPAN structure and modified dspread logic
- **Intraday Risk Management**: Risk desks must account for higher margin calls at BOD on expiry days and plan liquidity accordingly
- **Alignment with SEBI Policy**: This change aligns ICCL's framework with SEBI's broader policy to reduce systemic risk around SSD expiries by treating expiring contracts independently
- **Scope**: All members trading Single Stock Derivatives on BSE/ICCL are affected; index derivatives are not mentioned and presumably unaffected