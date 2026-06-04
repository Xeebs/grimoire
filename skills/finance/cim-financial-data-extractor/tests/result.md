# Quality Audit — cim-financial-data-extractor

**Audited**: 2026-06-03
**Auditor**: quality-auditor subagent
**Overall result**: PASS

---

## Scenario 1: Mid-Market Industrial Distribution — Halpern Distribution Services

| # | Criterion | Result | Notes |
|---|-----------|--------|-------|
| 1 | All 18 default metrics present in table | ✓ | All 18 rows present; Free Cash Flow and EBITDA NTM correctly marked "Not Found" with explanations, not omitted. |
| 2 | Revenue LTM extracted as $281.4M (Direct, Financial Summary p. 45-49); conflict with Executive Summary "approx. $280M" flagged | ✓ | Correctly extracted $281.4M from audited Financial Summary table. Conflict explicitly flagged between Executive Summary approximation (unaudited) and Financial Summary exact figure; recommendation to use Financial Summary for modeling. |
| 3 | EBITDA LTM as two rows: $41.6M (as-reported, Direct) and $43.9M (Management-Adjusted, Direct); adjustment basis noted | ✓ | Both rows present. Adjusted entry labeled "Management-Adjusted." All three adjustment components itemized with dollar amounts: restructuring $2.1M, founder comp $0.8M, PPP reversal -$0.9M. |
| 4 | Revenue NTM classified as "Mentioned, not quantified" (not Direct or Inferred) | ✓ | Correctly classified. Executive Summary "double-digit growth" noted but no NTM figure quantified or entered. |
| 5 | Interest Coverage Ratio classified as Inferred with reasoning chain; notes CIM references Lender Presentation for stated ratio | ✓ | Classified Inferred with both calculations (5.1x as-reported, 5.4x adjusted). Critical flag: CIM explicitly states ratio is in Lender Presentation; analyst instructed to obtain it rather than rely solely on calculated figure. |
| 6 | Net Debt classified as Inferred ($152.0M - $13.5M = $138.5M); both inputs cited as Direct | ✓ | Correctly classified Inferred. Calculation transparent; both inputs cited from Debt Schedule p. 60-64 with Direct provenance. |
| 7 | Leverage Ratio classified as Inferred; shows both adjusted (3.15x) and as-reported (3.33x) calculations | ✓ | Both calculations present. Analyst flagged to confirm which EBITDA basis to use for the model (adjusted vs. as-reported). |
| 8 | Revenue CAGR classified as Inferred; calculated from FY2021–FY2023 with period and math documented | ✓ | Calculated 12.1% CAGR over two years (FY2021 $224.1M → FY2023 $278.3M). Documentation complete. |
| 9 | EBITDA NTM classified as "Not Found"; no forward EBITDA in excerpts | ✓ | Marked "Not Found" with explanation; not omitted or estimated. |
| 10 | Ownership structure captures breakdown: Family 68%, Management 24.8%, Other 7.2%; Class B liquidation preference noted | ✓ | Breakdown accurate (Family Trust 62.4% + Harold Halpern 5.6% = 68%). Class B 1.25x liquidation preference documented. |
| 11 | Comparable company EV/EBITDA multiples recorded as Direct; range, mean, median, and peer names captured | ✓ | Range 8.9x–12.6x, Mean 10.4x, Median 10.1x. All five peers named. Source p. 94-99 cited. High confidence appropriate. |
| 12 | Conflict between Executive Summary approx. figures and Financial Summary exact figures flagged | ✓ | Conflict explicitly noted. Recommendation to use audited Financial Summary as model input. |
| 13 | Management-adjusted EBITDA flagged for analyst review; adjustment components itemized | ✓ | Explicitly flagged for analyst review. All three adjustments itemized with amounts. |
| 14 | Model-Readiness Summary present with accurate counts | ✓ | Summary present and accurate: 11 Direct, 4 Inferred, 0 Estimated, 3 Not Found, 1 Conflict, 0 Management Projections, 2 Management-Adjusted. |
| 15 | ANALYST ACTIONS lists: (1) resolve conflict, (2) obtain Lender Presentation, (3) validate adjustments, (4) request NTM projections, (5) confirm PPP treatment | ✓ | All five required actions listed with specificity. Additional context provided for each action. |

