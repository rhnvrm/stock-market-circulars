---
category: market-operations
circular_id: d323129df11e5246
date: '2025-11-14'
description: BSE introduces bidding mechanism for Zero Coupon Zero Principal (ZCZP)
  instruments on the Social Stock Exchange platform with specified file formats for
  SCSB participation.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={917CE6B8-82A5-4EA9-B8BE-C87854B2157A}&noticeno=20251114-45&dt=11/14/2025&icount=45&totcount=50&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Introduces new bidding mechanism for specialized SSE instruments affecting
  banks and investors participating in social enterprise fundraising
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251114-45&attachedId=df813df0-1b68-4e94-b2e0-ddbff74e4eb8
processing:
  attempts: 1
  content_hash: cce2a04c9da6b820
  processed_at: '2025-11-14T15:25:52.047210'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-11-14T13:41:19+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={917CE6B8-82A5-4EA9-B8BE-C87854B2157A}&noticeno=20251114-45&dt=11/14/2025&icount=45&totcount=50&flag=0
severity: medium
source: bse
stocks: []
tags:
- social-stock-exchange
- zczp
- bidding
- scsb
- file-format
- demat
- asba
title: Introduction of Bidding for Zero Coupon Zero Principal (ZCZP) Instrument for
  Social Stock Exchange (SSE)
---

## Summary

BSE has introduced a bidding mechanism for Zero Coupon Zero Principal (ZCZP) instruments on the Social Stock Exchange (SSE). The circular provides detailed file format specifications for Self-Certified Syndicate Banks (SCSB) to upload bid data and receive response files. Banks must mandatorily bid in ASBA mode with DEMAT type.

## Key Points

- Introduction of ZCZP instrument bidding on Social Stock Exchange platform
- Standardized upload file format for SCSB with 18 mandatory fields
- Response file format specification for bid confirmations
- Mandatory ASBA mode for banks with DEMAT only
- Support for both CDSL and NSDL depositories
- PAN and bank account details mandatory for all bids
- Action codes supported: N (new), M (modify), D (delete)
- Series value fixed at "0" for all bids
- Cut-off flag mandatory but set to "0" (zero)

## File Format Requirements

### Upload File Specifications

**Mandatory Fields:**
- Scrip ID (10 characters) - Symbol of the SSE entity
- Quantity (11 digits)
- Cut Off Flag (1 character) - Must be "0"
- Rate (6.2 numeric) - Face value
- Application Number (16 characters)
- PAN Number (10 characters)
- Category (5 characters) - SEBI client sub-category codes (11, 12, 21, 32, etc.)
- IFSC Code (11 characters)
- Type (Integer) - Must be "1" for DEMAT
- Series (Integer) - Must be "0"
- Action Code (1 character) - N/M/D

**Demat Details (Mandatory for DEMAT type):**
- Depository (4 characters) - CDSL or NSDL
- DP ID (16 characters) - "0" for CDSL, 8-digit for NSDL
- Client ID/Beneficiary ID (16 digits) - 16-digit for CDSL, 8-digit for NSDL

**Optional Fields:**
- Account Number (16 characters)
- Bank Reference Number (16 characters)

**Conditional Fields:**
- Cheque Received Flag (Y/N)
- Cheque Amount (12 digits) - Auto-generated if flag is "N", manual if "Y"
- Bid ID (16 digits) - System generated, "0" for new bids

### Response File Format

The response file mirrors the upload file structure, confirming bid acceptance with the same field specifications.

## Compliance Requirements

- SCSBs must use the prescribed file format for bid uploads
- All bids must be in DEMAT mode only (Type = 1)
- ASBA participation is mandatory for banks
- PAN verification required for all applications
- Depository details must match the specified format for CDSL/NSDL
- Series value must always be "0"
- Proper action codes must be used for bid modifications or deletions

## Important Dates

- Effective Date: November 14, 2025

## Impact Assessment

**Market Impact:** Medium - Creates new fundraising avenue for social enterprises through ZCZP instruments on SSE platform, expanding impact investing options.

**Operational Impact:** Medium - Requires SCSBs to implement new file format specifications and ensure system compatibility for ZCZP bid processing. Banks need to configure their systems to handle the 18-field upload format and process response files accordingly.

**Investor Impact:** Medium - Provides institutional and retail investors access to social impact investments through a structured bidding mechanism with DEMAT settlement, ensuring transparency and standardization in SSE fundraising.