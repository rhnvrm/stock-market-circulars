---
category: market-operations
circular_id: de8814b5ac63968f
date: '2026-07-21'
description: NSE has fixed September 05, 2026 as the discontinuation date for existing
  market data broadcast parameters (5 depth, 1 second refresh) for NNF users in the
  F&O segment, requiring members to migrate to new broadcast parameters with no further
  extension.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD75324.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operationally important for trading members using NNF connectivity
  as it mandates a hard migration deadline for market data feeds, but has no direct
  impact on listed securities or broader market participants.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD75324.pdf
processing:
  attempts: 1
  content_hash: 1d6b1e363e6da89e
  processed_at: '2026-07-21T16:35:05.624638'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-07-21T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD75324.pdf
severity: medium
source: nse
stocks: []
tags:
- market-data
- futures-and-options
- nnf
- broadcast-parameters
title: NSE to Discontinue Existing Broadcast Parameters in Futures & Options Segment
  from September 05, 2026
---

## Summary

NSE has issued a follow-up circular to its earlier communications (NSE/MSD/74133 dated May 08, 2026 and NSE/MSD/74448 dated May 27, 2026) regarding new broadcast parameters for market data in the Futures & Options (F&O) segment. The Exchange had earlier introduced new broadcast parameters to change the data type for token-level cumulative volume (total traded volume) from 'Unsigned Integer' (4 bytes) to 'LONG' (8 bytes), along with a coexistence phase during which both existing and new parameters were broadcast simultaneously. This circular now specifies the discontinuation date for the existing (old) broadcast parameters, after which only the new parameters will be available.

## Key Points

- Members using NNF (NEAT NNF) must note the discontinuation date for existing market data broadcast parameters.
- The existing broadcast parameters cover combined broadcast streams (price volume with 5 depth, 1 second refresh, other related data, master updates, market open/close status messages) as well as stream-wise broadcasts on additional streams in the F&O segment.
- Annexure 1 lists the existing broadcast parameters (multicast IPs, ports, and approximate bandwidth utilization) that will be discontinued.
- Annexure 2 lists the applicable (new) market data broadcast parameters members must migrate to.
- No further extension will be provided beyond the specified discontinuation timeline.
- All other details from the earlier referenced circulars remain unchanged.

## Regulatory Changes

This circular does not introduce new regulatory requirements but operationalizes a previously announced technical change — finalizing the end date of the coexistence period for old and new market data broadcast parameters in the F&O segment.

## Compliance Requirements

Members using NNF connectivity must migrate their systems to consume market data via the new broadcast parameters (Annexure 2) before the discontinuation date. Continued reliance on the existing parameters listed in Annexure 1 will result in loss of market data feed after the cutover, as the Exchange will not extend the timeline.

## Important Dates

- Discontinuation of existing market data broadcast parameters (5 depth, 1 second refresh) for NNF users: September 05, 2026 onwards.

## Impact Assessment

The impact is primarily technical and operational, affecting trading members and vendors who consume NSE's F&O market data via NNF broadcast. Firms that fail to migrate their data-handling systems (to support the 8-byte LONG data type for cumulative volume) before September 05, 2026 risk disruption to their market data feeds, which could affect trading and risk systems reliant on real-time F&O price/volume data. There is no direct impact on listed securities, investors, or broader market pricing.