---
category: market-operations
circular_id: 9587f6998cf55fb2
date: '2026-07-30'
description: NSE Clearing Limited outlines the process for handling early pay-in instructions
  for Invesco ETFs (IVZINNIFTY) on account of a face value split (10:1) with a record
  date of July 31, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT75475.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: This circular provides instructions for a specific ETF's stock split
  early pay-in mechanism, ensuring custodians and market participants use the correct
  ISINs during the transition period to avoid settlement discrepancies or loss of
  early pay-in benefits.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT75475.pdf
processing:
  attempts: 1
  content_hash: aa69e07953803923
  last_updated: '2026-08-12T23:16:49.237223'
  processed_at: '2026-08-12T23:16:40.321677'
  processor_version: '2.0'
  retry_requested_for_stage: claude_failed
  retry_source: backfill
  stage: completed
  status: published
published_date: '2026-07-30T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT75475.pdf
severity: medium
source: nse
stocks:
- IVZINNIFTY
tags:
- nse
- early-pay-in
- etf
- invesco
- split
- face-value-change
- corporate-action
- settlement
- mutual-fund
title: Early Pay-in of Securities for ETFs of Invesco Asset Management (India) Private
  Limited
---

## Summary

The NSE Clearing Limited (NCL) has issued a circular detailing the operational process for early pay-in (EPI) of securities for ETFs of Invesco Asset Management (India) Private Limited, specifically for the symbol **IVZINNIFTY** (Existing/Old ISIN: **INF205K01DA9**). This process is necessitated by a corporate action involving a **Face Value Split (Sub-Division)** from Rs 10/- per share to Re 1/- per share. The Record Date and Ex-Date for this corporate action are both set for **July 31, 2026**.

## Key Points

- **Security & Corporate Action**: ETFs of Invesco Asset Management (India) Private Limited (**IVZINNIFTY**), undergoing a face value sub-division from Rs 10/- per share to Re 1/- per share (1:10 ratio).
- **Early Pay-in (EPI) details**:
  - For EPI executed on **July 31, 2026** (Settlement 2026143), the old/existing ISIN (INF205K01DA9) must be used without adjusting for the conversion.
  - For EPI executed on **August 3, 2026** (Settlement 2026143 & 2026144), the new ISIN must be used.
- **EPI Quantity Example**: For a sale quantity of 10 shares, the early pay-in instruction in the depository on the ex-date/record date (July 31, 2026) must be for 1 share in the old ISIN.
- **Block Mechanism Restrictions**: When using the block mechanism in demat accounts of clients under SEBI rules, the client-wise early pay-in allocation file should not be uploaded.
- **Pool Account Client Allocations**: Custodians providing EPI through a pool account must upload client-wise EPI allocation details reflecting the actual traded quantity (e.g., 10 shares instead of 1).
- **Post-Record Date Instructions**: Market participants/custodians must execute pay-in or early-pay in instructions using the new ISIN after the record date in the depositories.

## Regulatory Changes

No new regulatory policy is introduced. Instead, this circular provides operational guidance under existing frameworks, referencing NCL circular NCL/CMPT/73996 (dated April 30, 2026) on Margin Exemption and NCL/CMPT/53386 (dated August 22, 2022) regarding SEBI's Block Mechanism in demat accounts.

## Compliance Requirements

- **Depository Instructions**:
  - Execute EPI in the **Old ISIN** on July 31, 2026, for Settlement 2026143 (at the pre-split ratio: e.g., 1 share for every 10 sold).
  - Execute EPI in the **New ISIN** starting August 3, 2026, for Settlement 2026143 & 2026144.
- **EPI Allocation Files**:
  - Do not upload client-wise early pay-in allocation files if early pay-in is performed via the block mechanism.
  - Upload client-wise EPI allocation details as per the actual traded quantity when providing early pay-in through a pool account.

## Important Dates

- **Ex-Date**: July 31, 2026
- **Record Date**: July 31, 2026
- **EPI in Old ISIN (Settlement 2026143)**: July 31, 2026
- **EPI in New ISIN (Settlement 2026143 & 2026144)**: August 3, 2026

## Impact Assessment

- **Operational Impact**: Medium. Clearing members, custodians, and PCMs must adjust their depository instructions and settlement file submissions depending on whether they are using the block mechanism or a pool account during the ex-date/record date transition.
- **Financial/Margin Impact**: Correctly executing the EPI instructions ensures that members receive margin exemption benefits as per NCL policies. Any mismatch in quantities or ISINs could lead to operational settlement failures or additional margin obligations.