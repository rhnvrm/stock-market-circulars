---
category: market-operations
circular_id: dd67dbb44cedeabd
date: '2026-02-26'
description: BSE mandates trading members to renew the CA certificate used for TLS-encrypted
  communication with exchange trading systems before March 7, 2026, failing which
  member applications will be unable to connect.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={C845A678-43CE-4C4F-88B9-FCB97B9657DB}&noticeno=20260226-1&dt=02/26/2026&icount=1&totcount=1&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Mandatory technical action required by all trading members across all
  segments by March 7, 2026. Non-compliance results in complete inability to connect
  to BSE trading systems, making this operationally critical.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260226-1&attachedId=
processing:
  attempts: 1
  content_hash: 00e7a1f26399443b
  processed_at: '2026-02-26T04:54:15.909667'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-02-26T03:17:12+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={C845A678-43CE-4C4F-88B9-FCB97B9657DB}&noticeno=20260226-1&dt=02/26/2026&icount=1&totcount=1&flag=0
severity: high
source: bse
stocks: []
tags:
- tls
- ca-certificate
- trading-connectivity
- infrastructure
- trading-members
- encryption
- market-operations
- mandatory-compliance
title: Renewal of CA Certificate for TLS Communication with BSE Exchange
---

## Summary

BSE is renewing its CA certificate used for TLS-encrypted communication with exchange trading systems. The existing certificate expires in March 2026. All trading members must replace the old CA certificate with the new one in their member applications before **March 7, 2026** to maintain uninterrupted connectivity with BSE trading systems across all segments.

## Key Points

- The existing BSE CA certificate for TLS communication is set to expire in March 2026
- New CA certificate is mandatory across all segments: Equity, Equity Derivatives, Currency Derivatives, and Commodities Derivatives
- Effective date for mandatory new certificate in production: **7th March 2026**
- New certificate available in simulation/test environment from **27th February 2026**
- A mock session is scheduled on **7th March 2026** for members to test connectivity
- No changes to connection parameters or member application code are required — only the certificate file needs to be replaced
- The new certificate is common for all segments and is available at [www.bseindia.com/nta.aspx](http://www.bseindia.com/nta.aspx)
- Member applications that do not update the certificate will **fail to connect** to BSE trading systems from March 7, 2026 onwards

## Regulatory Changes

No regulatory rule changes are involved. This is an infrastructure and security maintenance action — BSE is proactively renewing its TLS CA certificate ahead of its expiry to ensure continuity of encrypted trading channel communications.

## Compliance Requirements

- **Trading Members / Member Technology Teams** must:
  1. Download the new CA certificate from [www.bseindia.com/nta.aspx](http://www.bseindia.com/nta.aspx)
  2. Replace the old CA certificate with the new one in all member applications that connect to BSE trading systems
  3. Test connectivity using the simulation environment (available from 27th February 2026)
  4. Participate in the mock session on 7th March 2026 to validate production readiness
- No changes to application code or connection parameters are needed
- Contact BSE Tech Support for assistance: **022-22728053** | **bse.tech@bseindia.com**
- Contact respective Relationship Manager for queries

## Important Dates

| Date | Event |
|------|-------|
| 27th February 2026 | New CA certificate goes live in **simulation/test** environment |
| 7th March 2026 | New CA certificate becomes **mandatory in production** across all segments |
| 7th March 2026 | Mock session scheduled for members to test connectivity |
| March 2026 | Existing CA certificate **expires** |

## Impact Assessment

**Operational Impact: High** — Failure to replace the CA certificate before March 7, 2026 will result in a complete loss of connectivity to BSE trading systems for the affected member application. This would prevent trading across all segments (Equity, Equity Derivatives, Currency Derivatives, Commodities Derivatives).

**Implementation Effort: Low** — The certificate replacement is a straightforward file swap with no code changes or connection parameter updates required.

**Scope: All BSE Trading Members** — Every trading member using TLS-encrypted connections to BSE must take action. This is not segment-specific; the same certificate applies to all segments.

**Risk Mitigation:** BSE has provided early notice and a phased rollout with simulation environment access from February 27 and a mock session on March 7 to minimize disruption to live trading on Monday, March 9, 2026.