---
category: market-operations
circular_id: ef6b38740d575f0d
date: '2026-04-10'
description: NSE Clearing Limited introduces a new NMASS-based process for clearing
  members to block collaterals for OFS retail category bids, replacing the existing
  email-based process effective April 13, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT73695.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational process change affecting clearing members and custodians
  for OFS collateral blocking; limited to retail category bids and replaces an existing
  manual email workflow with a system-based process.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT73695.pdf
processing:
  attempts: 1
  content_hash: d4603c0bbdc0a801
  processed_at: '2026-04-10T13:26:53.835914'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-04-10T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT73695.pdf
severity: medium
source: nse
stocks: []
tags:
- ofs
- collateral
- nmass
- clearing-members
- retail-category
- capital-market
- nse-clearing
title: Collateral Blocking for OFS Retail Category Bids via NMASS
---

## Summary

NSE Clearing Limited (NCL) has introduced a new system-based process for clearing members to block collateral towards Offer for Sale (OFS) retail category bids via the NMASS system. The previous process of sending emails to the collaterals team is discontinued, and the new NMASS-based workflow becomes effective from April 13, 2026.

## Key Points

- Clearing members must make the required collateral amount available in the collateral pool before placing a blocking request.
- The facility to block collateral is available only for OFS bids in the **retail category** on T+1 day.
- Super admins must create or modify roles in NMASS to assign the new OFS services.
- A new menu item for OFS blocking requests has been introduced under the OFS module in NMASS.
- Blocking is done on a **settlement number basis**.
- Each blocking request is **additive** — the entered amount is added to the previously blocked amount.
- The system validates the blocking amount against the available pool in the common segment; insufficient pool amounts will trigger an error message.

## Regulatory Changes

- The existing process of emailing the collaterals team (`collaterals_ops@nsccl.co.in`) for OFS collateral blocking is **discontinued**.
- The new NMASS-based process replaces the email workflow effective **April 13, 2026**.

## Compliance Requirements

- Clearing members and custodians must transition to using the NMASS system for all OFS collateral blocking requests.
- Super admins are required to configure roles in NMASS for the new OFS services before the effective date.
- NMASS Navigation path: `NMASS → OFS → OFS Funds Pay-in → OFS Funds → OFS Collateral Blocking Request`.
- Ensure sufficient collateral pool balance in the common segment prior to submitting blocking requests.

## Important Dates

- **April 10, 2026**: Circular issued by NSE Clearing Limited.
- **April 13, 2026**: New NMASS-based collateral blocking process becomes effective; email-based process discontinued.

## Impact Assessment

This change primarily impacts clearing members, custodians, and principal clearing members (PCMs) who participate in OFS retail category bids. The shift from a manual email process to a system-driven NMASS workflow is expected to improve efficiency, auditability, and real-time validation of collateral availability. Members must update their internal workflows and ensure NMASS roles are configured ahead of the April 13 deadline to avoid disruption in OFS participation.