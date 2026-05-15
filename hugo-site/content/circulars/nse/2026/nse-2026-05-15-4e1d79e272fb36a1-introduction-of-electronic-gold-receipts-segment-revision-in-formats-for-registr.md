---
category: compliance
circular_id: 4e1d79e272fb36a1
date: '2026-05-15'
description: NSE revises the Non-Neat Frontend (NNF) software registration formats
  to include the Electronic Gold Receipts (EGR) segment, updating auditor certificate
  requirements and pre-trade risk control compliance checks.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/INVG74233.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational compliance update affecting trading members using NNF software
  (CTCL/IBT/DMA/STWT/SOR/AT); expands EGR segment coverage in risk checks but does
  not alter broader market structure or pricing.
pdf_url: https://nsearchives.nseindia.com/content/circulars/INVG74233.zip
processing:
  attempts: 1
  content_hash: 94c1f975f77ca9fa
  processed_at: '2026-05-15T14:27:25.058658'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-15T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/INVG74233.zip
severity: medium
source: nse
stocks: []
tags:
- egr
- nnf
- software-registration
- pre-trade-risk-controls
- electronic-gold-receipts
- ctcl
- ibt
- algo-trading
- system-audit
- compliance
title: Introduction of Electronic Gold Receipts Segment - Revision in NNF Software
  Registration Formats
---

## Summary

NSE has revised the formats for registration of Non-Neat Frontend (NNF) software to incorporate the newly introduced Electronic Gold Receipts (EGR) segment. The key change is the inclusion of EGR alongside existing segments (CM, FO, CD, CO) in mandatory pre-trade risk control compliance checks that system auditors must certify. Trading members deploying NNF products must now ensure their software and auditor certificates reflect EGR segment compliance.

## Key Points

- The Auditor's Certificate format (Annexure B2) for NNF software registration has been revised to include the EGR segment.
- Pre-trade risk controls — including Price Check, Quantity Limit Check, Order Value Check, Cumulative Open Order Value Check, and Net Position vs. Available Margin Check — are now explicitly applicable to the EGR segment.
- The certificate must be issued on the system auditor's letterhead, duly stamped and signed on all pages.
- NNF product types covered: CTCL, IBT, DMA, STWT, SOR, AT, and User Interface.
- Product category is specified as API.
- For SOR products, the software through which SOR is provided must be declared (CTCL/IBT/DMA/STWT/AT).
- Trade Price Protection Check and Market Price Protection Check remain applicable only to CM, FO, CD, and CO segments (not EGR).

## Regulatory Changes

- Annexure B2 (Auditor's Certificate for NNF Software Registration) revised to add EGR as an applicable segment for the following pre-trade risk controls:
  - Price Check (CM/FO/CD/CO/EGR)
  - Quantity Limit Check (CM/FO/CD/CO/EGR)
  - Order Value Check (CM/FO/CD/CO/EGR)
  - Cumulative Open Order Value Check (CM/FO/CD/CO/EGR)
  - Net Position vs. Available Margin Check (CM/FO/CD/CO/EGR)
- RBI Violation Check for FII Restricted stocks and Trade Price/Market Price Protection checks remain confined to CM/FO/CD/CO segments.

## Compliance Requirements

- Trading members using NNF software must obtain a revised Auditor's Certificate (Annexure B2) that includes EGR segment compliance attestation.
- System auditors must verify that NNF software complies with all SEBI/Exchange circulars applicable at the time of application, covering: Order Management, Systems and Network, Access and Security Controls, Cyber Security & Cyber Resilience Framework, and the updated pre-trade risk checks.
- Software must enforce all individual order-level and UCC-level risk controls for the EGR segment.
- Spread order checks for Quantity Limit and Order Value are also applicable for EGR.
- System must not permit users to set "Unlimited values" for Cumulative Open Order Value.

## Important Dates

- No specific effective date is mentioned in the available content; members should treat this as immediately applicable upon circular issuance and apply it to new or renewal NNF software registrations.

## Impact Assessment

- **Trading Members:** Must update their NNF software registration documentation and obtain fresh auditor certificates that cover EGR segment risk controls before deploying or renewing EGR-enabled trading systems.
- **System Auditors:** Must include EGR-specific compliance verification in their audit scope and certify adherence to price, quantity, order value, open order value, and margin checks for EGR.
- **Algo/AT Firms:** Algorithmic trading systems operating in the EGR segment are subject to the same pre-trade risk control certification requirements as other segments.
- **Market Impact:** Limited broader market impact; primarily an administrative and compliance process update for technology vendors and trading members participating in the EGR segment.