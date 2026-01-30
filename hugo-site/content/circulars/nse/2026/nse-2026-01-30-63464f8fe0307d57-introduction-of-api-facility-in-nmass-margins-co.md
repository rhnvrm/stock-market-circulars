---
category: market-operations
circular_id: 63464f8fe0307d57
date: '2026-01-30'
description: NSE Clearing introduces Web API protocol for members to access margin
  information programmatically in the Currency Derivatives (CO) segment through NMASS
  system.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/COM72541.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technology enhancement for clearing members to access margin data via
  API in CO segment. Improves operational efficiency but does not affect trading rules
  or market structure.
pdf_url: https://nsearchives.nseindia.com/content/circulars/COM72541.zip
processing:
  attempts: 1
  content_hash: 585524d595815bb5
  processed_at: '2026-01-30T13:09:45.293314'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-30T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/COM72541.zip
severity: medium
source: nse
stocks: []
tags:
- api
- nmass
- margins
- currency-derivatives
- co-segment
- technology
- member-services
- clearing
- web-api
title: Introduction of API Facility in NMASS-Margins-CO
---

## Summary

NSE Clearing Limited has introduced a Web API facility for clearing members to programmatically access margin-related information in the Currency Derivatives (CO) segment through the NMASS (NSE Margin and Settlement System). This protocol document (Version 1.0, dated January 20, 2026) provides technical specifications for API integration, including authentication mechanisms, endpoint definitions, and data formats for retrieving various margin and position reports.

## Key Points

- Web API protocol enables programmatic access to NMASS margin data for CO segment
- API supports multiple margin reports: CM (Clearing Member) margins, TM (Trading Member) margins, CLI (Client) margins
- Additional APIs available for positions, MOI (Margin Obligation Information), and MWPL (Member-wise Position Limits)
- Token-based authentication mechanism with HTTP status code responses
- API consumers must register before accessing the services
- Comprehensive error handling with standardized HTTP status codes and response formats
- Segment-specific environment details provided for FO, CD, and CO segments

## Regulatory Changes

No regulatory changes are introduced. This is a technological enhancement to existing margin reporting infrastructure, providing an alternative API-based method for members to access margin information that was previously available only through web interface.

## Compliance Requirements

- Clearing members intending to use the API facility must complete API Consumer Registration
- Members must implement proper API security protocols as specified in the documentation
- Authentication tokens must be obtained using the POST /<version>/request/token endpoint before accessing other APIs
- Members must handle HTTP status codes and error responses appropriately in their integration
- Confidentiality requirements apply - API protocols and documentation are proprietary to NSE Clearing Limited

## Important Dates

- January 20, 2026: Initial version (1.0) of the API protocol document released
- January 30, 2026: Circular date
- No specific implementation deadline mentioned in the circular

## Impact Assessment

**Operational Impact:** Positive operational impact for clearing members who can now automate margin data retrieval and integrate it with their internal systems. This reduces manual processes and enables real-time programmatic access to critical margin information.

**Technology Impact:** Requires members to develop or modify their systems to integrate with the new API endpoints. Members using automated risk management or margin monitoring systems will benefit from direct API access.

**Market Impact:** No direct market impact. This is an infrastructure enhancement that improves efficiency for clearing members without changing margin calculation methodologies or trading rules.

**Segment Scope:** Currently applies to Currency Derivatives (CO) segment, though similar API facilities are referenced for FO (Futures & Options) and CD (Currency Derivatives) segments, indicating broader API infrastructure rollout.