---
category: market-operations
circular_id: 2b0be0e5d26f4530
date: '2026-01-16'
description: SEBI introduces Closing Auction Session (CAS) for stocks with derivative
  contracts to determine closing prices through auction mechanism instead of VWAP,
  effective in a phased manner.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={92076462-9F16-4A3B-8248-DF9362F53368}&noticeno=20260121-6&dt=01/21/2026&icount=6&totcount=7&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Major structural change to price discovery mechanism affecting all
  stocks with derivative contracts, impacting settlement, NAV determination, index
  computation, and trading operations for all market participants
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260121-6&attachedId=715e4ae6-69f7-4982-92c6-f03c050e7cd2
processing:
  attempts: 1
  content_hash: 316e463499f882dc
  processed_at: '2026-01-21T09:36:53.291319'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-21T07:27:33+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={92076462-9F16-4A3B-8248-DF9362F53368}&noticeno=20260121-6&dt=01/21/2026&icount=6&totcount=7&flag=0
severity: high
source: bse
stocks: []
tags:
- closing-auction-session
- cas
- equity-cash-segment
- closing-price-determination
- vwap
- derivatives
- trading-session
- market-operations
- auction-mechanism
- passive-funds
- index-computation
- mutual-fund-nav
title: Introduction of Closing Auction Session (CAS) in the Equity Cash Segment and
  certain modifications in the Pre-Open Auction Session
---

## Summary

SEBI introduces Closing Auction Session (CAS) in the equity cash segment to determine closing prices through an auction mechanism. Initially, CAS will apply only to stocks on which derivative contracts are available. The closing price for these stocks will be determined through a 20-minute auction session (3:15 PM to 3:35 PM) instead of the current VWAP-based method. This change aligns Indian markets with global best practices and provides fair, transparent closing prices used for derivatives settlement, index computation, and mutual fund NAV determination.

## Key Points

- CAS will be implemented in a phased manner, initially for stocks with derivative contracts only
- Current VWAP-based closing price determination (last 30 minutes) will be replaced by auction mechanism for applicable stocks
- CAS session will run from 3:15 PM to 3:35 PM (20 minutes total)
- Order entry period divided into three phases with random closure between 3:28 PM and 3:30 PM
- Equity derivatives segment will continue until 3:40 PM
- Post-close session in cash segment will operate from 3:50 PM to 4:00 PM at closing price
- Remaining securities not covered by CAS will continue using VWAP method
- CAS aggregates market interest into single liquidity pool for fair price discovery
- Facilitates passive funds to transact at closing price, reducing tracking error
- Provides equal access to all investor categories

## Regulatory Changes

**Closing Price Determination Method:**
- Stocks with derivative contracts: Closing price determined through Closing Auction Session (CAS)
- Other securities: Continue with VWAP of trades executed during last 30 minutes of Continuous Trading Session (CTS)

**CAS Framework:**

**Session Structure (3:15 PM - 3:35 PM):**
1. Session 1 (3:15 PM - 5 mins): Reference price calculation / Transition from CTS to CAS
2. Session 2 (3:20 PM - 5 mins): Order entry for both limit and market orders
3. Session 3 (3:25 PM - 5 mins): Order entry only for limit orders, no modification/cancellation for market orders, random close in last 2 minutes
4. Session 4 (3:30 PM - 5 mins): Order matching

**Random Closure:**
- Order entry session closes randomly between 3:28 PM and 3:30 PM (system-driven)

**Impact on Other Segments:**
- Equity derivatives: Continue operating until 3:40 PM
- Post-close session: 3:50 PM to 4:00 PM (trades execute at closing price)
- Special trading sessions: CAS duration same as regular sessions, derivatives close 10 minutes after CAS order entry period ends

## Compliance Requirements

**Stock Exchanges:**
- Implement CAS framework for stocks with derivative contracts
- Configure 20-minute auction session (3:15 PM - 3:35 PM)
- Implement random closure mechanism between 3:28 PM - 3:30 PM
- Adjust derivatives segment timings to 3:40 PM close
- Configure post-close session (3:50 PM - 4:00 PM)
- Apply CAS to special trading sessions with appropriate derivative segment timings

**Clearing Corporations:**
- Update settlement systems to use CAS-determined closing prices for applicable stocks
- Adjust derivatives settlement to use CAS closing prices

**Market Participants:**
- Adapt trading systems and strategies to new CAS timings
- Update order routing systems to accommodate three-phase order entry period
- Prepare for random closure between 3:28 PM - 3:30 PM
- Adjust algorithmic trading strategies for auction mechanism

**Mutual Funds:**
- Use CAS-determined closing prices for NAV calculation for applicable stocks
- Leverage CAS for passive fund transactions to reduce tracking error

**FPIs and Other Investors:**
- Understand new price discovery mechanism for stocks with derivatives
- Adjust trading workflows for extended session timings

## Important Dates

**Circular Date:** January 16, 2026

**Implementation:** Phased manner (specific implementation date not mentioned in the circular)

**Note:** The circular does not specify the exact effective date for CAS implementation. Stock Exchanges are expected to issue separate circulars with implementation timeline.

## Impact Assessment

**Market Structure Impact:**
- Fundamental change in price discovery mechanism for liquid stocks with derivative contracts
- Alignment with global best practices used in major jurisdictions
- Enhanced price transparency and fairness in closing price determination
- Single liquidity pool for improved execution efficiency of large orders

**Operational Impact:**
- Extended trading hours: Main session ends at 3:35 PM (from current 3:15 PM)
- Derivatives segment operates additional 5 minutes (until 3:40 PM vs current 3:30 PM)
- Post-close session shifted to 3:50 PM - 4:00 PM
- Market participants need system upgrades for new session structure

**Settlement and Valuation Impact:**
- Derivatives settlement: Uses auction-determined closing price (more reflective of market consensus)
- Index computation: Enhanced accuracy with auction-based closing prices
- Mutual Fund NAV: Improved accuracy and fairness in valuation
- Reduced potential for price manipulation at close

**Investor Category Impact:**
- Passive funds: Reduced tracking error through direct closing price transactions
- Institutional investors: Better execution for large orders through aggregated liquidity
- Retail investors: Equal access to price discovery mechanism
- All categories: Transparent price formation reflecting collective market consensus

**Risk Management:**
- Random closure mechanism prevents gaming of auction
- Three-phase order entry allows gradual price discovery
- Market order restrictions in final phase enhance stability

**Scope:**
- High impact on stocks with derivative contracts (typically most liquid stocks)
- No immediate impact on remaining securities (continue with VWAP method)
- Phased implementation allows gradual market adaptation