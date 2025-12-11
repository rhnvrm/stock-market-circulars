---
category: market-operations
circular_id: 5335842398034df7
date: '2025-11-26'
description: NSE Clearing notifies members about early pay-in procedures for SIKKO
  securities undergoing face value split from Rs 10/- to Re 1/- with ex-date November
  27, 2025.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT71479.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Affects trading members and custodians dealing with SIKKO securities
  during the face value split period, requiring specific procedural compliance for
  early pay-in to avoid settlement issues.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT71479.pdf
processing:
  attempts: 1
  content_hash: 47375b47921e6b77
  processed_at: '2025-11-26T12:52:06.280313'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-11-26T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT71479.pdf
severity: medium
source: nse
stocks:
- SIKKO
tags:
- corporate-action
- depository
- early-pay-in
- face-value-change
- margin-exemption
- settlement
title: Early Pay-in of Securities for Sikko Industries Limited (SIKKO) - Face Value
  Split
---

## Summary

NSE Clearing Limited has issued instructions regarding early pay-in (EPI) of securities for Sikko Industries Limited (SIKKO) in connection with a face value split from Rs 10/- per share to Re 1/- per share. The corporate action has a record date and ex-date of November 27, 2025. Members and custodians must follow specific procedures for early pay-in using old and new ISINs depending on the settlement date.

## Key Points

- Face value split: Rs 10/- per share to Re 1/- per share (1:10 ratio)
- Old ISIN: INE112X01017
- Record Date and Ex-Date: November 27, 2025
- Settlement Numbers affected: 2025226 (Nov 27), 2025227 (Nov 28)
- Early pay-in on Nov 27 must be done in old ISIN without adjusting for conversion
- Early pay-in on Nov 28 can be done in new ISIN
- For 10 shares sold, early pay-in should be 1 share in old ISIN (pre-split quantity)
- Block mechanism must be used as per SEBI circular requirements
- Client-wise allocation file should NOT be uploaded when using block mechanism
- Custodians using pool accounts must upload client-wise allocation in actual traded quantity

## Regulatory Changes

This circular implements the early pay-in procedures outlined in Item 10.18 'Early Pay-in of Securities for Margin Exemption' of the consolidated circular NCL/CMPT/67751 dated April 29, 2025. Members must also adhere to NCL circular NCL/CMPT/53386 dated August 22, 2022 regarding SEBI's block mechanism in demat accounts for client sale transactions.

## Compliance Requirements

- **Trading Members**: Execute early pay-in instructions in old ISIN (INE112X01017) for November 27, 2025 (settlement 2025226) using pre-split quantity
- **Trading Members**: Use block mechanism for client demat accounts; do not upload client-wise early pay-in allocation file
- **Custodians**: If providing early pay-in through pool account, must upload client-wise allocation details using actual traded quantity (post-split quantity)
- **All Market Participants**: Execute pay-in/early pay-in instructions in new ISIN after the record date (from November 28, 2025 onwards)
- **Example Compliance**: For sale of 10 shares (post-split), early pay-in on November 27 should be 1 share in old ISIN

## Important Dates

| Date | Event | ISIN to Use | Settlement Number |
|------|-------|-------------|-------------------|
| November 27, 2025 | Ex-Date / Record Date | Old ISIN (INE112X01017) | 2025226 |
| November 28, 2025 | Post Record Date | New ISIN or Old ISIN | 2025226 & 2025227 |
| After November 27, 2025 | Normal Operations | New ISIN | Subsequent settlements |

## Impact Assessment

**Operational Impact**: Medium - Requires trading members and custodians to implement split-specific early pay-in procedures for a limited period. Incorrect ISIN usage or quantity adjustments could lead to settlement failures.

**Market Participants Affected**: All trading members, custodians, and PCMs dealing in SIKKO securities during the corporate action period.

**Risk Areas**: 
- Confusion between old and new ISIN usage during transition period
- Incorrect quantity calculation (pre-split vs post-split)
- Improper use of block mechanism and allocation files
- Settlement failures if procedures not followed correctly

**Mitigation**: Clear procedural guidelines provided with specific examples; help desk support available at 18002660050 (Option 2) and securities_ops@nsccl.co.in for clarifications.