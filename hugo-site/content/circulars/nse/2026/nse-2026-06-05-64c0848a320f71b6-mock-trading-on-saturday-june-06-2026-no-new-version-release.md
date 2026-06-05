---
category: market-operations
circular_id: 64c0848a320f71b6
date: '2026-06-05'
description: NSE will conduct a mock trading session in the Futures & Options segment
  on June 06, 2026, covering both Primary Site and DR Site sessions, with updated
  NEAT Adapter and CA certificate requirements.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/FAOP74588.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for F&O segment members; operational/technical
  in nature with no market-wide financial impact.
pdf_url: https://nsearchives.nseindia.com/content/circulars/FAOP74588.pdf
processing:
  attempts: 1
  content_hash: 051784df8ace3f4a
  processed_at: '2026-06-05T17:31:13.473369'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-05T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/FAOP74588.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- futures-and-options
- neat-adapter
- settlement-calendar
- live-activities-schedule
title: Mock Trading on Saturday, June 06, 2026 - Futures & Options Segment (No New
  Version Release)
---

## Summary

NSE will conduct a mock trading session in the Futures & Options (F&O) segment on Saturday, June 06, 2026. The session covers two trading windows — one from the Primary Site and one from the Disaster Recovery (DR) Site — and requires members to use the updated NEAT Adapter version and new CA certificate for certain connectivity scenarios.

## Key Points

- Mock trading is scheduled for June 06, 2026 in the F&O segment.
- No new version release is associated with this mock session.
- Session 1 (Primary Site): Normal Market opens at 10:15 hrs, closes at 13:00 hrs.
- Session 2 (DR Site): Normal Market opens at 13:53 hrs, closes at 14:30 hrs.
- Members using Direct connection via NNF must download the new CA certificate available on NSE Extranet by June 05, 2026.
- New NEAT Adapter (Version 1.0.29 for Windows and Linux) is mandatory from the July 06, 2026 mock onward, using GR Port 10841.
- NEATPlus version 7.8.7 is discontinued from June 06, 2026 (mock); version 7.8.8 is the current supported version.

## Regulatory Changes

- New CA certificate introduced for Extranet connectivity (available at `/faoftp/faocommon/Encryption_CA_Certificate/2026_Certificate`).
- Updated interactive parameters for F&O Derivatives segment: Gateway IP 172.19.13.85, New Port 10837; subnet 172.19.13.0/255.255.255.128, with additional ports 10820, 10841, and 10843.
- Port 10841 supports new encryption messages with MD5 checksum removal.
- Port 10843 additionally supports new immediate Ack request for order-related messages.

## Compliance Requirements

- Members must download and configure the new CA certificate before June 05, 2026 for NNF Direct connections.
- Members must ensure migration readiness (new NEAT Adapter + new ports) by July 06, 2026.
- NEATPlus 7.8.7 must be replaced with 7.8.8; version 7.8.7 is only compatible with existing broadcast parameters, while 7.8.8 requires new broadcast parameters (refer to NSE/MSD/74133 dated May 08, 2026).
- Members should refer to circulars NSE/MSD/74511 (June 02, 2026) and NSE/MSD/74559 (June 05, 2026) for CA certificate and NEAT Adapter version details.

## Important Dates

- **June 05, 2026**: New CA certificate made available on NSE Extranet.
- **June 06, 2026**: Mock trading session; NEATPlus version 7.8.7 discontinued.
- **July 06, 2026**: New NEAT Adapter Version 1.0.29 becomes mandatory; members must complete CA certificate migration.

## Impact Assessment

This is a routine operational mock session with no financial obligations or market-wide impact. The primary impact is technical — members must upgrade their NEAT Adapter and CA certificate configurations ahead of the July 06, 2026 mandatory deadline. Failure to migrate may result in connectivity issues during live trading after the cutover date. No stocks or indices are directly affected.