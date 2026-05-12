---
category: market-operations
circular_id: 2c568690d86c7e05
date: '2026-05-12'
description: NSE Clearing Limited has released Version 1.0 of the Web API Protocol
  for the NCMS (National Clearing Management System) in the Currency Derivatives Segment,
  detailing authentication, trade activity inquiry, and approval/rejection endpoints
  for member integration.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CD74170.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical API documentation update relevant to clearing members operating
  in the Currency Derivatives segment; operational impact is medium as it enables/mandates
  use of NCMS Web API for trade activity management, but is not a regulatory or compliance
  mandate with immediate market-wide impact.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CD74170.zip
processing:
  attempts: 1
  content_hash: a7f8f8482a833f96
  processed_at: '2026-05-12T14:34:14.468170'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-12T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CD74170.zip
severity: low
source: nse
stocks: []
tags:
- ncms
- currency-derivatives
- web-api
- nse-clearing
- clearing-members
- technical-specifications
- api-integration
- cd-segment
title: NSE Clearing NCMS Web API Protocol Version 1.0 for Currency Derivatives Segment
---

## Summary

NSE Clearing Limited (NCL) has published Version 1.0 of the Web API Protocol for the NCMS (National Clearing Management System) in the Currency Derivatives (CD) Segment. The document, initially released on 13-Apr-2026, defines the technical specifications for member integration with NCL's clearing systems via HTTP-based REST APIs, covering authentication, trade activity inquiries, and approval/rejection workflows.

## Key Points

- Version 1.0 of the NCMS Web API Protocol for the CD Segment has been released by NSE Clearing Limited.
- The API supports token-based authentication via `POST /<version>/request/token`.
- Members can query trade activity using `POST /<version>/inquire/trd-act`.
- Approval and rejection of requests are handled via `POST /<version>/request/approval-rejection`.
- Counterparty (CP) modification is supported through `POST /<version>/request/cp-modification`.
- Bulk approval of all pending requests is available via `POST /<version>/request/approve-all`.
- The document includes HTTP status codes, common error response JSON structures, environment details, and API consumer registration procedures.
- Reference codes for Market Type, Market Status, Transaction Code, Activity Type, Book Type, Client Type, and Buy/Sell Flag are provided in Appendix A.

## Regulatory Changes

This circular introduces formal API documentation for the NCMS facility in the Currency Derivatives Segment. It standardizes the programmatic interface through which clearing members interact with NSE Clearing's systems for trade activity management, replacing or supplementing earlier manual or proprietary access methods.

## Compliance Requirements

- Clearing members intending to use the NCMS Web API in the CD Segment must register as API consumers as per the registration procedure outlined in the document.
- Members must implement token-based API security as described in the API Security section.
- All API interactions must conform to the specified request/response JSON schemas and HTTP status code handling.
- Members must use the reference codes provided in Appendix A for correct field values in API requests.

## Important Dates

- **13-Apr-2026**: Initial release of NCMS Web API Protocol Version 1.0 for CD Segment.
- **2026-05-12**: Circular update published by NSE regarding the NCMS API facility.

## Impact Assessment

This update primarily affects clearing members active in the Currency Derivatives Segment who wish to integrate programmatically with NSE Clearing's NCMS system. The Web API enables automation of trade activity inquiries, approvals, rejections, and CP modifications, improving operational efficiency for members. There is no direct impact on trading strategies or market pricing. Members not yet using the API should evaluate integration requirements and initiate API consumer registration. The release of Version 1.0 suggests this is a new or significantly updated facility, and members should review the full protocol document to ensure compliance with the new interface standards.