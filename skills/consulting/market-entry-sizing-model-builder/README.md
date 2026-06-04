# Market Entry Sizing Model Builder

**Industry**: Consulting
**Role**: Strategy Consultant / Business Analyst
**Time saved**: 6–12 hours per market (vs. manual dual-method construction across 4–6 databases with independent reconciliation)

---

## What it does

Given a target market description, industry statistics inputs from named benchmark sources, and a client ICP profile, this skill constructs both a bottoms-up sizing model (ICP count × price × conversion) and a parallel top-down model (industry TAM through SAM/SOM penetration), calculates TAM/SAM/SOM at each level, identifies and explains the reconciliation gap between methods, flags the highest-sensitivity assumptions, and produces a slide-ready market sizing exhibit with a source-cited assumptions table.

The output is consulting-deliverable quality: two independent estimates, a defended reconciliation, and a sensitivity section that tells the client which assumptions to validate first.

---

## When to use it

Use this skill when you have:
1. A defined ICP (customer type, size, geography, qualifying criteria)
2. An ICP count from at least one named source (Census County Business Patterns, FDIC SDI, Definitive Healthcare, etc.)
3. A benchmark TAM figure from at least one named industry source (IBISWorld, IDC, Gartner, CMS, etc.)
4. Average deal size or ACV (from pricing research, comparable deals, or client estimate)
5. A win rate assumption (from comparable market analogs or client's pipeline data)

Do not use this skill if you have only one of the two required inputs (ICP count OR benchmark TAM but not both). A single-method model is not a triangulated sizing.

---

## Prompt template

Copy and fill in the variables below. Replace everything in `{CURLY BRACES}`.

---

You are a strategy consultant building the market entry sizing section of a client deliverable. I need you to construct a dual-method market sizing analysis — both a bottoms-up model and a top-down model — then reconcile the two estimates and flag the highest-sensitivity assumptions.

**Target market**: {One to three sentences describing the product or service, the buyer, and the target geography. Example: "B2B SaaS platform for IT service management (ITSM), targeting mid-market US companies with 100–1,000 employees that currently use email and spreadsheets for IT ticket management."}

**Industry sector for benchmark source selection**: {One of: SaaS/Enterprise Software | Healthcare/MedTech | Financial Services | Manufacturing/Industrial | Retail/Consumer | Professional Services}

---

### Bottoms-Up Inputs

**ICP definition**: {Specific description of the qualifying customer: company size, industry, technology qualification, or other screening criteria}

**Segments** (provide one row per segment, or a single row if not segmenting):

| Segment Name | ICP Count | ICP Count Source | Avg Deal Size (ACV) | Win Rate |
|---|---|---|---|---|
| {Segment 1 name} | {count} | {source: database name, NAICS code, and year} | ${amount} | {%} |
| {Segment 2 name, if applicable} | {count} | {source} | ${amount} | {%} |

**Win rate basis**: {Where does the win rate assumption come from? Example: "Comparable ITSM vendor win rates from Gartner ITSM Market Guide 2024" or "Client's own sales pipeline conversion data Q1–Q3 2025"}

---

### Top-Down Inputs

**Industry TAM source**: {Source name, report title, NAICS/SIC code, publication year, and stated market size. Example: "IDC Software Tracker 2024, ITSM category, North America: $4.5B"}

**Addressable percentage (SAM/TAM)**: {What fraction of the industry TAM is addressable by this client's offer? State the percentage AND the rationale. Example: "35% — IDC segments the ITSM market by company size; mid-market (100–1,000 employees) represents 35% of total ITSM spending per IDC 2024"}

**Capturable percentage (SOM/SAM)**: {What fraction of the SAM is realistically capturable in years 1–3? State the percentage AND the rationale. Example: "2.5% — based on comparable SaaS entrant trajectories in adjacent categories (HR tech, DevOps tooling)"}

---

### Conflicting sources (if applicable)

{If you have two sources with different TAM figures, list both here:}
- Source 1: {name, TAM figure}
- Source 2: {name, TAM figure}
- Likely reason for discrepancy: {your hypothesis}

---

### Instructions

1. **Build the bottoms-up model**: For each segment, calculate TAM (ICP count × avg deal size), SAM (full segment TAM since all ICPs are pre-qualified), and SOM (SAM × win rate). Show the segment-by-segment table. Aggregate to total bottoms-up TAM/SAM/SOM.

2. **Build the top-down model**: Apply the two-step penetration cascade (TAM → SAM via addressable_pct → SOM via capturable_pct). Show each step with the source and rationale for each percentage.

3. **Reconcile**: Calculate the gap between bottoms-up TAM and top-down TAM. Classify the gap as Aligned (<20%), Material Divergence (20–50%), or Inconsistent (>50%). Identify the 2–3 most likely explanations for the gap based on the inputs provided. State which estimate is the more reliable planning figure for this market type and why.

4. **Sensitivity analysis**: Identify the 3–5 inputs with the highest leverage on the TAM result. For each, show what happens to TAM (and SOM) if the input is 40% lower and 40% higher than the base case. Construct a tornado chart data table sorted by full swing (largest swing at top). Write 4–6 sentences identifying: the most impactful assumption, the second-most impactful, any assumptions with low source confidence that the client should validate first, and whether the model's market entry conclusion is robust under the pessimistic scenario.

5. **Produce the final exhibit**: Output in this order:
   - Section 1: Market Sizing Exhibit (TAM/SAM/SOM table — Bottoms-Up | Top-Down)
   - Section 2: Bottoms-Up Model Detail (segment table)
   - Section 3: Top-Down Model Detail (penetration cascade with source per step)
   - Section 4: Reconciliation Analysis (gap, explanation, recommended planning figure)
   - Section 5: Assumption Sensitivity Analysis (tornado table + narrative)
   - Section 6: Source-Cited Assumptions Table (all assumptions with source and confidence level)

**Constraints**:
- Do not produce a single-method estimate. Both models are required.
- Every ICP count must trace to a named source. Flag any without a source as [SOURCE REQUIRED].
- Do not blend the two estimates without explaining the reconciliation.
- Do not present a confidence range narrower than the cited sources' margin of error.
- Label the output: "AI-assisted draft — requires lead consultant review before client delivery."

---

## Example output

Below is a representative excerpt for a B2B SaaS product entering the mid-market ITSM space.

---

**MARKET SIZING EXHIBIT — MID-MARKET ITSM SAAS (US)**

| Metric | Bottoms-Up | Top-Down |
|--------|-----------|---------|
| TAM    | $1.05B    | $4.50B  |
| SAM    | $1.05B    | $1.58B  |
| SOM    | $105M     | $39M    |

Gap: 329% — INCONSISTENT. Top-down TAM significantly exceeds bottoms-up.

**Likely explanation**: The bottoms-up model counts 42,000 mid-market US companies using manual IT ticketing (NAICS 518210 + 541512, CBP 2022, filtered to 100–1,000 employees). IDC's $4.5B ITSM TAM includes enterprise (1,000+ employees, ~50% of market), global revenue, and adjacent categories (monitoring, asset management) beyond pure service desk software. The bottoms-up model is more accurate for this client's specific offer scope.

**Recommended planning figure**: Bottoms-up ($1.05B TAM, $105M SOM). Top-down serves as a ceiling sanity check.

**Sensitivity — Top 2 inputs by swing**:

| Input | -40% SOM | Base SOM | +40% SOM | Full Swing |
|-------|---------|---------|---------|-----------|
| ICP count (42K accounts) | $63M | $105M | $147M | $84M |
| Avg deal size ($25K ACV) | $63M | $105M | $147M | $84M |

*The ICP count and average deal size assumptions carry equal leverage on the SOM. ICP count is sourced from Census CBP 2022 (high confidence). Average deal size is a consultant estimate (low confidence) — this is the highest-priority validation item before finalizing the market entry recommendation.*

---

## Tips

1. **Source the ICP count rigorously.** The ICP count is usually the single most-impactful assumption in the bottoms-up model. Use US Census County Business Patterns (CBP) for manufacturing and B2B markets, FDIC SDI for banking institutions, or Definitive Healthcare for health plans and hospitals. Avoid sourcing the ICP count from "market research" TAM reports — those are top-down estimates, not account counts.

2. **The reconciliation gap is a signal, not a problem.** A large gap (>50%) usually means the two methods are measuring different things (different geographies, different customer types, different revenue categories). Diagnosing the gap is the most analytically valuable part of the market sizing — it tells the client exactly which assumptions are in dispute.

3. **Win rate is almost always low-confidence.** Unless the client has their own pipeline conversion data, win rates are estimates from analogous markets. Always flag the win rate as low-confidence in the assumptions table and include it in the sensitivity analysis — it is typically the second-highest-leverage assumption after ICP count.
