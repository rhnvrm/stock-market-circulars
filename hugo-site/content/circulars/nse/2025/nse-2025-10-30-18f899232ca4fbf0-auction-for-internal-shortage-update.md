---
category: market-operations
circular_id: 18f899232ca4fbf0
date: '2025-10-30'
description: NSE Clearing introduces close-out mechanism for unsuccessful internal
  shortage auctions, debiting members at auction rate and crediting at close-out price,
  effective from November 14, 2025.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT71045.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Introduces operational change to internal shortage auction mechanism
  affecting settlement process for clearing members with unsuccessful auctions
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT71045.zip
processing:
  attempts: 1
  content_hash: 29ad4abde27ebe4e
  processed_at: '2025-10-30T15:28:19.730640'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-30T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT71045.zip
severity: medium
source: nse
stocks: []
tags:
- auction
- auction-mechanism
- capital-market
- clearing
- close-out
- internal-shortage
- settlement
title: 'Auction for Internal Shortage - Update: Close-out Process for Unsuccessful
  Auctions'
---

## Summary

NSE Clearing Limited (NCL) has announced changes to the auction process for internal shortages. When auctions for internal shortages are unsuccessful, NCL will now close-out such shortages by debiting the member at the auction rate and crediting the member at the close-out price. This change will be implemented from auction trade date November 14, 2025 (settlement date November 17, 2025, Auction Settlement number 2025216). The details will be provided in the existing delivery report with specific transaction indicators.

## Key Points

- Close-out mechanism introduced for unsuccessful internal shortage auctions
- Members will be debited at auction rate and credited at close-out price
- Changes reference section 7.13(iv) of NCL Consolidated Circular NCL/CMPT/67751 dated April 29, 2025
- Details provided in existing delivery report: Delivery_NCL_CM_Auction_CM_<membercode>_YYYYMMDD_P_0000.csv
- Transaction indicator 'CLO' identifies close-out transactions
- Transaction type 'I' for debit (pay-in) and 'O' for credit (pay-out)
- Settlement occurs on auction settlement date

## Regulatory Changes

This circular updates the auction mechanism for internal shortages in the Capital Market segment. Previously, the process for unsuccessful internal shortage auctions was not explicitly defined with a close-out mechanism. The new process establishes a systematic close-out procedure where:

- Unsuccessful auction shortages are closed out automatically
- Members are debited at the auction rate (pay-in transaction)
- Members are credited at the close-out price (pay-out transaction)
- The differential amount is settled through the clearing mechanism

## Compliance Requirements

**For All Members:**
- Update internal systems to handle close-out transactions with TxInd value 'CLO'
- Configure settlement systems to process both debit and credit transactions for unsuccessful auctions
- Review delivery reports for close-out records starting from November 14, 2025
- Ensure accounting systems can reconcile auction rate debits and close-out price credits

**Report File Changes:**
- Monitor field TxInd for value 'CLO' (close-out transactions)
- Process field TxTp: 'I' for debit/pay-in, 'O' for credit/pay-out
- Extract settlement date from field DueDt
- Use SqrOffORValtnPric for auction rate (pay-in) and close-out price (pay-out)
- Calculate amounts using QtyORShrtQty × SqrOffORValtnPric
- Settlement amount provided in field SqrOffORValtnAmt

## Important Dates

- **Circular Date:** October 30, 2025
- **Implementation Date (Auction Trade Date):** November 14, 2025
- **Settlement Date:** November 17, 2025
- **Auction Settlement Number:** 2025216

## Impact Assessment

**Operational Impact:**
- Members must update their systems to process the new close-out transaction types
- Risk management systems need recalibration to account for price differentials between auction rate and close-out price
- Settlement reconciliation processes require modification to handle dual pricing mechanism

**Financial Impact:**
- Members with unsuccessful internal shortage auctions will face price risk between auction rate and close-out price
- Potential gains or losses depending on market movement between auction and close-out pricing
- Enhanced certainty in settlement process as unsuccessful auctions will be automatically closed out

**Market Impact:**
- Improved settlement efficiency by automating close-out of unsuccessful internal shortage auctions
- Reduced operational burden on clearing members for manual shortage resolution
- Better price discovery and risk management in auction process

**Contact Information:**
- Telephone: 18002660050 (IVR Option 2)
- Email: securities_ops@nsccl.co.in