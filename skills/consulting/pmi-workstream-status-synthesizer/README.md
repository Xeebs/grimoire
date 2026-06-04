# PMI Workstream Status Synthesizer

**Industry**: Consulting
**Role**: PMO Consultant / Integration Manager
**Time saved**: 4–7 hours per weekly steering committee cycle

## What it does

Takes raw, inconsistently formatted status updates from post-merger integration workstream leads, normalizes each to a defensible RAG status using defined criteria, flags where self-reported GREEN status conflicts with described blockers (optimism bias), maps cross-workstream dependency risks, and produces a complete executive steering committee dashboard with escalation list and time-allocated meeting agenda.

## When to use it

Weekly, after collecting status updates from all workstream leads and before producing the executive steering committee deck — specifically when you need to reconcile 10–50 varied status inputs, decide which risks are real versus overstated or understated, and structure a decision-focused agenda rather than a status readout.

## Prompt template

```
You are a PMO advisor supporting a post-merger integration. I will give you status updates from workstream leads. Your job is to normalize, synthesize, and produce an executive steering committee dashboard.

## Integration context
Integration name: {INTEGRATION_NAME}
Acquirer / Target: {ACQUIRER} acquiring {TARGET}
Week number / Reporting date: {WEEK_NUMBER} — {REPORTING_DATE}
Day 1 date: {DAY_1_DATE}
Key hard deadlines: {TSA_EXPIRY_DATE_AND_OTHER_CONTRACTUAL_DEADLINES}

## Workstream updates

{PASTE_ALL_WORKSTREAM_STATUS_UPDATES_HERE}

---

Using the updates above, produce the following in order:

**A. RAG Summary Table**
Normalize each workstream to GREEN / AMBER / RED using these criteria:
- GREEN: No active unresolved blockers, next milestone on track, no pending decisions that could delay it this week, no dependency on a RED/AMBER workstream for near-term deliverables.
- AMBER: Active blocker being managed with a resolution owner and timeline, OR milestone at risk but recoverable, OR pending decision with named owner and due date.
- RED: Blocker unresolved for 2+ weeks, OR missed milestone, OR dependency confirmed blocked, OR steering committee authority required and not yet obtained, OR TSA/contractual deadline at risk.
- AMBER-OVERRIDE: Self-reported GREEN but the narrative contains unresolved blockers, incomplete due actions, quietly shifted milestone dates, or language like "awaiting," "pending," "hoping to confirm," or "expecting" on critical path items.

For each AMBER-OVERRIDE, record the self-reported status, the normalized status, the exact triggering language, and a one-sentence explanation.

Format as a table: Workstream | Track | Self-Reported | Normalized | Override? | Owner

**B. Escalation List** (ranked by priority)
Rank by: (1) authority level required — steering committee/C-suite first, then cross-workstream resource, then budget/contract, then timeline extension; (2) days until milestone impact; (3) number of downstream workstreams affected.

For each item:
- Issue headline
- Authority needed
- Milestone at risk and date
- Downstream workstreams affected
- Recommended decision owner
- Recommended action (one sentence)

**C. Steering Committee Agenda**
Propose a 60-minute time-allocated agenda. Decision items first. Status-only items as pre-reads, not agenda items.

Format as a table: Time | Agenda Item | Owner | Goal

**D. Workstream Status Narratives**
For each workstream: exactly two sentences — (1) current status and completions since last meeting, (2) key risk or next milestone and what must happen to stay on track. If AMBER-OVERRIDE was applied, add a third sentence beginning with "NOTE:" stating the override and triggering language.

Rules:
- Do not invent blockers or dependencies not present in the inputs. Note any missing information as a data gap.
- Do not soften AMBER-OVERRIDE findings. Record the exact triggering text.
- Do not assign RED based on a general risk mention alone — apply the criteria strictly.
- Maximum two sentences (plus NOTE if applicable) per workstream in Section D.
```

## Example output

**Scenario**: IT workstream self-reports GREEN but mentions awaiting vendor sign-off; Finance ERP go-live depends on IT system cutover completing first.

---

**A. RAG Summary Table (excerpt)**

| Workstream | Track | Self-Reported | Normalized | Override? | Owner |
|---|---|---|---|---|---|
| IT Systems | Technology | GREEN | AMBER | AMBER-OVERRIDE: "awaiting vendor sign-off on network configuration" on Day 90 cutover path — self-reported GREEN without acknowledgment of open dependency | J. Chen |
| Finance / ERP | Finance | GREEN | AMBER | Dependency risk: ERP go-live (Day 105) depends on IT cutover (Day 90); IT now AMBER | M. Reyes |

---

**B. Escalation List (excerpt)**

> **1. IT Systems — Vendor sign-off delay threatens Day 90 network cutover**
> Authority needed: Steering committee escalation to accelerate vendor contract terms
> Impact: IT cutover milestone — Day 90 (14 days from reporting date)
> Downstream affected: Finance/ERP (Day 105 go-live), Payroll (Day 95 parallel run)
> Recommended owner: CTO / Integration Sponsor
> Recommended action: Authorize procurement team to invoke SLA escalation clause with network vendor by end of week.

---

**C. Steering Committee Agenda (excerpt)**

| Time | Agenda Item | Owner | Goal |
|---|---|---|---|
| 0:00–0:05 | Integration health overview — RAG dashboard | PMO Lead | Alignment on current status |
| 0:05–0:25 | DECISION: IT vendor escalation — authorize SLA clause invocation | CTO | Decision |
| 0:25–0:40 | DECISION: ERP go-live contingency — Day 105 vs. Day 120 option | CFO / PMO | Decision |
| 0:40–0:55 | Watch items: HR HRIS data migration (AMBER), Legal contracts (AMBER) | Track leads | Awareness |
| 0:55–1:00 | Action log and close | PMO Lead | Confirm owners |

---

**D. Workstream Status Narratives (excerpt)**

**IT Systems**: AMBER. Network infrastructure design is complete and vendor contracts are executed, but sign-off on final network configuration remains outstanding from the primary vendor. The Day 90 cutover milestone requires vendor confirmation by June 10 to preserve the go-live window; if not received, the PMO should trigger the SLA escalation clause. NOTE: Self-reported GREEN overridden to AMBER — "awaiting vendor sign-off on network configuration" is an unresolved blocker on the Day 90 critical path.

---

## Tips

1. **Paste updates in consistent separators.** Separate each workstream update with a clear label (e.g., "=== HR — HRIS Migration ===") so the model can parse them reliably, even if the update formats vary.

2. **Include hard deadlines in the integration context block.** TSA expiry dates, regulatory deadlines, and Day 100/180 milestone dates are essential for the model to calibrate RED vs. AMBER. Without them, it cannot determine whether a slipping milestone is critical or recoverable.

3. **Don't clean up the raw updates before pasting.** The model detects optimism bias from the actual language workstream leads use — hedged phrases like "hoping to," "we expect," and "should be resolved" are the signals. Paraphrasing before pasting will suppress the detection.
