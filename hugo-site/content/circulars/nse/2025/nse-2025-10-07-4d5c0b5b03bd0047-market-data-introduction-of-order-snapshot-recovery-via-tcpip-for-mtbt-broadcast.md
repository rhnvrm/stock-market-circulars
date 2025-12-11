---
category: market-operations
circular_id: 4d5c0b5b03bd0047
date: '2025-10-07'
description: NSE introduces Order Snapshot Recovery via TCP/IP for Multicast Tick
  by Tick (MTBT) broadcast in Capital Market segment, providing an alternative to
  existing Solace API functionality.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD70675.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Introduces additional connectivity option for market data recovery,
  enhancing flexibility for members but not mandating immediate changes. Existing
  Solace API will continue during transition period.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD70675.pdf
processing:
  attempts: 1
  content_hash: 1ae3432619d2148b
  processed_at: '2025-10-07T15:55:06.410790'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-07T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD70675.pdf
severity: medium
source: nse
stocks: []
tags:
- cm-segment
- market-data
- market-infrastructure
- mtbt
- order-snapshot-recovery
- tcp-ip
- technology
title: Market Data - Introduction of Order Snapshot Recovery via TCP/IP for MTBT Broadcast
  in CM Segment
---

## Summary

NSE has introduced Order Book Snapshot Recovery functionality via TCP/IP for Multicast Tick by Tick (MTBT) broadcast in the Capital Market segment. This new connectivity method provides an alternative to the existing Solace API, enabling members to recover the latest picture of outstanding orders in the order book. The TCP/IP connectivity will be available from October 13, 2025, with both methods coexisting during a transition period before the Solace API option is discontinued.

## Key Points

- Order Snapshot Recovery via TCP/IP now available as alternative to Solace API for MTBT broadcast
- TCP/IP connection parameters: IP 172.28.124.54, Port 91069
- Functionality provides latest picture of outstanding orders in order book till last refresh time
- Effective in live environment from October 13, 2025
- Available in mock trading session on October 11, 2025
- Interim coexistence period provided for both Solace API and TCP/IP methods
- Discontinuation date for Solace API will be communicated separately
- Snapshot recovery recommended when members have lost large number of ticks or joined MTBT feed late
- Client applications should disconnect after receiving snapshot message
- Reconnection possible if disconnection occurs during snapshot recovery due to refresh at Exchange end

## Regulatory Changes

No regulatory changes introduced. This circular announces a technical enhancement to existing market data infrastructure by adding TCP/IP as an additional connectivity option for Order Snapshot Recovery functionality.

## Compliance Requirements

- Members should refer to MTBT API document (Version 6.7) available on NSE website for implementation details
- Members must monitor and adequately size their infrastructure and systems while subscribing to feeds
- Members solely responsible for implementing and maintaining redundancy for market data broadcast
- Exchange data usage restrictions as per circulars NSE/MSD/64333 (Oct 03, 2024), NSE/COMP/56426 (Apr 20, 2023), and NSE/MEM/26958 (Jun 19, 2014) remain applicable
- Exchange data can only be used by member's clients registered for trading with the member
- Members advised to use snapshot recovery when large number of ticks lost or joined MTBT feed late

## Important Dates

- **October 11, 2025**: TCP/IP Order Snapshot Recovery available in mock trading session
- **October 13, 2025**: TCP/IP Order Snapshot Recovery effective in live environment
- **To be announced**: Discontinuation date for existing Solace API order book snapshot recovery

## Impact Assessment

**Operational Impact**: Medium. Members gain additional flexibility in connectivity options for market data recovery. The TCP/IP option may improve customization capabilities and efficiency for members' trading systems. However, immediate operational changes are not mandatory due to the coexistence period.

**Technical Impact**: Members utilizing MTBT broadcast should evaluate the TCP/IP connectivity option and plan migration from Solace API before its discontinuation. Infrastructure sizing and monitoring remain critical as broadcast size varies with market activity.

**Market Impact**: Low to Medium. Enhanced market data recovery options improve overall market infrastructure resilience and may reduce recovery time for members experiencing data feed interruptions, potentially improving market efficiency.