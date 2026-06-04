# Scenario 2: AI-Assisted Prior Authorization Workflow Tooling — Health Plan Market Entry

## Context

A healthcare AI software company is evaluating entry into the US market for AI-assisted prior authorization (PA) workflow tooling sold to mid-size health plans. The product automates the administrative burden of PA review queues — routing incoming PA requests, pre-populating clinical criteria checklists, and flagging auto-approvable requests — for health plan medical management teams. The company has completed a pilot with two regional health plans and is now commissioning a market sizing analysis to support its Series B fundraise and board strategy presentation.

The consulting team must size the market using the healthcare sector benchmark sources from the reference guide (CMS enrollment data, AHIP plan counts, Definitive Healthcare), construct both a bottoms-up model using a health plan count ICP, and a top-down model using CMS national health expenditure context, then produce a slide-ready exhibit with the reconciliation and sensitivity analysis.

The ICP is defined by health plan characteristics, not by member count alone — a structural difference from the standard company-size ICP, which requires the consultant to segment by plan type and adjust the average deal size by plan size within the ICP band.

## Input

**Target market description**: AI-assisted prior authorization workflow software sold to US commercial health plans with 50,000–500,000 covered lives (mid-size health plans), across plan types including regional/local HMO, PPO, and BCBS affiliates. Excludes Medicare Advantage-only plans (different PA regulatory environment), Medicaid managed care (different budget cycle and procurement), and the five largest national carriers (United, Aetna, Cigna, Humana, BCBS national) which operate at enterprise scale requiring direct enterprise procurement. Target geography: United States only.

**Industry sector**: Healthcare / MedTech

---

**ICP definition**: US commercial health plans with 50,000–500,000 covered lives (per CMS enrollment data), excluding Medicare Advantage-only plans, Medicaid-only managed care organizations, and plans with >500,000 commercial lives (enterprise tier). Must have an active prior authorization program managing inpatient, outpatient procedure, and specialty pharmaceutical PA requests.

**Segments**:

| Segment | ICP Count | ICP Count Source | Avg Deal Size (ACV) | Win Rate |
|---------|-----------|-----------------|---------------------|---------|
| Mid-Size Plans (50K–150K lives) | 180 | CMS 2024 Health Insurance Exchange Enrollment Data + AHIP 2024 Health Insurance Coverage Report: 180 commercial insurers in the 50K–150K life band, excluding Medicare Advantage-only and Medicaid-only plans | $185,000 | 15% |
| Regional Plans (150K–500K lives) | 95 | CMS 2024 Health Insurance Exchange Enrollment Data + AHIP 2024 Health Insurance Coverage Report: 95 commercial insurers in the 150K–500K life band, same exclusions applied | $420,000 | 12% |

**Win rate basis**: Comparable health IT SaaS point solutions in the PA adjacency (PA status tracking, clinical decision support tooling for utilization management): KLAS Research 2023 health plan technology adoption report shows 12–16% first-year win rates for point solution vendors entering mid-size health plan segment without incumbent relationships.

---

**Industry TAM source**:
- Source 1: CMS National Health Expenditure Accounts 2023, "Net Cost of Health Insurance" category: $334.4 billion in total health insurance administrative cost (all payers, all plan types, US)
- Source 2: McKinsey Health Institute 2024, prior authorization administrative burden estimate: $35B annually in US prior authorization processing costs across all payer types (commercial + Medicare + Medicaid), with commercial health plan share estimated at 58% (~$20.3B)

**Addressable percentage (SAM/TAM)**:
- Using CMS NHEA as the top-down TAM base ($334.4B total health insurance administrative cost): The PA administrative function represents approximately 6% of total health plan administrative cost per Milliman 2023 health plan cost structure analysis. Mid-size commercial plans (50K–500K lives) represent approximately 18% of total commercial health plan covered lives per CMS enrollment data. Therefore SAM = $334.4B × 6% (PA function) × 18% (mid-size commercial) × 35% (software-addressable fraction of PA admin per KLAS 2023) = addressable_pct ≈ 0.38% of NHEA base

Note: The McKinsey $20.3B commercial PA cost base provides a more directly applicable starting point. Using McKinsey as the TAM base: mid-size commercial share = 18% of lives × 1.1 cost loading factor (mid-size plans have higher per-member PA admin cost per Milliman 2023) = approximately 20% addressable; software-addressable fraction = 35% of PA admin cost per KLAS 2023 = SAM as a fraction of McKinsey TAM ≈ 7.0% (0.20 × 0.35)

