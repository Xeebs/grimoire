---
name: market-entry-sizing-model-builder
description: For strategy consultants and business analysts: given a target market description, industry statistics inputs from named benchmark sources, and a client ICP profile, constructs a bottoms-up sizing model and a parallel top-down model, calculates TAM/SAM/SOM at each level, identifies and explains the reconciliation gap between methods, flags high-sensitivity assumptions, and produces a slide-ready market sizing exhibit with a source-cited assumptions table.
industry: consulting
role: Strategy Consultant / Business Analyst
trigger: When building the market entry sizing section of a client deliverable — after the ICP definition is agreed and benchmark data has been pulled from 2+ industry statistics sources, before writing the sizing narrative — when the consultant must produce a defensible dual-method estimate with reconciliation rather than a single back-of-envelope figure.
---

## Context

You are a strategy consultant building the market sizing section of a client deliverable. The client has defined a target market and ICP. You have pulled benchmark data from 2–4 industry statistics sources (IBISWorld, BLS, Statista, Census, or sector-specific databases). You need to produce:

1. A **bottoms-up model** — built from the ICP count up through price and volume assumptions by segment
2. A **parallel top-down model** — built down from an industry TAM through SAM and SOM penetration rates
3. A **reconciliation analysis** — computing the gap between methods, explaining its most likely sources, and telling the client which estimate to rely on for decision-making
4. A **sensitivity analysis** — identifying which assumptions most affect the TAM range (invoke `SENSITIVITY-ANALYSIS.md`)
5. A **slide-ready exhibit** — TAM/SAM/SOM table with source-cited assumptions for the appendix

This skill executes the full workflow across three phases. Do not merge phases. The Python script handles all arithmetic — use `scripts/market_sizer.py` for calculations so outputs are reproducible. Use `reference/benchmark-source-guide.md` to validate source credibility ratings before citing any benchmark in a client deliverable.

---

## Sub-Files — Load on Demand

| File | Phase | Load When |
|------|-------|-----------|
| `reference/benchmark-source-guide.md` | Phase 1 | When validating benchmark sources and their margin-of-error characteristics |
| `scripts/market_sizer.py` | Phase 1 & 2 | When performing bottoms-up calculations, top-down penetration, or reconciliation math |
| `SENSITIVITY-ANALYSIS.md` | Phase 3 | When running the assumption sensitivity test before finalizing the narrative |

Load each file when its phase begins. Do not load all files at the start.

---

## Phase 1 — Build Both Models

**Load**: `reference/benchmark-source-guide.md` and `scripts/market_sizer.py`

### Step 1.1 — Parse and validate inputs

Collect and confirm all required inputs before proceeding. If any required field is missing, stop and request it.

**Required inputs:**

*Target market:*
- Market description (1–3 sentences: what product/service, for whom, in which geography)
- Primary industry sector (for benchmark source selection in `reference/benchmark-source-guide.md`)

*ICP profile (for bottoms-up):*
- ICP definition: the specific customer type being targeted (company size, industry, technology stack, or other qualifying criteria)
- ICP segment list: if the model has multiple segments (e.g., mid-market vs. enterprise), each segment must have:
  - `segment_name`
  - `icp_count` — number of qualifying accounts (must come from a named source)
  - `avg_deal_size` — average contract value or transaction size in USD
  - `win_rate` — realistic conversion rate from addressable account to customer (as a decimal, e.g., 0.12 for 12%)
- ICP count source (database, survey, or calculation method used)

*Benchmark data (for top-down):*
- `total_market_size` — industry TAM in USD from a named source (e.g., "IBISWorld SIC 7372: $48.2B")
- `addressable_pct` — fraction of the total market that matches the client's offer characteristics (as a decimal)
- `capturable_pct` — realistic market share achievable in the planning horizon (as a decimal)
- Source name, publication date, and NAICS/SIC code for each statistic cited

### Step 1.2 — Validate benchmark sources

Cross-reference each provided benchmark source against `reference/benchmark-source-guide.md`:

