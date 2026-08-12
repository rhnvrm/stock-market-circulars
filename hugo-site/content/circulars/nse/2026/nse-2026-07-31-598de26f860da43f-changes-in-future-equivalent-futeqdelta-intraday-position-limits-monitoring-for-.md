---
category: market-operations
circular_id: 598de26f860da43f
date: '2026-07-31'
description: NSE has announced changes to intraday position limit monitoring (introducing
  a fifth snapshot and eliminating the cure period post-14:45 hrs) and Order to Trade
  Ratio (OTR) calculations during the Closing Auction Session (CAS).
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/SURV75524.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: This circular modifies intraday position monitoring and OTR calculations
  for equity derivatives and cash segment stocks during the Closing Auction Session,
  directly affecting risk management and trading operations.
pdf_url: https://nsearchives.nseindia.com/content/circulars/SURV75524.pdf
processing:
  attempts: 1
  content_hash: 5dbde37d92f46af3
  last_updated: '2026-08-12T22:37:55.066119'
  processed_at: '2026-08-12T22:37:46.000858'
  processor_version: '2.0'
  retry_requested_for_stage: claude_failed
  retry_source: backfill
  stage: completed
  status: published
published_date: '2026-07-31T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/SURV75524.pdf
severity: medium
source: nse
stocks: []
tags:
- position-limits
- equity-index-derivatives
- order-to-trade-ratio
- closing-auction-session
- surveillance
- nse
- sebi
title: Changes in Future Equivalent (FutEq)/(Delta) Intraday Position Limits Monitoring
  for Equity Index Derivatives and Order to Trade Ratio (OTR) on account of Closing
  Auction Session (CAS)
---

## Summary

This circular from the National Stock Exchange of India (NSE) details changes in the framework for monitoring Future Equivalent (FutEq) / Delta Intraday Position Limits for Equity Index Derivatives and the Order to Trade Ratio (OTR) in the cash segment due to the Closing Auction Session (CAS).

## Key Points

- No intraday snapshots will be taken during the CAS period until the equilibrium price of the index is determined.
- An additional (fifth) snapshot will be added post-equilibrium price determination up to 15:40 hrs.
- The standard 15-minute cure period will not apply to any snapshots taken after 14:45 hrs.
- The closing price of the underlying index will be utilized in delta computations and contract valuation for snapshots taken post-equilibrium price.
- Same-day expiring contracts (where Expiry Date = Trade Date) are included in all intraday monitoring snapshots.
- Orders placed during CAS will be excluded from the computation of the Order to Trade Ratio (OTR) in the cash segment for stocks available in CAS.

## Regulatory Changes

- Modification of intraday position limit monitoring snapshots, increasing the minimum from four to five during the day by adding a snapshot from index equilibrium price determination to 15:40 hrs.
- Discontinuation of the 15-minute cure period for snapshots taken post-14:45 hrs.
- Adjustment of Time to Expiry for delta calculation as per Black & Scholes formula to reflect the revised derivatives market close time of 15:40 hrs on expiry days.
- Amendment to cash segment OTR calculation rules to exclude CAS orders for applicable stocks.

## Compliance Requirements

- **Surveillance and Risk Management**: Trading members must adapt their risk management systems to align with the five intraday snapshots and the exclusion of the 15-minute cure period post-14:45 hrs.
- **Delta Computation & Valuation**: Update Black & Scholes formula parameters to incorporate the revised derivatives market close time of 15:40 hrs on expiry days, and use close prices post-equilibrium.
- **OTR Monitoring**: Adjust internal OTR tracking mechanisms to exclude cash segment orders placed during the CAS for CAS-eligible stocks.

## Important Dates

- **Circular Date**: July 31, 2026.
- **Effective Date**: Immediate, as of the date of the circular.

## Impact Assessment

- **Operational Impact**: High. Trading members must quickly calibrate their automated trading systems, risk management systems, and surveillance alerts to prevent false positives or compliance breaches under the new snapshot timings and rules.
- **Market Impact**: Medium. These rules ensure that intraday margin and position limit computations are aligned with the realities of the Closing Auction Session pricing, while preventing artificial OTR penalties due to CAS orders.