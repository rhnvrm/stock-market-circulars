---
category: market-operations
circular_id: e94ad52e574b0647
date: '2026-07-01'
description: NSE will conduct mock trading in the F&O segment on July 04, 2026 across
  three sessions to test trading modalities related to the upcoming Closing Auction
  Session (CAS) in the Equity Cash segment, including a new NEATPlus version.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP74981.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational advisory for members on mock trading sessions and software
  version testing ahead of CAS rollout; no direct stock-specific or immediate market
  impact, but non-compliance could disrupt trading readiness.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP74981.pdf
processing:
  attempts: 1
  content_hash: 0f508a6b6fc185a7
  processed_at: '2026-07-01T20:04:19.581368'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-07-01T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP74981.pdf
severity: medium
source: nse
stocks: []
tags:
- mock-trading
- introduction-of-futures-contracts
- settlement-calendar
- live-activities-schedule
title: Mock Trading on Saturday, July 04, 2026 for Closing Auction Session (CAS) Testing
  in Equity Cash Segment
---

## Summary

NSE will conduct a mock trading session in the Futures & Options segment on Saturday, July 04, 2026, to test trading modalities related to the introduction of the Closing Auction Session (CAS) in the Equity Cash segment. The mock comprises three trading sessions, and requires members to use a new NEATPlus version (7.8.9) specifically for Session 1, before reverting to the existing version (7.8.8) for Sessions 2 and 3 and for live trading resuming July 06, 2026. Additional CAS-related mock sessions are scheduled for July 11, 18, and 25, 2026.

## Key Points

- Mock trading date: Saturday, July 04, 2026, across three trading sessions (Session 1 from Primary Site testing CAS-related changes, Session 2 from Primary Site, and Session 3 from DR Site).
- New NEATPlus version 7.8.9 must be used exclusively for Trading Session 1, downloadable from NSE Extranet path /faoftp/faocommon/Mock/04JULY2026/NEATPlus789, available from 07:00 hrs on July 04, 2026.
- After Session 1, members must reinstall and log in with the earlier NEATPlus version 7.8.8 (from /faoftp/faocommon/NEATPlus788) for Sessions 2 and 3, and for live trading resuming July 06, 2026.
- During Session 1, stock futures price bands will be updated for alignment with CAS in the CM segment, with reference price based on VWAP of stock futures trades executed between 09:00 a.m. and 09:15 a.m.
- Trades from Session 1 will not carry over to Sessions 2 or 3; trades from Session 2 will be available in Session 3. Members are asked to actively participate in all sessions.
- Both NEATPlus versions (7.8.8 and 7.8.9) are compatible with new broadcast parameters referenced in circular NSE/MSD/74448 dated May 27, 2026.
- Order book snapshot recovery via Solace API is being discontinued from July 04, 2026.
- Additional mock trading sessions for CAS testing in the CM segment are scheduled for July 11, July 18, and July 25, 2026, with timings to be announced separately.

## Regulatory Changes

This circular does not itself introduce a regulatory change but operationalizes testing for the previously announced Introduction of Closing Auction Session (CAS) in the Equity Cash segment (per circular NSE/FAOP/74467 dated May 29, 2026) and continues testing referenced in circular dated December 24, 2025 (Download No. 71999).

## Compliance Requirements

- Members must download and install NEATPlus version 7.8.9 for Session 1 only, then reinstall version 7.8.8 for Sessions 2, 3, and subsequent live trading.
- Members must actively participate in all three mock trading sessions.
- Members relying on Solace API for order book snapshot recovery must transition away from it as it will be discontinued from July 04, 2026.
- Members should refer to circular NSE/MSD/74448 for updated market data broadcast parameters.

## Important Dates

- July 04, 2026: Mock trading session (Sessions 1, 2, and 3) with CAS-related testing.
- July 06, 2026: Live trading resumes using NEATPlus version 7.8.8.
- July 11, 18, and 25, 2026: Additional mock trading sessions for CAS testing in the CM segment (timings to be announced).

## Impact Assessment

This is an operational/technical advisory primarily affecting NSE trading members' IT and trading infrastructure readiness ahead of the CAS rollout in the Equity Cash segment. Failure to use the correct NEATPlus version in the correct session, or to transition away from the Solace API for order book snapshot recovery, could disrupt a member's mock or live trading operations. There is no direct impact on listed securities or investors at this stage, but successful testing is a prerequisite for the broader CAS implementation affecting the equity cash market.