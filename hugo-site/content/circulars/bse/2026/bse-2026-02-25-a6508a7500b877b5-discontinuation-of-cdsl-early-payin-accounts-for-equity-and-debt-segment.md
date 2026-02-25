---
category: market-operations
circular_id: a6508a7500b877b5
date: '2026-02-25'
description: CDSL announces discontinuation of separate Early Pay-in (EP) accounts
  effective March 21, 2026, requiring Clearing Members to use CM Pool accounts for
  all settlement transactions including EP transactions.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={78F889CB-BCC0-4AF5-B181-455164831C97}&noticeno=20260225-41&dt=02/25/2026&icount=41&totcount=47&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational change affecting all Clearing Members, DPs, TMs and clients
  who use Early Pay-in accounts for settlement. Requires system and process updates
  but is a managed transition with clear timelines.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260225-41&attachedId=58e31b12-a59a-4e49-92b4-3eaa4a16d82e
processing:
  attempts: 1
  content_hash: f92825c3a6a1f959
  processed_at: '2026-02-25T19:15:13.823188'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-02-25T15:14:20+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={78F889CB-BCC0-4AF5-B181-455164831C97}&noticeno=20260225-41&dt=02/25/2026&icount=41&totcount=47&flag=0
severity: medium
source: bse
stocks: []
tags:
- settlement
- cdsl
- depository
- early-payin
- clearing-members
- cm-pool-account
- depository-participants
- operational-change
title: Discontinuation of CDSL Early Payin Accounts for Equity and Debt Segment
---

## Summary

Central Depository Services (India) Limited (CDSL) has announced the discontinuation of separate Early Pay-in (EP) accounts effective March 21, 2026. All Clearing Members (CMs) will be required to use their CM Pool accounts (with a valid BO Status/BO Sub-status) for executing settlement-related transactions, including EP transactions, eliminating the need to maintain a dedicated EP account.

## Key Points

- Effective March 21, 2026, CMs will no longer be required to maintain a separate Early Pay-in (EP) account with Clearing Corporations.
- CM Pool accounts will replace EP accounts for all settlement transactions including EP transactions.
- EP transactions can be executed using EP accounts only until 09:00 PM on March 20, 2026.
- After the cutoff, all in-transit EP transactions (status: 'Earmarked' and 'Overdue') will have their EP account replaced with the corresponding CM Pool account.
- No change in existing DIS (Delivery Instruction Slip) format.
- Opening of new EP accounts will be restricted in the CDSL system from March 21, 2026.
- For inter-depository EP transactions from NSDL to CDSL, the BOID of the CDSL CM Pool account must be provided instead of the EP account.

## Regulatory Changes

- CDSL Communiqué CDSL/OPS/DP/SETTL/2026/122 dated February 19, 2026 mandates consolidation of EP accounts into CM Pool accounts.
- The requirement for CMs to maintain a separate EP account with Clearing Corporations is being removed.
- Clients, TMs, and CMs must reference the BOID of the CM Pool account as 'Counter BOID' in Delivery Instruction Slips going forward.
- No changes to existing block mechanism guidelines for respective market types.

## Compliance Requirements

- **DPs / CMs / TMs / Clients**: Complete all EP transactions via existing EP accounts before 09:00 PM on March 20, 2026.
- **DPs**: Enter any pending EP transactions after SOD of March 21, 2026 using 'CM Pool account' in place of 'EP account'.
- **CMs**: Coordinate with respective Clearing Corporations to transfer balances from EP accounts to corresponding CM Pool accounts.
- **All participants using upload/online/eDIS/API mechanisms** (Easiest / WebCDAS): Use CM Pool account in place of EP account effective March 21, 2026.
- **TMs/CMs with NSDL client accounts**: Provide BOID of CDSL CM Pool account in DIS submitted to NSDL DP for inter-depository EP transactions.

## Important Dates

- **February 19, 2026**: CDSL Communiqué issued (CDSL/OPS/DP/SETTL/2026/122).
- **March 20, 2026, 09:00 PM**: Deadline for executing EP transactions via existing EP accounts; CDSL system will not allow new EP transaction setup after this time.
- **March 20, 2026 (EOD)**: All EP accounts marked for closure; NIL balance EP accounts closed during EOD processing.
- **March 21, 2026**: Effective date — EP accounts discontinued; CM Pool accounts to be used for all EP and settlement transactions; opening of new EP accounts restricted.

## Impact Assessment

This change affects all Depository Participants, Trading Members, Clearing Members, and their clients across all registered Stock Exchanges and Clearing Corporations. The transition simplifies the settlement infrastructure by consolidating EP functionality into existing CM Pool accounts, reducing operational overhead. Entities using automated systems (Easiest, WebCDAS, APIs, eDIS) will need to update their configurations to reference CM Pool account BOIDs instead of EP account BOIDs. EP accounts with non-NIL balances after March 20, 2026 will remain in a 'To be Closed' status (accepting only Corporate Action credits) until balances are transferred, requiring CMs to actively coordinate with their respective Clearing Corporations to complete the transition.