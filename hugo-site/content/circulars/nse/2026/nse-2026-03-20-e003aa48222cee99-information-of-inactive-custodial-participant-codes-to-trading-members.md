---
category: market-operations
circular_id: e003aa48222cee99
date: '2026-03-20'
description: NSE Clearing Ltd. introduces a facility for Custodians to disseminate
  information on inactive Custodial Participant (CP) codes, with a consolidated file
  made available to trading members by 8:00 PM daily. The facility goes live from
  March 27, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMPT73380.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational change affecting custodians and trading members regarding
  CP code activity status; limited to clearing and settlement workflow, no direct
  market or price impact.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMPT73380.zip
processing:
  attempts: 1
  content_hash: dcffeed877760d2e
  processed_at: '2026-03-20T09:44:48.263739'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-03-20T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMPT73380.zip
severity: medium
source: nse
stocks: []
tags:
- custodial-participant
- cp-codes
- clearing
- settlement
- n-mass
- trading-members
- custodians
- capital-market
title: Information of Inactive Custodial Participant Codes to Trading Members
---

## Summary

NSE Clearing Limited (NCL) is introducing a facility for Custodians to upload and disseminate information about inactive Custodial Participant (CP) codes — those for which clearing and settlement activities will not be performed by Custodians. A consolidated list of inactive CP codes from all custodians will be made available to trading members as a daily file by 8:00 PM. The facility becomes available from March 27, 2026.

## Key Points

- NSE Clearing will provide a daily file `CM_InactiveCP_ddmmyyyy.csv` listing all inactive CP codes by 8:00 PM
- Custodians can upload inactive CP code information via the N-MASS application between 9:00 AM and 7:00 PM on working days
- File upload is accessible via: N-MASS → Online CP → INACTIVE CP → FILE UPLOAD
- Custodians must assign the INACTIVE CP role for FILE UPLOAD and FILE DOWNLOAD services through ROLE MANAGEMENT, with 'Write' access
- Upload file naming convention: `CM_InactiveCP_DDMMYYYY_nn.csv` (nn = incremental batch number starting at 01)
- Response files are generated per batch: suffix 'S' for fully successful, 'R' if any/all records are rejected
- The consolidated file for trading members is placed at: Extranet/Common/clearing folder

## Regulatory Changes

- New operational facility introduced under NCL Circular Ref. No: 0114/2026
- Custodians now have a formal channel to flag CP codes as inactive for clearing and settlement purposes
- The latest successfully uploaded file from each custodian will be treated as the final record for inactive CP codes

## Compliance Requirements

- **Custodians** must:
  - Configure ROLE MANAGEMENT in N-MASS to enable INACTIVE CP access with 'Write' permissions
  - Submit all inactive CP codes in a single file; any modification, addition, or deletion requires re-uploading the complete file
  - Use UPPER CASE for all CP codes with no leading/trailing spaces or junk characters
  - Ensure CP codes are valid and linked to the custodian in NCL
  - No need to upload daily if there are no changes; last successful upload remains in effect
- **Trading Members** should:
  - Monitor the daily `CM_InactiveCP_ddmmyyyy.csv` file from the Extranet/Common/clearing folder to identify CP codes flagged as inactive

## Important Dates

- **March 20, 2026**: Circular issued
- **March 27, 2026**: Facility goes live for custodians and trading members

## Impact Assessment

This change affects custodians and trading members operating in the Capital Market Segment. Custodians gain a structured mechanism to communicate inactive CP codes to NCL, reducing settlement risks arising from trades routed through non-operational custodial accounts. Trading members will have daily visibility into inactive CP codes, enabling them to avoid or flag such trades proactively. The operational impact is moderate — requiring one-time role configuration in N-MASS and periodic file management by custodians.