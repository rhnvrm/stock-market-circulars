---
category: market-operations
circular_id: 9f6f421ba42ae94d
date: '2026-02-26'
description: BSE mandates trading members to replace the expiring TLS CA certificate
  by 7th March 2026 across all segments to maintain connectivity with exchange trading
  systems.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={C845A678-43CE-4C4F-88B9-FCB97B9657DB}&noticeno=20260226-1&dt=02/26/2026&icount=1&totcount=8&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Mandatory technical change with a hard deadline of 7th March 2026;
  failure to update the CA certificate will result in trading members being unable
  to connect to BSE trading systems across all segments, directly disrupting trading
  operations.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260226-1&attachedId=
processing:
  attempts: 1
  content_hash: 01f16a7576630fde
  processed_at: '2026-02-26T09:56:34.594289'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-02-26T03:17:12+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={C845A678-43CE-4C4F-88B9-FCB97B9657DB}&noticeno=20260226-1&dt=02/26/2026&icount=1&totcount=8&flag=0
severity: high
source: bse
stocks: []
tags:
- tls
- ca-certificate
- trading-connectivity
- infrastructure
- security
- technical
- trading-members
- all-segments
title: Renewal of CA Certificate for TLS Communication with BSE Exchange
---

## Summary

BSE has announced the renewal of the CA certificate used for TLS-encrypted communication between member applications and the exchange trading system. The existing certificate expires in March 2026 and must be replaced in all member applications before 7th March 2026. Post that date, only the new certificate will be accepted by the exchange across all segments.

## Key Points

- The current CA certificate for TLS communication with BSE is expiring in March 2026
- The new CA certificate becomes mandatory from **7th March 2026** across all segments
- Affected segments: Equity, Equity Derivatives, Currency Derivatives, and Commodities Derivatives
- No changes required to member application code — only the certificate file needs to be replaced
- No change in connection parameters for any segment
- New certificate is common across all segments
- New certificate is available at [www.bseindia.com/nta.aspx](https://www.bseindia.com/nta.aspx)
- A mock/test session will be scheduled on 7th March 2026 for connectivity testing
- The new certificate is applicable in the simulation/test market from **27th February 2026** onwards

## Regulatory Changes

This is a technical infrastructure change rather than a regulatory policy change. BSE is phasing in the certificate renewal to avoid last-minute disruptions, replacing the expiring TLS CA certificate with a new one in a controlled rollout across all trading segments simultaneously on 7th March 2026.

## Compliance Requirements

- Trading members must download the new CA certificate from [www.bseindia.com/nta.aspx](https://www.bseindia.com/nta.aspx)
- The old CA certificate must be replaced with the new certificate in member trading applications before 7th March 2026
- Members are advised to test connectivity using the simulation market environment available from 27th February 2026
- Members should participate in the mock session on 7th March 2026 to validate connectivity before live trading resumes on Monday
- For queries, members may contact their Relationship Manager or BSE Tech Support:
  - Phone: 022-22728053
  - Email: bse.tech@bseindia.com

## Important Dates

| Date | Event |
|------|-------|
| 27th February 2026 (Friday) | New certificate active in simulation/test market |
| 7th March 2026 (Saturday) | New certificate mandatory in production across all segments; mock session scheduled |
| March 2026 | Old certificate expiry deadline |

## Impact Assessment

**Operational Impact: High** — All trading members connected to BSE via TLS across Equity, Equity Derivatives, Currency Derivatives, and Commodities Derivatives segments must act before 7th March 2026. Failure to update the certificate will result in complete loss of connectivity to BSE trading systems, rendering trading operations non-functional.

**Effort Required: Low** — BSE has confirmed that no application code changes are needed. The change is limited to replacing the certificate file within the member's application configuration. The exchange has also provided ample lead time and a simulation environment for pre-production testing.

**Risk if Non-Compliant:** Trading members who do not replace the certificate before the deadline will be unable to connect to the BSE trading infrastructure from 7th March 2026 onwards, potentially causing significant trading disruptions.