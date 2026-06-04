# Industry Benchmark Source Guide

This reference file catalogs reliable industry benchmark sources by sector for use in market sizing models. Each sector entry lists the primary data sources, their typical margin-of-error characteristics, and citation format conventions for consulting deliverables.

**Usage**: Before citing any statistic in a client deliverable, verify the source appears in this guide and note its margin-of-error band when writing the assumptions table. If a source is not listed, flag it for lead consultant review before citing.

---

## When to Prefer Top-Down vs. Bottoms-Up

| Market Condition | Preferred Method | Reason |
|-----------------|-----------------|--------|
| Established, well-defined industry with public data | Top-down primary | IBISWorld/Statista provide accurate TAM; bottoms-up serves as sanity check |
| Emerging or rapidly shifting market (< 5 years old) | Bottoms-up primary | Top-down sources lag reality by 1–3 years; ICP count from current databases is more accurate |
| Niche B2B market with identifiable buyers | Bottoms-up primary | ICP count from Dunn & Bradstreet, Apollo, or Census NAICS counts is more precise than top-down penetration estimates |
| Consumer market with broad addressability | Top-down primary | ICP count cannot be reliably bounded; Census and Nielsen household data is more grounded |
| Market entering from an adjacency (new vertical) | Both equally weighted | Neither method has natural advantage; reconciliation gap is informative about market definition clarity |

---

## Source Citation Format for Consulting Deliverables

Standard citation format: `[Source Name] [Year], [Report/Dataset Title], [NAICS or SIC code if applicable], accessed [Month Year]`

Example: `IBISWorld 2024, Industry Report 7372 — Prepackaged Software, SIC 7372, accessed Jan 2025`

For government statistics: `US Census Bureau 2022, Economic Census: Retail Trade, NAICS 44-45`

Always include the access date because market data ages quickly; a source older than 3 years should be flagged with `[DATA AGE: verify current market conditions have not materially changed]`.

---

## SaaS / Enterprise Software

**Primary sources:**

| Source | Dataset / Code | Typical Margin of Error | Lag | Best Used For |
|--------|---------------|------------------------|-----|---------------|
| IBISWorld | SIC 7372 (Prepackaged Software) | ±15–20% | 6–12 months | Industry-level TAM for established software categories |
| IBISWorld | SIC 7371 (Computer Programming Services) | ±15–20% | 6–12 months | Custom software and IT services TAM |
| Gartner | Magic Quadrant market sizing (varies by category, e.g., ITSM, ERP, CRM) | ±20–25% | 12–18 months | Subcategory TAM where a named Gartner Magic Quadrant exists |
| IDC | Software Tracker by taxonomy category | ±15–20% | 6–9 months | Global and North America subcategory TAM; more granular than IBISWorld |
| G2 | Market category buyer data (public grid + G2 Research) | ±25–35% | 3–6 months | Company counts by software category; useful for ICP count validation |
| Statista | Technology & Telecommunications vertical | ±20–30% | 6–18 months | Quick reference TAM; wide range; always cross-check against IBISWorld or IDC |

**Guidance:**
- For B2B SaaS: IBISWorld SIC 7372 provides the broadest TAM. Narrow to the relevant subcategory using Gartner or IDC category data, then use G2 buyer counts as a floor for ICP count.
- Statista figures for software markets are frequently cited but have the highest margin of error in this sector. Do not cite Statista as the sole source for a TAM figure in a client deliverable; always pair it with IBISWorld or IDC.
- NAICS equivalent for IBISWorld: NAICS 511210 (Software Publishers) and NAICS 541511 (Custom Computer Programming Services).

---

## Healthcare / MedTech

**Primary sources:**

| Source | Dataset / Code | Typical Margin of Error | Lag | Best Used For |
|--------|---------------|------------------------|-----|---------------|
| IBISWorld | NAICS 339112 (Surgical & Medical Instrument Manufacturing) | ±15–20% | 6–12 months | MedTech device manufacturing TAM |
| IBISWorld | NAICS 621 group (Ambulatory Health Care Services) | ±15–20% | 6–12 months | Ambulatory care, clinics, physician practices TAM |
| CMS | National Health Expenditure Accounts (NHEA) | ±5–10% | 18–24 months | Gold standard for US total healthcare spending by category; highly reliable but lags 2 years |
| CMS | Medicare and Medicaid enrollment data (CMS.gov) | ±3–5% | 6–12 months | Payer-specific market counts; high reliability |
| IQVIA | IQVIA Institute Reports (Pharma market data) | ±10–15% | 3–6 months | Pharmaceutical market sizing; recognized standard for pharma segments |
| Definitive Healthcare | Provider intelligence platform | ±10–15% | 3–6 months | Hospital, health system, and physician practice counts by specialty and geography |
| AHRQ | Healthcare Cost and Utilization Project (HCUP) | ±5–10% | 12–18 months | Procedure volume and utilization data; useful for bottoms-up volume assumptions |

