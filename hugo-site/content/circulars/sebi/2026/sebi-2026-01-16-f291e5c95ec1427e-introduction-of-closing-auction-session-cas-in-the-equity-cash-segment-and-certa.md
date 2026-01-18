---
category: market-operations
circular_id: f291e5c95ec1427e
date: '2026-01-16'
description: SEBI introduces Closing Auction Session (CAS) for derivative stocks in
  equity cash segment to determine closing price through auction mechanism instead
  of VWAP, with phased implementation from 3:15 PM to 3:35 PM.
draft: false
guid: https://www.sebi.gov.in/legal/circulars/jan-2026/introduction-of-closing-auction-session-cas-in-the-equity-cash-segment-and-certain-modifications-in-the-pre-open-auction-session_99122.html
impact: high
impact_ranking: high
importance_ranking: high
justification: Major structural change to market operations affecting closing price
  determination for all derivative stocks, impacting derivatives settlement, index
  computation, mutual fund NAV calculations, and trading hours. Affects all market
  participants including institutional investors, passive funds, and individual traders.
pdf_url: https://www.sebi.gov.in/sebi_data/attachdocs/jan-2026/1768576287344.pdf
processing:
  attempts: 1
  content_hash: b3245e653202584f
  processed_at: '2026-01-18T01:59:34.579420'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-16T00:00:00+05:30'
rss_url: https://www.sebi.gov.in/legal/circulars/jan-2026/introduction-of-closing-auction-session-cas-in-the-equity-cash-segment-and-certain-modifications-in-the-pre-open-auction-session_99122.html
severity: high
source: sebi
stocks: []
tags:
- closing-auction-session
- cas
- equity-cash-segment
- closing-price
- derivatives
- market-operations
- trading-hours
- vwap
- auction-mechanism
- market-infrastructure
- passive-funds
- index-computation
- mutual-funds
- nav-determination
title: Introduction of Closing Auction Session (CAS) in Equity Cash Segment and Modifications
  to Pre-Open Auction Session
---

## Summary

SEBI has introduced a Closing Auction Session (CAS) in the equity cash segment to determine closing prices through an auction mechanism instead of the current Volume Weighted Average Price (VWAP) method. Initially, CAS will apply to stocks on which derivative contracts are available, while other securities will continue using VWAP. The CAS will operate from 3:15 PM to 3:35 PM daily, featuring a 20-minute session with order entry, random close, and order matching phases. This change aligns Indian markets with global best practices and provides fair, transparent closing prices used for derivatives settlement, index computation, and mutual fund NAV determination.

## Key Points

- CAS introduced as separate 20-minute session from 3:15 PM to 3:35 PM on all trading days
- Phased implementation: Initially applicable only to stocks with derivative contracts available
- Closing price for remaining securities continues to be determined by VWAP of last 30 minutes of CTS
- CAS session structure: 5 minutes reference price calculation, 5 minutes order entry (limit and market orders), 5 minutes order entry (limit orders only), 5 minutes order matching
- Random close between 3:28 PM to 3:30 PM (system-driven)
- Equity derivatives segment continues until 3:40 PM
- Post-close session operates 3:50 PM to 4:00 PM where trades execute at closing price
- Both limit and market orders allowed in CAS
- Market orders cannot be modified/cancelled in the final order entry period (3:25 PM - 3:30 PM)
- CAS also applicable to special trading sessions with same duration structure

## Regulatory Changes

**Closing Price Determination Method:**
- Previous: VWAP of trades executed during last 30 minutes of Continuous Trading Session
- New: Closing price determined through Closing Auction Session for derivative stocks
- Rationale: Aggregates market interest into single liquidity pool, provides fair and transparent closing price, improves execution efficiency for large orders

**Trading Session Structure:**
- CAS operates as separate session post-CTS closure
- Derivatives segment timing unchanged (continues to 3:40 PM)
- Post-close session shifted to 3:50 PM - 4:00 PM (from earlier timing)

**Order Entry Rules in CAS:**
- Session 1 (3:15-3:20 PM): Reference price calculation and transition from CTS
- Session 2 (3:20-3:25 PM): Order entry for both limit and market orders
- Session 3 (3:25-3:30 PM): Order entry only for limit orders; no modification/cancellation for market orders; random close in last 2 minutes
- Session 4 (3:30-3:35 PM): Order matching

