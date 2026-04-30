---
category: market-operations
circular_id: cda58fdb5e11f8f0
date: '2026-04-30'
description: NSE Clearing specifies file formats for clearing, settlement, risk and
  collateral management of trades in the Electronic Gold Receipts (EGR) segment, requiring
  member system development.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/EGR74018.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical circular mandating system development for EGR segment members;
  operationally significant for clearing and trading members participating in the
  newly launched EGR segment, but limited to a specific participant set.
pdf_url: https://nsearchives.nseindia.com/content/circulars/EGR74018.zip
processing:
  attempts: 1
  content_hash: 5ee3706d2be7afda
  processed_at: '2026-04-30T14:04:41.346984'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-04-30T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/EGR74018.zip
severity: medium
source: nse
stocks: []
tags:
- electronic-gold-receipts
- egr
- file-formats
- nse-clearing
- settlement
- system-development
- ncl
- clearing-member
- trading-member
title: File Formats for Electronic Gold Receipt Segment - NSE Clearing
---

## Summary

NSE Clearing Limited (NCL) has issued file format specifications for the Electronic Gold Receipts (EGR) segment following SEBI approval for clearing, settlement, risk, and collateral management of EGR trades. Members are required to develop systems compatible with these formats. A detailed circular covering full clearing, settlement, risk, and collateral management procedures will follow separately.

## Key Points

- SEBI has approved NSE Clearing for clearing, settlement, risk, and collateral management of EGR segment trades
- Nine distinct file formats are specified across funds, obligations, auction, and margin reporting
- Both Trading Members (TMs) and Clearing Members (CMs) have separate report files
- Files are distributed via Members Folder/Reports and Member Portal/Extranet paths
- A comprehensive clearing and settlement procedure circular is forthcoming
- Reference circulars: NSE/EGR/73891 (Apr 24, 2026) on EGR segment launch; NCL/CMPL/73975 on NCL membership

## Regulatory Changes

NSE Clearing has received SEBI approval to operate clearing, settlement, risk, and collateral management for the EGR segment. This formalises the operational framework for Electronic Gold Receipts trading on NSE.

## Compliance Requirements

Members must complete system development to consume and process the following file formats:

- **DFND** (Daily Funds Statement): `C_memcode_DFND_DDMMYYYYY.csv` — covers settlement transactions including debit/credit, original and due amounts
- **DFNS** (Bank Summary Report): `C_memcode_DFNS_DDMMYYYY.csv` — bank account-level transaction summary
- **Funds Brokerage TM File**: `memcode_T_NSP_DDMMYYYYY.csv` — brokerage amounts at trading member level
- **Funds Brokerage CM File**: `memcode_NSP_DDMMYYYYY.csv` — brokerage amounts at clearing member level
- **ADIF** (Auction Difference Report): `E_memcode_ADIF_SETTYPNO_DDMMYYYY.csv` — auction valuation and difference amounts
- **Trading Member Client-Wise Obligation**: `E_<MemberCode>_DEPO_DEL_DTLS_Normal<DDMMYYYY>.csv` / `Auction<DDMMYYYY>.csv` — client-level delivery obligation details including UCC, PAN, BO ID, and ISIN
- **CSQR** (Close-Out Price File): `E_CSQR_7_<Sett no>_ddmmyyyy.csv` — close-out prices per security and settlement
- **Auction Rate File**: `E_7_<sett no>_ddmmyyyy.txt` — weighted average auction prices per security
- **MG01** (Consolidated Margin Report): `E_MG01_<mem_cd>_DDMMYYYY.lis` — collateral details and margin components including base minimum capital, MTM, VAR, and extreme loss margin

## Important Dates

- **Apr 24, 2026**: NSE circular NSE/EGR/73891 on EGR segment launch
- **Apr 30, 2026**: This circular (NCL/EGR/74018, Ref No. 0155/2026) issued
- Detailed clearing and settlement circular to be issued shortly (date not specified)

## Impact Assessment

This circular directly impacts all members intending to participate in the EGR segment. System development teams at clearing and trading member firms must integrate the specified CSV/text file formats into their back-office and risk management systems before EGR trading goes live. The scope is limited to EGR segment participants and does not affect equity, derivatives, or other segments. Operational readiness depends on timely system changes, and members should monitor for the forthcoming detailed clearing procedure circular.