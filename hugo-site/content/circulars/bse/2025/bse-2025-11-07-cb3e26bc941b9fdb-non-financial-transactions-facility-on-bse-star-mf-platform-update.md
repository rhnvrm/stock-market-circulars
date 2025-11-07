---
category: market-operations
circular_id: cb3e26bc941b9fdb
date: '2025-11-07'
description: Updates to the NOM_STRUCTURE file format for Non-Financial Transactions
  on BSE StAR MF Platform, including field specifications for nominee updation and
  related processes.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={63AA1340-213C-40E5-BCC6-C69589350593}&noticeno=20251107-27&dt=11/07/2025&icount=27&totcount=30&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical update affecting mutual fund distributors and members using
  BSE StAR MF platform for non-financial transactions. Requires system updates to
  comply with revised file structure.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251107-27&attachedId=ac3da0e9-8267-4c80-b072-3f677984f077
processing:
  attempts: 1
  content_hash: 3c25b529dca96f00
  processed_at: '2025-11-07T12:43:20.235685'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-11-07T12:18:28+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={63AA1340-213C-40E5-BCC6-C69589350593}&noticeno=20251107-27&dt=11/07/2025&icount=27&totcount=30&flag=0
severity: medium
source: bse
stocks: []
tags:
- mutual-funds
- bse-star-mf
- non-financial-transactions
- nominee-updation
- technical-update
- file-format
title: Non-Financial Transactions Facility on BSE StAR MF Platform - Update
---

## Summary

BSE has issued an update to the Non-Financial Transactions (NCT) facility on the BSE StAR MF Platform, specifying the revised NOM_STRUCTURE file format. The circular details 34 fields required for processing non-financial transactions, particularly nominee updation requests, including mandatory and conditional mandatory fields for different transaction scenarios.

## Key Points

- Updated NOM_STRUCTURE file format with 34 fields for non-financial transactions
- Supports multiple NCT types including nominee updation for different RTAs (Kfin and CAMS)
- Three document type options: Wet Signature (W), eSign (E), and 2FA (O)
- Separate field requirements for 2FA authentication modes (Mobile, Email, or Both)
- Mandatory fields for ARN holders and RIAs with specific broker and RIA code requirements
- Conditional mandatory fields based on mode of holding (single/joint holders)
- Support for up to 3 nominees with detailed information requirements
- Declaration flags required for matching contact details across holders
- Specific validation rules for PAN, Aadhaar, Driving License, and Passport for nominee identification

## Regulatory Changes

The circular introduces refined field specifications for the NOM_STRUCTURE format:

- NCT_TYPE field now distinguishes between Kfin types (NCTCF01 for opting out, NCTCF02 for update/change) and CAMS (NOM)
- Enhanced 2FA authentication requirements with separate email and mobile fields for primary and joint holders
- New declaration fields (PH_EMA_DEC, PH_MOB_DEC, J1_EMA_DEC, J1_MOB_DEC, J2_EMA_DEC, J2_MOB_DEC) for matching contact details
- Declaration values limited to: SE (Self), SP (Spouse), DC (Dependent Children), DS (Dependent Siblings), DP (Dependent Parents)

## Compliance Requirements

**For BSE Members and Mutual Fund Distributors:**

- Update systems to comply with the revised 34-field NOM_STRUCTURE format
- Ensure proper validation of mandatory fields based on transaction type
- Implement conditional validation logic for 2FA transactions based on mode of holding
- ARN holders must provide Broker Code (Field 24)
- RIAs must provide RIA Code (Field 27)
- Validate nominee details including PAN/Aadhaar/other ID types based on selection
- Ensure declaration flags are provided when contact details match across holders

**Field-Specific Requirements:**

- DOC_TYPE must be W, E, or O
- TWOFA_AUTH must be M, E, or B (mandatory for 2FA transactions)
- Email and mobile fields conditionally mandatory based on 2FA mode selection
- Nominee percentage must be whole numbers (no decimals)
- Nominee identification based on type: PAN (10 alphanumeric), Aadhaar (last 4 digits), DL (max 20), Passport (max 9)

## Important Dates

- Circular Date: November 7, 2025
- Implementation timeline not specified in the provided content

## Impact Assessment

**Operational Impact:**

Medium impact on BSE StAR MF platform users. Members and distributors processing non-financial transactions must update their systems to accommodate the revised file structure with additional fields and validation rules.

**Market Participants Affected:**

- Mutual fund distributors using BSE StAR MF platform
- BSE trading members facilitating mutual fund transactions
- ARN holders and RIAs
- RTAs (Kfin and CAMS) processing nominee updation requests

**Technical Requirements:**

System modifications needed to handle:
- Extended field set (34 fields)
- Conditional mandatory field logic
- Enhanced validation for 2FA authentication modes
- Declaration flag processing for duplicate contact details
- Multiple nominee information capture and validation