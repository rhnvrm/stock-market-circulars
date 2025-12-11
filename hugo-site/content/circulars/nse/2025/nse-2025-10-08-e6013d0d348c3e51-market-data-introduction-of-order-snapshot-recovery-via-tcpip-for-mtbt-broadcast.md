---
category: market-operations
circular_id: e6013d0d348c3e51
date: '2025-10-08'
description: NSE updates port details for Order Snapshot Recovery through TCP/IP for
  MTBT broadcast in Cash Market segment, revising parameters from previous circular
  dated October 07, 2025.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD70707.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical update affecting market data broadcast infrastructure for
  members using Order Snapshot Recovery via TCP/IP. Critical for members utilizing
  this specific data feed but does not impact trading operations directly.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD70707.pdf
processing:
  attempts: 1
  content_hash: 6cfdd5ae0b6f347a
  processed_at: '2025-10-08T15:45:09.219805'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-08T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD70707.pdf
severity: medium
source: nse
stocks: []
tags:
- cm-segment
- market-data
- mtbt-broadcast
- order-snapshot-recovery
- port-update
- tcp-ip
- technical-infrastructure
title: Market Data - Introduction of Order Snapshot Recovery via TCP/IP for MTBT broadcast
  in CM segment - Update
---

## Summary

NSE has issued a partial modification to circular NSE/MSD/70675 dated October 07, 2025, updating the port details for Order Snapshot Recovery through TCP/IP for MTBT (Market by Trade Broadcast) in the Cash Market segment. The revised connection parameters specify IP 172.28.124.54 with Port 11984. All other details from the previous circular remain unchanged.

## Key Points

- Revised port number for Order Snapshot Recovery via TCP/IP: 11984
- IP address for connection: 172.28.124.54
- Applies to MTBT broadcast in CM (Cash Market) segment
- Partial modification of circular NSE/MSD/70675 dated October 07, 2025
- All other parameters from previous circular remain unchanged
- Contact: Toll Free 1800-266-0050 (Option 1) or msm@nse.co.in

## Regulatory Changes

This circular updates technical connection parameters for market data infrastructure. No regulatory framework changes are introduced.

## Compliance Requirements

- Members using Order Snapshot Recovery via TCP/IP must update their connection parameters to use the revised port 11984
- Members must ensure their systems connect to IP 172.28.124.54 with the updated port
- Members remain solely responsible for implementing and maintaining redundancy for market data broadcast
- Members must monitor and adequately size their infrastructure based on market activity
- Exchange data can only be used by member's clients registered for trading with the member
- Members must implement resilience and redundancy in market data subscriptions using two sources of data and/or data recovery mechanisms

## Important Dates

- Circular Date: October 08, 2025
- Effective Date: Immediate (no specific implementation deadline mentioned)
- Supersedes: Partial modification to NSE/MSD/70675 dated October 07, 2025

## Impact Assessment

**Operational Impact**: Medium - Members currently using Order Snapshot Recovery via TCP/IP for MTBT broadcast must update their connection configurations to reflect the new port number. Failure to update may result in connection failures or data feed disruptions.

**Market Impact**: Low - This is a technical infrastructure update that does not affect trading mechanics or market structure.

**Member Responsibility**: Members are reminded that they bear sole responsibility for infrastructure redundancy, bandwidth management, and any issues arising from their market data broadcast configurations. NSE will not be liable for disconnections, bandwidth utilization issues, or latency problems stemming from members' configuration decisions.

**Technical Considerations**: The broadcast size is an estimated approximation that varies with market activity, requiring members to continuously monitor and size their infrastructure appropriately.