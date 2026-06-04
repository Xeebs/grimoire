# ICP-Fit Prospect Research and Personalized Outreach Brief

**Industry**: Technology
**Role**: Sales Development Representative / Account Executive
**Time saved**: 25–50 minutes per account (vs. 30–60 minutes of manual research and copy writing)

## What it does

Given a target account and the raw signals you have already gathered (funding events, hiring velocity, tech stack, leadership changes, news), this skill synthesizes those signals into a structured ICP fit-score with rationale, identifies the two highest-urgency pain points specific to this account's current moment, and produces ready-to-send copy for all three outreach channels — email (with two subject line variants), a LinkedIn connection note (character-counted to fit LinkedIn's 300-character limit), and a cold call opener with objection handles. All three channel outputs anchor to the same account-specific hook, making them a coordinated sequence rather than three generic templates.

## When to use it

Invoke before building or launching an outreach sequence for a target account. You should have: the account name, your ICP criteria (firmographics, technographics, and any behavioral signals your ideal customer profile defines), a description of your product or service and its core value proposition, and at least two account-specific signals (a funding event, a job posting pattern, a tech stack indicator, a leadership change, or a piece of recent news). The more signals you provide, the more specific the personalization.

This skill is particularly high-value when:
- An account just raised a round, announced a leadership hire, or posted a cluster of jobs in a function your product supports
- You have an inbound intent signal (content download, pricing page visit, competitor review) and want to craft a warm outbound follow-up
- You are working a named account list at volume and need to personalize without the research bottleneck

## Prompt template

Copy the full prompt below into any AI assistant (Claude, ChatGPT, Gemini, etc.). Fill in all `{PLACEHOLDER}` variables. The more detail you provide in each section, the more specific the outreach copy.

---

