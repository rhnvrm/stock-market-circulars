---
category: trading
circular_id: 02844a3b0cf037c6
date: '2025-08-28'
description: BSE introduces pre-open session for equity derivatives with messaging
  format specifications for ETI API and market data streams.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={501AE259-8F06-42B5-8731-AA973E109EFF}&noticeno=20250828-11&dt=08/28/2025&icount=11&totcount=12&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Major trading infrastructure change affecting all equity derivatives
  trading members requiring system updates
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20250828-11&attachedId=581060ac-86b5-4a19-80db-bdeeb0cc0aa3
processing:
  attempts: 1
  content_hash: a38e8835731af32b
  processed_at: '2025-08-28T09:21:39.390455'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-08-28T07:47:32+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={501AE259-8F06-42B5-8731-AA973E109EFF}&noticeno=20250828-11&dt=08/28/2025&icount=11&totcount=12&flag=0
severity: high
source: bse
stocks: []
tags:
- pre-open-session
- equity-derivatives
- trading-session
- market-data
- eti-api
- eobi
- emdi
- mdi
- nfcast
title: Introduction of Pre-Open Session in Equity Derivatives Segment
---

## Summary

BSE is introducing a Pre-Open Session in the Equity Derivatives Segment. The circular provides technical specifications for ETI API messaging and market data communication formats (EOBI, EMDI, MDI, NFCAST) that will be used during the pre-open session. The existing ETI messaging format for order management remains unchanged, with no auction-exclusive messages required.

## Key Points

- ETI API messaging format for order management (addition, modification, deletion) remains unchanged during pre-open session
- No auction-exclusive messages required for equity derivatives segment
- Market data disseminated through four streams: EOBI, EMDI, MDI, and NFCAST with specific field values for auction sessions
- Pre-open session includes order entry, freeze, matching, and transition to continuous session phases
- Specific template IDs and field values defined for each session phase

## Regulatory Changes

- Introduction of pre-open session for equity derivatives trading
- New SecurityTradingStatus and SecurityMassTradingStatus field values for different session phases
- Auction Clearing Price Message (Template ID: 13501) will be sent during pre-open session
- New MDEntryType enum values: 6 (Auction Clearing Price), 12 (Auction Bid Cancel), 13 (Auction Offer Cancel)

## Compliance Requirements

- Trading members must review complete messaging format documents to identify all auction-related specifications
- Members need to assess changes required in their applications
- Systems must handle new field values for TradingSessionSubID, SecurityTradingStatus, and SecurityMassTradingStatus
- Applications must process Auction Clearing Price messages and new MDEntryType values

## Important Dates

No specific implementation dates mentioned in the provided content.

## Impact Assessment

- High impact on all equity derivatives trading members requiring system modifications
- Technical changes needed to handle new session states and message formats
- Market data feed applications require updates to process auction-specific messages
- Order management systems need testing to ensure compatibility with pre-open session flow