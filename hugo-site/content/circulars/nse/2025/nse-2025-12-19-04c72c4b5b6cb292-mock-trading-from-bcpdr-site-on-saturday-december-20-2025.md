---
category: market-operations
circular_id: 04c72c4b5b6cb292
date: '2025-12-19'
description: NSE will conduct mock trading sessions from Primary and BCP/DR sites
  on December 20, 2025, followed by a re-login session to avoid Monday login issues.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/SLBS71909.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Scheduled mock trading session for business continuity testing; affects
  all SLBS members but limited to weekend operations with no financial obligations
pdf_url: https://nsearchives.nseindia.com/content/circulars/SLBS71909.pdf
processing:
  attempts: 1
  content_hash: 8ee9634b4ecfe0e9
  processed_at: '2025-12-19T12:45:49.017486'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-19T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/SLBS71909.pdf
severity: medium
source: nse
stocks: []
tags:
- mock-trading
- bcp
- disaster-recovery
- dr-site
- securities-lending-borrowing
- slbs
- system-testing
title: Mock Trading from BCP/DR Site on Saturday, December 20, 2025
---

## Summary

NSE will conduct a mock trading session for Securities Lending and Borrowing Market on Saturday, December 20, 2025. The session includes trading from Primary site (9:15 AM - 12:00 PM), BCP/DR site (1:00 PM - 5:00 PM), and a re-login session from Primary site (6:30 PM - 7:00 PM) to prevent login problems on Monday, December 22, 2025.

## Key Points

- Mock trading session scheduled for December 20, 2025 from Primary and BCP/DR sites
- Non-graceful shutdown from primary site during transition to DR site
- All outstanding orders will be purged before BCP site trading starts
- No changes required in NEAT Adapter settings from Friday, December 19, 2025 configuration
- Members using NNF software must manually clear outstanding orders before BCP site trading
- No financial obligations - trades during mock sessions will not result in fund pay-in or pay-out
- NEAT version 1.3.3 to be used
- Connect2NSE and Extranet facility unavailable from 11:00 AM to 12:30 PM
- NOTIS application accessible during mock session-2

## Regulatory Changes

No regulatory changes introduced. This is a business continuity and disaster recovery testing exercise.

## Compliance Requirements

- Members must retain NEAT Adapter settings from live session of December 19, 2025
- Members must take necessary action per circular NSE/MSD/48662 dated June 18, 2021 to bring systems into consistent state during non-graceful shutdown
- Members using NNF software must clear outstanding orders of session 1 before trading from BCP site
- Only valid and compliant UCC/PAN uploaded and approved before cutoff will be allowed (per circulars NSE/ISC/51754 and NSE/ISC/52722)
- Members should refer to annexures for operational instructions, prerequisites, DR site guidelines, and algorithmic trading guidelines

## Important Dates

- **December 20, 2025, 9:15 AM - 12:00 PM**: Mock trading from Primary Site
- **December 20, 2025, 1:00 PM - 5:00 PM**: Mock trading from BCP Site
- **December 20, 2025, 6:30 PM - 7:00 PM**: Re-login Session from Primary Site
- **December 20, 2025, 11:00 AM - 12:30 PM**: Connect2NSE and Extranet unavailable
- **December 22, 2025**: Regular trading resumes on Monday

## Impact Assessment

**Operational Impact**: Medium - All SLBS members required to participate in weekend mock trading sessions. Members must ensure systems are properly configured and capable of handling switchover from primary to DR site. The non-graceful shutdown requires members to have procedures in place to maintain system consistency.

**Market Impact**: Low - Mock session conducted on Saturday with no financial obligations. No real trades or settlements occur. Primary purpose is to test business continuity and disaster recovery procedures to ensure smooth operations during actual contingencies.

**Technical Impact**: Medium - Members need to ensure connectivity readiness, manage order purging, and handle system transitions. UCC validation will be skipped during contingency time for order entry, but only pre-approved valid UCCs can participate otherwise.