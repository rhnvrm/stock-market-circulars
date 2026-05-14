---
category: market-operations
circular_id: 84b9d700a16f950f
date: '2026-05-14'
description: NSE releases NEAT Adapter version 1.0.25 for the Electronic Gold Receipts
  (EGR) segment, enabling login through NEATPlus frontend for both Windows and Linux
  platforms, available from May 16, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD74225.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational circular affecting EGR segment members who need to upgrade
  to NEAT Adapter v1.0.25 for continued trading access; limited to EGR segment participants
  and has a clear deadline of May 16, 2026.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD74225.zip
processing:
  attempts: 1
  content_hash: bb5b3c583464f0be
  processed_at: '2026-05-14T17:08:28.384348'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-14T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD74225.zip
severity: medium
source: nse
stocks: []
tags:
- neat-adapter
- electronic-gold-receipts
- egr
- neatplus
- member-services
- technology
- trading-infrastructure
- windows
- linux
title: NEAT Adapter Release for Electronic Gold Receipts (EGR) Segment
---

## Summary

NSE's Member Service Department has announced the release of NEAT Adapter version 1.0.25 for the Electronic Gold Receipts (EGR) segment. This release facilitates member login through the Exchange-provided NEATPlus frontend application. The application is available in both Windows and Linux variants and must be installed by May 16, 2026.

## Key Points

- NEAT Adapter v1.0.25 is being released for the EGR segment to support login via NEATPlus frontend
- Available for both Windows (`NA_1.0.25_Setup.exe`) and Linux (`NA_1.0.25_Setup.sh` + `NA_1.0.25_SetupFiles.zip`)
- Only 64-bit operating systems are supported; 32-bit is not supported
- Linux requires RHEL version 8.5 or higher (64-bit)
- Windows requires Windows 10 or higher (64-bit)
- GR Port 10863 is designated for EGR segment connectivity
- NA Analysis tool is available to assist with Neat Adapter configuration diagnostics
- Files available on Extranet at `/egcommon/NeatAdapter/Windows` and `/egcommon/NeatAdapter/Linux`

## Regulatory Changes

This circular references NSE/EGR/74203 dated May 13, 2026 regarding trading parameters in EGR. The NEAT Adapter release is a technical enablement circular, not a regulatory rule change, but it is mandatory for EGR segment members to adopt the specified version for continued access.

## Compliance Requirements

- Members must download and install NEAT Adapter v1.0.25 from the Extranet before May 16, 2026, 08:00 hours
- Members must use Port 10863 when connecting to the EGR segment via NEAT Adapter
- Members should refer to the attached user manual for OS compatibility, installation instructions, and network prerequisites
- Members may use the NA Analysis tool (available on Extranet at `/egcommon/NA_Analysis_tool`) for configuration assistance
- For support, members can contact the Toll Free number: 1800 266 0050 (Option 1) or email msm@nse.co.in

## Important Dates

- **May 14, 2026**: Circular issued
- **May 16, 2026, 08:00 hours onwards**: NEAT Adapter v1.0.25 available on Extranet for download; mock release effective

## Impact Assessment

This circular impacts EGR segment members who use the NEATPlus frontend for trading. Members must upgrade to NEAT Adapter v1.0.25 to maintain trading access in the EGR segment. The impact is operational and limited to the EGR segment participant base. Members running 32-bit OS or older Linux/Windows versions will need to upgrade their systems to comply with the new OS requirements before installing the adapter.