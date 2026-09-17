---
category: trading
circular_id: dabc3dc7b490d46b
date: '2026-09-17'
description: BSE issues an advisory for trading members to ensure their front-end
  applications dynamically process intraday throttle limit updates (Template ID 10028)
  in the Equity segment.
draft: false
guid: https://www.bseindia.com/downloads/UploadDocs/Notices/20260917-22/20260917-22.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Advises trading members to support dynamic handling of intraday ETI
  throttle limit updates to prevent order rejections.
pdf_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260917-22/20260917-22.pdf
processing:
  attempts: 1
  content_hash: b8d9b4651ad5dece
  processed_at: '2026-09-17T16:37:26.755384'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-09-17T13:09:55+00:00'
rss_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260917-22/20260917-22.pdf
severity: medium
source: bse
stocks: []
tags:
- trading
- equity
- throttle-limit
- api
- master-circular
title: Advisory on Handling Throttle Limit Update Notification Message
---

## Summary

BSE has issued an advisory reminding trading members to ensure their front-end trading applications correctly handle and process the Throttle Update Notification message (Template ID 10028). The Exchange continuously monitors throttle limit utilisation on an intra-day basis and may proportionately reduce limits during trading hours if predetermined thresholds are exceeded.

## Key Points

- Throttle limits regulate and control order flow originating from members' trading applications across different session types (HF LITE, HF FULL, LF LITE, LF FULL).
- Applicable throttle limits are communicated via logon response (Template ID 10001) and throttle update notifications (Template ID 10028).
- The Exchange continuously monitors utilization on an intra-day basis and may proportionately reduce limits if usage exceeds predetermined thresholds.
- Members must ensure their front-end systems support dynamic processing of intraday throttle limit revisions with immediate effect.

## Regulatory Changes

Partial modification to Exchange circular no. 20260430-18 dated April 30, 2026 (Master Circular for Equity segment).

## Compliance Requirements

Trading members must ensure that their front-end trading applications are capable of dynamically processing intraday throttle limit updates and regulating order flow accordingly to avoid order rejections.

## Important Dates

- Notice Date: September 17, 2026
- Effective: Immediate

## Impact Assessment

Trading members failing to implement dynamic processing of throttle limit update messages risk order rejections due to breaches of applicable intraday throttle limits.