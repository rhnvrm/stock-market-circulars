---
category: market-operations
circular_id: 32a132f4a1340861
date: '2026-02-25'
description: CDSL has announced the discontinuation of separate Early Pay-in (EP)
  accounts effective March 21, 2026. Clearing Members will use CM Pool accounts for
  all settlement and EP transactions going forward.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={78F889CB-BCC0-4AF5-B181-455164831C97}&noticeno=20260225-41&dt=02/25/2026&icount=41&totcount=42&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: This operational change affects all DPs, TMs, CMs, and clients across
  all registered stock exchanges and clearing corporations, requiring system and process
  updates by March 21, 2026.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260225-41&attachedId=58e31b12-a59a-4e49-92b4-3eaa4a16d82e
processing:
  attempts: 1
  content_hash: f926b211100bea28
  processed_at: '2026-02-25T16:14:21.008682'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-02-25T15:14:20+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={78F889CB-BCC0-4AF5-B181-455164831C97}&noticeno=20260225-41&dt=02/25/2026&icount=41&totcount=42&flag=0
severity: high
source: bse
stocks: []
tags:
- cdsl
- early-payin
- settlement
- depository-participants
- clearing-members
- cm-pool-account
- equity-segment
- debt-segment
- operational-change
title: Discontinuation of CDSL Early Payin Accounts for Equity and Debt Segment
---

## Summary

CDSL has issued a communiqué (CDSL/OPS/DP/SETTL/2026/122 dated February 19, 2026) announcing the discontinuation of separate Early Pay-in (EP) accounts effective March 21, 2026. After this date, Clearing Members (CMs) will no longer maintain a separate EP account with the Clearing Corporation (CC); instead, all settlement-related and EP transactions will be executed using the CM Pool account.

## Key Points

- Effective March 21, 2026, separate EP accounts will be discontinued for all CMs across all registered Stock Exchanges and Clearing Corporations
- CMs will only need to maintain a CM Pool account (with valid BO Status/BO Sub-status) for all settlement transactions including EP transactions
- EP transactions can continue to be executed via EP accounts until 09:00 PM on March 20, 2026
- After 09:00 PM on March 20, 2026, the CDSL system will not allow new EP transactions on EP accounts
- All in-transit EP transactions with status 'Earmarked' or 'Overdue' will have their EP accounts automatically replaced with the corresponding CM Pool accounts
- No new EP accounts can be opened effective March 21, 2026
- There is no change to the existing DIS format
- NSDL clients executing inter-depository EP transactions must now provide the BOID of the CDSL CM Pool account instead of the EP account

## Regulatory Changes

- CDSL is removing the requirement for CMs to maintain a separate EP account with the CC
- All EP transactions previously executed via EP accounts must now be executed via CM Pool accounts
- Clients/TMs/CMs submitting Delivery Instruction Slips (DIS) must now use the BOID of the CM Pool account as the 'Counter BOID'
- Upload mechanisms (Easiest/WebCDAS), Online setup, eDIS, and APIs must all reference CM Pool accounts instead of EP accounts

## Compliance Requirements

- **DPs/CMs/TMs/Clients**: Execute any pending EP transactions by 09:00 PM on March 20, 2026, or re-enter them using CM Pool accounts from SOD of March 21, 2026
- **CMs**: Coordinate with respective CCs to transfer balances from EP accounts to corresponding CM Pool accounts; EP accounts with remaining balances will have status 'To be Closed' until balance reaches NIL
- **DPs/TMs/CMs**: Update DIS submissions to reference CM Pool account BOID as Counter BOID
- **System/Platform Updates**: Entities using Easiest, WebCDAS, eDIS, or APIs must update configurations to use CM Pool accounts in place of EP accounts
- **NSDL DPs**: Process inter-depository EP transactions with CDSL CM Pool account as the counter account for clients of TMs/CMs

## Important Dates

- **February 19, 2026**: Date of CDSL communiqué
- **March 20, 2026, 09:00 PM**: Last time to execute EP transactions using EP accounts; CDSL will mark all EP accounts for closure before EOD
- **March 20, 2026 EOD**: All NIL balance EP accounts will be automatically closed; remaining EP accounts set to 'To be Closed' status
- **March 21, 2026**: Effective date — EP accounts discontinued; CMs to use CM Pool accounts for all EP and settlement transactions; opening of new EP accounts restricted

## Impact Assessment

This change has a broad and significant operational impact across the market ecosystem. All Depository Participants, Trading Members, Clearing Members, and their clients must update internal workflows, system configurations, and DIS submission processes before March 21, 2026. The shift simplifies account structure by eliminating a separate account type, but requires coordinated action to transfer remaining EP account balances to CM Pool accounts. Entities using automated upload or API-based settlement systems face a technical migration deadline. Failure to comply could disrupt settlement workflows. The change affects both equity and debt segments across all registered stock exchanges and clearing corporations in India.