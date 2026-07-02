---
category: market-operations
circular_id: 2a9d139860253a9b
date: '2026-07-02'
description: NSE will conduct a mock trading session in the Commodity Derivatives
  segment on Saturday, July 04, 2026, with no new software version release; members
  must mandatorily migrate to new NEAT Adapter version 1.0.29 and new CA certificate/ports
  by this date.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/COM75010.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine operational circular for members regarding a mock trading session
  and mandatory NEAT Adapter/CA certificate migration; no direct impact on listed
  securities or market pricing.
pdf_url: https://nsearchives.nseindia.com/content/circulars/COM75010.pdf
processing:
  attempts: 1
  content_hash: cee51683257a15a6
  processed_at: '2026-07-02T14:18:35.297051'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-07-02T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/COM75010.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- commodity-derivatives
- nse
- settlement-calendar
title: NSE Mock Trading Session in Commodity Derivatives Segment on Saturday, July
  04, 2026
---

## Summary

NSE will conduct a mock trading session in the Commodity Derivatives (COM) segment on Saturday, July 04, 2026. Unlike prior mock sessions, this one will not involve a new software version release. The circular reiterates the mandatory migration to the new NEAT Adapter version 1.0.29 (Windows and Linux) along with new CA certificates and gateway ports, which members must have ready by July 04, 2026.

## Key Points

- Mock trading session scheduled for Saturday, July 04, 2026, in the Commodity Derivatives segment.
- No new version release will accompany this mock session.
- Trading Session-1 (Primary Site): Normal market open at 12:45 hrs, contingency window from 14:00 to 15:30 hrs, normal market close at 16:00 hrs.
- Trading Session-2 (DR Site): Normal market open at 16:30 hrs, close at 17:30 hrs.
- Position Limit/Collateral value set-up cut-off and trade modification end time: 17:40 hrs.
- Live re-login window: 18:30 hrs to 19:00 hrs.
- Members must use New NEAT Adapter version 1.0.29 (Windows and Linux) with applicable new GR port (10869) from July 04, 2026 (mock) onward, mandatorily.
- Members using direct connection through NNF users must download and use the new CA certificate available on the Extranet path.
- New interactive parameters for the Commodity Derivatives (COM) segment: Gateway Router IP 172.19.15.85 with new ports 10865, 10869 (MD5 checksum removal), and 10871 (MD5 checksum removal plus new immediate Ack request); Gateway IP subnet 172.19.15.0/255.255.255.128, port 10850.
- Detailed instructions provided in three annexures covering mock trading procedures, environment prerequisites, and DR site switchover guidelines.

## Regulatory Changes

No new regulatory change is introduced; this circular operationalizes previously announced requirements from circular NSE/MSD/74511 (June 02, 2026) on the new CA certificate and NSE/MSD/74559 (June 05, 2026) on the new NEAT Adapter EXE version, in continuation of circular Download No. 71999 dated December 24, 2025.

## Compliance Requirements

- All Commodity Derivatives segment members must ensure readiness of their migration plan to the new NEAT Adapter version 1.0.29 and new CA certificate by July 04, 2026.
- Members using direct NNF connections must download the new CA certificate from the Extranet path (/comtftp/comtcommon/Encryption_CA_Certificate/2026_Certificate).
- Members must reconfigure interactive parameters to use the new gateway IP/port combinations for the COM segment.
- Members should refer to Annexures 1–3 for detailed mock trading, environment setup, and DR switchover guidelines.

## Important Dates

- Mock trading session: Saturday, July 04, 2026.
- New NEAT Adapter version and CA certificate migration: mandatory from July 04, 2026 (mock).
- Referenced prior circulars: December 24, 2025 (Download No. 71999), June 02, 2026 (NSE/MSD/74511), June 05, 2026 (NSE/MSD/74559).

## Impact Assessment

This is a routine operational/technical circular affecting only NSE Commodity Derivatives segment members' trading infrastructure and connectivity setup. It has no direct impact on listed securities, stock prices, or investor trading activity, but non-compliant members risk connectivity disruption once the new adapter/certificate/port requirements become mandatory.