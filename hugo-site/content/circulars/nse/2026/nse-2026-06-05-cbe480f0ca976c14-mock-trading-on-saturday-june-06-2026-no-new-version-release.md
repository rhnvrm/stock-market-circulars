---
category: market-operations
circular_id: cbe480f0ca976c14
date: '2026-06-05'
description: NSE will conduct a mock trading session in the Securities Lending and
  Borrowing Market (SLBM) on June 06, 2026, covering Primary Site and DR Site sessions.
  Members must use new NEAT Adapter version 1.0.28 and updated CA certificates, mandatory
  from July 06, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/SLBS74575.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for SLBM segment; relevant only to members
  using the securities lending platform. No market-wide impact; primarily an operational
  readiness test with a technology migration deadline.
pdf_url: https://nsearchives.nseindia.com/content/circulars/SLBS74575.pdf
processing:
  attempts: 1
  content_hash: d6da5c7ce5102429
  processed_at: '2026-06-05T20:06:23.789061'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-05T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/SLBS74575.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- slbm
- securities-lending
- neat-adapter
- ca-certificate
- market-operations
title: Mock Trading Session in SLBM on Saturday, June 06, 2026 - No New Version Release
---

## Summary

NSE is conducting a mock trading session in the Securities Lending and Borrowing Market (SLBM) on Saturday, June 06, 2026. The session spans two trading windows — one from the Primary Site and one from the Disaster Recovery (DR) Site. Members are also required to migrate to the new NEAT Adapter version 1.0.28 and new CA certificate, which become mandatory from July 06, 2026.

## Key Points

- Mock trading session scheduled for June 06, 2026 in the SLBM segment
- Session 1 (Primary Site): Normal market open 10:15, close 13:00; Contingency window 11:00–12:30
- Session 2 (DR Site): Normal market open 14:00, close 14:30
- Live re-login window: 16:00–16:30
- New NEAT Adapter version 1.0.28 (Windows and Linux) must be used during mock; mandatory from July 06, 2026
- Applicable GR Port for SLBM: 10889
- New CA certificate to be made available on NSE Extranet by June 05, 2026 (EOD)
- NNF users must download new CA certificate from `/slbftp/slbcommon/Encryption_CA_Certificate/2026_Certificate`

## Regulatory Changes

- New CA certificate introduces updated encryption with MD5 checksum removal
- Port 10889 will support new encryption messages with MD5 checksum removal
- New immediate Ack request for order-related messages introduced
- Gateway IP for SLBM: 172.19.14.85, Subnet: 172.19.14.0/25

## Compliance Requirements

- Members must use NEAT Adapter version 1.0.28 during the mock session
- Members using Direct NNF connections must download and configure the new CA certificate
- All members must ensure migration readiness by July 06, 2026
- Refer to circulars NSE/MSD/74511 (June 02, 2026) and NSE/MSD/74559 (June 05, 2026) for technical details
- Outstanding orders will be purged before each session; NNF members must manually clear orders

## Important Dates

- **June 05, 2026**: New CA certificate made available on NSE Extranet (EOD)
- **June 06, 2026**: Mock trading session in SLBM
- **July 06, 2026**: New NEAT Adapter version 1.0.28 and new CA certificate become mandatory

## Impact Assessment

This circular has low market impact as it pertains solely to an operational mock/readiness test for SLBM segment members. The primary significance is the technology migration deadline of July 06, 2026, by which all members must upgrade to the new NEAT Adapter and CA certificate. Failure to comply by the deadline could disrupt connectivity to the SLBM segment for non-compliant members.