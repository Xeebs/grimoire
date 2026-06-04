# Stakeholder Interview MECE Synthesizer

**Industry**: Consulting
**Role**: Management Consultant (Analyst / Associate)
**Time saved**: 2–4 days of synthesis work compressed to a structured first draft in under an hour

## What it does

Takes raw stakeholder interview notes from a consulting engagement and produces a full synthesis package: a MECE issue tree (mutually exclusive, collectively exhaustive), a contradiction register that names where stakeholder groups disagree and why it matters, and a hypothesis-driven recommendation brief — with every finding framed as "We believe X because Y" rather than as a neutral theme summary — mapped directly to the client's original strategic question.

## When to use it

Use this skill immediately after your final field interview, before the synthesis workshop or steerco preparation. The trigger moment is: you have all your interview notes open, you know what the client question is, and you need to move from raw notes to a structured issue tree and draft findings before the team convenes. It is most powerful when you have 10+ interviews across multiple stakeholder groups where contradictions are expected.

## Prompt template

Paste the full prompt below into Claude (or any capable LLM) and replace the placeholder sections with your actual materials.

---

You are assisting a management consultant who has just completed a round of stakeholder interviews. Your task is to synthesize the interview notes into a MECE issue tree, detect contradictions across stakeholder groups, and produce a hypothesis-driven recommendation brief mapped to the client's strategic question.

**The client question you must answer is:**
{CLIENT_QUESTION}

*(State the exact strategic or operational question the client is trying to decide. Example: "Should we centralize procurement and if so, how and over what timeline?" or "Is there a viable market for an AI-enabled advisory offering and what would it take to win?")*

**Interview scope:**
{INTERVIEW_SCOPE}

*(List the stakeholder groups interviewed and how many interviews were conducted with each. Example: "CFO (1), Regional General Managers (3), Procurement Leads (4), Plant Managers (5), External Suppliers (2)")*

**Client and engagement context:**
{CLIENT_CONTEXT}

*(2–4 sentences on the client: industry, size, the decision they face, and any constraints you know about — budget, timeline, political dynamics, prior failed initiatives. This sharpens the materiality standard for prioritization.)*

---

**Follow these steps in order:**

**Step 1 — Parse the client question and decision frame.**
Read the client question as stated above. Identify: (a) the core strategic or operational decision the client must make, (b) the decision-maker(s) and their constraints, and (c) the time horizon implied. State your interpretation of the decision frame in one sentence before proceeding. If the client question is compound or ambiguous, flag each distinct sub-question separately.

**Step 2 — Extract and tag all claims from the interview notes.**
For each interview, extract every distinct claim, concern, observation, or preference. A claim is any statement describing current state, expressing a preference or value, asserting a causal relationship, identifying a constraint, or signaling future behavior. Tag each claim with the interviewee's [Role/Title] and [Stakeholder Group]. Do not editorialize — extract claims as stated. Note any claim that contradicts something the same interviewee said elsewhere.

**Step 3 — Cluster into MECE issue buckets.**
Group all claims into named issue buckets. Apply the MECE test explicitly:

- **Mutual exclusivity**: Any claim that fits two buckets signals a boundary problem — resolve it and state your resolution.
- **Collective exhaustiveness**: Verify every claim from Step 2 is assigned to exactly one bucket. Claims that resist categorization go into an "Emerging / Uncategorized" bucket.

Name buckets with noun phrases capturing the strategic issue. Display the issue tree as a nested list with sub-themes under each top-level bucket.

**Step 4 — Detect contradictions across stakeholder groups.**
For each issue bucket, compare claims across stakeholder groups. Flag a contradiction when groups disagree on: a factual state, mutually exclusive preferred outcomes, or the predicted effect of the same action. For each contradiction record: which bucket, which groups, the nature (factual / preference / causal), the strategic significance, and the resolution path (data that could resolve it, or a fundamental value conflict the client must adjudicate).

Do not flatten contradictions into "mixed views" — each one must be named and its implication stated.

**Step 5 — Draft hypothesis-driven findings.**
For each issue bucket, write one primary finding:

"We believe [conclusion] because [evidence — cite specific stakeholder groups and substance of their claims]."

If a contradiction exists in this bucket, add: "However: [contradicting view, which group holds it, and what it would mean for the recommendation if this view is correct]."

If data is missing that could confirm or refute the finding, flag it as a data gap.

Every finding must be falsifiable — state what evidence would prove it wrong. Do not write neutral summaries. Phrases like "there were mixed views on X" are not findings.

