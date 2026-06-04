---
name: earnings-call-guidance-extractor
description: Given a current earnings call transcript and optionally a prior quarter's transcript, extracts and categorizes every forward-guidance statement by confidence level, flags management tone shifts quarter-over-quarter using an explicit hedging-language taxonomy, and produces a structured analyst brief distinguishing confirmed guidance from hedged or speculative signals — for Equity Research Analysts.
industry: finance
role: Equity Research Analyst
trigger: When an analyst receives a new earnings call transcript and needs to extract forward guidance, detect tone shifts vs. prior quarter, and produce an analyst-ready brief before updating their model or publishing a note
---

## Context

The analyst has just received or downloaded the transcript from a company's most recent earnings call. They may also have the prior quarter's transcript available. Their immediate tasks are:

1. Identify every management statement about future performance — revenue guidance, margin outlook, capex, headcount, product timelines, macro assumptions
2. Classify each statement by how confident management actually is (as opposed to how confident they sound)
3. Detect whether management's language has shifted compared to last quarter — a raise accompanied by newly hedged language is a different signal than a clean raise
4. Produce a structured output they can paste directly into their model notes or research report

The core analytical problem this skill solves: management teams are trained communicators who use deliberate linguistic softeners to protect themselves from guidance misses. A statement like "we remain comfortable with the previously communicated range, subject to the macro environment continuing to cooperate" is legally a reiteration but analytically is a downgrade in conviction. Generic LLM summaries miss this. This skill does not.

The analyst provides the current transcript as the primary input. If they also provide the prior quarter's transcript, the skill performs a QoQ comparison. If only the current transcript is provided, the skill extracts and classifies all forward-looking statements and explicitly flags that no prior-quarter baseline is available.

---

## Instructions

Follow these steps in sequence. Do not merge steps or skip ahead.

### Step 1 — Separate management statements from analyst questions

Read the full transcript provided. Identify every speaker and their role (CEO, CFO, COO, IR lead, sell-side analyst, buy-side analyst). Classify every block of speech as either:

- **Management statement** — spoken by a named company executive or IR lead
- **Analyst question** — spoken by a named external analyst or investor

Only management statements are analyzed in subsequent steps. Do not extract, quote, or classify statements from analyst questions as guidance, even if analysts attempt to characterize or summarize guidance in their questions. Flag any instance where an analyst's question contains a specific number or range that management then implicitly accepts without restating — this is a known pattern that requires explicit analyst attention. Mark it as: **[IMPLICIT ACCEPTANCE RISK — management did not restate; analyst assumption may not reflect confirmed guidance]**.

### Step 2 — Extract all forward-looking statements

From management statements only, identify every sentence or passage that describes future performance, intent, or expectations. A forward-looking statement is any management statement about:

- Financial metrics for a future period (revenue, gross margin, operating income, EBITDA, EPS, FCF, capex, headcount)
- Growth rates, directional trends, or year-over-year comparisons for a future period
- Product launches, market expansion, or strategic milestones with a time horizon
- Macro assumptions that underpin guidance (interest rates, FX, customer demand environment, supply chain)
- Guidance provided as a range, a rate, a ceiling, or a floor
- Statements that reiterate, raise, lower, or withdraw previously communicated guidance

For each extracted statement:
- Record the **speaker** and their **title**
- Record the **direct quote** (verbatim, no paraphrasing)
- Record the **subject metric** (e.g., "Q1 2025 revenue," "FY2025 gross margin," "capex intensity")
- Record the **time horizon** (e.g., "Q1 2025," "full year 2025," "next 12 months," "medium term")
- Record the **stated value or range** (numeric if given; directional if not — e.g., "above prior year," "in line with Q3")

If a statement does not specify a numeric value or range, record the directional language verbatim.

### Step 3 — Apply the hedging-language taxonomy

For each forward-looking statement extracted in Step 2, analyze the surrounding language for hedging markers. Use this taxonomy:

**Confirmed guidance** — Management provides a specific numeric range or value with no linguistic softeners. Language patterns: "our guidance is," "we are raising guidance to," "we now expect [metric] of [specific range]," restating a range verbatim without qualification.

**Guided (unhedged)** — Management provides a directional or range-bound expectation with normal confidence language. Language patterns: "we expect," "we anticipate," "we are targeting," "we plan to," "our outlook is," "we are comfortable with." Note: these are standard guidance verbs and do not alone signal hedging, but they do signal this is expectation rather than fact.

