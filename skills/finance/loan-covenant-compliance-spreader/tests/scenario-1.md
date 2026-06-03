# Scenario 1: Leveraged Buyout Portfolio Company — TTM DSCR and Leverage Covenant Near Breach

## Context

A credit analyst at a mid-market direct lending fund is processing the Q3 2024 quarterly compliance package for Apex Packaging Solutions LLC, a portfolio company owned by Crestwood Equity Partners. The borrower is a $95M senior secured term loan originated in June 2021, now in Year 4 of a 6-year term. EBITDA has softened over the past two quarters due to volume declines in the consumer goods sector. The analyst suspects the Debt Service Coverage Ratio may be near breach and wants to verify before the October 20, 2024 certificate deadline.

The credit agreement uses a custom definition of "Consolidated EBITDA" that includes add-backs for non-recurring restructuring charges (capped at $2,000,000 per year) and non-cash stock compensation. The agreement also has a DSCR step-down schedule: ≥ 1.30x through Q4 Year 3, then ≥ 1.20x from Q1 Year 4 onward. A 30-day equity cure right applies to the DSCR covenant only.

---

## Input

### CREDIT AGREEMENT EXCERPTS
**Borrower:** Apex Packaging Solutions LLC
**Lender:** Crestwood Direct Lending Fund II, LP
**Facility:** $95,000,000 Senior Secured Term Loan B
**Agreement Date:** June 1, 2021

---

**ARTICLE I — DEFINITIONS (Excerpts)**

**"Consolidated EBITDA"** means, for any period, the Consolidated Net Income of the Borrower and its Subsidiaries for such period, plus (without duplication) the sum of the following to the extent deducted in determining Consolidated Net Income for such period: (a) Consolidated Interest Expense; (b) income tax expense; (c) depreciation and amortization expense; (d) non-cash charges, including non-cash stock-based compensation expense; and (e) non-recurring restructuring and integration charges, provided that the aggregate amount added back pursuant to this clause (e) shall not exceed $2,000,000 in any trailing twelve-month period. For the avoidance of doubt, "Consolidated EBITDA" shall not include any gains on asset sales or insurance proceeds in excess of $500,000.

**"Consolidated Debt Service"** means, for any period, the sum of (a) Consolidated Interest Expense paid or payable in cash during such period, plus (b) scheduled principal payments on the Term Loan actually made during such period (excluding any voluntary prepayments).

**"Senior Secured Leverage Ratio"** means, as of any date of determination, the ratio of (a) Total Senior Secured Debt as of such date to (b) Consolidated EBITDA for the Trailing Twelve Month Period ending on such date.

**"Total Senior Secured Debt"** means, as of any date, the aggregate outstanding principal amount of all Indebtedness of the Borrower and its Subsidiaries that is secured by a first-priority Lien on the Collateral, including the Term Loan.

---

**ARTICLE VII — FINANCIAL COVENANTS**

**Section 7.01(a) — Minimum Debt Service Coverage Ratio.** The Borrower shall not permit the Debt Service Coverage Ratio, measured as of the last day of each fiscal quarter on a Trailing Twelve Month basis, to be less than:
- 1.30 to 1.00 from the Closing Date through and including the fiscal quarter ending December 31, 2023
- 1.20 to 1.00 for each fiscal quarter ending on or after March 31, 2024

**Equity Cure.** In the event of a failure to maintain the minimum Debt Service Coverage Ratio required under Section 7.01(a), the Borrower shall have the right, within 30 days following the applicable test date, to cure such failure by causing the direct or indirect equity holders to contribute cash equity to the Borrower (an "Equity Cure Contribution"), which contribution shall be deemed to increase Consolidated EBITDA for the applicable Trailing Twelve Month Period solely for purposes of this Section 7.01(a). Each Equity Cure Contribution may not be used more than twice during the term of the Loan.

**Section 7.01(b) — Maximum Senior Secured Leverage Ratio.** The Borrower shall not permit the Senior Secured Leverage Ratio, measured as of the last day of each fiscal quarter on a Trailing Twelve Month basis, to exceed 5.25 to 1.00. No cure right applies to this covenant.

---

### BORROWER FINANCIAL SUBMISSION
**Reporting Period:** Trailing Twelve Months ended September 30, 2024
**Submitted by:** Apex Packaging Solutions LLC Finance Department

