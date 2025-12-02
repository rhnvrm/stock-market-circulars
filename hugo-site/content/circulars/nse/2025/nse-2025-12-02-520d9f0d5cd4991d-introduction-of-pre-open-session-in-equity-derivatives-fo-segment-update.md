---
category: market-operations
circular_id: 520d9f0d5cd4991d
date: '2025-12-02'
description: NSE introduces additional indicator in order log reports for Pre-Open
  session in F&O segment effective December 08, 2025.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP71582.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical update to order log reports for pre-open session tracking;
  affects members' reporting systems but does not change trading rules or member obligations
  significantly.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP71582.pdf
processing:
  attempts: 1
  content_hash: f020c16508557c7b
  processed_at: '2025-12-02T13:01:55.321927'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-02T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP71582.pdf
severity: medium
source: nse
stocks: []
tags:
- pre-open-session
- equity-derivatives
- fo-segment
- order-logs
- trading-reports
- system-update
title: Introduction of Pre-Open Session in Equity Derivatives (F&O) Segment - Update
---

## Summary

NSE has announced that additional indicators will be provided in order log reports to identify Pre-Open session orders in the Equity Derivatives (F&O) segment. This update is effective from December 08, 2025, and is a continuation of the Pre-Open Session introduction announced in circular NSE/FAOP/71092 dated November 03, 2025. The changes will add a "Book Type" field with value "8 - Pre-Open" to identify orders placed during the pre-open session.

## Key Points

- Additional indicator to be added to order log reports from December 08, 2025
- New "Book Type" field will identify Pre-Open session orders with value "8 - Pre-Open"
- Changes apply to Order.txt file (field numbers 9 and 10) and Split Order Log file (field number 5)
- No change in file format; Pre-Open session data will be integrated into existing files
- Order.txt file available through NEAT screen (online backup)
- Split Order Log file (FO_ORD_LOG_<DDMMYYYY>_<TM_ID>_<COUNT>.CSV.gz) available on extranet server at \faoftp\F<Member Code> folder

## Regulatory Changes

This is a technical enhancement to existing reporting infrastructure. The Pre-Open session functionality was previously introduced via circular NSE/FAOP/71092 dated November 03, 2025. This update adds tracking and identification capabilities for Pre-Open orders in the order log reports.

## Compliance Requirements

- Members should update their systems to recognize and process the new "Book Type" indicator (value 8) for Pre-Open session orders
- Members need to ensure their order processing and reconciliation systems can handle the additional data field
- No changes to file formats, so existing parsers should continue to work with the additional data values

## Important Dates

- **Circular Date**: December 02, 2025
- **Implementation Date**: December 08, 2025 - Additional indicator becomes available in order log reports

## Impact Assessment

**Operational Impact**: Medium - Members will need to update their back-office systems and reporting tools to recognize and potentially filter/process Pre-Open session orders separately. The impact is limited as file formats remain unchanged, minimizing integration work.

**Market Impact**: Low - This is a reporting enhancement that provides better visibility and tracking of Pre-Open session activity. It does not affect trading mechanisms or market structure.

**Technical Impact**: Members using automated order processing systems should validate that the new Book Type values are handled correctly in their reconciliation and reporting workflows.