**Guided (hedged)** — Management provides guidance but qualifies it with conditional or uncertainty language. Explicit hedging markers to look for:
- Temporal hedges: "at this point," "as of today," "based on current visibility," "for now"
- Conditional hedges: "assuming," "subject to," "if [macro condition] continues," "barring," "provided that," "to the extent that," "absent"
- Softening hedges: "approximately," "roughly," "in the neighborhood of," "around," "broadly in line"
- Epistemic hedges: "we believe," "we think," "we feel," "we remain comfortable" (note: "remain comfortable" is a frequent softener that hedges against a prior confident statement)
- Effort hedges: "we are working toward," "we are on track to achieve," "we hope to"

A guidance statement qualifies as Guided (hedged) if it contains at least one marker from the above list in the same sentence or the immediately preceding or following sentence that modifies the guidance.

**Speculative** — Management makes a directional statement about the future with no specific metric, no numeric range, and heavy hedging or aspirational language. Language patterns: "we see opportunity in," "we are optimistic about," "over the longer term we believe," "we continue to invest in [X] for future growth," "we are monitoring [condition]."

**Withdrawn / No guidance** — Management explicitly declines to provide guidance for a metric that was previously guided. Look for: "we are not providing guidance on [metric] at this time," "we have paused our guidance on," "we will revisit [metric] guidance when [condition]."

For each statement, assign exactly one classification from this taxonomy. Do not use intermediate labels. If a statement straddles two levels, apply the more conservative (lower-conviction) classification and note why.

### Step 4 — Perform QoQ tone comparison (if prior transcript provided)

If the analyst has provided a prior quarter's transcript, perform a side-by-side comparison for each guidance topic that appears in both transcripts.

For each overlapping metric or topic:

- Extract the **prior quarter's direct quote** and its classification under the taxonomy
- Extract the **current quarter's direct quote** and its classification
- Assess the **delta**: Is this a guidance raise, reiterate, or lower based on numeric values or explicit management language?
- Assess the **language shift**: Has the classification level changed (e.g., Confirmed → Guided (hedged))? Has the hedging density increased even if the numeric range is the same?
- Flag any instance where the numeric guidance has been raised or maintained but the linguistic confidence level has dropped — this is the key analytical signal this skill is designed to detect. Label it: **[TONE DIVERGENCE: guidance [raised/maintained] but hedging density increased vs. prior quarter]**
- Flag any new hedging markers that did not appear in the prior quarter's equivalent statement

If no prior transcript is provided, skip this step and include the following notice in the output: **[QoQ COMPARISON NOT AVAILABLE — prior quarter transcript was not provided. All classifications are based on current quarter language only. Analyst should compare manually against prior transcript.]**

### Step 5 — Produce the analyst brief

Format the complete output as specified in the Output Format section below. Do not omit any section. Do not add narrative commentary outside the defined sections.

---

## Output Format

