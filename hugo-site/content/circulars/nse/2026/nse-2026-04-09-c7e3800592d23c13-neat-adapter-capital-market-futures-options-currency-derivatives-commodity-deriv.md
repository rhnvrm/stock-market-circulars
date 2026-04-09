---
category: market-operations
circular_id: c7e3800592d23c13
date: '2026-04-09'
description: NSE releases NEAT Adapter version 1.0.27 for all four segments with enhanced
  encryption and additional authentication mechanisms, available from April 10, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD73674.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Mandatory software upgrade for all trading members across four segments;
  non-compliance may disrupt trading access after discontinuation of older versions.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD73674.zip
processing:
  attempts: 1
  content_hash: 9286b9ee5b3aa316
  processed_at: '2026-04-09T10:17:16.363295'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-04-09T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD73674.zip
severity: medium
source: nse
stocks: []
tags:
- neat-adapter
- trading-software
- capital-market
- futures-options
- currency-derivatives
- commodity-derivatives
- encryption
- software-update
- member-services
- authentication
title: NEAT Adapter v1.0.27 Released for CM, FO, Currency & Commodity Derivatives
  Segments
---

## Summary

NSE's Member Service Department is releasing NEAT Adapter version 1.0.27 for Capital Market (CM), Futures & Options (FO), Currency Derivatives (CD), and Commodity Derivatives (CO) segments. The new version incorporates an updated encryption mechanism with additional authentication as mandated by earlier circulars. The software will be available for download from Extranet starting April 10, 2026 at 20:00 hours.

## Key Points

- New NEAT Adapter version 1.0.27 released for all four segments: CM, FO, CD, and CO
- Includes new encryption mechanism with additional authentication
- Available for both Windows and Linux platforms
- Download available from April 10, 2026, 20:00 hours onwards on Extranet
- Existing versions 1.0.20 and 1.0.22 have segment-specific GR ports; discontinuation dates to be communicated separately

## Regulatory Changes

This release implements encryption and authentication changes mandated by prior circulars:
- NSE/CD/70422 dated September 25, 2025 (Currency Derivatives)
- NSE/COM/71599 dated December 02, 2025 (Commodity Derivatives)
- NSE/CMTR/72769 dated February 12, 2026 (Capital Market)
- NSE/FAOP/72763 dated February 12, 2026 (Futures & Options)

## Compliance Requirements

All members using NEAT Adapter must download and install version 1.0.27:
- **Windows**: Download `NA_1.0.27_Setup.exe` and `Register_Installer.bat`
- **Linux**: Download `NA_1.0.27_Setup.sh`, `NA_1.0.27_SetupFiles.zip`, and `Register_Installer.sh`

Extranet download paths by segment:
- Currency Derivatives (CD): `/cdsftp/cdscommon/NeatAdapter/`
- Commodity Derivatives (CO): `/comtftp/comtcommon/NeatAdapter/`
- Capital Market (CM): `/common/NeatAdapter/`
- Futures & Options (FO): `/faoftp/faocommon/NeatAdapter/`

## Important Dates

- **April 10, 2026, 20:00 hrs**: NEAT Adapter v1.0.27 available for download on Extranet
- Discontinuation dates for older versions (1.0.20, 1.0.22) to be communicated separately

## Impact Assessment

All trading members across CM, FO, CD, and CO segments who use NEAT Adapter are impacted. The upgrade is mandatory and introduces stronger security through new encryption and authentication. Members should plan the installation before older versions are discontinued to avoid trading disruptions. GR ports remain segment-specific (CD: 10877, CO: 10857, CM: 10817, FO: 10827) during the coexistence period.