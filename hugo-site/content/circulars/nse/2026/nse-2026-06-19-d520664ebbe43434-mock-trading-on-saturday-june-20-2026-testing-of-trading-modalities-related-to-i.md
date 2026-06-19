---
category: market-operations
circular_id: d520664ebbe43434
date: '2026-06-19'
description: NSE will conduct mock trading in the Futures & Options segment on June
  20, 2026 to test trading modalities related to the introduction of Closing Auction
  Session (CAS) in the Equity Cash segment, including a new NEATPlus version 7.8.9
  for Session 1.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP74791.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational circular requiring member action for mock trading participation
  and software version management; no immediate market or price impact but mandatory
  preparation for upcoming CAS implementation.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP74791.pdf
processing:
  attempts: 1
  content_hash: 2c8d9750876dccb7
  processed_at: '2026-06-19T15:46:09.523289'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-19T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP74791.pdf
severity: medium
source: nse
stocks: []
tags:
- mock-trading
- futures-and-options
- closing-auction-session
- equity-cash-segment
- neatplus
- dr-site
- settlement-calendar
title: Mock Trading on Saturday, June 20, 2026 - Testing of Closing Auction Session
  (CAS) in Equity Cash Segment
---

## Summary

NSE will conduct a mock trading session in the Futures & Options (F&O) segment on Saturday, June 20, 2026, to test trading modalities related to the introduction of the Closing Auction Session (CAS) in the Equity Cash segment. The mock involves three trading sessions across Primary and Disaster Recovery (DR) sites, with members required to use a new NEATPlus version (7.8.9) exclusively for Session 1, then revert to version 7.8.8 for Sessions 2 and 3.

## Key Points

- Three mock trading sessions are scheduled: Session 1 from DR Site (09:00–11:20), Session 2 from Primary Site (13:45–15:45), and Session 3 from DR Site (16:30–17:25)
- NEATPlus version 7.8.9 must be used for Session 1 only; members must reinstall NEATPlus 7.8.8 before Sessions 2 and 3
- NEATPlus 7.8.9 will be available on NSE Extranet at `/faoftp/faocommon/Mock/20JUNE2026/NEATPlus789` from 07:00 on June 20, 2026
- During Session 1, stock futures price bands will be updated at 10:25 to align with CAS in the CM segment, using VWAP of trades between 10:10 and 10:25
- Trades from Session 1 will not carry over to Sessions 2 or 3; trades from Session 2 will be available in Session 3
- Live re-login window is 18:30–19:00
- Members must use the new NEAT Adapter (version 1.0.29) with new CA certificate and port 10841 for F&O, mandatory from July 06, 2026 (mock)
- Both NEATPlus versions 7.8.8 and 7.8.9 are compatible with new broadcast parameters (refer circular NSE/MSD/74448 dated May 27, 2026)

## Regulatory Changes

This mock tests changes related to the introduction of Closing Auction Session (CAS) in the Equity Cash segment, originally announced in circular NSE/FAOP/74467 dated May 29, 2026. The CAS implementation changes trading modalities in the Equity Derivatives segment, including new stock futures price band alignment logic based on VWAP during the CAS window.

## Compliance Requirements

- Members must download and use NEATPlus 7.8.9 exclusively for Trading Session 1 of the mock
- Members must reinstall NEATPlus 7.8.8 after Session 1 concludes for Sessions 2 and 3, and for live trading from June 22, 2026
- Members must adopt the new NEAT Adapter (version 1.0.29 for Windows and Linux) with new CA certificate (mandatory from July 06, 2026 mock)
- Members must use the applicable GR port 10841 for F&O login via the new NEAT adapter
- All members are requested to actively participate in all three mock trading sessions
- Refer to circulars NSE/MSD/74511 (June 02, 2026) and NSE/MSD/74559 (June 05, 2026) for CA certificate and NEAT Adapter details

## Important Dates

- **June 20, 2026**: Mock trading day
  - 07:00 – NEATPlus 7.8.9 available for download
  - 09:00–11:20 – Trading Session 1 (DR Site)
  - 13:45–15:45 – Trading Session 2 (Primary Site)
  - 16:30–17:25 – Trading Session 3 (DR Site)
  - 18:30–19:00 – Live Re-login window
- **June 22, 2026**: Live trading resumes using NEATPlus 7.8.8
- **July 06, 2026**: New NEAT Adapter (v1.0.29) with new CA certificate becomes mandatory for F&O segment (mock)

## Impact Assessment

This circular has medium operational impact for NSE F&O members. Members must manage two different NEATPlus software versions within the same mock day, requiring careful coordination and reinstallation between sessions. The mock is preparatory for the CAS introduction in the Equity Cash segment, which will alter price band update mechanisms for stock futures. Failure to participate or use the correct software version may result in connectivity issues during the mock and potential unpreparedness for the live CAS rollout. There is no direct market price impact, but members' operational readiness for the upcoming CAS implementation is at stake.