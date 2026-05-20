---
category: market-operations
circular_id: 80db3b2bdd31b595
date: '2026-05-20'
description: NSE will incorporate dummy securities (identified by 'NSETEST' suffix)
  in EGR security master files for internal pre-market sanity checks. Market participants
  should ignore any data related to these dummy securities.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/EGR74310.pdf
impact: low
impact_ranking: low
importance_ranking: low
justification: Purely an internal operational notice about dummy securities used for
  exchange testing. No regulatory change, no compliance action required from market
  participants beyond ignoring NSETEST-suffixed symbols.
pdf_url: https://nsearchives.nseindia.com/content/circulars/EGR74310.pdf
processing:
  attempts: 1
  content_hash: 5d7a788eed11b6f7
  processed_at: '2026-05-20T20:30:44.304118'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-20T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/EGR74310.pdf
severity: low
source: nse
stocks: []
tags:
- electronic-gold-receipts
- egr
- master-files
- dummy-securities
- pre-market
- sanity-checks
- trading-platform
- nsetest
title: Dummy Securities in EGR Master Files for Internal Exchange Testing
---

## Summary

NSE has introduced dummy securities into the Electronic Gold Receipts (EGR) security master files (`security_eg.txt` and `nnf_security_eg.dat`) to support internal pre-market sanity checks conducted before market hours each trading day. These dummy securities are identifiable by the last 7 characters of their symbol being "NSETEST" and are intended solely for internal exchange testing purposes.

## Key Points

- Dummy securities will be added to EGR master files: `security_eg.txt` and `nnf_security_eg.dat`
- Dummy securities are identified by symbols ending in "NSETEST" (last 7 characters)
- The exchange conducts internal order/trade activity before market hours as pre-market sanity checks
- Market participants must ignore any data, reports, feeds, or broadcasts related to these dummy securities
- Any processing or action taken on dummy security data is entirely at the participant's own risk
- NSE, its officers, and employees will bear no liability for decisions made based on this data

## Regulatory Changes

No regulatory changes. This is an operational update to the EGR trading platform to incorporate dummy securities for internal testing. The change is effective immediately and will remain in place until further notice.

## Compliance Requirements

- Market participants must identify dummy securities by the "NSETEST" suffix (last 7 characters of symbol)
- Participants must ignore receipt of any data, reports, feeds, or broadcasts involving these dummy securities
- No processing, referencing, or consumption of dummy security data should be performed
- Systems may need to be updated to filter out symbols ending in "NSETEST" from EGR master file processing

## Important Dates

- **Effective Date:** May 20, 2026 (already live)
- **Duration:** Until further notice

## Impact Assessment

Impact on market participants is minimal. This is an internal NSE operational measure for platform stability and pre-market testing. Participants who consume EGR security master files programmatically should implement a filter to exclude symbols with the "NSETEST" suffix to avoid unintended processing. No trading, financial, or compliance obligations are created by this circular.