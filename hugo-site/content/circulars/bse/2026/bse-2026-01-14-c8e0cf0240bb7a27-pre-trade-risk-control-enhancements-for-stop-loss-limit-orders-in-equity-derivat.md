---
category: trading
circular_id: c8e0cf0240bb7a27
date: '2026-01-14'
description: BSE introduces new price range validation checks for SL-Limit orders
  in equity derivatives to strengthen pre-trade risk controls and ensure orderly trading.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={0C5DD797-B949-45FF-9E73-A1622A334976}&noticeno=20260114-28&dt=01/14/2026&icount=28&totcount=31&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Mandatory system changes required for all derivatives trading members
  by January 19, 2026. Affects order entry and modification logic for stop-loss limit
  orders with specific validation rules that will reject non-compliant orders.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260114-28&attachedId=
processing:
  attempts: 1
  content_hash: d2f7dcff45a6bb5b
  processed_at: '2026-01-14T12:57:41.460068'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-14T12:26:00+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={0C5DD797-B949-45FF-9E73-A1622A334976}&noticeno=20260114-28&dt=01/14/2026&icount=28&totcount=31&flag=0
severity: high
source: bse
stocks: []
tags:
- derivatives
- trading
- risk-management
- stop-loss-orders
- pre-trade-controls
- futidx
- optidx
title: Pre-Trade Risk Control Enhancements for Stop Loss Limit Orders in Equity Derivatives
---

## Summary

BSE has announced enhancements to pre-trade risk control measures for Stop Loss Limit (SL-Limit) orders in the Equity Derivatives segment. The new rules introduce mandatory price range validation between trigger price and limit price, with specific parameters for different instrument types. Orders exceeding the permissible range will be rejected. The changes become effective January 19, 2026, with testing available on January 17, 2026.

## Key Points

- SL-Limit orders must satisfy price range validation: Abs(limit price - trigger price) <= X% * trigger price
- Different validation parameters apply based on instrument type and trigger price levels
- For FUTIDX: 2% range for trigger price >₹10,000; minimum ₹200 absolute range for trigger price ≤₹10,000
- For OPTIDX: 20% range for trigger price >₹50; minimum ₹10 absolute range for trigger price ≤₹50
- Validation applies to both new order entry and order modification requests
- Non-compliant orders will be rejected with error message: "Stop limit order price range check failed"
- Trading members must test their systems adequately before implementation

## Regulatory Changes

**New SL-Limit Order Validation Rules:**

| Instrument | Trigger Price (₹) | X% Range | Minimum Absolute Range (₹) |
|------------|------------------|----------|---------------------------|
| FUTIDX | ≤10,000 | - | 200 |
| FUTIDX | >10,000 | 2% | - |
| OPTIDX | ≤50 | - | 10 |
| OPTIDX | >50 | 20% | - |

**Validation Formula:** Abs(limit price - trigger price) <= 'X% * trigger price' (subject to minimum absolute range)

**Scope:** Applies to all SL-Limit order entry and modification requests in equity derivatives segment.

## Compliance Requirements

- **Trading Members:** Must update trading systems to comply with new SL-Limit order validation logic
- **System Testing:** Mandatory testing required before live implementation
- **Mock Trading Session:** Available Saturday, January 17, 2026 for testing purposes
- **System Readiness:** Ensure trading systems can handle the new validation checks and error messages
- **Member Education:** Familiarize trading personnel with new order rejection scenarios
- **Risk Controls:** Continue exercising due care and diligence while placing orders as per existing circulars and advisories

## Important Dates

- **January 17, 2026 (Saturday):** Mock trading session for testing available
- **January 19, 2026 (Monday):** Enhancement goes live in production trading

## Impact Assessment

**Operational Impact:**
- High impact on trading systems requiring code changes to implement new validation logic
- All SL-Limit orders in equity derivatives will be subject to mandatory price range checks
- Orders exceeding permissible range will be automatically rejected, requiring resubmission with compliant parameters
- Potential for increased order rejections if traders are not aware of new validation rules

**Market Impact:**
- Strengthens pre-trade risk management framework in derivatives segment
- Reduces potential for erroneous orders with wide price spreads
- Enhances orderly trading by limiting extreme price differences in stop-loss orders
- May require traders to adjust their stop-loss order strategies to comply with new ranges

**Technology Impact:**
- Trading member systems must be modified to handle new validation logic
- Order management systems need updates to process new error messages
- Risk management systems may need recalibration based on new parameters
- Limited testing window (one mock session) requires efficient testing protocols