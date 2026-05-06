---
category: market-operations
circular_id: 6d01d91ae7b9b72f
date: '2026-05-06'
description: NSE updates connection parameters for the new Order & Trade Drop Copy
  facility in the Capital Market segment, with updated gateway IPs effective May 11,
  2026 and mock testing on May 09, 2026.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMTR74087.pdf
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Technical update affecting member connectivity infrastructure for drop
  copy facility; operationally significant for members using the CM segment drop copy
  API but does not affect trading rules or listed securities.
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMTR74087.pdf
processing:
  attempts: 1
  content_hash: 0041ea27c62e93df
  processed_at: '2026-05-06T14:19:34.478353'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-05-06T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMTR74087.pdf
severity: medium
source: nse
stocks: []
tags:
- drop-copy
- capital-market
- trading-technology
- api
- gateway
- connectivity
- cm-segment
- order-management
- trade-data
title: New Order & Trade Drop Copy Facility in CM Segment - Updated Gateway Parameters
---

## Summary

NSE has issued a partial modification to earlier circulars (NSE/CMTR/72201 dated January 09, 2026 and NSE/MSD/73993 dated April 30, 2026) regarding the New Order & Trade Drop Copy facility in the Capital Market (CM) segment. The update provides revised connection parameters for the Drop Copy Gateway Router under API version 3.0, which has been live since January 12, 2026.

## Key Points

- This circular partially modifies NSE/CMTR/72201 (January 09, 2026) and NSE/MSD/73993 (April 30, 2026)
- The drop copy facility has been live since January 12, 2026
- Under API version 3.0, members must connect to the Drop Copy Gateway Router at login, which assigns a specific Drop Copy Gateway
- Members must then initiate connection with the assigned drop copy gateway router to receive required data
- Updated connection parameters are provided in Annexure 1
- All other details from previous circulars remain unchanged

## Regulatory Changes

No regulatory rule changes. This is a technical infrastructure update modifying the connection parameters for the existing Drop Copy Gateway facility in the Capital Market segment.

## Compliance Requirements

- Members must refer to Annexure 1 for updated connection parameters
- Members must complete necessary system setup at their end before May 11, 2026
- Updated Primary (BKC)/DR site parameters:
  - Segment: Capital Market (CM)
  - IP Address: 172.19.12.84
  - Port 9612: Both Order & Trade information
  - Port 9614: Trade information only
- Gateway IP subnet ranges:
  - Network: 172.19.12.0, Mask: 255.255.255.0, Port range: 8100–8153

## Important Dates

- January 12, 2026: Drop copy facility went live
- May 09, 2026: Updated parameters available for testing in scheduled mock session
- May 11, 2026: Updated parameters effective in LIVE environment

## Impact Assessment

This update affects NSE member firms using the Order & Trade Drop Copy facility in the Capital Market segment. Members relying on drop copy data for risk management, surveillance, or back-office reconciliation must update their system configurations to use the new gateway IP and port parameters before May 11, 2026. Failure to update may result in connectivity issues or loss of drop copy data feed. The mock testing window on May 09, 2026 provides an opportunity to validate system changes before the live cutover.