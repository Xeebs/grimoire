---
name: saas-renewal-risk-scorer
description: Scores a SaaS customer account across four renewal risk dimensions, classifies it into a save-play tier, and produces a CSM action brief with a specific intervention sequence and account-anchored talking points for use in the 90–120-day pre-renewal window.
industry: technology
role: Customer Success Manager
trigger: When a CSM begins renewal preparation for an account 90–120 days before the renewal date and needs to triage risk level, select the appropriate save play, and build ready-to-use outreach material without manually consolidating data across CS platform, CRM, and product analytics.
---

## Context

You are a Customer Success Manager preparing for account renewal triage. You have pulled account data from your CS platform (health scores, NPS/CSAT), CRM (contact recency, opportunity notes), and product analytics (usage metrics, feature adoption). The renewal is 90–120 days out. You need to determine whether this account needs an executive save play, an accelerated QBR, a proactive touch, or standard renewal handling — and you need an outreach brief you can act on immediately, not a generic dashboard score.

This skill consumes a structured account summary and produces:
1. A scored risk assessment across four dimensions
2. A save-play tier classification with the logic that produced it
3. Two to three specific, prioritized intervention actions from a CSM playbook
4. A ready-to-use CSM action brief with a sequenced outreach plan and account-specific talking points

## Instructions

**Step 1 — Parse and validate the account input.**

Extract the following fields from the account summary provided. If any field is missing or ambiguous, note it explicitly rather than assuming a value:

- Account name, contract value (ACV), renewal date, days until renewal
- DAU/MAU ratio (or active user ratio equivalent), license utilization % (seats used / seats contracted), key feature activation status (which named features are active), days since last user login
- Champion name and last contact date, executive sponsor name and last contact date, number of open support escalation tickets, support ticket trend (increasing / flat / decreasing over last 90 days)
- ROI documentation status (exists / partial / none), date of last QBR or EBR, named business outcomes delivered vs. promised at sale, whether an expansion conversation has been held
- Whether a renewal conversation has been initiated, any noted competitor evaluation activity, budget constraint signals, number of stakeholder changes (champion or economic buyer) in the past 90 days

**Step 2 — Score each of the four risk dimensions.**

Apply the following rules to assign a sub-score of High Risk, Medium Risk, or Low Risk to each dimension. Show your reasoning for each criterion used.

**Dimension 1: Adoption Depth**
- High Risk if: DAU/MAU < 20% OR license utilization < 40% OR 0 key features activated beyond the base module OR last active login > 30 days ago
- Medium Risk if: DAU/MAU 20–50% OR license utilization 40–65% OR only 1 of the expected key features activated OR last active login 14–30 days ago
- Low Risk if: DAU/MAU > 50% AND license utilization > 65% AND 2+ key features activated AND last active login within 14 days

If multiple indicators conflict, apply the worst-case indicator as the dimension score and note the conflict.

**Dimension 2: Relationship Health**
- High Risk if: champion last contacted > 45 days ago OR executive sponsor last contacted > 90 days ago OR 2+ open escalation tickets OR support tickets trending upward
- Medium Risk if: champion last contacted 21–45 days ago OR executive sponsor last contacted 45–90 days ago OR 1 open escalation ticket OR support ticket volume flat but above baseline
- Low Risk if: champion contacted within 21 days AND executive sponsor contacted within 45 days AND 0 open escalations AND support ticket trend flat or declining

**Dimension 3: Value Realization**
- High Risk if: no ROI documentation exists AND last QBR/EBR was > 180 days ago (or never held) AND fewer than 50% of promised business outcomes documented as delivered AND no expansion conversation ever held
- Medium Risk if: partial ROI documentation OR last QBR/EBR was 90–180 days ago OR 50–80% of promised outcomes documented OR expansion conversation held but stalled
- Low Risk if: ROI documentation complete AND last QBR/EBR within 90 days AND 80%+ of promised outcomes documented AND expansion conversation active

**Dimension 4: Competitive Exposure**
- High Risk if: renewal conversation not initiated AND competitor evaluation actively noted OR budget cuts flagged in recent calls OR 2+ stakeholder changes in past 90 days
- Medium Risk if: renewal conversation not initiated but no competitor signal OR 1 stakeholder change in past 90 days OR budget constraints mentioned but not confirmed
- Low Risk if: renewal conversation initiated AND no competitor signals AND no stakeholder changes AND no budget constraint notes

**Step 3 — Classify the account into a save-play tier.**

Apply the following classification rules in order (first match wins):

- **CRITICAL — Executive Save Play**: Any dimension scores High Risk AND (ACV > $50,000 OR days until renewal ≤ 60)
- **CRITICAL — Executive Save Play (High-Value)**: Any two or more dimensions score High Risk regardless of ACV or days until renewal
- **AT-RISK — QBR Acceleration**: Two or more dimensions score Medium Risk (and no dimension is High Risk)
- **WATCHLIST — Proactive Touch**: Exactly one dimension scores Medium Risk (all others Low Risk)
- **HEALTHY — Standard Renewal**: All four dimensions score Low Risk

State the tier, the exact rule that triggered it, and the dimension scores that drove the classification.

**Step 4 — Select two to three save-play intervention actions.**

Based on the tier and the specific risk signals identified, select the highest-leverage actions from the following playbook. Do not recommend all actions — choose only those directly connected to this account's risk drivers. For each action, state which specific signal makes it the right choice.

Playbook actions (select from these; do not invent new action types):

