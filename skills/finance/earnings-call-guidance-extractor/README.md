# Earnings Call Guidance Extractor

**Industry**: Finance
**Role**: Equity Research Analyst
**Time saved**: ~2–3 hours per transcript pair

## What it does

Given a current earnings call transcript and optionally a prior quarter's transcript, this skill extracts every forward-guidance statement made by management, classifies each by confidence level using a rigorous hedging-language taxonomy, flags quarter-over-quarter tone shifts where the numeric guidance and the linguistic conviction diverge, and produces a structured analyst brief ready for model updates or research notes.

## When to use it

Invoke immediately after downloading a new earnings call transcript, before updating your financial model or drafting a research note. Most useful when you also have the prior quarter's transcript available — the QoQ comparison is where the highest-signal output is produced. Works without the prior transcript too; it will extract and classify from the current quarter alone and flag the missing baseline.

## Prompt template

Copy this prompt in full. Replace `{CURRENT_TRANSCRIPT}` and `{PRIOR_TRANSCRIPT}` with the actual transcript text. If you do not have the prior transcript, delete the prior transcript section and note that in the prompt.

---

```
You are an expert equity research analyst assistant. Your task is to extract forward guidance from an earnings call transcript and produce a structured analyst brief. Follow all steps precisely.

---

## STEP 1 — Separate management statements from analyst questions

Read the full transcript. Identify every speaker by name and title. Classify all speech as either:
- Management statement (company executives or IR lead)
- Analyst question (external sell-side or buy-side analyst)

Only management statements are analyzed in subsequent steps. Do not treat anything said by an external analyst as guidance.

Flag any instance where an analyst's question contains a specific number or range (e.g., "so you're comfortable with $X?") and management responds without explicitly restating or rejecting that number. Label these: [IMPLICIT ACCEPTANCE RISK — management did not restate; analyst assumption may not reflect confirmed guidance].

---

## STEP 2 — Extract all forward-looking statements from management

From management statements only, extract every sentence or passage describing future performance, intent, or expectations. For each statement record:
- Speaker and title
- Direct quote (verbatim — do not paraphrase)
- Subject metric (e.g., "Q1 2025 revenue," "FY2025 gross margin")
- Time horizon
- Stated value or range (numeric if given; directional if not)

---

## STEP 3 — Classify each statement using this hedging-language taxonomy

Assign exactly one classification per statement:

**Confirmed** — Specific numeric range or value, zero linguistic softeners. Language: "our guidance is," "we are raising guidance to," restating a specific range verbatim without qualification.

**Guided (unhedged)** — Directional or range-bound expectation, standard confidence language, no softeners. Language: "we expect," "we anticipate," "we are targeting," "we plan to," "we are comfortable with."

**Guided (hedged)** — Guidance qualified with conditional or uncertainty language. Explicit hedging markers:
- Temporal: "at this point," "as of today," "based on current visibility," "for now"
- Conditional: "assuming," "subject to," "if [condition] continues," "barring," "provided that," "to the extent that," "absent"
- Softening: "approximately," "roughly," "in the neighborhood of," "around," "broadly in line"
- Epistemic: "we believe," "we think," "we remain comfortable" (note: "remain comfortable" hedges against prior confident language)
- Effort: "we are working toward," "we are on track to achieve," "we hope to"
A statement is Guided (hedged) if it contains at least one of these markers in the same sentence or the immediately adjacent sentence modifying the guidance.

**Speculative** — Directional statement, no specific metric, no numeric range, heavy hedging or aspirational language. Language: "we see opportunity in," "we are optimistic about," "over the longer term we believe," "we continue to invest in [X] for future growth."

**Withdrawn / No guidance** — Management explicitly declines to guide a metric previously guided. Language: "we are not providing guidance on [metric] at this time," "we have paused our guidance on."

If a statement straddles two levels, apply the more conservative (lower-conviction) classification and note why.

---

## STEP 4 — QoQ tone comparison

{QOQ_INSTRUCTION}

---

## STEP 5 — Produce the analyst brief in this exact format

```
EARNINGS CALL GUIDANCE BRIEF
=============================
Company:          [from transcript]
Quarter / Period: [from transcript]
Call Date:        [from transcript]
Analyst:          AI-assisted draft — requires analyst review before use in research
QoQ Comparison:   [Available (prior quarter: [period]) | Not available — prior transcript not provided]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 1 — FORWARD GUIDANCE TABLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| # | Metric / Topic | Time Horizon | Current Guidance | Prior Quarter Guidance | Delta | Confidence Level | Direct Quote (verbatim) |
|---|----------------|--------------|------------------|------------------------|-------|-----------------|-------------------------|
| 1 | [metric]       | [period]     | [value/direction]| [value or N/A]         | [Raised/Reiterated/Lowered/N/A] | [classification] | "[exact quote]" — [Speaker, Title] |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 2 — TONE SHIFT FLAGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For each tone divergence detected:

  Metric:            [metric]
  Prior Quarter:     "[prior quote]" — Classification: [level]
  Current Quarter:   "[current quote]" — Classification: [level]
  Numeric delta:     [Raised/Reiterated/Lowered by $X or X%]
  Language shift:    [Specific hedging language added or removed]
  Flag:              [TONE DIVERGENCE: guidance [raised/maintained/lowered] but hedging density [increased/decreased] vs. prior quarter]
  Analyst note:      [One sentence on analytical significance]

