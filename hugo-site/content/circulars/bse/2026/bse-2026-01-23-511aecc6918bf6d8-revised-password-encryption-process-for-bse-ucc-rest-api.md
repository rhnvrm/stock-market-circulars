---
category: compliance
circular_id: 511aecc6918bf6d8
date: '2026-01-23'
description: BSE mandates updated two-step password encryption (MD5 then SHA512) for
  UCC REST API, effective after March 2026 UAT testing completion.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={57E31B44-781F-49ED-AA39-C6B90A8047F7}&noticeno=20260123-41&dt=01/23/2026&icount=41&totcount=53&flag=0
impact: medium
impact_ranking: medium
importance_ranking: high
justification: Mandatory security update affecting all UCC REST API users requiring
  system changes and UAT testing before production rollout
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260123-41&attachedId=
processing:
  attempts: 1
  content_hash: 613498faf4cb64a2
  processed_at: '2026-01-23T18:49:24.911660'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-23T13:49:19+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={57E31B44-781F-49ED-AA39-C6B90A8047F7}&noticeno=20260123-41&dt=01/23/2026&icount=41&totcount=53&flag=0
severity: high
source: bse
stocks: []
tags:
- ucc-api
- password-encryption
- security-enhancement
- api-authentication
- uat-testing
- technical-compliance
title: Revised Password Encryption Process for BSE UCC REST API
---

## Summary

BSE has announced a revised password encryption process for the UCC REST API as part of ongoing security enhancements. The new process requires a two-step encryption method: first applying MD5 encryption to the password, then encrypting the resulting MD5 hash using SHA512. The final SHA512-encrypted password must be passed in request headers when invoking the API. Members must test this updated process in the UAT environment before the mandatory production rollout scheduled after end of March 2026.

## Key Points

- Two-step password encryption process introduced: MD5 followed by SHA512
- Final SHA512-encrypted password must be included in API request headers
- Changes are mandatory for all UCC REST API users
- UAT testing required before production implementation
- Production rollout scheduled after end of March 2026
- UAT environment available at https://uat.bseindia.in/UCC_REST_API_SERVICE/UCCService.svc

## Regulatory Changes

BSE is implementing enhanced security measures for the UCC REST API authentication process. The previous password encryption method is being replaced with a mandatory two-step encryption process combining MD5 and SHA512 algorithms. This change applies to all trading members utilizing the UCC REST API services.

## Compliance Requirements

**For All UCC REST API Users:**
- Update password encryption implementation to use the two-step process (MD5 then SHA512)
- Modify API request headers to pass the SHA512-encrypted password
- Conduct testing in the UAT environment at the earliest
- Complete UAT testing before the production migration deadline
- Update internal systems and API integration code to comply with new encryption standards

**Contact Information for Queries:**
- Phone: 022-2272 8005, 022-2272 8215
- Email: user.trdops@bseindia.com

## Important Dates

- **January 23, 2026**: Circular issued, UAT testing environment available
- **End of March 2026**: Deadline for production environment migration (after successful UAT testing by existing users)
- **Immediate**: Members advised to begin UAT testing at the earliest

## Impact Assessment

**Technical Impact:** High - All members using UCC REST API services must modify their integration code to implement the new two-step encryption process. This requires development effort, testing, and deployment of updated systems.

**Operational Impact:** Medium - Members need to allocate resources for development, testing, and implementation. The UAT period provides time for thorough testing before production rollout, minimizing operational disruption.

**Security Impact:** Positive - The enhanced encryption process strengthens API security by implementing a more robust authentication mechanism, reducing vulnerability to unauthorized access.

**Timeline Consideration:** Members have approximately two months to complete UAT testing and prepare for production migration, providing reasonable time for implementation while maintaining security priorities.