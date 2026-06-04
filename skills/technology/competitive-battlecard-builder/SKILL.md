---
name: competitive-battlecard-builder
description: Synthesizes competitor website excerpts, G2/TrustRadius review quotes, and sales call notes into a fully structured two-page sales battlecard for a Product Marketing Manager, with named sections covering positioning snapshot, landmines, trap-setting questions, and per-claim objection handlers anchored to the user's product capabilities.
industry: technology
role: Product Marketing Manager
trigger: When a PMM has gathered raw source materials for a specific competitor (positioning page copy, review site quotes, win/loss notes or Gong/Chorus fragments) and needs to synthesize them into a rep-ready battlecard for a competitive deal, without spending 8–16 hours on manual synthesis.
---

## Context

The practitioner is a Product Marketing Manager who owns competitive intelligence for their product line. They have already gathered raw source materials for one competitor — excerpts from the competitor's website positioning page, quotes pulled from G2/Capterra/TrustRadius, fragments from sales call notes or Gong/Chorus transcripts, and possibly a pricing page excerpt. They have their own product's positioning statement and named capability pillars in hand.

They need to produce a battlecard that an Account Executive or SDR can read in under five minutes and use live in a competitive deal — not a research document, not a SWOT grid, but a structured one-to-two-page card organized around the specific moments of competitive friction in a discovery or evaluation call.

The practitioner invokes this skill after raw research is collected and before the battlecard is formatted for Seismic, Highspot, Notion, or a shared Google Doc for the sales team.

---

## Instructions

Follow these steps in order. Do not combine steps or skip sections.

### Step 1 — Extract Competitor Positioning

Read the competitor website excerpts and identify:
- Their single core positioning claim (the one-sentence "who we are for") — pull verbatim language if available
- Their named ICP: the buyer profile, company size, vertical, or use case they claim to serve
- Their top 3 named differentiators — the specific capability or experience claims they lead with (e.g., "fastest implementation," "deepest enterprise integrations," "only platform with X")
- Their pricing model, if source materials include it (per-seat, usage-based, flat-rate, custom enterprise)

If any of these four items cannot be determined from the provided sources, output: `[NEEDS MORE DATA: recommended source — competitor pricing page / product page / G2 profile]`

Do not infer or fabricate positioning claims not present in the source material.

### Step 2 — Identify Customer-Validated Weaknesses

Read all G2/Capterra/TrustRadius review quotes provided. For each recurring weakness theme:
- Name the weakness category (e.g., "implementation complexity," "customer support responsiveness," "reporting depth")
- Count how many distinct review quotes cite this theme — express as a frequency indicator (e.g., "cited in 7 of 12 reviews")
- Pull one verbatim quote that best illustrates the weakness — it must be from the source material, not invented

Select the top 3 weaknesses by frequency. If fewer than 3 weaknesses are clearly supported by review evidence, note the gap: `[NEEDS MORE DATA: insufficient review volume — recommend pulling additional TrustRadius reviews for this category]`

### Step 3 — Identify Win Patterns

Read the sales call notes, win/loss summaries, or Gong/Chorus fragments provided. Extract 2–3 patterns describing the situations where the competitor typically wins:
- Deal type or sales motion (e.g., "net-new SMB below 200 employees," "replacement deals where buyer is already in their ecosystem")
- Buyer profile or champion type (e.g., "IT-led evaluation," "cost-conscious ops buyer")
- Use case or feature set that drove the win

If source materials contain insufficient win/loss signal, output: `[NEEDS MORE DATA: recommended source — sales call recordings, CRM opportunity data tagged with competitor, loss reason fields]`

### Step 4 — Map Competitor Strengths to Rebuttals

For each of the competitor's top 3 named differentiators (from Step 1), write one objection handler:
- State the competitor's claim as a prospect might voice it (e.g., "They said they have native Salesforce integration")
- Write a rebuttal that references a specific capability from the user's product positioning statement — name the capability explicitly
- The rebuttal must be a "Yes, and" or "That's true for X, but consider Y" structure — not a denial
- The rebuttal must NOT claim capabilities not stated in the user's positioning statement; if no matching capability exists, flag: `[GAP: no counter available from stated positioning — recommend PMM review before publishing]`

### Step 5 — Generate Landmines

Write 4–6 landmine phrases: specific words or concerns a prospect says in a discovery or evaluation call that signal competitor influence. Each landmine must:
- Reflect language pattern derived from the competitor's positioning, differentiator claims, or review themes in the source material
- Be specific enough that a rep can recognize it live without coaching (do NOT write generic phrases like "they mentioned pricing" or "they asked about integrations")
- Include a one-line coaching note: what the phrase signals and how the rep should respond

Example of a passing landmine: `"We need to keep our data in our own environment" → signals they were shown [Competitor]'s on-prem or private cloud offering; pivot to [Your Product]'s data residency controls and SOC 2 Type II coverage`

Example of a failing landmine: `"They mentioned scalability" → generic, not specific to this competitor`

### Step 6 — Generate Trap-Setting Questions

Write 3–4 discovery questions that expose competitor weaknesses without naming the competitor. Each question must:
- Target a specific weakness identified in Step 2 (map each question to its source weakness)
- Be open-ended and non-leading (no competitor name, no reference to the weakness directly)
- Surface information the rep can use to reframe the evaluation in their favor

