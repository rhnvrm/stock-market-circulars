---
category: compliance
circular_id: da7a1e80b5609f0e
date: '2026-05-26'
description: NSE has revised the FATCA/UBO data upload structure on the NSE MF Invest
  Platform, specifying updated field names, types, sizes, and mandatory/optional status
  for investor and guardian information.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/NMF74386.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational compliance change affecting all intermediaries and RTAs
  using the NSE MF Invest Platform for FATCA/UBO uploads; requires system-level updates
  but does not alter market trading or securities directly.
pdf_url: https://nsearchives.nseindia.com/content/circulars/NMF74386.zip
processing:
  attempts: 1
  content_hash: 5d03392665ff1ad0
  processed_at: '2026-05-26T10:04:38.217718'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-26T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/NMF74386.zip
severity: medium
source: nse
stocks: []
tags:
- fatca
- ubo
- mutual-fund
- nse-mf
- kyc
- compliance
- mf-platform
- mf-operations
title: Notice of Revisions to FATCA/UBO Upload Structure on NSE MF Invest Platform
---

## Summary

NSE has issued a notice detailing revisions to the FATCA (Foreign Account Tax Compliance Act) and UBO (Ultimate Beneficial Owner) data upload structure on the NSE MF Invest Platform. The circular provides an updated field specification (Annexure 1) governing the format, data types, field sizes, and mandatory/optional classification for investor and guardian information submitted through the platform.

## Key Points

- The upload structure includes 25+ defined fields covering investor identification, tax residency, and compliance data.
- PAN (`PAN_RP`) is mandatory; where PAN is absent, the PAN Exempt KYC Reference Number (`PEKRN`) must be provided.
- Investor name (`INV_NAME`) and tax status (`TAX_STATUS`) are mandatory fields.
- Data source indicator (`DATA_SRC`) must specify whether data was collected electronically ('E') or physically ('P').
- Up to four tax residency countries (`TAX_RES1` through `TAX_RES4`) can be captured, each with a corresponding Tax Payer Identification Number (`TPIN`) and identification document type (`ID_TYPE`).
- Country codes must conform to ISO-3166 standards.
- Place of birth/incorporation (`PO_BIR_INC`) must not be the same as the country of birth field.
- Wealth source code (`SRCE_WEALT`) is mandatory; specific codes include Foreign Exchange/Money Changer Services (01) and Gaming/Gambling/Lottery Services (02).
- `CORP_SERVS` field is mandatory for non-individual investors.

## Regulatory Changes

The revised upload structure replaces or updates the prior FATCA/UBO file format used on the NSE MF Invest Platform. Fields have been reorganized with explicit mandatory/optional designations, standardized field sizes, and updated remarks to reduce ambiguity in data submission.

## Compliance Requirements

- All mutual fund distributors, RTAs, AMCs, and other intermediaries using the NSE MF Invest Platform for FATCA/UBO data submission must update their upload files to conform to the revised field structure.
- Mandatory fields (PAN or PEKRN, investor name, tax status, data source, address type, place and country of birth/incorporation, primary tax residency, TPIN, and identification type) must be populated for every record.
- Entities must ensure country codes follow ISO-3166 standards.
- Non-individual investors must populate the `CORP_SERVS` field.

## Important Dates

- Circular date: 2026-05-26. Specific effective date for the revised upload structure was not explicitly stated in the available content; intermediaries should refer to the full circular for implementation timelines.

## Impact Assessment

This circular has a moderate operational impact on all participants submitting FATCA/UBO data via the NSE MF Invest Platform, including RTAs, AMCs, and distributors. System and file-generation workflows will need to be updated to match the revised field specifications. No direct market trading or securities pricing impact is anticipated. Non-compliance with the updated structure may result in rejected uploads or regulatory scrutiny under FATCA and AML/UBO reporting obligations.