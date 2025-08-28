---
category: trading
circular_id: fa3514ae6d6e6351
date: '2025-08-28'
description: BSE introduces pre-open session in equity derivatives with technical
  specifications for order management and market data communication.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={501AE259-8F06-42B5-8731-AA973E109EFF}&noticeno=20250828-11&dt=08/28/2025&icount=11&totcount=59&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical implementation affecting equity derivatives trading operations
  and market data systems
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20250828-11&attachedId=581060ac-86b5-4a19-80db-bdeeb0cc0aa3
processing:
  attempts: 1
  content_hash: c742628cbf55e42b
  processed_at: '2025-08-28T18:42:32.888240'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-08-28T07:47:32+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={501AE259-8F06-42B5-8731-AA973E109EFF}&noticeno=20250828-11&dt=08/28/2025&icount=11&totcount=59&flag=0
severity: medium
source: bse
stocks: []
tags:
- pre-open-session
- equity-derivatives
- market-data
- trading-session
- ETI-API
- EOBI
- EMDI
- MDI
- NFCAST
- technical-specifications
title: Introduction of Pre-Open Session in Equity Derivatives Segment
---

## Summary

BSE has issued technical specifications for the implementation of pre-open session in the equity derivatives segment. The circular provides detailed messaging format requirements for ETI API and market data communication streams (EOBI, EMDI, MDI, NFCAST) during pre-open sessions.

## Key Points

- ETI messaging format for order management remains unchanged during pre-open session
- All existing order-related actions (addition, modification, deletion) can be performed using current ETI messages
- No auction-exclusive messages required for equity derivatives pre-open session
- Market data dissemination continues through four distinct streams with specific field values for auction sessions
- Different SecurityTradingStatus values for various pre-open phases: 4 (order entry), 5 (freeze), 1 (matching end), 3 (continuous)

## Regulatory Changes

- Introduction of pre-open session in equity derivatives segment
- Specific template IDs and field values defined for different market data streams
- New auction clearing price message (Template ID: 13501) during pre-open session
- Enhanced market data communication with auction-specific enum values

## Compliance Requirements

- Members must review complete messaging format documents to identify all auction-related specifications
- Trading systems need to handle new SecurityTradingStatus and SecurityMassTradingStatus field values
- Market data consumers must accommodate auction clearing price messages and new MDEntryType enum values (6, 12, 13)
- Applications may require updates to process pre-open session states correctly

## Important Dates

No specific implementation dates mentioned in the circular.

## Impact Assessment

Medium impact on equity derivatives trading infrastructure. While existing order management remains unchanged, market data systems and trading applications will need updates to handle pre-open session states and auction-related messages. The change primarily affects technical systems rather than trading procedures.