Example of a passing question: `"Walk me through what your team does today when a customer support ticket requires escalation — who touches it, and how long does that process take?" [Targets: support responsiveness weakness, cited in 7/12 reviews]`

Example of a failing question: `"Do you find their support slow?" — names the issue directly, eliminates the diagnostic value`

### Step 7 — Write the Win Theme

Write a single sentence the AE can use to reframe the competitive conversation — not as a boast about your product, but as a reframe of how the evaluation should be structured. It should:
- Reference one specific weakness or win pattern identified in the source material
- Give the rep a frame they can return to throughout the discovery call
- Avoid marketing language (no superlatives, no vague claims)

---

## Output Format

Produce the battlecard using the following exact section structure. Use markdown headers. Do not add, remove, or rename sections.

---

# Battlecard: [Competitor Name]
**Prepared for**: [User's Product Name] sales team
**Last updated**: [today's date]
**Source confidence**: [High / Medium / Low — based on volume and recency of source materials provided]

---

## 1. Competitor Snapshot

| Field | Detail |
|---|---|
| Core positioning claim | [verbatim or paraphrased from source] |
| ICP target | [buyer profile, company size, vertical] |
| Named differentiators | 1. [claim] / 2. [claim] / 3. [claim] |
| Pricing model | [per-seat / usage-based / flat-rate / custom / NEEDS MORE DATA] |

---

## 2. Why They Win

Situations where this competitor typically wins a competitive deal:

1. [Deal type / buyer profile / use case — derived from win/loss sources]
2. [Deal type / buyer profile / use case]
3. [Deal type / buyer profile / use case — or NEEDS MORE DATA if insufficient signal]

---

## 3. Why They Lose

Top weaknesses validated by customer reviews:

| Weakness | Frequency | Representative Quote |
|---|---|---|
| [category] | Cited in X of Y reviews | "[verbatim quote from source]" |
| [category] | Cited in X of Y reviews | "[verbatim quote from source]" |
| [category] | Cited in X of Y reviews | "[verbatim quote from source]" |

---

## 4. Landmines to Listen For

Phrases in prospect conversations that signal competitor influence:

| What the prospect says | What it signals | How to respond |
|---|---|---|
| "[specific phrase]" | [competitor tactic or feature being referenced] | [one-line rep coaching note] |
| "[specific phrase]" | [competitor tactic or feature being referenced] | [one-line rep coaching note] |
| "[specific phrase]" | [competitor tactic or feature being referenced] | [one-line rep coaching note] |
| "[specific phrase]" | [competitor tactic or feature being referenced] | [one-line rep coaching note] |

*(Add rows 5–6 if additional landmines are supported by source material)*

---

## 5. Trap-Setting Questions

Discovery questions that surface competitor weaknesses without naming them:

1. **[Question text]**
   *Targets*: [weakness from Section 3] — [frequency indicator]

2. **[Question text]**
   *Targets*: [weakness from Section 3] — [frequency indicator]

3. **[Question text]**
   *Targets*: [weakness from Section 3] — [frequency indicator]

*(Add question 4 if supported)*

---

## 6. Objection Handlers

When the prospect raises a competitor strength claim:

### Claim 1: "[Competitor's differentiator claim as prospect might voice it]"
**Rebuttal**: [Yes-and or reframe response anchored to named user product capability]
*Capability cited*: [exact capability name from user's positioning statement]

### Claim 2: "[Competitor's differentiator claim as prospect might voice it]"
**Rebuttal**: [Yes-and or reframe response anchored to named user product capability]
*Capability cited*: [exact capability name from user's positioning statement]

### Claim 3: "[Competitor's differentiator claim as prospect might voice it]"
**Rebuttal**: [Yes-and or reframe response anchored to named user product capability]
*Capability cited*: [exact capability name from user's positioning statement]

---

## 7. Win Theme

*One sentence the AE uses to reframe the competitive conversation:*

"[Win theme sentence]"

---

## Data Gaps

List any sections where source material was insufficient:

- [Section name]: [NEEDS MORE DATA — recommended source]

*(Omit this section entirely if all sections are fully supported)*

---

## Constraints

- Do NOT fabricate competitor claims not present in the provided source material. If a competitor's differentiator is not stated in the sources, omit it or flag it as needing confirmation.
- Do NOT claim product capabilities in rebuttals that are not present in the user's positioning statement. Every rebuttal must cite its source capability by name. If no matching capability exists, flag the gap explicitly.
- Do NOT write generic landmines. A landmine that could apply to any competitor (e.g., "they mentioned price") is a failure mode. Every landmine must be traceable to this specific competitor's positioning or differentiation claims.
- Do NOT embed competitor names in trap-setting questions. Questions that name the competitor destroy their diagnostic value in a live call.
- Do NOT produce a market overview or industry comparison. This is a single-competitor, single-product battlecard for live deal use.
- Do NOT invent win/loss patterns. All "Why They Win" entries must be derived from the sales call notes or win/loss data in the source materials. If evidence is insufficient, use the NEEDS MORE DATA flag.
- Do NOT exceed the defined section structure. Do not add sections, merge sections, or reorder sections — the format is standardized for sales team adoption.
- If source materials are thin on any dimension, flag it clearly rather than padding output. A gap-flagged battlecard is more useful than a fabricated one.
