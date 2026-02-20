---
category: market-operations
circular_id: d4b3928447a66434
date: '2026-02-20'
description: CDSL has announced that effective March 21, 2026, Clearing Members will
  no longer be required to maintain a separate Early Pay-in (EP) account; only a CM
  Pool account will be needed for settlement transactions.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT72919.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational change affecting clearing members and depository participants
  requiring system and process updates, but no direct impact on listed securities
  or trading outcomes.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT72919.zip
processing:
  attempts: 1
  content_hash: f9d6ac1bdd8613c4
  processed_at: '2026-02-20T17:09:31.751829'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-02-20T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT72919.zip
severity: medium
source: nse
stocks: []
tags:
- settlement
- early-pay-in
- epi
- cdsl
- clearing-members
- depository-participants
- cm-pool-account
- cash-segment
- operational-change
title: Discontinuation of Separate Early Pay-in (EPI) Account for Cash Segment
---

## Summary

CDSL (Central Depository Services (India) Limited) has issued a communiqué (CDSL/OPS/DP/SETTL/2026/122 dated February 19, 2026) informing all market participants that effective March 21, 2026, Clearing Members (CMs) will no longer be required to maintain a separate Early Pay-in (EP) account with Clearing Corporations. CMs will only need to maintain a CM Pool account to execute all settlement-related transactions, including EP transactions.

## Key Points

- Effective March 21, 2026, separate EP accounts will be discontinued for the Cash segment.
- CMs will use their existing CM Pool account (with valid BO Status/BO Sub-status) for all EP transactions going forward.
- EP transactions can still be executed using the EP account until 09:00 PM on March 20, 2026.
- After 09:00 PM on March 20, 2026, the CDSL system will block any new EP transaction setups on EP accounts.
- In-transit EP transactions with status 'Earmarked' or 'Overdue' after 09:00 PM on March 20, 2026 will automatically have their EP account replaced with the corresponding CM Pool account.
- All EP accounts will be marked for closure before EOD on March 20, 2026; NIL balance EP accounts will be closed during EOD processing.
- Balances remaining in EP accounts post-closure will carry 'To be Closed' status; no fresh credits (except corporate action credits) will be allowed. CMs must coordinate with their CC to transfer balances to CM Pool accounts.
- Opening of new EP accounts will be restricted in the CDSL system from March 21, 2026.
- There is no change to the existing DIS (Delivery Instruction Slip) format; clients/TMs/CMs must mention the BOID of the CM Pool account as 'Counter BOID' in DIS submissions.
- For EP transactions submitted via upload (Easiest/WebCDAS), online setup, eDIS, or APIs, the CM Pool account BOID must be used instead of the EP account BOID.
- For inter-depository EP transactions from NSDL client accounts to CDSL, TMs/CMs must provide the BOID of the CDSL CM Pool account in the DIS submitted to the NSDL DP.

## Regulatory Changes

- CDSL is discontinuing the requirement to maintain a separate EP account for Early Pay-in transactions.
- The CM Pool account will now serve as the single account for all settlement-related transactions including EP transactions.
- No changes to the existing block mechanism guidelines for respective market types.

## Compliance Requirements

- **Depository Participants (DPs):** Must update operational processes to use CM Pool account BOIDs for EP transactions from March 21, 2026. Pending EP transactions after SOD on March 21, 2026 must use CM Pool account.
- **Clearing Members (CMs):** Must coordinate with respective Clearing Corporations to transfer any residual balances from EP accounts to CM Pool accounts. Must update system integrations (Easiest, WebCDAS, APIs) to reference CM Pool account.
- **Trading Members (TMs) / Clients:** Must use BOID of CM Pool account as Counter BOID in DIS submissions. For inter-depository EP transactions (NSDL to CDSL), must provide CDSL CM Pool account BOID to NSDL DP.
- All participants must complete any EP transactions via existing EP accounts before 09:00 PM on March 20, 2026.

## Important Dates

- **March 20, 2026, 09:00 PM:** Deadline to execute EP transactions using EP accounts. Post this time, no new EP transaction setups will be permitted on EP accounts.
- **March 20, 2026, EOD:** CDSL will mark all EP accounts for closure; NIL balance EP accounts will be closed during EOD processing.
- **March 21, 2026:** Effective date for discontinuation. Opening of new EP accounts restricted. CMs must use CM Pool account for all EP transactions.

## Impact Assessment

This change primarily impacts Clearing Members, Depository Participants, and Trading Members who currently use separate EP accounts for Early Pay-in transactions. The operational shift is administrative in nature—requiring system configuration updates and process changes—but does not affect trading activity, listed securities, or investor holdings directly. Participants using automated upload or API-based EP transaction submissions will need to update their systems to reference CM Pool account BOIDs. The transition window (until March 20, 2026 EOD) provides adequate time for preparation. Residual EP account balances require manual coordination with Clearing Corporations, which may require some administrative effort for participants holding significant balances.