# Scenario 2: Software / SaaS Buyout — Workflow Automation Platform with PIK Toggle Debt

## Context

A vice president at a large-cap PE firm is having a junior associate do the model audit for a proposed take-private of Synaptive Workflow Inc., a mid-market B2B SaaS company providing document automation software to regulated-industry clients (financial services, healthcare). The deal is complex because the debt structure includes a PIK toggle mezz tranche — a structure the AI modeling tool handled inconsistently in a prior deal, so the VP specifically wants the formula audit to focus on PIK accrual mechanics. The firm does not have a formal written convention list, so the associate will use the default standard convention set. The associate provides sector benchmarks from the firm's internal research note on vertical SaaS.

## Input

**DEAL OVERVIEW**
Target company: Synaptive Workflow Inc. (take-private)
Sector: Software / SaaS
Brief business description: B2B vertical SaaS platform for document workflow automation in regulated industries; ~$58M ARR with 92% gross revenue retention, primarily mid-market customers on 1–3 year contracts; EBITDA-positive for three years.

**AI-GENERATED MODEL SUMMARY**

Entry Assumptions:
- LTM EBITDA at close: $29.0M
- Entry multiple: 18.0x EV/EBITDA
- Enterprise value: $522.0M
- Total equity contribution: $209.0M (40% of EV)
- Net debt at close: $313.0M
- LTM ARR at close: $58.0M
- LTM Revenue at close: $62.5M (ARR plus ~$4.5M professional services)
- Management equity rollover: 12% of equity value (~$25.1M)

