---
category: compliance
circular_id: 4fa6f006fa6055ed
date: '2025-10-17'
description: BSE mandates system audit requirements and Terms of Reference (TOR) for
  stockbrokers and trading members covering CTCL, IBT, ALGO, DMA, and SOR systems
  for the half year ended September 30, 2025.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={8311276C-EE9E-42F7-BE0E-ECF47E8A6DF7}&noticeno=20251017-29&dt=10/17/2025&icount=29&totcount=33&flag=0
impact: high
impact_ranking: high
importance_ranking: high
justification: Mandatory system audit requirement for all stockbrokers and trading
  members with detailed TOR covering critical trading systems and controls for regulatory
  compliance
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20251017-29&attachedId=dabf5ed1-903b-48a8-85c2-157b29a48910
processing:
  attempts: 1
  content_hash: 1c0b15d58a4cd204
  processed_at: '2025-10-17T12:41:44.614066'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-10-17T11:32:44+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={8311276C-EE9E-42F7-BE0E-ECF47E8A6DF7}&noticeno=20251017-29&dt=10/17/2025&icount=29&totcount=33&flag=0
severity: high
source: bse
stocks: []
tags:
- system-audit
- stockbrokers
- trading-members
- ctcl
- ibt
- algo
- dma
- sor
- compliance
- audit-requirements
- order-management
- risk-management
title: System Audit of Stockbrokers / Trading Members for the Half Year Ended September
  30, 2025
---

## Summary

BSE has issued comprehensive Terms of Reference (TOR) for system audit of stockbrokers and trading members for the half year ended September 30, 2025. The audit covers all API-based trading terminals including CTCL (Client to Client Link), IBT (Internet Based Trading), SOR (Smart Order Routing), STWT (Single Touch What-If Trading), ALGO (Algorithmic Trading), and DMA (Direct Market Access) systems. This annexure outlines detailed system control and capability requirements that auditors must verify.

## Key Points

- System auditors must verify order tracking processes at API-based terminals (CTCL/SOR/IBT/STWT/ALGO/DMA)
- Systems must capture order ID, time stamping, order type, scrip details, action, quantity, price, and validity
- Order rejection capability required for orders failing validation at broker level and Exchange servers
- Timely communication of trade confirmation and order status to clients via email and trade logs is mandatory
- Client ID verification systems must recognize only authorized client orders
- Proper restrictions and controls required for proprietary account orders from CTCL terminals
- Orders must have unique flags/tags as specified by Exchange for different order types
- System parameters including approved software versions, strategy names, and order gateway versions must comply with Exchange norms
- Server location addresses for all trading systems must be documented
- Systems must provide price broadcast, order processing, modification/cancellation, and trade confirmation features
- Gateway parameters including Trader ID, Market Segment (CM), CTCL ID, and IP Address must be verified

## Regulatory Changes

This circular reinforces existing regulatory framework for system audits with detailed TOR. No new regulatory changes are introduced, but the comprehensive checklist ensures standardized audit procedures across all stockbrokers and trading members.

## Compliance Requirements

- Stockbrokers and trading members must ensure their systems comply with all specified TOR parameters
- Systems must have capability to generate/capture complete order details with proper time stamping
- IP addresses of order entry terminals must be captured for all orders
- Order level validation must be implemented at broker terminals and Exchange servers
- Client ID verification and mapping of user IDs to predefined locations for proprietary orders is mandatory
- Systems must distinguish orders by type (CTCL/IBT/STWT/ALGO/DMA/SOR) with unique Exchange-specified flags
- 15-digit CTCL field must be populated in order structure for every order
- Installed software versions and system features must match Exchange-approved specifications
- Order placement controls must allow only orders matching system parameters
- Features for order modification, cancellation, and outstanding order checks must be operational
- System-based controls over order input process must be implemented
- Trade history and confirmation features must be available to users

## Important Dates

- Audit Period: Half year ended September 30, 2025
- Submission deadline for system audit reports not specified in this excerpt (refer to main circular)

## Impact Assessment

**Operational Impact:** High - All stockbrokers and trading members must undergo comprehensive system audits covering multiple trading platforms and order management systems. This requires significant coordination between brokers, system auditors, and compliance teams.

**Market Impact:** Medium - Enhanced system controls and audit requirements strengthen market integrity and investor protection by ensuring robust order management and risk controls across all trading channels.

**Compliance Impact:** High - Detailed TOR creates stringent compliance requirements for system configurations, software versions, order tracking, and client verification processes. Non-compliance may result in regulatory action.

**Technology Impact:** High - Brokers must ensure their technology infrastructure meets all specified parameters including order tracking, IP capture, client verification, and system-based controls across all trading platforms.