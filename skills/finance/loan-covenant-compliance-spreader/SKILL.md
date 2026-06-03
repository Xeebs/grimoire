---
name: loan-covenant-compliance-spreader
description: Given a credit agreement and a borrower's quarterly financial submission, extracts contract-specific covenant definitions, calculates each required ratio from submitted financials, and produces a compliance certificate with pass/fail status and breach-proximity alerts — for Credit Analysts and Portfolio Managers.
industry: finance
role: Credit Analyst / Portfolio Manager
trigger: Borrower delivers quarterly (or semi-annual) financial package for covenant testing; analyst must produce or verify the compliance certificate before the reporting deadline.
---

## Context

The analyst has two documents in front of them:

1. A **credit agreement** (or loan agreement / credit facility agreement) that contains a Definitions section and Financial Covenants section specifying how each ratio is calculated for this particular loan. Terms like "EBITDA," "Adjusted EBITDA," "Total Indebtedness," "DSCR," "LTV," or "Leverage Ratio" are almost always defined differently across agreements — sometimes with add-backs, exclusions, or trailing-period conventions that deviate from textbook definitions.
2. A **borrower financial submission** — typically a quarterly income statement, balance sheet, and cash flow statement, sometimes in a standardized template, sometimes in the borrower's own format.

The analyst's job is to:
- Re-read the exact covenant definitions in this specific agreement
- Locate the corresponding line items in the borrower's submission
- Apply the agreement's formula (not a textbook formula) to calculate each ratio
- Compare each result to the threshold specified in the agreement
- Prepare or review the compliance certificate

This skill automates the extraction-calculation-certification pipeline. The analyst retains responsibility for verifying inputs and signing off on the certificate.

---

## Instructions

Follow these steps in sequence. Do not skip steps or merge them.

### Step 1 — Extract covenant definitions from the credit agreement

Read the credit agreement provided. Identify every financial covenant. For each covenant:

- Record the **covenant name** exactly as it appears in the agreement
- Record the **section number** where it is defined
- Write out the **exact formula** as stated in the agreement, quoting key defined terms verbatim (e.g., "Consolidated EBITDA" as defined in Section 1.01)
- Note any **add-backs, exclusions, or adjustments** called out in the definition
- Note the **testing period** (trailing twelve months, most recent fiscal quarter annualized, etc.)
- Record the **threshold** (minimum ratio, maximum ratio, or absolute floor/ceiling) and any step-downs or step-ups across the loan term

Present this as a **Covenant Definition Registry** table before proceeding to any calculations.

### Step 2 — Map financial submission line items to covenant inputs

Read the borrower's financial submission. For each defined term used in the covenant formulas (from Step 1):

- Identify the **corresponding line item(s)** in the submission
- Note the **exact value** and the **period it covers**
- Flag any term where the required line item is **absent, ambiguous, or requires aggregation** across multiple lines
- If a definition requires a trailing-twelve-month (TTM) figure but only one quarter is provided, flag this explicitly and state what additional periods would be needed — do not fabricate missing data

Present this as a **Line Item Mapping** table.

### Step 3 — Calculate each covenant ratio

For each covenant, apply the formula extracted in Step 1 using the mapped values from Step 2.

- Show the **full calculation** as a worked equation, not just the result
- Label each input with its source line item
- State the **calculated ratio** to two decimal places
- State the **required threshold** from the agreement
- State **pass or fail**
- Calculate **headroom** (distance from threshold) as both an absolute value and a percentage

If any input was flagged as missing or ambiguous in Step 2, mark the covenant result as **INCOMPLETE — MISSING INPUT** rather than producing a potentially incorrect calculation.

### Step 4 — Produce the compliance certificate

Format the output as a compliance certificate structured as follows (see Output Format section below). The certificate must:

- Open with the loan reference, borrower name, testing period, and certificate date
- Include a summary table of all covenants with their status
- Follow with the detailed calculation workings for each covenant
- Close with a breach-proximity alert section flagging any covenant within 15% of its threshold
- Include a Notes section for any flagged ambiguities, missing inputs, or items requiring analyst review

---

## Output Format

