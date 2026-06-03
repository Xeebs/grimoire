# Scenario 2: Commercial Real Estate Bridge Loan — LTV Breach and Ambiguous NOI Definition

## Context

A portfolio manager at a commercial real estate debt fund is reviewing the semi-annual compliance package for Harborview Logistics Center LLC, the borrower on a $52M floating-rate bridge loan secured by a Class B industrial warehouse complex in Memphis, Tennessee. The loan was originated in January 2023 with an 18-month initial term, now extended to a 36-month maturity. The borrower has submitted a Q2 2024 rent roll and trailing six-month operating statement. The portfolio manager needs to check the LTV covenant and the DSCR covenant before the August 15, 2024 compliance deadline. A third covenant — Minimum Debt Yield — is specified in the agreement but the borrower has not provided an appraisal value in this submission. The portfolio manager suspects the LTV may be in breach given recent cap rate expansion in the Memphis industrial market.

---

## Input

### CREDIT AGREEMENT EXCERPTS
**Borrower:** Harborview Logistics Center LLC
**Lender:** Bridgewater Real Estate Debt Fund III
**Facility:** $52,000,000 Floating Rate Bridge Loan
**Agreement Date:** January 10, 2023
**Maturity (as extended):** January 10, 2026

---

**ARTICLE I — DEFINITIONS (Excerpts)**

