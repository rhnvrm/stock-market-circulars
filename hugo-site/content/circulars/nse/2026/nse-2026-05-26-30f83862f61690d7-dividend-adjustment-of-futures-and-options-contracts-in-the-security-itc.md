---
category: trading
circular_id: 30f83862f61690d7
date: '2026-05-26'
description: NSE announces adjustment of ITC F&O contracts due to dividend of Rs 8.00/-
  per share (face value Re 1/-), effective 27-May-2026. Strike prices revised downward
  across all OPTSTK contracts expiring 30-Jun-2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP74416.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Routine but mandatory F&O contract strike price adjustment for ITC
  due to Rs 8/- dividend. Affects all ITC derivatives traders holding or intending
  to trade OPTSTK contracts expiring June 2026; members must load updated contract
  files before ex-date.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP74416.pdf
processing:
  attempts: 1
  content_hash: 2adc913622b22985
  processed_at: '2026-05-26T15:50:53.525027'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-26T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP74416.pdf
severity: medium
source: nse
stocks:
- ITC
tags:
- dividend
- adjustment-of-futures-and-options-contracts
- price-adjustment
- ex-date
- ex-dividend
- futures-and-options
title: 'ITC Dividend: Adjustment of Futures and Options Contracts (Ex-Date 27-May-2026)'
---

## Summary

NSE's Futures & Options department (Circular Ref. No. 71/2026, Download Ref No: NSE/FAOP/74416) announces the adjustment of Futures and Options contracts in ITC LIMITED (Symbol: ITC) pursuant to SEBI guidelines on corporate action adjustments. ITC has declared a dividend of Rs 8.00/- per share on a face value of Re 1/-, with the ex-date and effective date set as 27-May-2026. All affected option strike prices are revised downward accordingly.

## Key Points

- **Symbol:** ITC (ITC LIMITED)
- **Corporate Action:** Dividend of Rs 8.00/- per share (Face Value: Re 1/-)
- **Ex-Date / Effective Date:** 27-May-2026
- **Instrument Type Affected:** OPTSTK (Options on Stock)
- **Expiry Date Affected:** 30-Jun-2026
- Strike prices are revised by subtracting Rs 8.00 from existing strikes (e.g., 255.00 → 247.00, 260.00 → 252.00, 265.00 → 257.00, etc.)
- Revised strike/futures base prices and lot sizes may appear in decimal places and will be rounded to the nearest tick size; lot sizes rounded to the nearest integer
- Updated contract files (contract.gz / MII contract and spread files) must be loaded before trading on the ex-date

## Regulatory Changes

Pursuant to SEBI guidelines on adjustments to futures and options contracts upon announcement of corporate actions, NSE has revised the option strike prices for all ITC OPTSTK contracts expiring 30-Jun-2026. The full revised strike price table is available in Annexure 1 of the circular and via the NSE website at the equity derivatives corporate actions adjustments page.

## Compliance Requirements

- Members **must load the updated contract.gz / MII contract** (`NSE_FO_contract_ddmmyyyy.csv.gz`) and spread (`NSE_FO_spdcontract_ddmmyyyy.csv.gz`) files on their trading applications **before trading on 27-May-2026** (the ex-date).
- Files are available from the directory `faoftp/faocommon` on the Extranet server and also on the NSE website under All Reports – Derivatives.
- The methodology for position adjustments will be separately communicated by the respective Clearing Corporation.

## Important Dates

- **Circular Date:** 26-May-2026
- **Ex-Date / Effective Date:** 27-May-2026
- **Expiry of Affected Contracts:** 30-Jun-2026

## Impact Assessment

This is a standard, SEBI-mandated corporate action adjustment. All traders and members holding or planning to trade ITC OPTSTK contracts expiring 30-Jun-2026 are directly affected. Strike prices are reduced uniformly by Rs 8.00 (the dividend amount), preserving the economic value of existing positions. The primary operational risk is failure to load updated contract files before the ex-date, which could cause trading errors. No new contracts are introduced or excluded; this is purely a price-level adjustment to existing contracts.