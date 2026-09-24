---
category: trading
circular_id: 1b69761813c681c1
date: '2026-09-24'
description: NSE announces the dissemination of the Quantity Freeze Report for the
  Electronic Gold Receipt (EGR) segment starting October 9, 2026, applicable from
  October 12, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/EGR76507.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Establishes quantity freeze reporting schedules, file nomenclatures,
  and default security file values for the Electronic Gold Receipt (EGR) segment.
pdf_url: https://nsearchives.nseindia.com/content/circulars/EGR76507.pdf
processing:
  attempts: 1
  content_hash: 6b565625aaf7b0b5
  processed_at: '2026-09-24T11:14:14.787801'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-09-24T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/EGR76507.pdf
severity: low
source: nse
stocks: []
tags:
- electronic-gold-receipt
- freeze-quantity
- market-operations
- trading
title: Dissemination of Quantity Freeze Report for Electronic Gold Receipt Segment
---

## Summary

National Stock Exchange of India Limited (NSE) has announced the dissemination of the Quantity Freeze Report for the Electronic Gold Receipt (EGR) segment. The report will be disseminated at the end of the trading day starting from October 9, 2026, and will be applicable w.e.f. October 12, 2026.

## Key Points

- **Report Dissemination:** Quantity Freeze Report (`qty_freeze_ddmmyyyy.csv`) will be available at `/egftp/common/ntneat` starting October 9, 2026.
- **Applicability Date:** Effective from October 12, 2026.
- **Report Fields:** Includes `SYMBOL`, `SERIES`, and `FREEZE_QTY`. Orders exceeding the freeze quantity will be rejected by the trading system.
- **Default Security File Values:** EGR Security File (`security_eg.gz`) and NNF Security File will include default issue size (999999999999) and freeze percent (10000).

## Regulatory Changes

- Introduction of daily Quantity Freeze Report dissemination for the EGR segment.
- Definition of automated order rejection criteria for orders exceeding the specified freeze quantity.

## Compliance Requirements

- Trading members must update their trading systems and internal workflows to ingest and respect the `qty_freeze_ddmmyyyy.csv` file starting October 12, 2026.

## Important Dates

- **October 9, 2026:** Dissemination of Quantity Freeze Report begins.
- **October 12, 2026:** Quantity freeze values become applicable.

## Impact Assessment

- Enhances risk management and controls order execution limits in the Electronic Gold Receipt segment.