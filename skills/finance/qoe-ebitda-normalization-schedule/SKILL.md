---
name: qoe-ebitda-normalization-schedule
description: Given a target company's historical income statements and flagged unusual items, classifies each adjustment as recurring or non-recurring with M&A QofE judgment, rates defensibility, builds a period-by-period EBITDA bridge, and outputs a deal-room-standard normalization schedule — for M&A Analysts and Transaction Advisory Associates performing buy-side due diligence.
industry: finance
role: M&A Analyst / Transaction Advisory Associate
trigger: During buy-side QofE due diligence, after the initial financial review surfaces unusual or one-time items in the target's income statements and before the adjusted EBITDA figure is presented to the deal team, investment committee, or lender.
---

## Context

The analyst is in the middle of a buy-side quality of earnings engagement. They have 2–5 years of the target company's historical income statements (often from management-prepared financials or a CPA-reviewed package) and a list of items flagged as potentially non-recurring — either identified by management in their QofE package, surfaced during the analyst's own review, or called out in a sell-side QofE report.

The analyst's job is not simply to apply accounting rules. A quality of earnings normalization requires deal judgment: an item may be GAAP-compliant and still non-recurring for transaction purposes (e.g., a one-time ERP implementation, COVID-era government stimulus income, owner personal expenses run through the business). Each adjustment must be defensible — because the sell-side advisor, the lender's credit team, or the buyer's investment committee will challenge every line.

The output of this skill — the QofE Normalization Schedule — becomes a working document in the deal room. It is cited in the LOI, underwritten by lenders, and reviewed by deal attorneys. Every number needs a rationale, and every aggressive adjustment needs a flag.

---

## Instructions

Follow these steps in sequence. Do not skip steps or merge them.

### Step 1 — Reconstruct or verify reported EBITDA for each period

Read the income statements provided. For each period (year, partial year, or LTM):

- Identify whether an EBITDA line is explicitly stated or must be reconstructed
- If reconstructing: calculate EBITDA = Net Income + Interest Expense + Income Tax Expense + Depreciation & Amortization
- Record **Reported EBITDA** for each period as the baseline; this is the starting point for the bridge
- Note any irregularities in the income statement structure (e.g., non-standard line items, missing D&A disclosure, combined interest/tax lines) and flag them for analyst follow-up
- If the financials are management-prepared (unaudited), note this prominently — it affects the defensibility of the baseline itself

Present the reported EBITDA for each period in a summary table before proceeding.

### Step 2 — Classify each flagged item

For each item provided in the flagged-items list, assign one of four classifications:

**RECURRING** — The item is an ordinary business cost or income that a buyer should expect to continue post-close. Do not adjust. Include in normalized EBITDA as-is.

**NON-RECURRING ADD-BACK** — The item reduced reported EBITDA but is genuinely one-time and will not repeat post-close. Adding it back increases adjusted EBITDA. Example: one-time litigation settlement paid, facility closure costs.

**NON-RECURRING DEDUCTION** — The item increased reported EBITDA but is genuinely one-time and will not repeat post-close. It must be deducted from reported EBITDA. Example: PPP loan forgiveness income, insurance proceeds from a casualty event, gain on asset sale. This is frequently mishandled — analysts sometimes treat one-time income as neutral rather than deducting it. Flag any item in this category explicitly.

**REQUIRES CONFIRMATION** — The item cannot be confidently classified without additional information from management. This includes: items where the dollar amount is unsubstantiated, items where recurrence is unclear, or owner-related expenses where market-rate benchmarking is needed. Do not include in adjusted EBITDA until confirmed. Flag for management diligence.

For each classification, write a **rationale** of one to three sentences explaining the QofE basis for the decision — not just the accounting treatment.

### Step 3 — Apply QofE defensibility judgment

For each item classified as NON-RECURRING ADD-BACK or NON-RECURRING DEDUCTION, assign a defensibility rating:

**Conservative** — The adjustment will not be challenged. The item is clearly one-time, documented, and unlikely to recur. Any seasoned sell-side QofE advisor would agree. Examples: closed facility costs with supporting invoices, a specific litigation settlement with a final judgment date.

