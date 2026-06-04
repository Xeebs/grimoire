# Test Results: competitive-benchmarking-slide-synthesizer

**Tested**: 2026-06-03
**Overall verdict**: PASS

---

## Scenario 1: Regional Bank Losing Customers to Digital-First Competitors
**Verdict**: PASS

### Criteria evaluation
- ✓ Comparison table includes all six metrics as rows, four competitors plus Heartland as columns, Peer Median column with source tags and [R]/[E] markers in each cell
- ✓ Meridian's NPS cell marked [STALE] because January 2023 data is 22 months old relative to November 2024 memo date
- ✓ Continental's CAC cell marked [E] because value comes from Bankwell Analytics estimate, not company filing
- ✓ Both fintech digital adoption cells marked [NC] with direction to Definition Notes, because they report MAU counts rather than penetration rate
- ✓ Peer Median for Digital Adoption Rate calculated from Meridian 74% and Continental 69% = 71.5%, excluding non-comparable fintech figures
- ✓ Definition Notes include comprehensive entry for Digital Adoption Rate documenting MAU vs. penetration-rate mismatch and stating figures are not comparable
- ✓ Definition Notes include entry for Net Interest Margin noting Crest Digital's non-GAAP definition (includes interchange-equivalent revenue) vs. Heartland's GAAP NIM, flagging incomparability
- ✓ Strategic Gap Analysis selects CAC and Digital Adoption Rate as primary gaps (tier-1 metrics for customer-loss question), rather than defaulting to largest raw numerical variance
- ✓ NIM gap excluded from Strategic Gap Analysis with explicit reasoning: "not strategically relevant to the customer-loss question" as NIM is profitability metric, not customer acquisition or satisfaction metric
- ✓ Narrative headline is specific and falsifiable: "Heartland cannot compete on customer acquisition economics with digital-first players: at 3.8x the CAC of neobanks, Heartland is mathematically losing profitable customers faster than it can afford to replace them" — tied directly to digital-first customer loss question
- ✓ Each callout box includes data quality note (e.g., "Apex and Crest CAC figures are from Bankwell Analytics estimates (Q3 2024)")
- ✓ Narrative Arc explicitly addresses CAC data quality pushback in beat 2: anticipates objection "But our customers are older / less digital / higher churn" and provides anchoring alternative (Meridian comparison)

### Notes
The skill correctly prevents silent treatment of non-comparable digital adoption figures (MAU vs. percentage). It forces explicit documentation of stale data (Meridian NPS) and estimated figures (Continental CAC, fintech CAC). The strategic gap selection demonstrates tier-1 vs. tier-2 metric distinction — the analyst must link each gap to the stated question, not select by magnitude alone. The narrative arc is presentation-ready: it acknowledges data limitations while maintaining strategic clarity.

---

## Scenario 2: B2B SaaS Client Evaluating Pricing and Positioning Against Enterprise Competitors
**Verdict**: PASS

### Criteria evaluation
- ✓ Comparison table includes all seven metrics as rows, three competitors plus Vaultify as columns, Peer Median column, source tags, and [R]/[E] markers in each cell
- ✓ Arcana's ARR and ACV cells include currency conversion note documenting EUR/USD rate at time of report (August 2024: 1.09) and current spot rate (November 2024: 1.06), with 2.8% variance impact noted in Definition Notes
- ✓ All Nexus Workflow cells marked [STALE] because S-1 data is 26 months old relative to November 2024 memo date (exceeds 18-month threshold)
- ✓ Win rate cells marked [E] for Formidable, Arcana, and Nexus (Gartner estimate source), and [R] for Vaultify (internal CRM data)
- ✓ Definition Notes include entry for Gross Margin documenting Arcana's total revenue basis (including professional services) vs. Formidable's and Vaultify's subscription-only basis, with note on comparability impact
- ✓ Definition Notes include entry for R&D Spend noting Arcana's inclusion of product localization costs (typically COGS/S&M in US SaaS) and flagging directional impact (Arcana's R&D % likely overstated relative to US peers)
- ✓ Strategic Gap Analysis selects ACV (Gap 1), Win Rate (Gap 2), and NRR (Gap 3) as primary strategic gaps — directly addressing pricing (ACV) and positioning to win enterprise deals (win rate, NRR as customer stickiness/expansion proxy)
- ✓ NRR gap analysis acknowledges Nexus staleness and focuses comparison on current figures: Vaultify (104%) vs. Formidable (118%), explicitly excluding 26-month-old Nexus from primary analysis
- ✓ Narrative headline specifically addresses pricing and positioning: "Vaultify is winning enterprise deals at Formidable's rate but pricing 20% below market, leaving deal profitability and customer expansion potential on the table" — falsifiable claim tied to enterprise deal outcomes
- ✓ Narrative arc anticipates Nexus data staleness objection in beat 4 ("The win rate data is from Gartner, so treat it as directional") and in NRR callout note ("Nexus's 109% NRR is from September 2022 S-1 and is not included in this analysis")

### Notes
The skill correctly enforces currency normalization with explicit rate documentation and impact transparency. It identifies and flags definition mismatches (Arcana gross margin and R&D) that could silently distort comparisons. The strategic gap selection filters out metrics that are not relevant to "pricing and positioning for enterprise deals" (e.g., ARR scale, sales cycle length, gross margin) — this demonstrates the skill's effectiveness at enforcing the constraint that "Do not include a gap in the strategic gap analysis solely because it is the largest variance." The narrative arc is sophisticated: it separates data quality caveats (beat 4) from strategic implication (beat 3), and provides a two-pronged recommendation that addresses both capability gaps and pricing segmentation.

---

## Summary
- Scenario 1: PASS
- Scenario 2: PASS
- Overall: PASS

### Failure modes (if any)
None identified. The skill's instructions and enforcement mechanisms prevent the most common benchmarking analysis failures:
1. Silently treating incomparable definitions as comparable (prevented by Definition Notes requirement and [NC] markers)
2. Selecting gaps based on numerical magnitude rather than strategic relevance (prevented by explicit tier-1/tier-2 framework and strategic question linking)
3. Omitting or minimizing data quality documentation (prevented by mandatory [R]/[E]/[STALE]/[NC] markers and Definition Notes section)
4. Writing non-falsifiable or generic headlines (prevented by explicit instruction: "state the single most important strategic implication" and "the headline must be falsifiable")
5. Treating stale data as current (prevented by 18-month threshold and mandatory [STALE] marking)
6. Failing to address data quality pushback in client presentation (prevented by Narrative Arc requirement and explicit instruction to "address the likely client pushback")

### Recommended fixes (if any)
None. The skill is ready for publication. It ships with comprehensive, rigorous instructions that enforce professional-grade competitive benchmarking discipline. The dual-format (SKILL.md + README.md) architecture allows use in Claude Code environments and as a portable prompt template. Both test scenarios demonstrate that the skill's step-by-step framework and output structure prevent silent data quality failures and force strategic rigor in gap selection.
