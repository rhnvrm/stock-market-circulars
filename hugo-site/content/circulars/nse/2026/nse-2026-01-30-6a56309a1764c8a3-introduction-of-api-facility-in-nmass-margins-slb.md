---
category: market-operations
circular_id: 6a56309a1764c8a3
date: '2026-01-30'
description: NSE introduces Web API facility for members to access margin data for
  CM and SLB segments through NMASS system.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT72542.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technology enhancement for margin data access affecting trading members
  using CM and SLB segments, but not market-wide regulatory change
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT72542.zip
processing:
  attempts: 1
  content_hash: f082ac5ccb717f59
  processed_at: '2026-01-30T13:09:21.265282'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-30T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT72542.zip
severity: medium
source: nse
stocks: []
tags:
- api
- margins
- slb
- cm-segment
- nmass
- technology
- clearing
- web-api
title: Introduction of API Facility in NMASS- Margins-SLB
---

## Summary

NSE Clearing Limited has introduced a Web API facility for members to access margin-related data for Capital Market (CM) and Securities Lending and Borrowing (SLB) segments through the NMASS (NSE Margin And Settlement System) platform. This protocol document version 1.0, dated January 22, 2026, provides technical specifications for API integration including authentication, security protocols, and available endpoints for margin queries.

## Key Points

- Web API facility enables programmatic access to margin data for CM and SLB segments
- Protocol version 1.0 released with initial implementation dated January 22, 2026
- API supports multiple margin query types: CM margins, TM margins, CLI margins, security margins, and settlement margins
- Token-based authentication system for API security
- Requires API consumer registration before access
- HTTP-based REST API with JSON request/response format
- Includes standardized error codes and response structures

## Regulatory Changes

No regulatory changes. This is a technology infrastructure enhancement to provide members with API-based access to existing margin data that was previously available only through traditional interfaces.

## Compliance Requirements

- Members must register as API consumers before accessing the facility
- API security protocols must be followed including token-based authentication
- Members need to implement the specified HTTP endpoints and handle standard response codes
- Confidentiality requirements apply to API documentation and implementation

## Important Dates

- January 22, 2026: Initial version 1.0 of API protocol released
- January 30, 2026: Circular publication date

## Impact Assessment

This technology enhancement provides trading members with automated, programmatic access to margin data, enabling better integration with internal systems and real-time margin monitoring capabilities. The impact is primarily operational, improving efficiency for members who choose to implement the API. There is no mandatory requirement or market-wide impact, making this a medium-impact technology upgrade focused on facilitating member operations in CM and SLB segments.