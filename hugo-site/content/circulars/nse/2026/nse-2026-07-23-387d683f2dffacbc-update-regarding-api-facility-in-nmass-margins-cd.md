---
category: market-operations
circular_id: 387d683f2dffacbc
date: '2025-07-25'
description: NSE Clearing has issued an update on the API facility for NMASS-Margins-CD,
  including an Encryption/Decryption Integration Guide covering AES and RSA algorithm
  specifications for secure data exchange with members.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CD75361.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: This is a technical/operational update relevant to clearing members
  integrating with NSE Clearing's NMASS-Margins-CD API; it affects backend systems
  and compliance for members rather than broader market pricing or trading activity.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CD75361.zip
processing:
  attempts: 1
  content_hash: d9d379857b57e402
  processed_at: '2026-07-23T14:12:56.684906'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-07-23T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CD75361.zip
severity: medium
source: nse
stocks: []
tags:
- margins
- collateral
- market-operations
- product-launch
title: Update regarding API Facility in NMASS-Margins-CD
---

## Summary

NSE Clearing Limited (NCL) has released an update regarding the API Facility for NMASS-Margins-CD, accompanied by an Encryption/Decryption Integration Guide. This annexure specifies the technical standards members must follow to securely encrypt and decrypt data exchanged with NSE Clearing's NMASS-Margins-CD (National Margin System - Margins for Clearing Data) API, covering both AES and RSA based algorithms.

## Key Points

- The circular provides an "Annexure - Encryption Decryption Guide" detailing the technical integration requirements for members connecting to the NMASS-Margins-CD API facility.
- AES-256-CBC with PKCS5 Padding is mandated for symmetric encryption of message payloads.
- Cipher text must be UTF-8 encoded prior to encryption and Base64 encoded after encryption.
- A separate RSA-based algorithm guide is provided for asymmetric encryption requirements, including key requirements, data format expectations, and a reference Java decryption implementation.
- The document includes sample code and a FAQ section to assist members with implementation.

## Regulatory Changes

No change to existing trading, margin, or settlement regulations is introduced. This is a technical/operational specification governing secure API-based data exchange for the NMASS-Margins-CD facility.

## Compliance Requirements

- Members integrating with the NMASS-Margins-CD API must implement AES-256-CBC (PKCS5 padding) encryption/decryption using a mutually agreed 256-bit secret key and 128-bit Initialization Vector (IV).
- The secret key and IV must be identical on both encryption and decryption sides, generated securely, and shared/stored safely; incorrect key or IV length will result in decryption failure.
- Members must also implement RSA-based decryption on their side per the reference guide and Java sample code provided.
- Members are responsible for validating their encryption/decryption setup against NSE Clearing's specifications before going live on the API.

## Important Dates

No specific effective date or deadline is stated in the extracted content; members should refer to the full circular/annexure for any specified implementation timeline.

## Impact Assessment

The update primarily affects the technical/IT teams of clearing members using the NMASS-Margins-CD API, requiring them to implement or update encryption/decryption modules per the specified AES/RSA standards. There is no direct impact on trading, listed securities, or market pricing; impact is confined to backend system compliance and secure data interoperability for margin-related data exchange with NSE Clearing.