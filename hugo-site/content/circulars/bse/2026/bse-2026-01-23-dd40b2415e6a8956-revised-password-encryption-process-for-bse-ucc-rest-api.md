---
category: compliance
circular_id: dd40b2415e6a8956
date: '2026-01-23'
description: BSE announces mandatory update to password encryption process for UCC
  REST API, requiring MD5 followed by SHA512 encryption, to be implemented in production
  by end of March 2026.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={57E31B44-781F-49ED-AA39-C6B90A8047F7}&noticeno=20260123-41&dt=01/23/2026&icount=41&totcount=52&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Mandatory technical security change affecting all members using UCC
  REST API services with strict implementation deadline by end of March 2026
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260123-41&attachedId=
processing:
  attempts: 1
  content_hash: b44e0028d045ee99
  processed_at: '2026-01-23T15:37:54.736471'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-23T13:49:19+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={57E31B44-781F-49ED-AA39-C6B90A8047F7}&noticeno=20260123-41&dt=01/23/2026&icount=41&totcount=52&flag=0
severity: high
source: bse
stocks: []
tags:
- api
- security
- ucc
- rest-api
- encryption
- technical
- trading-operations
- password-security
title: Revised Password Encryption Process for BSE UCC REST API
---

## Summary

BSE has mandated an updated password encryption process for the UCC REST API as part of ongoing security enhancements. Members must implement a two-stage encryption process: first encrypting passwords using MD5, then encrypting the resulting hash using SHA512. The final SHA512-encrypted password must be passed in request headers when invoking the API. All members are required to begin UAT testing immediately, with mandatory production implementation by end of March 2026.

## Key Points

- Password encryption process updated for BSE UCC REST API
- Two-stage encryption required: MD5 first, then SHA512
- Final SHA512-encrypted password must be passed in API request headers
- Changes are mandatory for all UCC REST API users
- UAT testing available at https://uat.bseindia.in/UCC_REST_API_SERVICE/UCCService.svc
- Members must begin UAT testing at the earliest

## Regulatory Changes

BSE has introduced enhanced security requirements for UCC REST API authentication:

1. **New Encryption Process**: Members must implement dual-layer encryption
2. **Step 1**: Encrypt password using MD5 algorithm
3. **Step 2**: Encrypt the resulting MD5 hash using SHA512 algorithm
4. **Implementation**: Pass the final SHA512-encrypted password in request headers while invoking the API

## Compliance Requirements

**Mandatory Actions for Trading Members:**

- Implement the revised two-stage password encryption process (MD5 followed by SHA512)
- Begin testing the updated process in UAT environment immediately
- Update API integration code to comply with new encryption requirements
- Successfully complete UAT testing before production cutover
- Ensure production systems are updated before end of March 2026

**Testing Environment:**
- UAT URL: https://uat.bseindia.in/UCC_REST_API_SERVICE/UCCService.svc

**Support Contact:**
- Phone: 022-2272 8005 / 022-2272 8215
- Email: user.trdops@bseindia.com

## Important Dates

- **January 23, 2026**: Circular issued, UAT testing available
- **End of March 2026**: Mandatory production implementation deadline after successful UAT testing by existing UCC API users

## Impact Assessment

**Technical Impact:**
- High impact on all trading members currently using BSE UCC REST API
- Requires code changes to API authentication logic
- Mandatory testing period required before production deployment
- Potential service disruption if not implemented by deadline

**Operational Impact:**
- Members must allocate development and testing resources
- Coordination required between trading operations and IT teams
- No backward compatibility - all members must upgrade
- Failure to implement may result in API access denial after March 2026

**Security Enhancement:**
- Strengthened password security through dual-layer encryption
- Improved protection against unauthorized API access
- Aligns with modern security best practices