1. Identify which sector category applies (SaaS/Enterprise Software, Healthcare/MedTech, Financial Services, Manufacturing/Industrial, Retail/Consumer, Professional Services, or Other)
2. Note the typical margin-of-error range for the cited source
3. Flag any source not in the reference guide with: `[SOURCE NOT IN REFERENCE: confirm reliability before citing in deliverable]`
4. If two sources provide conflicting TAM figures, apply the following decision tree **before** considering the midpoint rule:

   **Scope check (run first, before business unit classification):**
   - When two sources have a gap > 50%, first determine whether the discrepancy is driven by scope rather than business-unit type. A scope mismatch exists when one source covers a broad universe (all functions, all payers, all industries, all subsectors) while the other is scoped narrowly to the specific product category or function.
   - To detect a scope mismatch: compute `gap_pct = abs(source_a - source_b) / max(source_a, source_b)`. If `gap_pct > 50%`, inspect whether the larger source's scope description is 5x or more broader than the smaller source's scope description. If yes, this is a scope mismatch — see the scope mismatch rule below.
   - **Scope mismatch rule**: SELECT the narrowly scoped source. Reject the broader source with documentation: `[SOURCE REJECTED: [source name] measures [broader scope description] — scope is [N]x broader than the target product category; not directly applicable as a product TAM without additional scoping adjustments. Replaced by [narrow source name] which is scoped to [specific product category].]`
   - **Healthcare sector mandatory enforcement**: If the healthcare sector is selected AND CMS NHEA is one of the provided sources, MANDATORY REJECTION of CMS NHEA regardless of gap size, with the annotation: `[CMS NHEA REJECTED: CMS NHEA measures total health insurance administrative cost across all payer types and functions — scope is 10–20x broader than any single product-category TAM. See benchmark-source-guide.md Healthcare section. Select a cost estimate scoped to the target product category (McKinsey Health Systems Practice, KLAS Research, Advisory Board).]`

   **Business unit mismatch check (run after scope check):**
   - Inspect what each remaining source is actually measuring. A source is measuring a **cost base** (not a revenue market) if its figure is denominated in terms like "total costs," "total spending," "administrative costs," "total expenditure," or "total cost base." A source is measuring a **software/product revenue market** if its figure is denominated in terms like "software market revenue," "product market size," "license fees," "software spend," or "SaaS market."
   - If one source measures a cost base and the other measures software/product revenue, they are measuring **different business units**. Before rejecting either source, compute `gap_pct = abs(source_a - source_b) / max(source_a, source_b)`:
     - **If gap_pct < 20%**: The two sources converge despite measuring different business units. Present BOTH sources. Label the cost-base source as "cost-displacement methodology, included as convergence validation." Use the midpoint as the operative TAM. Record in the Step 2.3 methodology analysis that convergence across independent methodologies increases confidence in the estimate.
     - **If gap_pct is 20–50%**: The sources diverge and measure different things. Select the source whose measurement unit matches the client's revenue model (if the client sells software licenses, use the software-revenue-denominated source; if the client captures a share of cost savings, use the cost-base source as a ceiling). Document the non-selected source explicitly: `[SOURCE NOT USED AS TAM: [source name] measures [cost base / software revenue] — not matched to client revenue model; noted as [value-ceiling reference / context only].]`
     - **If gap_pct > 50%**: Return to the scope check above — a gap this large between two different business-unit types almost always indicates a scope mismatch in addition to a methodology difference. Apply the scope mismatch rule first.
   - If both sources measure the same business unit type (e.g., both are software revenue market figures, or both are cost-base figures) but report different estimates — and no scope mismatch was found — then apply the midpoint rule from the reference guide and document the range.

### Step 1.3 — Build the bottoms-up model

Using `scripts/market_sizer.py`, call:

```
bottoms_up(
    icp_count=<total ICP count or use segments>,
    avg_deal_size=<ACV in USD>,
    win_rate=<conversion rate as decimal>,
    segments=<list of segment dicts with name/icp_count/avg_deal_size/win_rate>
)
```

Show the full segment-by-segment calculation table before presenting aggregates. For each segment, display:
- Segment name
- ICP count (with source)
- Average deal size
- Win rate
- TAM contribution (icp_count × avg_deal_size)
- SAM contribution (TAM × addressability factor if segment-specific)
- SOM contribution (SAM × win_rate)

Display the return dict: `tam`, `sam`, `som`, and `segment_breakdown`.

### Step 1.4 — Build the top-down model

Using `scripts/market_sizer.py`, call:

```
top_down(
    total_market_size=<industry TAM in USD>,
    addressable_pct=<SAM / TAM fraction>,
    capturable_pct=<SOM / SAM fraction>
)
```

