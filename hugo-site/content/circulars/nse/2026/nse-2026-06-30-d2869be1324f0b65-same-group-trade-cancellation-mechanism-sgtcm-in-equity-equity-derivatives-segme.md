---
category: trading
circular_id: d2869be1324f0b65
date: '2026-06-30'
description: NSE is introducing the Same Group Trade Cancellation Mechanism (SGTCM)
  to automatically cancel intraday trades executed between same group or related entities
  (identified by PAN) in Equity and Equity Derivatives segments on a voluntary basis
  for trading members.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/SURV74956.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: New voluntary surveillance mechanism with operational significance
  for trading members who have same-group/related-entity clients; implementation date
  still to be announced, limiting immediate urgency.
pdf_url: https://nsearchives.nseindia.com/content/circulars/SURV74956.pdf
processing:
  attempts: 1
  content_hash: ee472d7484169b0c
  processed_at: '2026-06-30T14:49:23.206770'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-30T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/SURV74956.pdf
severity: medium
source: nse
stocks: []
tags:
- sgtcm
- surveillance
- trade-cancellation
- unauthorized-market-practices
- equity-derivatives
- pan-verification
- intraday
- nse
title: NSE Introduces Same Group Trade Cancellation Mechanism (SGTCM) in Equity &
  Equity Derivatives Segments
---

## Summary

NSE is introducing the Same Group Trade Cancellation Mechanism (SGTCM), a voluntary facility for trading members to prevent intraday trades between same group or related entities. Based on PAN-level data submitted by trading members, the Exchange system will automatically cancel trades executed between identified related client pairs in Equity and Equity Derivatives segments during normal/continuous market hours.

## Key Points

- Exchange will monitor intraday transactions between pairs of PANs; trades between reported same group/related entities will be auto-cancelled.
- Cancellation applies even when the related PAN pair trades through different trading members.
- PAN is used as the unique identifier for client identification under SGTCM.
- The mechanism is voluntary — trading members may opt in by submitting related entity data to NSE Surveillance.
- SGTCM applies only during normal/continuous market sessions; Pre-open, Special Pre-open, and Closing Auction sessions are excluded.
- Upon trade cancellation, trading members receive an appropriate message/transcode on their trading terminals (NEAT message: "Trade CXL: <Trade details> Trade Cancelled by Exchange User Id").
- Client Code Modifications during market hours that satisfy SGTCM conditions will also result in trade cancellation.
- Implementation date will be communicated separately.

## Regulatory Changes

NSE is launching a new exchange-level automated trade cancellation mechanism under its surveillance framework. This introduces a formal process for same-group/related-entity trade monitoring at the PAN level, expanding surveillance capabilities beyond existing manual or post-trade review processes.

## Compliance Requirements

- Trading members wishing to use SGTCM must submit a CSV file listing related/same group client PANs to surveillance@nse.co.in by **3:30 PM on T Day**; the mechanism activates for those clients from **T+1 trading day**.
- **File naming convention:** `TM Code_SGTCM_DDMMYYYY.csv` (DDMMYYYY = T date).
- **File format (CSV columns):**
  1. TM Code — CHAR(5)
  2. Group No — CHAR(10), alphanumeric unique code
  3. PAN — CHAR(10)
  4. Addition/Deletion Flag — CHAR(1): 'A' for addition, 'D' for deletion
- Any additions or modifications to related entity data must also be submitted by the 3:30 PM cutoff.
- Participation is voluntary; non-participating members face no penalty.

## Important Dates

- **Circular Date:** June 30, 2026
- **File Submission Deadline (per T Day):** 3:30 PM on T Day (for T+1 applicability)
- **Implementation Date:** To be announced separately by NSE

## Impact Assessment

The SGTCM is a surveillance-enhancing measure aimed at preventing wash trades or circular trading between related entities. For trading members with complex client structures involving group companies or family entities, this mechanism provides a proactive compliance tool to avoid inadvertent same-group trades. The voluntary nature limits immediate mandatory compliance burden, but members with known related-entity client bases should evaluate whether to enroll ahead of the implementation date. The intraday auto-cancellation with terminal messaging ensures prompt notification, reducing settlement complications from such trades.