```
You are an expert B2B sales strategist working with an SDR or Account Executive.

Your task: synthesize the provided account signals into a structured ICP fit-score and produce a ready-to-send multi-touch outreach brief. Follow the five steps below in order.

---

STEP 1 — SIGNAL INVENTORY
Build a table of every signal provided. For each, record:
- The specific signal (exact fact, not a paraphrase)
- Signal type: FUNDING_EVENT | HIRING_VELOCITY | TECH_STACK_CHANGE | LEADERSHIP_CHANGE | COMPANY_NEWS | INTENT_SIGNAL | COMPETITIVE_SIGNAL | OTHER
- Recency: RECENT (<30 days) | WARM (30–90 days) | AGED (>90 days)

If no signals are provided beyond the account name, add this flag before proceeding:
[REP ACTION REQUIRED: No account signals provided. Outreach personalization will be generic without signal input. Provide at least 2 signals.]

---

STEP 2 — ICP FIT ASSESSMENT
A. Build a Fit Dimensions Table scoring each ICP dimension I provide:
   STRONG FIT | PARTIAL FIT | WEAK FIT | NO DATA — with a one-sentence rationale citing the specific signal or criterion.

B. Score the account on a 5-point scale:
   5 — Priority Tier: all core ICP dimensions match; at least one RECENT or WARM trigger event
   4 — Strong Fit: all core dimensions match; triggers are AGED or absent
   3 — Solid Fit: 75%+ of dimensions match; some gaps
   2 — Partial Fit: 50–74% match; proceed with caution
   1 — Low Fit: <50% match; [REP REVIEW: Confirm ICP criteria before investing in a full sequence]

   State the score and tier. Provide a 2–3 sentence rationale.

C. Identify the single highest-urgency "Why Now" trigger event and explain:
   - What the trigger is
   - Why it creates urgency (what decision or pain it activates)
   - The approximate window of relevance

---

STEP 3 — PAIN POINT IDENTIFICATION
Identify the two highest-relevance pain points for this specific account, ranked by (a) evidential strength and (b) urgency.

For each pain point:
- Name it
- Cite the specific signal(s) that indicate this account is experiencing or about to experience this pain
- Explain why this ranks above other potential pain points given the account's current context
- State in one sentence how the product/service I describe addresses it

Do not list generic category pain points. Every pain point must be anchored to a specific signal.

---

STEP 4 — MULTI-TOUCH OUTREACH BRIEF
Produce coordinated copy for all three channels. All three must share the same personalized hook and pain point framing — this is a sequence, not three independent templates.

TOUCHPOINT 1: EMAIL
Provide two subject line variants (A: curiosity/question-framing; B: direct relevance/trigger-event framing).
Draft the email body with this structure:
  Line 1–2: Personalized first line anchored to the specific trigger event or account signal (not generic)
  Line 3–5: Pain point hook — describe their current problem or the outcome they are missing (no feature lists)
  Line 6–7: Value proposition bridge — one sentence connecting the pain to the product capability
  Line 8–9: Low-friction CTA — offer a specific time or ask a single yes/no question (do not ask for 30 minutes on the first email)

Target: 75–120 words for the body. Flag if over 150 words.

TOUCHPOINT 2: LINKEDIN CONNECTION NOTE
Draft a connection request note of 300 characters or fewer (LinkedIn hard limit).
Include: (1) a specific account-relevant hook in the first sentence, (2) a reason for reaching out now, (3) no sales pitch.
Provide the character count alongside the note.

TOUCHPOINT 3: COLD CALL OPENER
Opening line (2–3 sentences, 20–30 seconds spoken): acknowledge the interruption, establish relevance using the trigger event, end with a permission question — not a pitch.

Also provide:
- "What's this about?" bridge response (2 sentences — value proposition without sounding scripted)
- "Not interested / send me an email" soft close (1 sentence — keeps the door open)

---

STEP 5 — ACCOUNT OUTREACH BRIEF SUMMARY
Produce a CRM-ready one-pager in this exact format:

ACCOUNT OUTREACH BRIEF
======================
Account:          [account name]
Prepared:         [today's date]
ICP Fit Score:    [N/5 — tier label]
Why Now:          [1-sentence trigger event summary]
Primary Pain:     [Pain Point 1 name — 1-sentence description]
Secondary Pain:   [Pain Point 2 name — 1-sentence description]

Recommended Sequence:
  Day 1: Email — [subject line used]
  Day 3: LinkedIn — [first 5 words of the connection note]
  Day 5: Cold Call — [first 5 words of the opener]

Signals used:     [bullet list of signals incorporated into the copy]
Signal gaps:      [any standard ICP signal category not covered — note it]

Rep notes:        [leave blank]

---

GUARDRAILS:
- Do not fabricate account details. If a signal is not provided, do not invent one.
- Do not write pain points not anchored to a provided signal.
- Do not pitch features in the email or LinkedIn note — describe outcomes and pain only.
- Do not exceed 300 characters on the LinkedIn note.
- The three channel outputs must share the same personalized hook — they are a sequence.
- If the fit score is 1, require rep review before completing the outreach brief.

---

MY INPUTS:

## TARGET ACCOUNT
Account name: {ACCOUNT_NAME}
Account website: {ACCOUNT_WEBSITE}
Industry/vertical: {ACCOUNT_INDUSTRY_VERTICAL}
Company size (employees): {EMPLOYEE_COUNT}
Revenue range (if known): {REVENUE_RANGE}
HQ location: {HQ_LOCATION}

## MY ICP CRITERIA
(List each dimension you use to qualify an account as ICP. Include firmographic, technographic, and behavioral criteria.)
{ICP_CRITERIA}

## MY PRODUCT / SERVICE
Product name: {PRODUCT_NAME}
One-sentence description: {PRODUCT_DESCRIPTION}
Core value proposition (the primary outcome you deliver): {VALUE_PROPOSITION}
Primary buyer persona: {PRIMARY_BUYER_PERSONA}

## ACCOUNT SIGNALS
(Paste or describe every signal you have gathered. Include source if known.)

Funding / financial events:
{FUNDING_SIGNALS}

Hiring velocity / job postings:
{HIRING_SIGNALS}

Tech stack indicators (from BuiltWith, G2, LinkedIn, etc.):
{TECH_STACK_SIGNALS}

Leadership changes:
{LEADERSHIP_SIGNALS}

Recent news / press / announcements:
{NEWS_SIGNALS}

Intent signals (if any — pricing page visits, content downloads, competitor reviews, etc.):
{INTENT_SIGNALS}

Other signals:
{OTHER_SIGNALS}

## OUTREACH PREFERENCES (optional)
Preferred tone (conversational / formal / challenger): {TONE_PREFERENCE}
Any competitors to reference or avoid mentioning: {COMPETITOR_CONTEXT}
Sequence architecture preference (default: Email D1 → LinkedIn D3 → Call D5): {SEQUENCE_PREFERENCE}
```

---

## Example output

The following excerpt shows the output style for a representative account. This is a partial example — full output includes all five sections.

---

**SIGNAL INVENTORY**

| Signal | Type | Recency |
|--------|------|---------|
| Raised $55M Series C led by Insight Partners, announced Feb 2026 | FUNDING_EVENT | WARM |
| 14 open roles for "Revenue Operations" and "Sales Enablement" on LinkedIn | HIRING_VELOCITY | RECENT |
| Using Salesforce CRM + Outreach (confirmed via BuiltWith) | TECH_STACK_CHANGE | WARM |
| New CRO (Sarah Nguyen) joined from HubSpot, announced Jan 2026 | LEADERSHIP_CHANGE | WARM |

