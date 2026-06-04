# CIM Financial Data Extractor

**Industry**: Finance
**Role**: Investment Banking Analyst / Private Equity Associate
**Time saved**: 2–3 hours per CIM (manual extraction typically takes 3+ hours per document)

---

## What it does

Given the text of a Confidential Information Memorandum (CIM) or a set of excerpts from one, this skill extracts a defined list of financial metrics into a structured table — classifying each value by how it was obtained (directly stated, calculated from other figures, estimated, or not found), citing the exact section and page for every value, and flagging conflicts where the same metric appears in multiple places with different figures. The output is a model-ready data sheet an analyst can trust to enter directly into a deal screening model.

---

## When to use it

Use immediately after receiving a CIM and before building or populating a preliminary deal screening or LBO model. Invoke it when you need to:
- Rapidly populate a screening model with LTM/NTM financials, leverage metrics, and valuation comps from a new deal
- Confirm which financial figures in the CIM are directly stated versus require calculation
- Identify data gaps before your first call with the seller's advisor
- Produce a verifiable record of where every model input came from

This skill is not appropriate for post-LOI financial due diligence work requiring forensic-level accounting analysis.

---

## Prompt template

Copy the following prompt into any AI assistant (Claude, GPT-4, etc.). Replace the placeholder variables with your actual content.

---

```
You are assisting an Investment Banking Analyst / PE Associate who is populating a deal screening model from a Confidential Information Memorandum (CIM). Your task is to extract a defined list of financial metrics from the CIM content provided, classify each by data provenance, cite every source, and produce a model-ready extraction table.

## METRICS TO EXTRACT

{TARGET_METRICS}

If TARGET_METRICS is "DEFAULT", extract the following standard deal-screening set:
1. Revenue — LTM (Last Twelve Months)
2. Revenue — NTM (Next Twelve Months, management projection)
3. Revenue CAGR — historical (state the period)
4. Gross Profit — LTM
5. Gross Margin % — LTM
6. EBITDA — LTM (note if management-adjusted or as-reported)
7. EBITDA — NTM (management projection)
8. EBITDA Margin % — LTM
9. Net Debt (Total Debt minus Cash)
10. Total Debt (gross)
11. Cash and Cash Equivalents
12. Interest Expense — LTM
13. Interest Coverage Ratio — LTM (EBITDA / Interest Expense; calculate if not stated)
14. Leverage Ratio — Net Debt / EBITDA
15. CapEx — LTM
16. Free Cash Flow — LTM
17. Equity Ownership Structure
18. Comparable company EV/EBITDA multiples (range and peer set as cited in CIM)

## CIM CONTENT

{CIM_CONTENT}

---

## INSTRUCTIONS

**Step 1 — Document structure scan.**
Before extracting any values, identify which sections of the provided CIM content contain financial data (e.g., Executive Summary, Financial Overview, Management Projections, Debt Schedule, Comparable Company Analysis). Note the section names and any page numbers visible.

**Step 2 — Extract each metric.**
For each metric in the list, search all sections. Do not stop at the first instance — check for the metric appearing in multiple places. Note the exact value, units, period, and location for each instance found.

**Step 3 — Apply the data-provenance taxonomy.**
Classify each extracted metric as exactly one of:
- **Direct**: Value is explicitly stated in the document without calculation.
- **Inferred**: Value derived from two or more directly stated figures using a defined formula. Show the full calculation in the Notes column.
- **Estimated**: Value requires approximation or judgment (e.g., reading a chart, interpolating). Flag prominently.
- **Not Found**: Metric is absent. If mentioned in narrative but not quantified, write "Mentioned, not quantified."

**Step 4 — Detect conflicts.**
If the same metric appears in two or more places with different values, flag both values, their sources, and the discrepancy. Mark Confidence as "Low — Conflict Detected."

**Step 5 — Separate management projections from historical actuals.**
Label every NTM or forward-looking figure "Management Projection" in the Data Provenance field. Label any adjusted figures (stock comp add-backs, owner comp normalization, non-recurring item exclusions) as "Management-Adjusted" with the adjustment basis in the Notes column.

**Step 6 — Produce the extraction table.**

Present the output as a Markdown table with these columns:

| Metric | Value | Units | Period | Data Provenance | Source (Section + Page) | Confidence | Notes |
|--------|-------|-------|--------|-----------------|------------------------|------------|-------|

Confidence levels:
- **High**: Direct extraction from an unambiguous, clearly labeled table
- **Medium**: Direct from narrative text, or Inferred from two High-confidence inputs
- **Low**: Estimated, derived from a Low-confidence input, or conflict detected

**Step 7 — Produce the Model-Readiness Summary.**

After the table, output:

MODEL-READINESS SUMMARY
=======================
Total metrics requested: [N]
Direct extractions:       [N] ([%])
Inferred (calculated):    [N] ([%])
Estimated (judgment):     [N] ([%])
Not Found / Unquantified: [N] ([%])
Conflicts detected:       [N] (metrics: [list])
Management projections:   [N] (require analyst validation before model use)
Management-adjusted figures: [N] (require analyst review of adjustment basis)

ANALYST ACTIONS REQUIRED BEFORE MODEL ENTRY:
1. [specific metric — specific issue]
2. [...]

---

## CONSTRAINTS

- Do NOT fabricate page numbers. If a page is unidentifiable, write "page uncertain."
- Do NOT silently resolve conflicts. Surface every one.
- Do NOT present management projections and historical actuals in the same row without clear labeling.
- Do NOT round values without noting it.
- Every metric in the list must appear in the table, even if its value is "Not Found."
- Management-adjusted EBITDA figures must be flagged for analyst review — they cannot be entered into a model as historical actuals without verification.
```

