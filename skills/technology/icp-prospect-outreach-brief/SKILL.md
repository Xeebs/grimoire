---
name: icp-prospect-outreach-brief
description: Given a target account name, ICP criteria, and raw account signals (funding, hiring, tech stack, leadership changes, news), synthesizes a structured ICP fit-score with rationale, identifies the two highest-relevance pain points for the specific account, and produces a ready-to-send multi-touch outreach brief with a personalized first line, a value proposition hook anchored to the account's current context, and a channel-specific call-to-action for email, LinkedIn, and cold call opener — for Sales Development Representatives and Account Executives.
industry: technology
role: Sales Development Representative / Account Executive
trigger: Before building or launching an outreach sequence for a target account; the rep has an account name and ICP match on paper, has gathered raw signals from Apollo/Clay/LinkedIn/news sources, and needs to synthesize those signals into a personalized "why now, why us" brief before writing any copy.
---

## Context

The SDR or AE has identified a target account that matches their ICP on firmographic dimensions — company size, industry vertical, revenue band, or geography. They have pulled raw signals from one or more sources: a recent funding announcement, LinkedIn job postings indicating headcount growth in a relevant function, a tech stack indicator from BuiltWith or G2, a leadership change, or a press mention. They may also have an inbound intent signal — a pricing page visit, a content download, or a competitor review on G2.

What they do not yet have is an answer to the question every prospect asks: "Why are you contacting me, right now?" Generic messaging built on ICP fit alone produces low reply rates. The value is in connecting the account's current moment — what they just funded, just hired for, just announced, or just changed — to a specific pain point your product addresses, and then translating that connection into copy that a real person would open and respond to.

This skill performs that interpretive synthesis step. It does not aggregate data — the rep provides that. It reads the signals provided, reasons about which signals indicate the highest-urgency pain points, assigns a structured ICP fit-score explaining why this account fits now (not just in general), and generates ready-to-send copy for three channels that all anchor to the same account-specific context. The three channels are not independent templates — they are a coordinated multi-touch sequence where each touchpoint reinforces the same personalized hook from a different angle.

The rep retains final judgment on tone, timing, and which channel to lead with. This skill produces a first draft that eliminates the blank-page and research-synthesis steps.

---

## Instructions

Follow these steps in sequence. Do not skip or combine steps.

### Step 1 — Signal Inventory

Read all provided signals and produce a **Signal Inventory** with two columns:

- **Signal**: The specific fact or observation (e.g., "Raised $40M Series B in March 2024 led by Andreessen Horowitz")
- **Signal Type**: Classify as one of: FUNDING_EVENT | HIRING_VELOCITY | TECH_STACK_CHANGE | LEADERSHIP_CHANGE | COMPANY_NEWS | INTENT_SIGNAL | COMPETITIVE_SIGNAL | OTHER

For each signal, note the approximate recency (if available): RECENT (< 30 days), WARM (30–90 days), or AGED (> 90 days).

If the rep has provided no signals and only the account name, proceed to Step 2 but flag at the top: `[REP ACTION REQUIRED: No account signals provided. ICP fit-score and outreach personalization will be generic without signal input. Provide at least 2 signals before sending.]`

### Step 2 — ICP Fit Assessment

Using the provided ICP criteria and the signal inventory, produce an **ICP Fit Assessment** with the following components:

**A. Fit Dimensions Table**

For each ICP dimension the rep has provided (firmographic, technographic, behavioral, or situational), score it STRONG FIT | PARTIAL FIT | WEAK FIT | NO DATA, with a one-sentence rationale citing the specific signal or criterion that supports the score.

| ICP Dimension | Score | Rationale |
|---------------|-------|-----------|

**B. Overall Fit Score**

Score the account on a 5-point scale:
- **5 — Priority Tier**: Matches all core ICP dimensions; has at least one RECENT or WARM trigger event
- **4 — Strong Fit**: Matches all core dimensions; trigger events are AGED or absent
- **3 — Solid Fit**: Matches 75%+ of ICP dimensions; some gaps
- **2 — Partial Fit**: Matches 50–74% of ICP dimensions; worth working but not top priority
- **1 — Low Fit**: Matches fewer than 50% of dimensions; flag for rep review before spending further time

State the score numerically and in the tier label. Provide a 2–3 sentence overall rationale explaining the score. If the score is 1 or 2, add: `[REP REVIEW: This account may not warrant full outreach sequence investment. Confirm ICP criteria before proceeding.]`

**C. "Why Now" Trigger**

Identify the single highest-urgency trigger event from the signal inventory — the signal that most directly indicates that the account has a live, active need your product addresses right now. State:
- The trigger event
- Why this specific event creates urgency (what pain point or decision it activates)
- The approximate window of relevance (e.g., "post-Series B spending decisions typically occur within 90 days of close")

If no clear trigger event exists, state: `[NO TRIGGER EVENT IDENTIFIED: outreach will rely on fit alone, not timing. Lower reply rate expected.]`

### Step 3 — Pain Point Identification

Identify the **two highest-relevance pain points** for this specific account, in priority order. For each:

**Pain Point [N]: [Name of the pain point]**
- **Account-specific evidence**: Which signal(s) indicate this account is experiencing or about to experience this pain? Be specific — cite the signal.
- **Why this pain point over others**: Explain why this pain point ranks above others for this account given its current context.
- **Value proposition connection**: State in one sentence how your product addresses this pain point. Use the value proposition input provided by the rep. Do not fabricate product capabilities.

Rank the pain points by: (a) evidential strength — how many signals point to it, and (b) urgency — how time-sensitive is the pain relative to the account's current moment.

