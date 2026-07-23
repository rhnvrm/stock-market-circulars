---
category: market-operations
circular_id: 1312996f81a0d970
date: '2026-07-23'
description: NSE Clearing Limited circular providing an update on the API facility
  for NMASS Margins-CO, accompanied by an Encryption/Decryption Integration Guide
  covering AES-256-CBC and RSA algorithms for secure message exchange with members.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/COM75362.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Circular is an operational/technical update for members on the NMASS
  Margins-CO API facility, including a mandatory encryption/decryption integration
  guide; relevant to clearing members' system integration but does not directly affect
  listed securities or trading.
pdf_url: https://nsearchives.nseindia.com/content/circulars/COM75362.zip
processing:
  attempts: 1
  content_hash: 16508bdf513d2baf
  processed_at: '2026-07-23T14:13:22.086610'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-07-23T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/COM75362.zip
severity: medium
source: nse
stocks: []
tags:
- margins
- collateral
- margin-collection
- nmass
- clearing-corporation
- api-integration
title: Update Regarding API Facility in NMASS-Margins-CO
---

## Summary

NSE Clearing Limited (NCL) has issued an update regarding the API Facility in NMASS (NSE Margin Analysis and Settlement System) for Margins-CO (Client Obligation). The circular includes a detailed Encryption/Decryption Integration Guide (Annexure) specifying the technical standards members must follow to securely exchange data through the API, covering both AES and RSA based encryption mechanisms.

## Key Points

- The circular pertains to an update on the API facility available for NMASS Margins-CO reporting/data exchange.
- An Encryption/Decryption Integration Guide is attached as an annexure, detailing mandatory cryptographic standards for API-based data exchange with NSE Clearing.
- Two encryption mechanisms are specified: AES-256-CBC (for symmetric encryption of message payloads) and RSA (for key/data exchange, details continued in later sections of the guide).
- AES specifications: Algorithm AES, Mode CBC, Padding PKCS5Padding, Secret Key size 256 bits (32 bytes), IV size 128 bits (16 bytes), Text Encoding UTF-8, Cipher Output Base64 encoded string.
- The secret key must be identical on both encryption and decryption ends and must be generated and stored securely.
- The Initialization Vector (IV) must be 16 bytes, shared securely with members, and ideally unique per session.
- Incorrect key or IV length will cause decryption failure.
- Encryption flow: convert plain text to UTF-8 bytes, encrypt using AES/CBC/PKCS5Padding, encode to Base64, and transmit.
- Decryption flow: decode Base64 cipher text, decrypt using the same AES key and IV, and convert decrypted bytes back to UTF-8 string.
- The document also outlines an RSA Algorithm Integration Guide (overview, purpose, key requirements, data format expectations, decryption flow, and reference Java code) for members' side implementation, along with member responsibilities and FAQs.

## Regulatory Changes

No new regulatory requirement is introduced; this is a technical/operational update establishing standardized encryption protocols (AES-256-CBC and RSA) that members must implement for secure API-based communication with NSE Clearing under the NMASS Margins-CO facility.

## Compliance Requirements

- Members integrating with the NMASS Margins-CO API must implement AES-256-CBC (with PKCS5 padding, UTF-8 encoding, Base64 cipher output) and RSA encryption/decryption exactly as specified in the guide.
- Members must ensure the secret key (256-bit) and IV (128-bit) match between encryption and decryption sides and are stored/exchanged securely.
- Members are responsible for correct implementation per the reference sample code and for adhering to the data format expectations outlined in the RSA section.
- Members should consult the FAQs section of the guide for common integration issues.

## Important Dates

No specific effective date, deadline, or compliance date is stated in the extracted content; members should refer to the full circular/annexure for any implementation timelines.

## Impact Assessment

This is a technical/operational circular primarily affecting clearing members' IT and integration teams responsible for connecting to the NMASS Margins-CO API. It does not directly impact trading, listed securities, or market pricing, but non-compliance with the specified encryption standards could result in failed data exchange (decryption failures) between members and NSE Clearing, affecting margin reporting operations.