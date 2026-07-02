---
category: market-operations
circular_id: 321e92278118305b
date: '2026-07-02'
description: NSE will conduct a mock trading session in the Securities Lending and
  Borrowing Market (SLBM) on Saturday, July 04, 2026, mandating use of new NEAT Adapter
  version 1.0.28 and new CA certificate/ports, with no new version release.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/SLBS75008.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Operational/technical circular for SLBM mock trading session affecting
  members' systems only; no direct impact on listed securities or investors.
pdf_url: https://nsearchives.nseindia.com/content/circulars/SLBS75008.pdf
processing:
  attempts: 1
  content_hash: 78c4d284780edf0d
  processed_at: '2026-07-02T14:18:11.133176'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-07-02T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/SLBS75008.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- settlement-calendar
- market-operations
title: NSE Mock Trading Session for SLBM Segment on Saturday, July 04, 2026
---

## Summary

NSE will conduct a mock trading session in the Securities Lending and Borrowing Market (SLBM) segment on Saturday, July 04, 2026. This is a system readiness test with no new version release, requiring members to use the new NEAT Adapter application (Version 1.0.28) along with new ports and CA certificates for the SLBM segment.

## Key Points

- Mock trading session scheduled for Saturday, July 04, 2026 in the SLBM segment.
- Trading Session-1 (Primary Site): Normal market open, contingency start at 13:00, contingency close at 14:00, normal market close at 15:30.
- Trading Session-2 (DR Site): from 16:00 to 16:45.
- Live re-login window: 17:30 to 18:30 (relogin timings section indicates re-login start/close around 18:30–19:00).
- Members must use new NEAT Adapter Version 1.0.28 (Windows and Linux) with new GR Port 10889, mandatory from July 04, 2026 (mock).
- Members using direct connection via NNF users must download and use the new CA certificate available on the Extranet path.
- New interactive parameters for SLBM segment: Gateway IP 172.19.14.85, New Port 10889, Network 172.19.14.0, Subnet Mask 255.255.255.128, Port 10860.
- All outstanding orders will be cleared before each session; NNF software users must manually clear orders.
- Trades during the mock session carry no financial obligation (no fund pay-in/pay-out).
- Only valid, approved UCC/PAN records uploaded before cutoff will be permitted; UCC validation is skipped during contingency time for order entry.

## Regulatory Changes

No new regulatory change; this is an operational/technical circular referencing prior circulars (NSE/MSD/74511 dated June 02, 2026; NSE/MSD/74559 dated June 05, 2026; NSE/MSD/73993 dated April 30, 2026; NSE/MSD/46441; SEBI/HO/MRD1/DSAP/CIR/P/2020/234; NSE/ISC/51754 and NSE/ISC/52722) mandating migration to updated NEAT Adapter software, CA certificates, and network ports for the SLBM segment.

## Compliance Requirements

- Members must ensure their systems are updated with NEAT Adapter Version 1.0.28 (Windows/Linux) and configured to use new GR Port 10889 by the mock date.
- Members using direct/NNF connections must download and install the new CA certificate from the Extranet path (/slbftp/slbcommon/Encryption_CA_Certificate/2026_Certificate).
- Members must ensure readiness of their migration plan by July 04, 2026.
- Members must clear outstanding orders in NNF systems manually before each session.
- Members must ensure UCC/PAN records are valid and approved before the applicable cutoff.

## Important Dates

- Mock trading date: Saturday, July 04, 2026.
- Trading Session-1 (Primary Site): Contingency start 13:00, Contingency close 14:00, Normal market close 15:30.
- Trading Session-2 (DR Site): 16:00 to 16:45.
- Re-login window: approximately 17:30 to 19:00.
- New NEAT Adapter version and ports mandatory from July 04, 2026 (mock).

## Impact Assessment

This circular has low market impact as it pertains solely to technical/operational readiness for the SLBM segment mock trading session on a non-trading Saturday. Trades executed during the mock session do not create financial obligations. The primary impact is on NSE trading members and their IT/operations teams, who must ensure timely software, certificate, and network configuration upgrades to avoid disruption during actual SLBM trading post-migration.