---
category: trading
circular_id: 222460d8f0c4810b
date: '2026-01-09'
description: NSE introduces enhanced Order & Trade Drop Copy facility in Capital Market
  segment, allowing members to receive real-time order and trade information with
  improved reliability and customization options.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMTR72201.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Important technical infrastructure upgrade affecting all trading members
  using drop copy facility. Requires migration but provides transition period. Impacts
  operational systems but not immediate market operations.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMTR72201.pdf
processing:
  attempts: 1
  content_hash: 2239c3bad7d588be
  processed_at: '2026-01-09T09:29:56.491817'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-01-09T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMTR72201.pdf
severity: medium
source: nse
stocks: []
tags:
- drop-copy
- trading-infrastructure
- capital-market
- order-management
- trade-data
- technical-upgrade
- tls-security
- gateway-router
title: Introduction of New Order & Trade Drop Copy Facility in CM Segment
---

## Summary

NSE is introducing a new Order & Trade Drop Copy facility in the Capital Market segment, replacing the existing Trade Drop Copy facility. The new system allows members to receive either trade information only or both order and trade information on a real-time basis. The facility will be available in mock session on January 10, 2026, and go live from January 12, 2026. Both old and new facilities will run in parallel during a transition period before the existing Trade Drop Copy is discontinued.

## Key Points

- New facility offers option to download trade information only or both order and trade information in real-time
- Connection parameters: IP 172.19.12.84, Port 9612 (both order & trade) or 9614 (trade only) for Primary BKC/DR site
- Mock session on January 10, 2026; live implementation from January 12, 2026
- Transition period with parallel operation of old and new facilities before old system discontinuation
- Uses TLS 1.3 security protocol for enhanced security
- Members can use existing trading user credentials for access
- Protocol Version 3.0 documentation available on NSE website

## Technical Requirements

### Connection Details
- **Segment:** Capital Market (CM)
- **IP Address:** 172.19.12.84
- **Ports:** 
  - 9612: Both Order & Trade
  - 9614: Trade Only

### Security Requirements
- TLS 1.3 security protocol mandatory for Gateway Router connection
- CA certificate required for validation of Gateway Router server certificate
- Certificate available for download from January 09, 2026 at 19:00 hours onwards
- Certificate validity: Up to March 31, 2027
- Download path: /common/Dropcopy_CA_Certificate (Extranet)
- New CA certificates will be provided one month before expiry

### Authentication
- Members can use existing trading user ID and password credentials
- No new credential creation required

## Compliance Requirements

- All existing Trade Drop Copy users must migrate to the new Order & Trade Drop Copy facility
- Members must download and configure CA certificate for TLS 1.3 connection
- Members should review Protocol Version 3.0 documentation available at: https://www.nseindia.com/trade/platform-services-neat-trading-system-protocols
- Members need to ensure their systems support TLS 1.3 security protocol
- Testing in mock session on January 10, 2026 recommended before live migration

## Important Dates

- **January 09, 2026, 19:00 hours:** CA certificate available for download
- **January 10, 2026:** Mock session for new facility
- **January 12, 2026:** New Order & Trade Drop Copy facility goes live
- **TBD:** Discontinuation date for existing Trade Drop Copy facility (to be announced via separate circular)
- **March 31, 2027:** Current CA certificate validity expires

## Impact Assessment

### Operational Impact
- **Medium Impact:** Requires technical migration by all members currently using Trade Drop Copy facility
- Members need to update connectivity parameters and implement TLS 1.3 security
- Parallel operation period provides buffer for smooth transition
- Enhanced facility provides greater flexibility with option to receive order information in addition to trades

### Technical Impact
- Implementation of TLS 1.3 encryption enhances security of data transmission
- Real-time order and trade data availability improves operational efficiency
- Members gain better customization options for data requirements
- May require system upgrades for members not currently supporting TLS 1.3

### Market Impact
- No immediate market disruption expected due to parallel operation period
- Improved reliability and enriched trading experience for members
- Better alignment with modern security standards

## Additional Information

**Support Contact:**
- Toll Free: 1800-266-0050 (Option 1)
- Email: msm@nse.co.in

**Reference Circular:** NSE/MSD/67674 dated April 24, 2025 (details continue to apply until further notice)

**Issued by:** Khushal Shah, Associate Vice President, NSE