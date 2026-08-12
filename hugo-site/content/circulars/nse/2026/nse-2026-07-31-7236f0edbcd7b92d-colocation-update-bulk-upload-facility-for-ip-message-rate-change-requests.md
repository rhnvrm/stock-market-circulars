---
category: market-operations
circular_id: 7236f0edbcd7b92d
date: '2026-07-31'
description: NSE has introduced a bulk upload facility via the ENIT system, allowing
  members to request message rate changes (upgrades or downgrades) for up to 100 Colocation
  IPs simultaneously.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD75498.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: The introduction of a bulk upload facility for up to 100 Colocation
  IP message rate changes significantly reduces the manual effort and time burden
  for trading members managing multiple IPs.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD75498.pdf
processing:
  attempts: 1
  content_hash: 03c06e55bf24e7e4
  last_updated: '2026-08-12T22:31:48.652696'
  processed_at: '2026-08-12T22:31:39.632598'
  processor_version: '2.0'
  retry_requested_for_stage: claude_failed
  retry_source: backfill
  stage: completed
  status: published
published_date: '2026-07-31T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD75498.pdf
severity: low
source: nse
stocks: []
tags:
- colocation
- enit
- message-rate
- ip-address
- bulk-upload
title: NSE Introduces Bulk Upload Facility for Colocation IP Message Rate Change Requests
---

## Summary

The National Stock Exchange of India (NSE) has introduced a new Bulk Upload Facility on the ENIT-NEW-TRADE portal. This facility allows trading members to submit Message Rate Change requests (upgrades or downgrades) for multiple Colocation IPs simultaneously. Designed to streamline operations and enhance efficiency, this bulk upload option is available in addition to the existing individual submission method.

## Key Points

- **Bulk Upload Path:** The bulk upload template is available for download and upload via ENIT-NEW-TRADE under `Membership > Colocation > Colocation Request Bulk Upload`.
- **Capacity Limit:** Members can submit a maximum of 100 IP records per file upload. The upload file must not contain any duplicate IP records.
- **Validation Rules:** The proposed segment-wise message bifurcation must be exactly equal to the New Message Rate specified for the IP. Furthermore, if user IDs are mapped with the IP (as Primary or Multilocked) in a segment, the message rate cannot be set to "0".
- **All-or-Nothing Processing:** A bulk file is only processed if all records within it are valid and error-free. If a file contains invalid entries, the entire file will be rejected, and no request reference numbers will be generated.
- **Error Feedback:** For rejected files, the system will generate an error file highlighting the problematic rows and providing remarks for rectification. This error file will be accessible at the same ENIT path.
- **Concurrency:** While the facility is available to all ENIT users at the member's end, only one ENIT user can upload a bulk file at any given time to prevent conflicts or data inconsistency.
- **Processing Fees:** The first Message Rate Change request per Colocation IP in a calendar month is free of charge, regardless of whether the request status is approved, pending, or rejected. Subsequent requests for the same IP in the same calendar month will incur a Processing Fee of ₹2,000/- (plus applicable taxes).

## Regulatory Changes

- No regulatory rules or compliance frameworks have been altered. This is an operational enhancement to the existing ENIT-NEW-TRADE portal workflows for colocation services.

## Compliance Requirements

- **Accuracy of Templates:** Members must ensure all fields in the bulk template (such as IP Address, Rack Number, and Current Message Rate) are filled accurately before uploading.
- **Internal Coordination:** Members should coordinate internal portal usage, as only one user per member can perform a bulk upload at any given moment.
- **Error Resolution:** In case of rejection, members must retrieve the error file via ENIT, rectify the problematic rows, and resubmit the complete file.

## Important Dates

- **Circular Date:** July 31, 2026
- **Effective Date:** August 03, 2026 (from start of business hours)
- **Cutoff Time:** Requests submitted on or before 3:00 p.m. on a working day will be processed on a best-effort basis, with completion expected within T+5 working days.

## Impact Assessment

- **Operational Impact:** High positive impact for trading members with large colocation setups. The ability to request rate changes for up to 100 IPs in one file saves significant administrative time and reduces manual data-entry errors.
- **Financial Impact:** Neutral. The fee of ₹2,000/- plus taxes for subsequent requests in a calendar month remains unchanged, but the automated enforcement of one free request per IP per month is clarified.