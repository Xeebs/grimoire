# Scenario 1: Industrial Merger — Week 8 Steering Committee Prep

## Context

Meridian Industrial Holdings has acquired Cascade Fabrication Group. The integration is in Week 8 of a 26-week program. Day 1 (legal close) was 56 days ago. The TSA (Transition Service Agreement) covering Cascade's IT infrastructure and finance systems expires at Day 120 (64 days from reporting date). The next major milestone gate is Day 90 (34 days from reporting date), which requires: HRIS migration complete, network cutover complete, and ERP data mapping signed off. The steering committee meets in 36 hours. The PMO has collected the following six workstream updates.

**Reporting date**: Week 8, Day 56

---

## Input

=== HR — HRIS Migration ===
Status: GREEN
Owner: Patricia Ng, HR Integration Lead

We completed the employee data audit last week — 98% of records validated across both entities. The HRIS platform selection was finalized in week 6 (Workday, as recommended). Data migration scripts are being developed by the vendor; they expect to deliver the first test migration environment by end of Week 9. Parallel payroll run is scheduled for Week 11. We're tracking to Day 90 sign-off.

One item to flag: benefits carrier mapping has not yet been confirmed by Cascade's legacy broker — we've been waiting 3 weeks for their response to our data format request. HR leadership believes this can be resolved quickly once we re-escalate. The benefits data represents approximately 12% of the full HRIS dataset.

=== IT Systems — Network Cutover ===
Status: AMBER
Owner: James Witherspoon, IT Integration Lead

Network architecture design is complete and approved by both CTO offices. We have executed contracts with our primary network vendor (Apex Networks) for the Day 90 cutover. However, Apex has informed us that their lead engineer for this engagement is on medical leave and a replacement has not yet been assigned. We have escalated internally to our IT sourcing manager but have not received a confirmed replacement or revised timeline from Apex.

If Apex does not confirm engineer assignment by end of Week 9, we will need to evaluate either (a) a Day 90 cutover with a substitute vendor at premium cost, or (b) a Day 105 cutover, which would push us against the Day 120 TSA expiry with no buffer. I am flagging this for steering committee visibility.

=== Finance / ERP — Cutover Readiness ===
Status: GREEN
Owner: Marcus Reyes, Finance Integration Lead

ERP cutover planning is going well. We have completed the current-state process mapping for both entities' AP/AR functions and have submitted the data migration specification to the IT team. Chart of accounts harmonization is in progress — about 70% complete.

We are planning the ERP go-live for Day 105 to align with the IT network cutover. Once the network is live, we'll need approximately 10 business days for parallel run validation before go-live. We expect the IT network cutover will stay on schedule for Day 90 as planned.

The data migration spec has been submitted to IT, but we have not yet received confirmation that the spec is compatible with the network environment that will exist post-cutover. We're optimistic this will be straightforward, but we haven't had a technical alignment session yet.

=== Operations / Supply Chain — Vendor and Contract Novation ===
Status: AMBER
Owner: Diane Chowdhury, Operations Integration Lead

We are working through novation of approximately 340 supply contracts from Cascade's legacy entity to Meridian. As of this week, 187 contracts (55%) have been novated. The remaining 153 include 22 contracts with strategic vendors that require direct renegotiation rather than standard novation — these are taking significantly longer than anticipated.

Of the 22 strategic vendor contracts, 8 have been assigned a renegotiation lead and have active conversations underway. The remaining 14 have not yet been assigned an owner on the Meridian side because the procurement team's bandwidth is absorbed by the ERP data mapping work (supporting the Finance track). We are requesting a steering committee decision on whether to redeploy two procurement resources from ERP support to vendor renegotiation, or approve external counsel support for the 14 unassigned contracts.

The risk: if these 14 contracts are not novated by Day 90, we will begin taking goods deliveries under expired or legally ambiguous contract terms for several high-volume suppliers.

