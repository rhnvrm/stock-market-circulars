---
category: market-operations
circular_id: 6993021ade0f323c
date: '2026-06-19'
description: NSE will conduct a mock trading session in the Currency Derivatives Segment
  on Saturday, June 20, 2026, with trading from 13:45–15:00. Members must use NEAT
  Adapter v1.0.29 and new CA certificate with updated ports, mandatory from July 06,
  2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CD74787.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session for Currency Derivatives members with
  infrastructure migration reminders; no market-wide impact or new regulatory obligations
  introduced.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CD74787.pdf
processing:
  attempts: 1
  content_hash: 7c270fba55237aee
  processed_at: '2026-06-19T15:48:55.198026'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-19T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CD74787.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- currency-derivatives
- nse
- neat-adapter
- technology-upgrade
title: NSE Currency Derivatives Mock Trading Session – June 20, 2026 (No New Version
  Release)
---

## Summary

NSE is conducting a mock trading session in the Currency Derivatives (CD) Segment on Saturday, June 20, 2026. No new software version is being released for this mock. Members are reminded to migrate to the new NEAT Adapter v1.0.29 and the new CA certificate with updated gateway ports, which become mandatory from July 06, 2026.

## Key Points

- Mock trading date: June 20, 2026 (Saturday)
- Trading session from Primary Site: 13:45–15:00 hrs
- Trade Modification end time: 15:10 hrs
- Live Re-login window: 18:30–19:00 hrs
- No new version release for this mock session
- Members must use NEAT Adapter v1.0.29 (Windows and Linux) with new ports for Currency Derivatives
- Members on Direct Connection (NNF users) must download and use the new CA certificate from Extranet path: `/cdsftp/cdscommon/Encryption_CA_Certificate/2026_Certificate`

## Regulatory Changes

No new regulatory changes are introduced in this circular. It reiterates requirements from:
- NSE/MSD/74511 dated June 02, 2026 (new CA certificate)
- NSE/MSD/74559 dated June 05, 2026 (new NEAT Adapter EXE version)
- NSE/MSD/73993 dated April 30, 2026 (interactive connectivity details)

## Compliance Requirements

- Members must use NEAT Adapter v1.0.29 in combination with new ports for the Currency Derivatives segment.
- NNF Direct Connection users must download the new CA certificate and update their configurations.
- Applicable new interactive GR ports for Currency Derivatives segment:
  - Gateway IP: 172.19.18.85 | Network: 172.19.18.0/255.255.255.128
  - Ports: 10870, 10871, 10885, 10889 (new encryption, MD5 checksum removed), 10891 (new encryption + immediate Ack for order messages)
- Members using NNF software must manually clear outstanding orders before each mock session.
- All trades during mock sessions carry no financial obligation (no fund pay-in or pay-out).
- Only valid and compliant UCC/PAN uploaded and approved before cutoff will be active during mock.

## Important Dates

- **June 20, 2026**: Mock trading session in Currency Derivatives Segment
- **July 06, 2026**: Mandatory migration deadline — new NEAT Adapter v1.0.29 and new CA certificate with updated ports become compulsory for Currency Derivatives

## Impact Assessment

This is a routine operational circular for Currency Derivatives Segment members only. There is no broader market impact. Members who have not yet migrated to the new NEAT Adapter or CA certificate should treat July 06, 2026 as a hard deadline to ensure continuity of trading access. The mock session provides an opportunity to validate readiness before the mandatory cutover.