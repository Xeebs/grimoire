# Scenario 2: SaaS Company — Buy-Side QofE with Partial-Year LTM, Recurring Credits, and SBC Add-Back Mechanics

## Context

A private equity associate at a growth equity fund is performing buy-side quality of earnings on Viridian Analytics Inc., a $12M ARR B2B SaaS company providing data analytics software to mid-market logistics companies. The fund is evaluating a Series C-equivalent growth buyout. The deal is pre-LOI; the associate needs to produce a draft QofE normalization schedule to support the investment committee memo's adjusted EBITDA section.

The company has provided two full years of financials (FY2022, FY2023) plus an 8-month partial year (January–August 2024). The associate must calculate LTM Adjusted EBITDA using the standard LTM formula. Several of the flagged items are SaaS-specific, including stock-based compensation and R&D tax credits — areas where QofE treatment is frequently contested between buy-side and sell-side advisors.

---

## Input

### TARGET COMPANY OVERVIEW
**Company:** Viridian Analytics Inc.
**Industry:** B2B SaaS — Supply Chain Analytics
**ARR:** $12.0M (as of August 2024)
**Ownership:** Founder-led; 3 institutional investors; no majority control
**Financial basis:** CPA-reviewed (FY2022, FY2023); Management-prepared (YTD Aug 2024)
**Periods provided:** FY2022, FY2023, YTD Aug 2024 (8 months)

---

### INCOME STATEMENTS
(All figures in $000s)

| Line Item                                  | FY2022    | FY2023    | YTD Aug 2024 (8 mo.) |
|--------------------------------------------|-----------|-----------|----------------------|
| Software Revenue (Subscriptions)           | $8,400    | $10,700   | $8,050               |
| Professional Services Revenue              | $1,100    | $1,300    | $900                 |
| Total Revenue                              | $9,500    | $12,000   | $8,950               |
| Cost of Revenue                            | ($2,850)  | ($3,480)  | ($2,620)             |
| Gross Profit                               | $6,650    | $8,520    | $6,330               |
| R&D Expense (net of credits)               | ($2,400)  | ($2,800)  | ($2,050)             |
| Sales & Marketing                          | ($1,980)  | ($2,350)  | ($1,720)             |
| General & Administrative                   | ($1,250)  | ($1,430)  | ($1,060)             |
| Stock-Based Compensation (non-cash)        | ($550)    | ($620)    | ($490)               |
| SOC 2 Audit & Compliance Build-Out         | —         | ($195)    | —                    |
| Enterprise Customer Acquisition Costs      | —         | ($450)    | —                    |
| Loss on Disposal — Legacy Infrastructure   | —         | ($390)    | —                    |
| EBIT                                       | $470      | $285      | ($990)               |
| Interest Expense                           | ($85)     | ($110)    | ($70)                |
| R&D Tax Credits Received                   | $175      | $175      | —                    |
| Income Tax Expense (benefit)               | $20       | ($35)     | $45                  |
| Net Income (Loss)                          | $580      | $315      | ($1,015)             |

**Notes from management's QofE package:**
- Stock-based compensation is non-cash and represents equity grants to employees; management proposes adding back in full each year
- SOC 2 audit and compliance build-out of $195K occurred in FY2023 as a one-time infrastructure investment; the ongoing maintenance cost will be substantially lower
- Enterprise customer acquisition costs of $450K in FY2023 relate to a single large contract (a Fortune 500 logistics company) that required custom onboarding and dedicated implementation resources; management does not expect comparable costs for future enterprise customers
- Founder salary of $280K/year in FY2023 (included in G&A) is estimated by management to be approximately $280K above a market-rate VP Engineering / CEO salary for a company of this size; management proposes an add-back of $280K
- R&D tax credits of $175K received in FY2022 and $175K in FY2023 are presented as a neutral item in management's package; no adjustment proposed
- Loss on disposal of legacy infrastructure of $390K in FY2023 relates to the retirement of on-premise server hardware as the company completed its cloud migration; management proposes adding back

---

### FLAGGED ITEMS FOR QofE REVIEW

1. **Stock-based compensation (non-cash)**
   - Period(s): FY2022 ($550K), FY2023 ($620K), YTD Aug 2024 ($490K)
   - Amount: as listed per period
   - Management's proposed treatment: Non-Recurring Add-Back
   - Notes: Represents equity grants (options and RSUs) to employees and management; non-cash; disclosed in the financials as a separate line item below operating expenses

2. **SOC 2 audit & compliance build-out**
   - Period(s): FY2023 only
   - Amount: $195K
   - Management's proposed treatment: Non-Recurring Add-Back
   - Notes: Engaged a Big 4 firm for SOC 2 Type II readiness and certification in FY2023; certification achieved; ongoing annual recertification cost estimated at $30–$40K

3. **Enterprise customer acquisition costs — single contract**
   - Period(s): FY2023 only
   - Amount: $450K
   - Management's proposed treatment: Non-Recurring Add-Back
   - Notes: Specific to the onboarding of a single Fortune 500 client signed in Q2 2023; management characterizes these as one-time; no comparable enterprise deal in FY2022 or YTD 2024

