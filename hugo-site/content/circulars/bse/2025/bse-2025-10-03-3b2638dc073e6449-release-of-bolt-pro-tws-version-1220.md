---
category: market-operations
circular_id: 3b2638dc073e6449
date: '2025-07-25'
description: BSE announces the release of BOLT Pro TWS Version 12.20 introducing separate
  Location ID configurations for manual, batch, and basket orders.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={24BA04B6-F86B-4A3A-B582-FD4E118D7184}&noticeno=20251003-8&dt=10/03/2025&icount=8&totcount=14&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Introduces necessary terminal setting updates and error handling for
  basket and batch orders based on separate Location IDs.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251003-8&attachedId=b5263904-2f75-448f-89d4-1939e7f8531b
processing:
  attempts: 1
  content_hash: d84aed687471117c
  last_updated: '2026-08-14T09:23:54.807994'
  processed_at: '2026-08-14T09:23:44.328875'
  processor_version: '2.0'
  retry_requested_for_stage: claude_failed
  retry_source: backfill
  stage: completed
  status: published
published_date: '2025-10-03T06:54:01+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251003-8&attachedId=b5263904-2f75-448f-89d4-1939e7f8531b
severity: medium
source: bse
stocks: []
tags:
- bolt-pro-tws
- trading-terminal
- location-id
- market-operations
- software-update
title: Release of BOLT Pro TWS Version 12.20 with New Classification of Location IDs
  for Basket and Batch Orders
---

## Summary

BSE has released BOLT Pro TWS Version 12.20, which introduces separate Location ID capture for Manual Orders, Basket Orders, and Batch Orders to align with exchange circulars on enhancing registered dealer terminal controls.

## Key Points

- Separate configuration fields added for Manual Order, Batch Order, and Basket Order Location IDs.
- Manual Order Location ID remains a mandatory field at login.
- Batch Order and Basket Order Location IDs are optional; however, unconfigured locations will restrict order placement from their respective windows.
- Clear error messages are prompted when required Location IDs are missing in the trading terminal settings.

## Regulatory Changes

- Implementation of separate Location ID tracking for different order types originating from BOLT Pro TWS following exchange circulars.

## Compliance Requirements

- Trading members must upgrade to BOLT Pro TWS Version 12.20 and configure appropriate Location IDs for manual, batch, and basket orders via preferences to avoid order placement restrictions.

## Important Dates

- Effective with the release of BOLT Pro TWS Version 12.20.

## Impact Assessment

- Trading operations must ensure dealers update terminal settings to prevent disruption in executing batch or basket orders.