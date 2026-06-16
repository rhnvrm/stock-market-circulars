---
category: trading
circular_id: 984d405acb88b585
date: '2026-06-16'
description: BSE discontinues additional multicast streams for the EDX (equity derivatives)
  segment from its Disaster Recovery site with immediate effect, following network
  optimisation that eliminated the packet drop issues the streams were introduced
  to address.
draft: false
guid: https://www.bseindia.com/downloads/UploadDocs/Notices/20260616-21/20260616-21.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Technical infrastructure change affecting only colocation members trading
  equity derivatives from DR site; existing primary multicast streams remain unchanged,
  and the discontinuation addresses an improvement rather than a disruption.
pdf_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260616-21/20260616-21.pdf
processing:
  attempts: 1
  content_hash: 5599b75f3d1c0c5f
  processed_at: '2026-06-16T17:02:22.925317'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-16T13:31:53+00:00'
rss_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260616-21/20260616-21.pdf
severity: low
source: bse
stocks: []
tags:
- derivatives
- mock-trading
- live-activities-schedule
- market-operations
- multicast
- disaster-recovery
- colocation
title: Discontinuation of Additional Multicast Streams for Equity Derivatives Segment
  from Disaster Recovery Site
---

## Summary

BSE (Notice No. 20260616-21) announces the immediate discontinuation of additional multicast streams for the Equity Derivatives (EDX) segment from its Disaster Recovery (DR) site. These streams were originally introduced in December 2024 (Notice 20241221-2) to mitigate frequent packet drops experienced by members trading from DR. Following network optimisation by the Exchange, packet drop rates on existing streams are now comparable to those on the additional streams, making them redundant. Discontinuing the additional streams also reduces unnecessary bandwidth consumption at the Exchange.

## Key Points

- Additional multicast streams for the EDX segment from DR site are discontinued with **immediate effect**.
- The streams will not be available in future DR mock sessions or live trading from DR.
- The original reason for the streams — high packet drops on existing DR multicast — has been resolved through Exchange network optimisation.
- The discontinued streams were available exclusively in the **colocation center**.
- **Existing multicast stream IPs and ports remain unchanged** and are common for both Primary (PR) and Disaster Recovery (DR) sites.

## Regulatory Changes

No regulatory rule changes. This is an operational infrastructure update by BSE Trading Operations.

## Compliance Requirements

- Members using the additional multicast streams (Incremental Service A and Snapshot Service A) listed below must update their systems to stop subscribing to the discontinued IPs/ports:

| Partition | Incremental Service A (IP / Port) | Snapshot Service A (IP / Port) |
|-----------|----------------------------------|--------------------------------|
| 1 | 238.0.0.84 / 15984 | 238.0.0.65 / 15965 |
| 2 | 238.0.0.66 / 15966 | 238.0.0.67 / 15967 |
| 3 | 238.0.0.68 / 15968 | 238.0.0.69 / 15969 |
| 4 | 238.0.0.70 / 15970 | 238.0.0.71 / 15971 |
| 5 | 238.0.0.72 / 15972 | 238.0.0.73 / 15973 |
| 6 | 238.0.0.74 / 15974 | 238.0.0.75 / 15975 |
| 7 | 238.0.0.76 / 15976 | 238.0.0.77 / 15977 |
| 8 | 238.0.0.78 / 15978 | 238.0.0.79 / 15979 |
| 9 | 238.0.0.80 / 15980 | 238.0.0.81 / 15981 |
| 10 | 238.0.0.82 / 15982 | 238.0.0.83 / 15983 |

- Members should continue using the existing (unchanged) multicast streams for the EDX segment from both PR and DR sites.

## Important Dates

- **Effective Date:** Immediate (16 June 2026)
- **Reference Notice:** 20241221-2 dated 21 December 2024 (original introduction of the additional streams)

## Impact Assessment

Impact is limited to colocation members who subscribed to the additional multicast streams for the EDX segment during DR operations. These members need to reconfigure their feed handlers to drop the discontinued IPs. Members relying solely on the standard/existing multicast streams are unaffected. The change reduces bandwidth overhead at the Exchange and simplifies the multicast topology for DR scenarios. No trading disruption is expected as the existing streams continue to function normally.