---

## Example output

The following is a partial example output for a mid-market industrial distribution CIM with LTM revenue of ~$280M and EBITDA of ~$45M.

| Metric | Value | Units | Period | Data Provenance | Source (Section + Page) | Confidence | Notes |
|--------|-------|-------|--------|-----------------|------------------------|------------|-------|
| Revenue — LTM | 281.4 | $M | LTM (FY2023) | Direct | Financial Summary, p. 47 | High | Stated in income statement summary table |
| Revenue — NTM | — | $M | NTM | Mentioned, not quantified | Executive Summary, p. 8 | Low | "expects double-digit growth" stated; no NTM figure tabled |
| EBITDA — LTM | 45.2 | $M | LTM (FY2023) | Direct | Financial Summary, p. 47 | High | Labeled "Adjusted EBITDA"; see Notes |
| EBITDA — LTM | 45.2 | $M | LTM (FY2023) | Direct — Management-Adjusted | Financial Summary, p. 47 | Medium | Excludes $2.1M one-time restructuring; unadjusted EBITDA not separately stated. Requires analyst review before model entry. |
| Interest Coverage Ratio | 5.6x | x | LTM (FY2023) | Inferred | Calculated from p. 47 + p. 62 | Medium | EBITDA $45.2M (p. 47) / Interest Expense $8.1M (p. 62, Debt Schedule). Neither source states the ratio directly. |
| Net Debt | 138.5 | $M | As of 12/31/2023 | Inferred | Calculated from p. 62 | Medium | Total Debt $152.0M minus Cash $13.5M (both Direct, Debt Schedule p. 62) |

**MODEL-READINESS SUMMARY**
Total metrics requested: 18
Direct extractions: 9 (50%)
Inferred (calculated): 4 (22%)
Estimated (judgment): 1 (6%)
Not Found / Unquantified: 4 (22%)
Conflicts detected: 1 (EBITDA — appears at $45.2M on p. 47 and $43.1M on p. 12 Executive Summary)
Management projections: 2
Management-adjusted figures: 1

ANALYST ACTIONS REQUIRED BEFORE MODEL ENTRY:
1. EBITDA — Resolve $45.2M vs. $43.1M conflict between p. 47 and p. 12. Confirm which is model basis.
2. Adjusted EBITDA — Confirm $2.1M restructuring exclusion is defensible as non-recurring before use.
3. NTM Revenue — Not tabled; request projection schedule from advisor before modeling growth.
4. Revenue CAGR — Chart visible on p. 31 but no data label. Estimated at 8–9% from chart axis; request underlying data.

---

## Tips

1. **Paste section by section, not the whole document at once.** For a 250-page CIM, paste the Executive Summary, Financial Overview, Debt Schedule, and Comparable Company Analysis as separate inputs if the full document exceeds the AI's context window. Run the extraction on each section and consolidate.

2. **Specify your model's exact metric names.** Replace `DEFAULT` in `{TARGET_METRICS}` with the exact field names from your screening model template. This prevents the need to re-map output labels to your spreadsheet headers.

3. **Always verify Inferred values manually before entry.** The skill documents every inference chain, but you own the model. Spot-check at least two Inferred values by locating the source pages cited and confirming the inputs. If a cited page number is off, that is your signal to re-run with more CIM context provided.
