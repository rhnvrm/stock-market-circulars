---
category: trading
circular_id: 256abf079d26d0a8
date: '2026-02-26'
description: BSE's CA certificate for TLS-encrypted trading channel communication
  expires in March 2026. All trading members must replace the old certificate with
  the new one before 7th March 2026 to maintain connectivity.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={C845A678-43CE-4C4F-88B9-FCB97B9657DB}&noticeno=20260226-1&dt=02/26/2026&icount=1&totcount=49&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Critical infrastructure change affecting all trading members across
  all segments — failure to update the CA certificate before 7th March 2026 will result
  in complete loss of connectivity to BSE trading systems.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260226-1&attachedId=
processing:
  attempts: 1
  content_hash: 789e54e97872508a
  processed_at: '2026-02-26T19:18:53.734195'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-02-26T03:17:12+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={C845A678-43CE-4C4F-88B9-FCB97B9657DB}&noticeno=20260226-1&dt=02/26/2026&icount=1&totcount=49&flag=0
severity: high
source: bse
stocks: []
tags:
- tls
- ca-certificate
- trading-system
- connectivity
- security
- infrastructure
- trading-members
- all-segments
title: Renewal of CA Certificate for TLS Communication with BSE Exchange
---

## Summary

BSE has announced the renewal of the CA certificate used for TLS-encrypted communication between member applications and the exchange trading system. The existing certificate is set to expire in March 2026. All trading members must update their applications with the new CA certificate before 7th March 2026 to avoid disruption to trading operations. The new certificate applies uniformly across all segments and is available on the BSE website.

## Key Points

- The CA certificate for TLS communication with BSE trading systems is expiring in March 2026
- New CA certificate will be mandatory across all segments effective **7th March 2026**
- Segments affected: Equity, Equity Derivatives, Currency Derivatives, and Commodities Derivatives
- Member applications that do not update the certificate will be **unable to connect** to BSE trading systems from 7th March 2026
- No changes are required to connection parameters — only the certificate needs to be replaced
- New certificate is common for all segments and is available at **www.bseindia.com/nta.aspx**
- New certificate will be applicable in the test/simulation market from **27th February 2026**
- A mock session will be conducted on **7th March 2026** to allow members to test connectivity

## Regulatory Changes

No regulatory rule changes are introduced. This is a technical infrastructure renewal mandated by BSE to maintain secure TLS-encrypted communication. The exchange will upgrade its systems to accept only the new CA certificate from 7th March 2026 onwards.

## Compliance Requirements

- Trading members must download the new CA certificate from **www.bseindia.com/nta.aspx**
- Replace the old CA certificate in member applications with the new certificate before 7th March 2026
- Test connectivity using the simulation environment (available from 27th February 2026)
- Participate in the mock session on 7th March 2026 to validate connectivity before live trading resumes on Monday
- Contact BSE Tech Support for queries: **022-22728053** or **bse.tech@bseindia.com**

## Important Dates

| Date | Event |
|------|-------|
| 27th February 2026 (Friday) | New CA certificate applicable in test/simulation market |
| 7th March 2026 (Saturday) | New CA certificate mandatory in production across all segments; mock session scheduled |
| March 2026 | Old CA certificate expiry deadline |

## Impact Assessment

This change has **high operational impact** on all trading members connected to BSE. Members who fail to update the CA certificate before 7th March 2026 will experience complete loss of connectivity to BSE trading systems, preventing them from trading in any segment. The impact is broad — covering Equity, Equity Derivatives, Currency Derivatives, and Commodities Derivatives segments. However, the technical effort required is minimal: only the certificate file needs to be replaced with no changes to application logic or connection parameters. BSE has provided advance notice and a phased approach (simulation first, production on 7th March) to minimise disruption.