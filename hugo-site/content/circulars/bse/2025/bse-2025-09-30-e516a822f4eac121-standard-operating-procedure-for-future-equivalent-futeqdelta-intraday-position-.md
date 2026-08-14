---
category: trading
circular_id: e516a822f4eac121
date: '2025-09-30'
description: BSE circular outlining the standard operating procedure for Delta computation
  and Future Equivalent (FutEq) intraday position limits monitoring for equity index
  derivatives.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={BCE23357-F71C-44BD-996E-88AC78603F5C}&noticeno=20250930-114&dt=09/30/2025&icount=11&totcount=114&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Establishes standardized methodology for Delta computation and intraday
  position limit monitoring for equity index derivatives.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20250930-114&attachedId=121f6603-2dc5-46a0-9ee1-1b7068b7c36f
processing:
  attempts: 1
  content_hash: 5624d3576930c565
  last_updated: '2026-08-14T09:49:59.242414'
  processed_at: '2026-08-14T09:49:49.039371'
  processor_version: '2.0'
  retry_requested_for_stage: claude_failed
  retry_source: backfill
  stage: completed
  status: published
published_date: '2025-09-30T17:19:22+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20250930-114&attachedId=121f6603-2dc5-46a0-9ee1-1b7068b7c36f
severity: medium
source: bse
stocks: []
tags:
- derivatives
- delta-computation
- position-limits
- risk-management
- equity-index-derivatives
title: Standard Operating Procedure for Future Equivalent (FutEq)/(Delta) Intraday
  Position Limits Monitoring for Equity Index Derivatives
---

## Summary

BSE issued a standard operating procedure (SOP) for Future Equivalent (FutEq) and Delta intraday position limits monitoring for equity index derivatives, detailing formulas and calculation examples.

## Key Points

- Real-time underlying index value at snapshot time is used for underlying price.
- Volatility of the underlying is based on the previous day EOD (T-1 day), taking the higher of underlying annualized volatility and futures annualized volatility.
- FutEq of a call option is equal to N(d1), put option is N(d1) - 1, and futures contract is equal to 1.
- Detailed formulas for d1 using the Black-Scholes model with risk-free rate fixed at the latest RBI Repo rate.
- Time to Expiry (TTE) is calculated based on calendar day minutes and normalized over 365 days.

## Regulatory Changes

- Implementation of uniform Delta computation SOP for monitoring intraday position limits in equity index derivatives.

## Compliance Requirements

- Market participants and trading members must align their risk management and position monitoring systems with the specified Delta and FutEq computation methodology.

## Important Dates

- Effective for applicable reporting and monitoring frameworks as per exchange directives.

## Impact Assessment

- Enhances transparency and consistency in intraday position limit monitoring for index options and futures.