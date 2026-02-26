---
category: trading
circular_id: 03d9320a41f73ced
date: '2026-02-26'
description: BSE mandates renewal of the CA certificate used for TLS-encrypted trading
  channel communication before March 7, 2026. Failure to update will result in inability
  to connect to exchange trading systems.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={C845A678-43CE-4C4F-88B9-FCB97B9657DB}&noticeno=20260226-1&dt=02/26/2026&icount=1&totcount=28&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Mandatory technical action required by all trading members across all
  segments before March 7, 2026; non-compliance will result in complete disconnection
  from BSE trading systems.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260226-1&attachedId=
processing:
  attempts: 1
  content_hash: e1482a0119daa8b7
  processed_at: '2026-02-26T13:21:09.918943'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-02-26T03:17:12+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={C845A678-43CE-4C4F-88B9-FCB97B9657DB}&noticeno=20260226-1&dt=02/26/2026&icount=1&totcount=28&flag=0
severity: high
source: bse
stocks: []
tags:
- tls
- ca-certificate
- trading-connectivity
- technology
- infrastructure
- equity
- derivatives
- currency
- commodities
title: Renewal of CA Certificate for TLS Communication with BSE Exchange
---

## Summary

BSE has announced the renewal of the CA certificate used for TLS-encrypted communication between member applications and the exchange's trading systems. The current certificate is set to expire in March 2026. Members must replace the old CA certificate with the new one in their applications before March 7, 2026, after which the old certificate will no longer be accepted by the exchange.

## Key Points

- The existing CA certificate for TLS communication with BSE trading systems is expiring in March 2026
- The new CA certificate will be mandatory across **all segments** (Equity, Equity Derivatives, Currency Derivatives, Commodities Derivatives) effective **March 7, 2026**
- Member applications failing to update the certificate will be unable to connect to BSE trading systems from that date
- No changes are required to application code — only the certificate file needs to be replaced
- No changes in connection parameters for any segment
- A mock/connectivity test session is scheduled on **March 7, 2026** for members to validate their updated configurations
- The new certificate will be live in the **test/simulation environment from February 27, 2026**
- The new CA certificate is common across all segments and is available at **www.bseindia.com/nta.aspx**

## Regulatory Changes

No regulatory policy changes. This is a technical infrastructure update — BSE is upgrading its TLS certificate infrastructure as part of routine certificate lifecycle management. The exchange will stop accepting connections using the old CA certificate from March 7, 2026.

## Compliance Requirements

- **All trading members** must download the new CA certificate from [www.bseindia.com/nta.aspx](http://www.bseindia.com/nta.aspx)
- Replace the old CA certificate with the new certificate in all member trading applications
- Validate connectivity using the simulation environment before February 27, 2026 and participate in the mock session on March 7, 2026
- Contact BSE Tech Support for queries:
  - Phone: 022-22728053
  - Email: bse.tech@bseindia.com
  - Alternatively, contact the respective Relationship Manager

## Important Dates

| Date | Event |
|------|-------|
| February 27, 2026 | New CA certificate goes live in test/simulation environment |
| March 7, 2026 | New CA certificate mandatory in production across all segments |
| March 7, 2026 | Mock connectivity session scheduled for member testing |
| March 2026 | Existing CA certificate expiry deadline |

## Impact Assessment

**Operational Impact: High** — All trading members connected to BSE across Equity, Equity Derivatives, Currency Derivatives, and Commodities Derivatives segments are affected. Members who do not update their CA certificate by March 7, 2026, will lose connectivity to BSE trading systems entirely, disrupting their trading operations.

**Implementation Effort: Low** — The update requires only replacing the certificate file in the member application; no code changes or connection parameter updates are needed.

**Risk of Non-Compliance: Critical** — Complete inability to connect to BSE trading systems from March 7, 2026, if the certificate is not updated. Members are strongly advised to test in the simulation environment from February 27 onwards to ensure a smooth transition.