---
category: market-operations
circular_id: 992b3a7bf71d016b
date: '2026-08-05'
description: NSE Clearing Limited has released integration guidelines for the NMASS-Margins-SLB
  API facility, detailing secure communication specifications using AES-256-CBC and
  RSA algorithms.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT75584.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Clearing members using NMASS APIs for Securities Lending and Borrowing
  (SLB) margins must implement the updated AES-256-CBC and RSA encryption/decryption
  guidelines for secure automated integration.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT75584.zip
processing:
  attempts: 1
  content_hash: d65082d9bed01e53
  last_updated: '2026-08-12T20:44:59.223984'
  processed_at: '2026-08-12T20:44:50.195439'
  processor_version: '2.0'
  retry_requested_for_stage: claude_failed
  retry_source: backfill
  stage: completed
  status: published
published_date: '2026-08-05T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT75584.zip
severity: medium
source: nse
stocks: []
tags:
- nse
- nmass
- margins
- slb
- api
- encryption
- collateral
title: Update regarding API Facility in NMASS-Margins-SLB
---

## Summary

NSE Clearing Limited (NCL) has provided integration guidelines for the API facility in the NMASS (NSE Management and Administration Support System) portal, specifically for the Margins module in the Securities Lending and Borrowing (SLB) segment. The circular outlines detailed technical requirements for secure message exchange using AES and RSA cryptographic algorithms.

## Key Points

- **AES Security Standards:** Employs AES-256-CBC with PKCS5 Padding, utilizing UTF-8 text encoding and Base64-encoded cipher text for secure message transmission.
- **Symmetric Key & IV Requirements:** Secret keys must be 32 bytes (256 bits) and Initialization Vectors (IV) must be 16 bytes (128 bits), unique per session where possible.
- **RSA Algorithm Integration:** Detailed specifications for asymmetric encryption and decryption to secure transmission channels.
- **Technical Interoperability:** Documentation includes reference Java decryption code to aid members in implementation.

## Regulatory Changes

- No changes to regulatory requirements or policy, but updates the technical security standards for automated member interactions with NCL's margin systems.

## Compliance Requirements

- **API Update:** Members utilizing the NMASS-Margins-SLB API facility must update their encryption/decryption subroutines to comply with the specified AES-256-CBC and RSA guidelines.
- **Security Configuration:** Ensure that keys and IV lengths strictly match the mandatory 256-bit and 128-bit constraints, as incorrect sizes will trigger decryption failures.

## Important Dates

- **Circular Date:** August 5, 2026
- **Effective Date:** Immediate implementation for integrated members

## Impact Assessment

- **Clearing Members:** Moderate technical/operational impact. Integrators and software vendors need to align their automated client systems with the new encryption/decryption flows.
- **Market Operations:** Low direct market impact, but improves operational reliability and security for automated margin queries and reporting in the SLB segment.