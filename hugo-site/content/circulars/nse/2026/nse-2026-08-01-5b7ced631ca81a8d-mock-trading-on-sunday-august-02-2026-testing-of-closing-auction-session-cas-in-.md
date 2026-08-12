---
category: trading
circular_id: 5b7ced631ca81a8d
date: '2026-08-01'
description: NSE is conducting a mock trading session on August 02, 2026, to test
  trading modality changes from the newly introduced Closing Auction Session (CAS)
  in the Equity Cash segment, requiring NEAT+ version 7.8.9.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMTR75534.pdf
impact: low
impact_ranking: medium
importance_ranking: medium
justification: The mock session is of medium importance as it tests the newly introduced
  Closing Auction Session (CAS) in the Equity Cash segment and details the mandatory
  transition from NEAT+ 7.8.8 to 7.8.9. The impact is medium because it requires members
  to perform system upgrades and master loading prior to testing on a Sunday.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMTR75534.pdf
processing:
  attempts: 1
  content_hash: 028a6462c05bdecc
  last_updated: '2026-08-12T22:00:05.353982'
  processed_at: '2026-08-12T21:59:56.036395'
  processor_version: '2.0'
  retry_requested_for_stage: claude_failed
  retry_source: backfill
  stage: completed
  status: published
published_date: '2026-08-01T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMTR75534.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- capital-market
- equity
- closing-auction-session
- trading-platform
title: NSE Mock Trading Session on August 02, 2026 - Testing of Closing Auction Session
  (CAS) in Equity Cash Segment
---

## Summary

The National Stock Exchange of India Limited (NSE) has announced a mock trading session scheduled for Sunday, August 02, 2026. This session is designed to test critical changes in trading modalities due to the introduction of the Closing Auction Session (CAS) in the Equity Cash (Capital Market) segment. The mock trading will be conducted from the primary site, followed by a live re-login session. Members are required to use the updated NEAT+ version 7.8.9 for CAS related changes and ensure system readiness.

## Key Points

- **Closing Auction Session (CAS)**: The mock session is specifically for testing the transition and operational changes associated with CAS in the Equity Cash segment.
- **NEAT+ Version Mandate**: Members participating via NEATPlus must explicitly use version 7.8.9. The previous version (7.8.8) will be discontinued from September 05, 2026.
- **Master File Insertion**: Members must load specific master files, including `security.gz` and `participant.gz`, before commencing mock trading on August 02, 2026.
- **Re-login Verification**: A live re-login session is scheduled from 14:00 to 14:30 on the mock day to verify connection stability and system state.
- **Order Purge Policy**: All outstanding orders will be automatically cleared before each session. Non-NEATPlus (NNF) users must manually clear orders in their systems.

## Regulatory Changes

- **Closing Auction Segment Integration**: Modality changes due to the Closing Auction Session (CAS) are being integrated into the Capital Market segment trading rules.
- **Version Discontinuation**: NEAT+ version 7.8.8 is officially scheduled to be discontinued on September 05, 2026.

## Compliance Requirements

- **Software Upgrade**: Members must download and install NEAT+ version 7.8.9 from the NSE Extranet path `/cmftp/common/NEATPlus789`.
- **Data Master Updates**: Download and load master files (`security.gz`, `participant.gz`, `nnf_security.gz`, `nnf_participant.gz`, `NSE_CM_security_31072026.csv.gz`, and `cm_contract_stream_info.csv`) from their designated Extranet directories prior to the mock session.
- **Manual Order Clearance**: Members utilizing NNF software must manually clear all outstanding orders from their local databases and applications before the start of sessions.

## Important Dates

- **Mock Trading Session**: Sunday, August 02, 2026
- **Live Re-login Period**: Sunday, August 02, 2026 (14:00 - 14:30 Hrs)
- **NEAT+ Version 7.8.8 Discontinuation**: September 05, 2026

## Impact Assessment

- **Operational Impact**: Medium. Trading members must carry out mandatory software updates, execute connectivity checks, and load master databases on a non-trading day (Sunday). Successful mock participation ensures that subsequent live trading sessions involving the Closing Auction Session will operate without technical bottlenecks.
- **Financial Impact**: Low. There are no financial obligations associated with the mock trading session, as per standard regulatory guidelines.