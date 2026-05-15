---
category: market-operations
circular_id: 53818db236f9c68e
date: '2026-05-15'
description: NSE will conduct a mock trading session in the EGR Segment on May 16,
  2026, with a new version of NEAT+ 1.0.0 available for download from May 15, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/EGR74260.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for EGR segment members to test new NEAT+
  1.0.0 software; no financial obligations arise and affects only EGR segment members
  during a Saturday mock session.
pdf_url: https://nsearchives.nseindia.com/content/circulars/EGR74260.pdf
processing:
  attempts: 1
  content_hash: 59bf1c17dbdf7b44
  processed_at: '2026-05-15T19:36:34.179466'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-15T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/EGR74260.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- electronic-gold-receipts
- egr
- neat-plus
- technology-upgrade
- disaster-recovery
- trading-system
title: Mock Trading in Electronic Gold Receipts (EGR) Segment on May 16, 2026 - NEAT+
  Version 1.0.0
---

## Summary

NSE is conducting a mock trading session in the Electronic Gold Receipts (EGR) Segment on Saturday, May 16, 2026, to facilitate testing of the new NEAT+ version 1.0.0. This is a two-session mock (Primary Site and DR Site) with no financial obligations for trades executed during the session.

## Key Points

- Mock trading scheduled for May 16, 2026 across two sessions: Trading Session-1 from Primary Site (12:15–15:15) and Trading Session-2 from DR Site (16:30–17:10)
- New NEAT+ version 1.0.0 available for download from May 15, 2026 at 20:00 hrs via NSE Extranet path `/egftp/egcommon/NEATPlus100`
- NEAT Adapter version 1.0.25 (Windows and Linux) must be used with GR PORT 11887
- Default login password for mock session: `Neat@EG1`
- Trades during mock sessions carry no financial obligation (no fund pay-in or pay-out)
- Connect2NSE and Extranet facility unavailable from 2:00 PM till end of mock session; Extranet API unavailable from 2:00 PM to 3:00 PM

## Regulatory Changes

No regulatory changes. This circular is an operational notice for a scheduled mock trading session.

## Compliance Requirements

- Members must download and install NEAT+ version 1.0.0 from the NSE Extranet before the mock session
- Members must use NEAT Adapter version 1.0.25 (Windows or Linux) with GR PORT 11887 for EGR segment login
- Members should refer to NEAT Adapter circular NSE/MSD/74225 dated May 14, 2026 for NEAT Adapter Exe application details
- Members must follow Annexures 1–5 for mock trading instructions, login parameters, market data broadcast parameters, installation procedures, and DR switchover guidelines

## Important Dates

- **May 15, 2026, 20:00 hrs**: NEAT+ version 1.0.0 available for download
- **May 16, 2026**: Mock trading session
  - Session-1 (Primary Site): Pre-open 12:15, Normal Market open 12:30, Market close 15:15
  - Session-2 (DR Site): Pre-open 16:30, Normal Market open 16:45, Market close 17:00, Trade modification end 17:10
  - Live re-login window: 19:15–19:45

## Impact Assessment

Impact is limited to EGR segment members who need to test the new NEAT+ 1.0.0 software. No financial or market impact as trades during mock sessions carry no obligations. Members should plan for Extranet/Connect2NSE unavailability from 2:00 PM on May 16, 2026. Gateway details: Primary/DR site IP 172.19.14.85, Port 11887; EGR multicast broadcast on 239.50.50.63:10863 (Source 1) and 239.50.50.68:10868 (Source 2).