---
category: market-operations
circular_id: 53cbc76b04e7d355
date: '2026-03-23'
description: NSE will discontinue order book snapshot recovery through Solace API
  in CM, FO, and CD segments effective June 06, 2026. Members must migrate to the
  new TCP/IP-based Order Snapshot Recovery facility before the deadline.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD73425.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Affects all NSE members using order book snapshot recovery via Solace
  API across three segments; mandates technical migration by June 06, 2026 with no
  extension granted, requiring infrastructure planning and system changes.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD73425.pdf
processing:
  attempts: 1
  content_hash: 9c91156db8d31873
  processed_at: '2026-03-23T13:09:45.705146'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-03-23T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD73425.pdf
severity: medium
source: nse
stocks: []
tags:
- market-data
- solace-api
- tcp-ip
- order-snapshot
- mtbt
- capital-market
- futures-options
- currency-derivatives
- migration
- member-services
- discontinuation
title: Market Data - Discontinuation of Order Snapshot Recovery via Solace API for
  MTBT Broadcast in CM, FO and CD Segments
---

## Summary

NSE is discontinuing the existing order book snapshot recovery functionality via Solace API for MTBT broadcast across Capital Market (CM), Futures & Options (FO), and Currency Derivatives (CD) segments, effective June 06, 2026. This follows the earlier introduction of Order Book Snapshot Recovery via TCP/IP announced in circulars NSE/MSD/70707 (October 08, 2025) and NSE/MSD/73149 (March 05, 2026). Members are required to complete migration to the new TCP/IP-based facility before the deadline, with no extension permitted.

## Key Points

- Solace API-based order snapshot recovery will be discontinued across CM, FO, and CD segments from June 06, 2026
- Replacement facility uses TCP/IP connectivity; all three segments share the IP address 172.28.124.54
- Port assignments: CM segment – 11984, FO segment – 11989, CD segment – 11985
- No extension of the discontinuation deadline will be granted
- All other details from prior circulars (NSE/MSD/70707 and NSE/MSD/73149) remain unchanged
- Members must independently plan and execute migration activities

## Regulatory Changes

This circular formalizes the retirement of the Solace API order snapshot recovery mechanism and mandates transition to TCP/IP-based recovery as the sole supported method for order book snapshot recovery in CM, FO, and CD segments post June 06, 2026.

## Compliance Requirements

- All NSE members currently using Solace API for order book snapshot recovery must migrate to the TCP/IP facility before June 06, 2026
- Members must connect to the new TCP/IP endpoint using the specified IP (172.28.124.54) and segment-specific ports
- Members are solely responsible for implementing and maintaining redundancy for market data broadcast
- Members should monitor and adequately size their infrastructure to handle feed requirements
- Members must review related circulars NSE/MSD/64333, NSE/COMP/56426, and NSE/MEM/26958 for data usage guidelines

## Important Dates

- **March 23, 2026**: Circular issued
- **June 06, 2026**: Discontinuation of Solace API order snapshot recovery in CM, FO, and CD segments (hard deadline, no extension)

## Impact Assessment

All NSE members subscribed to order book snapshot recovery via Solace API in the CM, FO, or CD segments are impacted and must undertake technical migration to TCP/IP connectivity. The change is operationally significant for high-frequency and algorithmic trading participants who rely on snapshot recovery for data continuity. The fixed deadline with no extension creates urgency for infrastructure teams to plan and test migration well in advance. The new TCP/IP parameters are straightforward, using a single IP for all three segments with distinct port numbers per segment, simplifying connection management.