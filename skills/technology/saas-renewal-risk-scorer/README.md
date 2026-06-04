# SaaS Renewal Risk Scorer and Save Playbook Builder

**Industry**: Technology
**Role**: Customer Success Manager
**Time saved**: 3–5 hours per at-risk account (replaces manual data consolidation, risk triage, save-play selection, and outreach brief drafting)

## What it does

Given a customer account summary, this skill scores renewal risk across four dimensions (Adoption Depth, Relationship Health, Value Realization, Competitive Exposure), classifies the account into one of four save-play tiers, selects two to three specific intervention actions from a CSM playbook, and produces a ready-to-use action brief with a sequenced outreach plan and account-specific talking points grounded in the account's actual data.

## When to use it

Invoke this skill when you are entering the 90–120-day pre-renewal window for an account and need to decide whether it requires an executive save play, an accelerated QBR, a proactive touch, or standard renewal handling. It is most valuable when you have pulled data from multiple tools (product analytics, CRM, CS platform) and need to consolidate signals into an actionable brief rather than a generic health score.

## Prompt template

Copy and paste the full prompt below. Replace every `{PLACEHOLDER}` with your account's real data before submitting.

---

You are a Customer Success expert performing renewal risk triage for a SaaS account. Analyze the account data below, score each of the four risk dimensions, classify the account into the correct save-play tier, select the two to three highest-leverage intervention actions from the CSM playbook, and produce a complete CSM Action Brief with a sequenced outreach plan and account-specific talking points.

### Scoring Rules

**Dimension 1 — Adoption Depth**
- High Risk: DAU/MAU < 20% OR license utilization < 40% OR 0 key features active beyond base module OR last login > 30 days ago
- Medium Risk: DAU/MAU 20–50% OR license utilization 40–65% OR only 1 key feature active OR last login 14–30 days ago
- Low Risk: DAU/MAU > 50% AND license utilization > 65% AND 2+ key features active AND last login within 14 days
- Worst-case indicator wins if signals conflict.

**Dimension 2 — Relationship Health**
- High Risk: champion last contacted > 45 days ago OR executive sponsor last contacted > 90 days ago OR 2+ open escalation tickets OR support tickets trending upward
- Medium Risk: champion last contacted 21–45 days ago OR exec sponsor 45–90 days ago OR 1 open escalation OR ticket volume flat but above baseline
- Low Risk: champion contacted within 21 days AND exec sponsor within 45 days AND 0 open escalations AND tickets flat or declining

**Dimension 3 — Value Realization**
- High Risk: no ROI documentation AND last QBR/EBR > 180 days ago or never held AND < 50% of promised outcomes delivered AND no expansion conversation ever held
- Medium Risk: partial ROI docs OR QBR 90–180 days ago OR 50–80% of outcomes delivered OR expansion stalled
- Low Risk: ROI documentation complete AND QBR within 90 days AND 80%+ outcomes delivered AND expansion active

**Dimension 4 — Competitive Exposure**
- High Risk: renewal not initiated AND (competitor evaluation active OR budget cuts flagged OR 2+ stakeholder changes in past 90 days)
- Medium Risk: renewal not initiated but no active competitor signal OR 1 stakeholder change OR budget constraint mentioned but unconfirmed
- Low Risk: renewal initiated AND no competitor signals AND no stakeholder changes AND no budget constraint notes

### Tier Classification (first match wins)

- **CRITICAL — Executive Save Play**: Any dimension is High Risk AND (ACV > $50,000 OR days until renewal ≤ 60)
- **CRITICAL — Executive Save Play (High-Value)**: Two or more dimensions are High Risk regardless of ACV or timeline
- **AT-RISK — QBR Acceleration**: Two or more dimensions are Medium Risk (no dimension High Risk)
- **WATCHLIST — Proactive Touch**: Exactly one dimension is Medium Risk (all others Low Risk)
- **HEALTHY — Standard Renewal**: All four dimensions are Low Risk

### CSM Playbook Actions (select 2–3 that match this account's risk drivers)

- **Executive Sponsor Reconnect**: Peer-to-peer VP/CSO call. Use when exec sponsor contact overdue or stakeholder change at VP+ level.
- **Champion Re-engagement and Value Review**: 1:1 with named champion to walk through usage data and understand internal dynamics. Use when champion contact overdue or new champion identified.
- **Technical Health Check**: Solutions Engineer audit of feature adoption gaps. Use when license utilization or feature activation is the primary risk.
- **ROI Validation Workshop**: Facilitated session to document delivered outcomes and quantify impact. Use when value realization is High or Medium Risk and ROI documentation is missing.
- **QBR/EBR Acceleration**: Pull forward the QBR or conduct an unscheduled EBR. Use when QBR is overdue and value realization is at risk.
- **Competitive Differentiation Brief**: Targeted comparison document addressing the named competitor. Use when competitor evaluation is actively noted.
- **Renewal Conversation Initiation**: Formal commercial conversation on renewal terms and multi-year options. Use when renewal not yet initiated and ≤ 90 days to renewal.
- **Stakeholder Mapping and Influence Assessment**: Identify new stakeholders from turnover, map priorities, conduct intro calls. Use when 1+ stakeholder change in past 90 days.
- **Adoption Acceleration Sprint**: 30-day engagement with power users and admins to drive feature activation. Use when adoption is the primary risk and renewal is 90+ days out.

