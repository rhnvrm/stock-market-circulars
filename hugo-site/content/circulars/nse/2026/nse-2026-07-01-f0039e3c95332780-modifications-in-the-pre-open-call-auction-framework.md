---
category: trading
circular_id: f0039e3c95332780
date: '2025-07-25'
description: NSE has released an updated FAQ (Version 2.0) revising the order entry
  and order matching schedule for the pre-open call auction session in the equity
  derivatives segment, effective September 7, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP74970.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Affects order entry and matching windows for F&O pre-open auctions
  market-wide, relevant to all trading members and algo/order routing systems, but
  is a procedural timing adjustment rather than a fundamental market structure change.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP74970.zip
processing:
  attempts: 1
  content_hash: 6e2414a0c67bbb9d
  processed_at: '2026-07-01T15:00:29.083931'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-07-01T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP74970.zip
severity: medium
source: nse
stocks: []
tags:
- introduction-of-futures-contracts
- modification-in-the-contract
- market-operations
- trading-session-timing
title: NSE Revises Pre-Open Call Auction Session Timings for Equity Derivatives (F&O)
  Segment
---

## Summary

NSE has issued an updated FAQ (Version 2.0, July 2026) on the Pre-Open Session in the Equity Derivatives (F&O) segment, revising the internal sub-period timings within the existing 9:00 am to 9:15 am pre-open call auction window. The revised framework will be applicable with effect from September 7, 2026.

## Key Points

- Pre-open call auction session applies to both single stock futures and index futures in the equity derivatives market.
- The overall session duration remains 15 minutes (9:00 am to 9:15 am); only the internal sub-period boundaries are being revised.
- Order Entry Period is split into two sub-parts under the revised schedule:
  - 9:00 am to 9:05 am: order entry, modification, and cancellation allowed for both limit and market orders.
  - 9:05 am to 9:10 am (with system-driven random closure in the last 2 minutes): only limit order entry, modification, and cancellation allowed; no modification/cancellation permitted for market orders.
- Order Matching & Trade Confirmation Period moves from the current 9:08 am–9:12 am to a revised 9:10 am–9:12 am window, starting immediately after order entry closes; this covers opening price determination, order matching, and trade confirmation.
- Buffer Period (9:12 am–9:15 am), covering transition from pre-open to the Continuous Trading Session (CTS), remains unchanged.
- Pre-open applies only to current-month futures contracts, except in the last five trading days before current-month expiry, when it extends to next-month futures contracts as well.
- In case of a market-wide circuit filter breach or trading outage, the market will reopen with a pre-open session, with timings communicated separately on that day.

## Regulatory Changes

The order entry period is being compressed and restructured (from the current 9:00–9:08 am undivided period to a bifurcated 9:00–9:05 am and 9:05–9:10 am structure), and the order matching window is shifted later (9:10 am–9:12 am instead of 9:08 am–9:12 am). The buffer period timing is unchanged.

## Compliance Requirements

Trading members and their technology/order management systems handling equity derivatives orders during the pre-open session must update their systems to align with the revised order entry, modification, and cancellation cut-off timings ahead of the effective date.

## Important Dates

- FAQ updated: July 1, 2026
- Revised pre-open framework effective from: September 7, 2026

## Impact Assessment

The change affects all trading members participating in the F&O pre-open call auction for single stock and index futures. Firms using automated or algorithmic order entry must recalibrate their systems to the new sub-period cut-offs to avoid order rejections or missed modification/cancellation windows. The overall market impact is moderate since it is a procedural refinement of existing pre-open mechanics rather than a structural change to trading hours or contract eligibility.