**INCOME STATEMENT — TTM ended September 30, 2024**
(All figures in $000s)

| Line Item | TTM Q3 2024 |
|---|---|
| Net Revenue | $124,350 |
| Cost of Goods Sold | ($87,040) |
| Gross Profit | $37,310 |
| SG&A Expenses | ($12,880) |
| Stock-Based Compensation (non-cash) | ($1,450) |
| Restructuring Charges | ($2,750) |
| Depreciation & Amortization | ($6,200) |
| EBIT | $14,030 |
| Interest Expense (cash) | ($8,400) |
| Interest Expense (non-cash PIK) | ($620) |
| Income Tax Expense | ($1,820) |
| Net Income | $3,190 |

**BALANCE SHEET — As of September 30, 2024**
(All figures in $000s)

| Line Item | Sept 30, 2024 |
|---|---|
| Total Assets | $186,200 |
| Senior Secured Term Loan (outstanding) | $81,500 |
| Total Debt | $81,500 |

**DEBT SERVICE SCHEDULE — TTM ended September 30, 2024**
(All figures in $000s)

| Item | TTM Q3 2024 |
|---|---|
| Scheduled principal payments (Term Loan) | $9,500 |
| Cash interest paid (Term Loan) | $8,400 |
| Total Cash Debt Service | $17,900 |

**NOTE:** The $2,750,000 restructuring charge relates to the closure of the Newark, NJ facility in Q1 2024. The borrower is presenting this as a non-recurring charge and including the full amount in the EBITDA add-back.

---

## Expected Output Criteria

- [ ] Section 1 correctly identifies both financial covenants (DSCR §7.01(a) and Senior Secured Leverage Ratio §7.01(b)) with verbatim formula definitions
- [ ] Section 1 correctly identifies and notes the DSCR step-down schedule (1.30x pre-Q1-2024, 1.20x from Q1-2024 onward) and applies the 1.20x threshold to Q3 2024
- [ ] Section 1 correctly identifies the equity cure right on DSCR and the absence of a cure right on the leverage ratio
- [ ] Section 2 correctly identifies that the $2,750,000 restructuring charge exceeds the $2,000,000 cap, meaning only $2,000,000 can be added back per the §1.01 definition
- [ ] Section 2 correctly excludes non-cash PIK interest ($620K) from Consolidated Debt Service (since the definition specifies "paid or payable in cash")
- [ ] Section 3 calculates Consolidated EBITDA as: Net Income $3,190 + Cash Interest $8,400 + PIK Interest $620 + Tax $1,820 + D&A $6,200 + Stock comp $1,450 + Restructuring (capped) $2,000 = $23,680K
- [ ] Section 3 calculates Consolidated Debt Service as: Scheduled principal $9,500 + Cash interest $8,400 = $17,900K (PIK excluded)
- [ ] Section 3 calculates DSCR = $23,680K / $17,900K = 1.32x, Status: PASS (above 1.20x threshold)
- [ ] Section 3 calculates Senior Secured Leverage Ratio = $81,500K / $23,680K = 3.44x, Status: PASS (below 5.25x threshold)
- [ ] Section 5 (Breach-Proximity Alerts) flags the DSCR at 10.0% headroom above the 1.20x threshold as a monitoring concern, given the restructuring add-back cap is already being hit
- [ ] Section 6 raises an explicit open item: the borrower claimed $2,750K restructuring add-back but only $2,000K is permitted; requests confirmation that the borrower understands the cap and has adjusted their own certificate accordingly
- [ ] Section 6 raises an open item about whether the PIK interest should be included in Consolidated Interest Expense for EBITDA purposes (it was deducted to reach Net Income, so it technically flows into the add-back), noting the definition says "paid or payable in cash" only applies to the Debt Service denominator — requires analyst confirmation
- [ ] The output is clearly labeled DRAFT requiring analyst review and sign-off

## What failure looks like

A failing output would:
- Apply a textbook DSCR formula (e.g., NOI / total debt obligations) instead of the contract-specific definition
- Accept the borrower's $2,750K restructuring add-back without flagging the $2,000K cap
- Include PIK interest in Consolidated Debt Service (incorrectly increasing the denominator)
- Apply the 1.30x DSCR threshold instead of the 1.20x step-down that applies from Q1 2024
- Produce a compliance summary without exposing the restructuring cap issue in Section 6
- Miss the DSCR breach-proximity alert given the add-back cap constraint
