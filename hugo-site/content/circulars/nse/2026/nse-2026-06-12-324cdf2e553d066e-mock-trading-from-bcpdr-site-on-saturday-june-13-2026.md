---
category: market-operations
circular_id: 324cdf2e553d066e
date: '2026-06-12'
description: NSE will conduct a mock trading session on June 13, 2026 from both Primary
  and BCP/DR sites for Commodity Derivatives, followed by a Re-Login session from
  Primary site to avoid login issues on June 15, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/COM74694.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for BCP/DR site testing with no financial
  obligations; affects only members participating in Commodity Derivatives segment
  and has no impact on regular investors or securities.
pdf_url: https://nsearchives.nseindia.com/content/circulars/COM74694.pdf
processing:
  attempts: 1
  content_hash: 66412ab212142748
  processed_at: '2026-06-12T15:09:15.487255'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-12T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/COM74694.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- bcp
- disaster-recovery
- commodity-derivatives
- neat
- settlement-calendar
title: Mock Trading from BCP/DR Site on Saturday, June 13, 2026
---

## Summary

NSE's Commodity Derivatives department has scheduled a mock trading session on Saturday, June 13, 2026, covering both Primary and BCP (Business Continuity Plan) / DR (Disaster Recovery) sites. The exercise is designed to test failover procedures and ensure members are prepared for potential site switchovers. A Re-Login session from Primary site will follow to pre-empt login issues on the next trading day, Monday June 15, 2026. No financial obligations arise from trades executed during mock sessions.

## Key Points

- Mock trading Session 1 (Primary Site): Normal Market open 09:00, close 11:00
- Mock trading Session 2 (BCP Site): Normal Market open 11:45, close 17:00; Trade modification end 17:15
- Re-Login Session (Primary Site): Live Re-login start 18:30, close 19:00
- No changes to NEAT Adapter settings are required; live settings from June 12, 2026 are retained
- Exchange will perform a non-graceful shutdown from the Primary site when switching to DR site
- All outstanding orders will be purged before each session starts
- Members using NNF software must manually clear Session 1 outstanding orders before trading from BCP site
- Multicast TBT sequence numbers will reset to '1' when trading starts from BCP site
- Only valid and compliant UCC/PAN approved before cutoff will be permitted
- NEAT version 1.5.5; NEAT Adapter versions 1.0.29 & 1.0.27

## Regulatory Changes

No regulatory changes. This is an operational readiness exercise referencing existing circulars:
- NSE/MSD/48662 dated June 18, 2021 (actions during non-graceful primary site shutdown)
- NSE/MSD/74511 dated June 02, 2026 (interactive connectivity details)
- NSE/MSD/46441 and SEBI/HO/MRD1/DSAP/CIR/P/2020/234 (software testing requirements)

## Compliance Requirements

- Members must retain NEAT Adapter settings from the live session of June 12, 2026 for all mock sessions
- Members using NNF software must manually clear outstanding orders from Session 1 before connecting to the BCP site
- Members should take necessary action per NSE/MSD/48662 in case of non-graceful shutdown
- UCC/PAN must be valid, compliant, uploaded, and approved before the applicable cutoff
- Members may use either Mock Trading or Simulated Environment to meet SEBI regulatory software testing requirements

## Important Dates

- **June 12, 2026 (Friday):** NEAT Adapter live settings to be retained for mock sessions
- **June 13, 2026 (Saturday):** Mock trading day
  - 09:00 – 11:00: Session 1 from Primary Site
  - 11:45 – 17:00: Session 2 from BCP Site (trade modification until 17:15)
  - 18:30 – 19:00: Re-Login Session from Primary Site
- **June 15, 2026 (Monday):** Next live trading day; Re-Login session on June 13 is intended to avoid login issues on this day

## Impact Assessment

This is a routine operational drill with no financial impact on members or investors. Trades executed during mock sessions do not result in any fund pay-in or pay-out. The primary operational consideration for members is ensuring their systems handle the non-graceful Primary-to-DR switchover correctly, clearing NNF outstanding orders between sessions, and noting the Multicast TBT sequence number reset. Members who do not participate in Commodity Derivatives are unaffected.