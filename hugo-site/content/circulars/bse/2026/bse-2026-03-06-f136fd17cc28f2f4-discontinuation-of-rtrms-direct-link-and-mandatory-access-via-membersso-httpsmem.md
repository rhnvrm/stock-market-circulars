---
category: market-operations
circular_id: f136fd17cc28f2f4
date: '2026-03-06'
description: BSE has discontinued the RTRMS direct link and mandated access through
  the new MemberSSO (Cymmetri) portal. This circular provides the user manual for
  brokers, banks, and mutual funds to onboard and use the new single sign-on system.
draft: false
guid: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={99FE9356-0F78-4A69-8179-737B910B48E8}&noticeno=20260306-18&dt=03/06/2026&icount=18&totcount=37&flag=0
impact: medium
impact_ranking: medium
importance_ranking: medium
justification: Operational change affecting all BSE members (brokers, banks, mutual
  funds) requiring migration to new SSO portal; no direct market or trading impact
  but mandatory compliance with new access procedures.
pdf_url: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?id=20260306-18&attachedId=09d61040-4bcc-4051-8d8c-2efffc39e76e
processing:
  attempts: 1
  content_hash: 2a6262a760b81152
  processed_at: '2026-03-06T15:52:38.076398'
  processor_version: '2.0'
  stage: completed
  status: published
published_date: '2026-03-06T13:01:05+00:00'
rss_url: https://www.bseindia.com/markets/MarketInfo/DispNoticesNCirculars.aspx?Noticeid={99FE9356-0F78-4A69-8179-737B910B48E8}&noticeno=20260306-18&dt=03/06/2026&icount=18&totcount=37&flag=0
severity: medium
source: bse
stocks: []
tags:
- member-sso
- rtrms
- authentication
- cymmetri
- broker-operations
- system-update
- access-management
title: Discontinuation of RTRMS Direct Link and Mandatory Access via MemberSSO Portal
  - User Manual
---

## Summary

BSE has discontinued the direct link for RTRMS and now mandates that all members (brokers, banks, and mutual funds) access BSE applications exclusively through the new Member Single Sign-On (SSO) portal powered by Cymmetri, available at https://membersso.bseindia.com/. This circular serves as the official user manual for onboarding and operating within the new portal.

## Key Points

- The new MemberSSO replaces the old Member SSO with an upgraded interface and enhanced features.
- New features include: redesigned UI, self-service password reset, multiple authentication modes, and self-unlock capability.
- Three modes of multi-factor authentication (MFA) are supported: Cymmetri Authenticator app, SMS OTP, and Secret Questions.
- Each member has one Member ID but can create multiple sub-users from the main/admin account.
- Sub-users can request access to specific applications with defined access periods (start/end date or lifetime).
- Access requests by sub-users require approval from the Main Member before access is granted.
- Accounts are locked after 3 consecutive incorrect password attempts.

## Regulatory Changes

- RTRMS direct link has been discontinued; all RTRMS and related application access must now go through the MemberSSO portal.
- Mandatory migration to the Cymmetri-based SSO for all BSE members.

## Compliance Requirements

- All brokers, banks, and mutual funds must log in to BSE applications via https://membersso.bseindia.com/.
- Members must set up at least one MFA method (Cymmetri Authenticator app, SMS, or Secret Questions).
- When creating sub-users, the UserType field must be set to `Sub_User`; incorrect UserType selection will prevent sub-user creation.
- Sub-users must request application access through the portal and obtain Main Member approval.
- Members should download the **Cymmetri Verify** app from Google Play Store or Apple App Store if using the Cymmetri Authenticator MFA option.

## Important Dates

- Effective immediately as of circular date (2026-03-06); direct RTRMS link has already been discontinued.

## Impact Assessment

This is an operational change affecting all BSE member firms. The transition to a centralized SSO portal improves security through mandatory MFA and self-service account management. Members who have not yet migrated will lose access to RTRMS and other BSE applications until they complete onboarding on the new Cymmetri portal. IT and compliance teams at brokerages, banks, and mutual funds should ensure all users are onboarded promptly to avoid disruption to trading and back-office operations.