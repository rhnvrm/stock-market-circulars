---
category: trading
circular_id: 1849a15864e546ed
date: '2025-12-30'
description: BSE introduces a daily free order message threshold for trading members
  in the equity cash segment with charges applicable beyond the threshold, with daily
  reporting via CSV files.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={3488181C-993C-48DA-8814-01F586CF5DC5}&noticeno=20251230-31&dt=12/30/2025&icount=31&totcount=31&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Introduces new charging mechanism for trading members exceeding daily
  order thresholds, affecting operational costs and order management strategies
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251230-31&attachedId=93ecd8b5-40cb-433a-ac23-e4cbbdae8815
processing:
  attempts: 1
  content_hash: ff8c796629785a78
  processed_at: '2025-12-30T12:52:25.337765'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-30T12:40:55+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={3488181C-993C-48DA-8814-01F586CF5DC5}&noticeno=20251230-31&dt=12/30/2025&icount=31&totcount=31&flag=0
severity: medium
source: bse
stocks: []
tags:
- order-threshold
- trading-members
- equity-cash-segment
- charges
- reporting
- order-messages
title: Introduction of Trading Member Level Daily Free Order Message Threshold in
  Equity Cash Segment
---

## Summary

BSE has introduced a Trading Member (TM) level daily free order message threshold in the equity cash segment. Trading members will be charged for order messages exceeding the daily threshold. BSE will provide daily CSV files containing order counts, daily charges, and cumulative monthly charges for each trading member via the Extranet portal.

## Key Points

- Daily free order message threshold established at trading member level for equity cash segment
- Charges apply for orders exceeding the daily threshold
- Daily reporting file (CSV format) available on Extranet between 7:30 PM and 9:00 PM
- File contains member code, trade date, daily order count, daily charges, and cumulative charges
- Cumulative charges tracked throughout the month
- File naming convention: Equity_OrderCharges_YYYYMMDD_MemberCode.csv
- Files published daily at end of day (EOD)

## Regulatory Changes

BSE has implemented a new order message charging structure for trading members in the equity cash segment. This represents a shift towards volume-based charging for order messages, with a daily free threshold and charges for excess orders.

## Compliance Requirements

- Trading members must monitor their daily order message volumes
- Members should track charges through daily CSV reports available on Extranet
- Access reports via path: Home -> EQ -> Transaction -> Month -> Date
- Monitor cumulative charges throughout the month
- Plan order management strategies to optimize costs within threshold limits

## Important Dates

- Implementation: Already in effect (update circular issued December 30, 2025)
- Daily reporting: Files published between 7:30 PM and 9:00 PM each trading day
- Cumulative charges: Reset at end of each month

## Impact Assessment

**Trading Members**: Medium to high impact depending on order volumes. Members with high-frequency trading strategies or large order volumes may face significant additional costs if exceeding daily thresholds. Requires operational adjustments to monitor and manage order message volumes.

**Market Operations**: May encourage more efficient order management practices and reduce unnecessary order messages, potentially improving market system performance.

**Cost Impact**: Variable based on trading patterns. Sample data shows charges ranging from zero (on low-volume days) to over 1 million rupees cumulative for high-volume trading members over a month.

**File Format Details**:
- Field 1: Member code (Numeric, 9 digits)
- Field 2: Trade Date (String, 10 characters, yyyy-mm-dd format)
- Field 3: Daily Number of Orders (Numeric, 22 digits)
- Field 4: Daily Charges (Numeric, 22 digits with 2 decimal places)
- Field 5: Daily Cumulative Charges (Numeric, 22 digits with 2 decimal places)