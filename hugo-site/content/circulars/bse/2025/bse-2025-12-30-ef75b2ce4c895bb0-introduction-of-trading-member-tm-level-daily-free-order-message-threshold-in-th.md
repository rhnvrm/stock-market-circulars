---
category: market-operations
circular_id: ef75b2ce4c895bb0
date: '2025-12-30'
description: BSE introduces a daily free order message threshold for trading members
  in the equity cash segment with detailed file format specifications for daily order
  charges reporting.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={3488181C-993C-48DA-8814-01F586CF5DC5}&noticeno=20251230-31&dt=12/30/2025&icount=31&totcount=59&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational update affecting trading members with new reporting requirements
  and charge structure for order messages. Medium impact as it affects TM operations
  and cost structure.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251230-31&attachedId=93ecd8b5-40cb-433a-ac23-e4cbbdae8815
processing:
  attempts: 1
  content_hash: 222d12de28371fe1
  processed_at: '2025-12-30T18:51:01.114558'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-30T12:40:55+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={3488181C-993C-48DA-8814-01F586CF5DC5}&noticeno=20251230-31&dt=12/30/2025&icount=31&totcount=59&flag=0
severity: medium
source: bse
stocks: []
tags:
- trading-members
- order-threshold
- equity-cash-segment
- daily-charges
- reporting-format
- market-operations
title: Introduction of Trading Member (TM) Level Daily Free Order Message Threshold
  in the Equity Cash Segment – Update
---

## Summary

BSE has introduced a Trading Member (TM) level daily free order message threshold in the equity cash segment. This circular provides detailed specifications for the daily order charges file that will be published on BSE Extranet, including file format, fields, and publishing schedule. Trading members will receive daily reports showing their order counts, daily charges, and cumulative monthly charges.

## Key Points

- Daily order charges file will be published on BSE Extranet between 7:30 PM and 9:00 PM
- File name format: Equity_OrderCharges_YYYYMMDD_MemberCode.csv
- File will be available at: Home->EQ->Transaction->Month->Date path on Extranet
- CSV format with header containing column names
- Reports include member code, trade date, daily order count, daily charges, and cumulative charges
- Daily charges calculated based on orders exceeding the free threshold
- Cumulative charges tracked till end of month

## Regulatory Changes

BSE has implemented a structured charging mechanism for trading members based on daily order message volumes:

- Introduction of daily free order message threshold for TMs in equity cash segment
- Charges apply to orders exceeding the daily free threshold
- Daily and cumulative charge tracking throughout the month
- Automated reporting system through BSE Extranet

## Compliance Requirements

**For Trading Members:**

- Monitor daily order message volumes through the published CSV files
- Review daily charges and cumulative monthly charges
- Access reports daily from BSE Extranet between 7:30 PM and 9:00 PM
- Maintain records of order charges for compliance and reconciliation
- Adjust order management strategies to optimize within free threshold limits

**File Format Specifications:**

- Field 1: Member Code (Numeric, 9 digits)
- Field 2: Trade Date (String, 10 characters, yyyy-mm-dd format)
- Field 3: Daily Number of Orders (Numeric, 22 digits)
- Field 4: Daily Charges (Numeric, 22 digits with 2 decimal places)
- Field 5: Daily Cumulative Charges (Numeric, 22 digits with 2 decimal places)

## Important Dates

- **File Publishing Time:** Daily between 7:30 PM and 9:00 PM
- **File Frequency:** Daily at End of Day (EOD)
- **Cumulative Charges Period:** Tracked till end of each month
- **Sample Data Period:** January 2026 (as per annexure)

## Impact Assessment

**Operational Impact:**
- Trading members need to implement monitoring systems for daily order volumes
- Cost implications for high-frequency trading members exceeding free thresholds
- Enhanced transparency in order-related charges through daily reporting

**Market Impact:**
- May influence order routing strategies for trading members
- Potential optimization of order management to stay within free thresholds
- Administrative burden for TMs to monitor and reconcile daily charges

**Technology Impact:**
- Trading members may need to integrate automated file retrieval from Extranet
- Systems required to process and track cumulative monthly charges
- Daily reconciliation processes needed for charge management

**Financial Impact:**
- Variable cost structure based on daily order volumes
- Charges accumulate throughout the month for orders exceeding thresholds
- Predictable cost structure with daily transparency