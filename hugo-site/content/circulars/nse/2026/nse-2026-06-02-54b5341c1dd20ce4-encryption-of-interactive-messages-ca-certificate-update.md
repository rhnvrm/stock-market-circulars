---
category: market-operations
circular_id: 54b5341c1dd20ce4
date: '2026-06-02'
description: NSE instructs all members to update their CA certificate for encrypted
  interactive messages before the existing certificate expires on July 05, 2026. New
  certificates valid until July 17, 2027 will be available by June 05, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD74511.pdf
impact: high
impact_ranking: high
importance_ranking: high
justification: Mandatory technical action for all NSE members with a hard deadline
  — failure to update before July 05, 2026 will result in loss of trading connectivity
  across CM, F&O, CD, SLBM, and COM segments.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD74511.pdf
processing:
  attempts: 1
  content_hash: 703ef84e6b9c7486
  processed_at: '2026-06-02T16:47:17.479118'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-02T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD74511.pdf
severity: high
source: nse
stocks: []
tags:
- encryption
- ca-certificate
- nse
- neat-adapter
- nnf-api
- interactive-messages
- trading-infrastructure
- connectivity
- member-services
- technical-update
title: NSE CA Certificate Update for Encryption of Interactive Messages
---

## Summary

NSE has issued a mandatory CA certificate update for encryption of interactive messages. The existing CA certificate (issued under circular NSE/MSD/67068 dated March 11, 2025) expires on July 05, 2026. Members must migrate to the new CA certificate, which will be made available by June 05, 2026, and is valid until July 17, 2027. This applies to all members connecting via NEAT Adapter (NA), NEAT application, or Direct connection via NNF API protocols across CM, F&O, CD, SLBM, and COM segments.

## Key Points

- Existing CA certificate expires on **July 05, 2026**; new certificate valid until **July 17, 2027**
- New certificate will be available on NSE Extranet by **June 05, 2026 (EOD)**
- An interim coexistence phase will allow login via both old and new CA certificates before the old one is fully disabled
- Members on NEAT Adapter (NA) / NEAT application will receive an updated version with new certificates pre-installed
- NA will verify Gateway Router server certificate after successful SSL connection
- Details of applicable NA versions will be shared via a separate circular
- Members using Direct connection via NNF API must manually download and configure the new CA certificate
- New gateway IPs and ports are provided for CM, F&O, CD, COM, and SLBM segments (see Annexure 2)
- FAQ available at https://www.nseindia.com/trade/continuous-markets-FAQs

## Regulatory Changes

This circular updates the CA certificate used for encrypting interactive messages between NSE members and Exchange gateway routers. New connectivity parameters (IPs and ports) accompany the new certificate for all segments. Two port variants are introduced:
- Standard ports supporting new encryption with MD5 checksum removal
- Additional ports supporting new encryption with MD5 checksum removal and new immediate Ack request for orders

## Compliance Requirements

- **NEAT Adapter / NEAT application users**: Await and install the new NA version when released; no separate certificate download required.
- **NNF API Direct connection users**:
  1. Download the new CA certificate from the designated Extranet path before the old certificate expires.
  2. Configure interactive connectivity using the new parameters in Annexure 2.
  3. Use the new CA certificate with new parameters for CM, F&O, CD, COM, and SLBM segments.
- All members must complete migration readiness before the end of the coexistence phase.

## Important Dates

| Event | Date |
|---|---|
| New CA certificate available on Extranet | June 05, 2026 (EOD) |
| Old CA certificate expiry | July 05, 2026 |
| New CA certificate validity end | July 17, 2027 |

## Impact Assessment

This is a high-impact operational circular affecting all NSE members across equity cash (CM), futures & options (F&O), currency derivatives (CD), commodity (COM), and securities lending (SLBM) segments. Failure to update the CA certificate before July 05, 2026 will result in loss of trading connectivity. Members using Direct NNF API connections face the highest manual effort, as they must download certificates, update Extranet paths, and reconfigure gateway IPs and ports. NEAT Adapter users have a simpler path via a forthcoming software release. Early preparation is strongly recommended to avoid last-minute connectivity failures.