---
category: trading
circular_id: 3e707d93bc76d45b
date: '2026-05-29'
description: NSE introduces Closing Auction Session (CAS) in the Equity Cash segment,
  requiring changes to trading timings and modalities in the Equity Derivatives segment
  effective August 3, 2026. Normal Market Close Time shifts to 15:40 hrs and VWAP
  computation window adjusts accordingly.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP74467.zip
impact: high
impact_ranking: high
importance_ranking: high
justification: Structural change to equity derivatives trading hours and close price
  computation affecting all F&O market participants, effective August 3, 2026, with
  mandatory contract file updates required.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP74467.zip
processing:
  attempts: 1
  content_hash: d72ffabca1632f1d
  processed_at: '2026-05-29T15:57:39.804912'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-29T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP74467.zip
severity: high
source: nse
stocks: []
tags:
- closing-auction-session
- equity-derivatives
- trading-hours
- mock-trading
- futures
- market-operations
- vwap
- neat-terminal
title: Introduction of Closing Auction Session (CAS) in Equity Cash Segment - Change
  in Equity Derivatives Trading Modalities
---

## Summary

NSE has issued this circular (NSE/FAOP/74467) in reference to the upcoming Closing Auction Session (CAS) in the Equity Cash segment. To align the Equity Derivatives segment with CAS, NSE is modifying trading timings, price band resets, NEAT terminal messaging, and close price computation windows. The changes are effective August 03, 2026.

## Key Points

- Normal Market Close Time for Equity Derivatives changes to **15:40 hrs** (previously 15:30 hrs)
- Pre-open session timings and Normal Market Open Time remain unchanged at 09:00 hrs, 09:08 hrs*, and 09:15 hrs respectively
- Trade Modification End Time remains at 16:15 hrs
- VWAP window for close price computation is set to **15:10 hrs to 15:40 hrs** (last 30 minutes)
- Close price computation logic itself remains unchanged
- NEAT terminals in Equity Derivatives will broadcast a notification when CAS triggers a price band reset for stock futures
- Price band and pre-trade risk control provisions reference NSE circular NSE/CMTR/73362 dated March 18, 2026

## Regulatory Changes

- **Trading Hours Update:** Normal Market Close Time in the Equity Derivatives segment moves from 15:30 hrs to 15:40 hrs, aligning with the new CAS window in the Equity Cash segment.
- **NEAT Terminal Broadcast:** A new system message will be sent to Equity Derivatives terminals at the start of CAS in the Equity segment: *"The operating price range for Stock future contracts is being revised. All outstanding orders outside the revised price range shall be cancelled by the Exchange as per extant rules."*
- **VWAP Window:** The half-hour window used for close price (VWAP) computation is redefined as 15:10 hrs to 15:40 hrs.

## Compliance Requirements

- All members must load the updated **contract.gz** and **NSE_FO_contract_ddmmyyyy.csv.gz** files in their trading applications before trading on the effective date (August 03, 2026).
- Files are available from the directory `faoftp/faocommon` on the Extranet server, and also at: https://www.nseindia.com/all-reports-derivatives
- Members must monitor NEAT terminal messages during the CAS window and handle automated order cancellations outside revised price ranges.
- Members should review FAQs on CAS (attached as Annexure) for detailed clarifications.

## Important Dates

- **May 29, 2026:** Circular issued
- **August 03, 2026:** Effective date for all changes in Equity Derivatives trading modalities
- **TBD:** Mock trading sessions for testing functional changes (separate circular to be issued by NSE)

## Impact Assessment

This circular has **high impact** across all Equity Derivatives market participants. The 10-minute extension of the normal trading session (to 15:40 hrs) and the associated price band reset during CAS introduce new intraday risk management considerations for traders holding open F&O positions near close. Automated order cancellation during CAS price band resets requires members to update their systems and risk management workflows. The mandatory contract file reload before August 03 is a hard operational requirement for all trading members. Testing via mock sessions is strongly recommended prior to go-live.