**Moderate** — The adjustment is reasonable and market-standard but could be contested. The sell-side or a lender's credit team may request additional documentation or apply a haircut. Examples: above-market owner compensation without a formal comp study, customer-specific acquisition costs that management characterizes as non-recurring.

**Aggressive** — The adjustment is a stretch. It may be characterized differently by sell-side advisors, lenders, or the acquirer's investment committee. Including it at full value creates deal risk. Examples: recurring-but-variable costs management calls "one-time," broad "strategic consulting" categorized as non-recurring without specificity, unsubstantiated owner personal expenses without a signed representation.

Aggressive adjustments must be individually flagged in the output. Do not omit them or silently downgrade them to Moderate to make the schedule look cleaner.

### Step 4 — Build the EBITDA bridge for each period

For each period (including LTM if provided):

1. Start with **Reported EBITDA** (from Step 1)
2. Apply each confirmed adjustment in order: Non-Recurring Add-Backs (positive), Non-Recurring Deductions (negative)
3. Items classified REQUIRES CONFIRMATION are excluded from the bridge but listed separately
4. Arrive at **Adjusted EBITDA** for the period
5. Show the complete walk — do not jump from reported to adjusted without showing each line

Present the EBITDA bridge as a table with a column per period and a row per adjustment line.

### Step 5 — Calculate LTM Adjusted EBITDA

If the most recent period provided is a partial year, calculate LTM (Last Twelve Months) Adjusted EBITDA:

LTM = Most Recent Full Year + YTD Current Period − Same Period Prior Year

Show this calculation explicitly. Do not estimate or annualize without disclosing the methodology.

If full LTM data is not available (e.g., only annual statements provided with no partial-year stub), state this clearly and use the most recent full-year adjusted EBITDA as the proxy, noting the limitation.

### Step 6 — Compute the defensible range and flag deal risks

After the schedule is complete:

1. **Defensible adjusted EBITDA range**: Calculate two figures:
   - **High case**: Reported EBITDA + all Conservative and Moderate add-backs − all Conservative and Moderate deductions
   - **Conservative case**: Reported EBITDA + Conservative add-backs only − all deductions (including Aggressive deductions)
   - Note: Aggressive add-backs are excluded from both cases; present them separately as "subject to diligence"

2. **Aggressive adjustment concentration check**: If the total of Aggressive add-backs exceeds 15% of Reported EBITDA in any period, flag this as a deal-risk signal — it indicates the normalized EBITDA figure is materially dependent on adjustments that are likely to be challenged.

3. **Items requiring management confirmation**: List all REQUIRES CONFIRMATION items as open diligence items with a suggested management request or representation needed to resolve each one.

### Step 7 — Output the full normalization schedule and summary

Produce all three output sections described in the Output Format below.

---

## Output Format

