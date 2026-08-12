---
category: market-operations
circular_id: 5a96a5c51e9d655c
date: '2026-08-07'
description: NSE is conducting a mock trading session in the Futures & Options segment
  on August 08, 2026, with no new NEATPlus software release. Crucial migration dates
  for broadcast parameters are outlined.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP75622.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Mock trading sessions are routine operational exercises with no financial
  obligations. However, there is an upcoming technical deadline for broadcast parameters
  migration by September 05, 2026.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP75622.pdf
processing:
  attempts: 1
  content_hash: ed214e7111be990a
  last_updated: '2026-08-12T19:40:56.369525'
  processed_at: '2026-08-12T19:40:47.313899'
  processor_version: '2.0'
  retry_requested_for_stage: claude_failed
  retry_source: backfill
  stage: completed
  status: published
published_date: '2026-08-07T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP75622.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- futures-and-options
- nse
- market-data
- connectivity
title: Mock Trading on Saturday, August 08, 2026 - No New Version Release
---

## Summary

The National Stock Exchange of India (NSE) has scheduled a mock trading session in the Futures & Options (F&O) segment on Saturday, August 08, 2026. No new version of the NEATPlus trading software is being released; versions 7.8.8 and 7.8.9 remain compatible. The mock session will test transition capabilities from both the Primary and Disaster Recovery (DR) sites. Additionally, members are warned that existing market data broadcast parameters will be discontinued from September 05, 2026, and priority migration is recommended.

## Key Points

- **Mock Trading Date**: Saturday, August 08, 2026.
- **Timings**: 
  - Session 1 (Primary Site): Pre-Open from 11:00 to 11:08; Normal Market from 11:15 to 13:30.
  - Session 2 (DR Site): Pre-Open from 14:15 to 14:23; Normal Market from 14:30 to 15:15.
- **Software Versions**: NEATPlus versions 7.8.8 and 7.8.9 are fully compatible with new broadcast parameters.
- **Broadcast Parameters Discontinuation**: Existing parameters will be discontinued from September 05, 2026. Members using NNF direct connections must migrate to the new parameters on priority.
- **Price Band Determination**: Reference prices for stock futures contacts during CAS (Call Auction Session) in the Capital Market segment will be based on the Volume Weighted Average Price (VWAP) of respective stock futures between 15:00 and 15:15 hours.

## Regulatory Changes

- **CAS Price Band Alignment**: Aligns the stock futures price bands applicable during the Call Auction Session (CAS) in the Capital Market (CM) segment with a reference price determined using the VWAP of trades executed between 15:00 and 15:15 hours.

## Compliance Requirements

- **Technical Migration**: Members using direct connection via NNF must plan to migrate to the new market data broadcast parameters prior to September 05, 2026.
- **Order Purging**: All outstanding orders will be automatically cleared before each session. Members using NNF software must manually clear orders in their systems.
- **UCC/PAN Validity**: Only valid, approved and fully compliant UCC/PANs uploaded before the cutoff will be permitted to participate. UCC validation will be skipped only during contingency time for order entry.

## Important Dates

- **August 07, 2026**: Circular publication date.
- **August 08, 2026**: F&O mock trading session date.
- **September 05, 2026**: Deadline/discontinuation date for existing broadcast parameters and mock discontinuation date for NEATPlus version 7.8.8.

## Impact Assessment

- **Operational Impact**: Low. There are no financial obligations or pay-in/pay-out settlements resulting from mock trading sessions.
- **Technical Impact**: Medium. IT and trading systems teams must prioritize migrating NNF broadcast parameters to avoid service disruptions when old parameters are retired on September 05, 2026.