---
category: trading
circular_id: eb228bc5922abd6a
date: '2025-08-28'
description: BSE announces phased rollout of enhanced market data streams with parallel
  support for existing format during transition period.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={B1F84EB1-EFF3-4EA5-AD4B-CB7458CADAC5}&noticeno=20250828-10&dt=08/28/2025&icount=10&totcount=58&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Critical system changes affecting all trading members and vendors with
  specific migration timelines and new multicast configurations
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20250828-10&attachedId=
processing:
  attempts: 1
  content_hash: 68910e56962111eb
  processed_at: '2025-08-28T15:35:42.740070'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-08-28T07:37:52+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={B1F84EB1-EFF3-4EA5-AD4B-CB7458CADAC5}&noticeno=20250828-10&dt=08/28/2025&icount=10&totcount=58&flag=0
severity: high
source: bse
stocks: []
tags:
- market-data
- trading-systems
- nfcast
- eobi
- emdi
- mdi
- multicast
- system-upgrade
title: Enhancement in Market Data Streams – Update with Parallel Run Implementation
---

## Summary

BSE announces a phased approach to implementing enhanced market data streams with parallel run support for NFCAST streams. The exchange will provide both existing and new format streams simultaneously during transition period, with segment-wise rollout from September 8-22, 2025, and discontinuation of parallel support by October 6-13, 2025.

## Key Points

- Parallel run of existing and new NFCAST market data formats to facilitate smooth migration
- New format streams will use different multicast IP addresses and ports
- EOBI/EMDI/MDI streams will switch directly to new format without parallel support
- Segment-wise implementation schedule spans September 8-22, 2025
- Mock trading sessions scheduled for September 6, 13, and 20, 2025
- Existing format support ends between October 6-13, 2025

## Regulatory Changes

- Introduction of new market data stream formats across all segments
- Implementation of new multicast IP and port configurations
- Mandatory migration from existing to new format within specified timeframes

## Compliance Requirements

- Trading members must update systems to support new market data formats
- Third-party trading application vendors must implement necessary changes
- System development and testing required before go-live dates
- Participation in mock trading sessions recommended

## Important Dates

- **September 6, 2025**: Mock trading for Currency Derivatives, Commodities Derivatives & EGR
- **September 8, 2025**: Go-live for Currency Derivatives, Commodities Derivatives & EGR (EOBI/EMDI/MDI and NFCAST)
- **September 13, 2025**: Mock trading for Equity Derivatives
- **September 15, 2025**: Go-live for Equity Derivatives (EOBI/EMDI/MDI and NFCAST)
- **September 20, 2025**: Mock trading for Equity segment
- **September 22, 2025**: Go-live for Equity segment (EOBI/EMDI/MDI and NFCAST)
- **October 3, 2025**: Last day of parallel support for Currency/Commodities Derivatives & EGR NFCAST
- **October 6, 2025**: Discontinuation of existing format for Currency/Commodities/Equity Derivatives NFCAST
- **October 10, 2025**: Last day of parallel support for Equity NFCAST
- **October 13, 2025**: Discontinuation of existing format for Equity NFCAST

## Impact Assessment

**High Impact**: All trading members and third-party vendors must implement system changes within tight timelines. The parallel run approach reduces migration risk but requires careful coordination. New multicast configurations may require network infrastructure updates. Failure to migrate by deadline dates will result in loss of market data access for affected systems.