4. **Founder salary above market rate**
   - Period(s): FY2022, FY2023, YTD Aug 2024
   - Amount: $280K/year estimated excess
   - Management's proposed treatment: Non-Recurring Add-Back
   - Notes: Founder serves as CEO; current salary $480K; management estimates market-rate CEO comp for a $12M ARR SaaS company at $200K; no independent comp study; the founder's dual role as technical lead (formerly VP Engineering) complicates the benchmark

5. **R&D tax credits received**
   - Period(s): FY2022 ($175K), FY2023 ($175K)
   - Amount: $175K/year
   - Management's proposed treatment: Not proposed (presented as neutral)
   - Notes: R&D tax credits received in cash under the federal R&D credit program (IRC §41); same dollar amount both years; company expects to continue qualifying activities and receiving credits going forward

6. **Loss on disposal of legacy infrastructure**
   - Period(s): FY2023 only
   - Amount: $390K
   - Management's proposed treatment: Non-Recurring Add-Back
   - Notes: Book loss on retirement of on-premise hardware as part of cloud migration completed in Q4 2023; cloud migration is complete; no further hardware disposals anticipated

---

## Expected Output Criteria

- [ ] Section A correctly classifies stock-based compensation as a Non-Recurring Add-Back rated Conservative, with rationale explaining that SBC is a non-cash charge that does not represent a cash cost to the business and is standard practice to add back in SaaS QofE — while noting that the buyer will incur future SBC expense post-close and that this add-back does not eliminate the ongoing equity dilution
- [ ] Section A correctly classifies R&D tax credits ($175K/year in both FY2022 and FY2023) as RECURRING — not as a neutral item and not as an add-back or deduction — with rationale citing identical dollar amounts in both years and management's expectation of continued qualification, concluding that a buyer should expect this credit income to continue post-close and it is already reflected in (as a benefit to) reported EBITDA; no adjustment warranted
- [ ] Section A correctly classifies the SOC 2 build-out ($195K, FY2023 only) as a Non-Recurring Add-Back rated Conservative, with rationale noting the distinction between the one-time certification build-out cost and the ongoing recertification cost (~$30–40K), and that only the incremental one-time portion is an appropriate add-back
- [ ] Section A correctly classifies the enterprise customer acquisition costs ($450K, FY2023 only) as a Non-Recurring Add-Back rated Moderate, with rationale noting that while the cost was specific to a single contract, the characterization of enterprise onboarding as non-recurring is a common area of sell-side pushback in SaaS QofEs since the company's growth strategy may involve more enterprise deals
- [ ] Section A classifies the founder salary excess ($280K/year) as either REQUIRES CONFIRMATION or Non-Recurring Add-Back rated Moderate, with rationale noting the absence of an independent comp study, the complexity of benchmarking a founder CEO with a dual technical/executive role, and that the $200K market rate assumption provided by management is likely understated for this ARR level — the specific deliverable needed is an independent comp study from a SaaS compensation benchmarking source
- [ ] Section A correctly classifies the loss on disposal of legacy infrastructure ($390K, FY2023) as a Non-Recurring Add-Back rated Conservative, noting the cloud migration is complete and documented and no further hardware disposals are anticipated
- [ ] Section B shows the EBITDA bridge for FY2022, FY2023, and YTD Aug 2024 (not annualized — shown as actual 8-month figures)
- [ ] Section B includes a separate LTM column calculated explicitly as FY2023 + YTD Aug 2024 − Jan–Aug 2023 equivalent (i.e., the standard LTM formula). If the Jan–Aug 2023 period is not provided separately in the input, the skill must note this gap and either request the data or show the LTM as estimated with the assumption stated explicitly
- [ ] Section B correctly includes the SBC add-back in each period including YTD, correctly excludes R&D tax credits from any adjustment line (they are Recurring — the bridge reflects them as-is in the Reported EBITDA baseline), and correctly shows the $390K loss on disposal as a positive add-back in FY2023 only
- [ ] Section C correctly identifies that the R&D tax credits should not be added back (management presented them as neutral, which is correct; the output should confirm neutral treatment and explain why, rather than silently ignoring them)
- [ ] Section C provides a Conservative case and High case for LTM Adjusted EBITDA
- [ ] Section C flags whether Aggressive adjustment concentration is triggered (it should not be, as no items are classified Aggressive — the highest-rated contested item is Moderate)

## What failure looks like

A failing output would:
- Add back the R&D tax credits as a non-recurring item (they are recurring and should not be adjusted; adding them back would double-count income)
- Treat the R&D tax credits as a Non-Recurring Deduction (also wrong — they are expected to recur and are already in the reported EBITDA baseline)
- Annualize the YTD Aug 2024 figures without disclosing the methodology, or present annualized YTD as LTM
- Classify the founder salary excess as Conservative without noting the absence of a comp study
- Classify SBC as Recurring (some non-QofE financial analysts do this) rather than correctly adding it back as a non-cash non-recurring item
- Produce a single aggregate adjusted EBITDA figure without showing period-by-period bridges
- Miss the LTM calculation requirement and report only FY2023 as the proxy for LTM without disclosing the limitation
- Apply the same $390K loss on disposal add-back to FY2022 (it occurred in FY2023 only)
