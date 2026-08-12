---
category: market-operations
circular_id: c7ce271481a3e645
date: '2026-07-30'
description: NSE Clearing Limited has issued operational guidelines for early pay-in
  of Narmada Agrobase Limited (NARMADA) shares due to a face value split from Rs 10
  to Rs 5.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT75476.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: This circular details critical depository and clearing procedures for
  market participants and custodians to execute early pay-in during a stock split
  transition, involving the handling of old and new ISINs.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT75476.pdf
processing:
  attempts: 1
  content_hash: 6237bee028f8a4c3
  last_updated: '2026-08-12T23:03:20.771515'
  processed_at: '2026-08-12T23:03:11.683480'
  processor_version: '2.0'
  retry_requested_for_stage: claude_failed
  retry_source: backfill
  stage: completed
  status: published
published_date: '2026-07-30T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT75476.pdf
severity: medium
source: nse
stocks:
- NARMADA
tags:
- early-pay-in
- face-value-change
- corporate-action
- split
- narmada
title: NSE Clearing Instruction for Narmada Agrobase Limited Stock Split
---

## Summary

NSE Clearing Limited has issued operational instructions for handling the Early Pay-in (EPI) of securities for Narmada Agrobase Limited (NARMADA). The company is undergoing a face value split (sub-division) from Rs 10/- per share to Rs 5/- per share. Due to this corporate action, ex-date and record date transitions require specific handling of old/existing and new ISINs. Clearing members, custodians, and market participants must execute early pay-in instructions differently depending on the date and settlement number to ensure margin exemption benefits pass correctly.

## Key Points

- **Stock Split Details**: Narmada Agrobase Limited is splitting its face value from Rs 10/- to Rs 5/- per share (1:2 split ratio).
- **ISIN Transition**: The existing/old ISIN is INE117Z01011. Transactions on or after the ex-date/record date will transition to a new ISIN.
- **EPI Execution in Old ISIN**: On July 31, 2026, for Settlement Number 2026143, early pay-in instructions must be executed using the Old ISIN without adjusting for the conversion.
- **EPI Execution in New ISIN**: Starting August 3, 2026, for Settlement Numbers 2026143 and 2026144, early pay-in instructions must be executed in the New ISIN.
- **Client Allocation Guidelines**: For pool account EPI, custodians must upload client-wise allocation details representing the actual traded quantity rather than the converted depository quantity. For EPI through the Block Mechanism, the client-wise allocation file should not be uploaded.

## Regulatory Changes

- **Face Value Subdivision**: Narmada Agrobase Limited (NARMADA) sub-divides its equity shares of Rs 10/- each to Rs 5/- each.
- **Reference Circulars**: This process refers to Item 10.18 of Consolidated Circular NCL/CMPT/73996 dated April 30, 2026 (Early Pay-in of Securities for Margin Exemption), and NCL circular NCL/CMPT/53386 dated August 22, 2022 (Block Mechanism in client demat accounts).

## Compliance Requirements

- **Depository Instructions**: Market participants and custodians must execute early pay-in instructions in the Old ISIN for July 31, 2026. For example, for a sale of 10 shares, early pay-in in the depository should be executed in the Old ISIN for 5 shares.
- **Client Allocation Upload**: Custodians using pool accounts must upload client-wise early pay-in allocation files using the actual traded quantity (e.g., 10 shares) to pass benefits to clients.
- **Block Mechanism Exclusion**: If early pay-in is executed via the block mechanism, the client-wise allocation file should not be uploaded.
- **New ISIN Execution**: Execution of pay-in or early pay-in instructions in the depositories after the record date must use the New ISIN.

## Important Dates

- **Ex-Date**: July 31, 2026
- **Record Date**: July 31, 2026
- **Old ISIN EPI Date**: July 31, 2026 (Settlement: 2026143)
- **New ISIN EPI Date**: August 3, 2026 (Settlements: 2026143 & 2026144)

## Impact Assessment

- **Operational Impact**: Medium. Back-offices, trading terminals, and custodians need to coordinate the dual-ISIN operational cycle carefully. Incorrect execution can result in a failure of margin benefits passing or failed deliveries.
- **System Changes**: Systems must handle the transition from Old ISIN to New ISIN, adjusting EPI ratios (1:2) on the ex-date/record date for settlement and allocation files.
- **Risk Management**: Close adherence to the specified settlement numbers and depository dates is essential to avoid margin penalties or settlement shortfalls.