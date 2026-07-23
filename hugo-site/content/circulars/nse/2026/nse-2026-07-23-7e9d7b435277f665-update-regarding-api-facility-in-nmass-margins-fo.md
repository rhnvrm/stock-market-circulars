---
category: market-operations
circular_id: 7e9d7b435277f665
date: '2025-07-25'
description: NSE Clearing has issued an update on the API facility for NMASS Margins-FO,
  including an encryption/decryption integration guide (AES-256-CBC and RSA) for secure
  data exchange with members.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT75360.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: This is a technical/operational update affecting members' system integration
  with NSE Clearing's NMASS-Margins-FO API; it does not directly affect listed securities
  or trading in specific stocks, but is important for members' operational compliance.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT75360.zip
processing:
  attempts: 1
  content_hash: 9de225b2b58ebcce
  processed_at: '2026-07-23T14:13:52.100869'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-07-23T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT75360.zip
severity: medium
source: nse
stocks: []
tags:
- margins
- collateral
- nmass
- kyc
title: NSE Clearing Update Regarding API Facility in NMASS-Margins-FO
---

## Summary

NSE Clearing Limited (NCL) has issued an update regarding the API Facility in NMASS-Margins-FO, accompanied by an Encryption/Decryption Integration Guide (Annexure) detailing the technical specifications members must follow when exchanging data with the API. The guide covers both AES-256-CBC symmetric encryption for message exchange and RSA-based encryption for secure key/data handling.

## Key Points

- The circular provides members with the technical integration requirements for securely exchanging data via the NMASS-Margins-FO API.
- AES encryption specifications: Algorithm AES-256-CBC with PKCS5Padding, UTF-8 text encoding, and Base64-encoded cipher text output.
- Secret key must be 256 bits (32 bytes) and must match on both encryption and decryption sides; keys should be generated securely and stored safely.
- Initialization Vector (IV) must be 128 bits (16 bytes), shared securely with members, and ideally unique per session.
- Incorrect key or IV length will cause decryption failures, so members must adhere strictly to specified formats.
- A separate RSA Algorithm Integration Guide is also provided for members needing asymmetric encryption/decryption, including key requirements and a reference Java decryption implementation.
- The document outlines member responsibilities for correctly implementing decryption on their end and includes an FAQ section for common integration issues.

## Regulatory Changes

No new regulatory policy changes are introduced; this is an operational/technical update specifying encryption standards and integration requirements for the NMASS-Margins-FO API used by clearing members.

## Compliance Requirements

- Members integrating with the NMASS-Margins-FO API must implement AES-256-CBC (PKCS5Padding) encryption/decryption exactly as specified, using UTF-8 encoding and Base64 cipher text formatting.
- Members must securely generate, store, and exchange the AES secret key and IV, ensuring correct key/IV lengths (32 bytes / 16 bytes respectively) to avoid decryption failures.
- Members using RSA-based flows must follow the specified key requirements and data format expectations, and may reference the provided Java decryption code sample.
- Members are responsible for testing and validating their integration against NCL's specifications before going live.

## Important Dates

No specific effective or deadline dates are mentioned in the extracted content; members should refer to the full circular/annexure for any rollout or compliance timelines.

## Impact Assessment

This update primarily affects clearing members' back-office and IT teams responsible for API integration with NSE Clearing's margin systems. It does not directly impact trading, listed securities, or investors, but non-compliance with the encryption specifications could disrupt a member's ability to exchange margin data via the API, creating operational risk for affected firms.