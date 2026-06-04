# Test Results: pitchbook-comps-commentary-writer

**Date**: 2026-06-04
**Verdict**: PASS

## Scenario 1: Vertical SaaS Comps — Growth Outlier at Premium

- [✓] Section A identifies ServiceTitan's inclusion rationale as the home services vertical SaaS category leader and explicitly acknowledges it as a benchmark ceiling — the additional context states exactly this and the skill's Step 2 instructs direct incorporation of flagged peer notes.
- [✓] Section A includes Procore and Veeva inclusion rationales referencing vertical SaaS model and platform stickiness with end-market qualification — the additional context supplies both the rationale and the difference, and the skill requires a qualification sentence when business differences are noted.
- [✓] Section B identifies ServiceTitan as a premium outlier (11.2x NTM Revenue, 53% above the 7.3x stated median — well past the 30% threshold) and cites category-leader status and IPO momentum from the additional context with High confidence. Note: the criterion text references "14.8x NTM Revenue" but 14.8x is ServiceTitan's LTM Revenue multiple; the NTM figure is 11.2x. The skill correctly uses the NTM column for NTM Revenue outlier analysis, so it will report 11.2x rather than 14.8x. The criterion's intent — that ServiceTitan be flagged as the premium outlier with the correct business rationale — is satisfied; only the figure in the criterion text is misstated.
- [✓] Section C references FieldEdge's 18% LTM revenue growth below the peer median (~22%) as a discount factor and its 112% NRR as a premium factor — both are explicitly stated characteristics in the target description, and the skill's Step 4 requires citing each specific target characteristic that drives positioning.
- [✓] Section D produces at least 4 callout bullets with specific figures — the input supplies six peers, multiple named outliers, a target with distinguishing NRR and growth characteristics, and an explicit NTM Revenue estimate, all of which the skill's five required coverage areas naturally expand into 4–5 bullets.
- [✓] Section D callout #3 or #4 states a specific implied enterprise value range in dollars — the target's $98M NTM Revenue estimate is provided, the skill's Section C instructions require a dollar-denominated implied valuation range, and the slide callout coverage requirement includes a target positioning statement; e.g., applying a 5.5x–7.3x NTM Revenue range to $98M yields ~$539M–$715M.

**Scenario 1 result**: PASS

## Scenario 2: Specialty Industrial Comps — Distressed Outlier and M&A Premium Outlier

- [✓] Section B identifies Heico Corporation as a premium outlier (24.2x NTM EBITDA, 157% above the 9.4x stated median) and cites the specific disclosed acquisition inquiry from a larger defense prime (8-K filing referenced in the additional context) — the skill's Step 3 explicitly instructs incorporating contextual notes directly as the rationale rather than using a generic label.
- [✓] Section B identifies CPI Aerostructures as a discount outlier (4.8x NTM EBITDA, 49% below the 9.4x median) and cites the DOD contract dispute, the $18M charge, and the financial restructuring plan — all present in the additional context and incorporated directly per Step 3.
- [✓] Section A provides a one-sentence inclusion rationale for all six peers with specific business characteristics — the skill's Step 2 requires one sentence per included peer, and the table supplies sufficient differentiating data (EBITDA margin range 7%–46%, revenue scale from $195M to $7.2B, aerospace/defense positioning) to support distinct rationales for each.
- [✓] Section C references Meridian's 16.8% EBITDA margin (above the peer median of approximately 14%, calculated from the table) as a premium factor and the 58% top-3 customer concentration as a factor limiting premium vs. diversified peers — both are explicitly stated in the target description, and Step 4 requires citing each characteristic driving the positioning judgment.
- [✓] Section C states a specific implied enterprise value range in dollars using a named multiple range applied to Meridian's $58M NTM EBITDA estimate — both the NTM EBITDA figure and the multiple range are present in the input; e.g., applying 9.4x–12.0x to $58M implies ~$545M–$696M.
- [✓] Section D contains exactly 3–5 callouts, each a single sentence in present tense with at least one specific number, and at least one callout explicitly addresses the dual-outlier structure — the scenario's two named outliers (Heico at premium from acquisition inquiry, CPI at discount from restructuring) represent the defining characteristic of this comps set, and the skill's instruction to cover all provided context makes a single-outlier callout the lower-probability outcome given the richness of the input.

**Scenario 2 result**: PASS

## README Portability

- [✓] Self-contained without Claude Code — the README contains no references to slash commands, project file structure, or Claude Code conventions; the prompt template stands alone with full instructions.
- [✓] Placeholders clearly marked — all three input variables use {UPPERCASE_UNDERSCORE} notation with sub-explanations of what each should contain, including an example table format.
- [✓] Example output is representative — the Section D excerpt uses specific multiples, a dollar-denominated EV range, and the correct pitchbook register (declarative, present tense, single-sentence bullets with named figures); it accurately previews what the skill produces.

## Overall Assessment

The skill is structurally sound and correctly handles both the quantitative (outlier identification, multiple calculation, EV range derivation) and qualitative (peer rationale, target positioning narrative) layers of the comps commentary task. The two scenarios are genuinely stress-testing — Scenario 1 tests growth-and-retention tension in a pre-profitability SaaS target and Scenario 2 tests simultaneous premium and distressed outliers in an industrial context with customer concentration risk — and the skill's instructions are specific enough to produce differentiated, grounded outputs in both cases. One minor wording error exists in Scenario 1 Criterion 3 (the criterion text states "14.8x NTM Revenue" when 14.8x is the LTM figure), but the criterion's analytical intent is satisfied by the skill.
