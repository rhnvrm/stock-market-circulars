---
category: trading
circular_id: 1c0362f27298dacf
date: '2026-09-11'
description: BSE issues a reminder to trading members to reaffirm and validate whitelisting
  of exchange Gateway IPs in the Equity Segment ahead of gateway assignments.
draft: false
guid: https://www.bseindia.com/downloads/UploadDocs/Notices/20260911-27/20260911-27.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Ensures uninterrupted trading connectivity by reminding members to
  whitelist exchange Gateway IPs for the Equity segment.
pdf_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260911-27/20260911-27.pdf
processing:
  attempts: 1
  content_hash: e1df5106547679c9
  processed_at: '2026-09-11T16:18:05.509995'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-09-11T13:27:14+00:00'
rss_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260911-27/20260911-27.pdf
severity: medium
source: bse
stocks: []
tags:
- trading
- equity
- gateway-ips
- connectivity
- network-security
- bolt-plus
title: Reminder to Reaffirm Whitelisting of Exchange Gateway IPs in Equity Segment
---

## Summary

BSE has issued a reminder regarding the whitelisting of exchange Gateway IPs in the Equity Segment. Members are requested to ensure that the required IP whitelisting has been completed and validated in advance of gateway assignments starting from Tuesday to avoid any connectivity or access-related issues.

## Key Points

- Reaffirmation of IP whitelisting for specific exchange IPs in Equity and Equity (BSE Colocation) segments.
- Specific IPs listed include ranges like 10.255.255.65 to 10.255.255.70 and 10.255.253.5 to 10.255.253.7 with ports 18906 to 18914.
- Recommendation as per BOLT Plus Connectivity Manual to allow the complete IP range of 10.255.X.X (subnet mask 255.255.0.0) to accommodate future server additions without client-side reconfiguration.
- Connection Gateway IP address remains unchanged, and connection requests should continue to be sent to the connection gateway as currently done.

## Regulatory Changes

None.

## Compliance Requirements

Trading members must verify and complete network whitelisting for the specified IP addresses and port ranges to ensure uninterrupted trading access.

## Important Dates

- Notice Date: 11 Sep 2026
- Effective/Assignment from: Tuesday onwards

## Impact Assessment

Failure to whitelist the required IPs may result in connectivity or access issues once gateway assignments are enabled.