---
category: market-operations
circular_id: bb20f316b94612bc
date: '2026-02-20'
description: CDSL announces discontinuation of separate Early Pay-in (EP) accounts
  for Clearing Members effective March 21, 2026. CMs will only need to maintain a
  CM Pool account for all settlement-related transactions including EP transactions.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT72920.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational change affecting Clearing Members, Depository Participants,
  and Trading Members; requires system and process updates before March 21, 2026 deadline
  but does not alter market fundamentals or trading rules.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT72920.zip
processing:
  attempts: 1
  content_hash: 75d721cb5204156f
  processed_at: '2026-02-20T17:08:16.710569'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-02-20T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT72920.zip
severity: medium
source: nse
stocks: []
tags:
- settlement
- cdsl
- clearing-member
- early-payin
- depository
- slb
- cm-pool-account
- operational-change
title: Discontinuation of Separate Clearing Member Pool and EPI Account in CDSL for
  SLB - Update
---

## Summary

CDSL has issued a communiqué (CDSL/OPS/DP/SETTL/2026/122) announcing the discontinuation of separate Early Pay-in (EP) accounts for Clearing Members effective March 21, 2026. From this date, CMs will only be required to maintain a CM Pool account (with a valid BO Status/BO Sub-status) for all settlement-related transactions, including EP transactions. This change affects Depository Participants (DPs), clients of Trading Members (TMs), TMs of all registered Stock Exchanges, and Clearing Members of all registered Clearing Corporations.

## Key Points

- Effective March 21, 2026, CMs will no longer need to maintain a separate EP account with the Clearing Corporation.
- All EP transactions must use the CM Pool account instead of EP account from March 21, 2026 onwards.
- EP transactions can still be executed using EP accounts until 09:00 PM on March 20, 2026.
- CDSL will replace EP accounts with CM Pool accounts for all in-transit EP transactions (status: 'Earmarked' or 'Overdue') after 09:00 PM on March 20, 2026.
- All EP accounts will be marked for closure before EOD of March 20, 2026.
- NIL balance EP accounts will be closed during EOD processing of March 20, 2026.
- Remaining balances in EP accounts will stay in those accounts (status: 'To be Closed') until transferred; no fresh credits except Corporate Action credits will be permitted.
- Opening of new EP accounts will be restricted in the CDSL system from March 21, 2026.
- No changes to existing DIS format.
- For inter-depository (NSDL to CDSL) EP transactions, BOID of CDSL CM Pool account must be provided instead of EP account.

## Regulatory Changes

CDSL is modifying its settlement infrastructure to consolidate EP transactions into CM Pool accounts, eliminating the requirement for a separate EP account. This simplifies the account structure for Clearing Members by reducing the number of accounts required for settlement operations. The change is operationally mandated and does not alter the nature of EP transactions themselves.

## Compliance Requirements

- **Clearing Members (CMs):** Must update all systems and processes to use CM Pool account in place of EP account for settlement and EP transactions from March 21, 2026. Must coordinate with respective Clearing Corporations to transfer any residual balances from EP accounts to CM Pool accounts.
- **Depository Participants (DPs):** Must ensure EP transactions entered after SOD of March 21, 2026 reference CM Pool account instead of EP account.
- **Trading Members (TMs) and Clients:** Must submit Delivery Instruction Slips (DIS) with the BOID of CM Pool account as 'Counter BOID' from March 21, 2026.
- **System Updates:** All transaction entry methods (Easiest/WebCDAS upload, Online setup, eDIS, APIs) must be updated to reference CM Pool account.
- **Inter-depository transactions:** TMs/CMs with client accounts in NSDL must provide CDSL CM Pool account BOID (not EP account BOID) in DIS submitted to NSDL DP.

## Important Dates

- **March 20, 2026, 09:00 PM:** Last time EP transactions can be executed using EP accounts.
- **March 20, 2026, EOD:** CDSL marks all EP accounts for closure; NIL balance EP accounts are closed.
- **March 21, 2026 (SOD onwards):** EP transactions must reference CM Pool account; opening of new EP accounts restricted.
- **Ongoing post March 21, 2026:** EP accounts with residual balances remain in 'To be Closed' status until balance becomes NIL, at which point they are automatically closed.

## Impact Assessment

This change has a moderate operational impact on Clearing Members, Depository Participants, and Trading Members who use EP accounts for settlement. Entities must update their internal systems, workflows, and DIS templates before March 21, 2026. The consolidation of EP transactions into CM Pool accounts simplifies account management and reduces overhead for CMs. There is no change to the DIS format itself, limiting the scope of documentation updates required. Residual balances in EP accounts will not be lost but will require coordination with Clearing Corporations for transfer. No direct impact on trading activity, securities pricing, or listed companies.