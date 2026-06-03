# Loan Covenant Compliance Spreader

**Industry**: Finance
**Role**: Credit Analyst / Portfolio Manager
**Time saved**: 3–6 hours per borrower per quarter (vs. manually re-reading agreement definitions, mapping line items, and building per-loan calculation spreadsheets)

---

## What it does

Given two documents — a credit agreement and a borrower's quarterly financial submission — this skill extracts the contract-specific covenant definitions, maps them to the submitted financials, calculates each ratio using the agreement's exact formula (not textbook defaults), and produces a structured compliance certificate with pass/fail status, headroom percentages, and breach-proximity alerts.

The core value is the two-document synthesis: every credit agreement defines terms like DSCR, Adjusted EBITDA, and Total Indebtedness differently. This skill forces the AI to read the agreement's definitions before calculating — not apply a generic formula that may not match the loan's terms.

---

## When to use it

Invoke this skill when:
- A borrower has delivered their quarterly (or semi-annual) financial package
- You need to produce or verify the compliance certificate before the reporting deadline
- You are onboarding a new loan and need to document the covenant calculation methodology
- You are reviewing a borrower-submitted compliance certificate for independent verification

Do not use this skill as the final signed certificate. It produces an AI-assisted draft that requires analyst review and authorized sign-off before submission to the lender.

---

## What you need

**Required — Document 1 (Credit Agreement):**
- The Definitions section (Article I or equivalent) covering all terms used in covenant formulas — e.g., "Consolidated EBITDA," "Total Indebtedness," "Debt Service," "Net Operating Income"
- The Financial Covenants section specifying each maintenance test, its threshold, and testing frequency
- Any amendment letters or waiver agreements that modify covenant thresholds or grant covenant holidays

**Required — Document 2 (Borrower Financials):**
- Income statement, balance sheet, and cash flow statement for the current reporting period
- For TTM covenants: either a pre-calculated TTM summary or four quarters of income statement data (the model will not annualize a single quarter without flagging it)

**Optional but improves output quality:**
- The borrower's own compliance certificate (for independent verification mode — discrepancies will be flagged)
- Prior-period compliance certificate (to confirm which step-down threshold applies in the current period)
- Rent roll or NOI schedule (for real estate loans with occupancy-linked covenants)

---

## Prompt template

Copy the entire prompt below. Replace every `{PLACEHOLDER}` with your actual content.

---

You are a Credit Analyst assistant. I will provide you with two documents. Your task is to produce an AI-assisted draft Covenant Compliance Certificate following the exact steps below. Do not deviate from the steps or merge them.

**DOCUMENT 1 — CREDIT AGREEMENT EXCERPT:**
{PASTE THE DEFINITIONS SECTION AND FINANCIAL COVENANTS SECTION FROM THE CREDIT AGREEMENT HERE. Include the exact text of every defined term used in covenant calculations, the covenant thresholds, and any step-down or step-up provisions.}

