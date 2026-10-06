---
category: trading
circular_id: 5864e244aea0d9d6
date: '2026-10-06'
description: NSE updates pre-trade risk controls and validation rules between NNF
  IDs and Algo IDs leading to order rejections in the currency derivatives segment.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CD76749.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Introduces additional validation checks between NNF IDs and Algo IDs
  resulting in order rejections, effective October 12, 2026.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CD76749.pdf
processing:
  attempts: 1
  content_hash: cb8fb142fd410bef
  processed_at: '2026-10-06T20:09:15.783265'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-10-06T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CD76749.pdf
severity: medium
source: nse
stocks: []
tags:
- pre-trade-risk
- risk-management
- algo-trading
- nnf-id
- currency-derivatives
- trading-restrictions
- nse
title: Pre-Trade risk controls - Pre-emptive order cancellation on account of NNF
  ID-Algo ID validations - Update
---

## Summary

National Stock Exchange (NSE) has issued an update regarding pre-trade risk controls and pre-emptive order cancellations on account of NNF ID and Algo ID validations in the Currency Derivatives Segment. This circular modifies item no. 1.10 E of the Exchange consolidated circular NSE/CD/73929 dated April 28, 2026, introducing specific additional validations and rejection criteria effective October 12, 2026.

## Key Points

- Introduces specific validation rules linking the 13th digit and first 12 digits of NNF IDs with Algo ID values.
- Orders violating these validation conditions will be rejected, and an order rejection message will be sent to the NNF user.
- Effective date for the new rules is October 12, 2026.
- Members are required to refer to the NNF API protocol (CD version 6.4) for error codes and messages.

## Regulatory Changes

- If the 13th digit in the NNF ID is '0', '2', '4', or '5' and the first 12 digits are '111111111111' or '333333333333', the order will be rejected.
- If the 13th digit in the NNF ID is '1', '3', '5', '6', '7', or '8' and the first 12 digits are '444444444444', the order will be rejected.
- If the first 12 digits of the NNF ID are anything other than '444444444444' and the Algo ID field contains '99999', the order will be rejected.

## Compliance Requirements

Trading members must update their algorithmic trading systems and order routing logic to align with the new NNF ID and Algo ID validation rules to prevent order rejections.

## Important Dates

- **Circular Date:** October 06, 2026
- **Effective Date:** October 12, 2026

## Impact Assessment

Algorithmic traders and trading members operating in the Currency Derivatives Segment must ensure compliance with the updated NNF ID and Algo ID validations to avoid unexpected order rejections during trading sessions starting October 12, 2026.