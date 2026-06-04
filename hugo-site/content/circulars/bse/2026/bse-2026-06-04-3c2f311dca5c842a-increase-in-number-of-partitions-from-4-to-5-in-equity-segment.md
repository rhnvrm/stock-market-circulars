---
category: trading
circular_id: 3c2f311dca5c842a
date: '2026-06-04'
description: BSE will increase the number of partitions in the Equity segment from
  4 to 5 effective June 15, 2026. Trading members using ETI-based applications, EMDI,
  or EOBI must update their systems to handle the new partition.
draft: false
guid: https://www.bseindia.com/downloads/UploadDocs/Notices/20260604-6/20260604-6.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational/technical change affecting trading members' ETI, EMDI,
  and EOBI applications; requires system updates before June 15, 2026 go-live but
  does not directly affect securities prices or corporate actions.
pdf_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260604-6/20260604-6.pdf
processing:
  attempts: 1
  content_hash: 528f733394fd2698
  processed_at: '2026-06-04T15:20:16.715006'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-04T10:01:24+00:00'
rss_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260604-6/20260604-6.pdf
severity: medium
source: bse
stocks: []
tags:
- equity-segment
- trading
- partition
- eti
- emdi
- eobi
- mock-trading
- market-data
- trading-technology
- bse
title: 'BSE Equity Segment: Partition Count Increasing from 4 to 5 Effective June
  15, 2026'
---

## Summary

BSE has announced that the number of partitions in the Equity segment will increase from 4 to 5, effective **June 15, 2026**. Each partition handles a set of products, and from the effective date all trading will be conducted across 5 partitions. A mock trading session is scheduled for **June 13, 2026** to allow members to test their updated systems.

## Key Points

- Partition count in the Equity segment increases from 4 to 5 effective June 15, 2026.
- Partition details are available in the Equity master file (`BSE_EQ_SCRIP_DDMMYY.csv`) under column 56 (`UnqPdctIdr`), formatted as `partition_id-product_id` (e.g., `4-261`).
- The number of partitions is also included in the Session Logon Response (Template ID 10001) under field `NoOfPartition (1770)` in the ETI API.
- Partition 5 has been available in the Simulation environment since April 4, 2026.
- The Exchange will gradually move certain products from existing partitions to the new Partition 5; any reassignment will be reflected in the master file.
- BOLTPLUS Configuration file version 1.17 (attached) provides details on partition-wise multicast streams for EMDI and EOBI; also available at www.bseindia.com/nta.aspx.

## Regulatory Changes

No new regulatory rule is introduced. This is an infrastructure change to the BSE trading platform expanding the Equity segment from 4 to 5 partitions to accommodate product growth.

## Compliance Requirements

- **ETI-based applications**: Must be updated to query 5 partitions (instead of 4) for retransmission of orders, trades, or other partition-oriented messages.
- **EMDI/EOBI applications**: Must be updated to handle product movements between partitions, as market data for a product will only be available from the multicast stream of its assigned partition.
- Members should review the BOLTPLUS Configuration file v1.17 for updated partition-wise multicast stream details.
- For queries, contact IML Tech Support at 22728053 or bse.tech@bseindia.com.

## Important Dates

| Date | Event |
|------|-------|
| April 4, 2026 | Partition 5 available in Simulation environment (already live) |
| June 13, 2026 | Mock trading session to test 5-partition setup |
| June 15, 2026 | Go-live: Equity segment operates on 5 partitions |

## Impact Assessment

This change is primarily operational and technical, affecting trading members who use ETI APIs, EMDI, or EOBI-based market data applications. Firms that do not update their systems before June 15, 2026 risk missing orders, trades, or market data for products reassigned to Partition 5. The mock session on June 13 provides a testing window. No direct impact on end investors or securities valuations; impact is limited to the technology infrastructure of trading members.