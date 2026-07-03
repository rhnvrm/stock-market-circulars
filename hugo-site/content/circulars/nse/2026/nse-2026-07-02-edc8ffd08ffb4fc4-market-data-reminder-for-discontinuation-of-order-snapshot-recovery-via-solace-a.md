---
category: market-operations
circular_id: edc8ffd08ffb4fc4
date: '2026-07-02'
description: NSE has reminded members that Order Snapshot Recovery through the Solace
  API for MTBT broadcast in FO and CD segments will be discontinued from July 04,
  2026, and members must migrate to the TCP/IP method using the specified IP and port
  details.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD75020.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: This is an operational/technical reminder affecting trading members'
  market data infrastructure in FO and CD segments, not a corporate action or listing
  event impacting specific stocks. It requires infrastructure migration by members
  but has no direct market or investor impact.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD75020.pdf
processing:
  attempts: 1
  content_hash: 7f407cd3ab3e65ce
  processed_at: '2026-07-03T03:06:30.569228'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-07-02T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD75020.pdf
severity: medium
source: nse
stocks: []
tags:
- market-data
- solace-api
- order-snapshot-recovery
- mtbt-broadcast
- tcp-ip
title: 'NSE Reminder: Discontinuation of Order Snapshot Recovery via Solace API for
  MTBT Broadcast in FO and CD Segments Effective July 04, 2026'
---

## Summary

NSE has issued a reminder circular referencing its earlier circular NSE/MSD/74567 dated June 05, 2026, informing members that the Order Snapshot Recovery through Solace API for MTBT broadcast in the Futures & Options (FO) and Currency Derivatives (CD) segments will be discontinued effective July 04, 2026. Members still relying on the Solace API for order book snapshot recovery are advised to migrate to the TCP/IP method on priority, using the connection parameters provided in the annexure.

## Key Points

- This circular is a reminder of a previously announced discontinuation (NSE/MSD/74567 dated June 05, 2026).
- Order Snapshot Recovery via Solace API will be discontinued for MTBT broadcast in FO and CD segments.
- Members must migrate to the TCP/IP method for order snapshot recovery on priority.
- Connection parameters for TCP/IP recovery are provided:
  - FO segment: IP 172.28.124.54, Port 11989
  - CD segment: IP 172.28.124.54, Port 11985
- All other details from the original circular (NSE/MSD/74567) remain unchanged.
- Members are responsible for implementing and maintaining redundancy for market data broadcast; NSEIL is not liable for disconnection, bandwidth, or latency issues arising from members' configuration decisions.

## Regulatory Changes

No new regulatory change; this is a reminder reiterating the discontinuation timeline first communicated via circular NSE/MSD/74567 dated June 05, 2026.

## Compliance Requirements

Members using the Solace API for order book snapshot recovery in FO and CD segments must migrate to the TCP/IP method using the specified IP and port parameters before the discontinuation date. Members must also ensure adequate infrastructure sizing and maintain their own redundancy for market data broadcast subscriptions.

## Important Dates

- June 05, 2026: Original circular NSE/MSD/74567 issued.
- July 02, 2026: This reminder circular issued.
- July 04, 2026: Discontinuation of Order Snapshot Recovery through Solace API for FO and CD segments takes effect.

## Impact Assessment

The impact is operational and limited to NSE trading members who still depend on the Solace API for order snapshot recovery in FO and CD segments. Failure to migrate to the TCP/IP method before July 04, 2026 could disrupt access to order book snapshot data, potentially affecting trading operations and risk management for affected members. There is no direct impact on listed securities or the broader market.