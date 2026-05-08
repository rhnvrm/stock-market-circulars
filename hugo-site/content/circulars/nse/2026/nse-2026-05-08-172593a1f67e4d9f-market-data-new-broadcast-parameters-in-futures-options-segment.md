---
category: market-operations
circular_id: 172593a1f67e4d9f
date: '2026-05-08'
description: NSE is introducing new broadcast parameters in the F&O segment to change
  the data type for token level cumulative volume from Unsigned Integer (4 bytes)
  to LONG (8 bytes), effective May 11, 2026 in live environment.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD74133.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical infrastructure change affecting F&O market data broadcast
  for member firms; requires system updates but does not change trading rules or affect
  listed securities directly.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD74133.pdf
processing:
  attempts: 1
  content_hash: 1df746a9e98fc86b
  processed_at: '2026-05-08T13:59:40.727903'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-08T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD74133.pdf
severity: medium
source: nse
stocks: []
tags:
- futures-and-options
- market-data
- broadcast-parameters
- nnf
- neat
- mbp
- bhavcopy
- technical-change
- data-dissemination
title: Market Data - New Broadcast Parameters in Futures & Options Segment
---

## Summary

NSE is modifying market data broadcast parameters in the Futures & Options (F&O) segment as a follow-up to circular NSE/MSD/74019 dated April 30, 2026. The key change involves upgrading the data type for token level cumulative volume (total traded volume) from Unsigned Integer (4 bytes) to LONG (8 bytes). New broadcast parameters will enhance data dissemination for Market by Price (MBP) updates, Market Watch updates, and Bhavcopy broadcasts.

## Key Points

- New broadcast parameters introduced for F&O segment covering price volume (5 depth, 1 second refresh), master updates, and market open/close status messages
- Data type for token level cumulative volume upgraded from Unsigned Integer (4 bytes) to LONG (8 bytes)
- Enhanced data dissemination for MBP update, Market Watch update, and Bhavcopy broadcast
- An interim coexistence period will be provided where both existing and new parameters will be active simultaneously
- No change in UDP application version
- Members must receive market data from a single parameter at a time (either existing or new)
- New transcodes (1833, 7201, 17208, 17211) introduced; existing transcodes (except 11833, 17201, 7208, 7211) remain available in new broadcast parameters

## Regulatory Changes

This is a modification to circular NSE/MSD/74019 dated April 30, 2026. The exchange is introducing new broadcast parameters for F&O segment market data:
- Table A: New message broadcast parameters for FO segment at 1-second frequency with 5 depth data
- Table B: New additional stream parameters for all streams in FO segment at 1-second frequency with 5 depth data

## Compliance Requirements

- Members must update systems to receive new broadcast parameters effective May 11, 2026
- Members must ensure all necessary SOP, policies, procedures, and mechanisms are in place to switch back to existing parameters if required during the coexistence period
- Members should not receive data from both existing and new parameters simultaneously
- Members must refer to the latest NNF API document (Version 9.48) for implementation details
- NNF API document available at: https://www.nseindia.com/trade/platform-services-neat-trading-system-protocols

## Important Dates

- **May 09, 2026**: Mock release of new market data broadcast parameters (5 depth, 1 second refresh)
- **May 09, 2026**: Release of new NEAT version with new broadcast market data parameters
- **May 11, 2026**: Go-live of new broadcast parameters in the live environment
- **TBD**: Discontinuation of existing market data broadcast parameters for NNF users (to be communicated separately)

## Impact Assessment

This change primarily impacts trading members and their technology teams who consume NSE F&O market data feeds. The upgrade from 4-byte Unsigned Integer to 8-byte LONG for cumulative volume allows for larger volume values, preventing potential overflow issues as trading volumes grow. Members using NNF (NEAT Next Generation) and NEAT platforms will need to update their systems before May 11, 2026. The coexistence period provides a safety net for gradual migration, but members must plan and test their system updates promptly. No impact on trading rules, listed securities, or retail investors.