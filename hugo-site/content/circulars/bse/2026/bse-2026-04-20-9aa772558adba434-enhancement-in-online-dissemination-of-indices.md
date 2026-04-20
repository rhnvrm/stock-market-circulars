---
category: market-operations
circular_id: 9aa772558adba434
date: '2026-04-20'
description: BSE proposes enhancements to online dissemination of indices including
  BSE FOCUSED IT, BSE FOCUSED MIDCAP, and BSE SENSEX NEXT 30 via NFCast, MDI/EMDI
  streams, and Indicative Close Value broadcasting, effective April 27, 2026.
draft: false
guid: https://www.bseindia.com/downloads/UploadDocs/Notices/20260420-33/20260420-33.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical enhancement affecting market data vendors and trading members
  who consume index broadcast feeds; no direct compliance burden on investors but
  requires system changes by third-party vendors before April 27, 2026.
pdf_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260420-33/20260420-33.pdf
processing:
  attempts: 1
  content_hash: 5ce74dec68077aaf
  processed_at: '2026-04-20T16:19:07.493413'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-04-20T14:08:07+00:00'
rss_url: https://www.bseindia.com/downloads/UploadDocs/Notices/20260420-33/20260420-33.pdf
severity: low
source: bse
stocks: []
tags:
- indices
- market-data
- nfcast
- mdi
- emdi
- sensex
- trading-development
- broadcast
- indicative-close-value
- equity-segment
title: Enhancement in Online Dissemination of Indices
---

## Summary

BSE is enhancing its online dissemination of indices by expanding real-time broadcast coverage to three additional indices — BSE FOCUSED IT, BSE FOCUSED MIDCAP, and BSE SENSEX NEXT 30 — across NFCast, MDI, and EMDI market data streams. Additionally, Indicative Close Value dissemination (currently limited to BSE SENSEX and BSE BANKEX) will be extended to these three indices. Changes go live on April 27, 2026, with a mock session on April 25, 2026.

## Key Points

- BSE FOCUSED IT, BSE FOCUSED MIDCAP, and BSE SENSEX NEXT 30 will be added to index broadcast message type 2011 via NFCast at 1-second intervals
- BSE SENSEX 50 will also move to message type 2011 (previously disseminated via type 2012)
- The same three new indices will be disseminated at 1-second intervals via MDI and EMDI streams, matching the frequency of SENSEX, BANKEX, SENSEX 50, and BSE 100
- Indicative Close Value for BSE FOCUSED IT, BSE FOCUSED MIDCAP, and BSE SENSEX NEXT 30 will be broadcast during the last 30 minutes of Equity segment trading hours via NFCAST and MDI/EMDI
- Enhancements are available for testing in the simulation environment immediately

## Regulatory Changes

No new regulatory mandate; this is a technical infrastructure enhancement by BSE Trading Development. It extends existing dissemination mechanisms (established under circulars 20230419-43, 20230503-26, and 20230529-11) to cover additional indices.

## Compliance Requirements

- Trading members and third-party trading application vendors must review the changes and make necessary system updates before April 27, 2026
- Participants are encouraged to test their systems during the mock trading session on April 25, 2026
- Contact BSE for queries: bsehelp@bseindia.com / 022-45720400 or iml.info@bseindia.com / 022-2272 8705

## Important Dates

- **April 20, 2026**: Circular issued
- **April 25, 2026**: Mock trading session to test enhancements
- **April 27, 2026**: Enhancements go live in Equity segment

## Impact Assessment

This enhancement primarily affects market data consumers — trading members, algorithmic traders, and third-party application vendors — who subscribe to NFCast, MDI, or EMDI feeds. Systems consuming index broadcast messages must be updated to handle the new indices in message type 2011 and the expanded Indicative Close Value feed. End investors are not directly impacted. The change improves real-time price discovery for BSE FOCUSED IT, BSE FOCUSED MIDCAP, and BSE SENSEX NEXT 30, which may benefit index-tracking products and derivatives strategies on these indices.