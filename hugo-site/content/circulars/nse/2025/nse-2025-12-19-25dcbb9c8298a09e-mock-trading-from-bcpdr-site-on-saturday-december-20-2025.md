---
category: market-operations
circular_id: 25dcbb9c8298a09e
date: '2025-12-19'
description: NSE will conduct mock trading sessions from Primary and BCP/DR sites
  on December 20, 2025, followed by a re-login session to avoid login issues on December
  22, 2025.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP71907.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Mandatory mock trading session for testing BCP/DR infrastructure; affects
  all F&O members but is scheduled exercise with no financial obligations
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP71907.pdf
processing:
  attempts: 1
  content_hash: 53e47812b46215cc
  processed_at: '2025-12-19T12:47:12.741079'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-19T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP71907.pdf
severity: medium
source: nse
stocks: []
tags:
- mock-trading
- bcp
- dr-site
- disaster-recovery
- business-continuity
- futures-and-options
- system-testing
- trading-session
title: Mock Trading from BCP/DR Site on Saturday, December 20, 2025
---

## Summary

NSE will conduct a mock trading session on Saturday, December 20, 2025 from both Primary and BCP/DR sites to test business continuity and disaster recovery systems. The mock will include two trading sessions followed by a re-login session from the Primary site to prevent login problems on Monday, December 22, 2025. All members are required to participate.

## Key Points

- Mock trading scheduled for Saturday, December 20, 2025 with two sessions
- Session 1 from Primary Site: 09:00 to 12:00 (pre-open 09:00-09:08, market 09:15-12:00)
- Session 2 from BCP Site: 12:45 to 15:30 (pre-open 12:45-12:53, market 13:00-15:30)
- Re-login session from Primary Site: 18:30 to 19:00
- Non-graceful shutdown will occur when switching from Primary to DR site
- All outstanding orders will be purged before BCP site trading starts
- No changes required in NEAT Adapter settings from Friday, December 19, 2025
- Multicast TBT sequence numbers will restart from '1' when trading from BCP site
- NEAT version supported: NEATPlus 7.8.7 & 7.8.6
- Trade modification allowed until 16:15

## Regulatory Changes

No regulatory changes introduced. This is a scheduled mock trading exercise to test disaster recovery infrastructure as per existing SEBI requirements for business continuity planning.

## Compliance Requirements

- Members must participate in all three sessions (Primary mock, BCP mock, and re-login)
- Members using NNF software must manually clear outstanding orders from Session 1 before trading from BCP site
- Members should follow procedures outlined in circular NSE/MSD/48662 dated June 18, 2021 to bring systems into consistent state after non-graceful shutdown
- Members must refer to installation guide available on NSE Extranet at /faoftp/faocommon/Installation_Procedure
- Colo participants should note different latencies on DR/BCP day compared to normal trading
- Members should comply with SEBI circular SEBI/HO/MRD1/DSAP/CIR/P/2020/234 regarding software testing requirements

## Important Dates

- **December 19, 2025**: Circular issued; retain NEAT Adapter settings from this date
- **December 20, 2025**: 
  - 09:00-12:00: Mock trading from Primary Site
  - 12:45-15:30: Mock trading from BCP Site
  - 16:15: Trade modification end time
  - 18:30-19:00: Re-login session from Primary Site
- **December 22, 2025**: Normal trading resumes on Monday

## Impact Assessment

**Operational Impact**: Medium - All F&O members must participate in the mock sessions and ensure their systems can handle the switchover from Primary to DR site. The non-graceful shutdown requires members to take specific actions to maintain system consistency.

**Market Impact**: Low - No financial obligations arise from mock trading; no actual fund pay-in or pay-out will occur. This is purely a systems testing exercise.

**Technical Impact**: Medium - Members need to ensure their systems can handle order purging, sequence number resets, and different latencies. Colo participants will experience different latencies during DR operations.

**Member Preparedness**: The mock session tests critical business continuity infrastructure and ensures members can continue operations in case of actual disaster recovery scenarios.