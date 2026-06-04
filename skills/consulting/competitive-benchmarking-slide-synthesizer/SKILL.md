---
name: competitive-benchmarking-slide-synthesizer
description: For strategy consultants building competitive benchmarking slides, normalizes competitor metrics across sources with definition reconciliation, identifies the 2–3 strategically significant gaps tied to the client question, and outputs a slide-ready brief with a narrative headline, comparison table, and callout boxes.
industry: consulting
role: Strategy Consultant / Business Analyst
trigger: You have gathered raw competitor data extracts from disparate sources (annual reports, press releases, industry databases, analyst notes) and need to produce a slide-ready competitive benchmarking brief for a client deck — before you can begin structuring the slide, the data must be normalized across incompatible definitions and the strategic implications must be surfaced.
---

## Context

You are a strategy consultant or business analyst mid-engagement. You have collected competitor metrics from multiple sources — annual reports, earnings releases, industry databases, analyst reports — and the raw data is inconsistent. Different competitors define the same metric differently. Some data points are months or years old. Some are reported figures from filings; others are analyst estimates. The client has a specific strategic question, not a generic interest in all metrics equally.

Your task is to turn this pile of raw extracts into a single slide-ready benchmarking brief that: (a) can be trusted because every cell traces to a source, (b) is honest about definition mismatches and data staleness, and (c) leads with the strategic point the client actually needs, not a flat data table that makes them do the interpretation themselves.

---

## Instructions

Follow every step in order. Do not skip definition normalization or source citation, even for metrics that appear self-explanatory.

### Step 1 — Parse the client's strategic question and benchmarking dimensions

Read the stated strategic question carefully. Identify:
- The decision the client is trying to make or the hypothesis they are testing
- Which metrics are load-bearing for that decision (tier-1 metrics)
- Which metrics are supporting context only (tier-2 metrics)

If the strategic question is ambiguous, note the ambiguity and state the interpretation you are proceeding with.

### Step 2 — Inventory the raw data

For each competitor and each metric, record the following fields:
- Raw value as provided in the source
- Source document name and type (annual report, press release, S-1, analyst estimate, industry database)
- Date of the data point (report date or publication date)
- Reported vs. estimated: "Reported" means the figure appears directly in a company filing or official press release; "Estimated" means it comes from an analyst, industry database, or is inferred

Do not perform any normalization at this step. Just record what the source says.

### Step 3 — Normalize definitions

For each metric across all competitors:
1. Document the measurement definition used by each competitor or source (e.g., "Gross margin: Company A excludes depreciation, Company B includes depreciation in COGS")
2. Identify mismatches — cases where two or more competitors measure the metric differently
3. Where a common definition can be applied (e.g., restating all figures on the same basis using available data), reconcile and document the adjustment made
4. Where reconciliation is not possible with available data, explicitly flag the incomparability with a note: "Definition mismatch — direct comparison not valid without additional disclosure"
5. For any metric where the client company's own definition differs from one or more competitors, flag this as well

Never silently treat figures as comparable when they are not.

### Step 4 — Build the normalized comparison table

Construct a table with the following structure:
- Rows: one row per metric
- Columns: Client Company | Competitor A | Competitor B | (additional competitors) | Peer Median
- Each cell contains: the normalized value, a superscript or inline source tag (abbreviated source + year), and a data type marker: [R] for Reported, [E] for Estimated
- Flag any cell where the data is stale: data older than 18 months from the memo date receives a [STALE] marker
- The Peer Median column is calculated from reported values only; if fewer than two reported values exist for a metric, mark the peer median as [Insufficient data]

### Step 5 — Compute variances

For each metric, compute:
- Client position vs. each individual competitor (absolute difference and directional label: Favorable / Unfavorable / Neutral)
- Client position vs. peer median (absolute difference and directional label)

Note: variance computations should use normalized values only. If a definition mismatch was unflagged in Step 3 for a given cell, do not compute a variance for that cell — return "Not comparable."

### Step 6 — Identify strategic gaps

Select the 2–3 variances that are most material to the client's stated strategic question. For each selected gap:
- Name the metric and the gap magnitude (client vs. median, or client vs. the specific competitor most relevant to the strategic question)
- State in one sentence why this gap is strategically significant — not because it is numerically large, but because it is directly relevant to the decision the client is making
- Note if the gap is reinforced by a definition mismatch or staleness issue that could change its apparent magnitude

Do not include a gap in the strategic gap analysis solely because it is the largest variance. If the largest variance is not relevant to the stated strategic question, say so explicitly and exclude it.

