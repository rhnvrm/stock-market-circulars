---
category: trading
circular_id: 867ac98b2e7fdb8e
date: '2025-09-05'
description: NSE withdraws NEAT Adapter version 1.0.21 for Currency Derivatives segment
  and instructs members to revert to version 1.0.20 immediately.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD70064.pdf
impact: high
impact_ranking: high
importance_ranking: high
justification: Critical system update affecting all currency derivatives trading members
  with immediate action required
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD70064.pdf
processing:
  attempts: 1
  content_hash: 10bd018e987f4a4a
  processed_at: '2025-09-05T12:40:04.629382'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-09-05T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD70064.pdf
severity: high
source: nse
stocks: []
tags:
- derivatives
- market-infrastructure
- system-update
- technical
- trading-platform
title: NEAT Adapter Update for Currency Derivatives Segment - Version 1.0.21 Withdrawn
---

## Summary

NSE has withdrawn NEAT Adapter version 1.0.21 for Currency Derivatives segment due to issues with new encryption mechanism and authentication measures. All members using version 1.0.21 must immediately revert to version 1.0.20 until a new version 1.0.22 is released.

## Key Points

- NEAT Adapter version 1.0.21 for Currency Derivatives segment is withdrawn with immediate effect
- Members must revert to existing version 1.0.20 on priority
- New version 1.0.22 will be announced via separate circular
- Version 1.0.20 uses GR PORT 10877 and remains effective
- Version 1.0.21 uses GR PORT 10879 and will be discontinued from October 4, 2025

## Regulatory Changes

Withdrawal of problematic NEAT Adapter version 1.0.21 that contained issues with new encryption mechanism and additional authentication measures introduced in previous circular NSE/MSD/69058 dated July 10, 2025.

## Compliance Requirements

- Members currently using NEAT Adapter version 1.0.21 must immediately revert to version 1.0.20
- Use appropriate setup files from designated extranet paths:
  - Windows: /cdsftp/cdscommon/NeatAdapter/Windows
  - Linux: /cdsftp/cdscommon/NeatAdapter/Linux
- Configure system to use GR PORT 10877 for version 1.0.20
- Contact toll-free support (1800 266 0050, Option 1) for configuration assistance

## Important Dates

- **September 5, 2025**: Circular issued, immediate action required
- **Immediate effect**: Version 1.0.20 to be used
- **October 4, 2025**: Version 1.0.21 to be discontinued
- **Future date (TBA)**: Version 1.0.22 release announcement

## Impact Assessment

High operational impact on all Currency Derivatives segment members. Immediate system downgrade required to maintain trading operations. Members using version 1.0.21 face potential trading disruption if not reverted promptly. Technical support resources may experience increased demand during transition period.