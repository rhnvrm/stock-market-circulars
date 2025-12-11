---
category: trading
circular_id: 5f7a789ac8213380
date: '2025-11-20'
description: NSE updates block trading parameters with minimum order size increased
  to Rs. 25 Crores and price range expanded to ±3%, effective December 08, 2025.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/CMTR71394.pdf
impact: high
impact_ranking: high
importance_ranking: high
justification: Significant changes to block trading framework affecting minimum order
  size (2.5x increase) and price range flexibility, impacting institutional and large-value
  traders
pdf_url: https://nsearchives.nseindia.com/content/circulars/CMTR71394.pdf
processing:
  attempts: 1
  content_hash: 103282c636ba00ce
  processed_at: '2025-11-20T15:50:08.876630'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-11-20T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/CMTR71394.pdf
severity: high
source: nse
stocks: []
tags:
- block-trading
- capital-market
- order-size
- price-range
- sebi-order
- trading-operations
- trading-window
title: 'Block Trading Session - Update: Revised Order Size and Price Range'
---

## Summary

NSE has revised the block trading session parameters following SEBI circular SEBI/HO/MRD/POD-III/CIR/P/2025/134 dated October 08, 2025. The changes include a substantial increase in minimum order size from Rs. 10 Crores to Rs. 25 Crores and expansion of price range from ±1% to ±3% of reference price. These modifications will be effective from December 08, 2025.

## Key Points

- Minimum order size increased from Rs. 10 Crores to Rs. 25 Crores (150% increase)
- Price range expanded from ±1% to ±3% of applicable reference price
- Price range subject to surveillance measures and applicable price bands in normal market
- Price range cannot exceed the day's applicable price range for the security
- For securities with 2% day price band, block deal range remains at ±2% (not increased to ±3%)
- For T0 parent series with dynamic ±1% band, TL series block deal range remains at ±1%
- Changes applicable to Capital Market Segment block trading window

## Regulatory Changes

### Order Size Parameter
**Previous:** Minimum order size of Rs. 10 Crores
**Revised:** Minimum order size of Rs. 25 Crores

### Price Range Parameter
**Previous:** ±1% of applicable reference price
**Revised:** ±3% of applicable reference price, with important caveats:
- Subject to surveillance measures applicable in normal market
- Cannot exceed the day's applicable price range
- If normal market price band is 2%, block deal range remains at ±2%
- For T0 parent series with ±1% dynamic band, TL series block deal range remains at ±1%

These changes are in partial modification to Chapter 1.7 Block Trading Session in Capital Market Consolidated Circular number 67774 dated April 30, 2025.

## Compliance Requirements

### For All NSE Members:
- Update trading systems to accommodate new parameters before December 08, 2025
- Load updated security files in trading application before effective date
- Download security.gz/nnf_security.gz/NSE_CM_security_ddmmyyyy.csv.gz from common/NTNEAT directory on Extranet server
- Alternatively, download CM-MII-Security File (.gz) from NSE website at https://www.nseindia.com/all-reports
- Ensure block deal orders meet the new Rs. 25 Crores minimum threshold
- Configure systems to apply appropriate price range limits based on security-specific bands
- Participate in mock trading session to test updated parameters

### Testing Requirements:
- Mock trading session scheduled for December 06, 2025
- Members should test the updated parameters during this session

## Important Dates

- **November 20, 2025:** Circular issued (Ref. No: 160/2025)
- **December 06, 2025:** Mock trading session for testing updated parameters
- **December 08, 2025:** Changes go live and become effective in production environment

## Impact Assessment

### Market Impact:
**High Impact on Block Trading Activity:**
- 150% increase in minimum order size may reduce the number of eligible block trades
- Higher threshold may consolidate block trading to larger institutional participants
- Smaller institutional trades (Rs. 10-25 Crores) will need to use regular market windows

### Operational Impact:
**Moderate to High:**
- Trading members must update systems and security files
- Price range expansion from ±1% to ±3% provides more flexibility for price discovery
- Complex price band logic requires careful system configuration (security-specific bands)
- Systems must handle conditional price ranges based on normal market bands

### Liquidity Impact:
**Mixed:**
- Wider price range (±3%) may improve execution probability for large orders
- Higher minimum size may reduce overall block trading volume
- May push some trades back to normal market hours

### Compliance Impact:
**Moderate:**
- Members need to ensure proper testing during mock session
- Security file updates are mandatory for smooth operations
- Failure to update could result in order rejections

### Strategic Considerations:
- Institutional investors planning block trades between Rs. 10-25 Crores need alternative execution strategies
- Larger price bands may reduce market impact for trades above Rs. 25 Crores
- Trading desks should review block trading strategies and thresholds