---
category: market-operations
circular_id: 32d81318aea6a0cc
date: '2026-04-29'
description: NSE circular specifying the proposed file formats and data structures
  for the Electronic Gold Receipts (EGR) segment, covering security files, participant
  files, order/trade logs, and bhavcopy files.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/EGR73954.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical operational circular defining file format standards for the
  EGR segment; critical for trading members and technology teams integrating with
  NSE EGR systems, but limited direct market-wide impact.
pdf_url: https://nsearchives.nseindia.com/content/circulars/EGR73954.zip
processing:
  attempts: 1
  content_hash: 78c0bd0a982a9f97
  processed_at: '2026-04-29T14:12:45.867576'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-04-29T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/EGR73954.zip
severity: medium
source: nse
stocks: []
tags:
- egr
- electronic-gold-receipts
- file-formats
- market-data
- trading-systems
- neat
- bhavcopy
- order-log
- trade-file
- extranet
title: Proposed File Formats for Electronic Gold Receipts (EGR) Segment
---

## Summary

NSE has issued a circular specifying the proposed file formats for the Electronic Gold Receipts (EGR) segment. The circular provides detailed structural specifications for 10 file types used by trading members and market participants to access security, participant, order, trade, and market data through NSE's NEAT/NEATPlus platforms and the extranet server.

## Key Points

- Ten annexures define the structure of all key EGR segment data files
- EGR Security File (`security_eg.gz`) and NNF Security File (`nnf_security_eg.gz`) are available at `/egftp/common/ntneat` on the extranet
- Security file fields include Token, Symbol, Series, InstrumentType, IssuedCapital, PermittedToTrade, CreditRating, SecurityStatus (across Normal, Oddlot, RETDBT, and Auction markets), and Eligibility flags
- InstrumentType supports: Equities (0), Preference Shares (1), Debentures (2), Warrants (3), Miscellaneous (4)
- PermittedToTrade values: Listed (0), Permitted to Trade (1), BSE Listed (2)
- SecurityStatus values across markets: Preopen (1), Open (2), Suspended (3), Preopen Extended (4), Stock Open With Market (5), Price Discovery (6)
- Order and Trade files are available via NEAT/NEATPlus online backup
- EGR Order Logs are available on the extranet server
- Final EGR UDiFF Trade File and EGR Bhavcopy (DAT) formats are also specified

## Regulatory Changes

This circular formalises the proposed file format standards for the EGR segment. It establishes the data field definitions and file naming conventions that participants must adhere to when interfacing with NSE's EGR systems.

## Compliance Requirements

- Trading members and technology vendors integrating with the EGR segment must align their systems to the specified file structures
- Participants accessing security, order, and trade data via the extranet or NEAT/NEATPlus must use the file formats defined in the ten annexures
- Systems must correctly interpret all defined field codes (e.g., SecurityStatus, InstrumentType, PermittedToTrade flags)

## Important Dates

No specific effective date is mentioned in the available content. Participants should refer to the full circular for implementation timelines.

## Impact Assessment

This circular primarily affects trading members, clearing members, and technology teams developing or maintaining systems for the EGR (Electronic Gold Receipts) segment. The standardised file formats ensure consistent data exchange between NSE and market participants for gold-backed instruments. There is no direct price or trading impact; however, non-compliance with the specified formats could disrupt data feeds, order management systems, or back-office reconciliation for EGR trades.