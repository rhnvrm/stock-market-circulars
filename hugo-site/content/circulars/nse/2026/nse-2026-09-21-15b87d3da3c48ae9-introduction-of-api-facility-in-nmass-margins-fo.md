---
category: market-operations
circular_id: 15b87d3da3c48ae9
date: '2025-07-25'
description: NSE Clearing Limited introduces an API facility for NMASS-Margins-FO,
  detailing cryptographic guidelines including AES-256-CBC and RSA integration.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT76433.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Provides technical integration guidelines and API facility details
  for clearing members participating in the NMASS-Margins-FO segment.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT76433.zip
processing:
  attempts: 1
  content_hash: 41e356cfa3a6a405
  processed_at: '2026-09-21T12:16:16.680680'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-09-21T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT76433.zip
severity: medium
source: nse
stocks: []
tags:
- nmass
- margins
- futures-and-options
- api-integration
- encryption-guidelines
title: Introduction of API Facility in NMASS-Margins-FO
---

## Summary

NSE Clearing Limited has announced the introduction of an API facility in NMASS-Margins-FO. The circular includes detailed integration guides for secure message exchange using AES-256-CBC and RSA algorithms, specifying mandatory key requirements, encryption and decryption flows, and reference implementation details.

## Key Points

- Introduction of API facility for NMASS-Margins-FO.
- Detailed AES-256-CBC configuration with PKCS5 padding and Base64 encoding for cipher text output.
- Mandatory requirements for 256-bit secret keys and 128-bit Initialization Vectors (IV).
- Clear separation of encryption and decryption flows for members.

## Regulatory Changes

- Integration guidelines established for secure electronic communication and data exchange within the NMASS-Margins-FO segment.

## Compliance Requirements

- Clearing members must ensure correct key and IV lengths (32 bytes for keys, 16 bytes for IVs) to prevent decryption failures.
- Members must securely store secret keys and handle initialization vectors appropriately.

## Important Dates

- Refer to the main circular notification for operational rollout and effective implementation timelines.

## Impact Assessment

- Streamlines automated margin processing and secure data transmission for trading members interfacing with the NMASS-Margins-FO platform.