---
category: compliance
circular_id: d410c6b0c23fc172
date: '2025-12-10'
description: NSE implements revised nomination opt-out facility as per SEBI circular
  dated January 10, 2025, requiring OTP authentication or video recording for investors
  opting out of nomination on the MF Invest platform, effective December 15, 2025.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/NMF71746.zip
impact: medium
impact_ranking: medium
importance_ranking: high
justification: High importance due to mandatory compliance requirement affecting all
  mutual fund investors opting out of nomination. Medium impact as it affects only
  those choosing opt-out option, with clear implementation timeline.
pdf_url: https://nsearchives.nseindia.com/content/circulars/NMF71746.zip
processing:
  attempts: 1
  content_hash: 99792c50a9b7a010
  processed_at: '2025-12-10T16:02:42.165986'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-10T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/NMF71746.zip
severity: high
source: nse
stocks: []
tags:
- authentication
- compliance
- investor-protection
- mf-invest-platform
- mutual-fund
- nomination
- sebi
- ucc-structure
title: Implementation of Revised Nomination Facilities for Opt-Out on NSE MF Invest
  Platform
---

## Summary

NSE has implemented revised nomination facilities for opt-out as per SEBI Circular dated January 10, 2025, on the NSE MF Invest Platform. The circular modifies the UCC (Unique Client Code) structure to mandate authentication for investors who choose not to appoint nominees for their mutual fund units. Investors opting out must now authenticate their decision via OTP with declaration form or video recording. The validation will be implemented effective December 15, 2025.

## Key Points

- New mandatory authentication requirement for nomination opt-out on NSE MF Invest platform
- Two authentication modes available for opt-out: OTP with declaration form (code 'O') or video recording (code 'V')
- Nomination opt-out reference number becomes conditionally mandatory field in UCC structure
- For investors choosing nomination (opt-in), authentication modes are: Wet Signature ('W'), E-sign ('E'), or OTP Authentication ('O')
- Feature enabled in UAT environment for member testing
- Members must upload Declaration Form (Annexure I) along with AOF when using OTP authentication
- References prior circulars NSE/NMFTM/71461 (November 25, 2025) and NSE/NMFTM/71524 (November 28, 2025)

## Regulatory Changes

### Modified UCC Structure Fields

**Field 122 - Nomination Opt:**
- Type: CHAR, Size: 1
- Status: Mandatory
- Values: Y (Yes to nomination) / N (No to nomination)

**Field 123 - Nomination Authentication Mode:**
- Type: Varchar, Size: 1
- Status: Mandatory
- Conditional Logic:
  - If Nomination Opt = 'Y': Must use 'W' (Wet Signature), 'E' (E-sign), or 'O' (OTP Authentication)
  - If Nomination Opt = 'N': Must use 'O' (OTP with Declaration) or 'V' (Video Recording)

**Field 176 (filler1) - Nominee Opt-Out Reference Number:**
- Type: CHAR, Size: 20
- Status: Conditionally Mandatory
- Required when Nomination Opt = 'N'
- Must contain OTP or Video Recording reference number

## Compliance Requirements

### For NSE Members

1. **System Updates:** Modify systems to accommodate revised UCC structure with new authentication fields
2. **Testing:** Conduct testing in NSE MF Invest UAT environment before December 15, 2025
3. **Documentation:** Upload Declaration Form (Annexure I) with AOF when investors opt-out using OTP authentication
4. **Record Keeping:** Maintain OTP/Video recording reference numbers for opt-out cases

### For Investors (Opt-Out Applicability)

1. **Eligible Investors:** Only applicable for:
   - Non-demat/physical mode holdings
   - Individual tax status (excluding minors)
   - Single holding only
   - Fresh purchases and new SIP registrations in new and existing UCCs

2. **Declaration Requirement:** Investors opting out must confirm understanding that:
   - No nominee will be appointed for mutual fund units
   - Legal heirs will need to submit requisite documents issued by Court or competent authority
   - Documentation requirements based on value of assets held in folio

3. **Authentication:** Must complete either OTP authentication with signed declaration form or video recording

## Important Dates

- **December 10, 2025:** Circular issued (Ref: NSE/NMFTM/71746, Circular No: 1054/2025)
- **Testing Phase:** Feature enabled in UAT environment (current)
- **December 15, 2025:** Effective date for validation implementation of nomination opt-out requirements

## Impact Assessment

### Market Impact
- **Medium Operational Impact:** All NSE mutual fund platform members must update systems and processes
- **Enhanced Investor Protection:** Strengthens safeguards by requiring explicit authentication for opt-out decisions
- **Process Complexity:** Adds authentication layer but improves documentation and audit trail

### Operational Impact

**For Members:**
- System integration required to capture and validate new authentication fields
- Training needed for handling two authentication modes (OTP vs. Video)
- Additional documentation management for declaration forms

**For Investors:**
- Simplified nomination process with clear authentication options
- Better awareness of implications of not appointing nominees
- Protects legal heirs by ensuring informed decision-making

### Compliance Impact
- Aligns with SEBI's investor protection framework
- Reduces disputes in transmission of units to legal heirs
- Creates verifiable audit trail for regulatory oversight

## Contact Information

- **Toll Free:** 1800 2100 940
- **Email:** support@nseinvest.com

## Declaration Form Details

The opt-out declaration form requires:
- Date and mutual fund/AMC details
- Folio number/Application number/PAN
- Sole/First holder name
- Explicit confirmation of not wishing to appoint nominees
- Acknowledgment of understanding consequences
- Awareness that legal heirs will need court-issued documents for transmission
- Unitholder signature and name