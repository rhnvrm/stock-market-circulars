---
category: market-operations
circular_id: 4947bcaa440a7657
date: '2026-07-02'
description: NSE will conduct a mock trading session in the Currency Derivatives segment
  on July 04, 2026, with no new software version release, alongside migration to TCP/IP
  order book snapshot recovery and new CA certificate/interactive port requirements.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CD75009.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine operational/technical circular affecting trading members' system
  readiness for a mock session; no direct impact on listed securities or investors.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CD75009.pdf
processing:
  attempts: 1
  content_hash: 9cab07d95620085d
  processed_at: '2026-07-02T14:18:57.278271'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-07-02T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CD75009.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- currency-derivatives
- live-activities-schedule
- market-operations
title: NSE Mock Trading in Currency Derivatives Segment on Saturday, July 04, 2026
---

## Summary

NSE will conduct a mock trading session in the Currency Derivatives segment on Saturday, July 04, 2026, continuing from an earlier circular dated December 24, 2025. This mock session will not involve a new software version release. The circular also mandates discontinuation of Order book snapshot recovery via Solace API from July 04, 2026, requiring migration to TCP/IP-based recovery, and specifies new CA certificate and interactive port requirements for the segment.

## Key Points

- Mock trading session scheduled for July 04, 2026 in the Currency Derivatives (CD) segment.
- No new version release accompanies this mock session.
- Trading Session-1 (Primary Site): Contingency Start 12:45, Contingency Close 14:00, Normal Market close 15:30/16:00 timings as specified.
- Trading Session-2 (DR Site): Normal Market open 16:00, close 16:30, Trade Modification end 17:30.
- Relogin timings: Live Re-login start 17:40, close 18:30, with further window to 19:00.
- Order book snapshot recovery via Solace API discontinued from July 04, 2026; members must mandatorily migrate to TCP/IP-based recovery per circular NSE/MSD/74567 dated June 05, 2026.
- Members must use new NEAT Adapter version 1.0.29 (Windows/Linux) with new Gateway Router port 10889 mandatorily from July 04, 2026 (mock).
- New CA certificate available on Extranet at /cdsftp/cdscommon/Encryption_CA_Certificate/2026_Certificate; migration readiness required by July 04, 2026.
- New interactive parameters for CD segment: Gateway Router IP 172.19.18.85, ports 10870/10871 (existing), 10885 (new interactive), 10889 (new, MD5 checksum removed), 10891 (new, MD5 checksum removed plus immediate Ack for order messages).
- All outstanding orders will be purged before each session; NNF software users must manually clear orders.
- NEAT Version for mock: 3.5.4.
- Members may use Mock Trading or Simulated Environment to meet SEBI regulatory testing requirements per SEBI circular SEBI/HO/MRD1/DSAP/CIR/P/2020/234.

## Regulatory Changes

No new regulatory policy change; this is an operational/technical circular implementing prior directives on connectivity migration (TCP/IP recovery, new CA certificate, new NEAT Adapter version and ports) referenced from earlier circulars (NSE/MSD/74567, NSE/MSD/74511, NSE/MSD/74559, NSE/MSD/73993, NSE/MSD/46441).

## Compliance Requirements

- Members must ensure migration to TCP/IP-based order book snapshot recovery is complete, as Solace API recovery is discontinued from July 04, 2026.
- Members must download and install the new CA certificate from the Extranet and update to NEAT Adapter version 1.0.29.
- Members using Direct/NNF connections must reconfigure to use new interactive ports and IP parameters for the CD segment.
- Members must clear/purge outstanding orders manually if using NNF software before each mock session.
- Members should refer to Annexures 1-3 for detailed mock trading guidelines, pre-requisites, and DR site switchover procedures.

## Important Dates

- July 02, 2026: Circular issue date.
- July 04, 2026 (Saturday): Mock trading session in Currency Derivatives segment; mandatory migration deadline for new NEAT Adapter version, ports, CA certificate, and discontinuation of Solace API-based order book snapshot recovery.

## Impact Assessment

This circular has low market impact as it pertains to a technical/operational mock trading exercise for trading members' system readiness rather than affecting listed securities, trading strategies, or investors directly. However, non-compliance by members with the new connectivity, certificate, and port requirements could disrupt their live trading connectivity post-migration, making IT/operations readiness important for affected trading members and vendors.