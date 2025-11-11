---
category: compliance
circular_id: ad838d58eac1ef04
date: '2025-11-11'
description: BSE circular implementing trading restrictions on clients with non-validated
  KYC from November 22, 2025, following SEBI KRA Regulations amendments and demise
  reporting requirements.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={DA9F79B1-E472-44E5-8C7E-02B9CCDFB9D6}&noticeno=20251111-43&dt=11/11/2025&icount=43&totcount=57&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Clients with non-validated KYC uploaded between October 1-31, 2025
  will be blocked from trading and position squaring from November 22, 2025. Also
  mandates blocking of deceased investor accounts based on daily KRA data.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251111-43&attachedId=
processing:
  attempts: 1
  content_hash: b9381c87481bbb8f
  processed_at: '2025-11-11T18:39:52.748884'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-11-11T15:30:59+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={DA9F79B1-E472-44E5-8C7E-02B9CCDFB9D6}&noticeno=20251111-43&dt=11/11/2025&icount=43&totcount=57&flag=0
severity: high
source: bse
stocks: []
tags:
- kyc
- kra
- compliance
- sebi-regulations
- client-onboarding
- trading-restrictions
- ucc
- aadhaar
- risk-management
- demise-reporting
title: Guidelines for Amendment to SEBI KYC Registration Agency Regulations - Client
  Restrictions from November 22, 2025
---

## Summary

BSE has issued guidelines following amendments to SEBI KYC Registration Agency (KRA) Regulations, 2011. Effective November 22, 2025, clients whose KYC records uploaded to KRA between October 1-31, 2025 remain "On Hold" (non-validated) will be prohibited from trading and cannot square up open positions. Trading members must also block debit transactions and suspend trading accounts for deceased investors based on daily demise data shared by KRAs. Non-compliant client PANs will be flagged and provided to members via daily files.

## Key Points

- Clients with non-validated KYC (both Aadhaar and Non-Aadhaar based) uploaded between October 1-31, 2025 will be restricted from November 22, 2025
- Restricted clients cannot trade on the exchange or square up existing open positions
- Open positions of non-compliant clients will naturally expire on contract expiry dates
- KRA shares demise data on daily basis with exchanges
- Trading members must block debit transactions, suspend trading accounts, and inactivate/close UCC for deceased investors
- Clients becoming KRA compliant will be permitted to trade on T+1 basis after Exchange receives confirmation from KRA
- Non-compliant client list provided daily at path: \EQ\Transaction\November-2025\11-11-2025 Non_Validated_Clients_by_KRAs_Clgno_xxxx.TXT

## Regulatory Changes

This circular implements several SEBI regulations:

1. **SEBI Circular SEBI/HO/MIRSD/FATF/P/CIR/2023/0144** (August 11, 2023): Simplification of KYC process and rationalization of Risk Management Framework at KRAs

2. **SEBI Circular SEBI/HO/OIAE/OIAE_IAD-1/P/CIR/2023/0000000163** (October 3, 2023): Centralized mechanism for reporting investor demise through KRAs

3. Previous BSE notice 20251013-63 (October 13, 2025) on KYC simplification and risk management

The amendments strengthen the KYC validation process and introduce systematic blocking mechanisms for non-compliant and deceased investor accounts.

## Compliance Requirements

**For Trading Members:**

1. Monitor daily files containing non-validated client PANs from the specified path
2. Block debit transactions in accounts of deceased investors
3. Suspend all transactions in trading accounts of deceased investors
4. Inactivate/close UCC (Unique Client Code) in all stock exchanges for deceased investors
5. Prevent trading for clients flagged as non-compliant by KRAs
6. Re-enable trading on T+1 basis once clients become KRA compliant
7. Review demise data shared daily by KRAs
8. Ensure clients complete KYC validation requirements to avoid trading restrictions

**For Clients:**

1. Ensure KYC records are validated by KRAs
2. Complete validation requirements if KYC is marked "On Hold"
3. Respond to KRA queries for both Aadhaar and Non-Aadhaar based OVD (Officially Valid Documents)
4. Understand that non-compliance will result in inability to trade or close positions

## Important Dates

- **October 1-31, 2025**: KYC upload period under review for validation status
- **November 11, 2025**: Notice date and circular issuance
- **November 22, 2025**: Effective date for trading restrictions on non-validated KYC clients
- **T+1**: Trading permitted for clients who become KRA compliant, based on KRA confirmation received on T Day
- **Daily**: KRA shares demise data and non-compliant client lists with Exchange

## Impact Assessment

**Operational Impact:**

- Trading members must implement daily monitoring systems for non-compliant client files
- Systems need to be configured to automatically flag and restrict trading for non-validated PANs
- Additional workflow required to track KRA compliance status and re-enable trading on T+1
- Enhanced monitoring of demise data and account blocking mechanisms

**Market Impact:**

- Clients with pending KYC validation face complete trading prohibition from November 22, 2025
- Affected clients cannot reduce risk by squaring off open positions, leading to forced expiry
- Potential market liquidity impact if significant number of clients are non-compliant
- Increased urgency for clients to complete KYC validation before the deadline

**Risk Management:**

- Strengthens overall market integrity through stricter KYC enforcement
- Reduces risk from deceased investor account misuse through centralized reporting
- Ensures regulatory compliance with SEBI's Risk Management Framework
- May create operational risk for positions held by non-compliant clients that cannot be squared up

**Severity Justification:** High severity due to complete trading prohibition and inability to manage existing positions for non-compliant clients, with system-wide implications for trading members.

## Contact Information

For clarifications, members may contact:
- **Phone**: 022-2272 8435/5785
- **Email**: ucc@bseindia.com
- **Keyur Punatar**: Deputy Vice President, Investigation
- **Poonam Pisat**: Assistant Vice President, Investigation