**"Net Operating Income"** or **"NOI"** means, for any period, all rental income and other operating income collected from tenants at the Property during such period (excluding (i) security deposits unless applied, (ii) lease termination fees in excess of one month's base rent, and (iii) interest income), less all operating expenses paid during such period, including property taxes, insurance, utilities (to the extent not reimbursed by tenants), property management fees, and routine maintenance and repair costs, but excluding debt service, depreciation, capital expenditures, and income taxes. NOI shall be calculated on a cash basis.

**"Appraised Value"** means the most recent "as-is" appraised value of the Property as determined by an MAI-certified appraiser acceptable to Lender, which appraisal shall have been conducted within the preceding 12 months. If no qualifying appraisal has been conducted within the preceding 12 months, Lender may, at its discretion, commission a new appraisal at Borrower's expense.

**"Loan-to-Value Ratio"** or **"LTV"** means, as of any date of determination, the ratio (expressed as a percentage) of (a) the then-outstanding principal balance of the Loan to (b) the Appraised Value of the Property.

**"Debt Service Coverage Ratio"** or **"DSCR"** means, for any period, the ratio of (a) Net Operating Income for such period, annualized, to (b) the total amount of interest expense (cash only, excluding any default interest) on the Loan accrued during such period, annualized. For the avoidance of doubt, DSCR shall be tested on a trailing six-month basis, annualized.

**"Debt Yield"** means the ratio (expressed as a percentage) of (a) annualized NOI to (b) the outstanding principal balance of the Loan.

---

**ARTICLE VI — FINANCIAL COVENANTS**

**Section 6.01(a) — Maximum LTV.** The Borrower shall not permit the Loan-to-Value Ratio to exceed 70.0% as of each semi-annual test date (June 30 and December 31 of each calendar year). In the event the LTV Covenant is breached, Borrower shall have 45 days to cure by (i) making a principal paydown sufficient to bring the LTV into compliance, or (ii) providing additional collateral acceptable to Lender.

**Section 6.01(b) — Minimum DSCR.** The Borrower shall not permit the DSCR to be less than 1.10 to 1.00, tested semi-annually as of June 30 and December 31 of each calendar year.

**Section 6.01(c) — Minimum Debt Yield.** The Borrower shall maintain a Debt Yield of not less than 8.50%, tested semi-annually as of June 30 and December 31.

---

### BORROWER FINANCIAL SUBMISSION
**Reporting Period:** Six months ended June 30, 2024
**Submitted by:** Harborview Logistics Center LLC, Asset Manager

**RENT ROLL — As of June 30, 2024**

| Tenant | Suite | Sq Ft | Monthly Base Rent | Lease Expiry | Status |
|---|---|---|---|---|---|
| Memphis Distribution Co. | Bldg A | 180,000 | $126,000 | Dec 2026 | Occupied |
| SunState Freight LLC | Bldg B | 95,000 | $61,750 | Mar 2025 | Occupied |
| Vacant | Bldg C | 60,000 | — | — | Vacant since Feb 2024 |
| Total | | 335,000 | $187,750/mo | | |

**OPERATING STATEMENT — Six Months ended June 30, 2024**
(All figures in $000s)

| Line Item | H1 2024 |
|---|---|
| Base Rent Collected | $1,127 |
| Tenant Reimbursements (NNN recoveries) | $312 |
| Lease Termination Fee (SunState, received May 2024) | $185 |
| Miscellaneous Income | $18 |
| Total Revenue | $1,642 |
| Property Taxes | ($198) |
| Insurance | ($62) |
| Utilities (unreimbursed) | ($24) |
| Property Management Fees (3% of base rent) | ($34) |
| Routine Maintenance & Repairs | ($47) |
| Capital Expenditure — Roof Repair (Bldg A) | ($210) |
| Total Operating Expenses | ($575) |
| Net Income (as reported by borrower) | $1,067 |

**DEBT SERVICE — Six Months ended June 30, 2024**

| Item | H1 2024 |
|---|---|
| Cash Interest Paid (SOFR + 350bps, avg rate 8.92%) | $2,319 |
| Default Interest Accrued (breach of reserve requirement, Q1 2024) | $48 |
| Total Interest Charges | $2,367 |

**NOTE FROM BORROWER:** The most recent appraisal of the Property was conducted in November 2022 (value: $78,500,000). A new appraisal has been ordered but is not yet complete. The borrower requests the November 2022 appraisal be used for the June 30, 2024 compliance test.

**Outstanding Loan Balance as of June 30, 2024:** $51,200,000

---

## Expected Output Criteria

- [ ] Section 1 correctly extracts all three covenants: LTV (§6.01a, ≤70%), DSCR (§6.01b, ≥1.10x TTM-6mo annualized), and Debt Yield (§6.01c, ≥8.50%)
- [ ] Section 1 correctly notes the 45-day cure right for LTV (principal paydown or additional collateral) and absence of cure rights for DSCR and Debt Yield
- [ ] Section 2 correctly excludes the $185K lease termination fee from NOI (per §1.01 definition: "lease termination fees in excess of one month's base rent" — one month's base rent for SunState is approximately $61,750, so the $185K fee significantly exceeds one month and should be excluded)
- [ ] Section 2 correctly excludes the $210K capital expenditure from operating expenses (CapEx is explicitly excluded from the NOI definition)
- [ ] Section 2 correctly excludes the $48K default interest from DSCR denominator (definition specifies "excluding any default interest")
- [ ] Section 2 flags the November 2022 appraisal as a [DATA GAP] — the definition requires an appraisal "within the preceding 12 months" and the November 2022 appraisal is 19 months old as of June 2024, making it non-qualifying; this renders the LTV and Debt Yield covenants INCOMPLETE
- [ ] Section 3 calculates NOI correctly: Base rent $1,127 + NNN recoveries $312 + Misc income $18 − property taxes $198 − insurance $62 − utilities $24 − mgmt fees $34 − maintenance $47 = $1,092K for H1 2024; annualized = $2,184K
- [ ] Section 3 calculates DSCR correctly: Annualized NOI $2,184K / Annualized cash interest (excluding default interest) $4,638K = 0.47x
- [ ] Section 4 marks DSCR as FAIL — BREACH (0.47x calculated vs. 1.10x required)
- [ ] Section 4 marks LTV as INCOMPLETE (no qualifying appraisal) rather than using the stale 2022 value
- [ ] Section 4 marks Debt Yield as INCOMPLETE (no qualifying appraisal for outstanding balance denominator — note: Debt Yield uses loan balance, not appraised value, so this should actually be calculable; the skill should recognize that Debt Yield = Annualized NOI / Loan Balance = $2,184K / $51,200K = 4.27% — FAIL)
- [ ] Section 5 flags the DSCR breach as critical and notes there is no cure period for this covenant
- [ ] Section 6 raises an explicit open item: the stale appraisal means LTV cannot be calculated per the contract definition — lender must commission a new appraisal at borrower's expense per §1.01; this is an action item, not a calculation matter
- [ ] Section 6 raises an open item about the lease termination fee exclusion and asks borrower to confirm the one-month base rent threshold calculation
- [ ] The certificate labels the DSCR and Debt Yield as FAIL — BREACH and notes the absence of any cure right for either

## What failure looks like

A failing output would:
- Include the $185K lease termination fee in NOI without flagging the contractual exclusion threshold
- Include the $210K capital expenditure as an operating expense deduction (it is explicitly excluded from NOI)
- Include the $48K default interest in the DSCR denominator
- Accept the November 2022 appraisal at face value and produce an LTV calculation of 65.2% ($51.2M / $78.5M) without flagging the 12-month staleness requirement
- Miss the Debt Yield covenant entirely or mark it INCOMPLETE when the loan balance (not appraised value) is the correct denominator
- Fail to flag the DSCR breach as lacking a cure period
- Produce an overall "PASS" or incomplete compliance summary that obscures the severity of the DSCR shortfall (0.47x vs. 1.10x required)
