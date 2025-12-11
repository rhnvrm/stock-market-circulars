---
category: trading
circular_id: 1432bf92927a8fd9
date: '2025-10-31'
description: NSE introduces SOP for intraday monitoring of Market Wide Position Limits
  utilization for single stocks using Future Equivalent basis, with 4 times daily
  monitoring and alerts at 60% threshold.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/SURV71090.pdf
impact: high
impact_ranking: high
importance_ranking: high
justification: Introduces new intraday surveillance framework for derivatives position
  monitoring affecting all trading members, with mandatory compliance from November
  3, 2025. Changes risk monitoring methodology and introduces real-time alerts.
pdf_url: https://nsearchives.nseindia.com/content/circulars/SURV71090.pdf
processing:
  attempts: 1
  content_hash: d56b5670c57de5ef
  processed_at: '2025-10-31T15:56:15.505647'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-31T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/SURV71090.pdf
severity: high
source: nse
stocks: []
tags:
- compliance
- derivatives
- futures-options
- options
- position-limits
- risk-monitoring
- sebi
- surveillance
title: Standard Operating Procedure for Intraday monitoring of MWPL utilization for
  Single Stocks on Future Equivalent (FutEq) basis
---

## Summary

NSE has issued a Standard Operating Procedure for intraday monitoring of Market Wide Position Limits (MWPL) utilization for single stocks on Future Equivalent (FutEq) basis, effective November 3, 2025. This circular implements SEBI directive SEBI/HO/MRD/TPD-1/P/CIR/2025/79 dated May 29, 2025, establishing a framework for enhanced risk monitoring in equity derivatives. The SOP mandates 4 times daily monitoring based on random snapshots and requires exchanges to broadcast alerts when FutEq open interest exceeds 60% of MWPL.

## Key Points

- MWPL utilization monitoring will be conducted 4 times daily based on random snapshots
- Both futures and options positions will be considered for monitoring single stocks
- Exchanges will calculate MWPL utilization based on Future Equivalent (FutEq) open interest at security level
- Alert broadcasts will be sent via exchange trading terminals when FutEq OI exceeds 60% of specified MWPL
- Real-time underlying security value at snapshot time will be used for underlying price
- T-1 day End of Day volatility will be used for intraday volatility computation
- Delta computation methodology specified: FutEq for call options = N(d1), put options = N(d1) - 1, futures = 1
- Risk-free interest rate fixed at latest RBI Repo rate
- Prorated time to expiry as per NSE circular NSE/SURV/70553 dated September 30, 2025

## Regulatory Changes

This circular implements enhanced surveillance measures as mandated by SEBI circular SEBI/HO/MRD/TPD-1/P/CIR/2025/79 dated May 29, 2025 on "Measures for Enhancing Trading Convenience and Strengthening Risk Monitoring in Equity Derivatives." The new framework shifts from end-of-day to intraday monitoring of position limits, introducing a Future Equivalent basis calculation methodology that consolidates futures and options positions for more accurate risk assessment.

## Compliance Requirements

- All trading members must comply with the SOP as detailed in Annexure 1 and Annexure 2
- Members must monitor MWPL utilization alerts broadcast on exchange-provided trading terminals
- Compliance with delta computation methodology for calculating Future Equivalent positions
- Adherence to the 60% MWPL threshold alert system
- Implementation of systems to track intraday position limits on FutEq basis
- Email communications to be directed to surveillance@nse.co.in

## Important Dates

- **Circular Date**: October 31, 2025
- **Effective Date**: November 3, 2025
- **Reference SEBI Circular**: May 29, 2025 (SEBI/HO/MRD/TPD-1/P/CIR/2025/79)
- **Reference NSE Circular**: September 30, 2025 (NSE/SURV/70553) for prorated time to expiry computation

## Impact Assessment

**Market Impact**: High - This circular fundamentally changes how position limits are monitored in equity derivatives markets, moving from end-of-day to intraday surveillance with 4 daily monitoring cycles. The 60% alert threshold provides early warning to market participants, potentially affecting trading strategies and position management.

**Operational Impact**: Trading members and market participants will need to adjust their risk management systems to accommodate real-time MWPL monitoring alerts. The FutEq calculation methodology requires implementation of Black-Scholes delta calculations for options positions, adding computational complexity to position tracking systems.

**Risk Management**: Enhanced surveillance through intraday monitoring strengthens market integrity by providing timely visibility into position concentration risks. The Future Equivalent methodology offers a more accurate representation of market exposure by consolidating futures and options positions into a single metric, enabling better risk assessment and preventive action before limits are breached.