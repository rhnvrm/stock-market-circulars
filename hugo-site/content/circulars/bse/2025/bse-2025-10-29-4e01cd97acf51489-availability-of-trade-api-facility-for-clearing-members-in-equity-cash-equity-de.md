---
category: trading
circular_id: 4e01cd97acf51489
date: '2025-10-29'
description: BSE introduces Trade API facility for Clearing Members to access trade
  inquiry data in Equity Cash and Equity Derivatives segments through token-based
  authorization.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={E7967237-70BB-4F52-AAA7-FBE6689DAB01}&noticeno=20251029-23&dt=10/29/2025&icount=23&totcount=60&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: This circular introduces a new technology infrastructure for Clearing
  Members to access trade data via API. While important for operational efficiency,
  it affects only Clearing Members and is an optional facility rather than a mandatory
  compliance requirement.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251029-23&attachedId=9e5d122e-a6e9-47f1-8f1d-2069a3dbedd0
processing:
  attempts: 1
  content_hash: 9dd788e91e74817f
  processed_at: '2025-10-29T18:46:32.652029'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-29T11:17:14+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={E7967237-70BB-4F52-AAA7-FBE6689DAB01}&noticeno=20251029-23&dt=10/29/2025&icount=23&totcount=60&flag=0
severity: medium
source: bse
stocks: []
tags:
- api-integration
- clearing-members
- derivatives
- equity-cash
- technology
- token-authorization
- trade-api
title: Availability of Trade API Facility for Clearing Members in Equity Cash & Equity
  Derivatives Segments
---

## Summary

BSE has launched Trade API facility (Version 1.0) for Clearing Members in Equity Cash and Equity Derivatives segments. The API enables Clearing Members to perform trade inquiries programmatically using token-based authorization. The system was released in October 2025 with initial market release date of October 28, 2025.

## Key Points

- New Trade API facility available for Clearing Members in Equity Cash and Equity Derivatives segments
- Token-based authorization system for secure API access
- API registration required before usage
- Login workflow includes token generation and validation process
- Trade inquiry functionality for retrieving trade data
- Separate response data structures for Equity and Equity Derivatives segments
- Version 1.0 released as initial market release

## Regulatory Changes

No regulatory changes. This is a new technology infrastructure offering.

## Compliance Requirements

- Clearing Members must complete API registration process before accessing the facility
- Members need to implement token-based authorization in their systems
- API integration must follow the specified structure and workflow:
  - Login handshake from Member to Exchange
  - Token generation request with proper validation
  - Use of generated token for trade inquiry requests
- Request headers and data fields must comply with specified format and validations

## Important Dates

- **October 28, 2025**: Initial Market Release
- **October 2025**: Documentation version 1.0 published

## Impact Assessment

**Operational Impact**: Clearing Members gain programmatic access to trade data, enabling automation of trade inquiry processes and improved operational efficiency. This facility allows for real-time data retrieval through API calls rather than manual processes.

**Technology Impact**: Members need to develop or update their systems to integrate with the new Trade API infrastructure, implement token-based authentication, and handle API responses for both Equity Cash and Equity Derivatives segments.

**Market Impact**: Low direct market impact as this is an operational tool for Clearing Members. The facility enhances technological capabilities but does not change trading rules or market structure. Adoption is voluntary and provides efficiency benefits to participating members.