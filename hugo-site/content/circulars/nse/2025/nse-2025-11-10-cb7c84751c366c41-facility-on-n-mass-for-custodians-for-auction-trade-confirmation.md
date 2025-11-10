---
category: market-operations
circular_id: cb7c84751c366c41
date: '2025-11-10'
description: NSE Clearing introduces auction trade confirmation facility for custodians
  through N-MASS application for trades executed with custodial participant codes.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT71182.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational enhancement for custodians to confirm auction trades via
  N-MASS system. Medium impact limited to custodians participating in auction market.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT71182.zip
processing:
  attempts: 1
  content_hash: a8bca19f173217d6
  processed_at: '2025-11-10T09:24:31.164979'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-11-10T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT71182.zip
severity: low
source: nse
stocks: []
tags:
- n-mass
- custodians
- auction-trade
- trade-confirmation
- clearing
- capital-market
title: Facility on N-MASS for Custodians for Auction Trade Confirmation
---

## Summary

NSE Clearing Limited has introduced a new trade confirmation facility for custodians to confirm trades executed in the auction market with custodial participant (CP) codes. The facility is available through the N-MASS application and includes both file upload and screen-based confirmation methods.

## Key Points

- Trade confirmation facility extended to custodians for auction market trades with CP codes
- Available through N-MASS application effective November 10, 2025
- Two confirmation methods: file upload and screen-based confirmation
- Confirmation window: 3:30 PM to 4:15 PM daily
- Custodians must assign "Auction Trade" service through Role Management menu with 'Write' access
- "Approve All" functionality available for bulk confirmation/rejection

## File Upload Process

**Download File Format:**
- Nomenclature: `<Custodian Code>AUCTION_<DDMMYYYY>.Dnn`
- Contains: Settlement No, Settlement Type, Quantity, Symbol, Series, TM Code, Custodial Participant Code, Value, WAP, Trade Date, Order Number
- Can be generated multiple times and includes all records (confirmed, rejected, pending)

**Upload File Format:**
- Nomenclature: `<Custodian Code>AUCTION_<DDMMYYYY>.Unn`
- Same fields as download file plus Confirmation Flag (Y/N) in last column
- Custodians mark 'Y' for confirmation or 'N' for rejection

## Compliance Requirements

- Custodians must configure role management to access the Auction Trade menu
- Write access must be enabled for the service
- Confirmation/rejection must be submitted during the designated time window (3:30 PM - 4:15 PM)

## Important Dates

- **Effective Date:** November 10, 2025
- **Daily Confirmation Window:** 3:30 PM to 4:15 PM

## Impact Assessment

**Operational Impact:** Streamlines auction trade confirmation process for custodians, replacing manual confirmation methods with automated file-based and screen-based systems. This enhancement improves operational efficiency and reduces processing time for custodial participants in the auction market segment.

**User Groups Affected:** Custodians participating in NSE's auction market segment with custodial participant codes.