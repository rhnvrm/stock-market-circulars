---
category: market-operations
circular_id: a01238c40da46213
date: '2026-06-12'
description: NSE will conduct a mock trading session on June 13, 2026 from Primary
  and BCP/DR sites, followed by a re-login session from Primary site to ensure smooth
  operations on Monday, June 15, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMTR74691.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock/disaster-recovery test session with no financial impact;
  affects only technical connectivity for member firms on a non-trading Saturday.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMTR74691.pdf
processing:
  attempts: 1
  content_hash: 474f07f748abba9b
  processed_at: '2026-06-12T15:10:51.523245'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-12T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMTR74691.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- bcp
- dr-site
- capital-market
- nse
- neat-adapter
- settlement-calendar
title: NSE Mock Trading Session from BCP/DR Site on Saturday, June 13, 2026
---

## Summary

NSE will conduct a mock trading session on Saturday, June 13, 2026, covering two trading sessions — Session 1 from the Primary Site and Session 2 from the BCP/DR Site. A live re-login session from the Primary site will follow (18:30–19:00) to prevent login issues on the next trading day, Monday, June 15, 2026.

## Key Points

- Mock trading is split into two sessions: Session 1 (Primary Site) and Session 2 (DR Site).
- Exchange will perform a **non-graceful shutdown** from the Primary site before shifting to DR/BCP site during Session 2.
- All outstanding orders will be purged before trading commences from the BCP site.
- Multicast TBT sequence numbers will reset to '1' when trading starts from BCP site.
- No changes to NEAT Adapter settings are required; live settings as of Friday, June 12, 2026 should be retained.
- Latencies for Colo Participants will differ on the DR/BCP day compared to normal trading days.
- Re-login from Primary site: 18:30–19:00 hrs.

## Regulatory Changes

No regulatory changes. This is a scheduled operational/business continuity mock exercise.

## Compliance Requirements

- Members must retain NEAT Adapter settings from the live session of June 12, 2026 for all sessions.
- Members using NNF software must clear outstanding orders from Session 1 before participating in BCP/DR session.
- Members should take necessary action per circular NSE/MSD/48662 dated June 18, 2021 in the event of a non-graceful shutdown.
- Members should refer to Annexure 1 (operational instructions), Annexure 2 (pre-requisites/general guidelines), and Annexure 3 (switchover guidelines) as provided in the circular.

## Important Dates

| Event | Date / Time |
|---|---|
| Mock Trading Date | Saturday, June 13, 2026 |
| Session 1 (Primary Site) — Trading Session Start | 08:45 hrs |
| Session 1 — Normal Market Open | 09:15 hrs |
| Session 1 — Normal Market Close | 11:45 hrs |
| Session 2 (DR Site) — Pre-Open | 11:53 hrs |
| Session 2 — Normal Market Open | 12:00 hrs |
| Session 2 — Normal Market Close | 15:30 hrs |
| Session 2 — Trade Modification End | 16:15 hrs |
| Live Re-login (Primary Site) | 18:30–19:00 hrs |
| Next Live Trading Day | Monday, June 15, 2026 |

## Impact Assessment

This is a routine business continuity planning (BCP) and disaster recovery (DR) mock exercise with no financial market impact. Member firms are required to participate to verify their systems can connect and operate seamlessly from both Primary and DR/BCP sites. The session is non-financial and confined to Saturday; normal live trading resumes Monday, June 15, 2026. Members with co-location infrastructure should anticipate higher latencies during the DR session.