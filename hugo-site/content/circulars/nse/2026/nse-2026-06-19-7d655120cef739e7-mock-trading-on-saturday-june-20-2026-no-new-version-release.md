---
category: market-operations
circular_id: 7d655120cef739e7
date: '2026-06-19'
description: NSE will conduct a mock trading session in the Securities Lending and
  Borrowing Market (SLBM) on Saturday, June 20, 2026, with trading from 14:00–15:00
  hrs. Members must use NEAT Adapter version 1.0.28 and new CA certificate; full migration
  mandatory by July 06, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/SLBS74790.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Routine mock trading session notice for SLBM segment members; no regulatory
  change, no stock-specific impact. Operational readiness and technology migration
  reminder.
pdf_url: https://nsearchives.nseindia.com/content/circulars/SLBS74790.pdf
processing:
  attempts: 1
  content_hash: 6b0b9a12922206f5
  processed_at: '2026-06-19T15:46:41.555068'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-19T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/SLBS74790.pdf
severity: low
source: nse
stocks: []
tags:
- mock-trading
- slbm
- securities-lending-and-borrowing
- nse
- neat-adapter
- connectivity
title: NSE SLBM Mock Trading Session – June 20, 2026 (No New Version Release)
---

## Summary

NSE will conduct a mock trading session in the Securities Lending and Borrowing Market (SLBM) on Saturday, June 20, 2026. There is no new version release accompanying this mock session. Members are required to use NEAT Adapter version 1.0.28 along with the new CA certificate and updated port 10889 for the SLBM segment. Full migration to the new setup is mandatory from July 06, 2026.

## Key Points

- Mock trading session for SLBM scheduled on Saturday, June 20, 2026
- Normal Market hours: 14:00–15:00 hrs (from Primary Site)
- Live Re-login window: 18:30–19:00 hrs
- No new software version is being released with this mock
- Members must use NEAT Adapter version 1.0.28 (Windows and Linux) with Gateway Router port 10889
- New CA certificate available on Extranet at `/slbftp/slbcommon/Encryption_CA_Certificate/2026_Certificate`
- NNF (direct connection) users must download and configure the new CA certificate
- All outstanding orders will be purged before each mock session; NNF users must clear orders manually

## Regulatory Changes

No new regulatory changes are introduced. This circular references existing circulars:
- NSE/MSD/74511 dated June 02, 2026 – New CA certificate
- NSE/MSD/74559 dated June 05, 2026 – New NEAT Adapter EXE version
- NSE/MSD/73993 dated April 30, 2026 – Interactive connectivity details

## Compliance Requirements

- Members must use NEAT Adapter version 1.0.28 (mandatory from July 06, 2026)
- Members using Direct/NNF connection must download the new CA certificate from the NSE Extranet
- Migration plan must be ready by **July 06, 2026**
- Gateway Router IP: 172.19.14.85 | New Port: 10889
- Subnet: 172.19.14.0 / 255.255.255.128 | Legacy Port: 10860
- NEAT version for mock: NEAT 1.3.3
- Installation Guide available on NSE Extranet at `/slbftp/slbcommon/Installation_Procedure`

## Important Dates

| Date | Event |
|------|-------|
| June 20, 2026 | SLBM Mock Trading Session (14:00–15:00 hrs) |
| June 20, 2026 | Live Re-login window (18:30–19:00 hrs) |
| July 06, 2026 | Mandatory migration to new NEAT Adapter v1.0.28 and new CA certificate |

## Impact Assessment

This circular has low market impact. It is a scheduled operational mock trading exercise for SLBM segment members only. The primary action required is technical: ensuring NEAT Adapter version 1.0.28 and the new CA certificate are deployed before the July 06, 2026 mandatory cutover. Members not prepared by that date may face connectivity issues in the live SLBM environment. No stock-specific or investor-level impact is expected.