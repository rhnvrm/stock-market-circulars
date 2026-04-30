---
category: compliance
circular_id: cd92a3d90fce0e5d
date: '2026-04-30'
description: NSE master circular consolidating guidelines for Unique Client Code (UCC)
  system including bulk upload file format specifications, segment-wise applicability,
  and compliance requirements for trading members.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/ISC73973.zip
impact: high
impact_ranking: high
importance_ranking: high
justification: Master circular affecting all trading members across all segments with
  mandatory UCC compliance requirements and specific file format specifications for
  client code uploads.
pdf_url: https://nsearchives.nseindia.com/content/circulars/ISC73973.zip
processing:
  attempts: 1
  content_hash: f72204c66f4352c7
  processed_at: '2026-04-30T14:17:36.155140'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-04-30T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/ISC73973.zip
severity: high
source: nse
stocks: []
tags:
- ucc
- unique-client-code
- trading-members
- compliance
- bulk-upload
- kyc
- client-registration
- equity
- derivatives
- commodity
- currency-derivatives
- slb
- debt-segment
title: Master Circular for Unique Client Code (UCC) - NSE
---

## Summary

NSE has issued a Master Circular for the Unique Client Code (UCC) system, consolidating all guidelines related to client identification and registration across market segments. The circular specifies the file format, structure, and field-level requirements for bulk uploading UCC data for all segments including Cash Market (CM), Futures & Options (FO), Currency Derivatives (CDS), Securities Lending & Borrowing (SLB), Debt, and Commodity segments.

## Key Points

- UCC bulk upload file must follow the naming convention: `UCI_YYYYMMDD.Tnn` (pipe-delimited format)
- File batch numbers run from 01 to 99; business date in filename must match the date field in the control record
- Account types are: `OWN` (proprietary trading by TM), `ERROR` (error account with member PAN), and `CLIENT` (all other entities)
- UPI opt-in field is applicable only for Individual and HUF categories (categories 1 & 3); values: Y (Registered), N (Not opted), NA (Not applicable), D (Deregistered)
- Segment codes: C (Cash Market), F (F&O), X (CDS), S (SLB), D (Debt), CO (Commodity)
- Where Account Type is `OWN`, PAN must belong to the trading member
- Where Account Type is `ERROR`, client code must be `ERROR` or `ERROR%` (where % is a number) and PAN must be of the member
- UPI facility is not applicable for PAN-exempt cases (value must be `NA`)
- For Individual/HUF clients with custodian details, UPI opt field shall be `NA`

## Regulatory Changes

- Consolidated master circular superseding previous individual circulars on UCC
- Updated file structure for bulk UCC uploads applicable across all trading segments
- Standardized account type classification (OWN/ERROR/CLIENT) for proprietary and client accounts
- UPI deregistration now supported via status `D` (can only transition from `Y`)

## Compliance Requirements

- All trading members must upload UCC data using the prescribed pipe-delimited file format (`UCI_YYYYMMDD.Tnn`)
- Control record must include: Record Type (10), Member Type (M), Member Code (5-char TM code), Date (DDMMYYYY), Batch Number, and Total Number of Detail Records
- Detail records must correctly classify each client under the appropriate Account Type (OWN/ERROR/CLIENT)
- UPI opt-in status must be accurately reported for all Individual and HUF clients in the Cash Market segment
- Segment field must use the correct code for each applicable segment per client
- Trading members must ensure PAN consistency with Account Type selection

## Important Dates

- Circular issued: 2026-04-30
- Effective immediately as a master circular consolidating existing UCC guidelines

## Impact Assessment

- **Trading Members**: Significant operational impact — all members must ensure their UCC bulk upload systems conform to the updated file format specifications across all six segments
- **Client Onboarding**: Standardized classification of OWN, ERROR, and CLIENT account types streamlines compliance checks and audit trails
- **UPI Integration**: Cash market participants with Individual/HUF clients must maintain accurate UPI registration status, including support for deregistration
- **Multi-segment Operations**: Members active across CM, FO, CDS, SLB, Debt, and Commodity segments must ensure segment-specific UCC submissions are correctly coded
- **System/IT Impact**: Back-office and upload systems may require updates to handle the prescribed file naming conventions, field lengths, and mandatory/optional field rules