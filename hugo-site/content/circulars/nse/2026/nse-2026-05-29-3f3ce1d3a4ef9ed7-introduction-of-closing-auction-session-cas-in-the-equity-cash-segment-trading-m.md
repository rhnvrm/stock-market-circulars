---
category: trading
circular_id: 3f3ce1d3a4ef9ed7
date: '2026-05-29'
description: NSE introduces a 20-minute Closing Auction Session (CAS) from 3:15 PM
  to 3:35 PM for derivative-eligible stocks in the Equity Cash segment, with single
  equilibrium price matching and specific order restrictions.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMTR74466.zip
impact: high
impact_ranking: high
importance_ranking: high
justification: Introduces a structural change to the equity market session framework
  affecting all members trading derivative-eligible stocks, with new session timings,
  order types, matching rules, and closing price methodology.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMTR74466.zip
processing:
  attempts: 1
  content_hash: 351a99f8049003b4
  processed_at: '2026-05-29T15:58:19.691098'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-29T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMTR74466.zip
severity: high
source: nse
stocks: []
tags:
- closing-auction-session
- equity-cash-segment
- trading-modalities
- order-matching
- price-discovery
- market-operations
- settlement-calendar
title: Introduction of Closing Auction Session (CAS) in Equity Cash Segment - Trading
  Modalities
---

## Summary

NSE is introducing a Closing Auction Session (CAS) in the Equity Cash segment as an additional 20-minute session from 3:15 PM to 3:35 PM on all trading days. This circular (NSE/CMTR/74466, Ref No. 71/2026) details the operational modalities, session timings, order restrictions, and closing price calculation methodology applicable to CAS, supplementing earlier circulars dated January 19, March 18, and April 22, 2026.

## Key Points

- CAS will be implemented in a phased manner, initially applicable only to stocks on which derivative contracts are available on any exchange.
- The session runs for 20 minutes (3:15 PM – 3:35 PM), with distinct sub-periods for reference price calculation, order entry, and order matching.
- Special term orders — Stop Loss (SL), Immediate or Cancel (IOC), and Disclosed Quantity (DQ) — are not permitted during CAS.
- All orders in CAS are matched at a single equilibrium price per security.
- Unexecuted orders at the end of the CAS matching phase are cancelled by the Exchange.
- Trade cancellation requests for CAS-executed trades will be rejected by the system.
- Post-close session timings (3:50 PM – 4:00 PM) and modalities remain unchanged.

## Regulatory Changes

- **New session introduced:** CAS (3:15 PM – 3:35 PM) is added as a separate session between the existing Closing Trading Session (CTS) and post-close session.
- **Closing price methodology updated:** For CAS-applicable securities, the closing price is the equilibrium price determined during CAS. If no equilibrium price is determined, the reference price (per circular NSE/CMTR/73362) is used. If the security was not traded at all that day, the latest available closing price is used.
- **Non-CAS securities:** Closing price continues per existing mechanism in circular NSE/CMTR/73927 dated April 28, 2026.
- **CAS exclusions:** CAS does not apply on the ex-date of a scheme of arrangement (if price is not determined during SPOS) or when an index circuit break halts trading for the remainder of the day.

## Compliance Requirements

- All members must update their trading systems and NEAT configurations to handle CAS-specific order entry rules and error messages.
- Members must ensure market orders are not submitted after the order entry period (3:25 PM); any such orders will be rejected with the message: *"Market orders are currently not allowed."*
- Members must note that trade cancellation for CAS trades will be rejected with the message: *"Trade executed during closing auction session is not allowed to cancel."*
- Members should communicate these operational changes to their clients, particularly regarding the restricted order types and non-cancellability of CAS trades.

## Important Dates

- **Circular Date:** May 29, 2026
- **CAS Session Timings (all trading days):**
  - 3:15 PM – 3:20 PM: Reference price calculation / Transition from CTS to CAS
  - 3:20 PM – 3:25 PM: Order entry, modification, and cancellation (limit and market orders)
  - 3:25 PM – 3:30 PM: Limit orders only; no market order modification/cancellation; system-driven random closure in last 2 minutes
  - 3:30 PM – 3:35 PM: Order matching and trade confirmation
  - 3:35 PM – 3:50 PM: Transition from CAS to post-close session
  - 3:50 PM – 4:00 PM: Post-close session (unchanged modalities)
- Reference circulars: NSE/CMTR/72394 (Jan 19, 2026), NSE/CMTR/73362 (Mar 18, 2026), NSE/CMTR/73845 (Apr 22, 2026), NSE/CMTR/73927 (Apr 28, 2026)

## Impact Assessment

This is a significant structural change to equity market microstructure. The introduction of CAS affects all members and their clients trading in derivative-eligible stocks. The single-price equilibrium matching mechanism during CAS is intended to improve price discovery at market close and reduce end-of-day volatility. Members need to update their trading systems, risk controls, and client-facing documentation. The restriction on trade cancellation for CAS trades and the auto-cancellation of unexecuted CAS orders are notable operational differences from the regular session that require member preparedness. The phased rollout (starting with F&O-eligible stocks) limits immediate disruption but sets the stage for broader applicability.