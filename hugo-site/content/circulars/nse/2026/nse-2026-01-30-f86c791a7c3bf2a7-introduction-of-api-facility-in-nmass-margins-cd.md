---
category: market-operations
circular_id: f86c791a7c3bf2a7
date: '2026-01-30'
description: NSE Clearing introduces Web API protocol for members to access margin
  and position data programmatically in Currency Derivatives segment through NMASS
  system.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CD72540.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technology enhancement enabling programmatic access to margin data
  for CD segment members, improving operational efficiency but not mandating immediate
  action
pdf_url: https://nsearchives.nseindia.com/content/circulars/CD72540.zip
processing:
  attempts: 1
  content_hash: 32cc5b27daa49b5c
  processed_at: '2026-01-30T13:10:06.300063'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-30T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CD72540.zip
severity: medium
source: nse
stocks: []
tags:
- api
- nmass
- margins
- currency-derivatives
- technology
- clearing
- web-api
- automation
title: Introduction of API Facility in NMASS-Margins-CD
---

## Summary

NSE Clearing Limited has introduced a Web API facility for members in the Currency Derivatives (CD) segment to access margin and position data programmatically through the NMASS (NSE Member Accounting and Settlement System) platform. This API protocol (Version 1.0) enables automated retrieval of critical clearing and settlement information including CM margins, TM margins, client margins, positions, margin obligations, and member-wise position limits.

## Key Points

- Web API facility launched for Currency Derivatives (CD) segment members
- API protocol version 1.0 released on January 20, 2026
- Enables programmatic access to margin and position data from NMASS system
- Supports multiple API endpoints for different margin types and position data
- Requires API consumer registration and token-based authentication
- Available for FO (Futures & Options), CD (Currency Derivatives), and CO (Commodity Derivatives) segments
- APIs include: token generation, CM margins, TM margins, client margins, positions, margin obligations (MOI), and member-wise position limits (MWPL)

## Regulatory Changes

No regulatory changes mandated. This is a technology enhancement providing an additional channel for members to access existing margin and position information that was previously available only through the web interface.

## Compliance Requirements

- Members wishing to use the API facility must complete API consumer registration
- Implement token-based authentication security protocol as specified
- Follow API security guidelines provided by NSE Clearing
- Adhere to HTTP status codes and error response handling protocols
- Use designated segment environment endpoints for API calls
- Maintain confidentiality of API credentials and access tokens

## Important Dates

- January 20, 2026: Initial version (1.0) of API protocol documentation released
- January 30, 2026: Circular notification date
- No specific implementation deadline specified - adoption is voluntary

## Impact Assessment

**Operational Impact:** Medium positive impact on members' operational efficiency by enabling automated margin monitoring and position tracking. Reduces manual effort in accessing NMASS data and allows integration with members' internal systems for real-time margin management.

**Market Impact:** Low direct market impact as this is an infrastructure enhancement. Indirectly benefits market participants through improved risk management capabilities and faster response times to margin requirements.

**Technology Impact:** Members can now build automated workflows for margin calculation verification, position reconciliation, and risk monitoring. Particularly beneficial for high-frequency trading firms and large brokers managing multiple client accounts.

**Adoption:** Voluntary adoption - existing web-based access remains available. API facility provides additional flexibility for technologically advanced members.