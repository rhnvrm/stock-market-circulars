---
category: market-operations
circular_id: ccef1d4c65ebfc24
date: '2026-06-12'
description: NSE Currency Derivatives segment will conduct a mock trading session
  on June 13, 2026 from both Primary and BCP/DR sites, followed by a re-login session
  from Primary site to ensure smooth operations on Monday, June 15, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CD74692.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading/BCP drill with no financial obligations or regulatory
  changes; affects only Currency Derivatives members on a Saturday.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CD74692.pdf
processing:
  attempts: 1
  content_hash: 1c2314d271157c2a
  processed_at: '2026-06-12T15:10:16.185366'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-12T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CD74692.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- bcp
- disaster-recovery
- currency-derivatives
- neat
- ucc
- nse
title: Mock Trading from BCP/DR Site on Saturday, June 13, 2026 – Currency Derivatives
---

## Summary

NSE Currency Derivatives (CD) segment will conduct a mock trading session on Saturday, June 13, 2026, covering both the Primary site and the BCP (Business Continuity Plan) / DR (Disaster Recovery) site. A re-login session from the Primary site will follow in the evening to prevent login issues on Monday, June 15, 2026. No funds pay-in or pay-out will occur for trades executed during this mock session.

## Key Points

- **Primary Site – Trading Session 1:** Normal Market open 09:00 hrs, close 11:00 hrs.
- **BCP Site – Trading Session 2:** Normal Market open 11:45 hrs, close 17:00 hrs; trade modification end time 17:30 hrs.
- **Re-Login from Primary Site:** Start 18:30 hrs, close 19:00 hrs.
- No changes to NEAT Adapter settings are required; live session settings as of Friday, June 12, 2026 will be retained.
- The Exchange will perform a non-graceful shutdown from the Primary site during switchover to BCP; members must take necessary action per circular NSE/MSD/48662 dated June 18, 2021.
- All outstanding orders will be purged before the start of trading from BCP site; NNF software users must manually clear outstanding orders from Session 1.
- For Multicast TBT, sequence numbers will restart from '1' once trading begins from BCP site.
- Colo Participants will experience different latencies on BCP/DR day compared to normal trading days.
- NEAT version: **3.5.4**; NEAT Adapter version: **1.0.29 & 1.0.27**.
- NOTIS application will be accessible during the mock session.
- Only valid and compliant UCC/PAN uploaded and approved before cutoff will be permitted; UCC validation will be skipped during contingency time for order entry.

## Regulatory Changes

No regulatory changes. This is an operational mock/BCP drill circular issued under the Currency Derivatives segment.

## Compliance Requirements

- Members must retain live NEAT Adapter settings from Friday, June 12, 2026 for connectivity to all sessions.
- Members using NNF software must manually clear outstanding orders from Session 1 before participating in the BCP site session.
- Members must follow circular NSE/MSD/48662 (June 18, 2021) procedures in case of non-graceful Primary site shutdown.
- Refer to Annexure 1 (operational instructions), Annexure 2 (prerequisites/general guidelines), and Annexure 3 (DR switchover guidelines) for complete instructions.
- Software testing compliance may be met using the Mock Trading or Simulated Environment per SEBI/HO/MRD1/DSAP/CIR/P/2020/234.
- Connectivity details available in circular NSE/MSD/74511 dated June 02, 2026.

## Important Dates

- **June 12, 2026 (Friday):** NEAT Adapter settings baseline date; retain for all mock sessions.
- **June 13, 2026 (Saturday):** Mock trading day.
  - Primary Site Session 1: 09:00–11:00 hrs
  - BCP Site Session 2: 11:45–17:00 hrs (trade modification end: 17:30 hrs)
  - Re-Login from Primary: 18:30–19:00 hrs
- **June 15, 2026 (Monday):** Live trading resumes; re-login session aims to prevent login issues.

## Impact Assessment

This is a routine BCP/DR drill with minimal market impact. All trades executed during the mock session carry no financial obligation (no fund pay-in or pay-out). Currency Derivatives segment members must prepare for sequence number resets on Multicast TBT feeds and should expect higher latencies for Colo Participants on the BCP day. Members using automated NNF systems need manual intervention to clear outstanding orders before the BCP session. The re-login session at 18:30–19:00 hrs is designed to ensure a smooth start on Monday, June 15, 2026.