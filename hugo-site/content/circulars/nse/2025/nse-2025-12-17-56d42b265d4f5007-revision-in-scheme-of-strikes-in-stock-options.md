---
category: trading
circular_id: 56d42b265d4f5007
date: '2025-12-17'
description: NSE revises strike scheme parameters including step values and number
  of strikes for stock options, effective December 31, 2025.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP71864.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical update affecting F&O traders dealing with stock options.
  Changes strike intervals and availability which impacts trading strategies but doesn't
  fundamentally alter market structure.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP71864.zip
processing:
  attempts: 1
  content_hash: ae443ac3e1d62bc9
  processed_at: '2025-12-17T15:54:09.654640'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-17T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP71864.zip
severity: medium
source: nse
stocks:
- 360ONE
- ABB
- ABCAPITAL
- ADANIENSOL
- ADANIENT
- ADANIGREEN
- ADANIPORTS
- ALKEM
- AMBER
- AMBUJACEM
- ANGELONE
- APLAPOLLO
- APOLLOHOSP
- ASHOKLEY
- ASIANPAINT
- ASTRAL
- AUBANK
- AUROPHARMA
- AXISBANK
- BAJAJ-AUTO
- BAJAJFINSV
tags:
- stock-options
- strike-scheme
- derivatives
- futures-and-options
- trading-parameters
- contract-specifications
title: Revision in Scheme of Strikes in Stock Options
---

## Summary

NSE has revised the strike scheme for stock options, updating step values and number of strikes available for trading. The changes reference Chapter 1.10 of the F&O Consolidated Circular (NSE/FAOP/67775 dated April 30, 2025) and will be implemented from December 31, 2025. Members must load updated contract files before trading commences on the effective date.

## Key Points

- Revised strike schemes apply to multiple stock options including narrow and wide range categories
- Strike schemes differentiate between Near, Mid, and Far month contracts
- Step values vary by stock and range from 2.5 to 200 points depending on the underlying security
- Number of strikes available varies by contract month (Near typically has most strikes, Far has least)
- Reserve strikes are also specified for each stock across different contract months
- Updated contract.gz file must be loaded from /faoftp/faocommon directory on extranet server

## Regulatory Changes

Revision of strike scheme parameters including:
- Step values for narrow range: Different values for Near, Mid, and Far months
- Step values for wide range: Typically double the narrow range values
- Strike scheme counts: Number of strikes available for trading varies by month
- Reserve strikes: Additional strikes kept in reserve for each contract month

Examples from Annexure 1:
- 360ONE: Narrow range step values 20/20/40, Wide range 40/40/80
- APOLLOHOSP: Narrow range step values 50/50/100, Wide range 100/100/200
- ASHOKLEY: Narrow range step values 2.5/2.5/5, Wide range 5/5/10

## Compliance Requirements

- Trading members must load the updated contract.gz file in their trading applications before December 31, 2025
- File to be obtained from /faoftp/faocommon directory on NSE extranet server
- Members must ensure systems are updated to reflect new strike schemes for affected stocks
- Reference to master circular NSE/FAOP/67775 dated April 30, 2025 for detailed framework

## Important Dates

- **Circular Date**: December 17, 2025
- **Effective Date**: December 31, 2025 (new strike schemes become applicable for trading)
- **System Update Deadline**: Before trading on December 31, 2025

## Impact Assessment

This revision affects F&O market participants trading stock options in the listed securities. The changes impact:

**Trading Strategy**: Modified strike intervals may require adjustments to options strategies and hedge positions

**Liquidity**: Changes in number of available strikes could affect liquidity distribution across different strike prices

**Risk Management**: Updated strike schemes require recalibration of risk management systems and position monitoring tools

**Market Participants**: Primary impact on options traders, market makers, proprietary trading desks, and institutional participants using stock options for hedging or speculation

**Operational Impact**: Members need to ensure technical systems are updated before the effective date to avoid trading disruptions