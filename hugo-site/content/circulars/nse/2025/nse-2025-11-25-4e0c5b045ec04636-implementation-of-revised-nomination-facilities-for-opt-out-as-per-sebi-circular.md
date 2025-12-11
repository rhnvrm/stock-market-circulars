---
category: compliance
circular_id: 4e0c5b045ec04636
date: '2025-11-25'
description: NSE implements revised nomination facilities allowing investors to opt-out
  via OTP-based authentication or video recording, effective December 15, 2025.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/NMF71461.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational change affecting mutual fund investor onboarding and nomination
  processes; requires system updates but no immediate market impact
pdf_url: https://nsearchives.nseindia.com/content/circulars/NMF71461.zip
processing:
  attempts: 1
  content_hash: 49b5f38d93ff242c
  processed_at: '2025-11-25T12:45:37.925911'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-11-25T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/NMF71461.zip
severity: medium
source: nse
stocks: []
tags:
- compliance
- declaration
- investor-protection
- kyc
- mutual-fund
- nomination
- opt-out
- sebi-order
- trading-platform
title: Implementation of Revised Nomination Facilities for Opt-Out as per SEBI Circular
  on NSE MF Invest Platform
---

## Summary

NSE has issued implementation guidelines for revised nomination facilities on the NSE MF Invest Platform, following SEBI circular SEBI/HO/OIAE/OIAE_IAD-3/P/ON/2025/01650 dated January 10, 2025. The changes enable investors to formally opt-out of nomination through two methods: OTP-based authentication with declaration or video recording. The revised facilities will be effective from December 15, 2025, and apply only to non-demat transactions.

## Key Points

- Three new fields added to UCC (Unique Client Code) structure for non-demat transactions
- Mode of Opt-Out field captures investor's preferred opt-out method (OTP or Video)
- Opt-out Declaration field obtains investor declaration for OTP-based authentication
- Unique Reference Number field captures the reference number of the opt-out process
- Existing fillers in UCC file structure will be utilized; no structural changes to existing format
- Additional headers will be added in APIs for these new fields
- No impact on existing SIPs, additional purchases, and redemptions in non-demat/physical mode
- No changes to existing transaction processes or reports

## Regulatory Changes

The circular implements SEBI's revised nomination framework with the following technical specifications:

**Field Structure Updates:**
- Field 122 (NOMINATION OPT): Character field, size 1, mandatory, values Y/N
- Field 176 (NOMINEE OPT OUT PROOF): Character field, size 1, conditional mandatory - required if NOMINATION OPT is 'N'; values: 'O' for OTP with declaration, 'V' for video recording
- Field 177 (NOMINEE OPT OUT REF. NO): Character field, size 20, conditional mandatory - required if NOMINATION OPT is 'N'; stores OTP/video recording reference number

**Regulated Entities Responsibilities:**
The following entities must capture and store opt-out evidence:
- AMCs of Mutual Funds and their RTAs
- AMFI
- Recognized Depositories
- Registered Depository Participants

## Compliance Requirements

**For Trading Members:**
- Update UCC registration systems to capture three new nomination opt-out fields
- Implement OTP-based authentication workflow for opt-out declarations
- Implement video recording workflow as alternative opt-out method
- Maintain unique reference numbers for all opt-out transactions
- Apply changes only to non-demat transactions
- Ensure existing transactions remain unaffected

**For Regulated Entities:**
- Capture and securely store evidence of investors opting out of nomination
- Submit evidence to RTA/AMC/Regulator on demand or at defined intervals
- Maintain audit trail of opt-out processes

**Declaration Requirements:**
Investors opting out must confirm they:
- Do not wish to appoint nominee(s) for mutual fund units
- Understand the issues involved in non-appointment of nominees
- Are aware that legal heirs will need to submit court documents or documents from competent authority based on asset value in the folio

## Important Dates

- **January 10, 2025**: SEBI circular issued (SEBI/HO/OIAE/OIAE_IAD-3/P/ON/2025/01650)
- **November 25, 2025**: NSE implementation circular issued
- **December 15, 2025**: Revised nomination facilities become effective

## Impact Assessment

**Operational Impact:**
- Medium impact on mutual fund platform operators requiring system updates to UCC registration processes
- Technology teams need to implement two distinct opt-out workflows (OTP and video recording)
- API modifications required to handle additional headers for new fields
- Database schema updates needed to store opt-out evidence and reference numbers

**Investor Impact:**
- Enhanced investor protection through formalized opt-out process
- Additional documentation burden for investors choosing to opt-out of nomination
- Legal heirs of deceased investors without nominees will face increased documentation requirements

**Market Impact:**
- Low immediate market impact; primarily an operational and compliance update
- Applies only to new UCC registrations and modifications post-December 15, 2025
- Existing portfolios and transactions continue without disruption
- No changes to trading, settlement, or existing SIP/redemption processes