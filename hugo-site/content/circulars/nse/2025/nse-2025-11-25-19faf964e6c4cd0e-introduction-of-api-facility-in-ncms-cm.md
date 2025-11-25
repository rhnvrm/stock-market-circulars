---
category: market-operations
circular_id: 19faf964e6c4cd0e
date: '2025-11-25'
description: NSE Clearing introduces API facility for NCMS-CM interface enabling trade
  download and actions inquiry for Capital Market segment members and custodians.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT71456.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: New technology infrastructure for members and custodians to access
  trade data via API. Operational enhancement rather than regulatory change. Voluntary
  adoption with UAT starting January 2026.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT71456.zip
processing:
  attempts: 1
  content_hash: e7fe4ddffd684cbb
  processed_at: '2025-11-25T12:46:20.166307'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-11-25T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT71456.zip
severity: medium
source: nse
stocks: []
tags:
- api
- ncms
- capital-market
- technology
- trade-download
- clearing
- members
- custodians
title: Introduction of API Facility in NCMS CM
---

## Summary

NSE Clearing Limited is introducing an API facility in the existing NCMS-CM (National Clearing Member System - Capital Market) interface for all members and custodians. The API will initially provide functionality for trade download and actions inquiry (modifications performed on CP trades) for the Capital Market segment. User Acceptance Testing (UAT) will be available from January 5, 2026.

## Key Points

- API facility being introduced for NCMS-CM interface for all members and custodians
- Initial functionality includes trade download and actions inquiry for Capital Market segment
- API specification document provided as annexure
- Protocol version 1.0 released on October 29, 2025
- Registration required via email to msd_clearing@nsccl.co.in with specific details
- Members need to provide: Primary Member Code/Custodian Code, Name, Email ID, Contact Number, and IP Address(es)
- HTTP-based API with token authentication mechanism
- Two main API endpoints: request/token and inquire/trd-act
- Support available via telephone (18002660050, IVR Option 2) and email

## Regulatory Changes

No regulatory changes. This is a technology infrastructure enhancement providing an alternative API-based method for members and custodians to access trade data and inquiry information.

## Compliance Requirements

- Members and custodians wanting to test the API facility must register by sending email to msd_clearing@nsccl.co.in
- Registration must include: Primary Member Code/Custodian Code, Member/Custodian Name, Email ID (Group ID preferred), Contact Number, and IP Address(es) from which API requests will be sent
- Members must refer to the attached API specification document for technical implementation details
- API consumers must follow security protocols including token-based authentication
- IP address whitelisting required for API access

## Important Dates

- **November 25, 2025**: Circular issued
- **January 5, 2026**: UAT (User Acceptance Testing) environment to be made available

## Impact Assessment

**Technology Impact**: Medium - This introduces modern API-based access to trade data, moving beyond traditional interface methods. Enables better automation and integration capabilities for members and custodians.

**Operational Impact**: Medium - Optional facility that provides additional channel for accessing trade information. Members can continue using existing methods while transitioning to API-based access.

**Member Impact**: Positive for members seeking automated trade data retrieval and inquiry capabilities. Requires technical implementation effort and IP address coordination.

**Market Impact**: Low to Medium - Enhances operational efficiency for clearing members and custodians but does not affect trading rules or market structure. Facilitates better data management and reconciliation processes.