For each penetration step, state:
- The source and rationale for the penetration percentage
- Whether the percentage is derived from: (a) a cited benchmark, (b) a comparable market analog, or (c) a consultant judgment estimate
- If (c), flag it as a low-confidence input

Display the return dict: `tam`, `sam`, `som`.

### Step 1.5 — Format the initial exhibit

Call `scripts/market_sizer.py`'s `format_exhibit()` with the outputs from Steps 1.3 and 1.4 to generate the slide-ready TAM/SAM/SOM comparison table. This is the preliminary exhibit before reconciliation adjustments.

---

## Phase 2 — Reconcile

**Load**: `scripts/market_sizer.py` (already loaded)

### Step 2.1 — Compute the reconciliation gap

Call:

```
reconcile(
    bottoms_up_tam=<bottoms-up TAM from Phase 1>,
    top_down_tam=<top-down TAM from Phase 1>
)
```

The function returns: `gap_pct`, `gap_direction`, `likely_explanation`.

Display these values exactly as returned before writing any narrative.

### Step 2.2 — Diagnose the gap

Using the `gap_direction` and `gap_pct`, apply this diagnostic logic:

**If bottoms-up > top-down (bottoms-up higher)**:
The most likely explanations are:
- ICP count is overstated (the source definition of qualifying accounts is broader than the true serviceable universe)
- Win rate assumption is too aggressive (check against comparable markets in `reference/benchmark-source-guide.md`)
- Average deal size includes upsell/expansion revenue not represented in the first-year ACV
- The industry TAM source is conservative or uses an older market definition

