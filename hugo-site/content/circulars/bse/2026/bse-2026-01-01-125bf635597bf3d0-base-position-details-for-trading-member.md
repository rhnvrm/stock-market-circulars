---
category: trading
circular_id: 125bf635597bf3d0
date: '2026-01-01'
description: ICCL introduces base position reporting at proprietary/constituent level
  for stocks under ban, enabling enhanced risk monitoring in equity derivatives effective
  January 5, 2026.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={19605EB1-EC41-4A49-9EFC-FCC067381E8B}&noticeno=20260101-9&dt=01/01/2026&icount=9&totcount=22&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational enhancement for risk monitoring affecting trading members
  dealing with banned stocks in F&O segment. Improves transparency but does not change
  trading rules.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260101-9&attachedId=
processing:
  attempts: 1
  content_hash: ac03da6a4125ec4e
  processed_at: '2026-01-01T12:51:16.380140'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-01T07:59:01+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={19605EB1-EC41-4A49-9EFC-FCC067381E8B}&noticeno=20260101-9&dt=01/01/2026&icount=9&totcount=22&flag=0
severity: medium
source: bse
stocks: []
tags:
- derivatives
- risk-management
- trading-members
- position-limits
- stock-ban
- iccl
- sebi-circular
- fno
- clearing
title: Base Position Details for Trading Members in Equity Derivatives Ban Stocks
---

## Summary

Indian Clearing Corporation Limited (ICCL) has introduced a new reporting mechanism providing trading members with detailed base position information at proprietary and constituent levels for stocks placed under ban. This circular partially modifies earlier ICCL Circular no: 20251128-6 dated November 28, 2025, and implements measures outlined in SEBI circular SEBI/HO/MRD/TPD-1/P/CIR/2025/79 regarding enhanced trading convenience and risk monitoring in equity derivatives.

## Key Points

- Trading members will receive base position details for stocks in ban at proprietary/constituent level
- File accessible via path: Home > FNO > Transaction > Month-YYYY > DD-MM-YYYY
- File nomenclature: BASEPOSITION_TM_MEMBERID_DDMMYYYY
- Base positions applicable for next day trading
- Covers both stock options (SO) and stock futures (SF)
- File includes detailed fields: Date, CM/Member/Client IDs, contract details, expiry dates, strike prices, option types, and base positions

## Regulatory Changes

This circular implements SEBI's directive (ref: SEBI/HO/MRD/TPD-1/P/CIR/2025/79 dated May 29, 2025) for enhancing trading convenience and strengthening risk monitoring in equity derivatives. It partially modifies the previous ICCL Circular no: 20251128-6 dated November 28, 2025, by providing granular position-level reporting for banned stocks.

## Compliance Requirements

- Trading members must access and review base position files daily through the FNO portal
- Members should monitor positions at UCC code level for stocks under ban
- File format includes comprehensive data fields covering clearing member ID, trading member ID, client ID, series details, contract specifications, and base positions
- Members must utilize this information for effective risk management and compliance with position limits

## Important Dates

- **Circular Date**: January 1, 2026
- **Effective Date**: January 5, 2026
- **Reference Circulars**: SEBI circular dated May 29, 2025; ICCL circular dated May 30, 2025; ICCL circular dated November 28, 2025

## Impact Assessment

**Operational Impact**: Medium - Trading members gain enhanced visibility into client-level positions for banned stocks, improving risk monitoring capabilities. The structured file format enables systematic tracking of stock options and futures positions.

**Market Impact**: Low to Medium - Strengthens risk management framework for equity derivatives by providing granular position data. May help prevent excessive concentration in banned stocks and improve overall market stability.

**Technical Impact**: Members need to integrate new file downloads into daily operational workflows and potentially update internal systems to consume the BASEPOSITION file format with 16 specified fields.