---
category: market-operations
circular_id: 7be6e5dd862a037f
date: '2025-12-19'
description: NSE will conduct mock trading session from Primary and BCP/DR sites on
  December 20, 2025, followed by Re-Login session to avoid login issues on December
  22, 2025.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/COM71911.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational mock session to ensure business continuity preparedness;
  no financial impact but requires member participation for testing DR site failover
  procedures
pdf_url: https://nsearchives.nseindia.com/content/circulars/COM71911.pdf
processing:
  attempts: 1
  content_hash: b208e8c399adfdb7
  processed_at: '2025-12-19T12:46:15.938607'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-19T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/COM71911.pdf
severity: medium
source: nse
stocks: []
tags:
- mock-trading
- bcp
- disaster-recovery
- commodity-derivatives
- system-testing
- contingency
title: Mock Trading from BCP/DR Site on Saturday, December 20, 2025
---

## Summary

NSE Commodity Derivatives segment will conduct a mock trading session on Saturday, December 20, 2025, from both Primary and BCP/DR sites. The mock will include trading from Primary site (09:00-12:00 hrs), BCP site (12:45-17:15 hrs), and a Re-Login session from Primary site (18:30-19:00 hrs) to prevent login issues on Monday, December 22, 2025.

## Key Points

- Mock trading session scheduled for December 20, 2025 (Saturday)
- Primary site session: 09:00 to 12:00 hrs
- BCP/DR site session: 12:45 to 17:15 hrs (trade modification ends at 17:15)
- Re-Login session from Primary site: 18:30 to 19:00 hrs
- Non-graceful shutdown will occur during switchover from Primary to DR site
- All outstanding orders will be purged before BCP site trading starts
- No changes required in NEAT Adapter settings
- Multicast TBT sequence numbers will restart from '1' when trading begins from BCP site
- NOTIS application will be accessible during session-2
- NEAT Version: 1.5.3

## Regulatory Changes

No regulatory changes introduced. This is a business continuity and disaster recovery testing exercise as per existing SEBI requirements for exchange infrastructure resilience.

## Compliance Requirements

- Members must retain Friday, December 19, 2025 NEAT Adapter settings for all sessions
- Members using NNF software must manually clear outstanding orders from session 1 before trading from BCP site
- Members should follow instructions per circular NSE/MSD/48662 dated June 18, 2021 to bring systems into consistent state during non-graceful shutdown
- UCC/PAN validity requirements apply as per circulars NSE/ISC/51754 (March 24, 2022) and NSE/ISC/52722 (June 23, 2022) - only valid and compliant UCC/PAN uploaded before cutoff will be allowed
- Members should refer to software testing requirements per circular NSE/MSD/46441 and SEBI circular SEBI/HO/MRD1/DSAP/CIR/P/2020/234

## Important Dates

- **December 19, 2025**: Last day for retaining NEAT Adapter settings
- **December 20, 2025**:
  - 09:00-12:00 hrs: Mock trading from Primary site
  - 12:45-17:00 hrs: Mock trading from BCP site
  - 17:15 hrs: Trade modification end time
  - 18:30-19:00 hrs: Re-Login session from Primary site
- **December 22, 2025**: Regular trading resumes (Monday)

## Impact Assessment

**Operational Impact**: Members must participate in the mock session to test their systems' ability to handle failover scenarios. The non-graceful shutdown during switchover simulates real disaster recovery conditions, requiring members to verify their infrastructure readiness.

**Market Impact**: No financial obligations or actual settlements will arise from mock trading. All trades are for testing purposes only.

**Technical Impact**: Members need to ensure their systems can handle order purging, sequence number resets for Multicast TBT, and connectivity switches between Primary and DR sites without manual intervention issues.

**Risk Mitigation**: The Re-Login session on Saturday evening is specifically designed to prevent potential login failures when regular trading resumes on Monday, reducing operational risk for the start of the trading week.