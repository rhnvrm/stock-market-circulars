---
category: compliance
circular_id: 7de3c19efd39c292
date: '2026-07-17'
description: NSE has consolidated operational and compliance requirements for UCC
  upload/modification, including a change effective July 24, 2026 discontinuing the
  'Inactive' to 'Active' client status modification via the Client Status module in
  UCI-Online.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/ISC75249.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational/compliance circular affecting all trading members' back-office
  UCC processes; no direct stock price impact but requires process changes ahead of
  a July 24, 2026 deadline.
pdf_url: https://nsearchives.nseindia.com/content/circulars/ISC75249.pdf
processing:
  attempts: 1
  content_hash: dbba078518fa41f8
  processed_at: '2026-07-17T16:29:50.776976'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-07-17T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/ISC75249.pdf
severity: medium
source: nse
stocks: []
tags:
- ucc
- unique-client-code
- kyc
- kra
- uci
- unique-client-identifier
- compliance
title: NSE Issues General Operational Guidelines on Unique Client Code (UCC)
---

## Summary

NSE's Investor Services Cell has issued a consolidated set of operational guidelines on Unique Client Code (UCC) management, reiterating existing requirements around timely updates, demat account details, KYC/KRA validation, data reconciliation, and file monitoring. The circular also announces a key procedural change: effective July 24, 2026, Members will no longer be able to modify a client's status from 'Inactive' to 'Active' using the Client Status module in UCI-Online.

## Key Points

- Any change in client information must be updated immediately in the Exchange UCC database.
- Demat account details should be included in the UCC modification file only when they have actually changed; submitting unchanged details may trigger unnecessary re-verification by Depositories and affect the client's Permitted to Trade status.
- Demat details must follow the prescribed format: NSDL DP ID (8 alpha/numeric characters) and BO ID (8 characters), or CDSL BO ID (16 numeric characters); Members must mark the appropriate account as Primary.
- Clients whose KYC is not validated by KRA can transact only once their KRA status is 'KRA Validated' or 'KRA Registered'; new client KYC must be uploaded to KRAs within the prescribed timeline.
- A full file request facility is available for Members to reconcile UCC data with Exchange records.
- Gross annual income details of clients (where applicable) must be kept updated at all times.
- UCCs marked compliant by the Exchange at 22:00 hrs on the previous day are treated as permitted to trade for the next trading day.
- The Exchange disseminates several files Members must actively monitor: Permitted/Not Permitted to Trade (batch 1 & 2), Mobile Number Revocation List, Demat and Bank account verification status, and a weekly mandatory-fields report.

## Regulatory Changes

Effective July 24, 2026, the Client Status module in UCI-Online will no longer allow modification of client status from 'Inactive' to 'Active'. This module will continue to support changes from 'Active' to 'Inactive', 'Active' to 'Close', and 'Inactive' to 'Close'.

## Compliance Requirements

- To reactivate a client from 'Inactive' to 'Active' after July 24, 2026, Members must use the 'Query Client' module, the 'New Client Bulk Upload' module, or the 'Client Profiling API' in UCI-Online.
- Members must exercise care while modifying client status given the reduced functionality of the Client Status module.
- Members must continuously monitor Exchange-disseminated UCC files and take timely action.
- Queries can be directed to uci@nse.co.in.

## Important Dates

- July 24, 2026: 'Inactive' to 'Active' client status modification via the Client Status module in UCI-Online is discontinued.

## Impact Assessment

This is a back-office/operational circular with no direct market or stock price impact. Members' compliance and operations teams need to update internal workflows before July 24, 2026 to use alternative modules (Query Client, New Client Bulk Upload, or Client Profiling API) for reactivating inactive clients, avoiding disruption to client onboarding and trading permissions.