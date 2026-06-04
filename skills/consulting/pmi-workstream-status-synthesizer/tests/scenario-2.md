# Scenario 2: Professional Services Acquisition — Week 14 Steering Committee Prep

## Context

Vantage Advisory Partners (acquirer) has acquired Thornfield Consulting Group (target), a 280-person management consulting firm. The acquisition closed 98 days ago. This is a talent-heavy integration: the primary risk is consultant attrition and client relationship disruption. The program is in Week 14 of a 20-week integration plan. Key hard deadlines: the Day 100 milestone (2 days from reporting date) requires completion of Thornfield's client transition notifications; the Day 120 milestone requires completion of all employment contract conversions and the new HRIS cutover. A regulatory compliance deadline requires Thornfield's legacy professional liability insurance to be novated or replaced by Day 130 — failure triggers a compliance gap on active client engagements.

The steering committee meets tomorrow. Five workstream updates have been received.

**Reporting date**: Week 14, Day 98

---

## Input

=== Talent / HR — Employment Contract Conversions and HRIS Cutover ===
Status: AMBER
Owner: Claire Beaumont, People Integration Lead

Employment contract conversions are progressing but behind plan. Of 280 Thornfield employees targeted for conversion to Vantage terms by Day 120, 194 (69%) have signed converted agreements. Of the remaining 86, 41 are in active negotiation (compensation alignment discussions) and 45 have not yet been engaged because their files are in a review queue with our employment counsel — the counsel team has been occupied with the Talent retention litigation response (see Legal/Compliance).

HRIS cutover from Thornfield's legacy BambooHR to Vantage's Workday platform requires all 280 employment records to be finalized before the migration can run. At current pace (approximately 12 contracts per week), the remaining 86 would complete around Day 126 — 6 days past the Day 120 milestone. The HRIS migration itself requires 10 days post-conversion completion, which would push cutover to approximately Day 136 — 16 days past the Day 120 milestone.

I am flagging this as AMBER rather than RED because we believe we can close the gap with additional resourcing — specifically, if employment counsel capacity is freed from the litigation response, we could accelerate conversion processing significantly.

=== Technology — Platform and Tooling Migration ===
Status: GREEN
Owner: David Okafor, Technology Integration Lead

Platform migration is on track. Thornfield's project management tools (Asana, Smartsheet) have been migrated to Vantage's standard stack (Microsoft 365, Dynamics). Email migration was completed in Week 12 with no data loss. Video conferencing consolidation (Zoom → Teams) completed in Week 13.

The remaining items are: (1) SharePoint permissions and folder structure for migrated Thornfield client files — this is 60% complete and being handled by our IT team in coordination with Client Transition; (2) billing system integration between Thornfield's legacy Sage system and Vantage's Dynamics ERP — we haven't started this yet, but it's scoped for Weeks 15–17 and we don't anticipate issues. The Sage system will remain active under a vendor license extension we obtained through Day 140.

Client-facing credentials (email signatures, client portal access) have all been updated. From a technology standpoint, the integration is substantially complete.

=== Client Transition — Relationship and Engagement Notifications ===
Status: GREEN
Owner: Priya Sundaram, Client Transition Lead

Client transition notifications are in progress and going smoothly. We have notified 68 of Thornfield's 112 active client accounts of the acquisition and relationship ownership. All 68 responded positively and confirmed continuation of engagements. Of the remaining 44, 31 are scheduled for notification calls this week.

The remaining 13 clients have not been scheduled — these are accounts where the original Thornfield relationship partner has not confirmed willingness to make the introduction call to Vantage leadership. We are working through this internally.

Day 100 milestone requires completion of all 112 client notifications. We are 60% complete with 2 days remaining. We expect to complete the remaining 44 this week, though the 13 unscheduled accounts depend on resolving the partner engagement issue.

Additionally, 4 client contracts are flagged by the Legal team as requiring novation approval before we can formally confirm engagement continuation — we have not received clearance from Legal on these, and two of those clients are among the 31 scheduled for notification this week.

=== Finance — Revenue Recognition and Billing Transition ===
Status: GREEN
Owner: Andrew Stiles, Finance Integration Lead

