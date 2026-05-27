---
category: compliance
circular_id: 842a3675b73569e6
date: '2026-05-27'
description: BSE announces updates to FATCA/UBO file structure on the StAR MF platform,
  including 17 new fields, revised validations, and mandatory TIN NA Declaration Form
  requirements, with go-live scheduled for August 31, 2026.
draft: false
guid: https://www.bseindia.com/downloads/UploadDocs/Notices/20260527-40/20260527-40.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical compliance change affecting all BSE StAR MF platform members
  and third-party vendors; requires system development and integration work by August
  31, 2026, but does not directly impact market trading or pricing.
pdf_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260527-40/20260527-40.pdf
processing:
  attempts: 1
  content_hash: 1affb8cedcb2e4a9
  processed_at: '2026-05-27T15:55:00.549994'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-27T14:18:09+00:00'
rss_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260527-40/20260527-40.pdf
severity: medium
source: bse
stocks: []
tags:
- mutual-fund
- star-mf
- fatca
- mf-platform
- mf-operations
- compliance
- kyc
- rta
- bse
title: Revision to FATCA/UBO File Structure and Validations on BSE StAR MF Platform
---

## Summary

BSE has revised the FATCA/UBO (Foreign Account Tax Compliance Act / Ultimate Beneficial Owner) file structure on the BSE StAR MF platform. The update introduces 17 additional fields, new validation rules for select existing fields, and a mandatory TIN NA Declaration Form requirement. All changes apply across the UI, bulk file upload utility, and APIs on the platform, with a go-live date of August 31, 2026.

## Key Points

- The FATCA/UBO file structure is being expanded with 17 new fields as detailed in Annexure I.
- New validation rules have been added for fields: PO_BIR_INC (Field 10), CO_BIR_INC (Field 11), UBO_PAN (Field 46), LOG_NAME (Field 73), and NPO_RGNO (Field 83).
- The "TIN NA Declaration Form" becomes mandatory when "NA" is selected under ID1_TYPE, ID2_TYPE, ID3_TYPE, or ID4_TYPE.
- Changes apply to the UI, bulk file upload utility, and all APIs on BSE StAR MF platform.
- This notice follows reference circular no. 20260212-29 dated February 12, 2026.

## Regulatory Changes

The Registrar and Transfer Agents (RTAs) are driving the revision to the FATCA/UBO file structure. BSE is aligning the StAR MF platform with these revised requirements across three areas:

1. **Additional Fields**: 17 new fields added to the FATCA/UBO file structure (see Annexure I for details).
2. **Validation Enhancements**: Additional validation rules introduced for five existing fields — PO_BIR_INC, CO_BIR_INC, UBO_PAN, LOG_NAME, and NPO_RGNO.
3. **Mandatory TIN NA Declaration**: Submission of the "TIN NA Declaration Form" is now mandatory whenever "NA" is selected as the ID type under any of ID1_TYPE, ID2_TYPE, ID3_TYPE, or ID4_TYPE.

## Compliance Requirements

- All members using BSE StAR MF platform must update their systems, processes, and interfaces to align with the revised FATCA/UBO file structure.
- Members using third-party vendor solutions or in-house developed trading applications must complete development, integration, and testing activities within the prescribed timelines.
- Ensure the TIN NA Declaration Form workflow is implemented for applicable ID type selections.
- Review Annexure I for the complete list of new fields and validation rules.

## Important Dates

- **Go-Live Date**: August 31, 2026 — implementation of all changes on BSE StAR MF platform.
- **UAT Deployment Date**: To be communicated separately by BSE.
- **Reference Circular**: 20260212-29 dated February 12, 2026 (earlier notice on the same subject).

## Impact Assessment

This circular primarily affects mutual fund intermediaries, distributors, and technology vendors integrated with the BSE StAR MF platform for FATCA/UBO reporting. All three access channels — UI, bulk upload, and API — are impacted, requiring coordinated technical updates across affected entities. Members relying on third-party systems should coordinate with vendors early to ensure readiness before the August 31, 2026 deadline. There is no direct impact on fund NAVs, investor portfolios, or market trading operations. For queries, members can contact the BSE Mutual Fund Helpdesk at 022-45720450/650 & 022-69158550 (business days, 8:00am–7:00pm) or raise tickets on the CRS portal.