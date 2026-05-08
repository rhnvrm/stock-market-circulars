---
category: trading
circular_id: e77535ed1ab52cbf
date: '2026-05-08'
description: BSE updates Limit Price Protection (LPP) parameters for BSE FOCUSED IT
  Futures and Options contracts, effective May 11, 2026, with testing available on
  May 9, 2026.
draft: false
guid: https://www.bseindia.com/downloads/UploadDocs/Notices/20260508-30/20260508-30.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Scoped update affecting only BSE FOCUSED IT derivative contracts with
  specific LPP parameter changes; no changes to other index derivatives. Relevant
  primarily to trading members active in BSE FOCUSED IT F&O segment.
pdf_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260508-30/20260508-30.pdf
processing:
  attempts: 1
  content_hash: 01dc9655c72dbda6
  processed_at: '2026-05-08T16:21:26.351626'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-08T13:49:18+00:00'
rss_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260508-30/20260508-30.pdf
severity: medium
source: bse
stocks: []
tags:
- pre-trade-risk-control
- limit-price-protection
- lpp
- derivatives
- equity-derivatives
- futures
- options
- trading-operations
- bse-focused-it
- risk-management
title: Pre-Trade Risk Control - Limit Price Protection (LPP) Update for BSE FOCUSED
  IT Derivatives
---

## Summary

BSE has updated the Limit Price Protection (LPP) parameters for BSE FOCUSED IT Futures and Options contracts under the Pre-Trade Risk Control framework. These parameters take effect from the contract launch day on Monday, May 11, 2026, and will be available for testing in the mock trading session on Saturday, May 9, 2026. No changes have been made to LPP parameters for other index derivatives contracts.

## Key Points

- LPP parameters are specified separately for Options and Futures under BSE FOCUSED IT contracts
- Options LPP: 80% of reference price, subject to a minimum absolute value of ₹80
- Futures LPP: 2% of reference price, subject to a minimum absolute value of ₹200
- LPP range auto-flexing is triggered only when at least 10 orders are rejected due to LPP validation within any 120-second interval, AND those rejections involve a minimum of 3 trading members and at least 5 unique UCCs
- This circular supersedes/updates earlier circulars dated April 5, 2024; April 20, 2024; July 29, 2024; November 28, 2025; and February 13, 2026

## Regulatory Changes

The following LPP parameters are now applicable to BSE FOCUSED IT Futures and Options contracts:

| Instrument Type | LPP% (on Ref. Price) | Minimum Absolute Value |
|---|---|---|
| Options | 80% | ₹80 |
| Futures | 2% | ₹200 |

The auto-flex conditions remain consistent with existing LPP framework logic: minimum 10 rejected orders within 120-second intervals, across at least 3 trading members and 5 unique UCCs. No changes apply to other index derivatives.

## Compliance Requirements

- Trading members dealing in BSE FOCUSED IT Futures and Options must configure their systems to comply with the updated LPP parameters before May 11, 2026
- Members are encouraged to participate in the mock trading session on May 9, 2026 to test system readiness
- No action required for members active only in other index derivative segments

## Important Dates

- **May 9, 2026 (Saturday):** Mock trading session available for testing updated LPP parameters
- **May 11, 2026 (Monday):** Effective date — updated LPP parameters apply from contract launch day for BSE FOCUSED IT derivatives

## Impact Assessment

This update has a moderate operational impact on trading members active in the BSE FOCUSED IT derivatives segment. The relatively wide LPP band for Options (80%) reflects the higher price volatility typical of options contracts, while the tighter 2% band for Futures aligns with standard futures pricing behavior. The auto-flex mechanism provides a safety valve to prevent excessive order rejections during fast-moving markets. Members should review their order management systems ahead of the May 11 launch and leverage the May 9 mock session for validation.