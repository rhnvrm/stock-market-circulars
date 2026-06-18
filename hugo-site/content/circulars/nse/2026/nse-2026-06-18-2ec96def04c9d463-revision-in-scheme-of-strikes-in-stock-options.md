---
category: trading
circular_id: 2ec96def04c9d463
date: '2026-06-18'
description: NSE revises the strike scheme for stock options, updating step values,
  strike counts, and reserve strikes for multiple securities effective July 1, 2026.
  Members must load the updated contract.gz file before trading on that date.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP74758.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational F&O circular requiring member action before July 1, 2026;
  affects strike availability and step values across a broad list of stock options
  but follows established NSE periodic revision process.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP74758.zip
processing:
  attempts: 1
  content_hash: 5b33924442760fad
  processed_at: '2026-06-18T15:44:25.622618'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-18T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP74758.zip
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
- ADANIPOWER
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
- futures-and-options
- modification-in-the-contract
- strike-scheme
- lot-size-change
title: Revision in Scheme of Strikes in Stock Options Effective July 1, 2026
---

## Summary

NSE has revised the scheme of strikes for stock options under circular NSE/FAOP/74758 dated June 18, 2026. The revision updates step values (narrow and wide range), the number of strikes (near, mid, and far expiry), and reserve strikes for a large set of eligible stocks. The changes take effect from **July 1, 2026**.

## Key Points

- Revision is made under chapter 1.11 of the strike scheme outlined in the F&O Consolidated Circular NSE/FAOP/73928 dated April 28, 2026.
- Both narrow-range and wide-range step values are revised, with far-expiry steps typically double those of near/mid expiry.
- Strike schemes specify the number of strikes available in near, mid, and far expiry for both narrow and wide ranges.
- Reserve strikes are provided for each range and expiry combination.
- Members must download and load the updated `contract.gz` file from `/faoftp/faocommon` on the NSE extranet server.

## Regulatory Changes

The revised strike parameters supersede the previous values under chapter 1.11 of the F&O Consolidated Circular (NSE/FAOP/73928, April 28, 2026). The annexure details per-symbol configurations covering:
- **Narrow Range**: Step values for near, mid, and far expiry; strike scheme counts; reserve strikes.
- **Wide Range**: Corresponding step values, strike scheme counts, and reserve strikes at approximately double the narrow-range values.

Example entries from the annexure:

| Symbol | NR Step (Near/Mid/Far) | WR Step (Near/Mid/Far) | NR Strikes (Near/Mid/Far) | WR Strikes (Near/Mid/Far) |
|---|---|---|---|---|
| 360ONE | 20 / 20 / 40 | 40 / 40 / 80 | 6 / 6 / 3 | 4 / 4 / 2 |
| ABB | 100 / 100 / 200 | 200 / 200 / 400 | 7 / 7 / 3 | 5 / 5 / 3 |
| ADANIPORTS | 20 / 20 / 40 | 40 / 40 / 80 | 9 / 9 / 5 | 7 / 7 / 3 |
| ASIANPAINT | 20 / 20 / 40 | 40 / 40 / 80 | 12 / 12 / 6 | 10 / 10 / 5 |
| AXISBANK | 20 / 20 / 40 | 40 / 40 / 80 | 7 / 7 / 3 | 5 / 5 / 3 |

## Compliance Requirements

- **All trading members** must update their trading applications with the revised `contract.gz` file available at `/faoftp/faocommon` on the NSE extranet server **before commencement of trading on July 1, 2026**.
- Failure to load the updated contract file may result in incorrect strike availability or trading errors in stock options.

## Important Dates

- **Circular Date**: June 18, 2026
- **Effective Date**: July 1, 2026 — revised strike scheme applies from this date.
- **Action Deadline**: Load updated `contract.gz` file before trading begins on July 1, 2026.

## Impact Assessment

This is a routine but operationally significant revision to the F&O strike scheme. It affects all members trading stock options across the listed securities. The update changes the granularity of available strikes (step values) and the breadth of the options chain (number of strikes in near, mid, and far expiry) for each stock. Wide-range parameters are consistently set at double the narrow-range values. Members need to take a specific technical action — updating the contract file — to ensure their trading systems reflect the new parameters. No change to lot sizes or underlying eligibility is indicated.