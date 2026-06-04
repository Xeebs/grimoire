---
name: lbo-model-assumption-auditor
description: Audits an AI-generated LBO model for formula logic errors, benchmarks assumptions against sector norms, generates a stress-test scenario matrix, and produces a firm-convention compliance checklist — for PE and IB associates doing final review before a model is presentation-ready.
industry: finance
role: Private Equity Associate / Investment Banking Associate
trigger: After an AI tool produces a first-pass LBO model from CIM inputs and you need to audit formula logic, validate assumptions, stress-test scenarios, and reformat outputs to match your firm's modeling conventions before the model can be used in a deal presentation or IC memo.
---

## Context

You are a PE or IB associate who has used an AI tool to generate a first-pass LBO model from a CIM or management presentation. The model has populated the income statement, balance sheet, debt schedule, and returns analysis. You now need to do the final 20% of model-build — the highest-risk work:

- Verify that circular reference logic (revolver draw/paydown, PIK accrual) resolves correctly
- Confirm debt schedule mechanics (amortization sequence, cash sweep priority, DSCR triggers) are sound
- Validate that the operating assumptions (revenue growth, EBITDA margin, capex intensity) are credible relative to sector benchmarks
- Stress-test the model at extreme scenarios to understand downside protection and return profile sensitivity
- Check that every element of the model matches your firm's proprietary formatting and convention standards

This skill takes the model as a structured description or export and your firm's convention list, and returns a prioritized audit with actionable pass/fail findings — not a narrative summary.

---

## Instructions

Follow these steps in order. Do not skip steps. Do not combine outputs.

### Step 1 — Parse Model Inputs

Extract and list the following from the model description provided:

- **Entry assumptions**: Entry EBITDA, entry multiple (EV/EBITDA), resulting enterprise value, equity contribution %, sponsor equity check
- **Debt structure**: Tranche names, amounts ($M and as x EBITDA), interest rates (fixed vs. floating, PIK toggle if present), amortization schedules, revolver size and drawn amount at close
- **Operating projections**: Revenue CAGR, EBITDA margin trajectory (Year 1 through exit year), capex as % of revenue, working capital assumptions
- **Exit assumptions**: Hold period, exit multiple (EV/EBITDA), exit year EBITDA, resulting equity value
- **Returns**: Sponsor MOIC, sponsor IRR, management equity rollover % if stated

If any of these items are missing from the input, flag them as **[DATA GAP]** in the parsed list — do not invent values.

### Step 2 — Formula Logic Audit

Audit the model's described mechanics against the following known failure modes. For each item, assign a status of PASS, FAIL, or NEEDS VERIFICATION, with a one-sentence rationale.

**Circular Reference Logic**
- Revolver: Does the revolver draw/paydown logic create a circular reference? If so, is it resolved via iteration (Excel) or a workaround (prior-period balance)? Flag if ambiguous.
- PIK toggle: If PIK interest is present, does it accrue to principal correctly in each period, or does the model use a static interest line?
- EBITDA definition: Does the EBITDA used in leverage ratio tests match the defined EBITDA in the debt agreement (i.e., does it include pro-forma add-backs)?

**Debt Schedule Mechanics**
- Amortization sequence: Is mandatory amortization deducted before or after cash sweep? Confirm sequence: (1) mandatory amortization, (2) interest, (3) cash sweep to optional prepayment, (4) revolver paydown.
- Cash sweep: Is the cash sweep applied to the correct tranche (highest-cost debt first, unless credit agreement specifies otherwise)?
- Revolver edge case: If the revolver is fully drawn at close, does the model correctly reflect a drawn balance at Year 0 and model paydown against free cash flow — not a zero balance?
- Covenant triggers: If the model includes a DSCR or leverage covenant, does the covenant test use beginning-of-period debt or average? Flag if not specified.

**Returns Logic**
- Equity bridge: Is the equity bridge (entry equity + cumulative FCF + exit proceeds - remaining debt) internally consistent?
- IRR calculation: Is IRR calculated on equity cash flows (equity in at Year 0, equity out at exit), not on enterprise value cash flows?
- MOIC: Is MOIC calculated as exit equity / entry equity (gross), or does it net transaction fees? Note which basis is used.

### Step 3 — Sector Benchmark Validation

Compare the model's operating assumptions to the sector benchmarks provided below. If the user provides sector-specific benchmarks in their input, use those; otherwise use the defaults below.

**Default sector benchmarks by deal type** (use if user does not specify):

| Assumption | Industrials / Manufacturing | Software / SaaS | Healthcare Services | Business Services |
|---|---|---|---|---|
| Revenue CAGR | 3–6% | 15–30% | 6–10% | 5–9% |
| EBITDA Margin (entry) | 12–20% | 20–40% | 10–18% | 14–22% |
| Capex as % Revenue | 3–7% | 1–3% | 2–5% | 1–3% |
| Net Working Capital Days | 45–75 | 15–30 (negative OK) | 30–50 | 20–40 |
| Entry Multiple (EV/EBITDA) | 6–9x | 12–25x | 8–13x | 7–11x |
| Exit Multiple vs Entry | Flat to -1x | Flat to +2x | Flat to -0.5x | Flat to -0.5x |
| Total Leverage at Close | 4–5.5x | 5–7x | 4–6x | 4–5.5x |

For each assumption in the model:
- State whether it falls **Within range**, **Above range** (aggressive), or **Below range** (conservative)
- If outside range, calculate the delta and flag it as **MATERIAL** (>15% outside range) or **NOTABLE** (5–15% outside range)
- If within range, mark **PASS**

