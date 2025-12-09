---
category: market-operations
circular_id: 7a0807eacd74def8
date: '2025-12-09'
description: BSE provides operating instructions for cancellation of dormant mandates
  on BSE StAR MF platform, including eligibility criteria, bulk upload process, and
  NPCI integration for mandate cancellation.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={4C70AA34-9CE0-40E5-9D4E-DE7947CF8BED}&noticeno=20251209-25&dt=12/09/2025&icount=25&totcount=25&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Provides operational guidelines for dormant mandate cancellation affecting
  mutual fund distributors and members using BSE StAR MF platform. Medium impact as
  it pertains to administrative processes rather than trading or compliance deadlines.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251209-25&attachedId=85ac1e26-4a21-4a54-8744-32bb47adf04c
processing:
  attempts: 1
  content_hash: b68899ff146440ac
  processed_at: '2025-12-09T12:49:30.210031'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-09T12:30:21+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={4C70AA34-9CE0-40E5-9D4E-DE7947CF8BED}&noticeno=20251209-25&dt=12/09/2025&icount=25&totcount=25&flag=0
severity: medium
source: bse
stocks: []
tags:
- mutual-funds
- mandate-management
- dormant-mandates
- bse-star-mf
- npci
- systematic-investment
- xsip
- enach
title: Levy of Annual Maintenance Charges for Dormant Mandates - Operating Instructions
  Update
---

## Summary

BSE has issued detailed operating instructions for the cancellation of dormant mandates on the BSE StAR MF platform. The circular outlines the eligibility criteria, cancellation process through bulk upload, NPCI integration for mandate cancellation, and reporting mechanisms. Members can now cancel approved dormant mandates that have no active XSIP/OTM registrations using a designated bulk upload facility.

## Key Points

- Dormant mandate cancellation facility available only for approved mandates with updated UMRN and no XSIP/OTM registered
- Facility applicable for Physical/Scan/E-Mandate/ENACH mandate types only
- Dormant mandate data accessible via Admin >> Admin Reports >> Mandate Reports >> Dormant Mandate Details report
- Cancellation requests must be submitted through bulk upload only (pipe-separated text file format)
- Upon upload, mandate status changes to 'Cancelled by Member' with remark 'Dormant Mandate'
- Cancellation request routed to NPCI and then to client's destination bank
- Final status reflected as 'REJECTED' with remark 'Dormant Mandate' after NPCI confirmation
- Cancelled mandates cannot be used for OTM payment and XSIP registration
- If NPCI rejects cancellation request, mandate status reverts to 'APPROVED' with blank remark

## Regulatory Changes

No new regulatory changes introduced. This circular provides operational implementation guidelines for the previously announced annual maintenance charges for dormant mandates.

## Compliance Requirements

- Members must use designated bulk upload path: Systematic Investment >> Mandate >> Dormant Mandate Upload
- File must be in pipe-separated text format (.txt) with structure: Client Code | Mandate ID
- Members can only cancel mandates meeting eligibility criteria (approved, updated UMRN, no active XSIP/OTM)
- Members must monitor mandate status changes through Mandate Detail Report at: Systematic Investment >> Mandate >> Mandate Search
- Once cancelled, mandates cannot be reused for OTM payments or XSIP registrations

## Important Dates

No specific dates or deadlines mentioned in this circular. The facility is now available for use by members.

## Impact Assessment

**Operational Impact:** Medium - Members and distributors using BSE StAR MF platform need to implement new workflow for dormant mandate management. The bulk upload process requires system integration and monitoring of mandate status changes through multiple report paths.

**Market Impact:** Low - This is an administrative process affecting backend mandate management rather than direct trading or investment activities.

**Technology Impact:** Medium - Members need to ensure their systems can generate pipe-separated text files in the prescribed format and integrate with the NPCI cancellation workflow. Status reconciliation processes must be established to handle both successful and failed cancellation requests.

**Client Impact:** Low to Medium - Clients with dormant mandates will see these cancelled, potentially requiring re-registration if they wish to resume systematic investments. However, this helps clean up inactive mandates and reduces maintenance charges.