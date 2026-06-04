# Sensitivity Analysis Sub-Workflow

This file governs Phase 3 of the `market-entry-sizing-model-builder` skill. It is invoked after both models are built and reconciled. Do not invoke this workflow before the Phase 2 reconciled outputs exist.

---

## Purpose

Market sizing models have fat tails: a small number of input assumptions drive the vast majority of variance in the final TAM/SAM/SOM figures. The sensitivity analysis identifies which inputs those are, quantifies their impact across a realistic uncertainty range, and tells the client which assumptions they should validate first before committing to a market entry decision.

This analysis does not produce a new TAM estimate. It produces a range, a tornado chart data table, and a prioritized list of assumptions the client must validate.

---

## Step S1 — Identify High-Leverage Inputs

From the finalized base inputs used in both models, extract the full assumption list. Then apply the leverage test to each input: "If this input changes by 20%, how much does the final TAM change?"

**Inputs that are typically high-leverage** (assess first):

| Input | Model | Why High-Leverage |
|-------|-------|-------------------|
| Market penetration rate (`addressable_pct`) | Top-down | Multiplied directly against the full industry TAM; a 5 percentage point change in addressability can move the SAM by hundreds of millions |
| ICP count (total or by segment) | Bottoms-up | The base of the entire bottoms-up calculation; errors here propagate through every segment |
| Average contract value / average deal size | Bottoms-up | Linear multiplier on every ICP in every segment |
| Win rate / conversion rate | Bottoms-up | Typically the most uncertain assumption and one with the widest variation across comparable markets |
| Industry TAM (benchmark figure) | Top-down | Source-dependent; varies by ±15–25% across different benchmark databases for the same market |

**Inputs that are typically low-leverage** (include but do not prioritize):

- Number of segments (affects model granularity but not overall TAM if segment counts sum correctly)
- Revenue breakdown between segments (if total ICP count is sourced correctly)
- Marginal adjustments to addressable geography (<5% change to TAM in most cases)

### S1 Output

Produce a leverage assessment table:

| Input | Base Value | Model | Leverage Classification | Source Confidence |
|-------|-----------|-------|------------------------|-------------------|
| [input name] | [value] | [bottoms-up / top-down / both] | High / Medium / Low | High / Low |

Source confidence is High if the input comes directly from a cited benchmark source in `reference/benchmark-source-guide.md`; Low if it is a consultant estimate, analog market benchmark, or unverified claim.

Select the **3–5 inputs with the highest leverage** for the full sensitivity table. If a high-leverage input has Low source confidence, it automatically becomes the top validation priority regardless of its rank by leverage alone.

---

## Step S2 — Build the Sensitivity Table

For each selected high-leverage input, call `scripts/market_sizer.py`'s `sensitivity_table()` function:

```
sensitivity_table(
    base_inputs=<the full base inputs dict used in the model>,
    variable_name=<the name of the input being varied>,
    range_pct=0.20   # for ±20% scenario
)
```

Run the function twice per input: once at `range_pct=0.20` (±20%) and once at `range_pct=0.40` (±40%).

For each sensitivity scenario, display:

| Input | Scenario | Input Value | TAM | SAM | SOM | % Change vs. Base |
|-------|----------|-------------|-----|-----|-----|-------------------|
| [input] | -40% | [value] | [TAM] | [SAM] | [SOM] | [%] |
| [input] | -20% | [value] | [TAM] | [SAM] | [SOM] | [%] |
| [input] | Base | [value] | [TAM] | [SAM] | [SOM] | 0.0% |
| [input] | +20% | [value] | [TAM] | [SAM] | [SOM] | [%] |
| [input] | +40% | [value] | [TAM] | [SAM] | [SOM] | [%] |

Show full tables before writing any narrative. Do not abbreviate or collapse the table.

---

## Step S3 — Construct the Tornado Chart Data

The tornado chart data table shows, for each high-leverage input, the full TAM swing between the -40% and +40% scenarios. This is the data a consultant would use to build a tornado chart in PowerPoint or Excel.

