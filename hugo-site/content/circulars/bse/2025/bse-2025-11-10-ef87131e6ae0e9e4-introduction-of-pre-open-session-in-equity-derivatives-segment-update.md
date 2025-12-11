---
category: market-operations
circular_id: ef87131e6ae0e9e4
date: '2025-11-10'
description: BSE introduces pre-open session for equity derivatives futures contracts
  with detailed FAQs on eligible contracts, timings, order types, and price discovery
  mechanism.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={6374395E-D31E-4BD2-8B2C-7792354A1A6D}&noticeno=20251110-40&dt=11/10/2025&icount=40&totcount=56&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Introduces significant change to derivatives trading mechanism affecting
  all market participants. New pre-open session impacts order placement strategies,
  price discovery, and trading workflows for all equity derivatives traders.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251110-40&attachedId=264eaff3-83ea-4818-9226-dfa3e7bbf701
processing:
  attempts: 1
  content_hash: 20ca9dc9c2896053
  processed_at: '2025-11-10T15:34:20.141625'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-11-10T14:02:03+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={6374395E-D31E-4BD2-8B2C-7792354A1A6D}&noticeno=20251110-40&dt=11/10/2025&icount=40&totcount=56&flag=0
severity: high
source: bse
stocks: []
tags:
- derivatives
- futures-options
- market-operations
- pre-open-session
- price-discovery
- trading-operations
title: Introduction of Pre-Open Session in Equity Derivatives Segment – Update
---

## Summary

BSE has introduced a pre-open session for equity derivatives segment covering current-month futures contracts on indices and single stocks. The 15-minute session runs from 9:00 AM to 9:15 AM, followed by continuous trading at 9:15 AM. During the last five trading days before expiry, next-month futures contracts are also included. Calendar spread futures and all option contracts are excluded from the pre-open session.

## Key Points

- Pre-open session timing: 9:00 AM to 9:15 AM (15 minutes duration)
- Applicable to current-month futures on indices and single stocks
- Next-month futures included during last 5 trading days before expiry
- Calendar spread futures and all options excluded from pre-open
- Only limit orders and market orders allowed; limit orders get priority
- Order entry period: 9:00 AM to 9:07/08 AM (random stoppage between 7th & 8th minute)
- Order matching period: 9:08 AM to 9:12 AM
- Buffer period: 9:12 AM to 9:15 AM
- Continuous trading starts at 9:15 AM for all derivatives contracts
- Special orders (displayed quantity, stop loss) not allowed
- Pre-open indicator added to contract files (field values: 0 or 1)

## Regulatory Changes

**Session Structure:**
- New pre-open session introduced before continuous trading
- Three distinct phases: Order Entry Period, Order Matching & Confirmation Period, and Buffer Period
- System-driven random stoppage between 7th and 8th minute of order entry period

**Contract Eligibility:**
- Current-month index futures and stock futures eligible
- Next-month futures eligible only during last 5 trading days before current-month expiry
- Calendar spread futures and all option contracts (index and stock) excluded

**Order Types:**
- Only limit orders and market orders permitted
- End of session (EOS) and Immediate or Cancel (IOC) orders allowed
- Displayed quantity orders not allowed
- Stop loss orders not allowed

**Data Feed Changes:**
- New field added to contract files: "Pre-Open session Indicator"
- Files affected: EQD_CODDMMYY.csv, EQD_CO_abr_DDMMYY.csv, EQD_INDEX_CODDMMYY.csv, BSE_EQD_CONTRACT_DDMMYYYY.csv, BSE_EQD_CONTRACT_abr_DDMMYYYY.csv
- Field values: 0 (not in pre-open), 1 (in pre-open)

## Compliance Requirements

**Trading Members:**
- Update trading systems to handle pre-open session orders
- Implement order type restrictions (reject displayed quantity and stop loss orders)
- Modify order placement logic to accommodate pre-open timings
- Update contract file parsing to read new pre-open indicator field
- Train dealers on new session timings and order rules

**System Updates:**
- Ensure order management systems support pre-open session workflow
- Implement controls to prevent order modification/cancellation after 9:08 AM
- Update risk management systems for pre-open price volatility
- Modify front-end systems to display indicative price and matchable quantity during matching period

**Order Management:**
- Orders can be added/modified/cancelled only during 9:00 AM to 9:07/08 AM
- No order modifications allowed from 9:08 AM to 9:15 AM
- Market orders will execute at last closing price if no limit orders exist

## Important Dates

- **Effective Date:** Not explicitly mentioned in the circular (marked as "Update")
- **Session Timing:** Daily from 9:00 AM to 9:15 AM
- **Continuous Trading Start:** 9:15 AM onwards
- **Next-month contract inclusion:** Last 5 trading days before current-month expiry

## Impact Assessment

**Market Impact:**
- Enhanced price discovery mechanism at market opening for futures contracts
- Reduced volatility at market open through structured pre-open session
- Better transparency with dissemination of indicative price and matchable quantity
- Improved order matching efficiency through volume maximization logic

**Operational Impact:**
- Trading members need significant system upgrades to support pre-open functionality
- Modified trading workflows for dealers and algorithms
- Risk management systems need recalibration for pre-open price movements
- Data vendors must update feeds to incorporate new pre-open indicator field

**Price Discovery Mechanism:**
- Opening price determined through volume maximization logic:
  1. Price with maximum tradable quantity
  2. If tie, price with minimum absolute order imbalance
  3. If still tied, price closest to previous day's closing price
- Limit orders prioritized over market orders
- Market orders execute at last closing price if no limit orders present

**Trading Strategy Impact:**
- Traders can gauge market sentiment during indicative price dissemination (9:08-9:12 AM)
- Algorithm trading strategies need adjustment for pre-open participation
- Reduced market impact for large orders placed during pre-open
- Better execution quality for opening trades