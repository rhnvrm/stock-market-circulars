---
category: trading
circular_id: d8b53ad1dfc6b9a3
date: '2026-01-14'
description: BSE introduces new pre-trade risk control measures for SL-Limit orders
  in equity derivatives, implementing price range checks between trigger and limit
  prices effective January 19, 2026.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={0C5DD797-B949-45FF-9E73-A1622A334976}&noticeno=20260114-28&dt=01/14/2026&icount=28&totcount=42&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Mandatory system changes required by all trading members with direct
  impact on order entry and modification logic for derivatives trading. Failed implementation
  will result in order rejections starting January 19, 2026.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260114-28&attachedId=
processing:
  attempts: 1
  content_hash: f4f7cb967a052710
  processed_at: '2026-01-14T15:42:39.778990'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-14T12:26:00+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={0C5DD797-B949-45FF-9E73-A1622A334976}&noticeno=20260114-28&dt=01/14/2026&icount=28&totcount=42&flag=0
severity: high
source: bse
stocks: []
tags:
- derivatives
- trading
- risk-management
- stop-loss-orders
- pre-trade-controls
- equity-derivatives
- futures
- options
title: Pre-Trade Risk Control – Enhancements for Stop Loss Limit Orders in Equity
  Derivatives Segment
---

## Summary

BSE is implementing enhanced pre-trade risk control measures for Stop Loss Limit (SL-Limit) orders in the Equity Derivatives segment. The new mechanism validates that the difference between trigger price and limit price remains within permissible ranges based on instrument type and price levels. Orders or modifications exceeding these ranges will be rejected. The changes go live on January 19, 2026, with mock trading available on January 17, 2026.

## Key Points

- New validation check for SL-Limit orders: difference between trigger price and limit price must be within permissible range
- Permissible range formula: Abs(limit price – trigger price) <= 'X% * trigger price' (subject to minimum absolute range)
- For FUTIDX: ≤₹10,000 trigger price has ₹200 minimum range; >₹10,000 has 2% range
- For OPTIDX: ≤₹50 trigger price has ₹10 minimum range; >₹50 has 20% range
- Applies to both new order entry and order modification requests
- Rejection error message: "Stop limit order price range check failed"
- Trading members must test their systems adequately before implementation

## Regulatory Changes

### New Order Validation Parameters

**Index Futures (FUTIDX):**
- Trigger price ≤ ₹10,000: Minimum absolute range = ₹200
- Trigger price > ₹10,000: X% = 2% of trigger price

**Index Options (OPTIDX):**
- Trigger price ≤ ₹50: Minimum absolute range = ₹10
- Trigger price > ₹50: X% = 20% of trigger price

### Scope of Application

- Incoming SL-Limit order entry requests
- SL-Limit order modification requests
- Orders exceeding permissible range will be rejected at pre-trade stage

## Compliance Requirements

### For Trading Members

1. **System Updates**: Modify order management systems to comply with new validation rules
2. **Testing**: Participate in mock trading session on January 17, 2026
3. **Adequate Testing**: Ensure thorough testing of systems before live implementation
4. **Risk Controls**: Review and update pre-trade risk control mechanisms
5. **Due Diligence**: Exercise care and diligence while placing orders as per Exchange circulars and advisories

### Error Handling

- Systems must be prepared to handle rejection message: "Stop limit order price range check failed"
- Implement appropriate error handling and user notification mechanisms

## Important Dates

- **January 14, 2026**: Circular issued (Notice No 20260114-28)
- **January 17, 2026 (Saturday)**: Mock trading session for testing
- **January 19, 2026 (Monday)**: Enhancement goes live for regular trading

## Impact Assessment

### Market Impact

- **High operational impact** on all derivatives trading members
- Mandatory system changes required across all trading platforms
- Orders with wide spread between trigger and limit prices will be rejected
- May affect algorithmic trading strategies using wide SL-Limit ranges

### Risk Management Benefits

- Strengthens pre-trade risk controls in derivatives segment
- Prevents erroneous orders with unrealistic price gaps
- Enhances orderly trading and effective risk management
- Reduces potential for fat-finger errors or system glitches

### Implementation Considerations

- Trading members must update order entry systems before January 19, 2026
- Clients using direct market access or algorithmic trading need to adjust their strategies
- Exchange may review and implement further improvements based on market feedback
- Non-compliance will result in automatic order rejections affecting trading operations