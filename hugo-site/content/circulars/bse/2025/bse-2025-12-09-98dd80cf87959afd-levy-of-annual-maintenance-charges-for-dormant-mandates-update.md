---
category: market-operations
circular_id: 98dd80cf87959afd
date: '2025-12-09'
description: BSE provides operational instructions for cancellation of dormant mandates
  on the BSE StAR MF platform, including pre-requisites, process flow, and reporting
  mechanisms.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={4C70AA34-9CE0-40E5-9D4E-DE7947CF8BED}&noticeno=20251209-25&dt=12/09/2025&icount=25&totcount=71&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational update affecting mutual fund distributors and members using
  BSE StAR MF platform for mandate management. Impacts dormant mandate handling but
  does not affect active trading or listing activities.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251209-25&attachedId=85ac1e26-4a21-4a54-8744-32bb47adf04c
processing:
  attempts: 1
  content_hash: 71f3bc8623b63ae2
  processed_at: '2025-12-09T15:49:42.225553'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-09T12:30:21+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={4C70AA34-9CE0-40E5-9D4E-DE7947CF8BED}&noticeno=20251209-25&dt=12/09/2025&icount=25&totcount=71&flag=0
severity: medium
source: bse
stocks: []
tags:
- mutual-funds
- mandate-management
- bse-star-mf
- npci
- operational-procedures
- dormant-mandates
- enach
- systematic-investment
title: Levy of Annual Maintenance Charges for Dormant Mandates - Update
---

## Summary

BSE has issued operating instructions for the cancellation of dormant mandates on the BSE StAR MF platform. The facility allows members to cancel approved mandates that have no XSIP/OTM registered against them through a bulk upload process. The cancellation requests are processed through NPCI and reflected in the platform's reporting system.

## Key Points

- Mandate cancellation facility available only for approved mandates with updated UMRN and no XSIP/OTM registered
- Facility applicable to Physical/Scan/E-Mandate/ENACH mandate types only
- Cancellation requests must be submitted via bulk upload in pipe-separated text file format
- Cancelled mandates display status as 'REJECTED' with remark 'Dormant Mandate'
- Once cancelled, mandates cannot be used for OTM payment and XSIP registration
- If NPCI rejects cancellation request, mandate status reverts to APPROVED
- Dormant mandate data accessible via Admin >> Admin Reports >> Mandate Reports >> Dormant Mandate Details report

## Regulatory Changes

No new regulatory changes introduced. This circular provides operational guidelines for implementing dormant mandate cancellation facility on BSE StAR MF platform.

## Compliance Requirements

**For Members:**
- Access dormant mandate data through member login path: Admin >> Admin Reports >> Mandate Reports >> Dormant Mandate Details report
- Submit cancellation requests only through bulk upload facility at: Systematic Investment >> Mandate >> Dormant Mandate Upload
- Use prescribed file format: pipe-separated text file (.txt) with Client Code and Mandate ID
- Monitor mandate status updates in Mandate Detail Report after NPCI processing
- Ensure cancelled mandates are not used for OTM payments or XSIP registrations

**File Format Requirements:**
- Format: Client Code | Mandate ID
- File Type: Pipe separated Text file (.txt)
- Example: Test01|477995

## Important Dates

No specific deadlines mentioned. The facility is operational and available for use by members.

## Impact Assessment

**Operational Impact:**
- Streamlines management of dormant mandates on BSE StAR MF platform
- Reduces clutter of inactive mandates in the system
- Provides systematic process for mandate lifecycle management

**Member Impact:**
- Members must use bulk upload process for dormant mandate cancellations
- Requires monitoring of mandate status updates post-NPCI processing
- Failed cancellation requests will revert mandate status to APPROVED

**System Impact:**
- Mandate status workflow: APPROVED → Cancelled by Member → REJECTED (with Dormant Mandate remark)
- Integration with NPCI for cancellation request processing
- Automated status updates in Mandate Detail Report accessible via Systematic Investment >> Mandate >> Mandate Search