Do not editorialize beyond the benchmark flag. If a deviation is material, note it but do not recommend a specific value.

### Step 4 — Stress-Test Scenario Matrix

Generate a stress-test scenario matrix with the following named scenarios. For each scenario, calculate the impact on (a) exit equity value and (b) sponsor IRR, using the base case as the starting point. Show directional impact (+/-) and approximate magnitude. If you cannot calculate exact values from the input provided, show the sensitivity direction and note that exact calculation requires the full model.

| Scenario | Revenue Impact | EBITDA Margin Impact | Debt/Rate Impact | Notes |
|---|---|---|---|---|
| **Base Case** | Per model | Per model | Per model | Baseline |
| **Revenue Stress -20%** | -20% vs base CAGR | -150 to -250 bps compression | None | Tests revenue durability |
| **Margin Compression** | Per model | -300 bps sustained | None | Tests operating leverage |
| **Rate Shock +200bps** | Per model | Per model | +200 bps on all floating debt | Tests refinancing risk |
| **Combined Downside** | -15% vs base CAGR | -200 bps | +150 bps floating | Simulates recession scenario |
| **Multiple Contraction** | Per model | Per model | None | Exit multiple -2x vs entry |
| **Delayed Exit (+2 Years)** | Per model | Per model | None | Hold period extended |

For each scenario, output:
- Approximate revised IRR (or directional delta if exact calc not possible)
- Approximate revised MOIC (or directional delta)
- Whether the deal still clears a 20% IRR / 2.0x MOIC minimum return hurdle (YES / NO / UNCERTAIN)

### Step 5 — Firm Convention Compliance Checklist

Compare the model against the firm conventions provided by the user. For each convention listed:

- Mark **PASS** if the model matches the convention
- Mark **FAIL** if the model violates it, with a specific description of the violation
- Mark **UNVERIFIABLE** if the input does not provide enough information to assess

Present as a numbered checklist table with columns: `#` | `Convention` | `Status` | `Finding`.

If the user provides no firm conventions, generate a standard convention checklist based on the following defaults (used by most top-tier PE/IB shops):

1. All monetary values in $M, two decimal places
2. Hard-coded inputs in blue font (noted in documentation)
3. Formulas reference named cells or ranges — no hardcoded numbers embedded in formulas
4. Debt schedule organized by tranche, each with its own amortization schedule tab
5. Returns summary on a standalone summary tab with sensitivity tables for entry multiple, exit multiple, and revenue growth
6. IRR and MOIC calculated on both gross and net-of-fees basis
7. All cells include units labels (x EBITDA, %, $M) in adjacent columns
8. No merged cells in data entry ranges
9. Sources and assumptions tab documenting all input sources with page/section citation
10. Version control notation on cover tab (version number, date, author initials)

### Step 6 — Executive Summary

Output a concise executive summary at the top of the response with:
- **Overall model status**: READY FOR PRESENTATION / NEEDS REVISION / SIGNIFICANT REWORK REQUIRED
- **Critical findings count**: Number of FAIL items across formula audit and convention checklist
- **Material benchmark deviations**: Count of MATERIAL flags from sector benchmarks
- **Stress-test floor**: The minimum IRR and MOIC across all scenarios
- **Top 3 priority actions**: The three most important fixes, in priority order

Place the executive summary first in the output, before all other sections.

---

## Output Format

Output must follow this exact structure. Each section is mandatory.

```
## LBO Model Audit Report

### Executive Summary
[Status badge: READY FOR PRESENTATION | NEEDS REVISION | SIGNIFICANT REWORK REQUIRED]
- Critical findings: X
- Material benchmark deviations: X
- Stress-test floor: X% IRR / X.Xx MOIC
- Top 3 priority actions:
  1. [Action]
  2. [Action]
  3. [Action]

---

### Section 1: Model Inputs Parsed
[Structured list as described in Step 1 — DATA GAPs flagged inline]

---

### Section 2: Formula Logic Audit
[Table: Item | Status (PASS/FAIL/NEEDS VERIFICATION) | Finding]
[Grouped by: Circular Reference Logic / Debt Schedule Mechanics / Returns Logic]

---

### Section 3: Sector Benchmark Validation
[Table: Assumption | Model Value | Benchmark Range | Status | Delta]
[Sector used: {sector name}]

---

### Section 4: Stress-Test Scenario Matrix
[Table: Scenario | Rev Impact | Margin Impact | Rate Impact | IRR | MOIC | Clears Hurdle?]

---

### Section 5: Firm Convention Compliance Checklist
[Table: # | Convention | Status | Finding]

---

### Section 6: Data Gaps and Limitations
[Bulleted list of DATA GAP items from Step 1 and UNVERIFIABLE items from Step 5, with a note on what additional model information would resolve each gap]
```

---

## Constraints

- Do NOT produce narrative summaries in place of structured tables. Every section must use the specified table or list format.
- Do NOT invent model inputs that were not provided. Use `[DATA GAP]` for missing values.
- Do NOT recommend specific revised assumption values. Flag deviations against benchmarks, but the associate makes the judgment call.
- Do NOT conflate formula logic issues with assumption issues. Section 2 is formula mechanics only. Section 3 is assumption quality only.
- Do NOT skip the stress-test section even if the model input is partial. Use directional analysis if exact calculation is not possible, and note the limitation.
- Do NOT produce a generic LBO model guide or tutorial. All output must reference the specific model inputs provided.
- Do NOT assess whether the deal is a good investment. Assess whether the model is internally consistent and convention-compliant.
- Do NOT use informal or conversational language. All output must match the register of a deal-team document.
