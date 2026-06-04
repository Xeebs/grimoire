# QofE EBITDA Normalization Schedule

**Industry**: Finance
**Role**: M&A Analyst / Transaction Advisory Associate
**Time saved**: 6–12 hours per deal vs. manual Excel rebuild; eliminates re-work from misdirected adjustments (add-backs treated as deductions, or vice versa)

## What it does

Given a target company's historical income statements and a list of flagged unusual items, this skill classifies each item as recurring or non-recurring using M&A quality-of-earnings judgment (not just accounting rules), rates the defensibility of each adjustment, builds a period-by-period EBITDA bridge, and outputs a deal-room-standard QofE normalization schedule with narrative rationale per adjustment and an open diligence checklist.

## When to use it

Invoke during buy-side due diligence, after the initial financial review has surfaced unusual or one-time items in the target's income statements and before the adjusted EBITDA figure is presented to the deal team, investment committee, or lender. It is particularly useful when management has provided their own QofE package and you need to independently assess whether their adjustments are defensible.

## Prompt template

```
You are an M&A Transaction Advisory analyst performing a buy-side quality of earnings review.

## Target company
{TARGET_COMPANY_NAME}

## Financial statements
{PASTE_INCOME_STATEMENTS_HERE}
Include all available periods. Format: period headers as columns, line items as rows.
Label the financial basis: Audited / CPA-Reviewed / Management-Prepared.

## Flagged items for QofE review
{LIST_EACH_FLAGGED_ITEM_AS_FOLLOWS}
- Item name: [description]
  Period(s): [which year(s) this item appears]
  Amount: [$XXX — positive if it reduced reported EBITDA, negative if it increased reported EBITDA]
  Management's proposed treatment: [add-back / deduction / not yet proposed]
  Supporting notes: [any context management has provided]

## Instructions

Follow these steps in order:

Step 1 — Reconstruct or verify Reported EBITDA for each period from the income statements provided. If EBITDA is not explicit, calculate it as Net Income + Interest Expense + Income Tax Expense + D&A. Produce a reported EBITDA summary table before proceeding.

Step 2 — For each flagged item, classify it as one of:
  - RECURRING (no adjustment — item is expected to continue post-close)
  - NON-RECURRING ADD-BACK (item reduced reported EBITDA; add it back to get adjusted EBITDA)
  - NON-RECURRING DEDUCTION (item inflated reported EBITDA; deduct it to get adjusted EBITDA)
  - REQUIRES CONFIRMATION (cannot classify without management input — exclude from bridge)
Write a 1–3 sentence QofE rationale for each classification — not just the accounting treatment, but why a buyer would or would not expect this item to recur post-close.

Step 3 — For each Non-Recurring item, assign a defensibility rating:
  - Conservative: clearly one-time, documented, will not be challenged by sell-side or lender
  - Moderate: reasonable but could be contested; documentation may be requested
  - Aggressive: stretch adjustment; sell-side advisor or lender credit team will likely push back
Do not soften Aggressive ratings to make the schedule look cleaner.

Step 4 — Build the EBITDA bridge per period: start from Reported EBITDA, apply each confirmed adjustment in sequence, arrive at Adjusted EBITDA. Show the full walk — do not skip to the total. Keep REQUIRES CONFIRMATION items out of the bridge; show them separately.

Step 5 — If partial-year data is provided, calculate LTM Adjusted EBITDA as: Most Recent Full Year + YTD Current Period − Same Period Prior Year. Show the calculation explicitly.

Step 6 — Compute the defensible range:
  - Conservative case: Conservative add-backs only (minus all deductions)
  - High case: Conservative + Moderate add-backs (minus all deductions)
  - Flag separately: total Aggressive add-backs as % of Reported EBITDA. If >15%, flag as a deal-risk signal.

Step 7 — Output the complete schedule in the format below.

## Output format

Produce three sections:

SECTION A — ADJUSTMENT SCHEDULE
A table with columns: # | Description | Period(s) | Amount ($K) | Classification | Defensibility | Rationale (QofE Basis) | Mgmt Confirmation Required
Show add-backs as positive amounts. Show deductions as negative (parenthetical) amounts.

SECTION B — EBITDA BRIDGE (PER PERIOD)
A table with columns for each period plus LTM. Rows: Reported EBITDA, each individual adjustment line, Adjusted EBITDA (Confirmed), Items Pending Confirmation, Adjusted EBITDA (If Confirmed).

SECTION C — QofE RISK SUMMARY
- Defensible Adjusted EBITDA Range (LTM): Conservative case and High case
- Aggressive adjustment concentration: total Aggressive add-backs as % of Reported EBITDA
- Open Diligence Items: list each REQUIRES CONFIRMATION item with the specific management representation or document needed to resolve it
- Analyst Notes: any income statement irregularities or items outside the flagged list that merit follow-up

Label the output: DRAFT — requires analyst review, management confirmation of flagged items, and deal team sign-off before use in a deal room, offering memorandum, or lending package.
```

