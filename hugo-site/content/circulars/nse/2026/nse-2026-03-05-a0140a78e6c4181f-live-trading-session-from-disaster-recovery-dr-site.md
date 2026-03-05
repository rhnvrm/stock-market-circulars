---
category: market-operations
circular_id: a0140a78e6c4181f
date: '2026-03-05'
description: NSE will conduct live trading/bidding sessions from its Disaster Recovery
  (DR) site on March 5-6, 2026, reverting to primary site on March 9, 2026. Members
  must use specified IP addresses for extranet connectivity.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD73126.pdf
impact: high
impact_ranking: high
importance_ranking: high
justification: This circular affects all NSE members conducting live trading across
  multiple segments (Equity, Equity Derivatives, Currency Derivatives, Commodity Derivatives,
  SLB) and requires immediate operational action for DR site connectivity. Colocation
  participants will experience different latencies, making this operationally critical.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD73126.pdf
processing:
  attempts: 1
  content_hash: 5bc44c862f3217b6
  processed_at: '2026-03-05T04:49:19.996647'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-03-05T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD73126.pdf
severity: high
source: nse
stocks: []
tags:
- disaster-recovery
- dr-site
- bcp
- live-trading
- connectivity
- colocation
- mtbt
- equity
- equity-derivatives
- currency-derivatives
- commodity-derivatives
- slb
- neat-adapter
- extranet
title: Live Trading Session from Disaster Recovery (DR) Site - March 5-6 & March 9,
  2026
---

## Summary

NSE is conducting a live trading/bidding session from its Disaster Recovery (DR) site on March 5-6, 2026, across all major segments. Trading will revert to the primary site on March 9, 2026. Members need to use specific IP addresses for extranet connectivity during the DR session, while no changes are required to NEAT Adapter settings.

## Key Points

- Live trading from DR site: March 5–6, 2026 (normal market timings)
- Return to Primary site: March 9, 2026
- No changes required to NEAT Adapter settings for Primary/DR connectivity
- BCP LIVE trading covers Equity, Equity Derivatives, Currency Derivatives, Commodity Derivatives, and SLB segments
- Web-based platforms (eIPO, eOFS, CBRICS, RFQ, EBP, NDM, Negotiated Trade Reporting, Tri-Party Repo) use existing URLs
- Lease-line members must connect via Extranet IP: 172.19.125.70 (https://172.19.125.70/extranet-api/ and C2N-172.19.125.70)
- Co-location facility and MTBT feed remain available on Production IPs
- Colocation orders routed from main site to BCP site; dissemination from BCP/DR site to colocation racks
- Latencies for Colo Participants will differ from a normal trading day

## Regulatory Changes

No new regulatory changes. This circular is operational in nature, referencing existing DR framework established under NSE/MSD/44692 dated June 18, 2020 (Unannounced live trading sessions from DR site).

## Compliance Requirements

- Lease-line members must connect to Extranet IP 172.19.125.70 during the DR session
- Members subscribing to MTBT feeds should subscribe to both multicast channels (Source 1 and Source 2) for each stream in active-active manner to minimize data loss
- Members should use TBT Recovery mechanisms if packet loss is observed in MTBT broadcasts
- Refer to circulars NSE/MSD/67674 (April 24, 2025), NSE/CD/70422 (September 25, 2025), and NSE/COM/71599 (December 02, 2025) for Interactive Connectivity Parameters
- Refer to circular nos. 69328 (July 28, 2025) and 67677 (April 25, 2025) for MTBT Source 1 and Source 2 multicast IP and port details

## Important Dates

- **March 5–6, 2026**: Live trading from Disaster Recovery (DR) site at normal market timings
- **March 9, 2026**: Live trading resumes from Primary site

## Impact Assessment

This is a high-impact operational event affecting all NSE members across major trading segments. Colocation participants should be prepared for latency differences compared to normal trading days, as orders from colocation are routed from the main site to the BCP site. MTBT feed subscribers may experience UDP packet drops and should have TBT Recovery mechanisms active. Members using lease lines must reconfigure connectivity to the DR extranet IP (172.19.125.70). Web-based platform users are unaffected as existing URLs remain valid. Members should contact NSE at 1800 266 0050 (Option 1) or msm@nse.co.in for queries.