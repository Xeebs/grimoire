# Scenario 1: At-Risk Enterprise Account with Mixed Signals and Partial Value Story

## Context

The CSM is Priya Nair, a mid-market and enterprise CS lead at a B2B SaaS workflow automation company. Her account, Castellan Group (a regional insurance brokerage with 340 employees), has been a customer for 22 months on a $78,000 ACV contract covering 120 seats. The renewal date is September 30, 2026 — 108 days out. Priya is doing renewal triage after flagging the account on her weekly at-risk review. The account was in Good health status three months ago but slipped to Yellow in the CS platform after a support escalation in April. She has pulled the following data from three separate systems and is pasting it into the skill.

The account has mixed signals: feature adoption is shallow despite a healthy seat count, the champion is engaged but the economic buyer (CFO) has gone quiet, value documentation is incomplete, and no competitive signal has been identified. The renewal conversation has not been formally opened.

## Input

**Account**: Castellan Group
**ACV**: $78,000
**Renewal Date**: 2026-09-30
**Days Until Renewal**: 108

**Adoption Depth**
- DAU/MAU ratio: 31% (average over past 60 days; peak was 44% in January during initial rollout)
- License utilization: 74 of 120 seats active in past 30 days (62%)
- Key features active: Workflow Builder (core module, active since onboarding); Document Routing (activated Month 4, used by 3 of 74 active users); Approval Chains (never activated — was listed as a primary use case in the sales discovery call); Integration Hub (activated Month 8, used by 1 admin only)
- Days since last active user login: 2 days (admin login; 11 days since a non-admin user last logged in)

