---
category: compliance
circular_id: 7f18e390f37fe817
date: '2025-11-28'
description: BSE introduces Nomination Opt Out API for mutual funds, implementing
  SEBI guidelines requiring OTP-based authentication or video recording for nomination
  opt-out.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={47D07729-D891-47B9-AEF5-DE8637C5D25A}&noticeno=20251128-14&dt=11/28/2025&icount=14&totcount=56&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Mandatory compliance requirement for mutual fund intermediaries and
  RTAs to implement nomination opt-out authentication mechanisms as per SEBI guidelines,
  affecting operational processes.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251128-14&attachedId=09f45fd0-e662-4f0a-bb7d-27011f72f4d8
processing:
  attempts: 1
  content_hash: a12f450520293b6d
  processed_at: '2025-11-28T15:43:11.523060'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-11-28T11:19:38+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={47D07729-D891-47B9-AEF5-DE8637C5D25A}&noticeno=20251128-14&dt=11/28/2025&icount=14&totcount=56&flag=0
severity: medium
source: bse
stocks: []
tags:
- mutual-funds
- nomination
- api
- sebi-guidelines
- investor-protection
- bse-star-mf
- compliance
- rta
- amc
title: Revise and Revamp of Nomination Facilities in Mutual Funds Segment - Update
---

## Summary

BSE has introduced a new Nomination Opt Out API for the mutual funds segment on BSE StAR MF platform in compliance with SEBI guidelines. The API enables investors to opt out of nomination facility through OTP-based authentication or video recording. This JSON-based API is mandatory for all individual tax status and new folios, and provides a mechanism for existing client codes to update nomination opt-out details with proper authentication.

## Key Points

- New JSON-based Nomination Opt Out API introduced for BSE StAR MF platform
- Both nominee opt-in and opt-out details must be reported to RTAs/AMCs as per SEBI guidelines
- Two authentication modes available: OTP-based authentication (O) or Video Recording (V)
- Mandatory for all individual tax status and new folios
- Applicable across Manual, Bulk Upload, and API channels
- Existing client codes with nomination opt-out status 'N' can use this API to provide required authentication details
- API URL: https://bsestarmfdemo.bseindia.com/BSEMFWEBAPI/api/NomineeRegistration/V1

## Regulatory Changes

SEBI guidelines now require that both nominee opt-in and nominee opt-out details be reported to RTAs/AMCs. The regulations mandate proper authentication mechanisms for investors opting out of nomination facilities, enhancing investor protection and compliance standards in the mutual fund industry.

## Compliance Requirements

**For Members/Intermediaries:**
- Implement the Nomination Opt Out API in their systems
- Ensure OTP-based authentication or video recording facility is available for investors
- Mandatory implementation for all individual tax status and new folio creation
- Update existing client codes where nomination opt-out is 'N' with authentication mode and reference number

**API Request Parameters (Mandatory):**
- UserId (20 characters)
- MemberCode (20 characters)
- Password
- ClientCode (10 characters)
- NominationOpt (must be 'N' for opt-out)
- NominationAuthMode ('O' for OTP with declaration or 'V' for Video Recording)
- NomOptRefNo (20 characters, alphanumeric reference number)

**API Response Codes:**
- StatusCode 100: Success
- StatusCode 101: Failure

## Important Dates

Effective Date: November 2025 (as per document date)

## Impact Assessment

**Operational Impact:**
- Mutual fund distributors, brokers, and intermediaries need to integrate the new API into their systems
- RTAs and AMCs must be prepared to receive and process nomination opt-out data with authentication details
- Enhanced compliance burden with mandatory authentication requirements

**Investor Impact:**
- Improved investor protection through mandatory authentication for nomination opt-out
- Additional step required for investors choosing to opt out of nomination
- Choice between OTP-based authentication and video recording provides flexibility

**Market Impact:**
- Standardization of nomination opt-out process across BSE StAR MF platform
- Enhanced audit trail and compliance documentation
- Potential operational challenges during initial implementation phase for market participants