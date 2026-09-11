---
category: compliance
circular_id: e8b451aad1300db5
date: '2025-07-25'
description: NSE circular detailing enhancements and updated validation specifications
  for Unique Client Code (UCC) and Unique Client Identifier (UCI) bulk uploads across
  all segments.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/ISC76299.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Updates file structures, formats, and validation rules for Unique Client
  Code (UCC) bulk uploads, affecting broker operations and compliance systems.
pdf_url: https://nsearchives.nseindia.com/content/circulars/ISC76299.zip
processing:
  attempts: 1
  content_hash: 320a298403cfc98d
  processed_at: '2026-09-11T16:16:31.939533'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-09-11T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/ISC76299.zip
severity: medium
source: nse
stocks: []
tags:
- ucc
- unique-client-code
- uci
- unique-client-identifier
- compliance
- kyc
- market-operations
title: Enhancement of Validations in Unique Client Code Fields
---

## Summary

NSE has issued a circular regarding the enhancement of validations in Unique Client Code (UCC) fields and the introduction of new bulk upload file structures for all segments. The file format is pipe-delimited and includes specific validations for account types (OWN, ERROR, CLIENT), UPI options, and segment mappings.

## Key Points

- File naming convention specified as `UCI_YYYYMMDD.Tnn` where T is the File Indicator and nn is the batch number (01 to 99).
- Detailed specifications for control records and detail records including account type rules.
- Specific handling for 'OWN' and 'ERROR' account types where the PAN must belong to the trading member.
- Segment-specific validation rules covering Cash Market, F&O, Currency Derivatives, SLB, Debt, and Commodity segments.

## Regulatory Changes

- Enhanced validation logic for Unique Client Code (UCC) and Unique Client Identifier (UCI) records.
- Standardized account type definitions and restrictions for proprietary and error trades.

## Compliance Requirements

Trading members must update their back-office and compliance systems to align with the new UCC file formats, control record structures, and field-level validation criteria.

## Important Dates

Refer to the specific implementation timeline provided in the circular and accompanying annexures.

## Impact Assessment

Trading members and clearing members must ensure their order management and client onboarding systems adhere to the revised UCC validation criteria to avoid upload rejections.