### Step 4 — Multi-Touch Outreach Brief

Produce channel-ready copy for three touchpoints. All three must anchor to the same account context and the same primary pain point identified in Step 3. They are a coordinated sequence, not three independent templates.

**Sequence architecture**: The default recommended sequence is Email (Day 1) → LinkedIn Connection Request + Note (Day 3) → Cold Call Opener (Day 5). If the rep specifies a different sequence architecture, follow theirs.

---

#### TOUCHPOINT 1: Email

**Subject line** (2 options — provide A and B variants):
- Option A: [Curiosity/question-framing subject line]
- Option B: [Direct relevance/trigger-event subject line]

**Email body**:
```
[PERSONALIZED FIRST LINE — anchored to the specific trigger event or account signal. Must reference something specific to this account, not a generic opener. 1–2 sentences.]

[PAIN POINT HOOK — connect their current context to the pain point identified in Step 3. 2–3 sentences. Do not list features. Describe the outcome they are missing or the problem they are about to face.]

[VALUE PROPOSITION BRIDGE — one sentence connecting the pain to your product's capability. Use the product/service description the rep provided.]

[CALL-TO-ACTION — low-friction ask. Default: offer a specific time or ask a single yes/no question. Do not ask for a 30-minute call in the first email.]
```

**Word count target**: 75–120 words for the body. Flag if the draft exceeds 150 words.

---

#### TOUCHPOINT 2: LinkedIn Connection Request Note

**Character limit**: 300 characters (LinkedIn hard limit for connection notes). Draft must fit within this limit.

```
[NOTE: Must include: (1) specific account-relevant hook in the first sentence, (2) a clear reason why the rep is reaching out now, (3) no pitch — this is a connection request, not a sales message.]
```

Provide the character count of the draft alongside it.

---

#### TOUCHPOINT 3: Cold Call Opener

**Opening line** (the first thing the rep says after the prospect picks up):
```
[Must: acknowledge the interruption, establish relevance in one sentence using the trigger event, and end with a permission question — not a pitch. Target: 2–3 sentences, 20–30 seconds spoken.]
```

**If they say "What's this about?" / "What are you selling?"** — provide a 2-sentence bridge that states the value proposition without sounding like a script:
```
[BRIDGE RESPONSE: 2 sentences]
```

**If they say "Not interested" / "Send me an email"** — provide a single-sentence soft close that keeps the door open:
```
[SOFT CLOSE: 1 sentence]
```

---

### Step 5 — Outreach Brief Summary

Produce a one-page summary the rep can attach to the account record in their CRM (Salesforce, HubSpot, or similar):

```
ACCOUNT OUTREACH BRIEF
======================
Account:          [Account name]
Prepared:         [Date]
ICP Fit Score:    [N/5 — Tier label]
Why Now:          [1-sentence trigger event summary]
Primary Pain:     [Pain Point 1 name — 1-sentence description]
Secondary Pain:   [Pain Point 2 name — 1-sentence description]

Recommended Sequence:
  Day 1: Email — [Subject line used]
  Day 3: LinkedIn — [First 5 words of the connection note]
  Day 5: Cold Call — [First 5 words of the opener]

Signals used:     [Bullet list of signals incorporated into the copy]
Signal gaps:      [Any standard ICP signal category not available — note it]

Rep notes:        [Leave blank for rep to complete]
```

---

## Output Format

The complete output follows this structure in order:

1. **Signal Inventory** — table with Signal | Signal Type | Recency
2. **ICP Fit Assessment** — Fit Dimensions Table, Overall Fit Score (N/5 + tier + rationale), Why Now Trigger
3. **Pain Point Identification** — Pain Point 1 and Pain Point 2, each with evidence, ranking rationale, and value proposition connection
4. **Multi-Touch Outreach Brief** — Touchpoint 1 (Email), Touchpoint 2 (LinkedIn Note), Touchpoint 3 (Cold Call Opener + objection handles)
5. **Account Outreach Brief Summary** — CRM-ready one-pager

Each section must be clearly headed with a section number and title. Use horizontal rules between sections. The copy blocks must be enclosed in code fences so the rep can copy them cleanly.

---

## Constraints

- **Do not fabricate account details.** If a signal is not provided, do not invent one. Personalization must be grounded in the specific signals the rep supplies. A made-up funding round or leadership change in the outreach copy is a reputation-damaging error.
- **Do not write generic pain points.** Pain points must be connected to signals specific to this account. "You might be struggling with X" statements not anchored to a provided signal are not acceptable.
- **Do not pitch product features.** The email and LinkedIn note must describe outcomes and pain, not feature lists. The product capabilities should appear only as a value proposition bridge (one sentence), not as a bulleted feature enumeration.
- **Do not exceed the LinkedIn character limit.** The connection note must be 300 characters or fewer. Always include the character count.
- **Do not produce three independent templates.** The three channel outputs must share the same personalized hook and pain point framing. They are a sequence, not parallel alternatives.
- **Do not infer ICP fit dimensions not provided.** If the rep does not specify an ICP criterion, do not add one. Score only the dimensions the rep defines.
- **Do not use manipulative or deceptive openers.** Do not draft subject lines that imply a prior relationship ("Following up on our conversation"), false urgency, or bait-and-switch framing.
- **Do not recommend proceeding with a score of 1.** If the fit score is 1, require rep review before proceeding. A score of 1 is a signal that the account may not be worth the sequence investment.
- **Do not provide legal, financial, or compliance advice.** If the prospect's context involves regulated industries, note any sensitivity without providing substantive legal or compliance analysis.
