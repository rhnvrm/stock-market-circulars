---
category: trading
circular_id: 898475fdf717c1a5
date: '2026-04-02'
description: NSE revises the Order-to-Trade Ratio framework effective April 6, 2026,
  expanding the exemption range for Equity Derivatives Options Segment to ±40% of
  LTP (premium) or ±INR 20, whichever is higher.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/SURV73597.zip
impact: high
impact_ranking: high
importance_ranking: high
justification: Directly impacts all algorithmic traders across equity derivatives
  and equity segments by modifying OTR penalty exemption criteria effective April
  6, 2026; mandated by SEBI circular and affects order placement strategies for algo
  participants.
pdf_url: https://nsearchives.nseindia.com/content/circulars/SURV73597.zip
processing:
  attempts: 1
  content_hash: 2d8b8988eb95096f
  processed_at: '2026-04-02T16:12:24.594105'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-04-02T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/SURV73597.zip
severity: high
source: nse
stocks: []
tags:
- order-to-trade-ratio
- algorithmic-trading
- surveillance
- equity-derivatives
- options
- futures
- sebi-circular
- algo-trading
- otr-framework
title: Revision of Order-to-Trade Ratio (OTR) Framework for Algorithmic Trading
---

## Summary

NSE has revised its Order-to-Trade Ratio (OTR) framework in continuation of Exchange circular NSE/SURV/45016 (July 14, 2020), pursuant to SEBI Circular No. HO/47/11/16(2)2025-MRD-POD2/I/4113/2026 dated February 4, 2026. The key change is an expanded exemption criterion for the Equity Derivatives – Options Segment, effective April 6, 2026. A mock trading session for the revised OTR functionality was conducted on March 14, 2026.

## Key Points

- The OTR framework is modified effective **April 06, 2026**
- For the **Equity Derivatives – Options Segment**, the exemption criterion is widened from the existing 0.75% of LTP to **±40% of LTP (premium) or ±INR 20, whichever is higher**
- For **Equity Derivatives – Futures Segment** and the **Equity Segment**, the existing exemption criterion (orders within 0.75% of LTP) remains unchanged
- Existing penal charges, actions, and other modalities under NSE/SURV/45016 remain the same
- Mock trading for the revised functionality was held on March 14, 2026

## Regulatory Changes

| Segment | Existing Criteria | Revised Criteria |
|---|---|---|
| Equity Derivatives – Options | Orders within 0.75% of LTP exempted from OTR penalty calculation | Orders within ±40% of LTP (premium) or ±INR 20 (whichever is higher) exempted |
| Equity Derivatives – Futures | Orders within 0.75% of LTP exempted | Same as existing criteria (no change) |
| Equity Segment | Orders within 0.75% of LTP exempted | Same as existing criteria (no change) |

This revision significantly broadens the exemption band for options algo orders, reflecting the higher price volatility and wider bid-ask spreads typical in options markets.

## Compliance Requirements

- All members engaged in algorithmic trading in the Equity Derivatives – Options Segment must update their systems to reflect the revised OTR exemption threshold of ±40% of LTP (premium) or ±INR 20, whichever is higher
- Members must ensure their order management and risk systems are reconfigured prior to April 6, 2026
- Penal charges and actions for high OTR breaches remain as per circular NSE/SURV/45016; members must continue to monitor OTR compliance
- For Futures and Equity segments, no changes to existing configurations are required

## Important Dates

- **February 4, 2026**: SEBI issued guidelines on OTR for Algorithmic Trading (SEBI Circular No. HO/47/11/16(2)2025-MRD-POD2/I/4113/2026)
- **February 6, 2026**: NSE issued related circular NSE/SURV/72668
- **March 14, 2026**: Mock trading session for revised OTR functionality conducted
- **April 02, 2026**: This circular issued (NSE/SURV/73597, Circular Ref. No. 240/2026)
- **April 06, 2026**: Revised OTR framework becomes effective

## Impact Assessment

This revision has a **high impact** on algorithmic traders, particularly those active in the Equity Derivatives – Options Segment. By widening the exemption band from 0.75% to ±40% of LTP (or ±INR 20, whichever is higher), NSE significantly reduces the likelihood that legitimate options algo orders near the market price will attract OTR penalties. This change acknowledges the structural differences in options pricing (premium-based, wider spreads) versus futures and equity instruments. Algo traders in options will benefit from reduced compliance friction and fewer inadvertent OTR breaches. For futures and equity algo traders, there is no operational change required.