---
category: market-operations
circular_id: aba1ef5b4e03ad32
date: '2025-07-25'
description: NSE has introduced an API facility in NMASS-Margins-CO, detailing AES
  and RSA encryption/decryption integration guidelines for secure message exchange.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/COM76435.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Introduces technical integration guidelines and API facility for NMASS
  margins.
pdf_url: https://nsearchives.nseindia.com/content/circulars/COM76435.zip
processing:
  attempts: 1
  content_hash: a761a60ed890f2f1
  processed_at: '2026-09-21T20:06:11.923383'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-09-21T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/COM76435.zip
severity: medium
source: nse
stocks: []
tags:
- nmass
- margins
- api
- encryption
- decryption
- security
- nse
title: Introduction of API Facility in NMASS-Margins-CO
---

## Summary

NSE Clearing Limited has introduced an API facility in NMASS-Margins-CO. The circular outlines integration guidelines covering AES-256-CBC and RSA algorithms, key and IV requirements, encryption/decryption flows, and sample implementation code to ensure secure message exchange between systems.

## Key Points

- Integration facility introduced for NMASS-Margins-CO via APIs.
- AES-256-CBC with PKCS5 Padding, UTF-8 encoding, and Base64 cipher text format specified.
- Mandatory requirements for Secret Key (256 bits/32 bytes) and Initialization Vector (IV - 16 bytes/128 bits).
- RSA algorithm integration guidelines and reference Java decryption code provided.

## Regulatory Changes

- Standardization of encryption and decryption protocols for API-based data exchange in NMASS-Margins-CO.

## Compliance Requirements

- Members must ensure correct key and IV lengths (AES 256-bit key, 128-bit IV) and adhere to the specified encryption/decryption flows to prevent integration failures.

## Important Dates

- Effective immediately as per circular issuance.

## Impact Assessment

- Streamlines secure automated communication and margin data exchange for clearing members integrating with the NMASS platform.