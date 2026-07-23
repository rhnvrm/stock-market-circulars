---
category: market-operations
circular_id: 853f08edc44aa711
date: '2026-07-23'
description: NSE will conduct a mock trading session in the Futures & Options segment
  on Saturday, July 25, 2026, across three sessions to test new NEATPlus versions
  and trading modalities related to the upcoming Closing Auction Session (CAS) in
  the Equity Cash segment.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP75367.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Mandatory mock trading affects all F&O trading members' technical readiness
  and requires software version updates, but has no direct market or stock-specific
  impact.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP75367.pdf
processing:
  attempts: 1
  content_hash: 617646d84221ec94
  processed_at: '2026-07-23T16:35:06.140049'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-07-23T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP75367.pdf
severity: medium
source: nse
stocks: []
tags:
- mock-trading
- introduction-of-futures-contracts
- settlement-calendar
title: Mock Trading on Saturday, July 25, 2026 – Testing of CAS-Related Trading Modalities
  in F&O Segment
---

## Summary

NSE will conduct a mock trading session in the Futures & Options segment on Saturday, July 25, 2026, to test trading modalities related to the upcoming introduction of the Closing Auction Session (CAS) in the Equity Cash segment, as referenced in circular NSE/FAOP/74467 dated May 29, 2026. The mock comprises three trading sessions, with a new NEATPlus version (7.8.9) required specifically for Trading Session-1 to test CAS-related changes, while Trading Sessions 2 and 3 will use the existing NEATPlus version (7.8.8) with unchanged trading modalities.

## Key Points

- Mock trading date: Saturday, July 25, 2026, with three distinct trading sessions.
- Trading Session-1 tests new CAS-related modalities using NEATPlus version 7.8.9, available for download from 07:00 hours on July 25, 2026 via NSE Extranet path /faoftp/faocommon/Mock/25JULY2026/NEATPlus789.
- Post Trading Session-1, members must reinstall and revert to NEATPlus version 7.8.8 for Trading Sessions 2 and 3, downloadable at /faoftp/faocommon/NEATPlus788.
- Trading Session-2 runs from the Primary Site; Trading Session-3 runs from the DR (Disaster Recovery) Site.
- Trades from Trading Session-1 will not carry over to Sessions 2 or 3; however, trades from Session-2 will be available in Session-3.
- During Trading Session-1, reference prices for stock future contracts (to align price bands with CAS in the CM segment) will be based on VWAP of trades executed between 08:45 a.m. and 09:00 a.m.
- NEATPlus versions 7.8.8 and 7.8.9 are compatible with new broadcast parameters described in circular NSE/MSD/75324 dated July 21, 2026.
- Members using direct NNF connections must migrate to new market data broadcast parameters before existing parameters are discontinued on September 5, 2026.
- NEATPlus version 7.8.8 will also be used for live trading from July 27, 2026.

## Regulatory Changes

This circular does not introduce new regulations but operationalizes testing for the previously announced Closing Auction Session (CAS) in the Equity Cash segment (per circular NSE/FAOP/74467 dated May 29, 2026), which will change trading modalities in the Equity Derivatives segment.

## Compliance Requirements

- All F&O trading members must actively participate in all three mock trading sessions.
- Members must download and install NEATPlus 7.8.9 specifically for Trading Session-1, then reinstall NEATPlus 7.8.8 for Sessions 2 and 3.
- Members using direct NNF connections must plan migration to new broadcast parameters ahead of the September 5, 2026 discontinuation deadline.
- Members should refer to Annexures 1 and 2 (referenced in the circular) for additional mock trading instructions and pre-requisites.

## Important Dates

- July 21, 2026: Related circular NSE/MSD/75324 on market data broadcast parameters issued.
- July 23, 2026: This circular issued.
- July 25, 2026: Mock trading day (Trading Session-1: Normal Market 09:00–10:45, Trade Modification end 10:55; Trading Session-2: Normal Market 13:30–17:00; Trading Session-3: Normal Market 19:00–19:30, Trade Modification end 19:30; Re-login window 20:00 close).
- July 27, 2026: Live trading begins using NEATPlus version 7.8.8.
- September 5, 2026: Existing broadcast parameters discontinued for members on direct NNF connections.

## Impact Assessment

The impact is primarily operational and limited to NSE trading members and their technology teams, who must ensure correct software versions are installed and tested for each session. There is no direct impact on listed securities, stock prices, or investors, but failure to properly test CAS-related modalities could pose operational risk once CAS goes live in the Equity Cash segment. Timely participation ensures a smoother transition when the Closing Auction Session mechanism is implemented.