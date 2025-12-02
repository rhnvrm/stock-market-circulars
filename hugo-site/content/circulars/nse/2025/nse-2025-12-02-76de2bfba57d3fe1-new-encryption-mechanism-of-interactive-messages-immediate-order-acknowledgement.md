---
category: trading
circular_id: 76de2bfba57d3fe1
date: '2025-12-02'
description: NSE implements AES-256 GCM encryption and immediate order acknowledgement
  for Commodity Derivatives segment interactive messages to enhance security posture.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/COM71599.pdf
impact: high
impact_ranking: high
importance_ranking: high
justification: Mandatory technical upgrade affecting all members trading in commodity
  derivatives segment. Requires system changes, testing, and migration to new encryption
  mechanism with defined deadlines.
pdf_url: https://nsearchives.nseindia.com/content/circulars/COM71599.pdf
processing:
  attempts: 1
  content_hash: 04c7457306e52254
  processed_at: '2025-12-02T12:58:25.744232'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-02T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/COM71599.pdf
severity: high
source: nse
stocks: []
tags:
- encryption
- security
- commodity-derivatives
- trading-system
- neat-adapter
- nnf
- order-acknowledgement
- technical-upgrade
title: New Encryption Mechanism of Interactive Messages & Immediate Order Acknowledgement
---

## Summary

NSE is implementing enhanced security measures for Commodity Derivatives (CO) segment by introducing AES-256 GCM encryption with additional authentication for interactive messages and immediate acknowledgement for order-related messages. This follows a similar implementation in Currency Derivatives segment. Members using NEAT Adapter and NNF protocols must migrate to the new encryption mechanism during a coexistence phase, after which the existing encryption mechanism will be discontinued.

## Key Points

- New encryption uses AES-256 bits GCM encryption with additional authentication, replacing existing mechanism
- Introduction of immediate acknowledgment messages sent instantly upon receiving orders
- Combination of TLS 1.3 security protocol and AES-256 bits symmetric encryption
- Interim coexistence phase will allow both old and new encryption mechanisms
- New NEAT Adapter version 1.0.23 will be released with new encryption mechanism
- Existing NEAT Adapter version 1.0.20 will be discontinued (date to be communicated separately)
- Members can continue using existing CA certificate mentioned in circular NSE/MSD/67695 dated April 25, 2025
- Updated CO NNF API document Version 6.3 available on NSE website

## Regulatory Changes

NSE is upgrading security infrastructure for Commodity Derivatives segment with:

1. **Enhanced Encryption**: Migration from existing encryption to AES-256 GCM encryption with additional authentication
2. **Immediate Order Acknowledgement**: New acknowledgment messages confirming instant receipt of orders by Exchange
3. **Network Configuration Changes**: New ports and IP configurations for encrypted data flows

## Compliance Requirements

**For All Members Trading in Commodity Derivatives:**

1. Configure new interactive session parameters for encrypted data flows
2. Use designated IP Address: 172.19.15.85 (Gateway Router)
3. Configure appropriate ports based on user type:
   - Port 10857: NEAT, NNF Users (existing encrypted mechanism)
   - Port 10859: NEAT, NNF Users (new encryption with MD5 checksum removal)
   - Port 10861: Only for NNF Users (new encryption & immediate acknowledgement)
4. Network configuration: Gateway IPs Subnet 172.19.15.0, Mask 255.255.255.128, Port 10850

**For NNF API Users:**
- Continue using existing CA certificate from circular NSE/MSD/67695 dated April 25, 2025
- Refer to CO NNF API document Version 6.3 for implementation details
- Available at: https://www.nseindia.com/trade/platform-services-neat-trading-system-protocols

**For NEAT Adapter Users:**
- Upgrade to new NEAT Adapter version 1.0.23 when released
- Prepare for discontinuation of version 1.0.20
- Additional authentication of encrypted message flow required

## Important Dates

- **December 02, 2025**: Circular issued
- **December 13, 2025**: Release of new interactive parameters for NEAT Adapter and NNF users
- **December 13, 2025**: Release of new NEAT Adapter version 1.0.23 with new encryption mechanism
- **To be communicated separately**: Discontinuation date for existing NEAT Adapter version 1.0.20
- **To be communicated separately**: Discontinuation date for existing encryption mechanism for NNF users

## Impact Assessment

**Operational Impact:**
- All members trading in Commodity Derivatives segment must upgrade their systems
- Testing and migration required during coexistence phase
- Potential trading disruption if members fail to migrate before discontinuation dates
- IT teams need to reconfigure network parameters and update applications

**Technical Impact:**
- Members using proprietary systems must implement AES-256 GCM encryption
- Integration of immediate order acknowledgement logic required
- Network infrastructure changes (IP, port configurations)
- NEAT Adapter users must upgrade software version

**Security Benefits:**
- Enhanced security posture with stronger encryption (AES-256 GCM)
- Additional authentication layer for interactive messages
- TLS 1.3 protocol implementation
- Improved order confirmation with immediate acknowledgement

**Business Continuity:**
- Coexistence phase minimizes disruption risk
- Members have time to test and validate new encryption before mandatory migration
- Separate communication planned for final discontinuation dates ensures adequate preparation time