Note: Do not recommend Adoption Acceleration Sprint as a primary intervention when renewal is fewer than 60 days out.

### Output Format

Produce the output using these exact sections:

**Account Renewal Risk Assessment: [Account Name]**
Renewal Date | Days Until Renewal | ACV

**Dimension Scores** (table: Dimension / Score / Key Signal(s))

**Tier Classification**
State the tier, the classification rule triggered, and a 2–3 sentence risk summary synthesizing what the dimension scores mean together.

**Recommended Interventions** (2–3)
For each: Action Name, why this account, owner role, timing relative to renewal date.

**CSM Action Brief**
- Primary risk driver (one sentence)
- Recommended outreach sequence (numbered steps with day ranges, named stakeholders, medium, and purpose)
- Talking points for champion (specific, data-anchored — no generic phrases)
- Talking points for executive sponsor (if executive engagement required)
- What to avoid (specific to this account's signals)

**Data Gaps**
List any missing fields and how each affected scoring. State "None identified" if complete.

### Constraints

- Do not invent account data. Mark missing fields as "Insufficient data" and flag in Data Gaps.
- Every talking point must reference a specific metric, name, date, or outcome from the input. Generic value-statement phrases are not acceptable.
- Do not recommend more than three interventions.
- Do not classify as HEALTHY unless all four dimensions are explicitly Low Risk.
- Do not use CS platform brand names in the output.
- Do not conflate champion and executive sponsor — each requires distinct outreach.

---

### Account Data

**Account**: {ACCOUNT_NAME}
**ACV**: ${ACV}
**Renewal Date**: {RENEWAL_DATE}
**Days Until Renewal**: {DAYS_UNTIL_RENEWAL}

**Adoption Depth**
- DAU/MAU ratio: {DAU_MAU_RATIO}
- License utilization: {SEATS_USED} of {SEATS_CONTRACTED} seats ({UTILIZATION_PCT}%)
- Key features active: {LIST_ACTIVE_FEATURES}
- Days since last active user login: {DAYS_SINCE_LAST_LOGIN}

**Relationship Health**
- Champion: {CHAMPION_NAME}, last contacted {CHAMPION_LAST_CONTACT_DAYS} days ago
- Executive sponsor: {EXEC_SPONSOR_NAME} ({EXEC_SPONSOR_TITLE}), last contacted {EXEC_SPONSOR_LAST_CONTACT_DAYS} days ago
- Open escalation tickets: {ESCALATION_COUNT} ({TICKET_DESCRIPTIONS_IF_ANY})
- Support ticket trend (past 90 days): {TREND: increasing / flat / decreasing}

**Value Realization**
- ROI documentation: {exists / partial / none}
- Last QBR/EBR date: {DATE_OR_NEVER}
- Business outcomes delivered vs. promised: {OUTCOMES_SUMMARY}
- Expansion conversation status: {held / stalled / never held}

**Competitive Exposure**
- Renewal conversation initiated: {yes / no}
- Competitor evaluation signals: {description or none}
- Budget constraint signals: {description or none}
- Stakeholder changes in past 90 days: {count and description}

**Additional context**: {ANY_OTHER_RELEVANT_NOTES}

---

## Example output

---

### Account Renewal Risk Assessment: Meridian Financial Services

**Renewal Date**: 2026-09-15 | **Days Until Renewal**: 103 | **ACV**: $112,000

---

#### Dimension Scores

| Dimension | Score | Key Signal(s) |
|---|---|---|
| Adoption Depth | Medium Risk | License utilization 52% (94/180 seats); Advanced Reporting and API Connector features never activated |
| Relationship Health | High Risk | Executive sponsor (CFO Dana Reyes) last contacted 97 days ago; 2 open escalation tickets (ticket #4891, #4902) |
| Value Realization | Medium Risk | Last EBR held 7 months ago (November 2025); ROI documentation partial — cost savings quantified but productivity gains not documented |
| Competitive Exposure | High Risk | Renewal conversation not initiated; procurement contact Sarah Bloom mentioned "evaluating alternatives" on 2026-05-20 call; CFO change 42 days ago |

---

#### Tier Classification

**Tier**: CRITICAL — Executive Save Play

**Classification rule triggered**: Two or more dimensions are High Risk (Relationship Health: High Risk; Competitive Exposure: High Risk), regardless of ACV or timeline.

**Risk summary**: Meridian has gone dark at the executive level precisely when competitive signals and a CFO transition make executive engagement most critical. The combination of an overdue CFO touch, two unresolved escalations, and an active competitive evaluation with renewal not yet initiated means the account's internal dynamics have shifted in a direction this CSM cannot correct at the champion level alone. If the escalation tickets are not resolved before the CFO makes a vendor decision, the competitive threat will be amplified by a perception of poor support quality.

---

#### Recommended Interventions

**Intervention 1: Executive Sponsor Reconnect**
- Why this account: CFO Dana Reyes has not been contacted in 97 days, a CFO-level change occurred 42 days ago (Reyes may now have a changed mandate), and a competitive evaluation was surfaced on the most recent call. The executive relationship must be reset before the competitive brief is relevant.
- Owner: CSM + VP of Customer Success
- Timing: Within 7 days

**Intervention 2: Competitive Differentiation Brief**
- Why this account: Sarah Bloom explicitly mentioned evaluating alternatives. A targeted brief addressing the specific competitor (if named) or category-level differentiation is needed before the next executive touch.
- Owner: CSM + Product Marketing
- Timing: Prepare within 5 days; deliver at or before executive reconnect call

**Intervention 3: ROI Validation Workshop**
- Why this account: The partial ROI documentation (cost savings only, productivity gains undocumented) leaves the account without a defensible internal business case to counter a competitive pitch. A facilitated session to complete the ROI summary gives the champion ammunition before the CFO decision window.
- Owner: CSM + Champion (Sarah Bloom)
- Timing: Schedule within 10 days; complete before executive reconnect

---

#### CSM Action Brief

**Primary risk driver**: CFO-level executive relationship has lapsed for 97 days during an active competitive evaluation with renewal not initiated — the account lacks executive sponsorship and an internal business case at the moment a competitive decision is most likely.

**Recommended outreach sequence**:

1. **Days 1–3** — Internal prep: Pull all open escalation tickets (#4891, #4902) and confirm resolution status with Support. Do not schedule any customer-facing executive call until both escalations have a clear path to closure.
2. **Days 3–5** — Champion email (Sarah Bloom): Acknowledge the recent CFO transition, confirm she is still the right point of contact for the renewal, and request a 30-minute call to review account standing and upcoming calendar.
3. **Days 5–7** — VP outreach to CFO Dana Reyes (via email, personalized by VP): Reference the 2.5-year relationship, acknowledge the recent leadership transition, and request a strategic alignment conversation at CFO-to-VP level before renewal discussions begin.
4. **Days 10–14** — ROI Validation Workshop with Sarah Bloom: Complete the productivity gains documentation and produce a one-page customer-owned ROI summary she can share upward.

**Talking points for Sarah Bloom (champion)**:
- "Since the EBR in November, your team has processed 47% more transactions through the platform with the same headcount — that's the productivity story we haven't formally captured yet and it should be in the renewal discussion."
- "I want to make sure you have what you need before any conversation with the new CFO about the renewal. The cost savings are documented; let's spend 45 minutes quantifying the time your team has saved so that story is complete."
- "On tickets #4891 and #4902 — I'm personally tracking both with our Support team and will have a status update for you by [specific date]. I don't want those sitting open when we go into renewal discussions."

**Talking points for CFO Dana Reyes (executive sponsor)**:
- "Your team has been on the platform for 2.5 years. Before we talk about next year's terms, I want to make sure you have a clear picture of what the platform has delivered — specifically the cost savings your team quantified last year and the productivity gains we're now putting numbers to."
- "We're aware we've been quiet at this level since November and that's on us. Given the transition you've been navigating, we want to make sure you have the full context, not just a renewal invoice."

**What to avoid**:
- Do not open the executive reconnect call by presenting multi-year pricing or expansion packaging — the CFO has not been engaged in 97 days and has heard a competitive pitch; leading with commercial terms before reestablishing value will accelerate churn, not prevent it.
- Do not reference ticket #4891 or #4902 with the CFO until they are resolved — mentioning unresolved escalations at the executive level amplifies the competitive risk.

---

#### Data Gaps

- Competitor name not specified: Sarah Bloom mentioned "evaluating alternatives" but no vendor name was provided. The Competitive Differentiation Brief cannot be made specific until the competitor is identified — CSM should ask Sarah Bloom directly on the champion call.
- Exact CFO change context unknown: It is unclear whether Dana Reyes is new to the CFO role or whether the change involved a different person taking the CFO title. Clarify on champion call before VP outreach is sent.

---

## Tips

1. **Feed complete data.** This skill's output quality is directly proportional to input completeness. Vague entries like "some support tickets" or "sporadic usage" produce weak talking points — pull the specific numbers from your CS platform and CRM before invoking the skill.

2. **Name every stakeholder.** The prompt will produce generic talking points if you provide role titles without names. "Champion last contacted 30 days ago" produces a worse brief than "Sarah Bloom (Director of Operations) last contacted 31 days ago via email — no response."

3. **Flag competitive signals precisely.** If a competitor was named on a call, include the name and date. The Competitive Differentiation Brief intervention is significantly more useful when anchored to a specific vendor the account is evaluating rather than a general competitive concern.