**Step 6 — Map each finding to the client question.**
For each finding, write one sentence: "[Finding] tells the client [specific implication for the decision]." If a finding does not inform the strategic decision, flag it as peripheral — do not include it in the main recommendation structure.

**Step 7 — Prioritize recommendations.**
Convert each finding into a draft recommendation. Rate each on:

- **Impact**: How much does this move the needle on the client question? (High / Medium / Low + one-sentence rationale)
- **Feasibility**: Can the client act on this in a 6–12 month horizon given the constraints surfaced in interviews? (High / Medium / Low + one-sentence rationale)

Assign to: **Strategic Bet** (high impact, medium-high feasibility), **Quick Win** (medium-low impact, high feasibility), or **Parking Lot** (low feasibility or low impact).

**Step 8 — Produce the recommendation brief.**
Use the output format below exactly.

---

**OUTPUT FORMAT:**

### RECOMMENDATION BRIEF
**Client**: [client name or description]
**Engagement**: [project name]
**Client Question**: [exact question as stated]
**Decision Frame**: [your one-sentence interpretation]
**Interview scope**: [N interviews | Stakeholder groups: list]

---

### EXECUTIVE SUMMARY
Three key messages — each a single declarative sentence:
1. [Most important directional conclusion]
2. [Most important tension or condition]
3. [Most important action implication]

---

### MECE ISSUE TREE
[Nested list of issue buckets and sub-themes. Note the number of interviews each bucket was raised in.]

---

### CONTRADICTION REGISTER

| # | Issue Bucket | Groups in Tension | Nature | Strategic Significance | Resolution Path |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... |

---

### FINDINGS AND RECOMMENDATIONS

For each issue bucket:

**[Issue Bucket Name]**
Finding: We believe [X] because [Y — cite stakeholder groups].
However: [Contradiction or caveat, if any]
Data gap: [Missing information, if any]
Informs decision by: [Link to client question]
Recommendation: [Specific action]
Priority: [Strategic Bet | Quick Win | Parking Lot]
Impact: [High | Medium | Low] — [Rationale]
Feasibility: [High | Medium | Low] — [Rationale]

---

### OPEN QUESTIONS
[Numbered list. For each: the precise question, the best stakeholder group to answer it, and the recommended follow-up action.]

---

### PERIPHERAL FINDINGS / MONITORING ITEMS
[One-sentence observations that do not inform the strategic decision, with a note on why each is peripheral.]

---

**GUARDRAILS — the model must follow these without exception:**
- Never produce a flat theme list. MECE structure and hypothesis-driven framing are required.
- Never write neutral summaries. Every finding must commit to a directional conclusion.
- Apply and state the MECE test explicitly. If a clean MECE structure is impossible, say so.
- Name every contradiction. Do not soften contradictions into "nuance" or "context-dependence."
- All claims in findings must trace to a specific stakeholder group. Do not invent evidence.
- Flag data gaps explicitly — especially if key stakeholder groups were not interviewed.
- Every prioritization label (Strategic Bet / Quick Win / Parking Lot) must have an impact and feasibility rationale.
- If findings point to a difficult recommendation, state it. Do not hedge to protect political comfort.

---

**INTERVIEW NOTES:**

{INTERVIEW_NOTES}