**DOCUMENT 2 — BORROWER FINANCIAL SUBMISSION:**
{PASTE THE BORROWER'S FINANCIAL STATEMENTS HERE — INCOME STATEMENT, BALANCE SHEET, AND CASH FLOW STATEMENT. Include the reporting period and any notes that explain line items.}

**LOAN REFERENCE:** {e.g., "ABC Lending — Term Loan B, Facility Agreement dated March 12, 2022"}
**BORROWER:** {Borrower legal name}
**TESTING PERIOD:** {e.g., "Trailing Twelve Months ended September 30, 2024" or "Fiscal Quarter ended September 30, 2024"}
**CERTIFICATE DATE:** {Today's date}

---

**STEP 1 — COVENANT DEFINITION REGISTRY**

Read Document 1. Identify every financial covenant. For each, produce a table with these columns:
- Covenant Name (exactly as written in the agreement)
- Agreement Section number
- Formula (verbatim from the agreement, quoting defined terms)
- Any add-backs, exclusions, or adjustments specified
- Testing period (TTM, single quarter, annualized, etc.)
- Threshold (minimum or maximum ratio) and any step-downs/step-ups

**STEP 2 — LINE ITEM MAPPING**

Read Document 2. For each defined term from Step 1, identify the corresponding line item(s) in the financial submission. Produce a table with: Defined Term | Source Line Item(s) | Value | Period | Flag (if absent, ambiguous, or requires aggregation). If a required input is missing, flag it — do not estimate or extrapolate.

**STEP 3 — COVENANT CALCULATIONS**

For each covenant, apply the formula from Step 1 using the values from Step 2. Show the full worked calculation (not just the result). State the result to two decimal places, the required threshold, pass/fail status, and headroom as both an absolute value and a percentage of the threshold. If any input was flagged missing, mark the result INCOMPLETE — MISSING INPUT.

**STEP 4 — COMPLIANCE CERTIFICATE**

Produce the final certificate in this format:

COVENANT COMPLIANCE CERTIFICATE
================================
Loan Reference:     [from input]
Borrower:           [from input]
Testing Period:     [from input]
Certificate Date:   [from input]
Prepared by:        AI-assisted draft — requires analyst review and sign-off

SECTION 1 — COVENANT DEFINITION REGISTRY
[Table from Step 1]

SECTION 2 — LINE ITEM MAPPING
[Table from Step 2]

SECTION 3 — COVENANT CALCULATIONS
[Full worked calculations from Step 3, one block per covenant]

SECTION 4 — COMPLIANCE SUMMARY
[Table: Covenant | Calculated | Required | Status | Headroom]
Overall Status: [ALL COVENANTS PASS / COVENANT BREACH DETECTED]

SECTION 5 — BREACH-PROXIMITY ALERTS
[Any covenant within 15% of its threshold. If none: "No covenants within breach-proximity threshold."]

SECTION 6 — ANALYST NOTES
[Any flagged ambiguities, missing inputs, interpretation decisions, or items requiring analyst review]

DRAFT — THIS CERTIFICATE REQUIRES ANALYST REVIEW AND AUTHORIZED SIGN-OFF BEFORE SUBMISSION TO LENDER.

---

**CRITICAL RULES:**
- Use only the formula as written in the credit agreement. Do not substitute textbook definitions.
- If a required input is missing from the financial submission, mark that covenant INCOMPLETE — do not fabricate data.
- If a definition is ambiguous, show the calculation under both interpretations and flag for analyst decision.
- Do not omit any covenant found in the agreement, even if it cannot be calculated.
- Carry full precision through calculations; round only the displayed result to two decimal places.
- If the borrower's reporting period does not match the covenant testing period (e.g., quarterly vs. TTM), flag this explicitly.

---

## Example output

Below is a condensed example for a two-covenant loan.

```
COVENANT COMPLIANCE CERTIFICATE
================================
Loan Reference:     Meridian Capital — Senior Secured Term Loan, dated June 1, 2021
Borrower:           Apex Manufacturing LLC
Testing Period:     Trailing Twelve Months ended September 30, 2024
Certificate Date:   October 15, 2024
Prepared by:        AI-assisted draft — requires analyst review and sign-off

SECTION 1 — COVENANT DEFINITION REGISTRY
| Covenant Name        | Section | Formula                                         | Testing Period | Threshold |
|----------------------|---------|--------------------------------------------------|----------------|-----------|
| Debt Service Coverage| §7.1(a) | Consolidated EBITDA / Consolidated Debt Service  | TTM            | ≥ 1.25x   |
| Total Net Leverage   | §7.1(b) | Total Net Debt / Consolidated EBITDA             | TTM            | ≤ 4.50x   |

[Consolidated EBITDA defined in §1.01 as Net Income + Interest Expense + Income Tax + D&A +
non-cash charges + restructuring charges not to exceed $2,000,000]

SECTION 3 — COVENANT CALCULATIONS (excerpt)

Debt Service Coverage Ratio (§7.1(a))
  Formula:    Consolidated EBITDA / Consolidated Debt Service
  EBITDA:     $18,450,000  (Net Income $9,200,000 + Interest $3,100,000 + Tax $2,650,000
                            + D&A $3,200,000 + Non-cash charges $300,000)
  Debt Svc:   $14,200,000  (Scheduled principal $11,100,000 + Cash interest $3,100,000)
  Result:     1.30x
  Required:   ≥ 1.25x
  Status:     PASS
  Headroom:   0.05x (4.0% above threshold)

SECTION 5 — BREACH-PROXIMITY ALERTS
  DSCR: 1.30x calculated vs. 1.25x required — 4.0% headroom. MONITOR CLOSELY.

SECTION 6 — ANALYST NOTES
  - "Non-cash charges" in EBITDA definition: borrower included $300,000 stock-based compensation.
    Confirm this qualifies as a non-cash charge under §1.01 before finalizing.
```

---

## Tips

1. **Paste the definitions verbatim, not a summary.** The quality of the output depends entirely on the AI reading the exact contractual language. Paraphrasing definitions before pasting them risks introducing errors that flow through every calculation.

2. **Include the entire Financial Covenants section, not just the ratios.** Threshold step-downs, cure periods, and equity cure provisions are often in the same section and affect whether a technical breach is actually actionable.

3. **Run one loan at a time.** Each credit agreement has its own definition ecosystem. Mixing two loans in one prompt produces cross-contamination between covenant definitions. Use a separate prompt for each borrower.
