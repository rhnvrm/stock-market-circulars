---
category: market-operations
circular_id: b2d06c78ddf29639
date: '2026-09-18'
description: NSE Clearing Limited introduces a file-based bulk confirmation facility
  for custodians regarding bids executed in Offer for Sale (OFS) via the N-MASS application,
  effective September 21, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT76417.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Facilitates bulk order confirmation processing for custodians in Offer
  for Sale (OFS) transactions through the N-MASS application.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT76417.zip
processing:
  attempts: 1
  content_hash: e546e4e9cac296c7
  processed_at: '2026-09-18T16:11:44.869320'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-09-18T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT76417.zip
severity: medium
source: nse
stocks: []
tags:
- offer-for-sale
- settlement-and-operations
- trading
title: File based bulk confirmation facility to Custodians for bids executed in Offer
  for Sale (OFS)
---

## Summary

NSE Clearing Limited has announced the introduction of a file-based bulk confirmation facility for custodians for bids executed in Offer for Sale (OFS). This functionality will be available through the N-MASS application effective September 21, 2026.

## Key Points

- Custodians must be assigned the "OFS" service through the role management menu under N-MASS (Clearing Management > Create and Update > Clearing Management).
- Order confirmation files can be generated using the path: `NMASS > OFS > Clearing Management > Ord Conf File Upload > Generate file`.
- File nomenclature for generation follows `<Custodian Code>_OFS_<DDMMYYYY>.Dnn`.
- Upload files for confirmation or rejection must follow the nomenclature `<Custodian Code>_OFS_<DDMMYYYY>.Unn` with approval/rejection flags ('Y'/'N') in the final field.
- The facility supports separate window timings for STP type 'H' and 'T'.

## Regulatory Changes

- Introduction of automated file-based bulk confirmation and rejection mechanisms for custodians handling OFS transactions.

## Compliance Requirements

- Custodians need to assign the appropriate roles within N-MASS and ensure proper nomenclature and formatting for generated and uploaded files within the defined confirmation windows.

## Important Dates

- **Effective Date:** September 21, 2026

## Impact Assessment

- Streamlines operational workflows for custodians participating in Offer for Sale (OFS) auctions by enabling bulk confirmation and reducing manual processing overhead.