---
category: trading
circular_id: 94c0bd558f6e1bea
date: '2025-08-28'
description: BSE extends rollout of enhanced market data streams with parallel format
  support for NFCAST streams during transition period.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={B1F84EB1-EFF3-4EA5-AD4B-CB7458CADAC5}&noticeno=20250828-10&dt=08/28/2025&icount=10&totcount=47&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Critical infrastructure change affecting all trading members and vendors
  with specific migration deadlines
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20250828-10&attachedId=
processing:
  attempts: 1
  content_hash: b026164dc4a29d69
  processed_at: '2025-08-28T12:48:42.835979'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-08-28T07:37:52+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={B1F84EB1-EFF3-4EA5-AD4B-CB7458CADAC5}&noticeno=20250828-10&dt=08/28/2025&icount=10&totcount=47&flag=0
severity: high
source: bse
stocks: []
tags:
- market-data
- market-infrastructure
- multicast
- nfcast
- system-update
title: Enhancement in Market Data Streams – Update
---

## Summary

BSE announces a phased rollout approach for enhanced market data streams, providing parallel support for existing and new NFCAST formats during transition. Currency/Commodities Derivatives go-live September 8, Equity Derivatives September 15, and Equity September 22, 2025. Existing format support ends October 3-10, 2025 depending on segment.

## Key Points

- Parallel run of existing and new NFCAST formats for limited transition period
- New multicast IP addresses and ports assigned for new format streams
- EOBI/EMDI/MDI streams switch directly to new format without parallel support
- Mock trading sessions scheduled before each segment go-live
- Staggered implementation across Currency Derivatives, Equity Derivatives, and Equity segments

## Regulatory Changes

- Enhanced market data stream format implementation across all BSE segments
- New multicast IP and port configurations for NFCAST streams
- Mandatory migration from existing to new data formats by specified deadlines

## Compliance Requirements

- Trading members and third-party vendors must update trading applications
- System development required to support new multicast IPs and ports
- Migration from existing format must be completed before discontinuation dates
- Participation in mock trading sessions recommended for testing

## Important Dates

- **September 6, 2025**: Mock trading for Currency/Commodities Derivatives & EGR
- **September 8, 2025**: Go-live for Currency/Commodities Derivatives & EGR
- **September 13, 2025**: Mock trading for Equity Derivatives
- **September 15, 2025**: Go-live for Equity Derivatives
- **September 20, 2025**: Mock trading for Equity segment
- **September 22, 2025**: Go-live for Equity segment
- **October 3, 2025**: Existing format discontinuation for Currency/Equity Derivatives
- **October 10, 2025**: Existing format discontinuation for Equity segment

## Impact Assessment

**High Impact**: All trading members and technology vendors must upgrade systems. Failure to migrate by deadline will result in loss of market data access. The phased approach with parallel streams provides transition time but requires careful planning and testing to ensure smooth migration without trading disruptions.