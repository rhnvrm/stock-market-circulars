---
category: market-operations
circular_id: d6fadc8c8062952d
date: '2025-12-19'
description: NSE to conduct mock trading session from Primary and BCP/DR sites on
  December 20, 2025, followed by re-login session from Primary site to avoid login
  issues on December 22, 2025.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CD71910.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Routine BCP/DR mock session for currency derivatives segment requiring
  member participation to test disaster recovery capabilities and prevent login issues
pdf_url: https://nsearchives.nseindia.com/content/circulars/CD71910.pdf
processing:
  attempts: 1
  content_hash: bae51042230c6eb5
  processed_at: '2025-12-19T12:46:43.759504'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-19T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CD71910.pdf
severity: medium
source: nse
stocks: []
tags:
- mock-trading
- bcp
- disaster-recovery
- currency-derivatives
- trading-session
- dr-site
title: Mock Trading from BCP/DR Site on Saturday, December 20, 2025
---

## Summary

NSE Currency Derivatives segment will conduct a mock trading session on Saturday, December 20, 2025, from both Primary and BCP/DR sites. The mock session includes three phases: morning trading from Primary site (09:00-12:00), afternoon trading from BCP site (12:45-17:30), and a re-login session from Primary site (18:30-19:00). This exercise is designed to test disaster recovery preparedness and prevent login problems on Monday, December 22, 2025.

## Key Points

- Mock trading session scheduled for Saturday, December 20, 2025
- Three distinct trading sessions planned throughout the day
- Exchange will perform non-graceful shutdown when switching from Primary to DR site
- All outstanding orders will be purged before BCP site trading begins
- No changes required in NEAT Adapter settings for connecting to Primary/DR site
- Multicast TBT sequence numbers will restart from '1' when trading starts from BCP site
- Colo participants will experience different latencies on DR/BCP day compared to normal trading
- NEAT version 3.5.4 to be used
- No financial obligations - trades will not result in fund pay-in or pay-out

## Regulatory Changes

No regulatory changes introduced. This is a routine business continuity and disaster recovery testing exercise.

## Compliance Requirements

- Members must retain NEAT Adapter settings from Friday, December 19, 2025 for all sessions
- Members must take necessary action per circular NSE/MSD/48662 dated June 18, 2021 to bring systems into consistent state during non-graceful shutdown
- Members using NNF software must manually clear outstanding orders from session 1 before trading from BCP site
- Members should refer to specified annexures for operational instructions and guidelines
- Software testing requirements per circular NSE/MSD/46441 and SEBI circular SEBI/HO/MRD1/DSAP/CIR/P/2020/234
- Only valid UCC/PAN as per circulars NSE/ISC/51754 and NSE/ISC/52722

## Important Dates

- **December 19, 2025**: Last live trading day before mock session (Friday)
- **December 20, 2025, 09:00-12:00**: Mock Trading Session-1 from Primary Site
- **December 20, 2025, 12:45-17:00**: Mock Trading Session-2 from BCP Site
- **December 20, 2025, 17:30**: Trade modification end time
- **December 20, 2025, 18:30-19:00**: Re-Login Session from Primary Site
- **December 22, 2025**: Next live trading day (Monday)

## Impact Assessment

**Market Impact**: Low - Mock session occurs on Saturday when markets are normally closed, with no financial obligations from trades executed during the session.

**Operational Impact**: Medium - Members must actively participate in all three sessions and follow specific technical procedures. The non-graceful shutdown during switchover from Primary to DR site requires members to take corrective actions at their end. Members using NNF software must manually clear orders between sessions. Colo participants should expect different latency profiles during the DR/BCP session compared to normal trading days.

**Technical Requirements**: Members must ensure their systems can handle sequence number resets for Multicast TBT and maintain connectivity across site transitions without requiring NEAT Adapter reconfiguration.