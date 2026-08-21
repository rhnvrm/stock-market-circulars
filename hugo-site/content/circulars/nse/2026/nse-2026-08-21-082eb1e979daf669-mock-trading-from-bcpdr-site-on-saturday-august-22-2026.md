---
category: market-operations
circular_id: 082eb1e979daf669
date: '2026-08-21'
description: NSE is conducting a mock trading session from its BCP/DR site on Saturday,
  August 22, 2026, followed by a re-login session from the primary site.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMTR75876.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for market participants to test BCP/DR
  site connectivity and procedures.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMTR75876.pdf
processing:
  attempts: 1
  content_hash: 29e4af2bd598bccd
  processed_at: '2026-08-21T12:52:26.665795'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-08-21T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMTR75876.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- disaster-recovery
- capital-market
- trading-operations
title: Mock trading from BCP/DR site on Saturday, August 22, 2026
---

## Summary

The National Stock Exchange of India Limited (NSE) will conduct a mock trading session from the Business Continuity Plan (BCP) / Disaster Recovery (DR) site on Saturday, August 22, 2026, for the Capital Market segment. The session will be followed by a re-login session from the Primary site.

## Key Points

- Mock trading date: August 22, 2026.
- Includes morning block deal window, pre-open, normal market, T+0 market, call auction illiquid session, auction market, and closing sessions.
- Switchover from the primary site during the mock session will be a non-graceful shutdown.
- All outstanding orders will be purged before trading starts from the BCP site.
- Multicast TBT sequence number will start from '1' once trading begins from the BCP site.
- Live re-login start time is 18:30 hrs and close time is 19:00 hrs.

## Regulatory Changes

No regulatory changes; this is a routine operational mock drill.

## Compliance Requirements

- Members should ensure their systems are brought into a consistent state as per circular NSE/MSD/48662 in the event of a non-graceful shutdown.
- NNF software users should clear outstanding orders of session 1 before trading from the BCP site.
- No changes in NEAT Adapter settings are required to connect to the Primary/DR site.

## Important Dates

- Mock Trading Date: August 22, 2026
- Live Re-login Start: August 22, 2026 at 18:30 hrs
- Live Re-login Close: August 22, 2026 at 19:00 hrs

## Impact Assessment

Minimal operational impact on live trading days as this is a scheduled Saturday mock session designed to ensure system readiness and prevent login issues on Monday, August 24, 2026.