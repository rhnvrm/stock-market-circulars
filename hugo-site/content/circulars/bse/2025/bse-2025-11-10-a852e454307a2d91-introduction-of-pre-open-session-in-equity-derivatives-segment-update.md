---
category: market-operations
circular_id: a852e454307a2d91
date: '2025-11-10'
description: BSE introduces a 15-minute pre-open session (9:00-9:15 AM) for equity
  derivatives futures contracts, with specific eligibility criteria and order matching
  procedures.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={6374395E-D31E-4BD2-8B2C-7792354A1A6D}&noticeno=20251110-40&dt=11/10/2025&icount=40&totcount=60&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Introduces significant structural change to equity derivatives trading
  with new session timings and order matching procedures affecting all derivative
  market participants
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251110-40&attachedId=264eaff3-83ea-4818-9226-dfa3e7bbf701
processing:
  attempts: 1
  content_hash: 3bdc0472d4f40b77
  processed_at: '2025-11-10T18:41:39.358089'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-11-10T14:02:03+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={6374395E-D31E-4BD2-8B2C-7792354A1A6D}&noticeno=20251110-40&dt=11/10/2025&icount=40&totcount=60&flag=0
severity: high
source: bse
stocks: []
tags:
- derivatives
- trading-session
- pre-open
- futures
- index-futures
- stock-futures
- market-operations
- order-matching
title: Introduction of Pre-Open Session in Equity Derivatives Segment – Update
---

## Summary

BSE has introduced a pre-open session in the Equity Derivatives Segment operating from 9:00 AM to 9:15 AM. The session applies to current-month futures contracts on both Indices and Single Stocks. During the last five trading days before expiry, next-month futures contracts are also included. Calendar spread futures and all option contracts are excluded. The continuous trading session will commence at 9:15 AM after the pre-open session ends.

## Key Points

- Pre-open session duration: 15 minutes (9:00 AM - 9:15 AM)
- Eligible contracts: Current-month Index and Stock futures; next-month futures during last 5 trading days before expiry
- Excluded contracts: Calendar spread futures and all option contracts
- Only Limit Orders and Market Orders permitted during pre-open
- Special orders (displayed quantity, stop loss) not allowed
- Order entry period: 9:00 AM - 9:07/08 AM with random system stoppage
- Order matching period: 9:08 AM - 9:12 AM
- Buffer period: 9:12 AM - 9:15 AM
- Continuous trading starts: 9:15 AM for all derivative contracts

## Session Structure

### Order Entry Period (9:00 AM - 9:07/08 AM)
- Order addition, modification, and cancellation allowed
- System-driven random stoppage between 7th and 8th minutes
- No trades executed during this period
- Dissemination of Indicative Price and Matchable Quantity

### Order Matching Period (9:08 AM - 9:12 AM)
- Starts immediately after order entry period completion
- Opening price determination through volume maximization logic
- Order matching and trade confirmation
- No order modifications or cancellations allowed

### Buffer Period (9:12 AM - 9:15 AM)
- Facilitates transition to continuous trading session
- No order addition, modification, or cancellation permitted

## Order Types and Priority

- **Permitted**: Limit Orders, Market Orders, End of Session orders, IOC orders
- **Not Permitted**: Displayed quantity orders, Stop loss orders
- **Execution Priority**: Limit orders get priority over market orders
- **Market Order Execution**: If no limit orders exist, all market orders execute at last closing price
- **Modification/Cancellation**: Only allowed during first 7-8 minutes of order entry period

## Opening Price Discovery Mechanism

Opening price determined using volume maximization logic with three-tier criteria:

1. **Primary**: Price at which maximum quantity is tradable
2. **Secondary**: Price with minimum absolute order imbalance (if multiple prices have same maximum quantity)
3. **Tertiary**: Price closest to previous day's closing price (if multiple prices have same order imbalance)

## Contract Identification

New field added to market data files to identify eligible contracts:

**File**: EQD_CODDMMYY.csv, EQD_CO_abr_DDMMYY.csv, EQD_INDEX_CODDMMYY.csv
- **Field Name**: Pre-Open session Indicator
- **Values**: "0" = Not in Pre-Open session, "1" = In Pre-Open session

**File**: BSE_EQD_CONTRACT_DDMMYYYY.csv, BSE_EQD_CONTRACT_abr_DDMMYYYY.csv
- **Field Name**: Pre-Open session Indicator
- **Values**: "0" = Not in Pre-Open session, "1" = In Pre-Open session

## Important Dates

- Effective immediately upon circular implementation
- Next-month futures included in pre-open during last 5 trading days before current-month contract expiry

## Impact Assessment

### Market Impact
- Enhanced price discovery mechanism for derivatives opening prices
- Reduced volatility at market open through structured order matching
- Improved transparency with indicative price dissemination during order entry period

### Operational Impact
- Trading members must adjust systems to handle new session timings
- Market data feeds will include new pre-open session indicator field
- Order management systems need updates to restrict special orders during pre-open
- Traders must adapt strategies for 9:15 AM continuous session start instead of 9:00 AM

### Participant Impact
- All equity derivatives market participants affected
- Option traders unaffected as options remain excluded from pre-open
- Calendar spread traders continue with 9:15 AM session start