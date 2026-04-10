---
category: market-operations
circular_id: b90d2c590029fd8d
date: '2026-04-10'
description: NSE announces mock trading session for Currency Derivatives Segment on
  Saturday, April 11, 2026, covering two sessions from Primary and DR sites. No new
  NEAT version release; existing NEAT 3.5.4 applies.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CD73690.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for Currency Derivatives Segment with
  no financial obligations and no new software version. Operational relevance limited
  to member IT and trading teams preparing for Monday April 13 live session.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CD73690.pdf
processing:
  attempts: 1
  content_hash: 77414d92f7accb69
  processed_at: '2026-04-10T13:27:24.933121'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-04-10T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CD73690.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- currency-derivatives
- neat
- disaster-recovery
- connectivity
- cd-segment
- neat-adapter
title: NSE Currency Derivatives Mock Trading Session - April 11, 2026 (NEAT 3.5.4)
---

## Summary

NSE will conduct a mock trading session in the Currency Derivatives (CD) Segment on Saturday, April 11, 2026. The session includes two sub-sessions — one from the Primary Site and one from the Disaster Recovery (DR) Site. No new NEAT version is being released; NEAT 3.5.4 remains in use. Trades executed during mock sessions carry no financial obligation.

## Key Points

- Mock trading date: **April 11, 2026 (Saturday)**
- Segment: Currency Derivatives
- No new NEAT version — NEAT **3.5.4** continues (download path: `/cdsftp/cdscommon/NEATCDS354`)
- Two trading sessions: Session-1 from Primary Site; Session-2 from DR Site
- Members must re-login to the live environment post-mock to ensure readiness for **Monday, April 13, 2026**
- NEAT Adapter combinations: Old (v1.0.20) uses port **10877**; New (v1.0.27) uses port **10879**
- No fund pay-in or pay-out resulting from mock trades
- NOTIS application will be accessible during the mock session

## Trading Session Schedule

| Particulars | Time (IST) |
|---|---|
| Session-1 (Primary Site) — Normal Market Open | 10:00 |
| Contingency Start Time | 12:00 |
| Contingency Close Time | 13:30 |
| Session-1 Normal Market Close | 14:00 |
| Session-2 (DR Site) — Normal Market Open | 14:45 |
| Session-2 Normal Market Close | 15:30 |
| Trade Modification End Time | 15:40 |
| Live Re-login Start Time | 17:00 |
| Live Re-login Close Time | 18:00 |

## Regulatory Changes

No regulatory changes. This circular is a continuation of circular (download no. 71999) dated December 24, 2025, covering the ongoing mock trading schedule for the Currency Derivatives Segment.

## Compliance Requirements

- Members must use **NEAT 3.5.4** for the mock session
- NEAT Adapter version and port combinations must align with the circular NSE/MSD/73674 dated April 09, 2026
- Only valid and compliant UCC/PAN uploaded and approved before cutoff will be permitted to trade; UCC validation is skipped during contingency periods
- Members using NNF software must **manually clear outstanding orders** between sessions
- Members should participate using all trading software and re-login to the live environment to confirm connectivity ahead of Monday's live market
- Connectivity setup per NSE/MSD/67674 (April 24, 2025) and NSE/CD/70422 (September 25, 2025)

## Important Dates

- **April 11, 2026**: Mock trading session (Currency Derivatives Segment)
- **April 13, 2026**: Live trading resumes; members must ensure re-login readiness
- Connect2NSE and Extranet unavailable: 12:30–17:30 and 18:00–21:30 on mock day
- Extranet API unavailable: 12:30–14:00 and 17:30–18:30 on mock day

## Impact Assessment

Impact is low and confined to operational and IT teams of CD Segment members. There are no financial consequences, no new software deployments, and no market structure changes. Members should verify NEAT Adapter version/port compatibility and confirm live re-login succeeds before 18:00 on April 11 to avoid any connectivity issues on the following Monday.