Debt Structure:
- First Lien Term Loan (FLTL): $175.0M, SOFR+425 bps (floating), 1% annual mandatory amortization, 7-year maturity
- Second Lien Term Loan (SLTL): $88.0M, SOFR+775 bps (floating), bullet maturity Year 8
- Mezzanine Note with PIK Toggle: $50.0M, 12.0% cash pay / 14.0% PIK (at issuer's option), 9-year maturity; model assumes PIK elected in Years 1 and 2, cash pay thereafter
- Revolving Credit Facility: $30.0M total commitment, $30.0M drawn at close, SOFR+375 bps, 6-year maturity
- Total leverage at close: 10.79x ($313.0M / $29.0M LTM EBITDA)
- Total first lien leverage: 6.03x ($175.0M / $29.0M)
- Cash sweep: 75% excess cash flow sweep to FLTL only

Operating Projections (Year 1 through Year 5):
- ARR Growth: Year 1: +18%; Year 2: +22%; Year 3: +25%; Year 4: +23%; Year 5: +20%
- Revenue (total): Year 1: $74.8M; Year 2: $92.9M; Year 3: $117.5M; Year 4: $145.3M; Year 5: $175.1M
- Revenue CAGR Year 1-5: 22.8%
- EBITDA margin: Year 1: 18.0% ($13.5M); Year 2: 22.0% ($20.4M); Year 3: 26.0% ($30.6M); Year 4: 29.0% ($42.1M); Year 5: 31.0% ($54.3M)
- Capex: Year 1: $1.1M (1.5% of revenue); Year 2: $1.4M; Year 3: $1.8M; Year 4: $2.2M; Year 5: $2.6M
- D&A: $8.0M Year 1, growing to $12.0M Year 5 (includes capitalized software amortization)
- Net Working Capital: Negative — ($5.0M) Year 1, growing to ($12.0M) Year 5 (subscription billing in advance)
- Tax rate: 28%
- SOFR assumption: 4.50% flat through hold period

PIK Mechanics as modeled:
- Year 1: $50.0M principal x 14.0% PIK rate = $7.0M accrued to principal; end-of-year mezzanine balance: $57.0M
- Year 2: $57.0M x 14.0% PIK = $7.98M accrued; end-of-year balance: $64.98M
- Year 3 onward: Cash interest on beginning-of-year balance at 12.0%
- Revolver: $30.0M drawn at close; model shows $30.0M balance flat through Year 5 (no paydown modeled)

Exit Assumptions:
- Hold period: 5 years
- Exit multiple: 20.0x EV/EBITDA
- Exit year EBITDA: $54.3M
- Exit enterprise value: $1,086.0M
- Remaining debt at exit: $253.7M (FLTL after amortization and sweep; SLTL bullet; Mezz at $64.98M end Year 2 then grown at 12%; revolver flat at $30.0M)
- Exit equity value: $832.3M

Returns:
- Sponsor gross MOIC: 3.98x ($832.3M / $209.0M)
- Sponsor gross IRR: 32.1%

Cash Flow (Year 2, as representative period):
- EBITDA: $20.4M
- Less: D&A: ($9.0M)
- EBIT: $11.4M
- Less: Cash interest (FLTL + SLTL + revolver; no mezz cash interest in Year 2): ($16.5M)
- EBIT less cash interest: ($5.1M)
- Plus: PIK interest (non-cash): $0 (not added back to FCF)
- Less: Mandatory amortization (FLTL only): ($1.75M)
- Less: Cash taxes: $0 (negative taxable income in Year 2)
- Less: Capex: ($1.4M)
- Plus: Working capital benefit (negative NWC expanding): $2.8M
- Free cash flow before sweep: ($5.45M)
- Cash sweep: $0 (negative FCF)
- Net FCF to balance sheet: ($5.45M)

Model notes from AI tool:
- PIK accrual uses beginning-of-year balance in both Years 1 and 2
- Revolver balance held flat at $30M drawn; no paydown or seasonal draw modeled
- No circular reference — revolver drawn at close and held constant, so no iterative calculation needed
- EBITDA used in leverage covenant test is reported EBITDA; no run-rate or ARR-bridge adjustment
- Management promote: 20% carry above 8% preferred return; not deducted from sponsor returns in model

**FIRM MODELING CONVENTIONS**
[Left blank by associate — use standard top-tier PE/IB default convention set]

**SECTOR BENCHMARKS (OPTIONAL)**
From firm internal research note "Vertical SaaS Buyout Benchmarks — Q1 2026":
- ARR Growth (Year 1-3): 15–25% for mid-market vertical SaaS with 90%+ GRR
- EBITDA Margin at Entry: 15–30% for EBITDA-positive SaaS
- EBITDA Margin at Exit (5-year hold): 28–40% for successful value-creation plan
- Capex as % Revenue: 1–3% (infrastructure-light SaaS)
- Net Working Capital: Negative working capital acceptable; ($8M)–($20M) range at exit for ~$175M revenue
- Entry Multiple (EV/EBITDA): 14–22x for vertical SaaS with 90%+ GRR and mid-market customer base
- First Lien Leverage: 5–7x at close
- Total Leverage: 9–12x acceptable for high-growth SaaS with clear path to deleveraging
- Exit Multiple Range: 18–24x for SaaS with improving margin profile

## Expected Output Criteria

- [ ] Section 1 correctly identifies all four debt tranches including the PIK toggle mezzanine, the drawn revolver balance ($30.0M at close), and flags missing net MOIC / net IRR (management promote exists but is not modeled) as [DATA GAP]
- [ ] Section 2 flags the PIK accrual mechanics as FAIL or NEEDS VERIFICATION: the model correctly accrues PIK but then switches to cash interest on end-Year-2 balance ($64.98M) rather than beginning-of-Year-3 balance — the same $64.98M figure, but the audit should confirm the model's Year 3 cash interest base is the post-accrual Year 2 closing balance, not the original $50.0M face
- [ ] Section 2 flags the revolver as FAIL or NEEDS VERIFICATION: the revolver is drawn $30.0M at close and held flat with no paydown modeled across 5 years, even as FCF turns strongly positive in Years 3–5; this is a material error in a cash sweep model — excess cash should reduce revolver balance
- [ ] Section 2 flags the claim "no circular reference — revolver held constant" as NEEDS VERIFICATION: the correct conclusion depends on whether the model actually has a fixed draw or whether it should dynamically model paydown; a static assumption eliminates the circular but may misstate returns
- [ ] Section 3 benchmarks the model's total leverage of 10.79x against the firm-provided benchmark of 9–12x and marks it Within Range; flags first lien leverage of 6.03x as Within Range against 5–7x benchmark
- [ ] Section 3 benchmarks Year 1 EBITDA margin of 18.0% as Within Range against the 15–30% entry benchmark
- [ ] Section 3 benchmarks Year 5 EBITDA margin of 31.0% against the 28–40% exit benchmark and marks it Within Range (not a deviation)
- [ ] Section 3 benchmarks revenue CAGR of 22.8% as Within Range against the 15–25% ARR growth benchmark
- [ ] Section 4 generates all seven named stress-test scenarios; the Combined Downside scenario for a 10.79x leveraged SaaS deal should clearly show IRR at or near the hurdle (approximately 15–18% range) given the debt load; output must state whether it clears the 20% hurdle
- [ ] Section 4 correctly identifies that the Multiple Contraction scenario (exit multiple -2x, from 20x to 18x) is within the firm's stated exit multiple benchmark range and therefore represents a moderate stress, not an extreme case — and notes this in the scenario findings
- [ ] Section 5 uses the default convention set (10 items) since no firm conventions were provided, and marks at least Convention #6 (net MOIC/IRR not modeled despite management promote existing) as FAIL
- [ ] Section 5 marks Convention #7 (sensitivity tables) as UNVERIFIABLE because the model input does not describe tab structure
- [ ] Executive Summary correctly identifies at least 2 critical FAIL items; status is NEEDS REVISION or SIGNIFICANT REWORK REQUIRED
- [ ] Output does not use phrases like "the deal looks attractive at these returns" or "strong SaaS fundamentals support the assumptions" — the skill must not make investment judgments

## What failure looks like

A failing output would:
- Miss the revolver paydown error — accepting the flat $30.0M revolver balance as reasonable without noting that positive FCF in Years 3–5 should trigger revolver paydown under a cash sweep model
- Validate the PIK mechanics as correct without checking whether the Year 3 cash interest base is explicitly the post-accrual balance (not face value) — passing over the most structurally complex part of the debt schedule
- Apply the wrong sector benchmarks: using the default industrials benchmarks (e.g., 3–7% capex) instead of the user-provided vertical SaaS benchmarks, leading to false MATERIAL flags on capex
- Fail to note that the Combined Downside scenario is particularly severe for a 10.79x leveraged deal and likely breaks the 20% IRR hurdle even with strong revenue growth
- Conflate ARR growth rate with revenue CAGR when benchmarking — ARR growth of 15–25% is provided, but total revenue CAGR includes professional services and may diverge
- Produce a narrative paragraph in Section 3 instead of the required benchmark table
- Omit Section 6 entirely or list only one data gap despite the missing net returns data being a clear gap
