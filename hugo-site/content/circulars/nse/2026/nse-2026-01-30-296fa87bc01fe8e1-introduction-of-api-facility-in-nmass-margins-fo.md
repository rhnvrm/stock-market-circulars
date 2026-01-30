---
category: market-operations
circular_id: 296fa87bc01fe8e1
date: '2026-01-30'
description: NSE introduces Web API protocol for members to access margin and position
  data in Derivatives segments (FO/CD/CO) through NMASS system.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT72539.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical enhancement enabling programmatic access to margin and position
  data for clearing and trading members in derivatives segments, improving operational
  efficiency but not mandating immediate changes to existing workflows
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT72539.zip
processing:
  attempts: 1
  content_hash: 50c9e84d84d2e504
  processed_at: '2026-01-30T15:45:32.085323'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-30T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT72539.zip
severity: medium
source: nse
stocks: []
tags:
- api
- margins
- derivatives
- fo-segment
- cd-segment
- co-segment
- technology
- clearing
- nmass
- trading-members
- clearing-members
title: Introduction of API Facility in NMASS-Margins-FO
---

## Summary

NSE Clearing Limited has released Protocol Version 1.0 for Web API access to the NMASS (NSE Margin Administration and Surveillance System) for Margin Derivatives segments. This API facility allows clearing members and trading members to programmatically access margin requirements, positions, and surveillance data for FO (Futures & Options), CD (Currency Derivatives), and CO (Commodity Derivatives) segments through secure RESTful APIs.

## Key Points

- Web API protocol introduced for NMASS-Margins in Derivatives segments (FO/CD/CO)
- Seven API endpoints provided: token generation, CM margins, TM margins, CLI margins, positions, MOI (Margin Obligation Information), and MWPL (Market Wide Position Limit)
- APIs support both clearing member and trading member level data access
- Token-based authentication mechanism for API security
- HTTP status codes and standardized error response JSON format for error handling
- Separate environment details provided for FO, CD, and CO segments
- API consumer registration required before access
- Version 1.0 released on January 20, 2026

## Regulatory Changes

No regulatory changes mandated. This is a technical infrastructure enhancement providing an additional channel for members to access existing margin and position data that is already available through traditional interfaces.

## Compliance Requirements

- Members wishing to use the API facility must complete API Consumer Registration process
- Members must implement proper API security protocols as outlined in the documentation
- Authentication tokens must be obtained using the POST /<version>/request/token endpoint before accessing other APIs
- Members must handle HTTP status codes and error responses appropriately in their implementations
- API access credentials and tokens must be kept confidential and secure

## Important Dates

- **January 20, 2026**: Protocol Version 1.0 initial release date
- **January 30, 2026**: Circular publication date
- No specific implementation deadline mentioned - adoption is voluntary

## Impact Assessment

**Operational Impact**: Medium - This API facility provides clearing members and trading members with programmatic access to critical margin and position data, enabling automation of margin monitoring, risk management, and compliance processes. Members can integrate this data into their internal systems for real-time monitoring.

**Technology Impact**: Members with technical capabilities can develop automated systems to retrieve CM margins, TM margins, client-level margins, positions, margin obligations, and MWPL data. This reduces manual effort and enables faster decision-making.

**Market Impact**: Low direct market impact as this is an optional technical enhancement. However, it may improve overall risk management efficiency for members who adopt the API facility.

**Segment Coverage**: Applies to Futures & Options (FO), Currency Derivatives (CD), and Commodity Derivatives (CO) segments with separate environment configurations for each.