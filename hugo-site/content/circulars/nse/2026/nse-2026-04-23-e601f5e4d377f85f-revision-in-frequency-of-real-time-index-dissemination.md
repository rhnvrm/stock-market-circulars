---
category: market-operations
circular_id: e601f5e4d377f85f
date: '2026-04-23'
description: NSE will double the dissemination frequency of the Nifty 50 index from
  500 milliseconds to 250 milliseconds on its trading system for CM and FO segments,
  effective May 11, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD73861.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical infrastructure change affecting all members using real-time
  Nifty 50 index data in trading systems; requires system readiness ahead of May 11,
  2026 effective date but does not alter trading rules or compliance obligations.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD73861.zip
processing:
  attempts: 1
  content_hash: 3bbf9020e1b2ba4f
  processed_at: '2026-04-23T13:40:58.609115'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-04-23T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD73861.zip
severity: medium
source: nse
stocks: []
tags:
- nifty-50
- index-dissemination
- market-operations
- trading-system
- real-time-data
- cm-segment
- fo-segment
- nse-indices
title: NSE Revises Nifty 50 Real-Time Index Dissemination Frequency to 250ms Effective
  May 11, 2026
---

## Summary

NSE's Member Service Department has announced a revision in the real-time dissemination frequency of the Nifty 50 index on its trading system. The frequency will be doubled from the current 500 milliseconds (0.5 second) to 250 milliseconds (0.25 second) in both the Capital Market (CM) and Futures & Options (FO) segments. The change is effective May 11, 2026, with a mock session available on May 9, 2026.

## Key Points

- Nifty 50 index dissemination frequency on the NSE trading system will change from 500ms to 250ms
- Change applies to both CM (Capital Market) and FO (Futures & Options) segments
- A mock session is scheduled for May 9, 2026, allowing members to test compatibility
- The change is driven by increasing use of indices for financial product valuation and rising derivatives trading volumes linked to Nifty 50
- NSE Indices currently computes over 425 indices; 134 indices (123 equity, 11 debt) are disseminated live at 500ms — other indices will be aligned in a phased manner
- Nifty indices underlie over 490 passive mutual fund products in India and 33 outside India, with a combined AUM of approximately USD 95 billion as of March 31, 2026

## Regulatory Changes

No change to trading rules or regulations. This is a technical infrastructure update to the index data feed on NSE's trading system. The dissemination interval for Nifty 50 is being halved (500ms → 250ms), effectively doubling the number of index value updates per second transmitted to members.

## Compliance Requirements

- All members receiving real-time Nifty 50 index data via the NSE trading system should review their systems and applications for compatibility with the increased update frequency
- Members are encouraged to participate in the mock session on May 9, 2026, to validate their infrastructure handles the higher data rate
- No explicit filing or reporting obligation is mandated; this is an operational readiness requirement

## Important Dates

- **April 22, 2026**: NSE Indices press release announcing the change
- **April 23, 2026**: NSE circular (NSE/MSD/73861) issued to all members
- **May 9, 2026**: Mock session — members can test systems against the new 250ms dissemination frequency
- **May 11, 2026**: Effective date — Nifty 50 live dissemination frequency changes to 250ms on CM and FO segments

## Impact Assessment

**Operational Impact (Medium):** Members and vendors consuming real-time Nifty 50 index data from NSE's trading system will receive twice as many data ticks per second. Systems with bandwidth constraints, message processing queues, or rate-limiting logic tuned for 500ms updates may need reconfiguration or capacity upgrades before May 11, 2026.

**Market Impact (Low-Medium):** Higher-frequency index values improve pricing accuracy for index derivatives (Nifty futures and options) and reduce latency in index-linked product valuation. Algorithmic and high-frequency traders may benefit from finer-grained index signals. The change does not affect trading hours, lot sizes, margin requirements, or any other market microstructure parameters.

**Phased Rollout:** NSE has indicated that other indices currently disseminated at 500ms will be progressively aligned to 250ms in subsequent phases, so members should anticipate further similar changes for other index data feeds.