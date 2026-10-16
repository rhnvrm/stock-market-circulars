---
category: trading
circular_id: 1a413e1e1386439e
date: '2026-10-16'
description: BSE introduces mandatory cautionary pop-up messages on trading terminals
  for International ETFs trading away from their Net Asset Value (NAV).
draft: false
guid: https://www.bseindia.com/downloads/UploadDocs/Notices/20261016-49/20261016-49.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Trading members must deploy mandatory cautionary alert functionality
  for International ETFs by November 16, 2026 to mitigate risks from NAV price variances.
pdf_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20261016-49/20261016-49.pdf
processing:
  attempts: 1
  content_hash: 058fc984937babe6
  processed_at: '2026-10-16T16:17:50.528447'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-10-16T15:18:26+00:00'
rss_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20261016-49/20261016-49.pdf
severity: medium
source: bse
stocks: []
tags:
- etf
- trading-terminal
- surveillance
- investor-protection
- bse
title: Cautionary Messages on Trading Terminal – ETF Update
---

## Summary

BSE, in consultation with SEBI, has introduced a mandatory cautionary pop-up message functionality on trading terminals for International Exchange Traded Funds (ETFs) that trade at a significant premium or discount relative to their Net Asset Value (NAV). Trading members must implement this feature on non-BOLT/BOW/BITs front-end applications by November 16, 2026.

## Key Points

- International ETFs frequently trade at prices reflecting significant premiums or discounts to their underlying NAV, creating potential risks for market and aggressive limit orders.
- A new cautionary alert message indicator has been added to the `REG1_INDDDMMYYY.csv` file (Column No. 24).
- Requirement applies to trading members with retail clients across non-BOLT/BOW/BITs front-end applications including IBT, STWT, CTCL, etc.
- Prompt format: "Security is under - would you like to continue? Yes / No" or specific ETF message such as "International ETFs may trade above their NAV.? Yes / No."
- Orders are transmitted to the Exchange only if the user selects "Yes".
- Trading members must maintain audit logs of all alert displays per scrip and the options selected by investors.

## Regulatory Changes

- Addition of a new indicator field in the daily `REG1_INDDDMMYY.csv` file structure (Column No. 24) to flag International ETFs.
- Mandatory deployment of pre-order confirmation prompt logic for retail orders on designated securities.

## Compliance Requirements

- Trading members, third-party trading application vendors, and back-office vendors must update their applications to support the new file structure and order entry pop-up logic.
- Fully deploy the functionality and ensure compliance by **November 16, 2026**.
- Maintain comprehensive audit logs of all prompt displays and client responses for review by management and system auditors.

## Important Dates

- **Circular Date:** October 16, 2026
- **Mandatory Compliance Deadline:** November 16, 2026

## Impact Assessment

- Significantly improves investor protection by alerting retail participants to price disparities prior to order execution in International ETFs.
- Requires development and operational adjustments by trading members and software vendors to update front-end order entry and logging mechanisms.