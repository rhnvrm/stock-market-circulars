---
category: market-operations
circular_id: 27c6ab079a28b78d
date: '2025-07-25'
description: NSE Clearing Limited has introduced an API facility for NMASS-Margins-CD,
  detailing AES and RSA encryption/decryption integration guidelines.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CD76434.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Provides technical integration guidelines for API-based margin operations
  in the currency derivatives segment.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CD76434.zip
processing:
  attempts: 1
  content_hash: 64c75b7167d4c201
  processed_at: '2026-09-21T20:06:26.773933'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-09-21T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CD76434.zip
severity: medium
source: nse
stocks: []
tags:
- api
- nmass
- margins
- encryption
- decryption
- clearing-operations
title: Introduction of API Facility in NMASS-Margins-CD
---

## Summary

NSE Clearing Limited has introduced an API facility in NMASS-Margins-CD. The circular provides comprehensive technical documentation and integration guidelines covering AES and RSA encryption/decryption workflows for secure message exchange between systems.

## Key Points

- Integration guidelines for AES-256-CBC with PKCS5 Padding, UTF-8 encoding, and Base64 cipher text output.
- Mandatory secret key (256 bits / 32 bytes) and IV (128 bits / 16 bytes) requirements.
- Step-by-step encryption and decryption flows for secure data transmission.
- RSA algorithm integration guidelines, purpose, key requirements, data formats, and member responsibilities.

## Regulatory Changes

- Implementation of standardized encryption and decryption protocols for API-based margin systems in the currency derivatives segment.

## Compliance Requirements

- Members must ensure correct key and IV lengths (AES-256 and 16-byte IV) to avoid decryption failures.
- Secure generation and storage of keys and initialization vectors.

## Important Dates

- Effective immediately as per the release of the technical specifications.

## Impact Assessment

- Enhances security and data interoperability for trading members integrating with the NMASS-Margins-CD API facility.