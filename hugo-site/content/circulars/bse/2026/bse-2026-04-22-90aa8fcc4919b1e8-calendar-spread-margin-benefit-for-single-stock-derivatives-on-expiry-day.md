---
category: trading
circular_id: 90aa8fcc4919b1e8
date: '2026-04-22'
description: ICCL implements changes to calendar spread margin benefit for Single
  Stock Derivatives (SSDs) on expiry day, effective May 4, 2026, in compliance with
  SEBI Circular dated February 5, 2026.
draft: false
guid: https://www.bseindia.com/downloads/UploadDocs/Notices/20260422-6/20260422-6.pdf
impact: high
impact_ranking: high
importance_ranking: high
justification: Mandatory SEBI-directed change affecting margin calculations for all
  single stock derivative positions on expiry day, requiring system-level preparedness
  from all members before May 4, 2026 BOD.
pdf_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260422-6/20260422-6.pdf
processing:
  attempts: 1
  content_hash: fb515fea7f3ae8ae
  processed_at: '2026-04-22T10:21:47.039384'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-04-22T09:24:31+00:00'
rss_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260422-6/20260422-6.pdf
severity: high
source: bse
stocks: []
tags:
- calendar-spread
- single-stock-derivatives
- span-margin
- extreme-loss-margin
- expiry-day
- iccl
- derivatives
- margin-framework
- sebi-circular
- risk-management
title: Calendar Spread Margin Benefit for Single Stock Derivatives on Expiry Day
---

## Summary

ICCL (Indian Clearing Corporation Limited) is implementing changes to the calendar spread margin benefit framework for Single Stock Derivatives (SSDs) on expiry day, effective from the Beginning of Day (BOD) on Monday, May 4, 2026. This is in compliance with SEBI Circular no. HO/47/15/11(2)2025-MRD-TPD1/I/4226/2026 dated February 5, 2026, and ICCL Circular no. 20260417-19 dated April 17, 2026.

## Key Points

- Calendar spread offset benefit across different expiries will not be available on the expiry day for contracts expiring on that day for single stock derivatives.
- Two SPAN tiers will be configured on expiry days: Tier 1 covers only the nearest expiry (T Date), Tier 2 covers next expiry to farthest expiry.
- On non-expiry days, a single tier covering nearest to farthest expiry continues as before.
- The `dspread` tag in SPAN files will exclude any expiry combinations involving the nearest expiry (T Date) on expiry day.
- Extreme Loss Margin (ELM) calendar spread benefit will not be available for contracts expiring on that day.
- A sample SPAN file illustrating the changes is enclosed with the circular.

## Regulatory Changes

**SPAN Margin Changes:**
- Introduction of two-tier `scanTiers` configuration on expiry days for stock symbols.
- Tier 1: Nearest expiry (T Date) to Nearest expiry (T Date) — isolated from spread benefit.
- Tier 2: Next expiry after T Date to Farthest expiry — eligible for spread benefit among themselves.
- `dspread` tag to exclude nearest expiry (T Date) combinations on expiry day.

**Extreme Loss Margin (ELM) Changes:**
- Positions in expiry-day stock futures contracts will not be eligible for calendar spread treatment.
- Such positions will be excluded from calendar spread benefit starting from the beginning of the expiry day.
- No ELM calendar spread benefit for contracts expiring on that day.

## Compliance Requirements

- All BSE/ICCL members must update their systems to reflect the new SPAN margin framework before May 4, 2026.
- Members must ensure system-level preparedness to handle the two-tier SPAN configuration on expiry days.
- Risk and margin systems must be configured to deny calendar spread offset for nearest-expiry SSD contracts on expiry day.
- Members should refer to the sample SPAN file (attachment: BSERISK20260416-00) for implementation guidance.

## Important Dates

- **February 5, 2026**: SEBI Circular issued mandating the change.
- **April 17, 2026**: ICCL Circular no. 20260417-19 issued.
- **April 22, 2026**: This BSE Notice issued (Notice No. 20260422-6).
- **May 4, 2026 (BOD)**: Effective date — all changes go live from the Beginning of Day.

## Impact Assessment

This change has a high operational and financial impact on members trading Single Stock Derivatives. On expiry days, traders holding calendar spread positions in SSDs will face increased margin requirements as the offset benefit against expiring contracts is removed. This may result in higher margin calls for members with near-month SSD positions on expiry days. Members need to update their risk management and margin calculation systems ahead of May 4, 2026. The change aligns India's SSD margin framework with SEBI's broader goal of reducing systemic risk around expiry events in single stock derivatives.