---
category: compliance
circular_id: 22fb589cd0fd285c
date: '2025-11-28'
description: BSE introduces new API for nomination opt-out reporting in mutual funds,
  mandating OTP-based authentication or video recording for individual investors opting
  out of nomination facilities.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={47D07729-D891-47B9-AEF5-DE8637C5D25A}&noticeno=20251128-14&dt=11/28/2025&icount=14&totcount=58&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Affects mutual fund distributors and investors using BSE StAR MF platform.
  Introduces new API requirements for nomination opt-out compliance with SEBI guidelines,
  but is operational enhancement rather than urgent regulatory change.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251128-14&attachedId=09f45fd0-e662-4f0a-bb7d-27011f72f4d8
processing:
  attempts: 1
  content_hash: 9d5d0a3aa600a532
  processed_at: '2025-11-28T18:54:28.529633'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-11-28T11:19:38+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={47D07729-D891-47B9-AEF5-DE8637C5D25A}&noticeno=20251128-14&dt=11/28/2025&icount=14&totcount=58&flag=0
severity: medium
source: bse
stocks: []
tags:
- mutual-funds
- nomination
- api
- compliance
- sebi-guidelines
- bse-star-mf
- investor-protection
- kyc
title: Revise and Revamp of Nomination Facilities in Mutual Funds Segment - Update
---

## Summary

BSE has introduced a new Nomination Opt-Out API for the mutual funds segment on the BSE StAR MF platform. As per SEBI guidelines, both nominee opt-in and opt-out details must be reported to RTAs/AMCs. The API enables investors to opt out of nomination through OTP-based authentication or video recording, applicable across manual, bulk upload, and API channels.

## Key Points

- New JSON-based API for reporting nomination opt-out details to RTAs/AMCs
- Mandatory OTP-based authentication or video recording for opting out of nomination
- Applies to all Individual tax status and new folios
- Available for manual, bulk upload, and API modes
- Existing client codes with nomination opt-out status 'N' can use this API to provide required authentication details
- API endpoint: https://bsestarmfdemo.bseindia.com/BSEMFWEBAPI/api/NomineeRegistration/V1

## Regulatory Changes

SEBI guidelines now require both nominee opt-in and nominee opt-out details to be reported to RTAs/AMCs. Opting out of nomination via OTP-based authentication or video recording is mandatory for all individual tax status investors and new folios.

## Compliance Requirements

**For BSE StAR MF Platform Members:**
- Implement the Nomination Opt-Out API in their systems
- Ensure nomination opt-out value is set to 'N' when applicable
- Capture nomination authentication mode: 'O' for OTP with declaration or 'V' for Video Recording
- Provide alphanumeric nomination opt-out reference number (up to 20 characters)
- Update existing client codes where nomination opt-out is 'N' with required authentication details

**API Request Parameters (Mandatory):**
- UserId (20 characters)
- MemberCode (20 characters)
- Password
- ClientCode (10 characters)
- NominationOpt (must be 'N')
- NominationAuthMode ('O' or 'V')
- NomOptRefNo (alphanumeric, 20 characters)

**API Response Codes:**
- StatusCode 100: Success
- StatusCode 101: Failure

## Important Dates

Effective Date: November 2025 (document dated NOV 2025)

## Impact Assessment

**Operational Impact:**
- Mutual fund distributors and platforms using BSE StAR MF must integrate the new API
- Additional authentication step required for investors opting out of nomination
- Enhanced compliance tracking for RTAs and AMCs

**Investor Impact:**
- Individual investors opting out of nomination must complete OTP authentication or video recording
- Improved investor protection through stronger authentication mechanisms
- Existing folios with opt-out status need to be updated with authentication details

**Technology Impact:**
- System integration required for API implementation
- JSON-based format for seamless data exchange
- Demo environment available for testing at bsestarmfdemo.bseindia.com