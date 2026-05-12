---
category: market-operations
circular_id: 7492f596c7566b62
date: '2026-05-12'
description: NSE Clearing Limited provides API specifications for payment aggregators
  to submit Global MIS data for Mutual Fund Service System, including authentication,
  encryption, and request/response field definitions.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MFSS74181.pdf
impact: medium
impact_ranking: medium
importance_ranking: low
justification: Technical API specification circular targeting a narrow audience of
  payment aggregators using own systems; operationally significant for affected participants
  but no broad market or regulatory impact.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MFSS74181.pdf
processing:
  attempts: 1
  content_hash: 14b359ace311fd9c
  processed_at: '2026-05-12T17:18:11.412188'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-12T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MFSS74181.pdf
severity: low
source: nse
stocks: []
tags:
- mutual-fund
- mfss
- payment-aggregator
- api
- global-mis
- nse-clearing
- technical-specification
- authentication
title: API for Mutual Fund Global MIS by Payment Aggregators
---

## Summary

NSE Clearing Limited (NCL), via circular NCL/MFSS/74181 dated May 12, 2026 (Ref. No. 0167/2026), provides detailed API specifications for payment aggregators participating in the Mutual Fund Service System (MFSS). This is a follow-up to circular NCL/MFSS/74000 dated April 30, 2026. Participants using their own payment aggregators must implement these APIs to submit Global MIS data to NSE.

## Key Points

- Applies to MFSS participants using their own payment aggregators
- API endpoint: `POST https://{{API URL}}/nsemfAmc/api/v1/globalmis`
- Authentication uses AES-128 bit encryption with an API Member License Key and random salt/IV values
- Encrypted password format: `base64(iv::salt::aes_encrypted_val)`
- Authorization header must carry `base64(Login User ID: Encrypted Password)`
- IP whitelisting is mandatory; unregistered IPs receive a `403 FORBIDDEN` error
- 17 fields defined in the Global MIS request, including mandatory fields for member ID, client ID, amount, UTR number, IFSC, account number, and funds transfer mode

## Regulatory Changes

This circular introduces no new regulatory rules but formalises technical API integration requirements for payment aggregators as a follow-up to NCL/MFSS/74000 (April 30, 2026).

## Compliance Requirements

- Participants must whitelist their IP addresses with NSE before using the API
- API credentials (API Secret and API Member License Key) must be obtained from NSE
- Requests must include all mandatory fields: `unique_request_id`, `member_id`, `client_id`, `amount`, `funds_receipt_date`, `utr_number`, `ifsc_number`, `pg_bank_reff_number`, `account_number`, `funds_transfer_pay_mode`, and `bank_code`
- Authentication parameters must be passed as request headers with `Content-Type: application/Json`

## Important Dates

- **May 12, 2026**: Circular issued (NCL/MFSS/74181)
- **April 30, 2026**: Preceding circular NCL/MFSS/74000 issued (reference baseline)
- No explicit go-live or deadline date stated in this circular

## Impact Assessment

Impact is limited to MFSS participants who use their own payment aggregators for mutual fund transactions. These entities must implement the specified API integration, including AES-128 encryption logic and IP whitelisting, to continue submitting Global MIS data. No impact on retail investors, listed companies, or broader market operations.