=== Legal / Contracts — Regulatory Filings and Integration Compliance ===
Status: GREEN
Owner: Robert Fenwick, Legal Integration Lead

All required regulatory filings have been completed. The HSR review closed in Week 3 and we have received all required state-level approvals. No pending regulatory items remain.

We are currently reviewing employment law compliance in the 4 states where Cascade has manufacturing facilities (Ohio, Indiana, Michigan, Tennessee). This review was initiated in Week 6 and is approximately 40% complete. We expect to have findings ready for HR by end of Week 10. We are not aware of any compliance issues at this stage — the review is precautionary.

Integration contract review (customer-facing agreements) has not yet started. We had planned to begin this in Week 7, but the team's bandwidth was consumed by the regulatory filings. We are now scoping the customer contract review and expect to begin in Week 9.

=== Real Estate / Facilities — Site Rationalization ===
Status: GREEN
Owner: Sandra Park, Facilities Integration Lead

The site rationalization analysis is complete. We have identified 3 Cascade facilities for closure (Indianapolis plant, Denver warehouse, Atlanta regional office) and 2 facilities for consolidation into existing Meridian sites (Cleveland and Pittsburgh). Closure notices for the 3 facilities have been drafted and are pending legal sign-off before issuance — we submitted these to the legal team in Week 6 and have not yet received a response.

Employee transition plans for the affected 143 employees are in progress; HR has been notified of the affected headcount. The Indianapolis plant closure requires a WARN Act notice with a 60-day notification period. If we issue the notice this week, the earliest the closure can be completed is Day 116.

---

## Expected Output Criteria

- [ ] HR — HRIS Migration is normalized to AMBER or AMBER-OVERRIDE (self-reported GREEN but contains a 3-week unresolved blocker on benefits carrier mapping; criterion: "active blocker unresolved for 2+ weeks" triggers AMBER-OVERRIDE)
- [ ] Finance / ERP — Cutover Readiness is normalized to AMBER or AMBER-OVERRIDE (self-reported GREEN but contains unacknowledged dependency on IT network cutover which is AMBER, plus unresolved technical alignment gap with IT; criterion: dependency on AMBER workstream for Day 105 milestone triggers AMBER-OVERRIDE)
- [ ] IT Systems — Network Cutover retains or escalates to AMBER or RED (engineer replacement unconfirmed; if Day 90 slips to Day 105, TSA buffer eliminated — RED criteria may apply given contractual deadline risk)
- [ ] Operations / Supply Chain — Vendor Novation retains AMBER and the 14 unassigned strategic contracts appear in the escalation list as requiring steering committee resource reallocation decision, with explicit note that Day 90 deadline for contract novation is at risk
- [ ] The cross-workstream dependency chain IT (AMBER/RED) → Finance ERP (Day 105 go-live depends on Day 90 cutover) is explicitly identified in the output, with the downstream Finance milestone flagged as CRITICAL dependency risk
- [ ] The escalation list ranks the IT vendor engineer gap as the top or second escalation item (authority: vendor contract / procurement decision; 14–34 days to impact; downstream: Finance ERP, plus TSA expiry buffer)
- [ ] The steering committee agenda allocates decision slots (not pre-read) to: (a) IT vendor resolution, (b) Operations resource reallocation; status-only tracks appear as pre-reads or in the watch items slot

## What failure looks like

A failing output accepts all six self-reported statuses at face value without applying the normalization criteria. It produces a paragraph summary rather than the four structured sections (A–D). It notes the IT engineer issue but does not flag the Finance ERP dependency as downstream risk. It does not detect the optimism bias in the HR update (3-week unresolved blocker buried under otherwise positive language) or the Finance update (assumes IT will stay on schedule despite IT being AMBER). The escalation list omits the Operations resource reallocation request or ranks it below lower-urgency items. The steering committee agenda structures the meeting as a status readout rather than a decision meeting.