```
QofE EBITDA NORMALIZATION SCHEDULE
====================================
Target Company:      [from input]
Engagement Type:     Buy-Side Quality of Earnings
Periods Covered:     [e.g., FY2021, FY2022, FY2023, LTM Q3 2024]
Prepared:            AI-assisted draft — requires analyst review before use in deal room
Financial Basis:     [Audited / Reviewed / Management-Prepared — as indicated in input]

────────────────────────────────────────────────────────────────────
SECTION A — ADJUSTMENT SCHEDULE
────────────────────────────────────────────────────────────────────
| # | Description           | Period(s) | Amount ($K) | Classification         | Defensibility | Rationale (QofE Basis)                         | Mgmt Confirmation Required |
|---|-----------------------|-----------|-------------|------------------------|---------------|------------------------------------------------|---------------------------|
| 1 | [Item description]    | FY2023    | $XXX        | Non-Recurring Add-Back | Conservative  | [1–3 sentence QofE rationale]                  | No                        |
| 2 | [Item description]    | FY2023    | ($XXX)      | Non-Recurring Deduction| Conservative  | [1–3 sentence QofE rationale]                  | No                        |
| 3 | [Item description]    | FY2023    | $XXX        | Recurring              | N/A           | [Rationale for recurring classification]       | No                        |
| 4 | [Item description]    | FY2023    | $XXX        | Requires Confirmation  | N/A           | [Why confirmation is needed]                   | Yes — [specific ask]      |
| 5 | [Item description]    | FY2023    | $XXX        | Non-Recurring Add-Back | Aggressive    | [QofE rationale + flag: challenge risk]        | No                        |

Note: Add-backs are shown as positive amounts. Deductions are shown as negative (parenthetical) amounts.
Items classified Aggressive are marked with [AGGRESSIVE FLAG] in the deal risk section.

────────────────────────────────────────────────────────────────────
SECTION B — EBITDA BRIDGE (PER PERIOD)
────────────────────────────────────────────────────────────────────
                                    FY[YYYY]    FY[YYYY]    FY[YYYY]    LTM
                                    --------    --------    --------    ---
Reported EBITDA                     $X,XXX      $X,XXX      $X,XXX      $X,XXX
Adjustments:
  [Add-back item 1]                 $XXX        $XXX        $—          $XXX
  [Add-back item 2]                 $—          $XXX        $XXX        $XXX
  [Deduction item 1]                ($XXX)      ($XXX)      ($XXX)      ($XXX)
  [Aggressive item — footnoted*]    $XXX        $XXX        $XXX        $XXX
                                    --------    --------    --------    ---
Adjusted EBITDA (Confirmed)         $X,XXX      $X,XXX      $X,XXX      $X,XXX
Items Pending Confirmation          $XXX        $XXX        $XXX        $XXX
Adjusted EBITDA (If Confirmed)      $X,XXX      $X,XXX      $X,XXX      $X,XXX

*Aggressive items are included in the bridge for transparency but flagged — see Section C.

────────────────────────────────────────────────────────────────────
SECTION C — QofE RISK SUMMARY
────────────────────────────────────────────────────────────────────

Defensible Adjusted EBITDA Range (LTM):
  Conservative Case (Conservative add-backs only):  $X,XXX K
  High Case (Conservative + Moderate add-backs):    $X,XXX K
  Aggressive Case (all add-backs, not recommended): $X,XXX K

Aggressive Adjustment Concentration:
  Total Aggressive add-backs as % of Reported EBITDA (LTM): XX%
  [DEAL RISK SIGNAL if >15%: flag here]

Open Diligence Items (Requires Confirmation):
  1. [Item description] — Requested: [specific management representation or document needed]
  2. ...

Analyst Notes:
  [Any irregularities in the financial statements, baseline concerns, or items outside the flagged list that merit investigation]

DRAFT — THIS SCHEDULE REQUIRES ANALYST REVIEW, MANAGEMENT CONFIRMATION OF FLAGGED ITEMS,
AND DEAL TEAM SIGN-OFF BEFORE USE IN A DEAL ROOM, OFFERING MEMORANDUM, OR LENDING PACKAGE.
```

---

## Constraints

- **Do not classify an item as Non-Recurring without a written QofE rationale.** Accounting treatment alone (e.g., "it is below the line") is not sufficient. The rationale must explain why a buyer would not expect this cost or income to continue post-close.
- **Do not omit or soften Aggressive ratings.** If an adjustment is a stretch by deal-market standards, rate it Aggressive regardless of whether it improves the normalized EBITDA. The defensibility rating exists to protect the analyst and the deal team — sanitizing it undermines the entire purpose of a QofE.
- **Do not confuse add-backs and deductions.** One-time income items (e.g., PPP forgiveness, insurance proceeds, gain on sale) are deductions from reported EBITDA, not neutral items. Misclassifying them overstates adjusted EBITDA and is a common QofE error. Always verify the direction of each adjustment before including it in the bridge.
- **Do not include REQUIRES CONFIRMATION items in the adjusted EBITDA bridge.** Show them separately. Including unconfirmed items inflates the normalized figure and creates liability.
- **Do not produce a single aggregate EBITDA figure.** The bridge must show each period separately so trend analysis is possible.
- **Do not apply a single-year adjustment to multiple periods without explicit evidence.** If a cost appears in only one year, only adjust that year — do not normalize it across all periods without documentation.
- **Do not use normalized EBITDA interchangeably with Adjusted EBITDA.** Be explicit that this is a QofE Adjusted EBITDA and that it is a deal-process document, not an audited figure.
- **Do not provide an enterprise value or purchase price implication.** This skill produces the EBITDA normalization schedule only. Valuation multiples and enterprise value calculations are outside scope.
