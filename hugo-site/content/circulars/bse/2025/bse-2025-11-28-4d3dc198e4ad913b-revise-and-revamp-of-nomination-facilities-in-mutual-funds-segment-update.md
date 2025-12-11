---
category: compliance
circular_id: 4d3dc198e4ad913b
date: '2025-11-28'
description: BSE introduces new Nomination Opt-Out API for mutual funds, mandating
  OTP-based authentication or video recording for investors opting out of nomination
  facilities.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={47D07729-D891-47B9-AEF5-DE8637C5D25A}&noticeno=20251128-14&dt=11/28/2025&icount=14&totcount=39&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Mandatory SEBI-mandated regulatory change affecting all mutual fund
  investors and intermediaries using BSE StAR MF platform, requiring system integration
  and process changes
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251128-14&attachedId=09f45fd0-e662-4f0a-bb7d-27011f72f4d8
processing:
  attempts: 1
  content_hash: c4e160efa576b40d
  processed_at: '2025-11-28T12:53:39.671280'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-11-28T11:19:38+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={47D07729-D891-47B9-AEF5-DE8637C5D25A}&noticeno=20251128-14&dt=11/28/2025&icount=14&totcount=39&flag=0
severity: high
source: bse
stocks: []
tags:
- api
- authentication
- investor-protection
- mutual-fund
- nomination
- sebi
title: Revise and Revamp of Nomination Facilities in Mutual Funds Segment - Update
---

## Summary

BSE has introduced a new JSON-based Nomination Opt-Out API as part of revised nomination facilities in the mutual funds segment, implementing SEBI guidelines. The API enables members to register nomination opt-out details for investors choosing not to provide nominee information. This facility requires mandatory authentication through either OTP-based verification or video recording for individual investors creating new folios.

## Key Points

- New JSON-based API for nomination opt-out registration on BSE StAR MF platform
- Mandatory OTP-based authentication or video recording for investors opting out of nomination
- Applies to all individual tax status investors and new folios
- Available through Manual, Bulk Upload, and API channels
- API endpoint: https://bsestarmfdemo.bseindia.com/BSEMFWEBAPI/api/NomineeRegistration/V1
- Requires nomination authentication mode (O for OTP, V for Video Recording)
- Alphanumeric reference number mandatory for opt-out requests

## Regulatory Changes

**SEBI Guidelines Implementation:**
- Both nominee opt-in and opt-out details must be reported to RTAs/AMCs
- Opting out of nomination via OTP-based authentication or video recording is now mandatory
- New facility provided for existing client codes where nomination opt-out is 'N' to update required details

**Authentication Requirements:**
- NominationAuthMode must be specified:
  - 'O' - OTP with declaration
  - 'V' - Video Recording
- NomOptRefNo (alphanumeric reference number) mandatory for all opt-out cases

## Compliance Requirements

**For BSE StAR MF Members:**
- Integrate new Nomination Opt-Out API into existing systems
- Implement JSON-based request/response handling
- Ensure authentication mode capture (OTP or Video Recording)
- Maintain alphanumeric reference numbers for all opt-out transactions

**Mandatory API Parameters:**
- UserId (20 characters)
- MemberCode (20 characters)
- Password
- ClientCode (10 characters)
- NominationOpt (must be 'N' for opt-out)
- NominationAuthMode ('O' or 'V')
- NomOptRefNo (20 characters, alphanumeric)

**Response Codes:**
- 100 - Success
- 101 - Failure

## Important Dates

- Document Release: November 2025
- Effective Date: Not explicitly specified in circular

## Impact Assessment

**Operational Impact:**
- Members must develop/modify systems to integrate new API functionality
- Additional data capture requirements for nomination opt-out cases
- Enhanced compliance tracking and audit trail requirements

**Investor Impact:**
- Mandatory authentication for opting out of nomination increases security
- Additional steps required for investors choosing not to nominate
- Applies to all new folios with individual tax status

**Market Impact:**
- Strengthens investor protection framework in mutual fund segment
- Standardizes nomination opt-out process across BSE StAR MF platform
- May initially slow account opening process due to additional authentication steps

**Technology Requirements:**
- JSON API integration capability
- OTP generation and validation infrastructure
- Video recording capability for alternate authentication method
- Secure storage of authentication reference numbers