---
category: market-operations
circular_id: 41fd206291ad6dba
date: '2026-06-19'
description: NSE will conduct a mock trading session in the Commodity Derivatives
  segment on Saturday, June 20, 2026, with normal market hours from 13:45 to 15:00.
  Members must prepare for mandatory migration to new NEAT adapter version and CA
  certificate by July 6, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/COM74796.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for the Commodity Derivatives segment
  with no new version release; primarily operational guidance for members ahead of
  a mandatory technology migration deadline.
pdf_url: https://nsearchives.nseindia.com/content/circulars/COM74796.pdf
processing:
  attempts: 1
  content_hash: 166bb7d6bb79cb56
  processed_at: '2026-06-19T15:45:41.038051'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-19T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/COM74796.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- commodity-derivatives
- neat-adapter
- ca-certificate
- nse
title: Mock Trading Session in Commodity Derivatives Segment - June 20, 2026
---

## Summary

NSE will conduct a mock trading session in the Commodity Derivatives (COM) segment on Saturday, June 20, 2026. There is no new software version release associated with this mock. The session also serves as a readiness exercise for members to test the new NEAT Adapter version (1.0.29) and new CA certificate, which become mandatory from July 6, 2026.

## Key Points

- Mock trading session scheduled for Saturday, June 20, 2026 in the Commodity Derivatives segment
- No new version release accompanying this mock session
- Normal Market open: 13:45 hrs; Normal Market close: 15:00 hrs
- Position Limit/Collateral value setup cutoff and Trade Modification end time: 15:10 hrs
- Live Re-login window: 18:30 hrs to 19:00 hrs
- Members must use NEAT Adapter Version 1.0.29 (Windows and Linux) with GR Port 10869
- New CA certificate available on Extranet at `/comtftp/comtcommon/Encryption_CA_Certificate/2026_Certificate`
- Members using Direct Connection via NNF users must download the new CA certificate

## Regulatory Changes

No new regulatory changes introduced by this circular. Members are directed to refer to:
- Circular NSE/MSD/74511 dated June 02, 2026 — new CA certificate details
- Circular NSE/MSD/74559 dated June 05, 2026 — new NEAT Adapter EXE application version

## Compliance Requirements

- Members must use NEAT Adapter Version 1.0.29 (Windows/Linux) with the applicable GR Port (10869) for the mock session
- Members on Direct Connection (NNF users) must download and configure the new CA certificate from Extranet
- All members must complete migration readiness by July 6, 2026
- Gateway Router IP: 172.19.15.85; New Ports: 10865, 10869 (MD5 checksum removal), 10871 (MD5 checksum removal + immediate Ack for order messages)
- Gateway network: 172.19.15.0 / 255.255.255.128, Port 10850

## Important Dates

- **June 20, 2026**: Mock trading session in Commodity Derivatives segment
- **July 6, 2026**: Mandatory adoption of new NEAT Adapter version and new CA certificate

## Impact Assessment

This is a routine operational mock session with low market impact. It primarily affects Commodity Derivatives segment members who need to validate their technology setup ahead of the July 6, 2026 mandatory migration to the new NEAT Adapter and CA certificate. Members who do not complete readiness testing risk non-compliance with the mandatory migration deadline. No changes to trading rules, fees, or listed securities are involved.