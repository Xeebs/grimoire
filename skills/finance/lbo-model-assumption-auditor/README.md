# LBO Model Assumption Auditor

**Industry**: Finance
**Role**: Private Equity Associate / Investment Banking Associate
**Time saved**: 3–5 hours per model review cycle (formula audit, benchmark validation, stress-test build, convention formatting)

## What it does

Takes an AI-generated LBO model summary and your firm's stated modeling conventions, then systematically audits circular reference resolution and debt schedule mechanics, benchmarks every operating assumption against sector norms, generates a named stress-test scenario matrix (revenue stress, margin compression, rate shock, multiple contraction), and outputs a firm-convention compliance checklist with PASS/FAIL status per item — returning a single structured report that covers the highest-risk 20% of model-build work.

## When to use it

Invoke this skill immediately after an AI tool (or junior analyst) has produced a first-pass LBO model from CIM inputs and before the model is used in an IC memo, deal team presentation, or client deliverable. The model has been populated; your job is the audit — formula sanity, assumption credibility, downside coverage, and formatting compliance.

This is not a model-building tool. It is a model-review tool for the practitioner who needs to sign off.

## Prompt template

Copy the full prompt below. Replace every `{PLACEHOLDER}` with your actual inputs.

---

You are an expert LBO model reviewer with deep knowledge of leveraged finance, PE modeling conventions, and sector-specific benchmarking. Audit the LBO model described below and produce a structured review report. Follow the exact output structure specified at the end of this prompt.

**DEAL OVERVIEW**
Target company: {TARGET_COMPANY_NAME}
Sector: {SECTOR — e.g., Industrials / Manufacturing | Software / SaaS | Healthcare Services | Business Services}
Brief business description: {ONE TO TWO SENTENCES ON WHAT THE COMPANY DOES}

**AI-GENERATED MODEL SUMMARY**
Paste the full model summary, export, or structured description below. Include all available detail on:
- Entry assumptions (entry EBITDA, entry multiple, enterprise value, equity contribution)
- Debt structure (tranches, amounts, rates, amortization, revolver)
- Operating projections (revenue, EBITDA margin, capex, working capital — Years 1 through exit)
- Exit assumptions (hold period, exit multiple, exit EBITDA)
- Returns (sponsor MOIC, sponsor IRR)

{MODEL_SUMMARY_TEXT}

**FIRM MODELING CONVENTIONS**
List your firm's proprietary conventions below, one per line. If you leave this blank, a standard top-tier PE/IB convention set will be used.

{FIRM_CONVENTIONS_LIST}

**SECTOR BENCHMARKS (OPTIONAL)**
If you have proprietary sector benchmarks, paste them here. If left blank, standard industry benchmarks will be applied.

{SECTOR_BENCHMARKS_OPTIONAL}

---

Now produce the LBO Model Audit Report in the following exact structure:

## LBO Model Audit Report

### Executive Summary
[Overall status: READY FOR PRESENTATION | NEEDS REVISION | SIGNIFICANT REWORK REQUIRED]
- Critical findings: [count of FAIL items]
- Material benchmark deviations: [count of MATERIAL flags]
- Stress-test floor: [minimum IRR and MOIC across all scenarios]
- Top 3 priority actions:
  1. [Most critical fix]
  2. [Second priority fix]
  3. [Third priority fix]

---

### Section 1: Model Inputs Parsed
List all parsed inputs. Flag missing items as [DATA GAP].

---

### Section 2: Formula Logic Audit
For each item below, assign PASS / FAIL / NEEDS VERIFICATION with a one-sentence rationale.

**Circular Reference Logic**
- Revolver circular reference resolution
- PIK toggle accrual mechanics
- EBITDA definition consistency with covenant tests

**Debt Schedule Mechanics**
- Amortization sequence (mandatory → interest → cash sweep → revolver paydown)
- Cash sweep tranche priority
- Revolver drawn-at-close edge case
- Covenant test period basis

**Returns Logic**
- Equity bridge internal consistency
- IRR calculated on equity cash flows (not EV)
- MOIC gross vs. net basis disclosed

Format as a table: Item | Status | Finding

---

### Section 3: Sector Benchmark Validation
Compare each model assumption to the sector benchmark range.
Format as a table: Assumption | Model Value | Benchmark Range | Status (Within Range / Above Range / Below Range) | Delta | Flag (MATERIAL / NOTABLE / PASS)

