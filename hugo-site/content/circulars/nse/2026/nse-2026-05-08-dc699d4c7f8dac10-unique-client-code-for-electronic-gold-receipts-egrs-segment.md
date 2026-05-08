---
category: trading
circular_id: dc699d4c7f8dac10
date: '2026-05-08'
description: NSE introduces UCC creation guidelines for the new Electronic Gold Receipts
  (EGR) segment, effective May 16, 2026, including segment code, validation rules,
  and reporting formats.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/ISC74132.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational circular for trading members to set up client codes for
  a new EGR segment; affects member back-office processes but limited to a niche gold
  receipts segment with a defined effective date.
pdf_url: https://nsearchives.nseindia.com/content/circulars/ISC74132.zip
processing:
  attempts: 1
  content_hash: 27bd3019920a73b8
  processed_at: '2026-05-08T14:00:12.563336'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-08T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/ISC74132.zip
severity: medium
source: nse
stocks: []
tags:
- egr
- electronic-gold-receipts
- ucc
- unique-client-code
- new-segment
- trading-members
- compliance
- bulk-upload
title: Unique Client Code for Electronic Gold Receipts (EGRs) Segment
---

## Summary

NSE has issued guidelines for Trading Members to create Unique Client Codes (UCCs) for the newly launched Electronic Gold Receipts (EGR) segment. The circular follows the earlier launch announcement (NSE/EGR/73891 dated April 24, 2026) and specifies the segment code, applicable validations, bulk upload format, trading permission timelines, and reporting structure. The circular is effective from May 16, 2026.

## Key Points

- Segment code for creating UCCs in the EGR segment is **"E"**.
- All existing Cash segment validations (as per Master Circular NSE/ISC/73973 dated April 30, 2026) also apply to the EGR segment.
- UCCs can be created using the New Client Bulk Upload file format (Annexure A).
- UCCs compliant by 22:00 hrs on the previous day will be deemed Permitted to Trade for the next trading day.
- A daily segment-wise report of UCCs (Permitted to Trade and Not Permitted to Trade) will be provided in batch 2.
- Existing reports (Full File, Mandatory Report, PAN Status Report) will be extended to include EGR segment records.

## Regulatory Changes

- Extension of the UCC framework to the new EGR segment with segment code "E".
- Cash segment validations are adopted wholesale for the EGR segment without modification.
- New segment-specific report files introduced under the path `/EGFTP/Reports`.

## Compliance Requirements

- Trading Members must register UCCs for clients wishing to trade in the EGR segment using the prescribed bulk upload format (UCI_YYYYMMDD.Tnn pipe-delimited file).
- Members must ensure UCCs are submitted and validated by 22:00 hrs on the day prior to intended trading.
- Members should update back-office and compliance systems to consume the new EGR segment reports.

## Important Dates

- **May 08, 2026**: Circular issued.
- **April 24, 2026**: Referenced launch circular NSE/EGR/73891 for EGR segment.
- **April 30, 2026**: Referenced Master Circular NSE/ISC/73973 for Cash segment validations.
- **May 16, 2026**: Effective date of this circular.

## Impact Assessment

This circular has a moderate operational impact on Trading Members who intend to offer EGR segment trading to clients. Members must update their UCC registration workflows, bulk upload processes, and report consumption pipelines to accommodate the new segment. The daily cut-off of 22:00 hrs for UCC compliance is operationally similar to existing Cash segment procedures, reducing the implementation burden. Investors and issuers are not directly affected; the impact is primarily on member back-office and compliance teams preparing for the May 16, 2026 launch.