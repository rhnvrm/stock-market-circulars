---
category: trading
circular_id: 5ef2488e448a30e4
date: '2026-05-15'
description: BSE mandates upgrade to ETI API version 1.6.14 for trading system enhancements
  across Equity, Equity Derivatives, Currency Derivatives, and Commodity Derivatives
  segments, with live trading rollout in June 2026.
draft: false
guid: https://www.bseindia.com/downloads/UploadDocs/Notices/20260515-36/20260515-36.pdf
impact: high
impact_ranking: high
importance_ranking: high
justification: Mandatory API upgrade affecting all trading members across multiple
  segments with specific compliance deadlines; non-compliance could disrupt trading
  operations.
pdf_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260515-36/20260515-36.pdf
processing:
  attempts: 1
  content_hash: 2263d59ec35c803c
  processed_at: '2026-05-15T16:56:45.771033'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-15T14:24:11+00:00'
rss_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260515-36/20260515-36.pdf
severity: high
source: bse
stocks: []
tags:
- api
- eti-api
- trading-system
- equity
- equity-derivatives
- currency-derivatives
- commodity-derivatives
- mandatory-release
- trading-members
- system-upgrade
title: BSE ETI API Version 1.6.14 Mandatory Release - Trading System Enhancements
---

## Summary

BSE has released ETI API version 1.6.14 as a mandatory upgrade for trading members operating in Equity, Equity Derivatives, Currency Derivatives, and Commodity Derivatives segments. All third-party trading application vendors and members with in-house trading applications must implement the new API changes before the respective go-live dates in June 2026.

## Key Points

- New ETI API version 1.6.14 is now available on the BSE website (http://www.bseindia.com/nta.aspx)
- New field: Algo ID added to order and quote mass cancellation messages
- New error code introduced for debarred clients
- Revised identification methodology for Location ID
- Simulation testing environment available from Tuesday, May 26, 2026
- Both third-party vendors and in-house development teams must update their trading applications

## Regulatory Changes

- Introduction of Algo ID field in mass cancellation messages enhances algorithmic order tracking and audit capability
- New debarred client error code strengthens compliance enforcement at the API level
- Revised Location ID identification improves system-level member/location tracking

## Compliance Requirements

- All trading members must review the new API documentation available at http://www.bseindia.com/nta.aspx
- Third-party trading application vendors must incorporate API v1.6.14 changes into their platforms
- Members with in-house developed trading applications must complete necessary system development
- Testing in the simulation environment should be completed before respective go-live dates
- Contact BSE Tech Team for clarifications: bse.tech@bseindia.com or 022-2272-8053

## Important Dates

- **May 15, 2026**: Notice issued; ETI API v1.6.14 made available
- **May 26, 2026 (Tuesday)**: Simulation/testing environment available for the new API
- **June 20, 2026 (Saturday)**: Mock trading for Equity segment
- **June 22, 2026 (Monday)**: Live trading go-live for Equity segment
- **June 27, 2026 (Saturday)**: Mock trading for Equity Derivatives, Currency Derivatives & Commodity Derivatives
- **June 29, 2026 (Monday)**: Live trading go-live for Equity Derivatives, Currency Derivatives & Commodity Derivatives segments

## Impact Assessment

This is a mandatory release affecting all trading members and their technology vendors across four major market segments. Failure to implement the API changes by the respective deadlines will likely result in trading disruptions or inability to connect to BSE's trading system. The staggered rollout (Equity first, then Derivatives) provides some buffer, but firms operating across all segments must manage two separate upgrade milestones within the same week. The addition of Algo ID to mass cancellation messages is particularly significant for algorithmic trading firms as it introduces new mandatory field handling.