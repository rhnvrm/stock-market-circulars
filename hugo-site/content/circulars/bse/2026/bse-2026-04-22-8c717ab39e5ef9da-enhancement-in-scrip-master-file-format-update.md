---
category: trading
circular_id: 8c717ab39e5ef9da
date: '2026-04-22'
description: BSE is updating the Standardised Scrip Master File (BSE_EQ_SCRIP_DDMMYYYY.csv)
  to add a Closing Auction Session (CAS) indicator in Field 24 and rename the ISO
  tag for BSE Exclusive flag in Field 59, effective July 31, 2026.
draft: false
guid: https://www.bseindia.com/downloads/UploadDocs/Notices/20260422-15/20260422-15.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical file format change affecting trading members, front-end vendors,
  and back-office vendors connecting via ETI API. No immediate market impact but requires
  system changes before July 31, 2026 go-live.
pdf_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260422-15/20260422-15.pdf
processing:
  attempts: 1
  content_hash: 442583bb5afbdb6c
  processed_at: '2026-04-22T13:44:52.343938'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-04-22T11:28:05+00:00'
rss_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260422-15/20260422-15.pdf
severity: medium
source: bse
stocks: []
tags:
- scrip-master
- cas
- closing-auction-session
- file-format
- trading-system
- api
- eti-api
- trading-development
title: Enhancement in Scrip Master File Format - CAS Indicator and ISO Tag Update
---

## Summary

BSE is updating the Standardised Scrip Master File format (BSE_EQ_SCRIP_DDMMYYYY.csv) as a continuation of circular 20260330-40 dated March 30, 2026. Two changes are being made: adding a Closing Auction Session (CAS) indicator in Field 24, and renaming the ISO tag for the BSE Exclusive flag in Field 59 from 'Rsvd01' to 'XchgExclsv'. These changes will go live end of day Friday, July 31, 2026.

## Key Points

- Field 24 (previously 'Filler') will be renamed to 'Closing Auction Session (CAS) Indicator' with ISO tag changing from 'ElgbltyRETDBTMkt' to 'ElgbltyClsgAuctnSsn'
- Field 24 values: '0' = Scrip not in CAS, '1' = Scrip in CAS; data type remains Char(1)
- Field 59 ('BSE Exclusive') ISO tag renamed from 'Rsvd01' to 'XchgExclsv'; field name, value, and data type remain unchanged
- Changes affect the file SCRIP_DDMMYY.TXT and BSE_EQ_SCRIP_DDMMYYYY.csv formats
- Annexure-I contains the full revised Standardised Scrip Master file format with highlighted changes and a sample file

## Regulatory Changes

- Field 24 ISO tag updated: 'ElgbltyRETDBTMkt' → 'ElgbltyClsgAuctnSsn'
- Field 24 field name updated: 'Filler' → 'Closing Auction Session (CAS) Indicator'
- Field 59 ISO tag updated: 'Rsvd01' → 'XchgExclsv' (no change to field name, value, or data type)

## Compliance Requirements

- Trading members must review the changes and update their applications accordingly before July 31, 2026
- Front-end trading application vendors connecting through ETI API must make necessary system changes
- Back-office vendors must update their applications to accommodate the revised file format
- Members should refer to Annexure-I for the full revised format and sample file

## Important Dates

- **April 22, 2026**: Circular issued
- **July 31, 2026 (End of Day, Friday)**: Scrip master file with CAS indicator goes live

## Impact Assessment

This is a technical change impacting all participants who consume the BSE Scrip Master file, including trading members, front-end trading application vendors using the ETI API, and back-office vendors. The addition of the CAS indicator enables downstream systems to identify which scrips participate in the Closing Auction Session. The ISO tag rename for Field 59 is cosmetic and does not alter values or data types. Participants must update their parsing logic and field mappings before the July 31, 2026 effective date to avoid integration issues. Contact: bsehelp@bseindia.com / 022-45720400 or iml.info@bseindia.com / 022-2272 8705.