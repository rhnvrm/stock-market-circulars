---
category: market-operations
circular_id: b689b3bd54d9f04d
date: '2026-06-18'
description: NSE updates Part B – Annexure 10 (Structure of Final EGR UDiFF Trade
  File) from circular 74203 dated May 13, 2026. No change in the actual file format;
  only the annexure content is refreshed.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/EGR74778.zip
impact: low
impact_ranking: low
importance_ranking: low
justification: Purely a documentation/clarification update to an existing annexure;
  explicitly states no change in file format, affecting only technical teams maintaining
  EGR trade-file integrations.
pdf_url: https://nsearchives.nseindia.com/content/circulars/EGR74778.zip
processing:
  attempts: 1
  content_hash: 655cdc76efddae98
  processed_at: '2026-06-18T15:34:14.566494'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-18T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/EGR74778.zip
severity: low
source: nse
stocks: []
tags:
- egr
- electronic-gold-receipts
- udiff
- trade-file
- file-format
- market-operations
- settlement-calendar
title: UDIFF Trade File Format for Electronic Gold Receipts (EGR) Segment – Annexure
  Update
---

## Summary

NSE's Electronic Gold Receipts (EGR) department (Circular Ref. No. 15/2026, Download Ref. NSE/EGR/74778, dated June 18, 2026) issues an updated version of Part B – Annexure 10 (Structure of Final EGR UDiFF Trade File) originally published in exchange circular 74203 dated May 13, 2026. NSE explicitly states there is **no change in the file format**; the annexure content is republished with refreshed detail.

## Key Points

- The circular updates Annexure 10 of the earlier circular NSE/EGR/74203 (May 13, 2026) on Trading Parameters in EGR.
- **No change in file format** – existing integrations do not require modification.
- The updated annexure covers file nomenclature for multiple segments: CM, FO, CD, CO, and EG.
- For EGR (segment code `EG`), the standard file naming convention is: `Trade_NSE_EG_0_TM_<member_code>_YYYYMMDD_<P/F>_<hhmm>.csv.gz`.
- T+0 settlement trade files (CM segment only) use market type `T0` in the filename.
- Large files may be split into parts (P1, P2 … Pn); the final consolidated file carries suffix `P0`.
- A trigger file (`.txt`) is required when record count exceeds 1 crore, listing all split-file names.

## Regulatory Changes

No regulatory changes. This is a clarification/documentation update replacing the earlier annexure. The file structure, naming convention, and operational rules remain unchanged from the original circular 74203.

## Compliance Requirements

- Members should replace their reference copy of Part B – Annexure 10 with the updated version attached to this circular.
- No system or process changes are required as the file format is unchanged.
- Members should verify that their EGR trade-file generation follows the naming convention: `Trade_NSE_EG_0_TM_<member_code>_YYYYMMDD_<P/F>_0000.csv.gz`.

## Important Dates

- **Circular Date:** June 18, 2026
- **Reference Circular:** NSE/EGR/74203 dated May 13, 2026 (original annexure being replaced)
- No new effective date specified; the updated annexure supersedes the prior version immediately.

## Impact Assessment

Impact is minimal. The circular is a housekeeping update to technical documentation for EGR segment trade-file consumers. Since no file format changes are introduced, trading members and clearing members who have already integrated UDIFF trade-file processing for EGR need not make any system changes. Technology teams should update their internal documentation to reference this revised annexure.