# Competitive Battlecard Builder

**Industry**: Technology
**Role**: Product Marketing Manager
**Time saved**: 6–12 hours per competitor (vs. 8–16 hours manual synthesis from raw sources)

---

## What it does

Given a competitor name, your product's positioning statement, and raw source materials (competitor website excerpts, G2/TrustRadius/Capterra review quotes, and sales call notes or win/loss fragments), this skill synthesizes a fully structured two-page sales battlecard. The output is organized into seven named sections — Competitor Snapshot, Why They Win, Why They Lose, Landmines to Listen For, Trap-Setting Questions, Objection Handlers, and a Win Theme — formatted for immediate use by AEs and SDRs in a competitive deal.

The skill performs the synthesis and formatting layer that sits above raw competitive intelligence data: deciding which weaknesses are deal-relevant, which rebuttals are credible based on your stated capabilities, and how to structure output for rep usability in a live call.

---

## When to use it

Use this skill when you have gathered raw source materials for one specific competitor and need to produce a rep-ready battlecard without spending a full day on manual synthesis. Typical trigger: you have pulled the competitor's positioning page, grabbed 10–20 G2 review quotes, and have win/loss notes or Gong/Chorus fragments from 3–5 competitive deals, and you need a structured card that the sales team can adopt without further editing.

Not designed for: market landscape overviews comparing multiple competitors, general SWOT analyses, or situations where you have no source material to ground the output.

---

## Prompt template

Copy the full prompt below. Replace every `{PLACEHOLDER}` with your actual content before submitting.

---

You are a Product Marketing Manager building a sales battlecard for a specific competitor. Your goal is to synthesize raw source materials into a fully structured, rep-ready battlecard that an Account Executive or SDR can use live in a competitive deal.

**Competitor name**: {COMPETITOR_NAME}

**Your product name**: {YOUR_PRODUCT_NAME}

**Your product positioning statement** (include your named capability pillars and differentiation claims — this is the ONLY source for rebuttal capabilities; do not invent capabilities not listed here):

{YOUR_POSITIONING_STATEMENT}

---

