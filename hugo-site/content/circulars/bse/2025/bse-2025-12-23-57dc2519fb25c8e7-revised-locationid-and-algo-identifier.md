---
category: trading
circular_id: 57dc2519fb25c8e7
date: '2025-12-23'
description: BSE revises the 14th digit order identifier for dealer terminal registration,
  requiring Trading Members to update Location IDs by January 31, 2026 to avoid penalties.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={86B7A018-8ED2-4E51-9741-EE878AA70171}&noticeno=20251223-22&dt=12/23/2025&icount=22&totcount=44&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Mandatory compliance requirement affecting all Trading Members with
  strict deadline and significant penalty structure (up to Rs. 1,00,000 per day) for
  non-compliance in algo order tagging.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251223-22&attachedId=
processing:
  attempts: 1
  content_hash: 45bf398aaf338c7d
  processed_at: '2025-12-23T15:41:31.166800'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-23T12:13:23+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={86B7A018-8ED2-4E51-9741-EE878AA70171}&noticeno=20251223-22&dt=12/23/2025&icount=22&totcount=44&flag=0
severity: high
source: bse
stocks: []
tags:
- trading-operations
- algo-trading
- compliance
- dealer-terminals
- location-id
- order-identifier
- penalties
title: Revised Location ID and Algo Identifier for Trading Members
---

## Summary

BSE has revised the 14th digit identifier system for dealer terminal registration. Trading Members must update their Location IDs by January 31, 2026. The revision clarifies algo order identification, where digits 1 (Algo Trading), 2 (Algo using SOR), and 4 (Inter-Exchange Algo) are considered algo orders. Non-compliance with algo order tagging will result in escalating penalties starting at Rs. 20,000 per day and reaching Rs. 1,00,000 per day after 10 instances.

## Key Points

- Revised 14th digit identifier replaces old system for order type classification
- Digit 0: Non Algo Trading (previously No Prog Trading)
- Digit 1: Algo Trading (unchanged)
- Digit 2: Algo using SOR (previously DMA)
- Digit 3: Non Algo SOR (previously DMA Algo)
- Digit 4: Inter Exchange Algo (previously SOR)
- Digit 5: RMS Square Off (previously Hand-Held Device)
- Digit 6: AMO (previously SOR with DMA)
- Digit 7: Basket (previously SOR DMA with Algo)
- Digit 8: Not specified in old system
- Digits 1, 2, and 4 are specifically classified as algo orders
- Vendor code 99 applicable for algo identifiers

## Regulatory Changes

The Exchange has modified the Location ID registration framework to enhance dealer terminal tracking. The new system provides clearer distinction between algo and non-algo trading types. This follows previous notices 20250924-54 (September 24, 2025) and 20250925-4 (September 25, 2025) regarding dealer terminal registration enhancements.

Detailed mapping provided for different user types (IBT, STWT, DMA, etc.) across segments (EQ, EQD, CDX, BCX, EGR) with specific pincode and TWS/Branch assignments.

## Compliance Requirements

Trading Members must:

1. Update the 14th digit order identifier for all dealer terminals by January 31, 2026
2. Ensure dealers are registered with appropriate 14th digit to avoid algo order non-compliance
3. Properly tag algo orders using identifiers 1, 2, or 4
4. Refer to the provided reference table for Location ID registration based on user type, application type, and segment
5. Contact BSE Helpdesk for clarifications

## Important Dates

- **Notice Date:** December 23, 2025
- **Compliance Deadline:** January 31, 2026
- **Reference Circulars:** September 24, 2025 (20250924-54), September 25, 2025 (20250925-4), October 10, 2025 (20251010-4)

## Impact Assessment

**Operational Impact:** All Trading Members must review and update their dealer terminal registrations across all segments. This requires coordination between trading operations, technology teams, and compliance departments.

**Financial Impact:** Non-compliance carries severe financial penalties:
- Rs. 20,000 per day for initial instances
- Rs. 50,000 per day after 3 instances
- Rs. 1,00,000 per day after 10 instances (for incremental instances)

**Compliance Risk:** Trading Members face significant penalty exposure if they fail to properly tag algo orders or miss the January 31, 2026 deadline. The escalating penalty structure emphasizes the importance of timely compliance.

**Market Impact:** The revision aims to improve order tracking, enhance regulatory oversight of algorithmic trading, and standardize identification across different trading platforms and segments.