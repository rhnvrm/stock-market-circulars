---
category: market-operations
circular_id: 1fc7d4c8967cf510
date: '2026-06-17'
description: BSECL (formerly ICCL) introduces an optional facility in RTRMS enabling
  Clearing Members to monitor intraday uncrystallised MTM losses at the Trading Member
  level for open futures positions.
draft: false
guid: https://www.bseindia.com/downloads/UploadDocs/Notices/20260617-36/20260617-36.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational update introducing an optional monitoring tool for Clearing
  Members in the derivatives segment. No mandatory compliance changes; impacts only
  those who opt in to the MTM loss monitoring facility.
pdf_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260617-36/20260617-36.pdf
processing:
  attempts: 1
  content_hash: 4b1b0bacfd9cf6f4
  processed_at: '2026-06-17T15:38:56.459212'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-17T14:12:50+00:00'
rss_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260617-36/20260617-36.pdf
severity: medium
source: bse
stocks: []
tags:
- futures-and-options
- margins
- rtrms
- mtm
- clearing-member
- trading-member
- derivatives
- risk-management
- settlement-operations
title: Provision of Facility for Monitoring Intraday Uncrystallised Mark-to-Market
  (MTM) Losses for Futures Contracts
---

## Summary

BSE Clearing Limited (BSECL), formerly Indian Clearing Corporation Limited (ICCL), has introduced an optional facility in its Real-Time Risk Management System (RTRMS) that allows Clearing Members to monitor intraday uncrystallised Mark-to-Market (MTM) losses at the Trading Member level for open futures positions. This facility operates independently of existing margin monitoring frameworks.

## Key Points

- Optional, request-based facility available to Clearing Members to define MTM loss limits for their associated Trading Members.
- Clearing Members must submit a formal request via email to BSECL's Risk Department to activate the facility.
- Once activated, Clearing Members can configure MTM loss limits per affiliated Trading Member through RTRMS.
- Automated email alerts are generated at 70%, 80%, 90%, and 100% utilisation of the configured MTM limit; each threshold triggers an alert only once upon first breach.
- MTM profit and loss is computed in real-time based solely on open futures positions using latest available futures prices.
- Net losses are aggregated across client and proprietary positions at the Trading Member level.
- Breach of a configured MTM limit does not trigger any automatic action (e.g., disablement or position close-out) unless BSECL specifically notifies otherwise.
- By default, the "Set Unlimited M2M Limit" option is enabled and MTM limits remain unconfigured.

## Regulatory Changes

No mandatory regulatory changes are introduced. This is an optional operational enhancement to RTRMS that provides Clearing Members with an additional monitoring tool for intraday MTM risk at the Trading Member level. The facility is entirely separate and mutually exclusive from the existing margin monitoring framework linked to allocated or pledged collateral.

## Compliance Requirements

- Clearing Members wishing to use the facility must submit a formal email request to BSECL's Risk Department (risk.monitoring@icclindia.com / risk.iccl@icclindia.com).
- Upon activation, Clearing Members are responsible for configuring MTM limits and email IDs for alerts at their sole discretion.
- Where a limit is configured, entry of the MTM value is mandatory and forms the basis for computing MTM utilisation percentages.
- No mandatory action is required for members not wishing to use this facility.

## Important Dates

- **Effective Date:** 17 June 2026 — The facility is now available in RTRMS as of this notice.

## Impact Assessment

This facility provides Clearing Members with enhanced intraday risk visibility for open futures positions of their Trading Members, without altering mandatory margin or collateral obligations. It is a purely optional monitoring tool and does not impose new compliance burdens. Members who opt in can proactively manage MTM exposure through configurable thresholds and automated alerts, potentially reducing risk events. The facility has medium operational relevance for active derivatives clearing participants but minimal impact on the broader market.