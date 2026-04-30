---
category: trading
circular_id: bbdc9e41288588af
date: '2026-04-30'
description: NSE introduces a new five-trading-day rolling horizon RTCM in addition
  to the existing intraday mechanism, enabling cancellation of reversal trades between
  PAN pairs that breach defined thresholds for quantity, ratio, and price difference
  across scrips and contracts.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/SURV74022.pdf
impact: high
impact_ranking: high
importance_ranking: high
justification: This circular introduces a significant new surveillance control that
  can result in automatic trade cancellations for all NSE members trading in equity
  and equity derivatives segments. The five-day rolling window substantially expands
  the scope of the existing intraday RTCM, affecting a broader range of trading strategies
  and imposing stricter monitoring on PAN-pair transactions.
pdf_url: https://nsearchives.nseindia.com/content/circulars/SURV74022.pdf
processing:
  attempts: 1
  content_hash: 75c22c03b4e0b802
  processed_at: '2026-04-30T16:51:00.495812'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-04-30T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/SURV74022.pdf
severity: high
source: nse
stocks: []
tags:
- surveillance
- rtcm
- reversal-trade-cancellation
- equity
- equity-derivatives
- trade-cancellation
- pan
- market-integrity
- artificial-volume
- intraday
title: Reversal Trade Cancellation Mechanism (RTCM) Extended to Five Trading Days
  Rolling Horizon in Equity & Equity Derivatives
---

## Summary

NSE has introduced an additional Reversal Trade Cancellation Mechanism (RTCM) operating on a five-trading-day rolling basis for the Equity and Equity Derivatives segments. This supplements the existing intraday RTCM (introduced via circulars from June 2024 through January 2025). The new mechanism monitors transactions between pairs of PANs (or CP Codes where applicable) across the previous five trading days and cancels trades when all specified threshold parameters are simultaneously breached. Client Code Modifications during market hours that result in a reversal of trade are also covered under this mechanism.

## Key Points

- A new five-day rolling RTCM is introduced in addition to the existing intraday RTCM in Equity and Equity Derivatives segments.
- The mechanism monitors transactions between a **pair of PANs** (PAN replaced by CP Codes where applicable) on a rolling basis across the previous five trading days.
- Trade quantity is aggregated across five days for two legs: First Leg (PAN A buys, PAN B sells) and Second Leg (PAN A sells, PAN B buys).
- A trade is eligible for cancellation only when **all four** threshold parameters are simultaneously breached.
- "Reversal Quantity" is defined as the minimum of aggregated bought and sold quantities between the PAN pair over the five-day window (e.g., if 500 bought and 600 sold, reversal quantity = 500).
- Client Code Modifications during market hours that result in trade reversals are also subject to cancellation under the five-day RTCM.
- References previous circulars: NSE/SURV/62493 (June 18, 2024), NSE/SURV/65645 (December 17, 2024), NSE/SURV/65736 (December 23, 2024), NSE/SURV/66070 (January 10, 2025).

## Regulatory Changes

NSE is expanding its surveillance framework by adding a five-day rolling horizon RTCM alongside the existing intraday mechanism. The four objective parameters that must all be breached to trigger cancellation are:

1. **Reversal Quantity vs. Market Volume (Parameter 3.1):** Combined traded quantity of the PAN pair for both legs (to the extent of reversal on that day) compared against market gross traded quantity in the respective scrip/contract for that day up to that point in time.
2. **Reversal Ratio (Parameter 3.2):** Ratio of First Leg aggregated quantity (x) to Second Leg aggregated quantity (y) across five days, calculated as (x/y × 100)%.
3. **Aggregated Square-Off Difference (Parameter 3.3):** Difference between the average sell price and average buy price across five days, multiplied by the reversal quantity in the respective scrip/contract.
4. **Individual PAN Reversal Ratio (Parameter 3.4):** For every day in the five-day horizon, reversal quantity (both legs) of each PAN in the pair compared with that PAN's total quantity traded in the respective scrip/contract for that day up to that point in time.

## Compliance Requirements

- All NSE members must be aware that trades in the Equity and Equity Derivatives segments may be cancelled if the five-day rolling RTCM parameters are breached.
- Members should monitor their clients' trading patterns across the five-day rolling window to ensure trades are not flagged as reversal transactions.
- Client Code Modifications during market hours that cause trade reversals will also be subject to cancellation; members must exercise caution when processing such modifications.
- Members should communicate this mechanism to their clients, particularly those engaged in frequent two-way trading in the same scrip/contract.

## Important Dates

- **Circular Date:** April 30, 2026
- **Download Ref No:** NSE/SURV/74022
- **Circular Ref No:** 319/2026
- Effective date of the new five-day RTCM mechanism is not explicitly stated in the available content; members should refer to the full circular PDF for implementation timelines.

## Impact Assessment

This circular has **high** market and operational impact. By extending RTCM to a five-day rolling window, NSE significantly broadens the scope of surveillance beyond intraday patterns, targeting sustained reversal trading activity that may be structured to avoid intraday detection. All members and their clients engaged in equity and equity derivatives trading are affected. Trading desks and proprietary traders engaged in hedging or high-frequency strategies involving repeated two-way trades in the same instruments between the same counterparties face elevated risk of trade cancellation. The inclusion of Client Code Modification reversals closes a potential loophole. Members will need to build or update compliance monitoring systems to track five-day rolling PAN-pair metrics across all four parameters to proactively identify and manage cancellation risk.