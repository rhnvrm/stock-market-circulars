---
category: market-operations
circular_id: a87e5889d1d8eaef
date: '2025-10-31'
description: BSE introduces methodology for computing Delta (FutEq) for intraday monitoring
  of Market Wide Position Limits using real-time underlying prices and T-1 day volatility.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={92A71735-0348-49E9-A52F-06871F638C0E}&noticeno=20251031-63&dt=10/31/2025&icount=63&totcount=66&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Critical operational procedure affecting all derivatives market participants
  for MWPL monitoring and compliance
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251031-63&attachedId=8b87c543-c785-4a93-a045-3b8443f5b35b
processing:
  attempts: 1
  content_hash: df3b26353cf38c55
  processed_at: '2025-10-31T18:33:45.132087'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-31T15:28:06+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={92A71735-0348-49E9-A52F-06871F638C0E}&noticeno=20251031-63&dt=10/31/2025&icount=63&totcount=66&flag=0
severity: high
source: bse
stocks: []
tags:
- derivatives
- futures-and-options
- market-wide-position-limits
- mwpl
- delta-computation
- risk-management
- surveillance
- trading-methodology
title: Standard Operating Procedure for Intraday monitoring of MWPL utilization for
  single stocks on Future Equivalent(FutEq) basis
---

## Summary

BSE has issued a Standard Operating Procedure (Annexure 2) detailing the methodology for Delta Computation used in intraday monitoring of Market Wide Position Limits (MWPL) for single stock derivatives on a Future Equivalent (FutEq) basis. The procedure specifies the use of real-time underlying prices and previous day's volatility for computing option deltas.

## Key Points

- Real-time underlying value of the security at the time of snapshot will be used for underlying price
- Volatility of the underlying on Previous day EOD (T-1 day) will be used for intraday volatility computation
- FutEq of a call option contract equals N(d1)
- FutEq of a put option contract equals N(d1) - 1
- FutEq of a futures contract equals 1
- Risk-Free Interest Rate (Rf) is fixed at the latest RBI Repo rate
- N(d1) represents the cumulative probability distribution function

## Regulatory Changes

This circular establishes the standardized methodology for computing Future Equivalent positions for derivatives contracts, ensuring consistent application of MWPL monitoring across the exchange.

## Compliance Requirements

**For Trading Members and Market Participants:**
- Understand the Delta computation methodology for accurate position monitoring
- Ensure compliance with MWPL limits calculated using the FutEq basis
- Monitor positions throughout the trading day as deltas are computed in real-time

**Computation Formula:**
- d1 = {ln(S/K) + (Rf + 0.5 * Vol_Annual^2) * T} / (Vol_Annual * sqrt(T))
- Where: S = Underlying Price at snapshot, K = Strike Price, Rf = RBI Repo rate, Vol_Annual = Annualized Applicable Volatility, T = Prorated Time to Expiry

## Important Dates

- **Effective Date:** October 31, 2025
- **Reference:** Exchange Notice no. 20250930-114 dated September 30, 2025 (for Time to Expiry definition)

## Impact Assessment

**Market Impact:**
- Provides transparency and standardization in MWPL monitoring for single stock derivatives
- Enhances risk management framework for the derivatives market
- Real-time computation ensures accurate position tracking throughout the trading session

**Operational Impact:**
- Trading members must align their internal systems with BSE's Delta computation methodology
- Use of T-1 day volatility provides stability in intraday calculations
- Standardized approach facilitates better risk assessment and position management

**Trading Impact:**
- Affects all participants trading in single stock futures and options
- Critical for maintaining positions within regulatory MWPL limits
- Intraday monitoring may trigger position adjustments if limits are approached