Billing transition is progressing well. Invoices for all Thornfield client engagements in Weeks 10–13 have been issued under the new Vantage billing structure. Revenue recognition for the acquisition period is being handled by our technical accounting team, and we do not anticipate any issues there.

One item: the intercompany billing reconciliation for Days 1–70 (the period between close and the billing system cutover) has not been completed. Our team flagged this as a Week 12 deliverable, but it was deprioritized when our finance analyst was seconded to support the HR employment contract review. We are hoping to complete this by Week 16, but have not yet confirmed a timeline with our analyst, who is still supporting HR.

The 4 client contracts flagged by Legal as requiring novation are relevant here — we cannot finalize billing terms or revenue recognition for those engagements until Legal provides clearance. We are waiting on Legal.

=== Legal / Compliance — Regulatory Filings and Contract Novation ===
Status: AMBER
Owner: Susan Park, Legal Integration Lead

Regulatory filings are complete. All professional licensing transfers for Thornfield's regulated practices (government advisory, healthcare consulting) have been filed — we are awaiting confirmation from two state licensing boards (estimated 3–4 weeks).

Professional liability insurance novation is the critical item. Thornfield's legacy policy must be replaced or formally novated to cover the combined entity by Day 130. We engaged our insurance broker in Week 10. The broker has submitted the application to three carriers; two have declined and one (Argonaut Specialty) has issued a preliminary quote that requires Vantage's risk committee approval. The risk committee meets quarterly — the next scheduled meeting is Day 145, which is 15 days after the Day 130 deadline.

We are working on requesting an ad hoc risk committee meeting but have not yet received a response from the committee chair. If we cannot get committee approval before Day 130, we will have a 15-day gap in professional liability coverage across all Thornfield client engagements. This is a material compliance issue.

The 4 client contract novations (flagged to Client Transition and Finance) are in our queue. They were deprioritized in Week 12 when the insurance issue escalated. We expect to complete them by end of Week 15 — approximately Day 107.

---

## Expected Output Criteria

- [ ] Client Transition is normalized to AMBER-OVERRIDE (self-reported GREEN but 13 of 112 notifications unscheduled with Day 100 milestone in 2 days, and 4 contracts awaiting Legal clearance that is described as outstanding — triggering language such as "we expect to complete" and "depends on resolving the partner engagement issue" should be cited)
- [ ] Finance — Revenue Recognition is normalized to AMBER-OVERRIDE (self-reported GREEN but contains a missed Week 12 deliverable on intercompany reconciliation with no confirmed new timeline, and an active blocker on 4 client contract novations waiting on Legal — triggering language such as "hoping to complete" and "have not yet confirmed a timeline" should be cited)
- [ ] The dependency chain Legal (AMBER) → Client Transition (blocked on 4 contract novations) AND Legal → Finance (blocked on same 4 contracts) is explicitly identified as a cross-workstream dependency, with both downstream workstreams flagged
- [ ] The Legal professional liability insurance gap (Day 130 deadline, risk committee meeting at Day 145, 15-day compliance gap) appears as the top-ranked escalation item, with authority identified as requiring an emergency/ad hoc board or executive committee decision to convene the risk committee before Day 130
- [ ] Talent / HR HRIS milestone slip (Day 120 → estimated Day 136) is escalated with downstream impact noted: HRIS cutover delay affects payroll processing and employment record finalization
- [ ] The steering committee agenda allocates at least two distinct decision slots: (a) Legal insurance escalation (risk committee convening authority), (b) Talent/HR resource reallocation (free employment counsel from litigation support to contract conversions); Day 100 client notification status appears as a watch item or time-sensitive update, not a pre-read given the imminent deadline

## What failure looks like

A failing output accepts Finance's GREEN and Client Transition's GREEN without applying the AMBER-OVERRIDE criteria to the missed deliverable and the "hoping to" language. It notes the Legal insurance issue but does not identify it as a compliance deadline breach risk requiring emergency escalation (instead treating it as a standard AMBER watch item). It fails to map the Legal delay as blocking both Client Transition (4 contracts) and Finance (4 contracts) simultaneously — missing the two-pronged downstream dependency. The steering committee agenda structures the meeting as a status tour across workstreams rather than centering on the two decisions that require steering committee authority. Section D narratives run longer than two sentences per workstream or blend into general analysis paragraphs.
