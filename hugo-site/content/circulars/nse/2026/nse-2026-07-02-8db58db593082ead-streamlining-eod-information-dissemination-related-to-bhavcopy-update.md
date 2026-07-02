---
category: market-operations
circular_id: 8db58db593082ead
date: '2026-07-02'
description: NSE will additionally disseminate FO, CD and CO segment bhavcopy reports
  (.DAT format) on Extranet at specified file paths effective July 06, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD75001.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Operational/technical update on data dissemination file paths for members;
  no direct market or stock-specific impact.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD75001.pdf
processing:
  attempts: 1
  content_hash: d7f4ebca2c49c3d8
  processed_at: '2026-07-02T14:21:33.750167'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-07-02T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD75001.pdf
severity: low
source: nse
stocks: []
tags:
- bhavcopy
- market-operations
- segment-bhavcopy
title: Streamlining EOD Information Dissemination Related to Bhavcopy - Update on
  Extranet File Paths
---

## Summary

NSE has updated members on its earlier circular (NSE/MSD/74764 dated June 18, 2026) regarding streamlining End-of-Day (EOD) information dissemination related to Bhavcopy. Effective July 06, 2026, the Exchange will additionally disseminate bhavcopy reports in .DAT format on Extranet for the Futures & Options (FO), Currency Derivatives (CD), and Commodity (CO) segments at specified file paths.

## Key Points

- This circular is a continuation/update to NSE/MSD/74764 dated June 18, 2026.
- Bhavcopy reports in .DAT format will now be disseminated on Extranet in addition to the existing website dissemination.
- Segments covered: FO (Futures & Options), CD (Currency Derivatives), and CO (Commodity).
- File naming conventions: FNO_BCDDMMYYYY.DAT, CD_BCDDMMYYYY.DAT, CO_BCDDMMYYYY.DAT.
- These files are currently available on the website at https://www.nseindia.com/all-reports-derivatives under display names F&O-Bhavcopy File (DAT), CD-Bhavcopy File (DAT), and COM-Bhavcopy File (DAT).

## Regulatory Changes

No regulatory changes; this is an operational enhancement to data dissemination channels for EOD bhavcopy reports, expanding availability from website-only to also include Extranet.

## Compliance Requirements

Members relying on Extranet-based data feeds should update their systems to retrieve bhavcopy files from the newly specified Extranet paths:
- FO segment: /faoftp/faocommon/Bhavcopy
- CD segment: /cdsftp/cdscommon/Bhavcopy
- CO segment: /comtftp/comtcommon/Bhavcopy

No other action is required; website-based access to bhavcopy files remains available.

## Important Dates

- June 18, 2026: Original circular (NSE/MSD/74764) issued.
- July 02, 2026: This update circular issued.
- July 06, 2026: Effective date for additional dissemination of bhavcopy files on Extranet.

## Impact Assessment

This is a low-impact operational update primarily relevant to member firms and systems integrators who consume EOD bhavcopy data via Extranet. It does not affect trading, listing, or any specific stock, and provides an additional, redundant channel for data access rather than replacing existing website-based dissemination.