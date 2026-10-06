---
category: trading
circular_id: 6469e224e24d6655
date: '2026-10-06'
description: NSE issues updates regarding pre-trade risk controls and pre-emptive
  order cancellations based on NNF ID and Algo ID validations in the F&O segment.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP76748.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Introduces additional validation checks between NNF ID and Algo ID
  resulting in order rejections for non-compliance.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP76748.pdf
processing:
  attempts: 1
  content_hash: 5e5086602eabbdc8
  processed_at: '2026-10-06T20:09:49.949834'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-10-06T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP76748.pdf
severity: medium
source: nse
stocks: []
tags:
- futures-and-options
- risk-management
- trading-controls
- nse
title: Pre-Trade Risk Controls - Pre-emptive Order Cancellation on Account of NNF
  ID-Algo ID Validations Update
---

## Summary

National Stock Exchange of India Limited (NSE) has issued a circular in partial modification to item no. 1.16 G regarding pre-emptive order cancellation on account of NNF ID-Algo ID validations in the Futures & Options segment.

## Key Points

- Additional validations introduced between NNF ID and Algo ID resulting in order rejections upon mismatch.
- Rule 1: Orders rejected if 13th digit of NNF ID is '0, 2, 4, or 5' and first 12 digits are '111111111111'.
- Rule 2: Orders rejected if 13th digit of NNF ID is '0, 2, 4, or 5' and first 12 digits are '333333333333'.
- Rule 3: Orders rejected if 13th digit of NNF ID is '1, 3, 5, 6, 7, or 8' and first 12 digits are '444444444444'.
- Rule 4: Orders rejected if first 12 digits of NNF ID are anything other than '444444444444' and Algo ID is '99999'.

## Regulatory Changes

Partial modification of Exchange consolidated circular NSE/FAOP/73928 dated April 28, 2026, adding specific validation criteria between NNF ID and Algo ID across specified digit patterns.

## Compliance Requirements

Trading members must ensure that order messages comply with the updated NNF ID and Algo ID validation rules and refer to the NNF API protocol (FO version 9.51) for error codes and messages.

## Important Dates

- Circular Date: October 06, 2026
- Effective Date: October 12, 2026

## Impact Assessment

Trading systems and algorithmic trading setups must be updated to align with the new pre-trade risk controls to prevent unexpected order rejections from October 12, 2026 onwards.