**Guidance:**
- **CMS NHEA — MANDATORY REJECTION as product TAM**: CMS NHEA measures total health insurance administrative cost across all payer types and functions (commercial + Medicare + Medicaid, claims processing + network management + plan administration). It is a cost accounting measure with a scope 10–20x broader than any single product-category TAM. **Do NOT use CMS NHEA as a direct TAM for healthcare software products.** Using CMS NHEA directly as a TAM produces figures 10–20x too large and will fail client scrutiny. For healthcare software product TAM, use estimates already scoped to the target function (McKinsey Health Systems Practice, KLAS Research, Advisory Board — all publish PA-specific, utilization management, or claims-specific cost estimates). CMS NHEA may be cited only as overall sector context, labeled "Total US health insurance administrative cost (all payers, all functions) — not product TAM."
- When CMS NHEA is provided alongside a narrowly scoped estimate (e.g., McKinsey PA processing cost), SKILL.md Step 1.2's scope check will MANDATORY REJECT CMS NHEA regardless of gap size. This is not a judgment call — it is an enforcement rule.
- CMS NHEA is appropriate as a reference ceiling for total value-at-stake arguments (e.g., "the total administrative cost pool is $X; our product addresses Y% of that cost"). It must be labeled as a cost-displacement ceiling, not a software TAM or product-category TAM.
- For health IT / digital health markets: There is no single authoritative source. IDC Health Insights and KLAS Research are sector-standard but require subscription access. Rock Health and CB Insights publish annual digital health market reports with reasonable methodology; note ±25–35% margin of error.
- For payer-side markets (health plans, managed care): CMS enrollment data provides reliable counts of covered lives. The National Association of Health Plans (AHIP) publishes plan counts annually.
- IQVIA data is the accepted standard for pharma market sizing in investor and regulatory contexts. Cite the specific IQVIA report name and edition.

---

## Financial Services

**Primary sources:**

| Source | Dataset / Code | Typical Margin of Error | Lag | Best Used For |
|--------|---------------|------------------------|-----|---------------|
| Federal Reserve | Flow of Funds (Z.1 release) | ±5% | 3–6 months | Asset and liability aggregates for banking, insurance, broker-dealer sectors |
| FDIC | Call Report Aggregates (FDIC Statistics on Depository Institutions) | ±3–5% | 3–6 months | Bank count, asset size distribution, deposit data; highly reliable |
| IBISWorld | SIC 6020 group (Commercial Banking) | ±15–20% | 6–12 months | Banking sector TAM |
| IBISWorld | SIC 6311/6321 group (Insurance Carriers) | ±15–20% | 6–12 months | Insurance sector TAM |
| IBISWorld | SIC 6282 (Investment Advice) | ±20–25% | 6–12 months | Wealth management and RIA market TAM |
| Statista | Financial Services vertical | ±20–30% | 6–18 months | Supplemental reference; cross-check against FDIC or Fed data for banking segments |
| S&P Global Market Intelligence | Banking and capital markets data | ±10–15% | 1–3 months | Institution counts, deal volumes, and market share data; requires subscription |

**Guidance:**
- FDIC SDI database is publicly available and highly reliable for US banking market structure data (institution counts, asset size distribution). Use this for ICP count validation in any fintech market targeting depository institutions.
- For payments and fintech markets: The Federal Reserve Payments Study (published every 3 years) is the authoritative source for transaction volume. The Nilson Report is the industry standard for card payments market data (subscription required; ±10% margin of error).
- For insurance: NAIC (National Association of Insurance Commissioners) publishes detailed market share data by line of business annually. More granular than IBISWorld for insurance subcategories.

---

## Manufacturing / Industrial

**Primary sources:**

