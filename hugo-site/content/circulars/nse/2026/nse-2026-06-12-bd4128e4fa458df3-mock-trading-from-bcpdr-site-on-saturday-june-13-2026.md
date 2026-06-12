---
category: market-operations
circular_id: bd4128e4fa458df3
date: '2026-06-12'
description: NSE Currency Derivatives segment will conduct a mock trading session
  on June 13, 2026 from both Primary and BCP/DR sites, followed by a Re-Login session
  from Primary site to prevent login issues on June 15, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPL74698.zip
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine scheduled mock/DR trading session with no financial obligations;
  affects only Currency Derivatives segment members on a Saturday.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPL74698.zip
processing:
  attempts: 1
  content_hash: 1131dba58fa529f0
  processed_at: '2026-06-12T17:48:07.397246'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-12T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPL74698.zip
severity: low
source: nse
stocks: []
tags:
- mock-trading
- bcp
- disaster-recovery
- currency-derivatives
- neat
title: Mock Trading from BCP/DR Site on Saturday, June 13, 2026 - Currency Derivatives
---

## Summary

NSE will conduct a mock trading session on Saturday, June 13, 2026 for the Currency Derivatives segment from both Primary and BCP/DR sites. A Re-Login session from the Primary site is scheduled afterward to prevent login issues on Monday, June 15, 2026. No financial pay-in or pay-out will result from trades executed during the mock session.

## Key Points

- Mock trading from Primary Site (Session 1): 09:00 – 11:00
- Mock trading from BCP Site (Session 2): 11:45 – 17:00 (trade modification end: 17:30)
- Re-Login session from Primary Site: 18:30 – 19:00
- No changes to NEAT Adapter settings required; retain live settings from June 12, 2026
- All outstanding orders will be purged before trading begins from BCP site
- Multicast TBT sequence numbers will reset to '1' upon BCP site trading commencement
- Colo Participants will experience different latencies on DR/BCP day vs. normal trading days
- NEAT version 3.5.4; Adapter versions 1.0.29 & 1.0.27

## Regulatory Changes

No regulatory changes. This is a scheduled operational drill for business continuity and disaster recovery preparedness.

## Compliance Requirements

- Members using NNF software must manually clear outstanding orders from Session 1 before connecting to BCP site.
- Members should refer to circular NSE/MSD/48662 (June 18, 2021) for actions required during non-graceful primary site shutdown.
- Only UCC/PAN uploaded and approved before the cutoff will be permitted; UCC validation will be skipped during contingency.
- Software testing using mock or simulated environment must comply with SEBI circular SEBI/HO/MRD1/DSAP/CIR/P/2020/234.
- Connectivity details available in circular NSE/MSD/74511 dated June 02, 2026.

## Important Dates

- **June 13, 2026 (Saturday):** Mock trading session (Primary 09:00–11:00; BCP 11:45–17:00; Re-Login 18:30–19:00)
- **June 15, 2026 (Monday):** Live trading resumes; Re-Login session on June 13 intended to prevent login issues

## Impact Assessment

Impact is limited to Currency Derivatives segment members participating in mock trading on a non-trading Saturday. No financial obligations arise from this session. Members with automated or co-location systems should prepare for sequence number resets and latency differences during BCP operation. Overall market impact is negligible.