**Scope of Application:**
- CAS applies to stocks in cash segment with available derivative contracts
- VWAP method retained for remaining securities in cash segment
- CAS closing price used for derivatives settlement, index computation, mutual fund NAV determination

## Compliance Requirements

**Stock Exchanges:**
- Implement CAS infrastructure and systems for derivative stocks
- Configure 20-minute CAS session with specified timings and phases
- Implement random close mechanism (system-driven) between 3:28 PM - 3:30 PM
- Adjust post-close session timing to 3:50 PM - 4:00 PM
- Ensure CAS applicable to special trading sessions with same duration structure
- Configure order entry rules: both limit/market orders in first entry period, only limit orders in second entry period
- Implement restrictions on market order modification/cancellation in final entry period

**Clearing Corporations:**
- Update settlement systems to use CAS-determined closing prices for derivative stocks
- Coordinate with stock exchanges on CAS implementation

**Market Participants (Brokers, Traders, Investors):**
- Adjust trading strategies and systems for new CAS timing (3:15 PM - 3:35 PM)
- Understand order entry rules and restrictions in different CAS phases
- Note market orders cannot be modified/cancelled after 3:25 PM in CAS
- Plan for random close mechanism between 3:28 PM - 3:30 PM

**Mutual Funds:**
- Update NAV calculation systems to use CAS-determined closing prices for derivative stocks
- Passive funds can utilize CAS to transact at closing price, reducing tracking error

**Index Providers:**
- Update index computation systems to use CAS-determined closing prices for constituent stocks with derivatives

## Important Dates

- Circular Date: January 16, 2026
- Implementation Date: Not specified in the circular (to be announced by stock exchanges)
- Circular Reference: HO/47/11/11(3)2025-MRD-POD2/I/2765/2026

**Daily CAS Timings (Post-Implementation):**
- 3:15 PM - 3:20 PM: Reference price calculation and transition
- 3:20 PM - 3:25 PM: Order entry period (limit and market orders)
- 3:25 PM - 3:30 PM: Order entry period (limit orders only, random close in last 2 minutes)
- 3:28 PM - 3:30 PM: Random close window (system-driven)
- 3:30 PM - 3:35 PM: Order matching
- 3:40 PM: Equity derivatives segment close
- 3:50 PM - 4:00 PM: Post-close session

## Impact Assessment

**Market Structure Impact:**
- High: Fundamental change in closing price determination mechanism for derivative stocks
- Aligns Indian markets with global best practices followed in major jurisdictions
- Aggregates market interest into single liquidity pool at day's end

**Liquidity and Price Discovery:**
- Positive: Improved execution efficiency for large orders through consolidated liquidity
- Enhanced price transparency through auction mechanism
- Fair and transparent closing price reflecting collective market consensus
- Single equilibrium price discovery versus time-weighted average

**Institutional Investors and Passive Funds:**
- High Positive: Passive funds can transact at closing price, reducing tracking error
- Better execution for index rebalancing and portfolio adjustments
- Reduced market impact for large closing orders

**Derivatives Market:**
- Critical: Closing prices used for derivatives settlement become auction-based
- More robust reference price for futures and options settlement
- Derivatives segment continues 10 minutes post-CAS (until 3:40 PM)

**Mutual Funds:**
- Significant: NAV determination for derivative stocks based on CAS closing price
- More reliable and transparent pricing for unit holders
- Potential reduction in NAV computation discrepancies

**Index Computation:**
- Material: Index values at close based on CAS prices for derivative constituents
- Enhanced index integrity and reduced manipulation risk
- Better benchmark reliability for passive products

**Trading Operations:**
- Medium: Extended trading activity window (additional 20 minutes post-CTS)
- Traders need to adapt strategies for CAS participation
- Random close mechanism prevents gaming of auction close time
- Post-close session provides additional execution opportunity at determined closing price

**Technology and Systems:**
- High: Stock exchanges and market participants require system upgrades
- Implementation of auction matching algorithms
- Random close mechanism implementation
- Order management systems need updates for CAS order types and restrictions

**Phased Implementation Consideration:**
- Initially limited to derivative stocks (lower implementation risk)
- VWAP continues for non-derivative stocks (gradual transition)
- Future expansion to all securities likely based on initial phase performance

**Stakeholder Consensus:**
- Decision based on public consultation (December 2024, August 2025)
- Secondary Market Advisory Committee deliberations
- Feedback from stock exchanges, clearing corporations, mutual funds, and FPIs incorporated