If none: "No tone divergences detected — language confidence levels consistent with prior quarter."
If no prior transcript: "[QoQ COMPARISON NOT AVAILABLE — prior quarter transcript was not provided.]"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3 — IMPLICIT ACCEPTANCE RISKS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For each implicit acceptance identified:

  Instance [N]:
  Analyst question: "[analyst quote with embedded assumption]"
  Management response: "[management response]"
  Risk: IMPLICIT ACCEPTANCE RISK — management did not confirm or deny the analyst's assumption.

If none: "None identified."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 4 — ANALYST BRIEF SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Guidance stance:    [Bullish / Cautiously bullish / Neutral / Cautiously bearish / Bearish]
Confirmed items:    [Count and list]
Hedged items:       [Count and list]
Withdrawn items:    [Count and list, or "None"]
Key tone signals:   [2–4 bullet points on most significant language patterns]
Model implications: [2–3 bullet points on what to consider updating — direction and uncertainty, no specific numbers]
Open questions:     [2–3 questions to resolve remaining ambiguity]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 5 — ANALYST NOTES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Unclassifiable items, speaker attribution ambiguities, topics guided last quarter but absent this quarter.]

DRAFT — Verify all direct quotes against source transcript before use in published research.
```

---

## CONSTRAINTS (must follow)

- Do not fabricate quotes. Every entry in the Direct Quote column must be verbatim from the transcript. If wording is unclear, flag it.
- Do not classify analyst statements as guidance. Only named company executives and IR leads.
- Do not silently accept implicit acceptances. Flag every instance in Section 3.
- Do not conflate a numeric raise with a conviction raise. If guidance is raised but surrounded by new hedging language, classify as Guided (hedged).
- Do not produce a single-word sentiment verdict. Output is classification-based.
- Do not omit any forward-looking statement. Capex, headcount, macro assumptions, and product timelines are all forward-looking.
- Do not provide investment advice or buy/sell/hold language.

---

## CURRENT TRANSCRIPT

{CURRENT_TRANSCRIPT}

---

## PRIOR QUARTER TRANSCRIPT

{PRIOR_TRANSCRIPT}

[If no prior transcript: Delete this section and replace Step 4 above with: "No prior transcript provided. Skip QoQ comparison. Include the following notice in Section 2 of the output: [QoQ COMPARISON NOT AVAILABLE — prior quarter transcript was not provided. All classifications are based on current quarter language only.]"]

```

---

## Example output

Below is a representative excerpt from Section 1 and Section 2 for a hypothetical SaaS company:

**Section 1 — Forward Guidance Table (excerpt)**

| # | Metric / Topic | Time Horizon | Current Guidance | Prior Quarter Guidance | Delta | Confidence Level | Direct Quote |
|---|----------------|--------------|------------------|------------------------|-------|-----------------|--------------|
| 1 | Annual Revenue | FY2025 | $480M–$495M | $460M–$480M | Raised | Guided (hedged) | "We are now targeting revenue in the range of $480 to $495 million for the full year, though we'd note this assumes the demand environment we've seen through Q3 continues to hold." — CFO Sarah Chen |
| 2 | Q4 Gross Margin | Q4 2024 | ~72% | 73–74% | Lowered | Guided (hedged) | "Gross margins in Q4 should land around 72%, roughly, depending on the timing of some infrastructure investments we're pulling forward." — CFO Sarah Chen |
| 3 | FY2025 Capex | FY2025 | Not guided | $45–50M | Withdrawn | Withdrawn | "We're not in a position to give specific capex guidance for next year at this point — we'll revisit that on the Q4 call." — CFO Sarah Chen |

**Section 2 — Tone Shift Flags (excerpt)**

```
Metric:            Annual Revenue
Prior Quarter:     "We are raising full-year revenue guidance to $460 to $480 million." — Classification: Confirmed
Current Quarter:   "We are now targeting revenue in the range of $480 to $495 million for the full year, though we'd note this assumes the demand environment we've seen through Q3 continues to hold." — Classification: Guided (hedged)
Numeric delta:     Raised (midpoint +$17.5M)
Language shift:    "though we'd note this assumes the demand environment...continues to hold" — conditional hedge absent in Q3
Flag:              TONE DIVERGENCE: guidance raised but hedging density increased vs. prior quarter
Analyst note:      Management raised the midpoint by $17.5M but introduced a new macro-conditionality clause not present last quarter; the raise is real but conviction has declined, warranting sensitivity analysis on demand softening scenarios.
```

---

## Tips

1. **Always provide both transcripts when you have them.** The QoQ comparison in Section 2 is where the highest-signal output is generated. A raise with new hedging is often more bearish than a reiterate with clean language.

2. **Read Section 3 (Implicit Acceptance Risks) carefully.** Sell-side analysts routinely embed numbers in their questions ("so you're comfortable with $500M?") and management sometimes answers around the number rather than restating it. The Street can treat this as a sanction that management never gave.

3. **Use Section 5 as a checklist.** If a metric was in your model and does not appear in any section of this output, it likely means management deliberately avoided it. Deliberate omission is itself a signal and belongs in your model notes.