| Source | Dataset / Code | Typical Margin of Error | Lag | Best Used For |
|--------|---------------|------------------------|-----|---------------|
| US Census Bureau | Economic Census: Manufacturing Sector (every 5 years, latest 2022) | ±5–10% | Up to 5 years | Establishment counts, employment, and shipment values by NAICS code; most comprehensive |
| US Census Bureau | Annual Survey of Manufactures (ASM) | ±10–15% | 12–18 months | Annual update to Economic Census data; more current but smaller sample |
| IBISWorld | NAICS 31-33 manufacturing codes | ±15–20% | 6–12 months | TAM by manufacturing subcategory |
| BLS | Occupational Employment and Wage Statistics (OEWS), by NAICS | ±5–10% | 12 months | Employment counts by occupation and industry — use for ICP count in B2B markets targeting manufacturing plants |
| BLS | Current Employment Statistics (CES) | ±3–5% | 1 month | Monthly employment data; use for demand proxies in manufacturing-dependent markets |
| US Census Bureau | County Business Patterns (CBP) | ±5–10% | 12–18 months | Establishment counts with employee size bands by NAICS — essential for bottoms-up ICP count by geography |

**Guidance:**
- County Business Patterns is the best public source for ICP count in manufacturing markets. It provides establishment counts by NAICS code and employee size band, filterable by state/county. The 2022 Economic Census is the most comprehensive but reflects 2022 conditions.
- BLS OEWS provides employment by occupation code within NAICS industries — use this to size markets targeting specific job functions (e.g., "manufacturing engineers at plants with 500+ employees").
- For industrial equipment markets: IBISWorld manufacturing codes provide revenue-based TAM. Cross-check against Census shipment values from the ASM for validation.

---

## Retail / Consumer

**Primary sources:**

| Source | Dataset / Code | Typical Margin of Error | Lag | Best Used For |
|--------|---------------|------------------------|-----|---------------|
| US Census Bureau | Monthly Retail Trade Survey (MRTS) | ±3–5% | 1–2 months | Total retail sales by category (NAICS 44-45); highly reliable |
| US Census Bureau | Annual Retail Trade Survey (ARTS) | ±5–8% | 12–18 months | Detailed annual retail data with more granular category breakdowns |
| IBISWorld | NAICS 44-45 (Retail Trade sector) | ±15–20% | 6–12 months | Subcategory retail TAM |
| Nielsen / NielsenIQ | Syndicated retail data (subscription required) | ±5–10% | 4–8 weeks | Point-of-sale and market share data for CPG and FMCG categories; industry standard |
| eMarketer (EMARKETER) | US Retail Ecommerce Forecast | ±15–20% | 3–6 months | E-commerce TAM and digital commerce subcategory sizing |
| Kantar Worldpanel | Consumer purchase panel data | ±10–15% | 3–6 months | Household penetration and buying frequency data; use for bottoms-up volume assumptions |

**Guidance:**
- Census MRTS is the authoritative source for retail category sales and is freely available. Use it as the TAM anchor and apply IBISWorld for subcategory segmentation.
- For e-commerce sizing: eMarketer is the most widely cited in investor presentations; its forecasts have ±15–20% accuracy and are forward-looking. Pair with actual Census e-commerce data (E-Stats) for the historical base.
- Nielsen data is subscription-gated. If available, it is the most reliable source for unit volume, market share, and household penetration in CPG markets.

---

## Professional Services

**Primary sources:**

| Source | Dataset / Code | Typical Margin of Error | Lag | Best Used For |
|--------|---------------|------------------------|-----|---------------|
| IBISWorld | SIC 7389 / NAICS 541610 (Management Consulting) | ±15–20% | 6–12 months | Management consulting sector TAM |
| IBISWorld | NAICS 5411 (Legal Services) | ±15–20% | 6–12 months | Legal services sector TAM |
| IBISWorld | NAICS 5412 (Accounting, Tax Preparation) | ±15–20% | 6–12 months | Accounting and tax services sector TAM |
| BLS | Occupational Outlook Handbook (OOH) | ±5–10% | 12–24 months | Employment projections by occupation; use for market sizing tied to headcount in professional roles |
| BLS | OEWS (Occupational Employment by NAICS) | ±5–10% | 12 months | Current employment counts by occupation within professional services industries |
| IBIS / Statista | Firm count data (advisory, accounting, legal) | ±20–30% | 6–18 months | Number of firms by size band; use for ICP count in markets targeting professional services firms |
| Kennedy Research Reports | Management consulting market data | ±15–20% | 12–18 months | Consulting-specific market data; recognized in industry but requires subscription |