```
EARNINGS CALL GUIDANCE BRIEF
=============================
Company:          [from transcript]
Quarter / Period: [from transcript, e.g., Q4 2024]
Call Date:        [from transcript]
Analyst:          AI-assisted draft — requires analyst review before use in research
QoQ Comparison:   [Available (prior quarter: [Q3 2024]) | Not available — prior transcript not provided]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 1 — FORWARD GUIDANCE TABLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| # | Metric / Topic     | Time Horizon | Current Guidance (stated value or direction) | Prior Quarter Guidance | Delta            | Confidence Level      | Direct Quote (verbatim)                          |
|---|--------------------|--------------|-----------------------------------------------|------------------------|------------------|-----------------------|--------------------------------------------------|
| 1 | [e.g., Q1 Revenue] | [Q1 2025]    | [$X–$Y million]                               | [$A–$B million]        | [Raised / Reiter / Lowered / N/A] | [Confirmed / Guided (unhedged) / Guided (hedged) / Speculative / Withdrawn] | "[exact management quote]" — [Speaker, Title] |

[Repeat for each forward-looking statement extracted]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 2 — TONE SHIFT FLAGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[If QoQ comparison is available:]

For each flagged tone divergence, provide:

  Metric:            [metric name]
  Prior Quarter:     "[prior quote]" — Classification: [level]
  Current Quarter:   "[current quote]" — Classification: [level]
  Numeric delta:     [Raised / Reiterated / Lowered by $X or X%]
  Language shift:    [Description of specific hedging language added or removed]
  Flag:              [TONE DIVERGENCE: guidance [raised/maintained/lowered] but hedging density [increased/decreased] vs. prior quarter]
  Analyst note:      [One sentence on the analytical significance — e.g., "Management raised the midpoint by $20M but added 'subject to macro environment cooperating,' a qualifier absent in Q3. Delta between numeric raise and linguistic hedge warrants follow-up on macro sensitivity."]

[If no flags: "No tone divergences detected — language confidence levels consistent with prior quarter."]

[If QoQ comparison not available: "[QoQ COMPARISON NOT AVAILABLE]"]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3 — IMPLICIT ACCEPTANCE RISKS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[List any instances where an analyst's question contained a specific number or range and management responded without restating or rejecting it. If none: "None identified."]

  Instance [N]:
  Analyst question: "[analyst quote with embedded assumption]"
  Management response: "[management response — note absence of restatement]"
  Risk: IMPLICIT ACCEPTANCE RISK — management did not confirm or deny the analyst's assumption. Do not treat this as confirmed guidance.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 4 — ANALYST BRIEF SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Guidance stance:   [Bullish / Cautiously bullish / Neutral / Cautiously bearish / Bearish] — based on classification distribution
Confirmed items:   [Count and list metrics with Confirmed classification]
Hedged items:      [Count and list metrics with Guided (hedged) or Speculative classification]
Withdrawn items:   [Count and list any Withdrawn guidance]
Key tone signals:  [2–4 bullet points summarizing the most analytically significant language patterns]
Model implications:[2–3 bullet points on what the analyst should consider updating in their financial model based on the above — do not provide specific numbers, flag the direction and the uncertainty]
Open questions:    [2–3 questions the analyst should ask in follow-up or next quarter's call to resolve ambiguity]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 5 — ANALYST NOTES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Any items that could not be classified with confidence, any ambiguities in speaker attribution, any statements where the management/analyst speaker boundary was unclear, and any guidance topics mentioned in prior quarter but entirely absent from current quarter (may signal deliberate omission).]

DRAFT — This output requires analyst review. Verify all direct quotes against the source transcript before use in published research or client-facing materials.
```

---

## Constraints

- **Do not fabricate quotes.** Every statement in the Direct Quote column must be verbatim from the transcript provided. If the exact wording is unclear due to transcript formatting (e.g., "[inaudible]"), flag it rather than paraphrasing.
- **Do not classify analyst statements as guidance.** Only statements from named company executives and IR leads are eligible for classification. Analyst questions, however leading, are not guidance.
- **Do not silently accept implicit acceptances.** If management fails to restate an analyst's embedded number and the analyst community may treat this as confirmation, flag it explicitly in Section 3. Never classify an implicitly accepted number as Confirmed or Guided.
- **Do not conflate a numeric raise with a conviction raise.** If management raises the midpoint of guidance but surrounds it with new conditional language, the correct classification is Guided (hedged), not Confirmed, regardless of the direction of the numeric change.
- **Do not use a single hedging marker to override an otherwise confident statement.** Common filler phrases like "obviously," "clearly," or "as you know" are not hedges. Apply the taxonomy as defined — look for the specific patterns listed in Step 3.
- **Do not produce a sentiment score or single-word verdict.** The output is a structured classification, not a sentiment rating. Phrases like "management sounded cautious" as a standalone conclusion are not acceptable outputs.
- **Do not omit any forward-looking statement found in the transcript.** Selective extraction that focuses only on headline metrics misses the analytical value. Capex timing, hiring pace, macro assumptions, and product-launch timing are all forward-looking and must be included.
- **Do not assume the prior quarter's transcript covers the same topics.** Some metrics are guided quarterly, some annually, some only when analysts ask. Note any metric guided in the prior quarter that does not appear in the current quarter — deliberate omission is itself a signal.
- **Do not provide investment advice or recommendations.** The output informs the analyst's judgment; it does not replace it. The brief must not contain buy/sell/hold language or price targets.
- **If no prior transcript is provided, flag this clearly** at the top of the output and in Section 2. Do not invent prior quarter language or make assumptions about what management said in prior periods.