**If top-down > bottoms-up (top-down higher)**:
The most likely explanations are:
- Bottoms-up undercounts the ICP universe (segment list is not exhaustive)
- The `addressable_pct` is too high (client's offer does not serve all of the SAM)
- The bottoms-up model excludes whitespace accounts or channel-driven sales
- The industry TAM includes revenue types not relevant to the client's specific offer

**If gap < 20%**: The methods are substantially aligned. Present both estimates. Recommend using the bottoms-up as the planning figure and the top-down as the sanity check.

**If gap is 20–50%**: The methods diverge materially. Identify the 2–3 most likely assumption drivers. Present a reconciled midpoint with explicit caveats. Do not blend without explanation.

**If gap > 50%**: The methods are inconsistent. One estimate is likely using a flawed assumption. Do not present a blended figure. Instead, present both estimates separately and state which the consultant recommends relying on and why.

### Step 2.3 — Draft the reconciliation narrative

Before writing any prose, complete the following methodology analysis. This analysis determines which explanatory logic to apply and must be recorded in the deliverable before the narrative paragraph.

**Methodology analysis (complete before drafting):**

1. Identify the top-down TAM's measurement type:
   - Is the top-down TAM source a **cost-displacement model** (i.e., it measures total cost of a function, administrative spending, or cost base that the product reduces or replaces)?
   - Or is it a **software-license-revenue model** (i.e., it measures total software market revenue, product market size, or license fees actually paid)?
   - State this explicitly: `Top-down source type: [cost-displacement / software-license-revenue]`

2. Identify the bottoms-up model's measurement type. Bottoms-up models using ICP count × ACV are always **software-license-revenue** models.

3. Apply the correct narrative logic based on the combination:
   - **Both models use software-license-revenue**: The gap reflects assumption differences (ICP count, win rate, addressable fraction). Explain the gap using the standard direction-based diagnostics from Step 2.2. Recommend the estimate with the better-sourced assumptions as the planning figure.
   - **Top-down uses cost-displacement, bottoms-up uses software-license-revenue (ICP × ACV), AND the two TAM figures converged (gap_pct < 20% as determined in Step 1.2)**: The two sources used independent methodologies but arrived at similar figures. State explicitly: "Two independent methodologies — [Source A's method, e.g., cost-displacement] and [Source B's method, e.g., software-license-revenue] — yield TAM estimates of [A] and [B], a convergence that increases confidence in the [midpoint] estimate. When independent methodological approaches align, the estimate is more robust than either method alone." Use the midpoint as the operative TAM. Recommend the bottoms-up figure for GTM planning and capacity modeling, the cost-displacement figure for investor context.
   - **Top-down uses cost-displacement, bottoms-up uses software-license-revenue (ICP × ACV), AND the two TAM figures diverged (gap_pct ≥ 20%)**: The two models are measuring structurally different things and a gap of any size is expected. Do NOT treat this as a data quality failure. State explicitly: "The top-down figure represents a ceiling on total addressable value (the cost pool available to be displaced); the bottoms-up figure represents the addressable software revenue opportunity (units × ACV). These are not directly comparable." Recommend the bottoms-up figure for GTM planning and capacity modeling. Recommend the top-down cost-displacement figure for investor context and total value framing.

Then write the reconciliation narrative in consulting deliverable style (3–5 sentences):

1. State both estimates and the gap size
2. Apply the explanation derived from the methodology analysis above (not generic gap-direction logic if the models measure different things)
3. State which estimate is more reliable for this market type (use `reference/benchmark-source-guide.md`'s guidance on when to prefer top-down vs. bottoms-up)
4. State the recommended planning figure and the confidence range

### Step 2.4 — Produce the final exhibit and assumptions table

Call `format_exhibit()` and `assumptions_table()` with the fully reconciled outputs. The assumptions table must include:
- Every assumption used in both models
- The source citation for each assumption
- Whether the assumption is high-confidence (directly sourced) or low-confidence (estimated/benchmarked)

---

## Phase 3 — Sensitivity Analysis

**Load**: `SENSITIVITY-ANALYSIS.md`

Follow the full sensitivity analysis workflow defined in `SENSITIVITY-ANALYSIS.md`:

1. Identify the 3–5 inputs with highest leverage on the TAM result
2. Build ±20% and ±40% sensitivity ranges for each input
3. Construct the tornado chart data table
4. Write the assumption sensitivity narrative
5. Distinguish high-confidence vs. low-confidence inputs by source quality

Append the sensitivity analysis output to the final deliverable as a dedicated section after the main exhibit.

---

## Output Format

The final deliverable contains four sections in this order:

```
MARKET SIZING ANALYSIS
======================
[Market name and client context]
[Methodology: Dual-method triangulation (bottoms-up + top-down)]
[Prepared: AI-assisted draft — requires review by lead consultant before client delivery]

SECTION 1 — MARKET SIZING EXHIBIT
  [TAM/SAM/SOM table: Bottoms-Up | Top-Down | Reconciled]
  [Source citations inline]

SECTION 2 — BOTTOMS-UP MODEL DETAIL
  [Segment-by-segment calculation table]
  [ICP count sources]

SECTION 3 — TOP-DOWN MODEL DETAIL
  [Penetration cascade with source and rationale per step]

SECTION 4 — RECONCILIATION ANALYSIS
  [Gap computation]
  [Reconciliation narrative]
  [Recommended planning figure with confidence range]

SECTION 5 — ASSUMPTION SENSITIVITY ANALYSIS
  [Tornado chart data table]
  [Sensitivity narrative]
  [High-priority validation inputs for client]

SECTION 6 — SOURCE-CITED ASSUMPTIONS TABLE
  [All assumptions with source, citation date, and confidence level]
```

---

## Constraints

- Do not produce a single-method estimate. Both models must be built and reconciled — a market sizing that shows only TAM without a second independent estimate is not a consulting-grade deliverable.
- Do not invent ICP counts. Every account count must trace to a named source. If the practitioner provides no source for an ICP count, flag it as `[SOURCE REQUIRED: this assumption has the highest sensitivity to TAM — see Sensitivity Analysis]`.
- Do not blend the two estimates without explaining the reconciliation. A blended average that is not explained is worse than picking one estimate and owning it.
- Do not present a confidence range narrower than the cited sources' margin of error. If IBISWorld reports ±20% margin of error for the sector, the TAM range must span at least ±20%.
- Do not perform market sizing calculations in prose. All calculations must be routed through `scripts/market_sizer.py` functions and displayed with inputs, formula, and output — not embedded as "the market is approximately $X."
- Do not use "addressable market" and "serviceable market" interchangeably. TAM = total industry, SAM = addressable by client's offer, SOM = capturable given resources and timeline.
- Do not cite a benchmark source without checking it against `reference/benchmark-source-guide.md`. Sources not in the guide must be flagged for consultant review before deliverable submission.
- Do not produce the sensitivity analysis before the main models are complete and reconciled. Sensitivity runs on finalized base inputs only.
- Label the output as a draft. The header must state this is an AI-assisted draft requiring lead consultant review before client delivery.
