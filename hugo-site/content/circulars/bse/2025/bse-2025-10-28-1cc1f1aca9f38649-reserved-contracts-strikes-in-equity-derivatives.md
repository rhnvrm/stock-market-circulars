---
category: trading
circular_id: 1cc1f1aca9f38649
date: '2025-10-28'
description: BSE announces enhanced notification framework for intraday contract activation
  in equity derivatives through News Message (Template ID 10031) with re-transmission
  support and HF session availability.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={8344DF3F-0F16-4234-836E-4A372A6E1DFF}&noticeno=20251028-51&dt=10/28/2025&icount=51&totcount=64&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical infrastructure update affecting derivative trading members'
  systems. Requires system configuration changes but enhances reliability through
  re-transmission support and HF session access.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251028-51&attachedId=21a259e9-b9f8-4870-94b3-5207c1172279
processing:
  attempts: 1
  content_hash: a1792f1f41cda622
  processed_at: '2025-10-28T18:46:53.046568'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-28T14:44:53+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={8344DF3F-0F16-4234-836E-4A372A6E1DFF}&noticeno=20251028-51&dt=10/28/2025&icount=51&totcount=64&flag=0
severity: medium
source: bse
stocks: []
tags:
- equity-derivatives
- trading-infrastructure
- eti-messaging
- contract-activation
- news-broadcast
- high-frequency-trading
- system-configuration
title: Reserved Contracts (Strikes) in Equity Derivatives - Intraday Activation Notification
  Framework
---

## Summary

BSE has updated the communication framework for reserved contract (strike) activation in equity derivatives. The exchange will use News Message (Template ID 10031) in ETI messaging format to notify members in real-time. Key enhancements include re-transmission capability for disconnected applications and extension of News Broadcast Message availability to High Frequency (HF) sessions on subscription basis.

## Key Points

- Activation notifications delivered via News Message Template ID 10031 in Exchange Trading Interface (ETI) format
- Activation message appears in Var Text field (30355)
- Real-time delivery of contract activation messages to member applications
- Re-transmission support ensures message delivery even if members were disconnected during activation
- No information loss due to temporary connection issues
- News Broadcast Message now available to both LF (Low Frequency) and HF (High Frequency) sessions on subscription
- Previously News Broadcast was only available to LF sessions

## Regulatory Changes

Expansion of News Broadcast Message framework to include High Frequency (HF) trading sessions, in addition to existing Low Frequency (LF) session support. This represents a technical enhancement to the existing notification infrastructure.

## Compliance Requirements

- Members must refer to ETI Messaging Format Document Version 1.6.13 for News Broadcast Message framework details
- Trading systems must be configured to receive and process Template ID 10031 messages
- Member applications should implement support for News Broadcast Message subscription for HF sessions if applicable
- Systems must be configured to handle Var Text field (30355) containing activation messages
- Members should ensure their applications can process re-transmitted messages correctly

## Important Dates

- Circular Date: October 28, 2025
- No specific implementation deadline mentioned; appears to be informational regarding existing/enhanced framework

## Impact Assessment

**Operational Impact:** Medium - Trading members using equity derivatives must ensure their systems are properly configured to receive activation notifications through the specified ETI messaging framework.

**Technical Impact:** The re-transmission feature significantly improves reliability by preventing information loss during temporary disconnections. Extension to HF sessions benefits high-frequency trading firms by providing real-time contract activation data through their preferred session type.

**Market Impact:** Low to Medium - Enhances operational efficiency and reduces risk of missed contract activations, particularly benefiting algorithmic and high-frequency trading strategies that require immediate awareness of newly activated strikes.