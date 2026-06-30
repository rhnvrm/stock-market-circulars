---
category: market-operations
circular_id: 0546f070c8310a17
date: '2026-06-30'
description: BSE is adding new IP gateways in its equity segment production setup
  effective July 6, 2026. Members using ETI-based applications may need to update
  network configurations to allow connectivity to the new gateway IP addresses.
draft: false
guid: https://www.bseindia.com/downloads/UploadDocs/Notices/20260630-14/20260630-14.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical infrastructure change requiring member action before July
  6, 2026; no market or regulatory policy change but network misconfiguration could
  disrupt trading connectivity.
pdf_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260630-14/20260630-14.pdf
processing:
  attempts: 1
  content_hash: 2368f14e26ac49e0
  processed_at: '2026-06-30T14:45:49.467389'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-30T10:11:19+00:00'
rss_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260630-14/20260630-14.pdf
severity: medium
source: bse
stocks: []
tags:
- gateway
- network-infrastructure
- equity
- trading
- bse
- colocation
- connectivity
title: Addition of New Gateways in Equity Production Environment
---

## Summary

BSE is expanding its equity segment production infrastructure by adding new connection gateways. Members using ETI-based applications will be automatically assigned these new gateways via the existing connection gateway mechanism, so network reachability to the new IP addresses must be ensured before July 6, 2026.

## Key Points

- BSE is adding new gateways to the equity and BSE Colocation segments in the production environment.
- The connection gateway IP address remains unchanged; only the pool of assigned gateways is expanding.
- ETI-based member applications connect to the connection gateway, which may now assign new gateway IPs in response.
- Members must ensure their networks can reach the new IP addresses and ports.
- BSE recommends allowing the full `10.255.0.0/255.255.0.0` IP range to avoid future reconfiguration.

## New Gateway Details

| Segment | IP Addresses | Ports |
|---|---|---|
| Equity | 10.255.255.65, 10.255.255.66, 10.255.255.67, 10.255.255.68, 10.255.255.69, 10.255.255.70 | 18906 to 18914 |
| Equity (BSE Colocation) | 10.255.253.5, 10.255.253.6, 10.255.253.7 | 18906 to 18914 |

## Regulatory Changes

No regulatory or policy changes. This is a purely technical infrastructure expansion.

## Compliance Requirements

- Members using ETI-based applications must verify that their network firewall and routing rules permit access to the new gateway IP addresses listed above on ports 18906–18914.
- If the member network already allows the full `10.255.0.0` range with subnet mask `255.255.0.0`, no changes are needed.
- Otherwise, members must update their network configurations to include the newly added gateway IPs before July 6, 2026.
- BSE advises permitting the entire `10.255.X.X` range as per the BOLT Plus Connectivity Manual to avoid disruption from any future gateway additions.

## Important Dates

- **July 6, 2026**: New gateways go live in production. All network configuration changes must be completed before this date.

## Impact Assessment

This change is operationally significant for trading members using ETI-based connectivity. Members who have restricted firewall rules to specific IPs (rather than the full `10.255.X.X` subnet) risk connectivity failures when the connection gateway begins assigning the new IPs after July 6, 2026. Members with broad subnet-level rules already in place will be unaffected. No market structure, regulatory, or instrument-level changes are involved.