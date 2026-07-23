---
category: market-operations
circular_id: dcf120b2ee58b44b
date: '2025-07-25'
description: NSE Clearing Limited has issued an updated Encryption/Decryption Integration
  Guide for the API facility used in NMASS-Margins-CM, specifying AES-256-CBC and
  RSA algorithm requirements for secure message exchange with members.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT75359.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical/operational update affecting members' API integration for
  margin data exchange under NMASS; does not directly impact listed securities or
  trading but requires compliance action from clearing members' technology teams.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT75359.zip
processing:
  attempts: 1
  content_hash: 7b2761db8aba877d
  processed_at: '2026-07-23T22:11:53.706805'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-07-23T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT75359.zip
severity: medium
source: nse
stocks: []
tags:
- margins
- collateral
- nse
- master-circular
title: 'Update Regarding API Facility in NMASS-Margins-CM: Encryption/Decryption Integration
  Guide'
---

## Summary

NSE Clearing Limited (NCL) has released an updated Annexure titled "Encryption / Decryption Integration Guide" as part of the API Facility in NMASS-Margins-CM (National Margin Aggregation and Settlement System). The guide specifies the technical standards for encrypting and decrypting data exchanged between NCL and members through the API facility, covering both AES and RSA based encryption mechanisms.

## Key Points

- The circular provides members with a standardized Encryption/Decryption Integration Guide to ensure interoperability while exchanging margin-related data via the NMASS API facility.
- Two algorithms are specified: AES (AES-256-CBC with PKCS5 Padding) for symmetric encryption and RSA for asymmetric encryption.
- AES configuration: Algorithm - AES, Mode - CBC (Cipher Block Chaining), Padding - PKCS5Padding, Secret Key Size - 256 bits (32 bytes), IV Size - 128 bits (16 bytes), Text Encoding - UTF-8, Cipher Output - Base64 encoded string.
- Secret key and Initialization Vector (IV) must match exactly between encryption and decryption sides; incorrect key or IV length will cause decryption failure.
- The IV should ideally be unique per session and must be shared securely with members.
- Encryption flow: convert plain text to UTF-8 bytes, encrypt using AES/CBC/PKCS5Padding, encode to Base64, and transmit the Base64 cipher text.
- Decryption flow: decode Base64 cipher text, decrypt using the same AES key and IV, and convert decrypted bytes back to a UTF-8 string.
- The annexure also includes an RSA Algorithm Integration Guide covering key requirements, data format expectations, and the RSA decryption flow to be implemented on the members' side, along with reference Java decryption code.
- Members' responsibilities and a FAQ section are included to assist technology teams with implementation.

## Regulatory Changes

This is a technical/operational update rather than a regulatory rule change. It formalizes the encryption/decryption standards members must implement to securely consume the NMASS-Margins-CM API facility.

## Compliance Requirements

- Members and their technology/IT teams integrating with the NMASS-Margins-CM API must implement AES-256-CBC (PKCS5 padding) and RSA decryption exactly as specified in the guide.
- Secret keys must be 256 bits and IVs must be 128 bits; both must be securely stored and securely shared between NCL and the member.
- Members should use the reference sample code (AES and Java-based RSA decryption code) provided in the annexure to ensure correct implementation and avoid decryption failures.

## Important Dates

No specific effective date, deadline, or transition timeline is mentioned in the extracted content; members should refer to the full circular/annexure for any implementation timeline.

## Impact Assessment

The update is operational in nature, primarily affecting clearing members' technology and IT teams responsible for integrating with NCL's NMASS-Margins-CM API. Correct implementation of the specified encryption/decryption standards is necessary to ensure secure and error-free exchange of margin data; incorrect key/IV configuration could result in data exchange failures. There is no direct impact on trading activity, listed securities, or investors.