```
COVENANT COMPLIANCE CERTIFICATE
================================
Loan Reference:     [from agreement / input]
Borrower:           [from submission]
Testing Period:     [e.g., FY Q3 2024 / TTM ended September 30, 2024]
Certificate Date:   [today's date]
Prepared by:        AI-assisted draft — requires analyst review and sign-off

────────────────────────────────────────
SECTION 1 — COVENANT DEFINITION REGISTRY
────────────────────────────────────────
| Covenant Name      | Agreement Section | Formula (as defined)         | Testing Period | Threshold        |
|--------------------|-------------------|------------------------------|----------------|------------------|
| [Covenant 1]       | §X.XX             | [Verbatim formula]           | TTM / Quarter  | [e.g., ≥ 1.25x] |
| ...                | ...               | ...                          | ...            | ...              |

────────────────────────────────────────
SECTION 2 — LINE ITEM MAPPING
────────────────────────────────────────
| Defined Term           | Source Line Item              | Value      | Period     | Flag          |
|------------------------|-------------------------------|------------|------------|---------------|
| [Consolidated EBITDA]  | [Net income + D&A + ...]      | $X,XXX,XXX | TTM        |               |
| ...                    | ...                           | ...        | ...        |               |

────────────────────────────────────────
SECTION 3 — COVENANT CALCULATIONS
────────────────────────────────────────

[Covenant 1 Name] (§X.XX)
  Formula:    [Numerator] / [Denominator]
  Numerator:  $X,XXX,XXX  ([source line items])
  Denominator:$X,XXX,XXX  ([source line items])
  Result:     X.XXx
  Required:   ≥ X.XXx
  Status:     PASS / FAIL
  Headroom:   X.XXx (XX.X% above / below threshold)

[Repeat for each covenant]

────────────────────────────────────────
SECTION 4 — COMPLIANCE SUMMARY
────────────────────────────────────────
| Covenant           | Calculated | Required   | Status | Headroom    |
|--------------------|------------|------------|--------|-------------|
| [Covenant 1]       | X.XXx      | ≥ X.XXx    | PASS   | XX.X%       |
| ...                | ...        | ...        | ...    | ...         |

Overall Status: [ALL COVENANTS PASS / COVENANT BREACH DETECTED]

────────────────────────────────────────
SECTION 5 — BREACH-PROXIMITY ALERTS
────────────────────────────────────────
[List any covenant within 15% of threshold]
[If none: "No covenants within breach-proximity threshold."]

────────────────────────────────────────
SECTION 6 — ANALYST NOTES
────────────────────────────────────────
[List any flagged ambiguities, missing inputs, definitional interpretation decisions, or items requiring analyst review before the certificate is finalized]

DRAFT — THIS CERTIFICATE REQUIRES ANALYST REVIEW AND AUTHORIZED SIGN-OFF BEFORE SUBMISSION TO LENDER.
```

---

## Constraints

- **Do not use textbook ratio definitions.** Always extract the exact formula from the credit agreement. If a term is not defined in the agreement, flag it explicitly — do not substitute a standard market definition.
- **Do not fabricate missing financial data.** If a required input is absent from the borrower's submission, mark the covenant INCOMPLETE and flag it for analyst follow-up.
- **Do not provide legal or audit opinions.** The output is an AI-assisted computational draft. Label it clearly as requiring analyst review and authorized sign-off.
- **Do not interpret ambiguous definitions silently.** If a definition could be read two ways, state both interpretations, show the calculation under each, and flag for analyst decision.
- **Do not omit any covenant found in the agreement.** If a covenant definition is in the agreement but cannot be calculated due to missing data, it must still appear in the output marked INCOMPLETE.
- **Do not apply step-downs or covenant holidays without explicitly noting them.** If the agreement specifies different thresholds for different periods (e.g., a DSCR step-down from 1.30x to 1.25x in Year 3), confirm which threshold applies to the current testing period and state why.
- **Do not round intermediate calculations.** Carry full precision through to the final result; only round the displayed result to two decimal places.
- **Do not conflate reporting period and testing period.** If the borrower submits a quarterly P&L but the covenant requires TTM data, flag the gap rather than annualizing without disclosure.
