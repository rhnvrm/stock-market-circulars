---
category: market-operations
circular_id: 6d4314ce0c300da0
date: '2026-04-22'
description: NSE introduces changes to security master files (security.txt, nnf_security.dat,
  and MII Security File) to include a Closing Auction Session eligibility indicator,
  effective August 3, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMTR73845.zip
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical file format change affecting all members who consume NSE
  security master data feeds; advance notice of ~3.5 months provided before August
  2026 effective date. No trading restrictions or stock-specific impact.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMTR73845.zip
processing:
  attempts: 1
  content_hash: 7ac5d7d8bbfa3e96
  processed_at: '2026-04-22T13:35:08.078989'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-04-22T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMTR73845.zip
severity: medium
source: nse
stocks: []
tags:
- closing-auction-session
- security-master
- equity-segment
- file-format-change
- market-operations
- technical-update
- cas
title: NSE Security Master File Modifications for Closing Auction Session (CAS) in
  Equity Segment
---

## Summary

NSE is modifying the structure of security master files to support the introduction of the Closing Auction Session (CAS) in the Equity Segment. Specifically, the existing RETDEBT market eligibility/status fields are being repurposed or relabeled to indicate CAS eligibility. The changes affect security.txt, nnf_security.dat, and NSE_CM_security_ddmmyyyy.csv.gz. The effective date is August 03, 2026.

## Key Points

- An eligibility indicator for Closing Auction Session (CAS) will be introduced in all security master files
- Field 12 (security.txt / nnf_security.dat): "SecurityStatus in RETDBT market" is renamed to "Filler" (retired)
- Field 13 (security.txt / nnf_security.dat): "Eligibility" (RETDEBT Market) renamed to "Eligibility for Closing Auction Session" with updated value descriptions
- Field 23 (NSE_CM_security_ddmmyyyy.csv.gz): "SecurityStatus in RETDBT market" renamed to "Filler"; ISO tag SctyStsRETDBTMkt removed
- Field 24 (NSE_CM_security_ddmmyyyy.csv.gz): "Eligibility" (RETDEBT Market) renamed to "Eligibility for Closing Auction Session"; ISO tag updated from ElgbltyRETDBTMkt to ElgbltyClsgAuctnSsn
- Field 59 (NSE_CM_security_ddmmyyyy.csv.gz): ISO tag revised from Rsvd01 to XchgExclsv (filler field, no functional change)
- No other changes to file structure, format, or remaining fields

## Regulatory Changes

This circular partially modifies Part-D of the Capital Market consolidated circular (NSE/CMTR/67774 dated April 30, 2025). It is issued in furtherance of:
- SEBI circular HO/47/11/11(3)2025-MRD-POD2/I/2765/2026 dated January 16, 2026 (introducing CAS)
- NSE circular NSE/CMTR/72394 dated January 19, 2026
- NSE circular NSE/CMTR/73362 dated March 18, 2026

The field changes repurpose existing RETDEBT-related fields to serve CAS eligibility purposes in the Equity Segment.

## Compliance Requirements

- All NSE members and data consumers who parse or integrate security master files must update their systems to handle the revised field names, descriptions, and ISO tags
- Systems should treat Field 12 (security.txt/nnf_security.dat) and Field 23 (CSV file) as filler fields going forward
- Field 13 and Field 24 values (0/1) retain the same binary structure but now denote CAS eligibility rather than RETDEBT eligibility
- Members should validate their downstream systems against the updated Annexure A specifications before the effective date

## Important Dates

- **Circular Date:** April 22, 2026
- **Effective Date:** August 03, 2026

## Impact Assessment

This is a technical/operational change with moderate impact on members and vendors who consume NSE security master data feeds. The file structure itself is unchanged; only field semantics and ISO tags are revised, which limits integration risk. Members have approximately 3.5 months to update their parsing logic and downstream systems. No impact on trading rules, price bands, or individual securities. The change is market-wide and applies to all Equity Segment securities eligible for the new Closing Auction Session.