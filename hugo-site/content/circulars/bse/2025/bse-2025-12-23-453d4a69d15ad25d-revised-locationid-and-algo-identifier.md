---
category: trading
circular_id: 453d4a69d15ad25d
date: '2025-12-23'
description: BSE revises the 14th digit identifier system for Location ID registration
  to distinguish algo and non-algo trading orders, with mandatory compliance by January
  31, 2026.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={86B7A018-8ED2-4E51-9741-EE878AA70171}&noticeno=20251223-22&dt=12/23/2025&icount=22&totcount=48&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Mandatory system update affecting all trading members with strict deadline
  and escalating penalties for non-compliance (Rs 20,000 to Rs 1,00,000 per day)
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251223-22&attachedId=
processing:
  attempts: 1
  content_hash: 7d2691ffaf5d5d2e
  processed_at: '2025-12-23T18:48:17.138865'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-23T12:13:23+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={86B7A018-8ED2-4E51-9741-EE878AA70171}&noticeno=20251223-22&dt=12/23/2025&icount=22&totcount=48&flag=0
severity: high
source: bse
stocks: []
tags:
- algo-trading
- location-id
- dealer-terminal-registration
- order-identifier
- compliance
- penalty
- trading-members
title: Revised Location ID and Algo Identifier - Updated 14th Digit Order Classification
---

## Summary

BSE has revised the 14th digit identifier system used in Location ID registration for dealer terminals. The new classification system better distinguishes between algo and non-algo trading orders. Trading Members must update their Location IDs with the revised 14th digit identifiers by January 31, 2026. Non-compliance with algo order tagging will attract penalties ranging from Rs 20,000 to Rs 1,00,000 per day based on the number of instances.

## Key Points

- Revised 14th digit identifier system replaces old classification for order types
- Digits 1, 2, and 4 (Algo Trading, Algo using SOR, Inter-Exchange Algo) are classified as algo orders
- Comprehensive mapping provided for different user types (ETI, TWS, API, Dealer) and segments
- Vendor Code 99 is applicable for the 14th digit identifier
- Previous notices 20250924-54 and 20250925-4 referenced for context on dealer terminal registration enhancement

## Regulatory Changes

### Old vs Revised 14th Digit Classification

**Old System:**
- 0: No Prog Trading
- 1: Algo Trading
- 2: DMA
- 3: DMA Algo
- 4: SOR
- 5: Hand-Held Device
- 6: SOR with DMA
- 7: SOR DMA with Algo
- 8: Batch

**Revised System:**
- 0: Non Algo Trading
- 1: Algo Trading
- 2: Algo using SOR
- 3: Non Algo SOR
- 4: Inter Exchange Algo
- 5: RMS Square Off
- 6: AMO
- 7: Basket
- 8: (Not specified in content)

### Algo Order Definition
14th digit identifiers 1, 2, and 4 are classified as algo orders.

### User Type Mapping Table

**ETI (User Type 201 onwards):**
- Segments: EQ, EQD, CDX, BCX, EGR
- Application: IBT
- Algo/Non Algo: Non Algo
- Pincode: 111111
- TWS/Branch: 1111
- User ID: 111
- Applicable 14th digits: 0, 3, 6, 7, 8

**TWS (User Type 1-199):**
- Application: STWT (Non Algo) and DMA (Non Algo)
- Pincode: 555555 / 222222
- TWS/Branch: 5555 / 2222
- User ID: 555 / 222
- 14th digits: 0, 3, 6, 7, 8

**DMA CLIENT:**
- Application: DMA (Algo)
- Pincode: 222222
- TWS/Branch: 2222
- User ID: 222
- 14th digits: 1, 2, 4

**DIRECT API:**
- Application: DIRECT (Algo)
- Pincode: 444444
- TWS/Branch: 4444
- User ID: 444
- 14th digits: 1, 2, 4

**DEALER:**
- Application: DEALER (Non Algo / Algo / Non Algo)
- Pincode: Based on actual location
- TWS/Branch: Based on actual branch
- User ID: Based on actual user
- 14th digits: 0, 3, 5, 6, 7, 8 / 1, 2, 4 / 0, 7, 8

## Compliance Requirements

### For Trading Members:

1. **Update Location IDs:** Register dealers with appropriate 14th digit identifier based on order type
2. **Deadline:** Complete all updates by January 31, 2026
3. **Proper Classification:** Ensure dealers are registered with correct 14th digit to avoid non-compliance related to algo orders
4. **Reference Circular:** Review BSE Circular 20251010-4 dated October 10, 2025 regarding penalty rationalization

### Penalty Structure for Non-Compliance:

As per Circular 20251010-4 on non-tagging of unique identifiers for algo orders:
- **First instance:** Rs 20,000 per day
- **After 3 instances:** Rs 50,000 per day
- **After 10 instances:** Rs 1,00,000 per day (for incremental instances)

## Important Dates

- **Notice Date:** December 23, 2025 (Notice No. 20251223-22)
- **Compliance Deadline:** January 31, 2026 (deadline for updating 14th digit identifiers)
- **Reference Notices:**
  - September 24, 2025 (Notice 20250924-54) - Enhancement in dealer terminal registration
  - September 25, 2025 (Notice 20250925-4) - Enhancement in dealer terminal registration
  - October 10, 2025 (Circular 20251010-4) - Penalty rationalization and standardization

## Impact Assessment

### Operational Impact:
- **High:** All Trading Members must review and update their Location ID registration systems
- Requires mapping of all dealer terminals to new 14th digit classification
- System changes needed to ensure proper tagging of algo vs non-algo orders
- Affects multiple user types: ETI, TWS, API users, and dealers across all segments (EQ, EQD, CDX, BCX, EGR)

### Financial Impact:
- Escalating penalty structure creates significant financial risk for non-compliance
- Maximum penalty of Rs 1,00,000 per day after 10 instances of non-compliance
- Creates strong incentive for timely compliance by January 31, 2026

### Market Impact:
- Improved transparency in distinguishing algo and non-algo trading activity
- Better regulatory oversight of algorithmic trading practices
- Standardization of order identification across trading platforms

### Technical Implementation:
- Trading Members need to update dealer terminal registration processes
- Vendor Code 99 applicable for 14th digit identifier implementation
- May require coordination with technology vendors and internal IT systems

**Contact:** Trading Members should contact BSE Helpdesk for clarifications

**Issued by:** Kaushal Mehta (VP - Trading Operations) and Sanjay Pardiwala (DVP - Trading Operations)