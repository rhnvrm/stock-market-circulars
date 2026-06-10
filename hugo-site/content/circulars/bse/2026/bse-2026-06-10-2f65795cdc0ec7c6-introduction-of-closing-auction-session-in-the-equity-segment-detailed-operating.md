---
category: trading
circular_id: 2f65795cdc0ec7c6
date: '2026-06-10'
description: BSE issues detailed operating guidelines for the Closing Auction Session
  (CAS) in the Equity Segment, covering session timings, applicability, reference
  price determination, and order types for derivative-eligible stocks.
draft: false
guid: https://www.bseindia.com/downloads/UploadDocs/Notices/20260610-41/20260610-41.pdf
impact: high
impact_ranking: high
importance_ranking: high
justification: This circular introduces a significant structural change to equity
  market trading hours and session mechanics affecting all trading members and derivative-eligible
  stocks, requiring operational and system-level adaptations.
pdf_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260610-41/20260610-41.pdf
processing:
  attempts: 1
  content_hash: d6cf624bce50e1b0
  processed_at: '2026-06-10T15:41:27.638254'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-10T15:28:01+00:00'
rss_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260610-41/20260610-41.pdf
severity: high
source: bse
stocks: []
tags:
- closing-auction-session
- trading
- equity-segment
- sebi
- continuous-trading
- market-operations
- order-entry
- price-discovery
- derivatives
title: Introduction of Closing Auction Session in the Equity Segment – Detailed Operating
  Guidelines
---

## Summary

BSE has issued detailed operating guidelines for the Closing Auction Session (CAS) in the Equity Segment, pursuant to SEBI circular dated January 16, 2026, and prior Exchange circulars. CAS will initially apply to stocks with available derivative contracts (excluding CDSL and BSE itself), with a phased rollout. The session runs from 3:15 PM to 3:35 PM, replacing the existing continuous trading end time for eligible securities.

## Key Points

- CAS is applicable initially to stocks with derivative contracts available, excluding CDSL and BSE (unless invoked under Business Continuity provisions)
- Continuous Trading Session (CTS) for CAS-eligible securities ends at 3:15 PM (previously 3:30 PM)
- CAS runs from 3:15 PM to 3:35 PM, with a buffer period up to 3:50 PM, followed by post-closing session from 3:50 PM to 4:00 PM
- Securities not eligible for CAS continue trading until 3:30 PM; their post-closing session is revised to 3:50 PM–4:00 PM
- New securities are added to CAS eligible list from their first trading date in derivatives across exchanges
- A security exits the CAS eligible list from the trading day after its last derivatives trading date across exchanges
- CAS is not applicable on ex-dates of scheme of arrangement (if price not determined during SPOS) or if a market-wide index circuit breaker halts trading for the remainder of the day
- Market orders cannot be placed or modified during the limit-order-only entry period (3:25 PM–3:30 PM); such requests are rejected with the message: "Market order cannot be placed during this period."

## Regulatory Changes

- Continuous trading session end time for CAS-eligible securities moved from 3:30 PM to 3:15 PM
- Introduction of a structured 20-minute Closing Auction Session (3:15 PM–3:35 PM) for derivative-eligible stocks
- Post-closing session for all securities (CAS-eligible and non-eligible) revised to 3:50 PM–4:00 PM
- Pending Stop Loss and Revealed Quantity orders from CTS are cancelled at 3:15 PM during the CTS-to-CAS transition
- Reference to SEBI/HO/47/11/11(3)2025-MRD-POD2/I/2765/2026 dated January 16, 2026

## Compliance Requirements

- Trading members must update systems to handle the revised session timings and new CAS order flow
- Members must ensure market orders are not submitted between 3:25 PM and 3:30 PM for CAS-eligible securities
- Members should note automatic cancellation of Stop Loss and Revealed Quantity orders at the CTS-to-CAS transition (3:15 PM–3:20 PM)
- Members must track the dynamic list of CAS-eligible securities based on derivatives availability across exchanges

## Important Dates

- Circular Date: June 10, 2026
- Reference SEBI Circular: January 16, 2026
- Prior Exchange Circulars: January 19, 2026 (no. 0260119-17) and March 19, 2026 (no. 20260319-21)
- CAS Session Daily Schedule (for eligible securities):
  - 3:15 PM – 3:20 PM: Reference price calculation and transition from CTS to CAS
  - 3:20 PM – 3:25 PM: Order entry (limit and market orders; no trade execution)
  - 3:25 PM – 3:30 PM: Order entry for limit orders only; system-driven random stoppage in last 2 minutes
  - 3:30 PM – 3:35 PM: Order matching, trade confirmation, closing price determination
  - 3:35 PM – 3:50 PM: Buffer period
  - 3:50 PM – 4:00 PM: Post-closing session

## Impact Assessment

This is a high-impact structural change to equity market microstructure. All trading members dealing in derivative-eligible stocks must update front-end and risk management systems to account for the revised CTS end time (3:15 PM instead of 3:30 PM) and the new CAS mechanics. The introduction of a formal auction closing mechanism is intended to improve closing price discovery and reduce end-of-day volatility. Algorithmic trading strategies operating near market close will require recalibration. The phased rollout tied to derivatives eligibility limits initial scope but will cover a significant portion of liquid large-cap stocks. Post-closing session timing changes affect all securities regardless of CAS eligibility.