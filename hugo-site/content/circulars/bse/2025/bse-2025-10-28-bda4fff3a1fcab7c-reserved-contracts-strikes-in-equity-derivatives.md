---
category: trading
circular_id: bda4fff3a1fcab7c
date: '2025-10-28'
description: BSE introduces real-time notification mechanism for intraday contract
  activation in equity derivatives through News Message framework, now available for
  both LF and HF sessions.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={8344DF3F-0F16-4234-836E-4A372A6E1DFF}&noticeno=20251028-51&dt=10/28/2025&icount=51&totcount=52&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical infrastructure update affecting equity derivatives trading
  members. Requires system configuration changes to receive real-time contract activation
  messages. Extends News Broadcast to HF sessions, improving information delivery
  reliability.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251028-51&attachedId=21a259e9-b9f8-4870-94b3-5207c1172279
processing:
  attempts: 1
  content_hash: 2cbecd796a59ffa4
  processed_at: '2025-10-28T15:30:37.736307'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-28T14:44:53+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={8344DF3F-0F16-4234-836E-4A372A6E1DFF}&noticeno=20251028-51&dt=10/28/2025&icount=51&totcount=52&flag=0
severity: medium
source: bse
stocks: []
tags:
- contract-activation
- derivatives
- eti-messaging
- market-infrastructure
- news-broadcast
- technical-update
title: Reserved Contracts (Strikes) in Equity Derivatives - Intraday Activation Messaging
---

## Summary

BSE has implemented a real-time notification mechanism for communicating intraday contract activation in equity derivatives. The Exchange will send activation notifications through the News Message (Template ID 10031) as defined in the Exchange Trading Interface (ETI) messaging format. The activation message will appear in the Var Text field (30355). Importantly, the News Broadcast Message framework, previously available only to LF (Low Frequency) sessions, will now also be available to HF (High Frequency) sessions on subscription.

## Key Points

- Intraday contract activation communicated via News Message (Template ID 10031) in ETI messaging format
- Activation message delivered in Var Text field (30355)
- Real-time delivery mechanism ensures immediate notification
- Re-transmission support ensures message delivery even during temporary disconnections
- News Broadcast Message now available to both LF and HF sessions on subscription
- Members must refer to ETI Messaging Format Document Version 1.6.13 for implementation details

## Regulatory Changes

Expansion of News Broadcast Message availability from LF sessions only to both LF and HF sessions on subscription basis. This represents an enhancement to the existing messaging infrastructure for equity derivatives trading.

## Compliance Requirements

- Member applications must be configured to receive News Message (Template ID 10031)
- Systems should be set up to parse the Var Text field (30355) for activation messages
- Members must refer to the News Broadcast Message framework detailed in ETI Messaging Format Document Version 1.6.13
- Member systems should subscribe to News Broadcast Messages for their respective session types (LF/HF)
- Systems must be appropriately configured to handle re-transmission mechanism

## Important Dates

No specific implementation dates mentioned. Circular appears to document existing/current functionality.

## Impact Assessment

**Technical Impact:** Medium - Requires member systems to be configured for News Message framework and ETI messaging format Version 1.6.13. Members need to ensure their applications can receive and process these notifications.

**Operational Impact:** Positive - Real-time notification and re-transmission support eliminates information loss due to temporary disconnections, improving operational reliability for derivatives trading members.

**Trading Impact:** Medium - Affects equity derivatives trading infrastructure. Members trading in reserved contracts (strikes) need proper system configuration to receive activation notifications in real-time.

**Member Preparedness:** Members should verify their systems are subscribed to News Broadcast Messages and properly configured to handle Template ID 10031 messages, particularly HF session members who now have access to this framework.