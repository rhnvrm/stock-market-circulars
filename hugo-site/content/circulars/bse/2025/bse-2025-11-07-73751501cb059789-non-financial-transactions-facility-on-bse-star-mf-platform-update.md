---
category: market-operations
circular_id: 73751501cb059789
date: '2025-11-07'
description: BSE updates the data structure specifications for Non-Financial Transactions
  (NCT) facility on the StAR MF Platform, including detailed field requirements for
  nominee updation and other NCT types.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={63AA1340-213C-40E5-BCC6-C69589350593}&noticeno=20251107-27&dt=11/07/2025&icount=27&totcount=70&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical update for mutual fund platforms affecting operational procedures
  for NCT processing. Important for members using BSE StAR MF platform but does not
  impact trading or market operations directly.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251107-27&attachedId=ac3da0e9-8267-4c80-b072-3f677984f077
processing:
  attempts: 1
  content_hash: a4679c3f8089daa0
  processed_at: '2025-11-07T15:47:00.406010'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-11-07T12:18:28+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={63AA1340-213C-40E5-BCC6-C69589350593}&noticeno=20251107-27&dt=11/07/2025&icount=27&totcount=70&flag=0
severity: low
source: bse
stocks: []
tags:
- 2fa
- digital-transactions
- esign
- mutual-fund
- nominee-updation
- non-financial-transactions
- technical-specification
- trading-platform
title: Non-Financial Transactions Facility on BSE StAR MF Platform - Update
---

## Summary

BSE has issued an updated specification for the Non-Financial Transactions (NCT) facility on the BSE StAR MF Platform. The circular provides detailed technical specifications for the NOM_STRUCTURE data format, which includes 34+ fields covering member information, client details, transaction types, digital authentication modes, and nominee information. The update primarily focuses on nominee updation processes and supports multiple authentication methods including wet signature, eSign, and 2FA (Two-Factor Authentication).

## Key Points

- Data structure includes mandatory fields for Member Code, UCC (Client Code), NCT Type, AMC Code, and Folio Number
- NCT Types supported: For Kfin - "NCTCF01" (Opting out of Nomination) and "NCTCF02" (Update/Change of Nominee Details); For CAMS - "NOM"
- Three document authentication types supported: W (Wet Signature), E (eSign), O (2FA)
- 2FA authentication modes available: M (Mobile), E (Email), B (Both)
- Conditional mandatory fields based on mode of holding (MOH) and presence of joint holders
- Supports up to 3 nominees with details including name, relation, percentage, PAN, minor flag, and DOB
- Declaration flags required when contact details match between holders (SE-Self, SP-Spouse, DC-Dependent Children, DS-Dependent Siblings, DP-Dependent Parents)
- Broker Code mandatory for ARN Holders, RIA Code mandatory for RIAs
- EUIN and Sub Broker Code are optional fields

## Regulatory Changes

No new regulatory changes introduced. This is a technical specification update for existing NCT facility operations on the BSE StAR MF Platform.

## Compliance Requirements

- Members must ensure data submissions follow the updated NOM_STRUCTURE format with 34+ fields
- Mandatory fields must be populated: Member Code, UCC, NCT_TYPE, AMC_CODE, FOLIO_NO, TAX_NUMBER (Primary PAN), and DOC_TYPE
- For 2FA transactions, appropriate email and/or mobile numbers must be provided based on authentication mode selected
- When multiple holders exist with same contact details, appropriate declaration flags (PH_EMA_DEC, PH_MOB_DEC, J1_EMA_DEC, etc.) must be provided
- For nominee updation, if opting out is "N", nominee details (name, relation, percentage) become mandatory
- ARN Holders must provide Broker Code; RIAs must provide RIA Code
- For minors as nominees, DOB is mandatory
- Character length and data type restrictions must be adhered to as specified

## Important Dates

Circular issued: November 7, 2025
No specific implementation deadline mentioned - appears to be effective immediately as an operational update.

## Impact Assessment

**Operational Impact:** Medium - Members using BSE StAR MF Platform will need to ensure their systems are configured to submit NCT data in the updated format with all mandatory and conditional mandatory fields properly populated.

**Technology Impact:** Medium - May require system updates for members to accommodate new field requirements, validation rules, and conditional logic based on authentication modes and holder configurations.

**Business Impact:** Low to Medium - Primarily affects operational processes for mutual fund distributors, RIAs, and ARN holders processing non-financial transactions through BSE platform. Does not impact trading or pricing.

**Market Impact:** Low - Technical/operational update with no direct market implications. Enhances digital transaction capabilities and nominee management processes for mutual fund investments.