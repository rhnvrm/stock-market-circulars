---
category: market-operations
circular_id: 85faf830e58dca76
date: '2026-06-17'
description: NSE Clearing issues an encryption and decryption integration guide for
  the API facility in NMASS Margins for the Futures & Options segment, detailing AES-256-CBC
  and RSA algorithm requirements for secure data exchange.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT74751.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical operational circular from NSE Clearing on API security for
  the NMASS Margins F&O facility; relevant to members integrating with the margin
  system but does not introduce new regulatory obligations or affect broader market
  pricing.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT74751.zip
processing:
  attempts: 1
  content_hash: 0981d1c2d352c065
  processed_at: '2026-06-17T15:51:26.665736'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-17T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT74751.zip
severity: medium
source: nse
stocks: []
tags:
- margins
- api
- futures-and-options
- nse
- collateral
- encryption
- market-operations
title: Update regarding API Facility in NMASS-Margins-FO
---

## Summary

NSE Clearing Limited has issued an Encryption/Decryption Integration Guide for members using the API facility in NMASS-Margins for the Futures & Options (FO) segment. The guide specifies the cryptographic standards and implementation requirements that members must follow to ensure secure and interoperable communication with NSE Clearing's systems.

## Key Points

- The API facility uses **AES-256-CBC with PKCS5 Padding** for symmetric encryption; cipher text is Base64-encoded.
- A 256-bit (32-byte) secret key and a 128-bit (16-byte) Initialization Vector (IV) are mandatory; incorrect lengths will cause decryption failure.
- **RSA asymmetric encryption** is also used; the guide provides key requirements, data format expectations, and a reference Java decryption implementation for members.
- Members are responsible for securely generating, storing, and handling their cryptographic keys.
- The IV should be unique per session where possible (recommended best practice).
- Reference sample code is provided for both AES and RSA integration.

## Regulatory Changes

No new regulatory rules are introduced. This circular provides a technical implementation guide to support the existing NMASS-Margins API facility for the FO segment.

## Compliance Requirements

- Members integrating with the NMASS-Margins API must implement AES-256-CBC encryption/decryption as specified.
- Secret keys and IVs must meet the mandatory size requirements (256-bit key, 128-bit IV).
- Members must follow the RSA decryption flow on the member side as described in the guide.
- Members are responsible for the secure storage and handling of all cryptographic material.

## Important Dates

No specific effective date or deadline is mentioned in the available circular content.

## Impact Assessment

This circular impacts trading members and participants who use or plan to use the NMASS API facility for Futures & Options margin-related operations. The technical specifications ensure secure data exchange between member systems and NSE Clearing. Members who do not implement the specified encryption standards correctly may face API integration failures. The impact is operational and confined to the technology teams responsible for member-side API integration.