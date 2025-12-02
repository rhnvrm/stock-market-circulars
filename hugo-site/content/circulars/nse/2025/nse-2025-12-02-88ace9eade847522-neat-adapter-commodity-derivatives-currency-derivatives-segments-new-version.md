---
category: trading
circular_id: 88ace9eade847522
date: '2025-12-02'
description: NSE releases new version 1.0.23 of NEAT Adapter application for Commodity
  and Currency Derivatives segments with enhanced encryption mechanism and additional
  authentication, available from December 12, 2025.
draft: false
guid: https://nsearchives.nseindia.com/content/circulars/MSD71601.zip
impact: high
impact_ranking: high
importance_ranking: high
justification: Mandatory trading system upgrade affecting all members trading in commodity
  and currency derivatives segments with specific technical requirements and port
  changes.
pdf_url: https://nsearchives.nseindia.com/content/circulars/MSD71601.zip
processing:
  attempts: 1
  content_hash: 7f6ed7feb6d6f321
  processed_at: '2025-12-02T15:52:02.318896'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2025-12-02T00:00:00+05:30'
rss_url: https://nsearchives.nseindia.com/content/circulars/MSD71601.zip
severity: high
source: nse
stocks: []
tags:
- neat-adapter
- commodity-derivatives
- currency-derivatives
- trading-software
- encryption
- authentication
- technical-upgrade
title: NEAT Adapter - Commodity Derivatives & Currency Derivatives Segments - New
  Version 1.0.23
---

## Summary

NSE is releasing new version 1.0.23 of NEAT Adapter application for Commodity Derivatives (CO) and Currency Derivatives (CD) segments. The new version incorporates changes for new encryption mechanism with additional authentication as mentioned in previous circulars NSE/CD/70422 dated September 25, 2025 and NSE/COM/71599 dated December 02, 2025. Members must download and install the new version from the designated extranet paths starting December 12, 2025 at 20:00 hours.

## Key Points

- New NEAT Adapter version 1.0.23 released for both Windows and Linux operating systems
- Available for download from December 12, 2025, 20:00 hours onwards via Extranet
- Supports only 64-bit operating systems (32-bit not supported)
- New version uses designated port 10879 for CD segment and port 10859 for CO segment
- Multiple versions will coexist during transition period
- Windows version requires Windows 10 (64 bit) or higher
- Linux version requires RHEL 8.5 (64 bit) or higher

## Technical Specifications

**Windows Version:**
- Setup file: NA_1.0.23_Setup.exe and Register_Installer.bat
- Extranet path for CD: /cdsftp/cdscommon/NeatAdapter/Windows
- Extranet path for CO: /comtftp/comtcommon/NeatAdapter/Windows
- Minimum OS: Windows 10 (64 bit)

**Linux Version:**
- Setup files: NA_1.0.23_Setup.sh and NA_1.0.23_SetupFiles.zip with Register_Installer.sh
- Extranet path for CD: /cdsftp/cdscommon/NeatAdapter/Linux
- Extranet path for CO: /comtftp/comtcommon/NeatAdapter/Linux
- Minimum OS: RHEL 8.5 (64 bit)

## Port Configuration

**Currency Derivatives (CD):**
- Old version (1.0.20): Port 10877 (discontinuation date to be communicated separately)
- New version (1.0.23): Port 10879 (released w.e.f December 13, 2025 in mock)

**Commodity Derivatives (CO):**
- Old version (1.0.22): Port 10857 (released w.e.f October 04, 2025 in mock)
- New version (1.0.23): Port 10859

## Compliance Requirements

- All members trading in Commodity Derivatives and Currency Derivatives segments must download and install NEAT Adapter version 1.0.23
- Members must ensure their systems meet the 64-bit OS requirement
- Members must configure the new designated ports for respective segments
- For Commodity Derivatives segment, members must use new NEAT Adapter version along with designated port 10859 as specified in Exchange Circular No. NSE/COM/71599 dated December 02, 2025
- Refer to attached user manual for OS compatibility details, installation instructions, and network environment prerequisites

## Important Dates

- **December 12, 2025, 20:00 hours**: New NEAT Adapter version 1.0.23 available for download from Extranet
- **December 13, 2025**: Release date for new version in mock environment for CD segment
- **October 04, 2025**: Old version 1.0.22 for CO segment was released in mock
- **Discontinuation date for old versions**: To be communicated separately

## Impact Assessment

This is a critical technical upgrade affecting all members engaged in commodity and currency derivatives trading. The new encryption mechanism and additional authentication represent significant security enhancements. Members must allocate resources for:

1. **Infrastructure readiness**: Verify and upgrade OS to 64-bit if needed
2. **Network configuration**: Update port settings for CD (10879) and CO (10859) segments
3. **Testing**: Conduct thorough testing in mock environment before production deployment
4. **Training**: Ensure technical teams are familiar with new installation procedures
5. **Downtime planning**: Schedule installation during non-trading hours to minimize disruption

Failure to upgrade by the mandatory deadline could result in inability to trade in these segments. Members should contact NSE support (Toll Free: 1800 266 0050, Option 1 or msm@nse.co.in) for configuration assistance.

## Support Contact

- **Toll Free Number**: 1800-266-0050 (Option 1)
- **Email**: msm@nse.co.in
- **Issued by**: Khushal Shah, Associate Vice President, National Stock Exchange of India Limited