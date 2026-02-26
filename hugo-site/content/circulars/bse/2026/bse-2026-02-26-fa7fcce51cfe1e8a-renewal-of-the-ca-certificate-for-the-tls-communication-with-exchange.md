---
category: trading
circular_id: fa7fcce51cfe1e8a
date: '2026-02-26'
description: BSE mandates renewal of the CA certificate used for TLS-encrypted trading
  channel communication before March 2026 expiry. New certificate becomes mandatory
  across all segments from 7th March 2026.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={C845A678-43CE-4C4F-88B9-FCB97B9657DB}&noticeno=20260226-1&dt=02/26/2026&icount=1&totcount=47&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Mandatory certificate replacement with hard deadline — failure to update
  will result in trading members being unable to connect to BSE trading systems, causing
  potential trading disruption across all segments from 7th March 2026.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260226-1&attachedId=
processing:
  attempts: 1
  content_hash: ab8e8fe14e27bfbc
  processed_at: '2026-02-26T16:21:32.347353'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-02-26T03:17:12+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={C845A678-43CE-4C4F-88B9-FCB97B9657DB}&noticeno=20260226-1&dt=02/26/2026&icount=1&totcount=47&flag=0
severity: high
source: bse
stocks: []
tags:
- tls
- ca-certificate
- trading-connectivity
- technical-infrastructure
- encryption
- trading-members
- connectivity
title: Renewal of CA Certificate for TLS Communication with BSE Exchange
---

## Summary

BSE has announced the renewal of its CA (Certificate Authority) certificate used for TLS-encrypted communication over the trading channel. The existing certificate is set to expire in March 2026. Trading members must replace the old certificate with the new one in their member applications before 7th March 2026, after which the new certificate becomes mandatory across all market segments.

## Key Points

- The current CA certificate used for TLS communication with BSE trading systems will expire in March 2026
- The new CA certificate will be mandatory across all segments — Equity, Equity Derivatives, Currency Derivatives, and Commodities Derivatives — effective **7th March 2026**
- Member applications that do not update to the new certificate will be unable to connect to BSE trading systems from that date
- No changes are required to the member application itself; only the certificate file needs to be replaced
- There is no change in any connection parameters for any segment
- A mock/connectivity test session will be held on 7th March 2026 to allow members to verify connectivity before live trading resumes on Monday
- The new certificate will be active in the test/simulation environment from **27th February 2026** onwards
- The new TLS CA certificate (common for all segments) is available for download at: [www.bseindia.com/nta.aspx](http://www.bseindia.com/nta.aspx)

## Regulatory Changes

No regulatory rule changes. This is an operational/infrastructure update — the exchange is upgrading its TLS CA certificate as part of routine certificate lifecycle management. The exchange system will be updated to accept only the new certificate from 7th March 2026 onwards.

## Compliance Requirements

- **Trading members** must download the new CA certificate from [www.bseindia.com/nta.aspx](http://www.bseindia.com/nta.aspx)
- Replace the old CA certificate with the new certificate in their member/trading applications
- Test connectivity using the simulation environment (available from 27th February 2026) and/or the mock session on 7th March 2026
- Ensure the update is completed before 7th March 2026 to avoid any disruption to live trading
- Contact BSE Tech Support for queries: **022-22728053** or **bse.tech@bseindia.com**

## Important Dates

| Date | Event |
|------|-------|
| 27th February 2026 (Friday) | New certificate active in test/simulation market |
| 7th March 2026 (Saturday) | New certificate mandatory in production across all segments; mock connectivity session scheduled |
| March 2026 | Expiry of existing CA certificate |

## Impact Assessment

**Operational Impact: HIGH** — This is a mandatory infrastructure change affecting all trading members connected to BSE across all segments (Equity, Equity Derivatives, Currency Derivatives, Commodities Derivatives). Non-compliance will result in complete loss of connectivity to BSE trading systems from 7th March 2026, making trading impossible until the certificate is updated. The change itself is low-complexity (replace a certificate file, no code changes needed), but the deadline is firm and the consequence of missing it is severe. Members are advised to prioritize this update well ahead of the deadline, leveraging the simulation environment and mock session for testing.