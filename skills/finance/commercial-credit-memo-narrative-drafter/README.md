# Commercial Credit Memo Narrative Drafter

**Industry**: Finance
**Role**: Commercial Banking Credit Analyst / Underwriter
**Time saved**: 3–6 hours per deal (vs. 4–8 hours manual drafting)

## What it does

Drafts all eight named narrative sections of a commercial credit memorandum — company overview, management, industry analysis, financial performance, credit strengths, risks, mitigants, and recommendation — from your spread data and term sheet, with inline citations to every factual claim and explicit `[ANALYST INPUT REQUIRED]` flags wherever source data is insufficient to support the narrative without judgment.

## When to use it

Invoke immediately after completing the financial spread and gathering the credit agreement term sheet, when you are about to start writing the memo narrative from scratch. You need at minimum: a financial spread (income statement, balance sheet, key ratios for 2–3 years), a term sheet or loan summary, and a description of the borrower's business and industry.

## Prompt template

```
You are a commercial banking credit analyst. Draft a complete commercial credit memorandum narrative from the inputs below. Follow this exact protocol for every section:

1. Before drafting, produce an Input Inventory and Section Coverage Assessment identifying which sections can be fully drafted, which are partial, and which are insufficient based on the provided inputs.

2. Draft each of the following eight sections in sequence:
   I. Company Overview
   II. Management and Ownership
   III. Industry and Sector Analysis
   IV. Financial Performance
   V. Credit Strengths (3–5 items)
   VI. Credit Risks and Concerns (3–5 items, each with a HIGH/MEDIUM/LOW severity label)
   VII. Mitigants (one per risk, with FULL/PARTIAL offset assessment)
   VIII. Recommendation

3. Citation rule: After every factual claim in the narrative, insert a parenthetical citation in this format: [Source: {document name}, {specific field or line}]. If a claim cannot be cited to a provided input, replace it with: [ANALYST INPUT REQUIRED: {describe the specific information needed}].

4. Do not fabricate financial figures, industry statistics, management biographies, or customer names not present in the inputs.

5. Do not draft around data gaps with vague hedge language. If data is missing, insert the [ANALYST INPUT REQUIRED] flag.

6. Close the memo with: "This credit memorandum is an AI-assisted draft. All narratives, citations, and recommendations require analyst review and verification before credit committee submission."

---

INPUTS PROVIDED:

## BORROWER AND LOAN SUMMARY
Borrower legal name: {BORROWER_NAME}
State of incorporation / formation: {STATE_OF_INCORPORATION}
Business description: {BUSINESS_DESCRIPTION}
Industry / SIC code: {INDUSTRY_AND_SIC_CODE}
Proposed loan type and amount: {LOAN_TYPE_AND_AMOUNT}
Proposed tenor: {LOAN_TENOR}
Collateral: {COLLATERAL_DESCRIPTION}
Guarantors: {GUARANTORS}
Proposed rate / pricing: {RATE_AND_PRICING}
Loan purpose: {LOAN_PURPOSE}

## OWNERSHIP AND MANAGEMENT
{OWNERSHIP_STRUCTURE_AND_PRINCIPALS}
(Include: owner names, ownership percentages, titles, years with company, relevant background if available)

## FINANCIAL SPREAD
(Paste the financial spread below — income statement, balance sheet, and key ratios for at least 2 years. Include period labels for all figures.)

{FINANCIAL_SPREAD}

Key ratios calculated (or provide raw data and the skill will calculate):
- DSCR: {DSCR_VALUES_BY_YEAR}
- Leverage (Debt/EBITDA): {LEVERAGE_VALUES_BY_YEAR}
- Current Ratio: {CURRENT_RATIO_BY_YEAR}
- Gross Margin %: {GROSS_MARGIN_BY_YEAR}
- EBITDA Margin %: {EBITDA_MARGIN_BY_YEAR}

## INDUSTRY CONTEXT (optional but recommended for Section III)
{INDUSTRY_MARKET_OVERVIEW}
(If not provided, Section III will contain [ANALYST INPUT REQUIRED] flags for all market characterizations.)

## ADDITIONAL NOTES OR CREDIT OFFICER GUIDANCE (optional)
{ADDITIONAL_CONTEXT}
```