---

### Section 4: Stress-Test Scenario Matrix
For each scenario below, estimate revised IRR and MOIC, and state whether the deal clears a 20% IRR / 2.0x MOIC hurdle.

Scenarios:
1. Base Case
2. Revenue Stress -20%
3. Margin Compression (-300 bps sustained)
4. Rate Shock +200 bps (floating debt only)
5. Combined Downside (-15% revenue, -200 bps margin, +150 bps rate)
6. Multiple Contraction (exit multiple -2x vs entry)
7. Delayed Exit (+2 years hold)

Format as a table: Scenario | Revenue Impact | Margin Impact | Rate Impact | IRR | MOIC | Clears Hurdle?

---

### Section 5: Firm Convention Compliance Checklist
Check the model against each convention provided (or the standard set if none provided).
Format as a table: # | Convention | Status (PASS / FAIL / UNVERIFIABLE) | Finding

---

### Section 6: Data Gaps and Limitations
Bullet list of all [DATA GAP] items from Section 1 and UNVERIFIABLE items from Section 5. For each, note what additional model information would resolve the gap.

---

Important rules:
- Use structured tables and lists throughout. No narrative paragraphs in place of tables.
- Do not invent model inputs. Use [DATA GAP] for anything missing.
- Do not recommend specific revised values. Flag deviations; the associate makes the judgment call.
- Do not conflate formula logic issues with assumption quality issues.
- Do not assess whether this is a good investment. Assess model integrity and convention compliance only.

---

## Example output

Below is an abbreviated example of what Section 2 and the Executive Summary look like for an industrials deal.

---

**Executive Summary**
Status: NEEDS REVISION
- Critical findings: 3
- Material benchmark deviations: 2
- Stress-test floor: 14.2% IRR / 1.6x MOIC (Combined Downside scenario)
- Top 3 priority actions:
  1. FAIL — Revolver circular reference: model uses prior-period balance workaround, creating a one-period lag that understates Year 1 revolver interest by ~$1.2M. Confirm whether iteration is enabled or switch to a corkscrew structure.
  2. FAIL — Cash sweep applied to Term Loan B before Term Loan A; credit agreement requires reverse order. Revise tranche priority.
  3. MATERIAL deviation — Capex at 2.1% of revenue vs. industrials benchmark of 3–7%. Revisit with management capex schedule from CIM Section 8.

---

**Section 2: Formula Logic Audit (excerpt)**

| Item | Status | Finding |
|---|---|---|
| Revolver circular reference resolution | FAIL | Model uses prior-period revolver balance; creates one-period interest lag in Year 1 |
| PIK toggle accrual | PASS | PIK accrues to principal at stated rate; compound schedule matches tranche documentation |
| EBITDA definition for covenant tests | NEEDS VERIFICATION | Model uses reported EBITDA; unclear whether pro-forma add-backs from CIM are included per credit agreement definition |
| Amortization sequence | PASS | Mandatory amortization before cash sweep; sequence confirmed correct |
| Cash sweep tranche priority | FAIL | Sweep flows to TLB before TLA; credit agreement requires TLA priority — revise |
| Revolver drawn-at-close edge case | PASS | $15M drawn at close reflected in Year 0; paydown modeled against FCF |
| IRR calculation basis | PASS | IRR on equity cash flows only; enterprise-level cash flows excluded |
| MOIC basis | NEEDS VERIFICATION | MOIC shown as 2.4x; unclear whether gross or net of transaction fees and management promote |

---

## Tips

1. **Paste the full model output, not just the returns summary.** The audit is most useful when it can see the debt schedule structure, the operating projection table, and the assumptions tab. A one-page summary will trigger many [DATA GAP] flags and limit the formula audit.

2. **Always provide your firm's conventions.** The default convention set reflects common top-tier PE/IB practice, but shops vary significantly on debt schedule tab structure, IRR calculation methodology (gross vs. net), and sensitivity table layouts. Five minutes entering your conventions will save an hour of reformatting.

3. **Run this after the AI model tool, not instead of it.** This skill reviews a model that already exists. It is not a model-building tool. Sequence: (1) AI generates first-pass model from CIM, (2) this skill audits it, (3) you make targeted fixes based on the FAIL items.