## Example output

**SECTION A — ADJUSTMENT SCHEDULE (partial)**

| # | Description | Period(s) | Amount ($K) | Classification | Defensibility | Rationale (QofE Basis) | Mgmt Confirmation Required |
|---|-------------|-----------|-------------|----------------|---------------|------------------------|---------------------------|
| 1 | Owner compensation above market rate | FY2021–FY2023 | $850 | Non-Recurring Add-Back | Moderate | Owner-operator comp of $650K/year is approximately $850K above the estimated market rate for a General Manager role in this industry and revenue band. A buyer would replace with a hired manager at market rate; the excess is a normalization add-back. Requires a comp study or market benchmark to defend the specific amount. | No — but documentation recommended |
| 2 | PPP loan forgiveness income | FY2021 | ($180) | Non-Recurring Deduction | Conservative | Federal COVID-era PPP loan forgiveness was recognized as income in FY2021. This inflated reported EBITDA in that period. A buyer would not expect this income to recur post-close; it must be deducted from FY2021 reported EBITDA, not added back. | No |
| 3 | "Strategic consulting" fees | FY2021–FY2023 | $0 | Recurring | N/A | The company incurred $230K of "strategic consulting" fees in each of the three years reviewed. Recurrence across all periods indicates this is an ongoing business cost, regardless of label. No adjustment warranted. Analyst should investigate the nature of these engagements during management calls. | No |

**SECTION B — EBITDA BRIDGE (partial)**

```
                              FY2021      FY2022      FY2023      LTM
                              --------    --------    --------    --------
Reported EBITDA               $3,820      $4,150      $4,490      $4,610
Add-back: Owner comp (excess) $850        $850        $850        $850
Deduction: PPP income         ($180)      $—          $—          $—
Add-back: ERP implementation  $—          $—          $420        $420
Add-back: Litigation settl.   $—          $—          $310        $310
                              --------    --------    --------    --------
Adjusted EBITDA (Confirmed)   $4,490      $5,000      $6,070      $6,190
Items Pending Confirmation    $95         $95         $95         $95
Adjusted EBITDA (If Confirmed)$4,585      $5,095      $6,165      $6,285
```

**SECTION C — QofE RISK SUMMARY (partial)**

Defensible Adjusted EBITDA Range (LTM):
- Conservative case (Conservative add-backs only): $5,340K
- High case (Conservative + Moderate): $6,190K

## Tips

1. **Always check the direction of one-time income items.** PPP forgiveness, insurance recoveries, and gains on asset sales inflate reported EBITDA in the year they appear. The correct treatment is a deduction, not a neutral pass-through. Misclassifying them as non-adjustments overstates the baseline that lenders will underwrite.

2. **Watch recurring items dressed as one-time.** A cost that appears under a different label every year (e.g., "consulting," "special projects," "transition costs") is recurring regardless of what management calls it. Sort flagged items by period and look for pattern recurrence before assigning a classification.

3. **Supply supporting documentation requests alongside the schedule.** For every REQUIRES CONFIRMATION item and every Moderate or Aggressive adjustment, note exactly what documentation would upgrade its defensibility — a signed comp study, a settlement agreement, an invoice with a non-recurring vendor, or a written management representation. Lenders and buy-side attorneys will ask for this; having the list ready shortens the diligence cycle.
