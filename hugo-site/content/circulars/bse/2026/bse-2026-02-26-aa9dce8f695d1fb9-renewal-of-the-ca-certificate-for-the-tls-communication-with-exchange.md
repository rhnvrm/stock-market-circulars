---
category: trading
circular_id: aa9dce8f695d1fb9
date: '2026-02-26'
description: BSE is renewing its CA certificate used for TLS-encrypted trading channel
  communication, mandatory for all segments from 7th March 2026.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={C845A678-43CE-4C4F-88B9-FCB97B9657DB}&noticeno=20260226-1&dt=02/26/2026&icount=1&totcount=2&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Mandatory technical change affecting all trading members across all
  segments; failure to update CA certificate before 7th March 2026 will result in
  complete loss of connectivity to BSE trading systems.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260226-1&attachedId=
processing:
  attempts: 1
  content_hash: d1229032ae1f3e1f
  processed_at: '2026-02-26T07:02:01.357662'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-02-26T03:17:12+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={C845A678-43CE-4C4F-88B9-FCB97B9657DB}&noticeno=20260226-1&dt=02/26/2026&icount=1&totcount=2&flag=0
severity: high
source: bse
stocks: []
tags:
- tls
- ca-certificate
- trading-connectivity
- technical
- infrastructure
- equity
- derivatives
- currency-derivatives
- commodities
title: BSE CA Certificate Renewal for TLS Communication - March 2026
---

## Summary

BSE is renewing its CA certificate used for TLS-encrypted communication over the trading channel. The existing certificate is set to expire in March 2026. All trading members must replace the old CA certificate with the new one in their member applications before 7th March 2026. Failure to do so will result in inability to connect to BSE trading systems.

## Key Points

- The CA certificate used for TLS communication with BSE trading systems will expire in March 2026
- The new CA certificate becomes mandatory across all segments from **7th March 2026**
- Affected segments: Equity, Equity Derivatives, Currency Derivatives, and Commodities Derivatives
- No changes required to member application code — only the certificate file needs to be replaced
- No changes to connection parameters for any segment
- New certificate (common for all segments) is available at: www.bseindia.com/nta.aspx
- The new certificate will be available in the test/simulation environment from **27th February 2026**
- A mock session is scheduled on 7th March 2026 to allow members to test connectivity before live trading resumes Monday

## Regulatory Changes

No regulatory rule changes are involved. This is a mandatory infrastructure/security upgrade driven by the expiry of the existing TLS CA certificate. BSE is phasing the rollout to minimize disruption.

## Compliance Requirements

- Trading members must download the new CA certificate from www.bseindia.com/nta.aspx
- Replace the old CA certificate with the new one in all member trading applications
- Complete the update before 7th March 2026 to avoid connectivity disruption
- Members are encouraged to test connectivity using the simulation environment from 27th February 2026
- For queries, contact the assigned Relationship Manager or BSE Tech Support:
  - Phone: 022-22728053
  - Email: bse.tech@bseindia.com

## Important Dates

- **27th February 2026**: New CA certificate becomes active in test/simulation market
- **7th March 2026**: New CA certificate becomes mandatory in production across all segments; mock session scheduled on this date
- **March 2026**: Existing CA certificate expires

## Impact Assessment

This change has a high operational impact on all BSE trading members. Any member application that is not updated with the new CA certificate before 7th March 2026 will be unable to connect to BSE trading systems, effectively disrupting trading activity. The change itself is technically straightforward — only a certificate file replacement is needed with no code changes or connection parameter updates. BSE has proactively scheduled a mock session and made the new certificate available in simulation early to facilitate smooth testing and transition.