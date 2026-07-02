---
category: market-operations
circular_id: 2e991ccb9ca28eef
date: '2026-07-02'
description: NSE reminds members that old interactive ports for encrypted data flow
  across CM, FO, CD, COM and SLBM segments will be discontinued effective July 05,
  2026, requiring use of new interactive ports only.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD75014.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: This is an operational/technical connectivity change affecting trading
  members' system infrastructure; it does not directly impact listed securities or
  investors but requires timely member action to avoid connectivity disruption.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD75014.pdf
processing:
  attempts: 1
  content_hash: 14200de18349abc8
  processed_at: '2026-07-02T19:48:34.640524'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-07-02T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD75014.pdf
severity: medium
source: nse
stocks: []
tags:
- market-operations
- connectivity
- encryption
- interactive-parameters
title: 'Encryption of Interactive Messages: Old Interactive Ports to be Discontinued
  from July 5, 2026'
---

## Summary

NSE has issued a reminder to all members regarding the discontinuation of old interactive parameters used for encrypted data flow. This follows the earlier circular NSE/MSD/74511 dated June 02, 2026, which introduced a new CA certificate for encryption of interactive messages. The old interactive ports across CM, FO, CD, COM and SLBM segments will be discontinued effective July 05, 2026, and members must transition to using only the new interactive ports.

## Key Points

- This circular is a reminder to NSE/MSD/74511 dated June 02, 2026 regarding new CA certificate for encryption of interactive messages and discontinuation of old interactive parameters.
- Old interactive ports will be discontinued with effect from July 05, 2026.
- New ports and corresponding old ports are specified for each segment: CM, FO, CD, COM, and SLBM.
- Ports marked with a single asterisk (*) support new encryption messages with MD5 checksum removal.
- Ports marked with double asterisk (**) support new encryption messages with MD5 checksum removal plus new immediate Ack request for order related messages.
- Members still logging in via old ports must switch to using only the new interactive ports.
- All other details from the earlier circular (NSE/MSD/74511) remain unchanged.

## Regulatory Changes

No change in regulatory policy; this is a technical/operational update to network connectivity parameters (IP addresses, ports, subnet ranges) for interactive message encryption across trading segments (CM, FO, CD, COM, SLBM).

## Compliance Requirements

Members must ensure their systems are configured to use the new interactive ports (as specified for each segment) before July 05, 2026, since the old ports will cease to function from that date. Members using old ports will lose interactive connectivity if they do not migrate in time.

## Important Dates

- June 02, 2026: Original circular (NSE/MSD/74511) issued introducing new CA certificate and new ports.
- July 02, 2026: This reminder circular issued.
- July 05, 2026: Old interactive ports discontinued; only new ports will be operational.

## Impact Assessment

The impact is operational and limited to trading members' technical/IT infrastructure teams responsible for exchange connectivity. Members who fail to migrate to new interactive ports by July 05, 2026 risk losing interactive order connectivity to the exchange, which could disrupt trading operations. There is no direct impact on listed securities, stock prices, or investors.