**Guidance:**
- For markets targeting professional services firms as buyers: IBISWorld firm count data and BLS OEWS provide the most accessible ICP count sources. Filter by employee size band to match ICP definition.
- BLS Occupational Outlook Handbook is useful for 10-year employment projections — use for market growth rate assumptions, not current TAM.
- Kennedy Research (Consultancy.org) is the recognized specialist in management consulting market data; more granular than IBISWorld for consulting subcategories but requires subscription.

---

## Handling Conflicting Source Estimates

When two sources provide materially different TAM figures for the same market, apply this protocol:

1. **Document both figures** with source, publication date, and NAICS/SIC code.
2. **Check for scope mismatch first (when gap > 50%).** Compute `gap_pct = abs(source_a - source_b) / max(source_a, source_b)`. If gap > 50%, determine whether one source covers a broader universe (all functions, all payers, all industries) while the other is narrowly scoped to the specific product category. If a scope mismatch is found, SELECT the narrow-scope source and reject the broad-scope source with documentation. See SKILL.md Step 1.2 for the full scope-check rule and the Healthcare mandatory enforcement rule (CMS NHEA). Do not proceed to step 3 until the scope check passes.
3. **Check for business unit mismatch.** Determine whether the remaining sources are measuring the same type of quantity:
   - A source is measuring a **cost base** if its figure is denominated as "total costs," "total spending," "administrative costs," "total expenditure," or similar.
   - A source is measuring a **software/product revenue market** if its figure is denominated as "software market revenue," "product market size," "license fees," or "SaaS market."
   - If the two sources measure **different business units** (one cost base, one software revenue), check the gap: if gap < 20%, present both as convergence validation and use the midpoint; if gap ≥ 20%, select the source matching the client's revenue model. See SKILL.md Step 1.2 for the full decision tree. Do not proceed to step 4 unless both sources are same-type.
4. **Apply the midpoint rule** (only if both sources measure the same business unit type and no scope mismatch was found): use the arithmetic mean of the two figures as the base TAM. Display the full range in the exhibit (e.g., "$42B–$58B, base case $50B").
4. **Flag the range in the assumptions table** as the source-driven uncertainty band. This range feeds directly into the sensitivity analysis in `SENSITIVITY-ANALYSIS.md`.
5. **Do not average without explanation.** If the discrepancy exceeds 40%, the two sources are likely using different market definitions. Reconcile definitions before averaging.

**Example conflict documentation:**
> IBISWorld SIC 7372 reports the US prepackaged software market at $48.2B (2024). IDC Software Tracker reports the US packaged software market at $62.1B (2024). The discrepancy likely reflects IBISWorld's exclusion of cloud-delivered SaaS revenue, which IDC includes. For this analysis, we use IDC's figure of $62.1B as the TAM base because it captures the addressable market for a SaaS entrant. IBISWorld's figure is noted as the lower bound for the reported range.

---

## General Guidance

**Source age**: Data more than 3 years old should be flagged `[DATA AGE]`. Market conditions, company counts, and spending patterns can shift materially in 3 years, especially in technology-adjacent markets.

**Government vs. commercial sources**: Government sources (Census, BLS, FDIC, CMS) have lower margin of error (typically ±3–10%) but higher data lag (12–24 months). Commercial databases (IBISWorld, Gartner, IDC) are more current but have higher margin of error (±15–25%). Use government sources to anchor the ICP count; use commercial sources for TAM and growth rate estimates.

**Citing Statista**: Statista aggregates data from many primary sources with varying quality. Always trace Statista figures back to the underlying primary source it cites and cite that primary source directly. A Statista citation alone is not acceptable in a consulting deliverable that will face client or investor scrutiny.

**Subscription-gated data**: Gartner, IDC, Nielsen, IQVIA, and similar subscription sources are widely used in consulting. If the practitioner has access, these are preferred over free alternatives for their lower margin of error. If not available, note the gap: `[PREMIUM SOURCE NOT ACCESSED: [source name] — verify with client if they have access]`.
