---
category: market-operations
circular_id: 8d2ff309e4453da7
date: '2025-10-27'
description: BSE announces updates to the Contract Master file format specifications
  for Equity Derivatives trading, including new field definitions and data structures.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={015D8FCA-578D-4D41-9AA5-DBB2447F0939}&noticeno=20251027-48&dt=10/27/2025&icount=48&totcount=63&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical update affecting equity derivatives trading systems and participants
  using contract master files for futures and options. Important for system integrations
  but does not directly impact trading rules.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251027-48&attachedId=e94e5aeb-c16b-41d3-b95c-325200d83235
processing:
  attempts: 1
  content_hash: e9aebec44ec64c49
  processed_at: '2025-10-27T18:48:02.473417'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-27T13:11:20+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={015D8FCA-578D-4D41-9AA5-DBB2447F0939}&noticeno=20251027-48&dt=10/27/2025&icount=48&totcount=63&flag=0
severity: medium
source: bse
stocks: []
tags:
- contract-master
- derivatives
- eti-api
- file-format
- futures-options
- market-infrastructure
- options
- technical-specification
title: Enhancement in Contract Master File Formats for Equity Derivatives Segment
---

## Summary

BSE has published enhanced specifications for Contract Master file formats used in the Equity Derivatives Segment. The document provides detailed field-level specifications for three CSV file types: EQD_CODDMMYY.csv (standard contract master), EQD_CO_abr_DDMMYY.csv (abbreviated format), and EQD_INDEX_CODDMMYY.csv (index contracts). The format includes 58 fields covering contract identifiers, instrument details, strike prices, lot sizes, tick sizes, and ETI API integration parameters.

## Key Points

- Contract Master files available in three CSV formats for equity derivatives
- Files contain comprehensive contract specifications with 58 defined fields
- Supports Index Futures (IF), Index Options (IO), Stock Futures (SF), and Stock Options (SO)
- Contract tokens and asset tokens provide unique identifiers for contracts and underlying securities
- Strike prices displayed in paise with precision value of 2
- Option types include Call European (CE) and Put European (PE)
- Pre-Open session indicator field distinguishes contracts available in pre-open
- Minimum lot size, board lot quantity, and tick size specifications included
- Single order maximum quantity limits defined per contract
- ETI API integration fields included: Partition ID, Instrument ID/SimpleSecurityID, Market Segment ID
- Series codes follow naming convention indicating underlying, expiry, contract type (e.g., SENSEX20SEPFUT, SENSEX20MAR34900.00CE)
- Weekly and monthly contract formats supported for both futures and options

## Regulatory Changes

This circular represents an enhancement to existing Contract Master file format specifications. The standardized format ensures consistency in how contract information is distributed to market participants and trading systems.

## Compliance Requirements

- Market participants and trading members using Contract Master files must update their systems to handle the specified file format
- Systems must correctly parse all 58 fields including new ETI API integration fields
- Data parsing must account for date format DD-MMM-YYYY and strike prices in paise
- Trading systems integrating with ETI API must map fields correctly (Partition ID, SimpleSecurityID, MarketSegmentID)
- Pre-Open session indicator must be processed to determine contract availability

## Important Dates

No specific implementation or effective dates mentioned in the circular. The document appears to be a technical specification reference.

## Impact Assessment

**System Impact:** Medium - Trading members, technology vendors, and market data consumers using BSE equity derivatives data will need to ensure their systems correctly parse and process the enhanced Contract Master file format.

**Operational Impact:** Medium - Organizations may need to update file parsing routines, data validation logic, and downstream systems consuming contract master data.

**Market Impact:** Low - This is a technical specification update that does not change trading rules, lot sizes, or contract specifications themselves.

**Integration Impact:** Medium - Systems using ETI API for trading must properly handle fields like Partition ID (field 13), SimpleSecurityID (field 37), and MarketSegmentID (field 29) for correct order routing and execution.