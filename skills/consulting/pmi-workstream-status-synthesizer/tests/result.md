# Test Results: pmi-workstream-status-synthesizer

**Date**: 2026-06-04
**Verdict**: PASS

## Scenario 1: Industrial Merger — Week 8 Steering Committee Prep

- [✓] HR — HRIS Migration normalized to AMBER-OVERRIDE — The benefits carrier mapping blocker is explicitly described as 3 weeks unresolved ("waiting 3 weeks for their response"), meeting the AMBER-OVERRIDE trigger for unresolved blockers described as "awaiting" and meeting the RED criterion for 2+ week unresolved blockers. The skill's Step 2 AMBER-OVERRIDE rules require recording the specific triggering language, which is present verbatim in the update.
- [✓] Finance / ERP normalized to AMBER-OVERRIDE — Finance self-reports GREEN while (a) depending on IT Network Cutover (AMBER) for its Day 105 go-live milestone, (b) using the exact AMBER-OVERRIDE trigger phrase "we expect the IT network cutover will stay on schedule," and (c) acknowledging no technical alignment session has occurred. The skill's dependency-on-AMBER-workstream trigger and "we expect" language trigger both apply.
- [✓] IT Systems retains or escalates to AMBER or RED — IT self-reports AMBER; the Apex engineer issue is an active unresolved blocker and the TSA Day 120 expiry creates a hard contractual deadline risk if Day 90 slips to Day 105, satisfying the RED criterion "TSA expiry or hard contractual deadline is at risk." The skill permits AMBER or RED; either satisfies the criterion.
- [✓] Operations retains AMBER, 14 unassigned contracts appear in escalation list with Day 90 risk — Operations explicitly requests a steering committee resource reallocation decision. The skill's Step 4 escalation rules rank cross-workstream resource reallocation as priority #2, and the Day 90 risk for unnovated contracts is stated in the input. The skill's instructions require this item to appear in the escalation list.
- [✓] IT → Finance ERP dependency chain identified as CRITICAL — Finance's Day 105 ERP go-live depends on IT's Day 90 cutover, placing the impacted milestone 34 days from reporting date (within the 4-week CRITICAL window). The skill's Step 3 requires explicitly classifying this as CRITICAL and flagging Finance as a downstream workstream at risk from IT's AMBER/RED status.
- [✓] IT vendor engineer gap ranked first or second in escalation list — The skill's primary sort places "steering committee/C-suite authority required" first. IT's vendor engineer issue requires procurement/contract authority with TSA deadline downstream consequences and affects Finance ERP (downstream blast radius). Operations also requires steering committee resource authority; the secondary sort (days to impact: IT at 34 days for Day 90, Operations also at Day 90) and tertiary sort (IT affects Finance ERP plus TSA expiry vs. Operations affecting its own track) support IT ranking #1.
- [✓] Steering committee agenda allocates decision slots (not pre-reads) to IT vendor resolution and Operations resource reallocation — The skill's Section C instructions explicitly state "Decision items should occupy the majority of time. Status-only items should be pre-reads, not agenda items." Both IT and Operations require decisions with named authority; the skill's output structure enforces this separation.

**Scenario 1 result**: PASS

## Scenario 2: Professional Services Acquisition — Week 14 Steering Committee Prep

- [✓] Client Transition normalized to AMBER-OVERRIDE — Self-reported GREEN with Day 100 milestone in 2 days and only 60% of notifications complete. AMBER-OVERRIDE triggers present verbatim: "we expect to complete the remaining 44 this week" and "depends on resolving the partner engagement issue." Four contracts also blocked on Legal without clearance received. All three AMBER-OVERRIDE triggers apply simultaneously.
- [✓] Finance normalized to AMBER-OVERRIDE with triggering language cited — Self-reported GREEN with a missed Week 12 deliverable (intercompany reconciliation) having no confirmed new timeline, and verbatim triggers: "hoping to complete by Week 16" and "have not yet confirmed a timeline." Active blocker on 4 client contracts waiting on Legal. The skill requires recording exact triggering language for each AMBER-OVERRIDE.
- [✓] Legal → Client Transition AND Legal → Finance dependency chain explicitly identified — Both Client Transition and Finance explicitly state they are waiting on Legal's 4 contract novations. The skill's Step 3 requires listing all named dependencies in both directions and flagging each downstream workstream at risk from an upstream RED/AMBER status. Legal is AMBER; both downstream workstreams declared the dependency in their own updates.
- [✓] Legal insurance gap is top-ranked escalation with authority identified as emergency executive/ad hoc committee decision — The Day 130 deadline, the risk committee's next scheduled meeting at Day 145 (15 days past deadline), and the compliance gap affecting all Thornfield client engagements satisfy the skill's primary sort criterion "requires steering committee decision or C-suite/board authority." The ad hoc risk committee convening requires executive authority not yet obtained, which also satisfies the RED criterion "Steering committee decision or executive authority is required and has not been obtained." Maximum downstream blast radius (all Thornfield engagements) and 32 days to impact place this unambiguously at #1.
- [✓] Talent/HR HRIS milestone slip escalated with downstream impact noted — Day 120 milestone projected to slip to Day 136 at current pace (stated explicitly in the update). The skill's escalation criteria require surfacing at-risk milestones; the narrative explicitly connects the slip to employment counsel bandwidth (litigation support), providing the resource reallocation angle. Downstream impacts (payroll processing, employment record finalization for HRIS cutover) are inferable from the input and must be noted per the skill's instructions.
- [✓] Steering committee agenda allocates two distinct decision slots (Legal insurance, Talent/HR resource); Day 100 notification appears as watch/update item not a pre-read — Legal insurance requires an ad hoc committee authority decision; Talent/HR requires employment counsel reallocation (resource decision). The skill requires decision items to lead the agenda. Day 100 is 2 days away — the skill's instructions distinguish decision items from pre-reads; a missed imminent deadline is a time-sensitive update requiring agenda time, not a pre-read.

**Scenario 2 result**: PASS

## README Portability

- [✓] Self-contained without Claude Code — The README includes the complete prompt template with all RAG criteria definitions, output format requirements (Sections A–D with table structures and ranking logic), and usage tips. A practitioner can paste this into any AI tool without Claude Code context.
- [✓] Placeholders clearly marked — All placeholders use `{ALL_CAPS_DESCRIPTIVE_NAME}` format: `{INTEGRATION_NAME}`, `{ACQUIRER}`, `{TARGET}`, `{WEEK_NUMBER}`, `{REPORTING_DATE}`, `{DAY_1_DATE}`, `{TSA_EXPIRY_DATE_AND_OTHER_CONTRACTUAL_DEADLINES}`, `{PASTE_ALL_WORKSTREAM_STATUS_UPDATES_HERE}`. No ambiguity about what to substitute.
- [✓] Example output is representative — The example demonstrates IT/Finance dependency detection with an AMBER-OVERRIDE, an escalation item with all required fields, a time-allocated agenda distinguishing decision items from pre-reads, and a two-sentence-plus-NOTE narrative. This covers the skill's core differentiated functionality accurately.

## Overall Assessment

The skill's instruction set is precise enough to produce correct outputs on both scenarios without ambiguity: the AMBER-OVERRIDE criteria include verbatim trigger phrases that appear in both scenario inputs, the escalation ranking logic produces unambiguous ordering given the inputs, and the output format requirements (Sections A–D with specified table structures) leave no structural discretion. The README is fully portable and the example output is representative of the skill's most complex case (dependency detection + optimism bias override). No failures were identified across 13 criteria.

## Failure Notes (if applicable)

None.
