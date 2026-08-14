---
category: trading
circular_id: 38bfb7de73989336
date: '2025-07-25'
description: BSE circular detailing revisions to the location ID structure, specifically
  incorporating identification for ALGO orders from client Direct API and 14th digit
  validations.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={5F76F509-59AF-4553-92F8-5EBFC85D149C}&noticeno=20250924-54&dt=09/24/2025&icount=54&totcount=75&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Provides critical technical validation rules for location IDs, order
  types, and algorithmic trading flags for trading members.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20250924-54&attachedId=260ce4d0-f3d2-4b8d-b5fa-1a96fd362a18
processing:
  attempts: 1
  content_hash: 0b815db1b32e330a
  last_updated: '2026-08-14T13:03:48.876421'
  processed_at: '2026-08-14T13:03:38.517967'
  processor_version: '2.0'
  retry_requested_for_stage: claude_failed
  retry_source: backfill
  stage: completed
  status: published
published_date: '2025-09-24T13:59:07+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20250924-54&attachedId=260ce4d0-f3d2-4b8d-b5fa-1a96fd362a18
severity: medium
source: bse
stocks: []
tags:
- trading
- market-operations
- algorithmic-trading
- dealer-terminals
title: Enhancement in registering dealer terminals and location ID structure
---

## Summary

BSE has issued a circular regarding enhancements in registering dealer terminals, specifically detailing revised identification requirements for location IDs (first 16-digits and 14th digit) to incorporate ALGO orders from client Direct API and define validation rules across various trading platforms.

## Key Points

- Revised identification guidelines for the first 13 digits and 14th digit of location IDs.
- Incorporation of identification rules for ALGO orders originating from client Direct API.
- Specific validations defined for different trading platforms including ETI, IBT, STWT, DMA, and Client Direct API.
- Clarification on the allowed values for the 14th digit to determine algorithmic versus non-algorithmic orders.

## Regulatory Changes

- Updated schema and structure for location IDs across platforms.
- Defined explicit 14th digit values corresponding to Non-Algorithmic Orders, Algorithmic Orders, and Algo using SOR.

## Compliance Requirements

- Trading members must ensure their systems and order placement mechanisms comply with the revised location ID and 14th digit validation standards.

## Important Dates

- Effective immediately as per exchange notice provisions.

## Impact Assessment

- Requires technical updates by trading members and API users to correctly populate location IDs and order type flags for compliance and order routing.