```
TORNADO CHART DATA — TAM SENSITIVITY
======================================
Base TAM: $[X]M

Input                     | TAM at -40%  | TAM at +40%  | Full Swing  | Swing %
--------------------------|--------------|--------------|-------------|--------
[Input 1 — largest swing] | $[X]M        | $[X]M        | $[X]M       | [X]%
[Input 2]                 | $[X]M        | $[X]M        | $[X]M       | [X]%
[Input 3]                 | $[X]M        | $[X]M        | $[X]M       | [X]%
[Input 4 (if applicable)] | $[X]M        | $[X]M        | $[X]M       | [X]%
[Input 5 (if applicable)] | $[X]M        | $[X]M        | $[X]M       | [X]%
```

Sort rows by Full Swing descending (largest swing at top). This is the standard consulting presentation order.

**Compute the composite uncertainty range**: using the two largest-swing inputs only (not all inputs combined, which would overstate uncertainty by assuming all inputs move simultaneously), state: "Under the two most sensitive input assumptions, the TAM estimate ranges from $[low] to $[high] — a [X]x spread around the base case."

---

## Step S4 — Write the Assumption Sensitivity Narrative

Write 4–6 sentences for the client narrative section. Structure:

**Sentence 1**: State the base TAM and acknowledge it is a point estimate within a wider range.

**Sentence 2**: Name the single input with the largest tornado swing and quantify the TAM impact of the ±40% scenario. Be specific: "A 40% decrease in the addressable percentage assumption (from 35% to 21%) would reduce the TAM from $X to $Y — a $Z reduction."

**Sentence 3**: Name the second-ranked input and its impact.

**Sentence 4**: Identify any inputs with Low source confidence. State: "The [input name] assumption carries low source confidence because [reason]. This is the highest-priority input for the client to validate before committing to a market entry budget."

**Sentence 5**: State whether the model's conclusions are robust or fragile under sensitivity: "Even under the pessimistic (-40%) scenario for both top inputs, the TAM remains above $[floor], which [supports / does not support] the viability of the market entry at the client's stated investment threshold."

**Sentence 6** (if applicable): State any input where the ±40% scenario crosses a business-critical threshold (e.g., TAM drops below the minimum scale required to justify investment). Flag this as a decision risk.

---

## Step S5 — Prioritized Validation Checklist

Produce a checklist of the inputs the client should validate before finalizing the market entry decision. Order by: (1) High-leverage + Low-confidence first; (2) High-leverage + High-confidence second; (3) Low-leverage inputs last.

```
ASSUMPTION VALIDATION PRIORITIES
==================================
[For each input in priority order:]

[ ] PRIORITY [N]: [Input name]
    Current value: [value]
    Source: [source name and date]
    Confidence: [High / Low]
    Validation approach: [How the client should verify this — primary research, database cross-check, pilot test, customer interview, etc.]
    Risk if wrong: [What happens to the market entry recommendation if this input is 40% lower than assumed]
```

Do not list more than 6 validation priorities. If there are more than 6 high-leverage inputs, select the 6 with the largest tornado swings.

---

## Constraints

- Do not run sensitivity on reconciliation narrative assumptions (e.g., the explanation of the gap). Sensitivity applies to numerical model inputs only.
- Do not combine multiple inputs into a "pessimistic scenario" unless the client has explicitly requested a stress scenario. Tornado analysis tests inputs independently.
- Do not present a range narrower than ±20% for any input unless the source citation explicitly states a margin of error below 20%.
- Do not characterize a model as "robust" if the ±40% scenario for any single high-leverage input changes the SOM by more than 60%.
- Do not omit the validation checklist. The purpose of sensitivity analysis in a consulting deliverable is not to quantify uncertainty for its own sake — it is to tell the client what to do next.
- Do not assign High source confidence to an assumption unless it is directly cited from a source in `reference/benchmark-source-guide.md` with a publication date within the last 3 years.
