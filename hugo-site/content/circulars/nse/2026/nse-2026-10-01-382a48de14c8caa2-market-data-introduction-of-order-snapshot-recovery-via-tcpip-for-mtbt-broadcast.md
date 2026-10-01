---
category: market-operations
circular_id: 382a48de14c8caa2
date: '2026-10-01'
description: National Stock Exchange introduces order book snapshot recovery via TCP/IP
  for MTBT broadcast in the Commodity Derivatives segment effective October 12, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD76689.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Introduces order snapshot recovery via TCP/IP for the Commodity Derivatives
  segment, improving order book recovery for trading members.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD76689.pdf
processing:
  attempts: 1
  content_hash: e554470dc62f40e7
  processed_at: '2026-10-01T20:24:17.102709'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-10-01T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD76689.pdf
severity: low
source: nse
stocks: []
tags:
- market-data
- commodity-derivatives
- tcp-ip
- mtbt
- order-snapshot-recovery
title: Market Data - Introduction of Order Snapshot Recovery via TCP/IP for MTBT broadcast
  in Commodity Segment
---

## Summary

The National Stock Exchange (NSE) has announced the introduction of Order Book Snapshot Recovery via TCP/IP for MTBT broadcast in the Commodity Derivatives (CO) segment, effective October 12, 2026. This functionality aims to enhance trading experiences, enable greater customization, and improve efficiency for members.

## Key Points

- Order book snapshot recovery is extended to the Commodity Derivatives segment (previously available in CM, FO, and CD segments).
- MTBT Order Book Snapshot Recovery Server provides the latest picture of the order book, constructed from MTBT feed and refreshed every 30 seconds.
- Connection parameters for Commodity segment Order Snapshot Recovery: IP `172.19.125.84`, Port `10969`.
- Effective implementation date: October 12, 2026.
- Members are advised to use snapshot recovery when losing a large number of ticks on multicast or joining the MTBT feed late.
- Client applications must disconnect after receiving the snapshot message.

## Regulatory Changes

- Extension of MTBT order snapshot recovery infrastructure to the Commodity Derivatives segment under consolidated circular framework NSE/MSD/74019.

## Compliance Requirements

- Members subscribing to market data broadcasts must monitor and adequately size their infrastructure and systems.
- Members are solely responsible for implementing and maintaining redundancy for market data broadcasts.
- Reference MBT API document version 7.1 for detailed technical implementation available on the Exchange website.

## Important Dates

- Date of Circular: October 01, 2026
- Effective Date of Implementation: October 12, 2026

## Impact Assessment

- Improves operational efficiency and tick recovery for trading members operating in the Commodity Derivatives segment by enabling fast snapshot recovery over TCP/IP.