**Scenario 1 result**: PASS

---

## Scenario 2: B2B SaaS — Nexora Analytics, Inc.

| # | Criterion | Result | Notes |
|---|-----------|--------|-------|
| 1 | All 27 metrics (18 default + 9 custom SaaS) present in table | ✓ | All 27 rows present. Free Cash Flow and Equity Ownership correctly marked "Not Found." Leverage Ratio marked "N/A — net cash position." No silent omissions. |
| 2 | ARR extracted as $62.3M (Direct, p. 4-11); discrepancy from annualized MRR $61.0M flagged; $1.3M difference explained | ✓ | Correctly extracted $62.3M as contractually committed ARR. Discrepancy with MRR explicitly noted and attributed to multi-year prepayments. Both figures marked Direct; analyst actions flag need for clarification. |
| 3 | MRR extracted as $5,087K / $5.087M (Direct, p. 29-34); ending MRR as of 6/30/23 | ✓ | Correctly extracted from MRR-to-ARR reconciliation as ending MRR. Source cited. |
| 4 | Revenue LTM correctly extracted as $55.4M (GAAP, Direct, p. 51-58); distinguished from ARR; not conflated | ✓ | Revenue and ARR kept separate. GAAP basis explicitly noted for revenue. No confusion between the two metrics. |
| 5 | EBITDA LTM as two rows: GAAP -$3.2M (Direct) and Adjusted $7.2M (Direct — Management-Adjusted); both present | ✓ | Both rows present. Negative GAAP figure clearly shown; Adjusted labeled "Management-Adjusted." |
| 6 | Adjusted EBITDA flagged as Management-Adjusted; SBC ($10.4M) noted as real economic cost per CIM footnote; buyer should assess SBC run-rate | ✓ | Explicitly flagged. CIM's own footnote (p. 57) warning about SBC real cost is cited directly. Notes recommend buyer validate SBC sustainability. |
| 7 | Rule of 40 Score extracted as 54 (Direct, p. 4-11); decomposed as 41% ARR growth + 13% Adjusted EBITDA margin; non-GAAP basis noted | ✓ | Correctly decomposed: 41% + 13% = 54. **Critical note**: Using GAAP margin (-5.8%) would yield 35.2%, significantly different. Analyst explicitly alerted to non-GAAP basis. |
| 8 | NRR extracted as 118% (Direct); same figure confirmed across sections; no conflict; High confidence | ✓ | Extracted as 118% with both sources (Executive Summary, SaaS Metrics Bridge) cited. Consistency across sections noted. |
| 9 | GRR extracted as 94% (Direct, p. 29-34) | ✓ | Correctly extracted. |
| 10 | Logo Churn Rate extracted as 6.3% (Direct, p. 29-34) | ✓ | Correctly extracted and verified from source data. |
| 11 | CAC Payback Period extracted as "approximately 18 months" (Direct, p. 29-34); Medium confidence flagged because underlying S&M/ACV inputs in p. 78-82 (not provided) | ✓ | Correctly extracted as stated. Confidence appropriately marked Medium. Analyst actions flag need to obtain p. 78-82 for verification. |
| 12 | Revenue NTM extracted as $74.0M (Direct — Management Projection, p. 103-108); labeled as projection requiring validation | ✓ | Correctly extracted and labeled. Medium confidence appropriate for management projection. |
| 13 | EBITDA NTM extracted as $14.8M (Direct — Management Projection, excl. SBC, p. 103-108); double-flagged as projection and management-adjusted | ✓ | Correctly extracted. Both projection and SBC-exclusion flags present. Analyst review required before model entry. |
| 14 | Net Debt correctly recorded as negative (-$15.3M), indicating net cash; not positive $15.3M | ✓ | Correctly calculated and signed. Net cash position explicitly stated. No sign error. |
| 15 | Interest Coverage Ratio classified as Inferred; shows both bases: Adjusted 8.0x and GAAP -3.6x; notes GAAP negative is economically relevant; analyst must choose basis | ✓ | Both calculations transparent. GAAP negative result highlighted. Low confidence marked due to conflict. Notes recommend considering GAAP basis for conservatism. |
| 16 | Comps correctly noted as EV/Revenue (not EV/EBITDA); EV/EBITDA recorded as "Not applicable"; EV/Revenue ranges captured | ✓ | Correctly reflects CIM's explicit statement that EV/EBITDA not presented for pre-profitability peers. Alternative multiples captured (EV/NTM Revenue 4.8x–10.2x, EV/LTM Revenue 5.8x–11.8x). Peer names listed. |
| 17 | Revenue CAGR (historical) classified as Inferred; calculated ≈50% CAGR FY2021–FY2023; Notes flag ARR CAGR (41%) is more standard SaaS metric | ✓ | Correctly calculated: ($55.4M / $24.6M)^(1/2) - 1 ≈ 50%. Notes appropriately alert analyst that ARR CAGR is standard SaaS metric and differs from GAAP revenue CAGR. |
| 18 | Model-Readiness Summary present; accurately counts all provenance categories; management projections separated | ✓ | Summary present and accurate: 18 Direct, 2 Inferred, 0 Estimated, 7 Not Found. Management projections clearly distinguished. |
| 19 | ANALYST ACTIONS lists: (1) validate SBC treatment, (2) clarify ARR/MRR, (3) obtain p. 78-82 for CAC verification, (4) confirm EBITDA basis for ICR | ✓ | All minimum actions plus comprehensive additional flags: SBC run-rate, projection validation, equity ownership disclosure, FCF data request, comps guidance, Rule of 40 non-GAAP notation. Specific and actionable. |

