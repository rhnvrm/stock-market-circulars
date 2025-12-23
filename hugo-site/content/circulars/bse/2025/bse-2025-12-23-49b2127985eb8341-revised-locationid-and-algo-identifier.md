---
category: trading
circular_id: 49b2127985eb8341
date: '2025-12-23'
description: BSE revises the 14th digit identifier for dealer terminal registration
  to distinguish algo and non-algo orders, with mandatory compliance by January 31,
  2026, and penalties for non-compliance.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={86B7A018-8ED2-4E51-9741-EE878AA70171}&noticeno=20251223-22&dt=12/23/2025&icount=22&totcount=24&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Critical operational change affecting all trading members with strict
  compliance deadline and significant penalties (up to Rs. 1,00,000 per day) for non-compliance
  with algo order tagging requirements.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251223-22&attachedId=
processing:
  attempts: 1
  content_hash: 4cbd7c2054c235a7
  processed_at: '2025-12-23T12:48:33.305751'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-23T12:13:23+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={86B7A018-8ED2-4E51-9741-EE878AA70171}&noticeno=20251223-22&dt=12/23/2025&icount=22&totcount=24&flag=0
severity: high
source: bse
stocks: []
tags:
- algo-trading
- compliance
- dealer-terminals
- location-id
- order-identifier
- penalties
- trading-operations
title: Revised Location ID and Algo Order Identifier - 14th Digit Classification
---

## Summary

BSE has revised the 14th digit identifier system used in dealer terminal Location IDs to better classify algo and non-algo trading orders. Trading Members must update their Location IDs by January 31, 2026. The 14th digits 1, 2, and 4 are now designated for algo orders (Algo Trading, Algo using SOR, and Inter-Exchange Algo respectively), while other digits indicate non-algo orders. Non-compliance with proper algo order tagging will result in escalating penalties starting at Rs. 20,000 per day and reaching Rs. 1,00,000 per day after 10 instances.

## Key Points

- Revision of 14th digit identifier in Location ID registration for dealer terminals
- Three specific digits (1, 2, 4) designated as algo order identifiers
- Mandatory update deadline: January 31, 2026
- Escalating penalty structure for non-compliance with algo order tagging
- Different Location ID formats for various user types (IBT, STWT, DMA, etc.)
- Supersedes previous notices dated September 24 and 25, 2025

## Regulatory Changes

### Revised 14th Digit Classification

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

**New System:**
- 0: Non Algo Trading
- 1: Algo Trading
- 2: Algo using SOR
- 3: Non Algo SOR
- 4: Inter Exchange Algo
- 5: RMS Square Off
- 6: AMO
- 7: Basket
- 8: (Reserved)

### Algo Order Definition

The following 14th digit identifiers are classified as algo orders:
- 1: Algo Trading
- 2: Algo using SOR
- 4: Inter-Exchange Algo

### Location ID Structure by User Type

| User Type | TWS | Segment | Application Type | Algo/Non-Algo | Pincode | TWS/Branch | User ID | Applicable 14th Digits |
|-----------|-----|---------|------------------|---------------|---------|------------|---------|------------------------|
| IBT | 201+ | EQ/EQD/CDX/BCX/EGR | STWT | Non Algo | 111111 | 1111 | 111 | 0,3,6,7,8 |
| DMA | 201+ | EQ/EQD/CDX/BCX/EGR | DMA | Non Algo | 555555 | 5555 | 555 | 0,3,6,7,8 |
| DMA CLIENT | 201+ | EQ/EQD/CDX/BCX/EGR | DMA | Non Algo | 222222 | 2222 | 222 | 0,3,6,7,8 |
| DIRECT API | 201+ | EQ/EQD/CDX/BCX/EGR | DEALER | Algo | 222222 | 2222 | 222 | 1,2,4 |
| DEALER | 201+ | EQ/EQD/CDX/BCX/EGR | DEALER | Algo | 444444 | 4444 | 444 | 1,2,4 |
| DEALER | 1-199 | EQ/EQD/CDX/BCX/EGR | DEALER | Non Algo | Pincode | TWS/Branch | User ID | 0,3,5,6,7,8 |
| DEALER | 1-199 | EQ/EQD/CDX/BCX/EGR | DEALER | Algo | Pincode | TWS/Branch | User ID | 1,2,4 |
| DEALER | ETI/TWS | EQ/EQD/CDX/BCX/EGR | DEALER | Non Algo | Pincode | TWS/Branch | User ID | 0,7,8 |

Applicable Vendor Code: 99

## Compliance Requirements

### For Trading Members

1. **Update Location IDs:** Register dealer terminals with appropriate 14th digit identifier based on trading type (algo vs non-algo)
2. **Compliance Deadline:** Complete all Location ID updates by January 31, 2026
3. **Proper Classification:** Ensure all algo orders use digits 1, 2, or 4 in the 14th position
4. **Avoid Non-Compliance:** Properly tag unique identifiers for algo orders to avoid penalties
5. **Reference Materials:** Use the provided table for Location ID registration guidance
6. **Contact Helpdesk:** Reach out for clarifications on implementation

### Penalty Structure (per Circular 20251010-4)

For non-compliance related to non-tagging of unique identifiers for algo orders:
- **First instances:** Rs. 20,000 per day
- **After 3 instances:** Rs. 50,000 per day
- **After 10 instances:** Rs. 1,00,000 per day (for incremental instances)

## Important Dates

- **Circular Date:** December 23, 2025
- **Compliance Deadline:** January 31, 2026 (mandatory update of 14th digit order identifier)
- **Reference Notices:** September 24, 2025 (Notice 20250924-54) and September 25, 2025 (Notice 20250925-4)
- **Penalty Circular:** October 10, 2025 (Circular 20251010-4)

## Impact Assessment

### Operational Impact

**High Impact on Trading Members:**
- All Trading Members must review and update their dealer terminal registrations
- Requires coordination across operations, compliance, and technology teams
- System changes may be needed to ensure correct 14th digit assignment
- Approximately 5 weeks until mandatory compliance deadline

### Technology Impact

- Order management systems must correctly populate the 14th digit based on order type
- Risk management systems need to validate algo order classification
- Trading platforms must support the new identifier scheme
- Testing required to ensure proper implementation before deadline

### Compliance Risk

**Significant Financial Penalties:**
- Daily penalties can escalate quickly to Rs. 1,00,000 per day
- Multiple dealer terminals increase compliance complexity
- Non-compliance tracking is cumulative across instances
- Financial impact can be substantial for firms with high trading volumes

### Market Impact

- Better regulatory oversight of algorithmic trading activity
- Improved market surveillance capabilities for BSE
- Enhanced transparency in distinguishing algo vs non-algo orders
- Standardization aligns with industry best practices

### Segments Affected

- Equity (EQ)
- Equity Derivatives (EQD)
- Currency Derivatives (CDX)
- Bond Currency Exchange (BCX)
- Electronic Gold Receipts (EGR)