## Example output

The following is a representative excerpt showing the citation and flagging style. This is not full output — a complete memo draft will be substantially longer.

---

**PRE-DRAFT: INPUT INVENTORY AND SECTION COVERAGE**

Input Documents Received:
  1. Borrower and Loan Summary — business description, loan terms, ownership structure
  2. Financial Spread — FY2022, FY2023, FY2024 income statement and balance sheet; calculated ratios
  3. Industry Context — not provided

Section Coverage Assessment:
| Section                  | Coverage Status                                                  |
|--------------------------|------------------------------------------------------------------|
| Company Overview         | PARTIAL — ownership percentages not provided                     |
| Management and Ownership | PARTIAL — management bios not provided                           |
| Industry and Sector      | INSUFFICIENT — no industry input provided                        |
| Financial Performance    | FULL                                                             |
| Credit Strengths         | FULL                                                             |
| Credit Risks             | PARTIAL — customer concentration data not provided               |
| Mitigants                | PARTIAL — depends on risks identified                            |
| Recommendation           | FULL                                                             |

---

**I. COMPANY OVERVIEW**

Acme Precision Manufacturing, LLC ("the Company" or "Acme") is a [ANALYST INPUT REQUIRED: state of formation not provided — confirm legal domicile] limited liability company engaged in the contract manufacture of precision-machined metal components for the industrial equipment and aerospace sectors [Source: Borrower and Loan Summary — Business Description]. The Company was founded in 2007 and has operated from its current facility in Dayton, Ohio for approximately 17 years [Source: Borrower and Loan Summary — Years in Operation]. [ANALYST INPUT REQUIRED: ownership percentages not provided — confirm member interests and whether any ownership changes have occurred in the past 24 months].

---

**IV. FINANCIAL PERFORMANCE (excerpt)**

The Company generated net revenue of $18.4 million in FY2024, representing a 9.5% increase from $16.8 million in FY2023 [Source: Financial Spread, FY2023–FY2024 Income Statement — Revenue]. Gross margin compressed modestly from 34.2% in FY2023 to 32.8% in FY2024 [Source: Financial Spread, FY2023 Gross Profit $5.75M / Revenue $16.8M; FY2024 Gross Profit $6.03M / Revenue $18.4M], reflecting higher steel input costs partially offset by pricing adjustments [ANALYST INPUT REQUIRED: management commentary on margin driver not provided — confirm whether input cost pressure is expected to persist].

---

**VI. CREDIT RISKS AND CONCERNS**

Risk 1 [HIGH]: The Company carries elevated leverage relative to cash flow, with a Debt/EBITDA ratio of 4.1x as of FY2024.
  The FY2024 total funded debt of $7.6 million [Source: Financial Spread, FY2024 Balance Sheet — Long-Term Debt + Current Portion] against EBITDA of $1.85 million [Source: Financial Spread, FY2024 Income Statement — calculated as Net Income $0.72M + D&A $0.43M + Interest $0.70M] yields a leverage ratio of 4.1x, above the 3.5x level commonly considered elevated for mid-market manufacturers.
  Severity rationale: A covenant breach or further EBITDA compression leaves limited cushion for debt service before technical default.

---

## Tips

1. **Provide at least two full fiscal years in the spread.** A single year gives the Financial Performance section nothing to trend against; you will receive flags for every comparative statement. Three years is optimal for a term loan renewal.

2. **Supply industry context as a separate input block.** The Industry and Sector section cannot be grounded without it. A two- to three-sentence market overview from a recent earnings call, industry report, or analyst note is sufficient to anchor the section.

3. **Use the `[ANALYST INPUT REQUIRED]` flags as a checklist.** After receiving the draft, treat each flag as an action item. The flags are designed to tell you exactly what to go find, so they double as a diligence gap tracker before credit committee submission.