**SOURCE MATERIAL — Competitor Website Excerpts**
(paste text from competitor's homepage, product pages, or pricing page)

{COMPETITOR_WEBSITE_EXCERPTS}

---

**SOURCE MATERIAL — Customer Review Quotes**
(paste verbatim quotes from G2, TrustRadius, Capterra, or similar; include the source and date if available; aim for 10–20 quotes minimum for strong output)

{REVIEW_QUOTES}

---

**SOURCE MATERIAL — Sales Call Notes / Win-Loss Data**
(paste Gong/Chorus transcript fragments, CRM loss reason notes, or PMM win/loss interview summaries for deals where this competitor was involved)

{SALES_CALL_NOTES}

---

Now produce a battlecard with the following exact sections. Do not add, remove, or rename sections.

**Section 1 — Competitor Snapshot**
A table with: core positioning claim (verbatim if available), ICP target, top 3 named differentiators they claim, and pricing model. If any field cannot be determined from the source material, write: [NEEDS MORE DATA: recommended source].

**Section 2 — Why They Win**
2–3 specific situations where this competitor typically wins: deal type, buyer profile, or use case. Derive only from the sales call notes or win/loss data provided. If insufficient signal exists, flag: [NEEDS MORE DATA: recommended source — CRM win/loss data, loss reason fields].

**Section 3 — Why They Lose**
Top 3 weaknesses validated by customer reviews. For each: name the weakness category, note how many reviews cite it (e.g., "cited in 7 of 12 reviews"), and include one verbatim quote from the provided source material. If fewer than 3 weaknesses are clearly supported by evidence, flag the gap.

**Section 4 — Landmines to Listen For**
4–6 specific phrases a prospect might say that signal competitor influence. Each must:
- Be traceable to this competitor's specific positioning or differentiator claims (not generic)
- Include a one-line coaching note: what the phrase signals and how the rep should respond
Generic phrases like "they asked about integrations" or "they mentioned pricing" are NOT acceptable — be specific to this competitor.

**Section 5 — Trap-Setting Questions**
3–4 open-ended discovery questions that surface competitor weaknesses without naming the competitor. Each question must:
- Target a specific weakness from Section 3 (label which weakness it targets)
- Contain no competitor name or direct reference to the weakness
- Surface information the rep can use to reframe the evaluation

**Section 6 — Objection Handlers**
For each of the competitor's top 3 named differentiators: state the claim as a prospect might voice it, then write a rebuttal anchored to a specific capability named in {YOUR_PRODUCT_NAME}'s positioning statement. Use a "Yes, and" or reframe structure — not a denial. If no matching capability exists in the positioning statement, write: [GAP: no counter available from stated positioning — recommend PMM review before publishing].

**Section 7 — Win Theme**
One sentence the AE can use to reframe the competitive conversation. It must reference a specific weakness or win pattern from the source material. Avoid superlatives and marketing language.

**Data Gaps section**
List any sections where source material was insufficient, with recommended sources. Omit this section if all sections are fully supported.

---

## Example output

Below is an abbreviated example showing the expected format for a CRM software battlecard. Your actual output will be based entirely on the source materials you provide.

---

# Battlecard: Pipedrive
**Prepared for**: Salesforce Sales Cloud sales team
**Last updated**: 2026-06-04
**Source confidence**: Medium (12 G2 reviews, 4 loss call summaries, competitor pricing page)

## 1. Competitor Snapshot

| Field | Detail |
|---|---|
| Core positioning claim | "The CRM designed to keep salespeople selling" |
| ICP target | SMB sales teams, 10–200 employees, deal-volume-driven orgs |
| Named differentiators | 1. Pipeline visualization / 2. Minimal admin overhead / 3. Fast onboarding (< 1 day) |
| Pricing model | Per-seat, $14.90–$99/seat/mo, no enterprise tier |

## 2. Why They Win

1. SMB net-new deals where the buyer has rejected Salesforce as "too complex for our team size"
2. Cost-sensitive ops buyers with fixed per-seat budget below $30/seat
3. Replacement deals where the current CRM requires heavy admin to maintain

## 3. Why They Lose

| Weakness | Frequency | Representative Quote |
|---|---|---|
| Reporting depth | Cited in 8 of 12 reviews | "The reporting is fine for pipeline status but the moment you want anything custom you're exporting to Excel" |
| Native integration gaps | Cited in 6 of 12 reviews | "We had to pay for Zapier to connect it to our support desk — should be built in" |
| Enterprise scalability | Cited in 5 of 12 reviews | "Works great at 15 reps but we hit walls when we got to 80 and added territories" |

## 4. Landmines to Listen For

| What the prospect says | What it signals | How to respond |
|---|---|---|
| "We just need something simple — we're not Salesforce-sized" | Pipedrive pitched simplicity as primary value; prospect may be anchoring on admin overhead | Acknowledge, then ask who owns their rev ops function and what reports their VP of Sales runs weekly |
| "We looked at your price and it's just too much per seat" | Pipedrive's per-seat pricing at $15–30 has been used as anchor; prospect hasn't scoped total cost of integration and admin | Ask about their current integration spend and how they handle reporting today |

## 5. Trap-Setting Questions

1. **"Walk me through how your team builds a monthly forecast today — what data goes into it and who touches it?"**
   *Targets*: Reporting depth weakness — cited in 8 of 12 reviews

2. **"When a new integration comes up — say your support desk or billing system — how does your team handle connecting it to your CRM?"**
   *Targets*: Native integration gaps — cited in 6 of 12 reviews

## 6. Objection Handlers

### Claim 1: "They said their setup is done in a day — your implementation takes months"
**Rebuttal**: "Fast setup is real for a 10-rep team with standard pipeline stages. The question is whether that setup still works when you add territories, custom objects, or multi-currency. Our guided implementation includes a revenue ops configuration review that Pipedrive's self-serve model doesn't include — which is why 73% of our customers expand their instance within 12 months rather than re-platforming."
*Capability cited*: Guided implementation with revenue ops configuration review

## 7. Win Theme

"The question isn't whether setup is fast today — it's whether the tool grows without a re-platform when your team doubles."

---

## Tips

1. **Volume of review quotes matters.** For Section 3 (Why They Lose) and Sections 4–5 to be specific, aim for at least 10–15 distinct review quotes. Fewer than 8 quotes will produce a generic or gap-flagged output in those sections.

2. **Your positioning statement drives rebuttal quality.** The skill will only write rebuttals for capabilities explicitly named in your positioning statement. If your positioning statement is vague ("we're the leading platform for X"), the objection handlers will be vague. Include named features, named integrations, and specific performance or compliance claims.

3. **Flag gaps rather than expanding source material on the fly.** If the output shows [NEEDS MORE DATA] in multiple sections, that is the expected behavior — the skill will not fabricate. Use those flags as a targeted list of what to research next before the battlecard goes to the sales team.
