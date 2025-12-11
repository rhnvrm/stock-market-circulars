---
category: compliance
circular_id: 29027c3c8cb65ec8
date: '2025-12-10'
description: SEBI relaxes the requirement for NRI clients to be physically located
  in India when undertaking re-KYC through digital mode, allowing geo-location to
  match their country of residence.
draft: false
guid: https://www.sebi.gov.in/legal/circulars/dec-2025/relaxation-on-geo-tagging-requirement-in-india-for-nris-while-undertaking-re-kyc_98284.html
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: This circular provides operational ease for NRI clients and intermediaries
  by relaxing geo-location requirements for re-KYC, but does not fundamentally change
  KYC obligations or affect market operations directly.
pdf_url: https://www.sebi.gov.in/sebi_data/attachdocs/dec-2025/1765366958310.pdf
processing:
  attempts: 1
  content_hash: c6c429053dc69aed
  processed_at: '2025-12-11T06:41:24.550601'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-10T00:00:00+05:30'
rss_url: https://www.sebi.gov.in/legal/circulars/dec-2025/relaxation-on-geo-tagging-requirement-in-india-for-nris-while-undertaking-re-kyc_98284.html
severity: low
source: sebi
stocks: []
tags:
- kyc
- nri
- re-kyc
- digital-onboarding
- geo-tagging
- compliance
- client-onboarding
- intermediaries
title: Relaxation on Geo-Tagging Requirement in India for NRIs During Re-KYC
---

## Summary

SEBI has modified the Master Circular on KYC to ease the re-KYC process for Non-Resident Indians (NRIs). The requirement that clients must be physically located in India during digital KYC verification has been relaxed specifically for NRI clients undertaking re-KYC. However, the GPS location captured must still match the latitude and longitude of the country mentioned in the client's Proof of Address.

## Key Points

- Physical location requirement in India is relaxed for NRI clients during re-KYC through digital mode
- Relaxation applies only to existing clients undergoing re-KYC, not new client onboarding
- GPS location must match the country specified in the client's Proof of Address
- Apps must prevent connections from spoofed IP addresses
- Random action initiation and time stamping features remain mandatory
- Modification applies to Para 51 of Master Circular on KYC dated October 12, 2023

## Regulatory Changes

Para 51 of the Master Circular on KYC (dated October 12, 2023) has been amended to include:

1. **Relaxation for NRIs**: The requirement of physical location being in India during digital onboarding is now relaxed for undertaking re-KYC for existing NRI clients.

2. **Geographic Validation**: The app must ensure that GPS location (latitude and longitude) captured matches with the latitude and longitude of the country given in Proof of Address provided by the client.

3. **Retained Requirements**: Apps must continue to have features for random action initiation, time stamping, and prevention of spoofed IP address connections.

## Compliance Requirements

**Applicable to:**
- All intermediaries registered with SEBI under Section 12 of SEBI Act, 1992
- Stock Exchanges

**Action Required:**
- Update digital KYC systems to allow geo-location outside India for NRI re-KYC
- Ensure GPS validation matches client's country of residence as per Proof of Address
- Maintain anti-spoofing controls for IP addresses
- Continue implementing random action initiation and time stamping features

## Important Dates

- **Circular Issue Date**: December 10, 2025
- **Effective Date**: Immediate (no transition period specified)

## Impact Assessment

**Operational Impact:**
- Significantly improves accessibility for NRI clients seeking to complete re-KYC requirements
- Reduces operational friction for intermediaries serving NRI clientele
- May increase re-KYC compliance rates among NRI investors

**Market Impact:**
- Low direct market impact
- Potentially positive for brokers and intermediaries with large NRI client bases
- Addresses stakeholder concerns regarding KYC access barriers

**Technical Impact:**
- Intermediaries may need to update their digital KYC apps to validate international geo-locations
- Systems must be configured to cross-verify GPS coordinates with country data from Proof of Address documents