*(Paste your interview notes here. Label each interview clearly: "INTERVIEW — [Role/Title], [Stakeholder Group], [Date if available]". Include the interviewee's responses as completely as possible. Bullet-point notes are fine — full transcripts are better. If an interview was conducted but notes are sparse, include what you have and note it was a partial record.)*

## Example output

**RECOMMENDATION BRIEF**
Client: MidWest Manufacturing Corp
Engagement: Procurement Operating Model Review
Client Question: Should we centralize procurement and if so, how and over what timeline?
Decision Frame: The client must decide whether to shift procurement authority from five regional GMs to a central function, accepting short-term agility risk in exchange for long-term cost reduction and supplier leverage.
Interview scope: 20 interviews | CFO (1), Regional GMs (3), Procurement Leads (4), Plant Managers (5), Key Suppliers (2), Operations Directors (2), Finance BPs (2), HR (1)

---

**EXECUTIVE SUMMARY**
1. Centralization will deliver $8–12M in annual savings via supplier consolidation and volume leverage, but only if the central function is built with embedded regional category expertise — without it, the 2019 pilot's failure will repeat.
2. The three Regional GMs present the highest implementation risk: they control escalation paths to the board and will resist any model that removes their authority over emergency procurement decisions.
3. A phased model — centralizing direct materials in Year 1 while preserving regional discretion for MRO and local services — captures 70% of the savings with significantly lower political and operational risk than a full-transition approach.

---

**MECE ISSUE TREE**

- Cost Structure and Savings Potential (raised in 18 of 20 interviews)
  - Supplier consolidation and volume leverage opportunity
  - Process inefficiency from duplicated regional procurement teams
  - Hidden cost of emergency/spot purchasing under regional model
- Operational Agility and Regional Autonomy (raised in 16 of 20 interviews)
  - Lead time sensitivity for regional plant operations
  - Emergency procurement authority and decision speed
  - Regional supplier relationships as competitive advantage
- Governance Design and Change Management (raised in 14 of 20 interviews)
  - Central function capability requirements and staffing
  - Regional stakeholder buy-in and escalation risk
  - Transition timeline and phasing options
- Supplier Relationship Impact (raised in 8 of 20 interviews)
  - Preferred supplier status under centralized negotiation
  - Regional supplier viability under volume consolidation

---

**CONTRADICTION REGISTER**

| # | Issue Bucket | Groups in Tension | Nature | Strategic Significance | Resolution Path |
|---|---|---|---|---|---|
| 1 | Cost Structure | CFO vs. Regional GMs | Factual | CFO asserts 15% savings from consolidation; GMs assert savings are overstated because regional emergency procurement is unavoidable and not counted in HQ models | Pull historical emergency procurement spend by region and run against consolidated pricing scenarios |
| 2 | Operational Agility | Plant Managers vs. Procurement Leads | Causal | Plant Managers assert regional procurement autonomy is essential for 48-hour emergency response; Procurement Leads assert a central function with regional liaisons can meet the same SLA | Benchmark against peer companies that have centralized: what are actual emergency response times? |
| 3 | Governance | Regional GMs vs. CFO | Preference | GMs prefer a federated model preserving local P&L control over procurement; CFO will not approve a model that does not consolidate supplier contracts | Fundamental value conflict — client must adjudicate; no data will resolve it |

---

**FINDINGS AND RECOMMENDATIONS**

**Cost Structure and Savings Potential**
Finding: We believe centralization can generate $8–12M in annual savings because the CFO's analysis (supported by two Finance BPs) identifies $6M in supplier duplication and $3–4M in process redundancy — and Procurement Leads (3 of 4) independently validated that no regional team currently achieves volume leverage above $2M per category.
However: Three Regional GMs assert the savings model omits emergency procurement spend, which runs at 15–20% premium to contract pricing and would erode headline savings by $2–4M annually if centralization reduces response speed.
Data gap: We do not have a clean split of emergency vs. planned procurement spend by region. This data exists in the ERP system and should be pulled before finalizing the savings case.
Informs decision by: The savings magnitude directly determines whether centralization clears the client's ROI threshold for a major operating model change.
Recommendation: Commission a 3-week ERP analysis to build the true total-cost-of-procurement baseline before committing to a savings target in the business case.
Priority: Quick Win
Impact: Medium — validates or adjusts the core financial rationale before the board presentation
Feasibility: High — data exists internally; no new interviews required

---

**OPEN QUESTIONS**
1. What is the actual emergency procurement spend by region, broken down by category? — Best answered by: Finance BPs with ERP access — Follow-up: formal data request within 2 weeks
2. Can the proposed central function meet a 48-hour emergency response SLA? — Best answered by: Benchmarking against 2–3 peer companies that have centralized — Follow-up: rapid benchmarking workstream
3. What are the contractual constraints on existing regional supplier agreements? — Best answered by: Legal review of top 20 supplier contracts by spend — Follow-up: document review

## Tips

1. **Provide the client question verbatim, not a paraphrase.** The model uses the exact wording to test whether each finding genuinely informs the decision. A vague question ("how should we improve procurement?") produces vague output. A precise question ("should we centralize procurement and if so, how?") produces a MECE structure anchored to a real decision.

2. **Label every interview by role and stakeholder group before pasting.** The contradiction detection depends on knowing which groups hold which views. An interview labeled "Interview 7" tells the model nothing useful. Label it "INTERVIEW — Regional GM, Midwest Region, Plant A" and the contradiction register becomes operationally meaningful.

3. **Include your engagement context, including prior failed initiatives.** If the client tried centralization before and it failed, the model needs to know this to flag it as a data-driven constraint on feasibility. Without context, the model will generate recommendations that are analytically sound but politically naive.