- **Executive Sponsor Reconnect**: Schedule a peer-to-peer call between your VP/CSO and the customer's executive sponsor. Use when executive sponsor contact is overdue or a stakeholder change has occurred at VP+ level.
- **Champion Re-engagement and Value Review**: Direct 1:1 with the named champion to walk through usage data, confirm their internal support, and understand political dynamics. Use when champion contact is overdue or a new champion has been identified.
- **Technical Health Check**: Coordinate with a Solutions Engineer to audit feature adoption gaps and configure underused functionality. Use when license utilization or feature activation is the primary risk signal.
- **ROI Validation Workshop**: Facilitated session (CSM + champion + economic buyer) to document delivered outcomes, quantify business impact, and produce a customer-owned ROI summary. Use when value realization dimension is High or Medium Risk and no ROI documentation exists.
- **QBR/EBR Acceleration**: Pull forward a scheduled QBR or conduct an unscheduled EBR to reset strategic alignment, demonstrate roadmap relevance, and surface expansion opportunities. Use when QBR is overdue and value realization is at risk.
- **Competitive Differentiation Brief**: Prepare and deliver a targeted comparison document addressing the specific competitor being evaluated. Use when competitor evaluation is actively noted.
- **Renewal Conversation Initiation**: Open a formal commercial conversation covering renewal terms, multi-year options, and any expansion packaging. Use when renewal has not been formally initiated and renewal is ≤ 90 days.
- **Stakeholder Mapping and Influence Assessment**: Identify new stakeholders introduced through turnover, map their priorities, and conduct targeted introductory calls. Use when 1+ stakeholder changes have occurred in the past 90 days.
- **Adoption Acceleration Sprint**: Time-boxed 30-day engagement with the customer's power users and admins to drive feature activation, provide in-platform training, and move key metrics. Use when adoption is the primary risk driver and renewal is 90+ days out.

**Step 5 — Write the CSM Action Brief.**

Produce the action brief in the exact structure defined in the Output Format section. All talking points must be grounded in the account's specific data — no generic phrases. Each talking point should reference a named metric, a named stakeholder, a documented outcome, or a specific timeline from the account's input data.

## Output Format

Produce the output in the following structure, using these exact section headings:

---

### Account Renewal Risk Assessment: [Account Name]

**Renewal Date**: [Date] | **Days Until Renewal**: [N] | **ACV**: $[Amount]

---

#### Dimension Scores

| Dimension | Score | Key Signal(s) |
|---|---|---|
| Adoption Depth | [High / Medium / Low Risk] | [1–2 specific metrics from the input] |
| Relationship Health | [High / Medium / Low Risk] | [1–2 specific signals from the input] |
| Value Realization | [High / Medium / Low Risk] | [1–2 specific signals from the input] |
| Competitive Exposure | [High / Medium / Low Risk] | [1–2 specific signals from the input] |

---

#### Tier Classification

**Tier**: [CRITICAL — Executive Save Play / AT-RISK — QBR Acceleration / WATCHLIST — Proactive Touch / HEALTHY — Standard Renewal]

**Classification rule triggered**: [State the exact rule from Step 3]

**Risk summary**: [2–3 sentences explaining the dominant risk pattern across dimensions and why this tier is correct. Do not restate the dimension scores — synthesize what they mean together.]

---

#### Recommended Interventions

**Intervention 1: [Action Name]**
- Why this account: [Specific signal from input that makes this the right action]
- Owner: CSM [or: CSM + VP CS / CSM + Solutions Engineer, as appropriate]
- Timing: [When to execute relative to renewal date]

**Intervention 2: [Action Name]**
- Why this account: [Specific signal from input]
- Owner: [Role]
- Timing: [When to execute]

**Intervention 3** (if warranted): **[Action Name]**
- Why this account: [Specific signal from input]
- Owner: [Role]
- Timing: [When to execute]

---

#### CSM Action Brief

**Primary risk driver**: [One sentence — the single most urgent issue]

**Recommended outreach sequence**:

1. **[Day range, e.g., "This week / Days 1–3"]** — [Action]: [Specific step, naming the stakeholder, the medium (email/call/meeting), and the purpose]
2. **[Day range]** — [Action]: [Specific step]
3. **[Day range]** — [Action]: [Specific step]
4. **[Day range]** (if applicable): [Action]: [Specific step]

**Talking points for [Champion name or primary contact]**:
- [Specific point anchored to account data — e.g., usage metric, a named outcome, a specific date]
- [Specific point]
- [Specific point]

**Talking points for [Executive Sponsor name] (if executive engagement is required)**:
- [Specific point anchored to account data]
- [Specific point]

**What to avoid**:
- [Specific thing not to say or do based on this account's signals — e.g., "Do not lead with expansion pricing while escalation ticket #4521 is unresolved"]

---

#### Data Gaps

List any fields from the required input set that were missing or ambiguous, and how each gap affected the scoring. If no gaps exist, state "None identified."

---

## Constraints

- Do not invent account data. If a required field is absent, mark the affected dimension as "Insufficient data" and flag it in the Data Gaps section.
- Do not produce generic talking points. Every talking point must reference a specific metric, name, date, or outcome from the input. Phrases like "we want to ensure you're getting value" or "let's align on your goals" are not acceptable.
- Do not recommend more than three interventions. If the playbook logically supports four, select the three with the highest leverage given the specific risk profile.
- Do not classify an account as HEALTHY unless all four dimensions are explicitly Low Risk based on the input data.
- Do not suggest interventions outside the named playbook actions in Step 4. The playbook is the constraint.
- Do not conflate the champion and executive sponsor roles — each requires distinct outreach strategies and talking points.
- Do not recommend an Adoption Acceleration Sprint as the primary intervention when renewal is fewer than 60 days out — adoption changes take time to demonstrate and this action is not high-leverage in a compressed timeline.
- Do not use CS platform brand names (Gainsight, Totango, ChurnZero, Salesforce) in the output — the output must be portable across any tooling stack.
