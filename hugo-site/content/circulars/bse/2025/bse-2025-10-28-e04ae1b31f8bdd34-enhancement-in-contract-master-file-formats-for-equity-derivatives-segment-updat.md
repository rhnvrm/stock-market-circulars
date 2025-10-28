---
category: market-operations
circular_id: e04ae1b31f8bdd34
date: '2025-10-28'
description: BSE updates the Contract Master file format specifications for Equity
  Derivatives segment, including new field definitions and data structures for futures
  and options contracts.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={515BFEE3-9CC9-4E62-984C-76F19BAA3996}&noticeno=20251028-48&dt=10/28/2025&icount=48&totcount=64&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical update affecting trading members and system integrators who
  process contract master files for equity derivatives. Important for operational
  continuity but does not directly impact trading rules or compliance requirements.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251028-48&attachedId=2e874865-314d-4ae0-bbc5-c1c8ea4f5014
processing:
  attempts: 1
  content_hash: 36d0abe2e447bdf0
  processed_at: '2025-10-28T18:48:46.659316'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-28T14:26:26+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={515BFEE3-9CC9-4E62-984C-76F19BAA3996}&noticeno=20251028-48&dt=10/28/2025&icount=48&totcount=64&flag=0
severity: medium
source: bse
stocks: []
tags:
- equity-derivatives
- contract-master
- file-format
- technical-specification
- trading-system
- futures
- options
- ETI-API
title: Enhancement in Contract Master File Formats for Equity Derivatives Segment
  - Update
---

## Summary

BSE has published updated specifications for Contract Master file formats used in the Equity Derivatives segment. The document provides detailed field-level specifications for three CSV file formats: EQD_CODDMMYY.csv (main contract master), EQD_CO_abr_DDMMYY.csv (abbreviated version), and EQD_INDEX_CODDMMYY.csv (index contracts). These files contain essential contract parameters for Index Futures (IF), Index Options (IO), Stock Futures (SF), and Stock Options (SO).

## Key Points

- Three CSV file formats specified for contract master data distribution
- Detailed field definitions provided for 58+ fields including contract identifiers, instrument types, strike prices, expiry dates, and trading parameters
- Support for both monthly and weekly futures/options contracts
- Integration with ETI (Enhanced Trading Interface) API including fields like SimpleSecurityID, MarketSegmentID, and Partition ID
- Control record contains Segment Indicator (value '2' for underlying market) and Version Number
- Contract tokens, asset tokens, and instrument IDs serve as unique identifiers
- File format supports pre-open session indicators and reserved contract flags
- Date fields use DD-MMM-YYYY format for consistency
- Price and strike price values displayed in paise with precision field (default '2')
- Series code examples provided for futures and options naming conventions

## Technical Specifications

### File Formats
- **EQD_CODDMMYY.csv**: Primary contract master file
- **EQD_CO_abr_DDMMYY.csv**: Abbreviated contract master file
- **EQD_INDEX_CODDMMYY.csv**: Index-specific contract master file

### Instrument Types
- IF: Index Futures
- IO: Index Options
- SF: Stock Futures
- SO: Stock Options

### Option Types
- CE: Call Option (European)
- PE: Put Option (European)
- Blank for Futures Contracts

### Key Fields
- Contract Token Number / Series ID (Unique identifier)
- Asset Token Number (Underlying identifier, e.g., 500410)
- Strike Price (in paise, default '0' for futures)
- Expiry Date (last trading date)
- Tick Size (minimum price movement in paise)
- Minimum Lot Size / Board Lot Quantity
- Single Order Max Quantity
- Quantity Multiplier (lot size multiplier)
- Pre-Open Session Indicator (0=not in pre-open, 1=in pre-open)
- Reserved Identifier (0=active, 1=reserved)

## ETI Integration

The file format includes specific fields required for trading through BSE's Enhanced Trading Interface (ETI):
- Partition ID (field 13)
- Market Segment ID / Product ID (field 29)
- Capacity Group ID (field 30)
- SimpleSecurityID / Instrument ID (field 37)

## Data Format Standards

- All CSV format files
- Underlying Asset Class default: 'EDX'
- Precision default: '2' decimal places
- Dates in DD-MMM-YYYY format
- Symbol/Asset Code examples: BSX, BSI
- Underlying assets: RIL, SENSEX, TATAMOTORS, etc.

## Series Code Convention

Examples of series code naming:
- SENSEX20SEPFUT (Monthly Future)
- SENSEX20SEP07FUT (Weekly Future)
- SENSEX20MAR34900.00CE (Monthly Call Option)

## Impact Assessment

This update primarily affects:
- Trading members and brokers who consume contract master files
- System integrators and software vendors developing trading applications
- Risk management systems that rely on contract specifications
- Market data vendors distributing BSE derivatives data

Trading members should ensure their systems are updated to parse the complete field set as specified. The integration with ETI API fields enables seamless trading operations for participants using the enhanced trading interface.