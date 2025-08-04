---
category: market-operations
circular_id: d14b1ae174d35de8
date: '2025-08-04'
description: BSE circular detailing the file format specification for reversal of
  excess shares under open offer through EPN return process.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={75716050-DDA2-465A-A49A-9F4A51545736}&noticeno=20250804-45&dt=08/04/2025&icount=45&totcount=55&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical specification for processing excess shares under open offers
  - important for market intermediaries handling takeover transactions
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20250804-45&attachedId=963f9275-dda3-4ba5-a442-de48f2ce09c2
processing:
  attempts: 1
  content_hash: 0ab28ab3801f3f1d
  processed_at: '2025-08-04T15:37:59.849965'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-08-04T13:30:10+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={75716050-DDA2-465A-A49A-9F4A51545736}&noticeno=20250804-45&dt=08/04/2025&icount=45&totcount=55&flag=0
severity: medium
source: bse
stocks: []
tags:
- open-offer
- epn-return
- file-format
- excess-shares
- reversal
- takeover
title: Reversal of Excess Shares Under Open Offer - EPN Return File Format
---

## Summary

BSE has issued the technical specification for the EPNReturnSSS_MMMM.csv file format used for reversal of excess shares under open offer. This file format is used by clearing members and depositories to process the return of excess shares that were tendered during open offer processes.

## Key Points

- File format: EPNReturnSSS_MMMM.csv with 10 defined fields
- Includes essential fields: CM Code, Scrip Code, ISIN, EPN Quantity, EPN Return Quantity
- Supports both EDIS and Non-EDIS processing flags
- DP ID Client ID field supports up to 16 characters for depository participant identification
- Remark field allows up to 500 characters for additional information

## Technical Specifications

### File Structure
- **CM Code**: 4-digit numeric field for clearing member identification
- **Scrip Code**: 6-digit numeric field for security identification
- **Scrip Name**: Variable length alphanumeric field
- **ISIN**: Variable length alphanumeric field for international security identification
- **EPN Qty**: 13-digit numeric field for original EPN quantity
- **EPN Return Qty**: 13-digit numeric field for quantity being returned
- **Remark**: 500-character alphanumeric field for processing notes
- **EDIS/Non-EDIS Flag**: 50-character field indicating processing method
- **DP ID Client ID**: 16-character field for depository participant and client identification
- **FILLER1**: Variable length filler field for future use

## Compliance Requirements

- Clearing members must use the specified file format for EPN return processing
- All mandatory fields must be populated with accurate data
- File naming convention must follow EPNReturnSSS_MMMM.csv pattern
- Both CDSL and NSDL depository formats are supported

## Impact Assessment

This specification ensures standardized processing of excess share reversals under open offers, facilitating smooth settlement of takeover transactions and maintaining market integrity during corporate action events.