---
category: market-operations
circular_id: 35194f4eb8b4fce7
date: '2026-02-27'
description: NSE will conduct a mock trading session in the Currency Derivatives Segment
  from the DR site on February 28, 2026, with trading hours from 09:00 to 17:00 and
  re-login into live environment by 19:00.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CD73047.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for Currency Derivatives segment from
  DR site; no financial obligations, affects only member connectivity testing and
  does not impact regular market operations or listed securities.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CD73047.pdf
processing:
  attempts: 1
  content_hash: a28d12e20017003c
  processed_at: '2026-02-27T15:59:35.203776'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-02-27T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CD73047.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- bcp-dr
- currency-derivatives
- neat
- disaster-recovery
- trading-session
title: Mock Trading from BCP/DR Site on Saturday, February 28, 2026 - Currency Derivatives
---

## Summary

NSE will conduct a mock trading session in the Currency Derivatives Segment from the Business Continuity Plan (BCP)/Disaster Recovery (DR) site on Saturday, February 28, 2026. The session is intended to allow members to test trading software and re-login into the live environment to ensure smooth connectivity for the regular trading day on Monday, March 2, 2026. No financial obligations arise from trades executed during mock sessions.

## Key Points

- Mock trading will be conducted from the DR site in the Currency Derivatives Segment on February 28, 2026
- Normal Market open time: 09:00 hrs; Normal Market close time: 17:00 hrs
- Trade Modification end time: 17:30 hrs
- Re-login window: 18:30 hrs (start) to 19:00 hrs (close)
- NEAT version 3.5.4 to be used; download path on NSE Extranet: `/cdsftp/cdscommon/NEATCDS354`
- Old NEAT Adapter (v1.0.20) uses GR PORT 10877; Old NEAT Adapter (v1.0.22) and New NEAT Adapter (v1.0.23) use GR PORT 10879
- All outstanding orders will be cleared before each session
- Connect2NSE and Extranet will be unavailable from 04:45 am to 08:15 am and 06:00 pm to 09:00 pm

## Regulatory Changes

No regulatory changes. This circular references existing SEBI circular SEBI/HO/MRD1/DSAP/CIR/P/2020/234 and NSE circular NSE/MSD/46441 for software testing compliance requirements. Members may use either Mock Trading or the Simulated Environment to meet regulatory requirements.

## Compliance Requirements

- Members must use NEAT version 3.5.4 for this mock session
- Members using NNF software must manually clear orders in their systems before the session
- Only valid and compliant UCC/PAN uploaded and approved before cutoff will be allowed during mock trading (UCC validation skipped during contingency time)
- Members should refer to NEAT Adapter circulars NSE/MSD/70421 (September 25, 2025) and NSE/MSD/71601 (December 02, 2025) for the correct NEAT Adapter version and port combinations
- Members must participate using all trading software and re-login into the live environment after the mock session
- For connectivity details, refer to circulars NSE/MSD/67674 (April 24, 2025) and NSE/CD/70422 (September 25, 2025)

## Important Dates

- **February 28, 2026**: Mock trading session from DR site
- **09:00 hrs**: Normal Market open
- **17:00 hrs**: Normal Market close
- **17:30 hrs**: Trade Modification end
- **18:30 hrs**: Live Re-login start
- **19:00 hrs**: Live Re-login close
- **March 2, 2026**: Regular live trading resumes (Monday)

## Impact Assessment

This is a routine operational exercise with no financial impact on members or the market. Trades executed during the mock session will not result in any fund pay-in or pay-out. The session is confined to the Currency Derivatives Segment and is intended solely to test member readiness for DR-site connectivity. Members should ensure they complete the re-login into the live environment by 19:00 hrs on February 28 to be prepared for normal trading on Monday, March 2, 2026. The NOTIS application will be accessible during the mock session for reference.