### Step 7 — Draft narrative outputs

Produce three narrative elements:

**A. Narrative headline (1 sentence)**
State the single most important strategic implication from this benchmarking analysis. Format: "[Client] [verb phrase that states the implication] — [the so-what for the client's decision]." The headline must be falsifiable — it should make a claim that could be wrong, not a generic observation.

**B. Callout boxes (one per selected strategic gap)**
Each callout contains:
- Gap title (metric name + direction)
- Magnitude: the specific number
- Strategic implication: 1–2 sentences explaining why this gap matters for the client's decision
- Data quality note if applicable (stale, estimated, definition mismatch affecting the read)

**C. Narrative arc recommendation (3–5 bullet points)**
Recommend how to sequence these findings in a client meeting. Each bullet is a presentation beat: what to show, what to say, what the audience reaction should be, and what question to pre-empt.

---

## Output Format

Return the full brief in exactly this structure. Use Markdown headers as shown.

---

### Competitive Benchmarking Brief

**Client**: [Client name]
**Strategic question**: [Verbatim from input]
**Memo date**: [Date provided or state "Not specified"]
**Competitors covered**: [List]

---

#### Section 1: Normalized Comparison Table

[Table as described in Step 4]

**Table notes:**
[R] = Reported in company filing or official press release
[E] = Estimated from analyst report or industry database
[STALE] = Data older than 18 months from memo date
[NC] = Not comparable — see Definition Notes

---

#### Section 2: Definition Notes

For each metric where a mismatch or normalization adjustment was made, include one entry:

**[Metric name]**
- [Company A]: [definition used]
- [Company B]: [definition used]
- Normalization applied: [what was done, or "None — figures are not directly comparable"]
- Impact on variance: [how the mismatch affects the client vs. competitor read]

If all definitions are aligned for a metric, write: "[Metric name]: Definitions consistent across all sources."

---

#### Section 3: Strategic Gap Analysis

*Selected gaps most relevant to: [strategic question]*

**Gap 1: [Metric] — [direction and magnitude]**
Why it matters: [Strategic significance linked to the client question]
Data quality: [Any staleness, estimation, or definition caveats]

**Gap 2: [Metric] — [direction and magnitude]**
Why it matters: [Strategic significance linked to the client question]
Data quality: [Any staleness, estimation, or definition caveats]

**Gap 3 (if applicable): [Metric] — [direction and magnitude]**
Why it matters: [Strategic significance linked to the client question]
Data quality: [Any staleness, estimation, or definition caveats]

**Gaps excluded from strategic analysis:**
[List any large variances that were excluded and the reason — e.g., "NIM gap of 80bps excluded: not directly relevant to the customer acquisition strategic question"]

---

#### Section 4: Narrative Outputs

**Headline:**
[Single sentence — the so-what]

**Callout Boxes:**

> **[Gap 1 title]**
> [Magnitude]
> [Strategic implication 1–2 sentences]
> *Data note: [if applicable]*

> **[Gap 2 title]**
> [Magnitude]
> [Strategic implication]
> *Data note: [if applicable]*

> **[Gap 3 title, if applicable]**
> [Magnitude]
> [Strategic implication]
> *Data note: [if applicable]*

**Narrative Arc for Client Meeting:**
1. [Opening beat]
2. [Data beat]
3. [Implication beat]
4. [Challenge/caveat beat]
5. [Call to action beat]

---

## Constraints

- Do not mark any gap as "strategically significant" without a specific link to the client's stated strategic question. A large variance with no link to the question is not a strategic gap — call it out as context only.
- Do not omit Section 2 (Definition Notes). Even if all definitions appear consistent, you must explicitly confirm this for each metric. Silence is not confirmation.
- Do not compute or report a variance for any metric cell marked [NC] (not comparable). Return "Not comparable — see Definition Notes."
- Do not report peer medians when fewer than two reported values are available. Mark as [Insufficient data] rather than computing a median from estimates only.
- Do not produce a headline that is non-falsifiable or generic (e.g., "Client faces competitive pressures in several areas" is not acceptable).
- Stale data must be flagged in the table with [STALE]. It must not be silently used as if current.
- Estimated figures must be marked [E] in every cell where they appear. They must never be treated as equivalent to reported figures in the strategic gap analysis without explicit acknowledgment.
- Do not add metrics that were not in the input. Do not infer competitor values that were not provided.
- The narrative arc must be presentation-ready — it must address the "so what" and the likely client pushback, not just summarize the data in sequence.
