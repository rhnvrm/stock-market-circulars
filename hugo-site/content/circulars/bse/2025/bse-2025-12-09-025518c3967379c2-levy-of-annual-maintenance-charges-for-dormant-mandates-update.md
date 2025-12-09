---
category: market-operations
circular_id: 025518c3967379c2
date: '2025-12-09'
description: BSE provides operating instructions for cancellation of dormant mandates
  on the StAR MF platform, including bulk upload process and reporting mechanisms.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={4C70AA34-9CE0-40E5-9D4E-DE7947CF8BED}&noticeno=20251209-25&dt=12/09/2025&icount=25&totcount=72&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational update affecting mutual fund distributors and members managing
  dormant mandates; impacts workflow but not immediate trading operations
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251209-25&attachedId=85ac1e26-4a21-4a54-8744-32bb47adf04c
processing:
  attempts: 1
  content_hash: f812a2701381a4a1
  processed_at: '2025-12-09T18:54:16.555257'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-09T12:30:21+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={4C70AA34-9CE0-40E5-9D4E-DE7947CF8BED}&noticeno=20251209-25&dt=12/09/2025&icount=25&totcount=72&flag=0
severity: medium
source: bse
stocks: []
tags:
- mutual-funds
- mandate-management
- star-mf
- npci
- dormant-mandates
- enach
- systematic-investment
title: Levy of Annual Maintenance Charges for Dormant Mandates - Update
---

## Summary

BSE has issued operating instructions for the cancellation of dormant mandates on the BSE StAR MF platform. Members can now cancel dormant mandates through a bulk upload facility, which will trigger cancellation requests to NPCI and subsequently to destination banks. The facility is available only for approved mandates with updated UMRN that have no XSIP/OTM registered against them.

## Key Points

- Dormant mandate cancellation facility available only for Physical/Scan/E-Mandate/ENACH mandate types
- Mandates must have updated UMRN and no XSIP/OTM registered against them
- Cancellation requests must be submitted via bulk upload in pipe-separated text file format
- Upon upload, mandate status changes to 'Cancelled by Member' with 'Dormant Mandate' remark
- Cancellation requests are routed through NPCI to client's destination bank
- Successfully cancelled mandates appear as 'REJECTED' status with 'Dormant Mandate' remark
- Cancelled mandates cannot be used for OTM payment or XSIP registration
- Failed cancellation requests revert mandate status to 'APPROVED' with blank remarks

## Regulatory Changes

No new regulatory changes. This circular provides operational guidelines for implementing dormant mandate cancellation on the BSE StAR MF platform.

## Compliance Requirements

**For Members:**
- Access dormant mandate data through: Admin >> Admin Reports >> Mandate Reports >> Dormant Mandate Details report
- Submit cancellation requests only through bulk upload facility at: Systematic Investment >> Mandate >> Dormant Mandate Upload
- Use specified file format: Client Code | Mandate ID (pipe-separated text file)
- Monitor mandate status through Mandate Details Report at: Systematic Investment >> Mandate >> Mandate Search

**File Format Requirements:**
- Format: Pipe separated text file (.txt)
- Fields: Client Code | Mandate ID

## Important Dates

No specific deadlines mentioned. The facility is currently available for eligible dormant mandates.

## Impact Assessment

**Operational Impact:**
- Streamlines dormant mandate management for mutual fund distributors and members
- Reduces maintenance burden by enabling systematic cancellation of unused mandates
- Provides clear audit trail through status updates and reporting mechanisms

**Process Impact:**
- Introduces mandatory bulk upload process (individual cancellation not permitted)
- Requires coordination between BSE StAR MF platform, NPCI, and destination banks
- Cancelled mandates permanently unavailable for future transactions

**Member Impact:**
- Members can proactively manage dormant mandates to avoid maintenance charges
- Clear visibility of cancellation status through existing reporting infrastructure
- Failed cancellation requests automatically revert to approved status