**Relationship Health**
- Champion: Marcus Trent (Director of Operations), last contacted 18 days ago via Zoom; has been responsive and expressed intent to renew in conversation but said "the CFO will need to approve anything above $60K"
- Executive sponsor: Janet Yoo (CFO), last contacted 71 days ago via email (Priya sent a QBR summary; no reply received)
- Open escalation tickets: 1 open ticket (#ESC-2241, opened April 14, 2026 — integration failure causing document routing errors for finance team; partial workaround applied, root cause under investigation by engineering; ticket age: 51 days)
- Support ticket trend (past 90 days): Increasing — 3 tickets in Q1, 9 tickets in Q2 (3 routine, 5 moderate, 1 escalation); spike driven by integration issues

**Value Realization**
- ROI documentation: Partial — time savings for the operations team have been informally quantified by Marcus ($120K annual equivalent based on manual process hours eliminated) but no formal ROI document exists and the CFO has not seen the numbers
- Last QBR/EBR date: December 10, 2025 (9 months ago); a Q1 2026 QBR was scheduled but cancelled by Marcus due to the April escalation
- Business outcomes delivered vs. promised: At sale, Castellan was promised three outcomes — (1) eliminate manual document routing (partially delivered: routing is automated for ops team, not finance team due to integration bug); (2) reduce approval cycle times by 40% (not measured); (3) enable multi-department workflow standardization (not started — Approval Chains never activated)
- Expansion conversation status: Never held; Marcus mentioned in the last call that two additional departments (HR and Compliance) have asked him about the tool, but no formal expansion conversation has been initiated

**Competitive Exposure**
- Renewal conversation initiated: No; renewal has not been formally opened
- Competitor evaluation signals: None identified; no competitor mentioned in any call notes or emails
- Budget constraint signals: Marcus mentioned in the May 15 call that "Janet has been tightening the budget across the board since Q1 — everything above $60K needs her direct sign-off this year, which wasn't the case last year"
- Stakeholder changes in past 90 days: 0 — Marcus and Janet are both still in role; no org change noted

**Additional context**: The April escalation (#ESC-2241) was caused by a breaking change in Castellan's internal ERP system upgrade that broke the Integration Hub connector. Engineering has a fix in the next release (ETA: 3 weeks). The integration issue is the direct cause of the finance team not adopting the Document Routing feature. Marcus is aware of the ETA and says he has "been managing expectations internally" but is worried about bringing the CFO into a conversation while the bug is still open.

## Expected Output Criteria

- [ ] Adoption Depth scored Medium Risk — DAU/MAU of 31% falls in the 20–50% band; license utilization of 62% falls in the 40–65% band; Approval Chains (a promised use case) is never activated; these signals collectively justify Medium Risk, not Low Risk
- [ ] Relationship Health scored Medium Risk — champion (Marcus) was contacted 18 days ago (within the 21-day Low threshold but barely), executive sponsor (Janet) last contacted 71 days ago (falls in the 45–90-day Medium band), 1 open escalation ticket; output must not score this High Risk (no criterion for High Risk is met: champion < 45 days, exec < 90 days, only 1 escalation, tickets trending upward but driven by a single integration issue)
- [ ] Support ticket trend noted as a contributing factor but output explains that the upward trend is tied to a single root cause (ESC-2241) rather than a systemic relationship breakdown
- [ ] Value Realization scored High Risk or Medium Risk — last QBR was 9 months ago (> 180 days = High Risk trigger), and two of three promised outcomes (approval cycle measurement, multi-department standardization) are undelivered; output must not score this Low Risk
- [ ] Competitive Exposure scored Medium Risk — renewal has not been initiated (Medium Risk trigger under the rule "renewal not initiated but no active competitor signal"); budget constraint signal (Janet's $60K sign-off requirement) is surfaced as a relevant contributing factor
- [ ] Tier classified as AT-RISK — QBR Acceleration or CRITICAL — Executive Save Play; the exact tier depends on how the model resolves Value Realization; if Value Realization is High Risk and ACV ($78K > $50K threshold), CRITICAL is correct; if Value Realization is scored Medium, AT-RISK (2+ Medium dimensions) is correct; either is acceptable if the reasoning matches the scoring
- [ ] Two to three interventions selected from the named playbook; must include QBR/EBR Acceleration (QBR is 9 months overdue, value realization is the primary risk) and Renewal Conversation Initiation (108 days out, not initiated) as logical choices
- [ ] Intervention selection explicitly addresses the ESC-2241 escalation ticket timing — the brief must not recommend scheduling the CFO executive reconnect or QBR before the bug fix ETA (3 weeks) without acknowledging the risk of conducting executive engagement while an escalation is open
- [ ] Talking points for Marcus reference specific data: the $120K informal ROI figure, the Approval Chains feature never being activated, the May 15 call note about Janet's $60K sign-off threshold, and the 3-week bug fix ETA
- [ ] Talking points for Janet (CFO) are distinct from Marcus talking points and address the CFO's budget approval lens, not operational metrics
- [ ] Output notes the expansion signal (HR and Compliance departments expressed interest) as context for the QBR agenda or renewal conversation — it should not be ignored even though the account is at-risk
- [ ] Data Gaps section identifies that the $120K ROI figure is informal/unvalidated and that approval cycle time improvement has never been measured — these are gaps that affect the strength of the value story

## What failure looks like

- Scoring all four dimensions as Medium Risk mechanically without engaging with the specific data (e.g., not distinguishing that the support ticket trend is driven by a single integration bug with a known ETA)
- Classifying the account as HEALTHY or WATCHLIST — the QBR is 9 months overdue and two of three promised outcomes are undelivered, which are not Low Risk signals
- Recommending an Adoption Acceleration Sprint as a primary intervention without noting that the feature adoption gap (Approval Chains never activated) is downstream of the unresolved integration issue, not a training or onboarding problem
- Producing talking points that do not reference specific data: generic phrases like "we want to make sure you're getting value" instead of anchoring to the $120K ROI estimate, the May 15 call, or the Approval Chains gap
- Recommending the executive CFO call be scheduled immediately without any acknowledgment that ESC-2241 is still open and that Marcus himself flagged this as a concern
- Ignoring the expansion signal entirely — the HR and Compliance interest should appear somewhere in the brief (in the QBR agenda recommendation, the renewal conversation framing, or as a talking point)
