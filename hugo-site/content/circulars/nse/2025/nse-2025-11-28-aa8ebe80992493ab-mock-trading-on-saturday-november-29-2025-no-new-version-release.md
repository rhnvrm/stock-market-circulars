---
category: market-operations
circular_id: aa8ebe80992493ab
date: '2025-11-28'
description: NSE will conduct mock trading session in F&O segment on November 29,
  2025 to test Pre-Open Session implementation with two trading sessions scheduled.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP71527.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Mock trading session for testing Pre-Open Session in F&O segment; requires
  active member participation and system preparation but no live market impact
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP71527.pdf
processing:
  attempts: 1
  content_hash: f05ff2eda65d7323
  processed_at: '2025-11-28T13:01:30.792641'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-11-28T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP71527.pdf
severity: medium
source: nse
stocks: []
tags:
- mock-trading
- pre-open-session
- futures-and-options
- equity-derivatives
- neat-plus
- algorithmic-trading
- testing
- system-upgrade
title: Mock Trading Session on Saturday, November 29, 2025 - No New Version Release
---

## Summary

NSE will conduct a mock trading session in the Futures & Options segment on Saturday, November 29, 2025, to test the implementation of Pre-Open Session in Equity Derivatives. The mock session will consist of two trading sessions, with Trading Session-1 including the new pre-open functionality and Trading Session-2 running without pre-open as per current live scenario. Members are required to use NEAT+ version 7.8.6 for pre-open session testing.

## Key Points

- Mock trading scheduled for Saturday, November 29, 2025 in F&O segment
- Two separate trading sessions: Session-1 (10:00-13:10) with pre-open, Session-2 (16:45-17:25) without pre-open
- Pre-open session timing: Open at 10:00, Close at 11:23 with random closure in last one minute
- Normal market open time for Session-1: 11:30
- NEAT+ version 7.8.6 required for placing orders in pre-open session
- Pre-open applicable only for December & January month futures contracts (FUTIDX & FUTSTK)
- NEAT+ version 7.8.4 to be discontinued on December 06, 2025
- Orders and trades from Trading Session-1 will not be available in Trading Session-2
- Live re-login window: 19:00 to 19:30 on November 29, 2025
- Master files for Trading Session-1 available on NSE Extranet by 8:30 hours on November 29, 2025
- Testing of algorithmic trading safeguards for retail investors required

## Regulatory Changes

This circular implements testing for the Pre-Open Session in Equity Derivatives (F&O) Segment as referenced in NSE/FAOP/71092 dated November 03, 2025. Members must also test functionality related to safer participation of retail investors in algorithmic trading as per SEBI circular SEBI/HO/MIRSD/MIRSD-PoD/P/CIR/2025/132 dated September 30, 2025.

## Compliance Requirements

- Trading members must upgrade to NEAT+ version 7.8.6 for pre-open session participation
- Download and load master files (contract.gz, NSE_FO_contract_29112025.csv) from NSE Extranet path /faoftp/faocommon/Mock/29Nov2025 before mock trading
- Actively participate in both trading sessions during mock trading
- Test algorithmic trading functionality for retail investor safeguards
- Download master files generated post EOD activities on November 28, 2025 for mock session-2 and live trading on December 01, 2025
- Discontinue use of NEAT+ version 7.8.4 by December 06, 2025

## Important Dates

- **November 28, 2025**: Circular date; EOD master files generation
- **November 29, 2025**: Mock trading session day
  - Trading Session-1: 10:00 to 13:10 (with pre-open)
  - Trading Session-2: 16:45 to 17:25 (without pre-open)
  - Live re-login: 19:00 to 19:30
  - Master files available by 8:30 hours
- **December 01, 2025**: Live trading resumes
- **December 06, 2025**: NEAT+ version 7.8.4 discontinuation date (mock)

## Impact Assessment

**Operational Impact**: Members must prepare systems and infrastructure to test the new pre-open session functionality. This requires downloading specific NEAT+ version 7.8.6 and updated master files. The mock session provides critical testing opportunity before live implementation.

**Market Participants**: All F&O trading members are encouraged to actively participate in both mock sessions to ensure smooth transition when pre-open goes live. Separate testing is needed for algorithmic trading safeguards.

**Technical Requirements**: Members need to ensure proper version management with version 7.8.6 for pre-open functionality while version 7.8.4 faces discontinuation. Master file management is critical as different files apply to different sessions.

**Risk Mitigation**: The two-session approach (one with pre-open, one without) allows comprehensive testing while maintaining familiarity with current live scenario. This reduces implementation risk for the actual pre-open session rollout.