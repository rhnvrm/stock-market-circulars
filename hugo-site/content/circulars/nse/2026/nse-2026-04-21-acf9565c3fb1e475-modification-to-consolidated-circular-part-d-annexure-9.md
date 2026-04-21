---
category: market-operations
circular_id: acf9565c3fb1e475
date: '2026-04-21'
description: NSE modifies Part D Annexure 9 of the F&O consolidated circular to expand
  the Total Volume field size from char(10) to char(17) in the Final Bhav Copy (DDMM0000.md)
  file, effective May 9, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP73824.pdf
impact: medium
impact_ranking: medium
importance_ranking: low
justification: Technical file format change affecting systems that consume F&O Final
  Bhav Copy data; no trading rule or compliance obligation change, but member systems
  processing the md file must be updated before the May 9, 2026 go-live to avoid data
  truncation.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP73824.pdf
processing:
  attempts: 1
  content_hash: b84782d5a5499aad
  processed_at: '2026-04-21T13:38:13.848964'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-04-21T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP73824.pdf
severity: low
source: nse
stocks: []
tags:
- futures-options
- bhav-copy
- file-format
- data-format
- fno-segment
- technical-change
- market-operations
title: 'NSE F&O Segment: Total Volume Field Size Expanded in Final Bhav Copy Format'
---

## Summary

NSE's Futures & Options segment has issued a partial modification to Part D Annexure 9 of the F&O consolidated circular (NSE/FAOP/67775, dated April 30, 2025). The change expands the `Total Volume` field (field number 12) in the Final Bhav Copy file (`DDMM0000.md`) from `char(10)` to `char(17)`. All other fields and the overall file structure remain unchanged. The effective date for live implementation is **May 9, 2026**, preceded by a mock run.

## Key Points

- Only one field is modified: **Field 12 – Total Volume**, size increased from `char(10)` to `char(17)`
- File nomenclature (`DDMM0000.md`) and all other fields remain unchanged
- Change is in **Part D, Annexure 9** of the F&O consolidated circular
- Reference base circular: NSE/FAOP/67775 dated April 30, 2025
- Circular Ref. No: 48/2026; Download Ref: NSE/FAOP/73824

## Regulatory Changes

Partial modification to Part D of the F&O Consolidated Circular:

| Annexure | File | Field No. | Field Name | Current Size | Revised Size |
|---|---|---|---|---|---|
| 9 | DDMM0000.md | 12 | Total Volume | char(10) | char(17) |

No structural or format changes beyond the above field size expansion.

## Compliance Requirements

- All members and their technology vendors who parse or ingest the Final Bhav Copy (`DDMM0000.md`) file must update their systems to accommodate the expanded `Total Volume` field size (`char(17)`) before the effective date
- Systems with fixed-width or strict-length parsing logic for field 12 are at risk of data truncation or processing errors if not updated
- Members should test their updated systems during the mock run period prior to May 9, 2026

## Important Dates

- **April 21, 2026** – Circular issued
- **May 9, 2026** – Effective date of implementation (mock run precedes live go-live)

## Impact Assessment

This is a technical operational change with moderate impact on member back-office and data systems that consume NSE's F&O Final Bhav Copy file. The field size expansion from 10 to 17 characters for Total Volume suggests increasing trade volumes in the F&O segment have exceeded the previous capacity of the field. Members using automated data pipelines, risk systems, or reporting tools that parse this file must update their field definitions before May 9, 2026 to avoid data integrity issues. There is no change to trading rules, margins, or compliance obligations.