**Scenario 2 result**: PASS

---

## Summary

The CIM Financial Data Extractor skill demonstrates exceptional rigor in applying the data-provenance taxonomy and producing analyst-ready extraction tables. On both scenarios:

- **All 18 default metrics** (Scenario 1) and **all 27 metrics** (Scenario 2, including custom SaaS KPIs) are extracted and classified with accurate provenance labeling (Direct, Inferred, Estimated, Not Found).
- **Conflicts are surfaced explicitly**, not glossed over. When the same metric appears in multiple places with different values (Scenario 1: Executive Summary approx. vs. Financial Summary exact; Scenario 2: ARR vs. annualized MRR), both figures are recorded, differences are explained, and analyst is directed to clarify.
- **Management adjustments and projections are clearly segregated** from historical actuals. The skill correctly identifies and flags when figures require analyst judgment (SBC add-backs, restructuring charges, PPP loan treatment, founder comp normalization, management projections).
- **Reasoning chains are complete**. Every Inferred metric shows its calculation; every Estimated metric documents the approximation method; every Not Found metric explains why (narrative mention without quantification, data in unreferenced section, etc.).
- **Output format is consistently Markdown table structure**, not narrative. Model-Readiness Summary and ANALYST ACTIONS sections provide specific, actionable next steps.
- **README portability is strong**: The portable template (`README.md`) is self-contained, uses clear placeholder syntax (`{TARGET_METRICS}`, `{CIM_CONTENT}`), and includes a representative example output with realistic numbers and industry-appropriate metrics.

Both tests pass all 15+ criteria without exception. The skill is production-ready and enforces a quality standard that reduces analyst error and accelerates deal screening workflows.

## Failure notes

None. Skill passes all criteria on both scenarios.
