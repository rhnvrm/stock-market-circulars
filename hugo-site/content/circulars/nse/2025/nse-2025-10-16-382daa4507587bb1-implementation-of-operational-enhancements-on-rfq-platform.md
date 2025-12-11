---
category: trading
circular_id: 382daa4507587bb1
date: '2025-10-16'
description: NSE introduces four key operational enhancements to the RFQ platform
  including mandatory broker execution for brokered transactions, yield-price calculator,
  client holdings upload facility, and FIX API integration, effective October 28,
  2025.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/DS70879.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Moderate impact affecting debt market participants using RFQ platform;
  requires operational adjustments by brokers and participants for brokered transactions
  and optional adoption of new features like FIX API.
pdf_url: https://nsearchives.nseindia.com/content/circulars/DS70879.pdf
processing:
  attempts: 1
  content_hash: 24b1685945637eae
  processed_at: '2025-10-16T19:01:05.283457'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-16T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/DS70879.pdf
severity: medium
source: nse
stocks: []
tags:
- broker-execution
- debt-securities
- fix-api
- operational-enhancements
- otm-transactions
- rfq-platform
- risk-management
- sebi-order
- trading-platform
- yield-calculator
title: Implementation of Operational Enhancements on RFQ Platform
---

## Summary

NSE has implemented four major operational enhancements to the RFQ (Request for Quote) platform for the debt segment, as per SEBI directions and recommendations. These changes aim to improve platform efficiency, transparency, and user experience. Key modifications include mandatory broker execution for brokered OTM transactions, introduction of an independent yield-price calculator, optional client holdings upload facility for risk management, and FIX API integration for enhanced connectivity.

## Key Points

- Manual marking of 'Brokered' transactions in One-to-Many (OTM) mode removed; brokers must now execute brokered transactions on behalf of participants
- Participants can continue to execute 'Direct' transactions themselves in OTM mode
- New standalone yield-price calculator feature enables conversion between clean/dirty price and yield for any ISIN
- Optional facility for brokers to upload client holdings and cash positions for risk mitigation
- FIX API integration introduced as additional connectivity option alongside existing RFQ API
- FIX API currently available in UAT environment for testing and integration
- All changes effective from October 28, 2025

## Regulatory Changes

These enhancements have been implemented as per SEBI direction and recommendations to improve the RFQ platform's operational framework. The key regulatory-driven change is the removal of the manual 'Brokered' transaction marking option, which now mandates brokers to execute such transactions directly on the platform, enhancing transparency and accountability in brokered deals.

## Compliance Requirements

**For Brokers:**
- Must execute all brokered transactions on behalf of participants through the RFQ Platform in OTM mode
- May optionally utilize the client holdings upload facility to upload client holdings and cash positions for risk management purposes
- Should begin FIX API integration and validation in UAT environment if planning to adopt the new interface

**For Participants:**
- Can no longer manually mark OTM deals as 'Brokered'
- Must route brokered transactions through brokers for execution
- Continue to have ability to execute 'Direct' transactions in OTM mode
- May selectively disclose portfolio holdings to brokers for improved trade execution certainty

## Important Dates

- **October 16, 2025**: Circular issued
- **October 28, 2025**: All operational enhancements become effective
- **Current**: FIX API available in UAT environment for testing

## Impact Assessment

**Operational Impact:**
- Brokers will need to adjust operational workflows to handle execution of brokered transactions on behalf of clients
- Participants lose direct control over marking brokered transactions but gain improved transparency
- Optional client holdings upload may reduce trade failures and short sales, improving settlement efficiency

**Technology Impact:**
- FIX API introduction provides global standard integration option, potentially easing connectivity for international participants
- Participants have flexibility to choose between RFQ API and FIX API based on system requirements
- UAT testing period allows adequate time for system integration before production rollout

**Risk Management Impact:**
- Client holdings upload facility enables better pre-trade risk assessment
- Reduced likelihood of settlement failures through improved visibility of client positions
- Enhanced certainty in trade execution for brokers with access to client holdings data

**Market Efficiency:**
- Yield-price calculator as standalone feature improves pricing transparency and reduces calculation errors
- Streamlined brokered transaction process may improve execution speed and audit trail

**Contact Information:**
- RFQ Platform Helpdesk: 1800 266 0050 (Option 1)
- Email: DL-DEBT-BD@nse.co.in