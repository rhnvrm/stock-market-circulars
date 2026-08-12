---
category: market-operations
circular_id: 63b36bc7de3894a4
date: '2026-08-11'
description: NSE has introduced a new Multiplier field (Field 55) to the EGR Security
  File and NNF Security File to enable correct Bid/Ask price calculation, effective
  September 7, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/EGR75691.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: The introduction of a new field (Field 55) in the EGR security file
  requires members to modify their trading and NNF systems to load and process the
  files properly before September 7, 2026.
pdf_url: https://nsearchives.nseindia.com/content/circulars/EGR75691.pdf
processing:
  attempts: 1
  content_hash: 204b6ea20c88513f
  processed_at: '2026-08-12T09:46:22.537625'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-08-11T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/EGR75691.pdf
severity: medium
source: nse
stocks: []
tags:
- electronic-gold-receipts
- egr
- file-format
- market-operations
- trading
title: Introduction of Multiplier Field in Electronic Gold Receipts Security File
---

## Summary

The National Stock Exchange of India (NSE) has announced the introduction of a new "Multiplier" field in the Electronic Gold Receipts (EGR) Security File and NNF Security File. This change modifies Part B – Annexure 1 of the structure of the EGR Security File & NNF Security File, which was previously specified in circular `NSE/EGR/74203` dated May 13, 2026. The new multiplier field (Field 55) contains a numeric multiplier value used to calculate the actual price (Bid/Ask Price) of the security by multiplying it with its quotation price. The changes will go live on September 7, 2026.

## Key Points

- **New Field Added**: Field number 55 ("Multiplier") is introduced in the EGR security file (`security_eg.gz`) and NNF security file (`nnf_security_eg.gz`).
- **Purpose**: This field holds the numeric multiplier value used to determine the actual security price (Bid/Ask) from its quotation price.
- **Extranet Path**: The files can be fetched from `/egftp/egcommon/ntneat` on the Extranet server.
- **Effective Date**: The modification goes live in production on September 7, 2026.

## Regulatory Changes

- **Modification to Security File Structure**: Modifies the EGR and NNF Security File structures specified in circular `NSE/EGR/74203` (dated May 13, 2026).
- **Field 55 Integration**: Introduces "Multiplier" as Field 55 in both files.

## Compliance Requirements

- **System Updates**: Members must update their trading applications to correctly parse the updated 55-field file structure.
- **File Loading**: Trading members must load the latest security file containing the new field onto their systems before trading on September 7, 2026.

## Important Dates

- **Circular Date**: August 11, 2026
- **Effective Date**: September 7, 2026

## Impact Assessment

- **Operational Impact**: Systems parsing `security_eg.gz` and `nnf_security_eg.gz` must adapt to the extra field to avoid parser crashes or missing security data. Correct calculation of Bid/Ask prices depends on the application of this multiplier value.
- **Vendor/IT Readiness**: Software vendors and in-house development teams handling NNF or EGR segments need to test and implement this update in their test environments before the live date.