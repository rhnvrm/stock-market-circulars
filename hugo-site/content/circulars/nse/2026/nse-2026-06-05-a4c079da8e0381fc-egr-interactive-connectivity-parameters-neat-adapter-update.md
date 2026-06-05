---
category: market-operations
circular_id: a4c079da8e0381fc
date: '2026-06-05'
description: NSE notifies updated IP parameters for the Electronic Gold Receipts (EGR)
  segment effective June 08, 2026, and requires members to install the new NEAT Adapter
  version 1.0.25 while retiring the existing IP 172.19.14.85 from June 06, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/EGR74591.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational update affecting EGR segment members requiring mandatory
  IP configuration change and NEAT Adapter upgrade within a short timeframe; no broad
  market or investor impact but critical for affected members to maintain connectivity.
pdf_url: https://nsearchives.nseindia.com/content/circulars/EGR74591.pdf
processing:
  attempts: 1
  content_hash: d1ae002394c04b22
  processed_at: '2026-06-05T17:29:39.408589'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-05T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/EGR74591.pdf
severity: medium
source: nse
stocks: []
tags:
- electronic-gold-receipts
- egr
- neat-adapter
- connectivity
- ip-update
- market-operations
- mock-trading
title: 'EGR Segment: New IP Parameters and NEAT Adapter v1.0.25 Update'
---

## Summary

NSE has notified a new IP parameter for the Electronic Gold Receipts (EGR) segment as a partial modification to earlier circulars NSE/MSD/74225 (May 14, 2025) and NSE/EGR/74203 (May 13, 2026). Members must update their connectivity settings and install the new NEAT Adapter version 1.0.25. The new IP will be available during the mock session on June 06, 2026 and go live from June 08, 2026.

## Key Points

- New EGR Gateway Router IP: **172.19.14.86**, Port: **11887**
- Subnet range: 172.19.14.0, Network Mask: 255.255.255.128, Port: 11860
- Existing IP **172.19.14.85** will be decommissioned from June 06, 2026 onwards
- New NEAT Adapter version **1.0.25** available for both Windows and Linux platforms
- NA installer files available on Extranet from June 06, 2026 by 08:00 hours
- Modifies circulars NSE/MSD/74225 dated May 14, 2025 and NSE/EGR/74203 dated May 13, 2026

## Regulatory Changes

This circular partially modifies:
- NSE/MSD/74225 (May 14, 2025): EGR NEAT Adapter version details
- NSE/EGR/74203 (May 13, 2026): Item 5.4 — Interactive connectivity parameters for EGR segment

All other details from the above circulars remain unchanged.

## Compliance Requirements

- Members must **uninstall** the earlier NEAT Adapter version before installing v1.0.25
- Download and install the updated NA from the Extranet paths:
  - Windows: `/egcommon/NeatAdapter/Windows` — files: `NA_1.0.25_Setup.exe`, `Register_Installer.bat`
  - Linux: `/egcommon/NeatAdapter/Linux` — files: `NA_1.0.25_Setup.sh`, `NA_1.0.25_SetupFiles.zip`, `Register_Installer.sh`
- Update firewall/routing rules to allow connectivity via the new IP 172.19.14.86
- Ensure old IP 172.19.14.85 is removed from configuration before June 06, 2026

## Important Dates

- **June 06, 2026**: New IP and NA v1.0.25 available during mock session; old IP 172.19.14.85 decommissioned; NA files available on Extranet by 08:00 hours
- **June 08, 2026**: New IP parameter goes live in production

## Impact Assessment

This update is operationally significant for EGR segment members (trading members using interactive/NEAT connectivity). Failure to update the NEAT Adapter and IP configuration before June 06, 2026 will result in loss of connectivity to the EGR segment. The change has no direct impact on securities prices, listings, or investors. Members should plan the upgrade during off-market hours and test connectivity during the mock session on June 06, 2026 before the live effective date of June 08, 2026.