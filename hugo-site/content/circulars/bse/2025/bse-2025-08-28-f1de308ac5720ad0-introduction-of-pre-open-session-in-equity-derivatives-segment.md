---
category: trading
circular_id: f1de308ac5720ad0
date: '2025-08-28'
description: BSE introduces pre-open session for equity derivatives with detailed
  messaging format specifications for market participants.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={501AE259-8F06-42B5-8731-AA973E109EFF}&noticeno=20250828-11&dt=08/28/2025&icount=11&totcount=47&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Major trading infrastructure change affecting all equity derivatives
  participants with new session structure and messaging requirements
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20250828-11&attachedId=581060ac-86b5-4a19-80db-bdeeb0cc0aa3
processing:
  attempts: 1
  content_hash: b3a70ae2c87c1e67
  processed_at: '2025-08-28T12:49:03.015379'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-08-28T07:47:32+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={501AE259-8F06-42B5-8731-AA973E109EFF}&noticeno=20250828-11&dt=08/28/2025&icount=11&totcount=47&flag=0
severity: high
source: bse
stocks: []
tags:
- auction-clearing-price
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

BSE has introduced a Pre-Open Session in the Equity Derivatives Segment with detailed technical specifications for market participants. The implementation uses existing ETI messaging format for order management while providing specific market data communication protocols across four distinct streams (EOBI, EMDI, MDI, NFCAST).

## Key Points

- ETI API messaging format remains unchanged for order management during pre-open session
- All existing order-related actions (addition, modification, deletion) can be performed using current ETI messages
- No auction-exclusive messages required for equity derivatives pre-open session
- Market data disseminated through four streams with specific messaging formats
- Session phases include Pre-open Order Entry, Pre-open Freeze, Pre-open Matching End, and Continuous Session

## Technical Specifications

### EOBI Stream Messages:
- Product State Message (Template ID: 13300) with TradingSessionSubID = 1
- Mass Instrument State Message (Template ID: 13301) with SecurityTradingStatus values: 4 (pre-open entry), 5 (freeze), 1 (matching end), 3 (continuous)
- Auction Clearing Price Message (Template ID: 13501) during pre-open session

### EMDI/MDI Stream Messages:
- SecurityMassTradingStatus values: 4 (pre-open entry), 5 (freeze), 0 (matching), 3 (continuous)
- Special MDEntryType enum values: 6 (Auction Clearing Price), 12 (Auction Bid Cancel), 13 (Auction Offer Cancel)
- Depth Incremental and Depth Snapshot messages for order actions

### NFCAST Stream:
- Implementation details for pre-open session messaging (content appears truncated in source)

## Compliance Requirements

- Market participants must review complete messaging format documents to identify all auction-related specifications
- Applications may require changes to handle new session states and message types
- Members strongly advised to assess required changes in their trading applications
- Order-by-order updates continue as in current sessions

## Important Dates

No specific implementation dates mentioned in the circular content provided.

## Impact Assessment

**High Impact on Trading Infrastructure:**
- All equity derivatives market participants affected
- Trading systems must handle new session phases and state transitions
- Market data feed consumers need to process additional message types
- Price discovery mechanism through auction clearing price affects trading strategies
- System testing required for new session handling and message processing