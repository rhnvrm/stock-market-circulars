---
category: trading
circular_id: 23439d5f1bfbb927
date: '2026-01-14'
description: BSE introduces new pre-trade risk controls for Stop Loss Limit orders
  in equity derivatives, implementing price range checks between trigger and limit
  prices effective January 19, 2026.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={0C5DD797-B949-45FF-9E73-A1622A334976}&noticeno=20260114-28&dt=01/14/2026&icount=28&totcount=44&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Critical system changes affecting all derivative trading members requiring
  mandatory system testing and implementation by January 19, 2026. Non-compliance
  will result in order rejections.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260114-28&attachedId=
processing:
  attempts: 1
  content_hash: cd071ede27b345bd
  processed_at: '2026-01-14T18:47:45.707958'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-14T12:26:00+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={0C5DD797-B949-45FF-9E73-A1622A334976}&noticeno=20260114-28&dt=01/14/2026&icount=28&totcount=44&flag=0
severity: high
source: bse
stocks: []
tags:
- derivatives
- risk-management
- pre-trade-controls
- stop-loss-orders
- trading-rules
- equity-derivatives
- futidx
- optidx
title: Pre-Trade Risk Control – Enhancements for Stop Loss Limit Orders in Equity
  Derivatives
---

## Summary

BSE is implementing enhanced pre-trade risk control measures for Stop Loss Limit (SL-Limit) orders in the Equity Derivatives segment to strengthen risk management and ensure orderly trading. The new mechanism introduces validation checks on the difference between trigger price and limit price, with specific permissible ranges based on instrument type and price levels. Orders exceeding these ranges will be rejected. The changes become effective for live trading from January 19, 2026, with mock trading testing available on January 17, 2026.

## Key Points

- SL-Limit orders must satisfy a new price range validation: Abs(limit price – trigger price) <= 'X% * trigger price' (subject to minimum absolute range)
- For FUTIDX: If trigger price > ₹10,000, permissible range is 2% of trigger price; if ≤ ₹10,000, minimum absolute range is ₹200
- For OPTIDX: If trigger price > ₹50, permissible range is 20% of trigger price; if ≤ ₹50, minimum absolute range is ₹10
- Validation applies to both new order entries and order modification requests
- Rejected orders will receive error message: "Stop limit order price range check failed"
- Trading members must test their systems adequately before implementation

## Regulatory Changes

### New Pre-Trade Validation Rules

The Exchange has introduced mandatory price range checks for SL-Limit orders with the following parameters:

**FUTIDX (Index Futures):**
- Trigger price ≤ ₹10,000: Minimum absolute range of ₹200 applies
- Trigger price > ₹10,000: Maximum 2% difference between trigger and limit price

**OPTIDX (Index Options):**
- Trigger price ≤ ₹50: Minimum absolute range of ₹10 applies
- Trigger price > ₹50: Maximum 20% difference between trigger and limit price

### Scope of Application

- Applies to all incoming SL-Limit order entries
- Applies to SL-Limit order modification requests
- Orders/modifications failing validation will be immediately rejected

### Future Modifications

The Exchange reserves the right to review and implement further improvements or changes based on market experience and participant feedback.

## Compliance Requirements

### For Trading Members

1. **System Updates**: Ensure trading systems are updated to comply with new SL-Limit order validation rules
2. **Testing**: Mandatory participation in mock trading session on January 17, 2026 to test system compatibility
3. **Adequate Testing**: Conduct thorough internal testing before live implementation
4. **Error Handling**: Implement proper error handling for rejection message "Stop limit order price range check failed"
5. **Risk Controls**: Continue to exercise due care and diligence while placing orders as per existing Exchange circulars and advisories
6. **Client Communication**: Inform clients about the new order validation rules to prevent order rejections

## Important Dates

- **January 14, 2026**: Circular issuance date (Notice No 20260114-28)
- **January 17, 2026 (Saturday)**: Mock trading session available for testing
- **January 19, 2026 (Monday)**: Enhancement goes live for actual trading

## Impact Assessment

### Operational Impact

**Trading Members**: High impact requiring immediate system changes and testing. Trading members must modify their order management systems to incorporate the new validation logic before January 19, 2026. Failure to adapt will result in SL-Limit order rejections.

**Market Participants**: Traders using stop loss limit orders in equity derivatives will need to adjust their order placement strategies to ensure compliance with the new price range requirements. Orders with wider spreads between trigger and limit prices may be rejected.

### Risk Management Benefits

- Reduces potential for erroneous orders with extreme price differences
- Enhances pre-trade risk controls in derivatives segment
- Promotes orderly trading by preventing orders with unrealistic price ranges
- Protects against potential fat-finger errors and system glitches

### Market Segment Affected

Equity Derivatives segment only - specifically FUTIDX and OPTIDX instruments. Cash equity segment and other derivative instruments are not affected by these changes.

### Technical Considerations

The two-day window between mock trading (January 17) and live implementation (January 19) is tight. Trading members must prioritize system testing and be prepared for potential order rejections if validation rules are not properly implemented in their systems.