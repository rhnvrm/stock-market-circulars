---
category: trading
circular_id: 85b59414f46c0817
date: '2025-08-28'
description: BSE introduces pre-open session for equity derivatives with detailed
  messaging format specifications for ETI API and market data communication.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={501AE259-8F06-42B5-8731-AA973E109EFF}&noticeno=20250828-11&dt=08/28/2025&icount=11&totcount=58&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Major trading infrastructure change affecting all equity derivatives
  trading participants
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20250828-11&attachedId=581060ac-86b5-4a19-80db-bdeeb0cc0aa3
processing:
  attempts: 1
  content_hash: 6f561bd9a65fe64a
  processed_at: '2025-08-28T15:35:18.221339'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-08-28T07:47:32+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={501AE259-8F06-42B5-8731-AA973E109EFF}&noticeno=20250828-11&dt=08/28/2025&icount=11&totcount=58&flag=0
severity: high
source: bse
stocks: []
tags:
- derivatives
- emdi
- eobi
- eti-api
- market-data
- mdi
- nfcast
- pre-open-session
- trading-session
title: Introduction of Pre-Open Session in Equity Derivatives Segment
---

## Summary

BSE is introducing a Pre-Open Session in the Equity Derivatives Segment with detailed technical specifications for order management and market data communication. The implementation maintains existing ETI messaging format for order operations while defining specific market data protocols across four communication streams (EOBI, EMDI, MDI, NFCAST).

## Key Points

- ETI API messaging format remains unchanged for order management during pre-open session
- All existing order actions (addition, modification, deletion) can be performed using current ETI messages
- No auction-exclusive messages required for equity derivatives segment
- Market data disseminated through four distinct streams with specific messaging formats
- Pre-open session includes order entry, freeze, matching, and transition to continuous session

## Technical Specifications

### EOBI Stream Messages
- Product State Message (Template ID: 13300) with TradingSessionSubID set to 1
- Mass Instrument State Message (Template ID: 13301) with SecurityTradingStatus values:
  - 4 for Pre-open Order Entry Session
  - 5 for Pre-open Freeze
  - 1 for Pre-open Matching End
  - 3 for Continuous Session
- Auction Clearing Price Message (Template ID: 13501) during pre-open session

### EMDI/MDI Stream Messages
- SecurityMassTradingStatus field values:
  - 4 for Pre-open Order Entry
  - 5 for Pre-open Freeze
  - 0 for Pre-open Matching
  - 3 for Continuous Session
- New MDEntryType enum values: 6 (Auction Clearing Price), 12 (Auction Bid Cancel), 13 (Auction Offer Cancel)

## Compliance Requirements

- Members must review complete messaging format documents for all auction-related specifications
- Applications may require changes to handle new session states and message types
- Systems must be updated to process auction clearing price messages
- Order-by-order updates continue as in current sessions

## Important Dates

No specific implementation date mentioned in the circular content provided.

## Impact Assessment

High impact on all equity derivatives trading participants as this introduces a new trading session phase. Members need to assess and potentially modify their trading systems to handle the new pre-open session messaging protocols. The change affects order management systems, market data processing, and trading applications across all four market data communication streams.