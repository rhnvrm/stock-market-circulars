---
category: compliance
circular_id: 304480a417be8178
date: '2025-11-28'
description: NSE implements revised nomination facilities following SEBI circular
  dated January 10, 2025, requiring capture of opt-out mode (OTP or Video Recording)
  and evidence storage by regulated entities, effective December 15, 2025.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/NMF71524.zip
impact: high
impact_ranking: high
importance_ranking: high
justification: Mandatory compliance requirement affecting all mutual fund transactions
  on NSE MF Invest Platform with specific implementation deadline of December 15,
  2025. Impacts AMCs, RTAs, AMFI, depositories, and depository participants with new
  data capture and evidence storage obligations.
pdf_url: https://nsearchives.nseindia.com/content/circulars/NMF71524.zip
processing:
  attempts: 1
  content_hash: d120dabc9c7b4b53
  processed_at: '2025-11-28T13:05:20.465395'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-11-28T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/NMF71524.zip
severity: high
source: nse
stocks: []
tags:
- amc
- compliance
- depository
- investor-protection
- kyc
- mutual-fund
- nomination-facilities
- rta
- sebi
title: Implementation of Revised Nomination Facilities for Opt-Out on NSE MF Invest
  Platform
---

## Summary

NSE implements revised nomination facilities on the NSE MF Invest Platform in compliance with SEBI circular SEBI/HO/OIAE/OIAE_IAD-3/P/ON/2025/01650 dated January 10, 2025. The changes become effective from December 15, 2025, and introduce new fields for capturing investor opt-out preferences, authentication modes, and reference numbers for non-demat transactions. Regulated entities including AMCs, RTAs, AMFI, depositories, and depository participants must capture and store evidence of investors opting out of nomination facilities.

## Key Points

- New fields added to UCC (Unique Client Code) for non-demat transactions only
- Mode of Opt-Out: Capture investor's preferred mode (OTP-based or Video Recording)
- Opt-out Declaration for OTP-based authorization required
- Unique Reference Number of Opt-Out must be captured
- UCC file structure uses existing fillers - no structural changes
- Three fields modified: NOMINATION OPT (Field 122), Nomination Authentication Mode (Field 123), and NOMINEE OPT OUT REF. NO (Field 176/filler1)
- No impact on existing SIPs, additional purchases, and redemptions in non-demat/physical mode
- No changes to existing transaction processes or reports

## Regulatory Changes

**SEBI Circular Reference**: SEBI/HO/OIAE/OIAE_IAD-3/P/ON/2025/01650 dated January 10, 2025

**Field Structure Changes**:

1. **Field 122 (NOMINATION OPT)**: Mandatory, CHAR(1), Values: Y/N
2. **Field 123 (Nomination Authentication Mode)**: Mandatory, Varchar(1)
   - If NOMINATION OPT = "Y": Must be "W" (Wet Signature) / "E" (E-sign) / "O" (OTP Authentication)
   - If NOMINATION OPT = "N": Must be "O" (OTP with Declaration) or "V" (Video Recording)
3. **Field 176/filler1 (NOMINEE OPT OUT REF. NO)**: Conditional Mandatory, CHAR(20)
   - Mandatory if NOMINATION OPT = "N"
   - Must provide OTP or Video Recording reference number

**Regulated Entities Defined**:
- Asset Management Companies (AMCs) of Mutual Funds and their RTAs
- Association of Mutual Funds in India (AMFI)
- Recognized Depositories
- Registered Depository Participants

## Compliance Requirements

**For AMCs, RTAs, AMFI, Depositories, and Depository Participants**:
- Capture and store evidence of investors opting out of nominees
- Submit evidence to RTA/AMC/Regulator as and when required or at defined intervals
- Members/Distributors must follow the prescribed route for capturing evidence

**For Members on NSE MF Invest Platform**:
- Update UCC processes to capture three new/modified fields for non-demat transactions
- Implement OTP-based authentication or Video Recording mechanism for opt-out
- Obtain opt-out declarations from investors
- Generate and store unique reference numbers for all opt-out transactions
- Ensure existing file structure compatibility (uses fillers, no structural changes)
- Update APIs with additional headers for new fields

**Applicability**:
- Changes apply to non-demat transactions only
- Existing transactions (SIPs, purchases, redemptions) remain unaffected

## Important Dates

- **SEBI Circular Date**: January 10, 2025
- **NSE Circular Date**: November 28, 2025
- **Implementation Date**: December 15, 2025 (effective date)

## Impact Assessment

**Operational Impact**: High - Requires system changes to UCC file structure and API modifications, implementation of new authentication mechanisms (OTP and Video Recording), and evidence storage systems.

**Market Participants Affected**:
- All members trading on NSE MF Invest Platform
- AMCs and their Registrar and Transfer Agents
- AMFI
- Depositories and Depository Participants
- Mutual fund distributors

**Technology Impact**: Medium - Uses existing filler fields in UCC structure minimizing structural changes, but requires API header additions and backend logic for conditional mandatory field validation.

**Investor Impact**: Medium - Investors opting out of nomination must now choose authentication mode and complete either OTP-based declaration or video recording, adding an additional step to the opt-out process.

**Compliance Risk**: High - Non-compliance after December 15, 2025, may result in inability to process new non-demat UCC registrations or opt-out requests. Evidence storage and submission requirements create ongoing compliance obligations.

**Contact Information**:
- Toll Free: 1800 2100 940
- Email: support@nseinvest.com