---

**ICP FIT ASSESSMENT**

Fit Dimensions Table:

| ICP Dimension | Score | Rationale |
|---------------|-------|-----------|
| B2B SaaS, 200–1000 employees | STRONG FIT | 380 employees per LinkedIn; B2B SaaS product confirmed |
| Active RevOps investment | STRONG FIT | 14 open RevOps/Enablement roles — directional hiring signal |
| Salesforce user | STRONG FIT | Confirmed via BuiltWith |
| Recent leadership change in sales function | STRONG FIT | New CRO from HubSpot within last 90 days |
| Series B or later | STRONG FIT | Series C confirmed |

**Overall Fit Score: 5/5 — Priority Tier**
Every core ICP dimension is matched, and the combination of a new CRO and a Series C close within the last 90 days creates a rare dual trigger: a new leader who will reshape the sales stack and fresh capital to fund that rebuild. This account warrants immediate, prioritized outreach.

**Why Now Trigger**: New CRO Sarah Nguyen joined from HubSpot in January 2026. New sales leadership consistently evaluates and replaces incumbent tools in the first 90 days; her HubSpot background suggests familiarity with integrated RevOps stacks and a bias toward platforms that provide pipeline visibility from top-of-funnel through close. The window for getting on her radar before she finalizes a preferred vendor list is approximately 30–60 days.

---

**PAIN POINT IDENTIFICATION**

Pain Point 1: Forecasting Accuracy Under a New CRO
Account-specific evidence: A new CRO will face immediate pressure to produce a credible forecast to present to the board. The Series C close means investors will scrutinize pipeline health aggressively. With 14 open RevOps roles, the current team is understaffed for manual forecast hygiene.
Why this ranks first: The urgency is tied to a specific leadership event with a known timeline; every new CRO needs a defensible forecast within their first quarter.
Value proposition connection: [Product] eliminates manual forecast scrubbing by auto-syncing Salesforce activity data to a live pipeline model, giving a new CRO board-ready accuracy from Day 1.

---

**TOUCHPOINT 1: EMAIL**

Subject A: Quick question about Sarah's first 90-day plan
Subject B: [Company] just closed a Series C — how's the forecast setup looking?

```
Sarah joined from HubSpot, so I'm guessing she already has opinions about what
a clean pipeline looks like — and what it doesn't.

Most new CROs we talk to find the same thing in week two: the Salesforce data
is three calls behind, and rep-updated forecasts are closer to gut feel than
signal. The board doesn't love that conversation, especially post-Series C.

[Product] auto-syncs your sales activity into a live forecast model so Sarah
can walk into her first board meeting with a number she can actually defend.

Worth a 15-minute call this week? I have Thursday at 2pm or Friday at 10am PT.
```
Word count: 106 words.

---

**TOUCHPOINT 2: LINKEDIN NOTE**

```
Congrats on the Series C! Saw Sarah joined as CRO from HubSpot — reached out
because we work with RevOps teams at post-Series B SaaS cos navigating exactly
the forecast stack rebuild she's probably scoping. Happy to share what's worked.
```
Character count: 244 / 300.

---

**TOUCHPOINT 3: COLD CALL OPENER**

Opening line:
"Hi [Name], this is [Rep] from [Company] — I know this is out of the blue. I saw you just brought on Sarah Nguyen as CRO and closed your Series C, and I work with RevOps teams at companies at exactly this stage. Is now a terrible time for literally 30 seconds?"

"What's this about?" bridge:
"We help post-Series C SaaS companies get board-ready forecast accuracy in Salesforce without manual rep hygiene. We're working with a few companies right now going through the same CRO transition you are."

"Not interested / send me an email" soft close:
"No problem at all — I'll send something short. If the timing ever makes sense, I'd love to show you what we've built."

---

## Tips

1. **Lead with your sharpest signal, not your most recent one.** A leadership change + a funding event is more powerful than a job posting cluster alone. If you have a dual trigger, name both in the personalized first line and let the email open with that combination.

2. **The LinkedIn note is a connection request, not a pitch.** If it reads like an email, it will be ignored or declined. The goal is to get connected so you can follow up with direct messages; the note just needs to establish relevance and human credibility. Remove anything that sounds like a product pitch.

3. **Do not wait for perfect signal coverage.** If you have two strong signals, proceed. The skill flags signal gaps explicitly in the Account Outreach Brief Summary so you know what to pursue in discovery. A well-timed outreach with two great signals outperforms a perfectly-researched message sent two weeks late.
