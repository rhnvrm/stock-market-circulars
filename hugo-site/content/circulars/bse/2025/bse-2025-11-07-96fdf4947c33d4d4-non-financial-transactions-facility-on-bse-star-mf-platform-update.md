---
category: market-operations
circular_id: 96fdf4947c33d4d4
date: '2025-11-07'
description: Update on the Non-Financial Transactions (NFT) facility on BSE StAR MF
  Platform, detailing the NOM_STRUCTURE field specifications for nominee updation
  and related processes.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={63AA1340-213C-40E5-BCC6-C69589350593}&noticeno=20251107-27&dt=11/07/2025&icount=27&totcount=76&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical update affecting mutual fund intermediaries and members using
  BSE StAR MF platform for non-financial transactions, particularly nominee updation
  processes. Important for operational compliance but not market-moving.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251107-27&attachedId=ac3da0e9-8267-4c80-b072-3f677984f077
processing:
  attempts: 1
  content_hash: 9599ab8f547db295
  processed_at: '2025-11-07T18:53:49.419273'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-11-07T12:18:28+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={63AA1340-213C-40E5-BCC6-C69589350593}&noticeno=20251107-27&dt=11/07/2025&icount=27&totcount=76&flag=0
severity: medium
source: bse
stocks: []
tags:
- mutual-funds
- non-financial-transactions
- nominee-updation
- bse-star-mf
- technical-specifications
- file-structure
title: Non-Financial Transactions Facility on BSE StAR MF Platform - Update
---

## Summary

BSE has issued an update regarding the Non-Financial Transactions (NFT) facility on the BSE StAR MF Platform. The circular provides detailed technical specifications for the NOM_STRUCTURE file format, which is used for processing nominee-related transactions including nominee updation, opting out of nomination, and updating/changing nominee details across different RTAs (Kfin and CAMS).

## Key Points

- The NOM_STRUCTURE contains 34 fields with specific mandatory/optional requirements
- Supports three document types: Wet Signature (W), eSign (E), and 2FA (O)
- Two-Factor Authentication (2FA) can be conducted via Mobile (M), Email (E), or Both (B)
- Different NCT types for Kfin (NCTCF01 for opting out, NCTCF02 for updates) and CAMS (NOM)
- Detailed specifications for nominee information including name, relation, percentage allocation, PAN, and minor flag
- Conditional mandatory fields based on document type, mode of holding, and 2FA authentication mode
- Includes provisions for joint holders (J1, J2) with separate contact detail requirements
- Declaration flags required when contact details match between holders
- Broker code mandatory for ARN holders, RIA code mandatory for RIAs

## Technical Specifications

### Core Fields (1-7)
- Member Code and UCC (Client Code) are mandatory
- NCT_TYPE specifies transaction type with different codes for Kfin and CAMS
- AMC_CODE, FOLIO_NO, and Primary PAN are mandatory
- DOC_TYPE indicates signature/authentication method

### 2FA Requirements (Field 8-17)
- 2FA authentication mode mandatory for digital NCTs in 2FA mode
- Email and mobile number requirements vary based on 2FA mode selection
- Conditional requirements for joint holders based on mode of holding

### Contact Detail Declarations (Field 18-23)
- Declaration flags mandatory if contact details match between holders
- Five possible values: SE (Self), SP (Spouse), DC (Dependent Children), DS (Dependent Siblings), DP (Dependent Parents)

### Intermediary Codes (Field 24-27)
- Broker Code mandatory for ARN holders
- EUIN optional
- Sub Broker Code optional
- RIA Code mandatory for RIAs

### Nominee Details (Field 28-34)
- Nomination opt-out flag (Y/N)
- Nominee name, relation, and percentage allocation
- PAN mandatory for new folio creation with specific ID type conditions
- Support for different ID types: PAN (10 digits), Aadhaar (last 4 digits), Driving License (max 20 digits), Passport (max 9 characters)
- Minor flag and date of birth for minor nominees

## Compliance Requirements

- Members must ensure all mandatory fields are populated based on transaction type
- For 2FA transactions, appropriate email/mobile details must be provided based on authentication mode
- Declaration flags must be accurately filled when contact details are shared between holders
- ARN holders must include broker code; RIAs must include RIA code
- For nominee updation, complete nominee details including relation and percentage must be provided
- PAN/ID proof requirements must be met for new folio creation

## Important Dates

No specific implementation or effective dates mentioned in the circular.

## Impact Assessment

### Operational Impact
- Members and intermediaries using BSE StAR MF platform must ensure their systems comply with the updated field structure
- Enhanced data capture requirements for 2FA transactions may require system modifications
- Improved nominee management capabilities with detailed specification of fields

### Market Participants Affected
- BSE StAR MF Platform members
- ARN holders and RIAs
- RTAs (Kfin and CAMS)
- Mutual fund investors conducting non-financial transactions

### Process Enhancement
- Standardized structure for nominee-related transactions across different RTAs
- Clear conditional logic for mandatory fields reduces processing errors
- Support for multiple authentication modes provides flexibility for digital transactions