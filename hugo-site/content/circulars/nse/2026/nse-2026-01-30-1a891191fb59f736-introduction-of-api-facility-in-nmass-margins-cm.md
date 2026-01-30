---
category: market-operations
circular_id: 1a891191fb59f736
date: '2026-01-30'
description: NSE introduces Web API facility for members to access margin-related
  data for CM and SLB segments through NMASS (NSE Margin Administration and Surveillance
  System).
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT72538.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical enhancement enabling API-based access to margin data for
  trading members. Improves operational efficiency but does not affect trading rules
  or market participants directly.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT72538.zip
processing:
  attempts: 1
  content_hash: cb1c768c28218aa6
  processed_at: '2026-01-30T15:47:12.334983'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-30T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT72538.zip
severity: medium
source: nse
stocks: []
tags:
- api
- margins
- technology
- clearing
- cm-segment
- slb-segment
- nmass
- web-api
- integration
title: Introduction of API Facility in NMASS-Margins-CM
---

## Summary

NSE Clearing Limited has introduced a Web API facility for members to access margin-related information for the Cash Market (CM) and Securities Lending and Borrowing (SLB) segments through NMASS (NSE Margin Administration and Surveillance System). This API-based system allows members to programmatically retrieve various margin calculations including CM margins, TM margins, CLI margins, security margins, and settlement margins.

## Key Points

- Web API Protocol Version 1.0 released for Margin Equities (CM/SLB)
- API enables retrieval of five types of margin data: CM margins, TM margins, CLI margins, security margins, and settlement margins
- Token-based authentication system for API security
- Members need to register as API consumers before accessing the facility
- Separate environment details provided for CM and SLB segments
- HTTP-based RESTful API with standard status codes and error responses
- Protocol documented with version 1.0 dated January 22, 2026

## Regulatory Changes

This is a new technological facility being introduced. No changes to existing margin calculation rules or regulatory requirements. The API provides programmatic access to existing margin data that was previously available through other interfaces.

## Compliance Requirements

- Members must complete API Consumer Registration process
- Members must implement API security protocols as specified
- Token-based authentication required for all API requests
- Members must adhere to the specified HTTP protocol and request/response formats
- Confidentiality of API credentials and proprietary information must be maintained

## Important Dates

- Protocol Version 1.0 Initial Release: January 22, 2026
- Circular Date: January 30, 2026

## Impact Assessment

**Operational Impact:** Medium - Trading and clearing members can now automate margin data retrieval through API integration, improving operational efficiency and reducing manual processes. This enables better integration with members' internal risk management systems.

**Technical Impact:** Members with technical infrastructure can leverage this API for real-time margin monitoring and automated reconciliation processes. Requires development effort for API integration.

**Market Impact:** Low direct market impact as this is an infrastructure enhancement. Indirect benefits include improved risk monitoring capabilities for members and potential reduction in margin-related queries and disputes.