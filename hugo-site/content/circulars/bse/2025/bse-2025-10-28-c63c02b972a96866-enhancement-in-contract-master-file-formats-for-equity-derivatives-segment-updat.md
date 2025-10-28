---
category: trading
circular_id: c63c02b972a96866
date: '2025-10-28'
description: BSE announces updated specifications for Contract Master file formats
  in the Equity Derivatives segment, including new field definitions and data structures
  for futures and options contracts.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={515BFEE3-9CC9-4E62-984C-76F19BAA3996}&noticeno=20251028-48&dt=10/28/2025&icount=48&totcount=52&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical update affecting all equity derivatives trading members and
  systems integrating with BSE's Contract Master files. Important for operational
  compliance but routine system update.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251028-48&attachedId=2e874865-314d-4ae0-bbc5-c1c8ea4f5014
processing:
  attempts: 1
  content_hash: 9b5c1750acc7b25b
  processed_at: '2025-10-28T15:32:45.410452'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-28T14:26:26+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={515BFEE3-9CC9-4E62-984C-76F19BAA3996}&noticeno=20251028-48&dt=10/28/2025&icount=48&totcount=52&flag=0
severity: medium
source: bse
stocks: []
tags:
- derivatives
- equity-derivatives
- contract-master
- file-format
- technical-specification
- futures
- options
- trading-system
- ETI
title: Enhancement in Contract Master File Formats for Equity Derivatives Segment
  - Update
---

## Summary

BSE has issued an update to the Contract Master file formats for the Equity Derivatives Segment. The circular provides detailed specifications for three file types: EQD_CODDMMYY.csv, EQD_CO_abr_DDMMYY.csv, and EQD_INDEX_CODDMMYY.csv. These files contain comprehensive contract information including token numbers, instrument types, strike prices, expiry dates, and trading parameters required for equity derivatives trading on BSE's platform.

## Key Points

- Three CSV file formats specified for Contract Master data: regular equity derivatives, abbreviated format, and index derivatives
- Contract Master files include 58+ fields covering contract identification, underlying asset details, trading parameters, and settlement information
- Support for Index Futures (IF), Index Options (IO), Stock Futures (SF), and Stock Options (SO)
- Integration with ETI (Enhanced Trading Interface) API with specific field mappings
- Reserved Identifier field added to distinguish between active (0) and reserved (1) contracts
- Pre-Open session indicator included to identify contracts in pre-open phase
- Strike prices displayed in paise for precision
- Date format standardized as DD-MMM-YYYY
- Series codes distinguish between monthly futures, weekly futures, and options with strike prices
- Capacity Group ID and Partition ID fields included for trading system architecture

## Regulatory Changes

This is a technical specification update rather than a regulatory change. It standardizes the data structure and field definitions for Contract Master files used in equity derivatives trading. The update enhances the existing file format with additional fields for better contract identification and trading system integration.

## Compliance Requirements

- Trading members and system integrators must update their systems to parse the updated Contract Master file format
- Systems must handle all specified field types and data formats correctly
- Integration with ETI API requires mapping to specific fields like SimpleSecurityID(30048) and MarketSegmentID(1300)
- Systems must correctly interpret the Reserved Identifier field to distinguish active vs reserved contracts
- Pre-Open session indicator must be processed to identify contracts in pre-open phase
- Strike price values must be processed as paise denomination

## Important Dates

No specific implementation dates mentioned in the circular. This appears to be a specification document for ongoing system operations.

## Impact Assessment

**Operational Impact:** Medium - Trading members and vendors providing derivatives trading systems need to ensure their software correctly parses and processes all fields in the updated Contract Master file format.

**System Impact:** All systems consuming BSE equity derivatives Contract Master files must be validated against the updated specifications. This includes trading platforms, risk management systems, and market data vendors.

**Market Participants Affected:** All equity derivatives trading members, system vendors, algorithmic trading firms, and market data consumers using BSE's Contract Master files.

**Technical Requirements:** Systems must handle 58+ fields including integer, character, and datetime data types with specific precisions and formats.