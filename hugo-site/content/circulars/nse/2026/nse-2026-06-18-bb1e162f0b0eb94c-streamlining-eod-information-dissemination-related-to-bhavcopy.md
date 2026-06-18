---
category: market-operations
circular_id: bb1e162f0b0eb94c
date: '2026-06-18'
description: NSE will make bhavcopy (.DAT) reports available via Extranet from July
  2026 and will discontinue .MS/.MD format files and NNF API broadcast dissemination
  effective October 12, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD74764.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational change affecting all NSE members who consume bhavcopy data
  via legacy formats or broadcasts; requires technical migration by October 2026 but
  does not affect trading or pricing.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD74764.pdf
processing:
  attempts: 1
  content_hash: 166556e9cd7439bc
  processed_at: '2026-06-18T15:42:18.193953'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-06-18T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD74764.pdf
severity: medium
source: nse
stocks: []
tags:
- bhavcopy
- segment-bhavcopy
- market-data
- eod-data
- extranet
- data-dissemination
- nse
title: 'NSE Streamlines EOD Bhavcopy Dissemination: Extranet Access Added, Legacy
  Formats Discontinued'
---

## Summary

NSE is consolidating its end-of-day bhavcopy dissemination infrastructure. Starting July 2026, the existing website-based .DAT bhavcopy files will also be available on the Exchange Extranet. Concurrently, legacy .MS and .MD format bhavcopy files on the Extranet and bhavcopy broadcasts via the NNF API will be discontinued on **October 12, 2026**, as these duplicate information already available in the .DAT reports.

## Key Points

- Bhavcopy (.DAT format) currently published on the NSE website will be simultaneously disseminated via Extranet, rolled out by segment in phases from July 2026.
- Extranet paths for .DAT files: CM → `/cmftp/common/bhavcopy`, FO → `/faoftp/faocommon/Bhavcopy`, CD → `/cdsftp/cdscommon/Bhavcopy`, CO → `/comtftp/comtcommon/Bhavcopy`.
- Effective **October 12, 2026**, the following will be discontinued:
  - Extranet bhavcopy files in `.MS` and `.MD` formats across CM, FO, CD, and CO segments.
  - Bhavcopy dissemination via NNF API broadcasts for CM, FO, CD, and COM segments.
- Segment-wise effective dates for the new Extranet .DAT dissemination will be communicated separately.

## Regulatory Changes

No new regulatory mandate is introduced. This is an infrastructure rationalisation initiative by NSE to eliminate redundant data channels and standardise bhavcopy delivery to a single .DAT format across website and Extranet.

## Compliance Requirements

- Members consuming bhavcopy via Extranet .MS/.MD files must migrate their systems to use the .DAT format files on the corresponding Extranet paths before **October 12, 2026**.
- Members using NNF API broadcasts to receive bhavcopy data must switch to the Extranet .DAT file-based method before **October 12, 2026**.
- No action is required for members already using the website-based .DAT bhavcopy files.

## Important Dates

- **July 2026 onwards**: Phased rollout of .DAT bhavcopy files on Extranet (segment-wise dates to be communicated separately).
- **October 12, 2026**: Discontinuation of .MS/.MD bhavcopy files on Extranet and bhavcopy via NNF API broadcasts for all segments (CM, FO, CD, CO/COM).

## Impact Assessment

This change has moderate operational impact on members with automated systems that ingest bhavcopy data from Extranet legacy formats (.MS, .MD) or NNF API broadcasts. Such members must update their data pipelines to fetch .DAT files from the new Extranet paths. The content of the bhavcopy data itself is unchanged; only the delivery mechanism is being consolidated. Members relying solely on the NSE website for bhavcopy data are unaffected.