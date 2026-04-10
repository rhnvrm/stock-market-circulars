---
category: market-operations
circular_id: 5831eba984ee0b90
date: '2026-04-10'
description: NSE announces a mock trading session in the Capital Market segment on
  April 11, 2026. No new version release; functional changes from the new encryption
  mechanism will be effective from April 13, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMTR73692.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session announcement with no new version release;
  primarily operational/technical guidance for exchange members.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMTR73692.pdf
processing:
  attempts: 1
  content_hash: 52ac41530fe95e10
  processed_at: '2026-04-10T10:12:50.341205'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-04-10T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMTR73692.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- capital-market
- neat-plus
- encryption
- trading-session
- technical-update
- disaster-recovery
title: Mock Trading on Saturday, April 11, 2026 - Capital Market Segment (No New Version
  Release)
---

## Summary

NSE has scheduled a mock trading session in the Capital Market segment on Saturday, April 11, 2026. There is no new version release for this mock. Functional changes related to the new encryption mechanism of interactive messages and immediate order acknowledgement (announced in circular NSE/CMTR/72769 dated February 12, 2026) will be effective from April 13, 2026, not during this mock.

## Key Points

- Mock trading session in the Capital Market segment on Saturday, April 11, 2026
- No new software version is being released for this mock session
- NEAT+ version 7.8.7 is applicable (download path: `/common/NEATPlus787` on NSE Extranet)
- New encryption mechanism changes go live on April 13, 2026
- Two trading sessions: Session-1 from Primary Site and Session-2 from DR Site
- Old NEAT Adapter (v1.0.20) uses GR Port 10817; new NEAT Adapter (v1.0.27) uses GR Port 10823
- Members should refer to NEAT Adapter circular NSE/MSD/73674 dated April 09, 2026 for adapter version details

## Regulatory Changes

No regulatory changes in this circular. This is an operational/technical notification for a mock session. The underlying regulatory change (new encryption mechanism for interactive messages and immediate order acknowledgement) was communicated in circular NSE/CMTR/72769 dated February 12, 2026 and will be effective April 13, 2026.

## Compliance Requirements

- Members must participate in the mock trading session using NEAT+ version 7.8.7
- Members should use the correct NEAT Adapter version and corresponding GR port:
  - Old NEAT Adapter v1.0.20 (Windows/Linux): Port 10817
  - New NEAT Adapter v1.0.27 (Windows/Linux): Port 10823
- Members should follow instructions in Annexures 1, 2, and 3 for mock session participation, general guidelines, and DR switchover procedures
- Connectivity parameters per circular NSE/MSD/67674 dated April 24, 2025

## Important Dates

- **April 11, 2026 (Saturday)**: Mock trading session in Capital Market segment
- **April 13, 2026**: New encryption mechanism functional changes go live on the trading platform
- **Session-1 (Primary Site) Key Timings**:
  - Pre-Open: 10:00 – 10:08
  - Normal Market Open: 10:15
  - T+0 Market Open: 10:15; Close: 12:30
  - Normal Market Close: 14:00
- **Session-2 (DR Site) Key Timings**:
  - Pre-Open: 14:00 – 14:53
  - Normal Market Open: 15:00
  - Normal Market Close: 16:00
  - Trade Modification End: 16:30
  - Live Re-login: 17:00 – 18:00

## Impact Assessment

This circular has low market impact as it concerns a routine mock/test trading session with no new version deployment. The session is intended for members to test connectivity and readiness ahead of the April 13, 2026 go-live of the new encryption mechanism. No real trades or market positions are affected. Members using the new NEAT Adapter (v1.0.27) must ensure they connect on the correct port (10823) to avoid connectivity issues during the mock.