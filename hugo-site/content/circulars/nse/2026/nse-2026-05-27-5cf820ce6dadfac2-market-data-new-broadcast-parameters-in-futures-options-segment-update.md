---
category: market-operations
circular_id: 5cf820ce6dadfac2
date: '2026-05-27'
description: NSE updates multicast IP and port details for stream-wise broadcast in
  the Futures & Options segment, partially modifying circular NSE/MSD/74133 dated
  May 08, 2026. Members using stream broadcast must update their parameters to receive
  existing and new transcodes.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD74448.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical infrastructure update affecting NSE members who use stream-wise
  broadcast in the F&O segment; requires action to update multicast IP/port parameters
  but does not affect trading rules or listed securities.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD74448.pdf
processing:
  attempts: 1
  content_hash: f3497f79d94dddf6
  processed_at: '2026-05-27T16:06:46.809283'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-27T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD74448.pdf
severity: medium
source: nse
stocks: []
tags:
- market-data
- futures-and-options
- broadcast
- multicast
- member-service
- nse
title: 'NSE Futures & Options Segment: Updated Market Data Broadcast Parameters (Table
  B)'
---

## Summary

NSE's Member Service Department has issued a partial modification to circular NSE/MSD/74133 (dated May 08, 2026), updating the port details in Table B for stream-wise broadcast in the Futures & Options segment. Members currently using stream broadcast must migrate to the new parameters to continue receiving existing transcodes (except 17201, 11833, 7208 & 7211) as well as new transcodes (7201, 1833, 17208 & 17211). All other details from the original circular remain unchanged.

## Key Points

- This is a partial modification to NSE/MSD/74133 dated May 08, 2026; only Table B (stream-wise broadcast) parameters are updated.
- Updated multicast IP and port details apply to FO Stream B (Stream 1) and FO Stream C (Stream 2) for both Source 1 and Source 2.
- Combined broadcast parameters in Table A remain unchanged.
- Approximate bandwidth utilization per stream: 0.115 Mbps.
- Members must use master stream file to determine security/contract allocation per stream.

## Regulatory Changes

No regulatory or trading rule changes. This is a technical infrastructure update to market data dissemination parameters for the Futures & Options segment.

## Compliance Requirements

- Members using stream-wise broadcast in the F&O segment **must update** their multicast IP addresses and port numbers as per the new Table B to continue receiving market data.
- Updated parameters for Source 1 and Source 2:
  - FO Stream B (Stream 1): Source 1 — 239.50.51.21:15021; Source 2 — 239.50.51.121:15121; Master — 239.50.51.20:15020 (both sources).
  - FO Stream C (Stream 2): Source 1 — 239.50.51.22:15022; Source 2 — 239.50.51.122:15122; Master — 239.50.51.20:15020 (both sources).
- Members not using stream broadcast are unaffected; they may continue using combined broadcast (Table A).

## Important Dates

- Circular date: May 27, 2026.
- Original circular (NSE/MSD/74133) date: May 08, 2026.
- No explicit go-live deadline stated; members should implement the parameter changes promptly to avoid data disruption.

## Impact Assessment

This update has a moderate operational impact on NSE trading members who subscribe to stream-wise market data feeds in the F&O segment. Failure to update multicast IP/port parameters will result in loss of market data for those streams. Members using the combined broadcast (Table A) are unaffected. The change is purely technical and does not affect trading strategies, margin requirements, or listed contracts.