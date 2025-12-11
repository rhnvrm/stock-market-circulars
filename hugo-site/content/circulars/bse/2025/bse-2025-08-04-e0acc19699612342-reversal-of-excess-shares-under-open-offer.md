---
category: market-operations
circular_id: e0acc19699612342
date: '2025-08-04'
description: BSE provides technical specification for EPNReturnSSS_MMMM.csv file format
  used for reversal of excess shares under open offers.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={75716050-DDA2-465A-A49A-9F4A51545736}&noticeno=20250804-45&dt=08/04/2025&icount=45&totcount=60&flag=0
impact: low
impact_ranking: low
importance_ranking: low
justification: Technical file format specification for operational process
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20250804-45&attachedId=963f9275-dda3-4ba5-a442-de48f2ce09c2
processing:
  attempts: 1
  content_hash: 8fcfad5d20a20f54
  processed_at: '2025-08-04T18:38:01.578561'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-08-04T13:30:10+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={75716050-DDA2-465A-A49A-9F4A51545736}&noticeno=20250804-45&dt=08/04/2025&icount=45&totcount=60&flag=0
severity: low
source: bse
stocks: []
tags:
- csv-format
- excess-shares
- file-format
- reversal
- takeover
- technical-specification
title: Reversal of Excess Shares Under Open Offer - CSV File Format Specification
---

## Summary

BSE has provided the technical specification for the EPNReturnSSS_MMMM.csv file format used for processing reversal of excess shares under open offers. The specification defines 10 fields including CM code, scrip details, quantities, and client information.

## Key Points

- CSV file format specification for excess share reversal process
- Contains 10 mandatory fields with specific data types and lengths
- Includes scrip identification, quantity details, and client information
- Supports both EDIS and Non-EDIS processing flags
- Field lengths range from 4 characters to undefined for certain fields

## File Format Details

**Required Fields:**
- CMCode (4 digits): CM code
- ScripCode (6 digits): Security identifier
- ScripName: Security name
- ISIN: International Securities Identification Number
- EPN Qty (13 digits): Original EPN quantity
- EPN Return Qty (13 digits): Quantity to be returned
- Remark (500 chars): Processing remarks
- EDIS/Non-EDIS Flag (50 chars): Processing type indicator
- DP ID Client ID (16 chars): Depository participant and client details
- FILLER1: Additional field for internal use

## Compliance Requirements

- Market participants must use the specified CSV format for excess share reversal submissions
- All mandatory fields must be populated with correct data types and lengths
- ISIN codes must be valid and match the scrip being processed

## Impact Assessment

This is a technical specification document that standardizes the file format for operational processes. It ensures consistent data submission for excess share reversal under open offers, facilitating automated processing and reducing errors.