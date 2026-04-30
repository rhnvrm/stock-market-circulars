---
category: market-operations
circular_id: 52052f39a9bf45a0
date: '2026-04-30'
description: NSE consolidated circular replacing NSE/MSD/67674 (April 24, 2025), providing
  updated gateway IPs, ports, and subnet parameters for interactive connectivity across
  Capital Market, F&O, Currency Derivatives, Commodity Derivatives, and SLBM segments.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD73993.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational circular for exchange members updating technical connectivity
  parameters; does not affect market rules or listed securities, but non-compliance
  with updated parameters could disrupt member trading access.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD73993.pdf
processing:
  attempts: 1
  content_hash: aa7b466f980ad437
  processed_at: '2026-04-30T14:12:31.890381'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-04-30T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD73993.pdf
severity: medium
source: nse
stocks: []
tags:
- interactive-connectivity
- network-parameters
- gateway
- capital-market
- futures-options
- currency-derivatives
- commodity-derivatives
- slbm
- trade-drop-copy
- member-services
- consolidated-circular
- technical-infrastructure
title: Interactive Connectivity Parameters - Consolidated Circular (NSE/MSD/73993)
---

## Summary

NSE's Member Service Department has issued a consolidated circular (Ref No: NSE/MSD/73993, Circular 32/2026) replacing the earlier consolidated circular NSE/MSD/67674 dated April 24, 2025. This circular compiles all interactive connectivity-related instructions issued up to March 31, 2026, and provides updated gateway IP addresses, port numbers, and subnet parameters for all trading segments.

## Key Points

- Replaces consolidated circular NSE/MSD/67674 dated April 24, 2025
- Covers all circulars pertaining to interactive connectivity issued up to March 31, 2026
- Parameters apply to all live and mock (regular and BCP) trading sessions
- Includes parameters for Trade Drop Copy Facility and New Order & Trade Drop Copy Facility
- Non-compliance may invite disciplinary action under Exchange Byelaws, Rules and Regulations
- New encryption message ports introduced with MD5 checksum removal
- Additional port variant supports new immediate Ack request for order-related messages

## Regulatory Changes

This consolidated circular introduces updated port designations across segments:

- **Starred ports (*)**: Support new encryption messages with MD5 checksum removal
- **Double-starred ports (**)**: Support new encryption messages with MD5 checksum removal AND new immediate Ack request for order-related messages

No information has been rescinded in this consolidation. Actions taken under rescinded guidelines in any future rescission remain valid and unaffected.

## Compliance Requirements

- Members must use the CA certificate with the parameters specified in Annexure 1
- Members must configure connectivity using the updated gateway IPs and port numbers for each segment
- Members must remain compliant with all Exchange circulars, communications, instructions, and directions issued from time to time
- Parameters apply across live trading, mock (regular), and BCP (Business Continuity Plan) sessions

**Gateway Parameters (Annexure 1 — CA Certificate):**

| Segment | Gateway Router IP | Port | Subnet | Mask | Port |
|---|---|---|---|---|---|
| Capital Market (CM) | 172.19.12.85 | 10817, 10823*, 10825**, 10827 | 172.19.12.0 | 255.255.255.128 | 10810 |
| Futures & Options (FO) | 172.19.13.85 | 10833*, 10835** | 172.19.13.0 | 255.255.255.128 | 10820 |
| Currency Derivatives (CD) | 172.19.18.85 | 10877, 10879*, 10881** | 172.19.18.0 | 255.255.255.128 | — |
| Commodity Derivatives (COM) | 172.19.15.85 | 10857, 10859*, 10861**, 10870, 10871 | 172.19.15.0 | 255.255.255.128 | 10850 |
| SLBM | 172.19.14.85 | 10887 | 172.19.14.0 | 255.255.255.128 | 10860 |

## Important Dates

- **Circular Date**: April 30, 2026
- **Replaces**: NSE/MSD/67674 dated April 24, 2025
- **Coverage**: All interactive connectivity circulars issued up to March 31, 2026

## Impact Assessment

This is a technical/operational circular targeting exchange members' IT and network teams. The update to encryption parameters (MD5 checksum removal, new Ack request mechanism) signals a security and protocol modernization effort. Members who have not already migrated to the new starred/double-starred ports will need to update their connectivity configurations. Failure to comply could result in trading disruptions or disciplinary action. No direct impact on listed securities, market structure, or retail investors.