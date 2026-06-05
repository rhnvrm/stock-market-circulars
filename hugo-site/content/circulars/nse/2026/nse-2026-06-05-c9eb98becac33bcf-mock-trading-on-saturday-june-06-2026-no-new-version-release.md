---
category: market-operations
circular_id: c9eb98becac33bcf
date: '2026-06-05'
description: NSE will conduct a mock trading session in the Currency Derivatives segment
  on June 06, 2026, covering both Primary Site and DR Site sessions. Members must
  use NEAT Adapter Version 1.0.29 and the new CA certificate, with mandatory migration
  by July 06, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CD74564.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for Currency Derivatives segment; operational
  in nature with no market-moving implications. Relevant only to members participating
  in the mock session.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CD74564.pdf
processing:
  attempts: 1
  content_hash: e3b75052efc2b32e
  processed_at: '2026-06-05T20:09:15.375245'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-05T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CD74564.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- currency-derivatives
- neat-adapter
- ca-certificate
- disaster-recovery
title: Mock Trading on Saturday, June 06, 2026 - Currency Derivatives Segment (No
  New Version Release)
---

## Summary

NSE's Currency Derivatives segment will conduct a mock trading session on Saturday, June 06, 2026. The mock covers two sessions: Session 1 from the Primary Site and Session 2 from the Disaster Recovery (DR) Site. This circular also mandates the use of NEAT Adapter Version 1.0.29 and a new CA certificate, with full migration required by July 06, 2026.

## Key Points

- Mock trading scheduled for June 06, 2026 in the Currency Derivatives segment.
- Session 1 (Primary Site): Normal Market opens at 10:00, Contingency window 11:00–12:30, Normal Market closes at 13:00.
- Session 2 (DR Site): Normal Market opens at 13:45, closes at 14:30; Trade Modification ends at 14:40.
- Live Re-login window: 16:00–16:30.
- Members must use NEAT Adapter Version 1.0.29 (Windows and Linux) with GR Port 10889.
- New CA certificate to be available by June 05, 2026 (EOD) on Extranet path `/cdsftp/cdscommon/Encryption_CA_Certificate/2026_Certificate`.
- NNF users on Direct Connection must download and deploy the new CA certificate.
- All outstanding orders will be cleared before each session.

## Regulatory Changes

No new regulatory changes introduced. This circular operationalises previously announced infrastructure changes (new CA certificate per NSE/MSD/74511 dated June 02, 2026, and new NEAT Adapter per NSE/MSD/74559 dated June 05, 2026) within the mock trading context.

## Compliance Requirements

- Members must use **NEAT Adapter Version 1.0.29** for both Windows and Linux during the mock session.
- Members using Direct Connection through NNF users must download the new CA certificate from the Extranet by June 05, 2026 (EOD).
- Currency Derivatives interactive parameters to use with the new CA certificate:
  - Gateway IP: 172.19.18.85
  - Ports: 10870/10871, 10885, 10889 (new encryption, MD5 checksum removed), 10891 (new encryption + immediate Ack for order messages)
  - Subnet: 172.19.18.0 / 255.255.255.128
- Members must ensure migration readiness by **July 06, 2026** (mandatory cutover).
- Refer to Annexures 1–3 for detailed mock session instructions, prerequisites, and DR switchover guidelines.
- NEAT version in use: 3.5.4.

## Important Dates

| Date | Event |
|------|-------|
| June 05, 2026 | New CA certificate available on Extranet (EOD) |
| June 06, 2026 | Mock trading session — Currency Derivatives segment |
| July 06, 2026 | Mandatory migration to new NEAT Adapter and CA certificate |

## Impact Assessment

Impact is limited to Currency Derivatives segment members participating in the mock session. No production trading is affected. The mock serves as a readiness test for the upcoming mandatory infrastructure migration (new CA certificate and NEAT Adapter) effective July 06, 2026. Members who fail to test connectivity during this mock may face readiness issues at the mandatory cutover date.