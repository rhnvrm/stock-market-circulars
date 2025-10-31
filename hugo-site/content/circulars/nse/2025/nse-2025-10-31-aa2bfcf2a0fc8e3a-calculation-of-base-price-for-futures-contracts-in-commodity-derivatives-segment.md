---
category: trading
circular_id: aa2bfcf2a0fc8e3a
date: '2025-10-31'
description: NSE modifies the methodology for calculating base price for futures contracts
  in the commodity derivatives segment, introducing theoretical price calculation
  under specific conditions.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/COM71089.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Affects pricing methodology for commodity futures contracts but is
  a technical update to existing procedures with limited operational disruption
pdf_url: https://nsearchives.nseindia.com/content/circulars/COM71089.pdf
processing:
  attempts: 1
  content_hash: d606a70472f5e082
  processed_at: '2025-10-31T15:54:40.450371'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-31T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/COM71089.pdf
severity: medium
source: nse
stocks: []
tags:
- commodity-derivatives
- futures-contracts
- base-price
- calculation-methodology
- trading-parameters
- price-determination
title: Calculation of Base Price for Futures Contracts in Commodity Derivatives Segment
  - Update
---

## Summary

NSE has issued a partial modification to the base price calculation methodology for futures contracts in the Commodity Derivatives Segment. The circular updates item 1.5 (Close Price, Base Price and Operating ranges) of the consolidated circular NSE/COM/67724 dated April 28, 2025. The update introduces two distinct scenarios for determining base price based on how the close price is computed, with the second scenario allowing theoretical price calculation using the formula S * e^rt.

## Key Points

- Partial modification to base price calculation for commodity futures contracts
- Two scenarios defined based on close price computation method
- When close price is computed per sub-points 1.a or 1.b, that close price becomes the base price
- When close price is computed per sub-points 1.c or 1.d, theoretical price can be set as base price
- Theoretical price formula: S * e^rt (where S = underlying price, r = MIBOR rate, t = time to maturity in years)
- Special provision for electricity futures: S can be underlying price OR close price of near month contract
- Members must download updated contract files before trading

## Regulatory Changes

The circular modifies the base price determination methodology for futures contracts in commodity derivatives:

**Scenario A (Close price per sub-points 1.a or 1.b):**
- The computed close price shall be directly set as the base price

**Scenario B (Close price per sub-points 1.c or 1.d):**
- Theoretical price calculation is permitted for base price determination
- Formula: S * e^rt
- Components:
  - S: Appropriate underlying price (for electricity futures: underlying price OR close price of near month contract)
  - r: Applicable MIBOR (Mumbai Interbank Offered Rate)
  - t: Time to maturity in years

## Compliance Requirements

**For Trading Members:**
- Download updated contract files from NSE extranet before commencing trading
- File paths: /comtftp/comtcommon
- Required files:
  - co_contract.gz
  - NSE_COM_contract_ddmmyyyy.csv.gz
- Ensure trading systems are updated with new base price calculation logic
- Update risk management systems to reflect modified pricing methodology

## Important Dates

- **Circular Issue Date:** October 31, 2025
- **Effective Date:** Immediate (members advised to update files before trading)
- **Reference Circular:** NSE/COM/67724 dated April 28, 2025 (partially modified)

## Impact Assessment

**Market Impact:**
- Medium impact on commodity derivatives trading operations
- Affects price discovery mechanism for futures contracts
- May result in different base prices compared to previous methodology in certain scenarios

**Operational Impact:**
- Trading members must update systems and download new contract files
- Risk management systems require recalibration for theoretical price scenarios
- Electricity futures have special treatment requiring additional system logic

**Technical Impact:**
- Introduction of theoretical pricing formula adds complexity to base price determination
- MIBOR rate becomes a critical input for base price calculation in specific scenarios
- Time to maturity calculation becomes essential for pricing accuracy

**Member Actions Required:**
- Immediate: Download updated contract files from NSE extranet
- Update front-office and risk management systems
- Train dealers on new base price calculation scenarios
- Test systems before resuming commodity derivatives trading