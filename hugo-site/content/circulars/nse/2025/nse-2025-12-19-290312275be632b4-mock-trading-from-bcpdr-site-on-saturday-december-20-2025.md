---
category: market-operations
circular_id: 290312275be632b4
date: '2025-12-19'
description: NSE will conduct mock trading session from Primary and BCP/DR sites on
  December 20, 2025, followed by re-login session to avoid login issues on December
  22, 2025.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMTR71914.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Routine mock trading session for BCP/DR testing, requires member participation
  but no market or regulatory impact
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMTR71914.pdf
processing:
  attempts: 1
  content_hash: b24c4dda7cd9d0da
  processed_at: '2025-12-19T16:16:02.378954'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-19T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMTR71914.pdf
severity: medium
source: nse
stocks: []
tags:
- mock-trading
- bcp
- disaster-recovery
- trading-session
- capital-market
- technical
- system-testing
title: Mock Trading from BCP/DR Site on Saturday, December 20, 2025
---

## Summary

NSE will conduct a mock trading session on Saturday, December 20, 2025 from both Primary and BCP/DR sites. The mock session will include non-graceful shutdown from primary site to DR site, followed by a live re-login session from the Primary site to prevent login problems on Monday, December 22, 2025. All members are required to participate and follow specific operational instructions.

## Key Points

- Mock trading scheduled for December 20, 2025 with two sessions: Trading Session-1 from Primary Site and Trading Session-2 from DR Site
- Non-graceful shutdown will occur when exchange shifts from primary to DR site during mock session
- All outstanding orders will be purged before BCP site trading starts
- Multicast TBT sequence numbers will restart from '1' when trading begins from BCP site
- Live re-login session scheduled from 18:30 to 19:00 to avoid Monday login issues
- No changes required in NEAT Adapter settings - members should retain Friday December 19, 2025 settings
- Latencies for Colo Participants will differ on DR/BCP day compared to normal trading

## Trading Session Schedule

**Session-1 from Primary Site:**
- Morning Block Deal Window: 08:45 - 09:00
- Pre-Open: 09:00 - 09:08 (random closure in last minute)
- Special Pre-open for IPO/Relisted: 09:00 - 09:45 (random closure in last 10 minutes)
- Normal Market Open: 09:15
- T+0 Market Open: 09:15
- Call Auction Illiquid: 09:30 (2 sessions of 1 hour each)
- Normal Market Open for special pre-open stocks: 10:00
- Normal Market Close: 12:00

**Session-2 from DR Site:**
- Pre-Open: 12:45 - 12:53 (random closure in last minute)
- Normal Market Open: 13:00
- T+0 Market Close: 13:30
- Call Auction Illiquid: 13:00 (2 sessions of 1 hour each)
- T+0 Trade Modification End: 13:45
- Auction Market: 14:30 - 15:15
- Normal Market Close: 15:30
- Closing Session: 15:40 - 16:00
- Trade Modification End: 16:15

**Re-login Session:**
- Live Re-login: 18:30 - 19:00

## Compliance Requirements

- Members must retain NEAT Adapter settings from Friday, December 19, 2025 to connect to all sessions
- Members using NNF software must clear outstanding orders from session 1 before trading from BCP site
- Members must take necessary action per circular NSE/MSD/48662 dated June 18, 2021 to bring systems into consistent state during non-graceful shutdown
- Members must refer to operational instructions in Annexures 1-4 provided with the circular

## Important Dates

- **December 19, 2025**: Retain NEAT Adapter settings from this date
- **December 20, 2025**: Mock trading session from Primary and DR sites
- **December 20, 2025 (18:30-19:00)**: Live re-login session
- **December 22, 2025**: Normal trading resumes on Monday

## Impact Assessment

This is a routine BCP/DR testing exercise with medium operational impact. Members must participate to ensure system readiness and prevent potential login issues. The non-graceful shutdown simulation tests disaster recovery capabilities. No financial obligations or actual trading occurs during the mock session. Technical teams need to be available for the mock and re-login sessions. Colo participants should note different latency patterns during DR operations.