**For this analysis**, use the McKinsey $20.3B commercial PA cost estimate as the top-down TAM (it is more directly scoped than CMS NHEA). Apply addressable_pct = 0.07 (7.0% per the methodology above). Apply capturable_pct = 0.035 (3.5% of SAM — rationale: health IT point solution market share trajectory for first-mover vendors in an emerging automation category, per KLAS 2023 reference range of 2–5% for well-positioned entrants in years 1–3).

**Capturable percentage (SOM/SAM)**: 3.5% as stated above.

---

**Conflicting sources**:
- CMS NHEA $334.4B: Total administrative cost for all insurance (commercial + government, all functions)
- McKinsey $20.3B: Commercial PA-specific processing cost only
- These are not measuring the same thing; CMS NHEA is an inappropriate direct TAM for this product category. The analysis must note this and use McKinsey as the operative top-down base, with CMS NHEA cited as context only.

## Expected Output Criteria

- [ ] Bottoms-up TAM computed correctly: Mid-size segment TAM = 180 × $185,000 = $33,300,000; Regional segment TAM = 95 × $420,000 = $39,900,000; Total bottoms-up TAM = $73,200,000 (within ±$1,000 rounding tolerance)
- [ ] Bottoms-up SOM computed correctly: Mid-size SOM = $33.3M × 15% = $4,995,000; Regional SOM = $39.9M × 12% = $4,788,000; Total SOM = $9,783,000 (~$9.8M) (within ±$5,000 tolerance)
- [ ] Top-down model correctly uses McKinsey $20.3B as TAM (not the CMS NHEA $334.4B), with the reasoning documented: CMS NHEA is total insurance admin cost, not PA-specific; McKinsey's $20.3B is the appropriate PA-cost-based TAM for this product
- [ ] Top-down SAM = $20.3B × 7.0% = $1,421,000,000 ($1.42B); SOM = $1.42B × 3.5% = $49,700,000 (~$49.7M)
- [ ] Reconciliation gap identified: Top-down TAM ($20.3B) >> Bottoms-up TAM ($73.2M) — gap exceeds 50%, classified as INCONSISTENT; output explains this is expected because McKinsey's $20.3B represents the total cost base (revenue opportunity context), not a count of software licenses that can be sold to ICP accounts
- [ ] Reconciliation narrative correctly recommends bottoms-up as the planning figure: the bottoms-up model is grounded in actual plan counts and ACV data; the top-down is a cost-displacement ceiling, not a customer revenue model; the consultant should use bottoms-up TAM ($73.2M) for pipeline and GTM planning
- [ ] Output applies the healthcare benchmark source guide correctly: cites CMS enrollment data and AHIP plan count data as sources, notes McKinsey Health Institute as the PA cost source, does not conflate CMS NHEA administrative cost data with a direct product revenue TAM
- [ ] At minimum 3 sensitivity flags identified: ICP count (health plan count), avg deal size (ACV), and win rate; tornado chart data table present with at least 3 inputs sorted by full swing descending
- [ ] Output explicitly flags that the addressable_pct assumption (7.0% of McKinsey TAM) carries low source confidence — it is derived from a chain of three multiplied estimates (PA share × mid-size share × software fraction), each with its own margin of error; recommends this as a priority validation item
- [ ] Slide-ready exhibit format: TAM/SAM/SOM table present with both methods; must show the dramatic scale difference between methods and explain why this does not invalidate the analysis
- [ ] Source-cited assumptions table present with all 6+ numerical assumptions, each with a source citation; Confidence level column distinguishes CMS and AHIP plan count data (High) from McKinsey cost estimate and KLAS win rate analog (Medium) from the derived addressable_pct chain calculation (Low)
- [ ] Output is labeled as "AI-assisted draft — requires lead consultant review before client delivery" or equivalent

## What failure looks like

A failing output would:
- Use the CMS NHEA $334.4B figure as the direct TAM without flagging that it measures total insurance administrative cost, not PA automation software revenue opportunity
- Compute a top-down SOM of $334.4B × some percentage and present that as the market opportunity without explaining the cost-to-revenue conversion
- Fail to recognize that the large TAM gap (top-down cost base vs. bottoms-up license revenue) is structural and expected — not an error to be smoothed over
- Omit segment-level calculation tables (lumping all 275 health plans together with a single ACV)
- Present the addressable_pct chain calculation (PA share × mid-size share × software fraction) as high-confidence rather than flagging it as three compounded estimates each with error bars
- Write a reconciliation narrative that picks one estimate without explaining the fundamental difference in what each model measures (cost displacement vs. software license revenue)
- Produce a tornado chart that includes the McKinsey TAM base ($20.3B) as a sensitivity variable without explaining that varying the TAM base is a source-selection question, not a model assumption
