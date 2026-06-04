# Scenario 1: SMB Accounts Payable Automation — Fintech Market Entry

## Context

A B2B fintech startup is evaluating entry into the US SMB accounts payable (AP) automation market. The client has developed a cloud-native AP automation platform targeting US-based companies with $5M–$50M in annual revenue that currently process invoices manually (paper-based or email-based workflows with no dedicated AP automation software). The consulting engagement is a 4-week market entry feasibility study. The lead consultant needs a market sizing section for the final client presentation.

The consultant has pulled benchmark data from two sources: BLS QCEW for establishment counts and Statista for AP automation market size. They also have a preliminary deal size from the client's pilot pricing conversations and a win rate analog from a comparable fintech entrant (expense management SaaS).

## Input

**Target market description**: Cloud-based accounts payable automation SaaS for US companies with $5M–$50M annual revenue (approximately 50–499 employees) that currently manage AP without dedicated automation software. Target geography: United States only.

**Industry sector**: SaaS / Enterprise Software

---

**ICP definition**: US-based for-profit companies with $5M–$50M annual revenue (roughly 50–499 employees per BLS size-band mapping), across all industries except government and non-profit, that have no existing AP automation software (manual or semi-manual AP workflows).

**Segments**:

| Segment | ICP Count | ICP Count Source | Avg Deal Size (ACV) | Win Rate |
|---------|-----------|-----------------|---------------------|---------|
| SMB Lower ($5M–$20M revenue) | 185,000 | US Census County Business Patterns 2022, all NAICS, 50–99 employees, filtered to for-profit only; multiplied by 0.62 to exclude those with existing AP software per Ardent Partners 2023 AP Automation Adoption Survey (38% adoption rate in this size band) | $12,000 | 12% |
| SMB Upper ($20M–$50M revenue) | 68,000 | US Census County Business Patterns 2022, all NAICS, 100–249 employees, filtered to for-profit only; multiplied by 0.51 to exclude those with existing AP software (49% adoption rate per Ardent Partners 2023 for this band) | $28,000 | 10% |

**Win rate basis**: Comparable fintech SaaS entrant in SMB expense management (Ramp/Brex early cohort data, referenced in CBInsights fintech report 2023): 10–13% win rate on outbound-qualified accounts in years 1–3 of market entry.

---

**Industry TAM source**:
- Source 1: Statista 2024, "Accounts Payable Automation Market — United States," market size $4.1 billion (2024 estimate, NAICS 511210 adjacent, enterprise + SMB combined)
- Source 2: Ardent Partners 2024 State of ePayables Report, US AP automation total addressable market estimated at $3.6 billion (2024, methodology: total AP processing costs × automation-accessible fraction)

**Addressable percentage (SAM/TAM)**: 22% — Ardent Partners 2024 segments the US AP automation market: enterprise (>$500M revenue) represents ~51% of spend, mid-market ($50M–$500M) represents ~27%, and SMB (<$50M) represents ~22%. Client's ICP falls entirely within the SMB segment.

**Capturable percentage (SOM/SAM)**: 1.8% — Based on comparable SMB fintech SaaS entrants (expense management, spend management category). Year 3 realistic market share for a well-funded new entrant with strong product-market fit, per CBInsights SMB fintech benchmark 2023.

---

**Conflicting sources**:
- Statista: $4.1B US AP automation market
- Ardent Partners: $3.6B US AP automation market
- Likely reason: Statista uses a revenue-based market definition (software license + implementation + services fees); Ardent Partners uses a cost-displacement methodology (total AP processing costs that automation can address). The Ardent Partners figure is narrower.

## Expected Output Criteria

- [ ] Bottoms-up TAM computed correctly: SMB Lower TAM = 185,000 × $12,000 = $2,220,000,000; SMB Upper TAM = 68,000 × $28,000 = $1,904,000,000; Total bottoms-up TAM = $4,124,000,000 (within ±$1M rounding tolerance)
- [ ] Bottoms-up SOM computed correctly: SMB Lower SOM = $2,220M × 12% = $266.4M; SMB Upper SOM = $1,904M × 10% = $190.4M; Total SOM = $456.8M (within ±$1M tolerance)
- [ ] Top-down model applies the two-step penetration cascade: TAM uses the midpoint of the two conflicting sources ($3.85B), SAM = $3.85B × 22% = $847M, SOM = $847M × 1.8% = $15.25M
- [ ] Conflicting source reconciliation: The output either (a) uses the midpoint ($3.85B) with the range documented, or (b) explicitly selects one source and explains why; a blended average without explanation is a fail
- [ ] Reconciliation gap identified: Bottoms-up TAM ($4.12B) is higher than top-down TAM ($3.85B range or midpoint); gap direction correctly identified as BOTTOMS_UP_HIGHER or ALIGNED (gap < 10% relative to midpoint)
- [ ] Reconciliation narrative addresses: why the bottoms-up TAM and top-down TAM are close in this case (the Ardent Partners cost-displacement methodology closely mirrors a bottoms-up construction), and notes that this alignment increases model confidence
- [ ] At minimum 3 sensitivity flags identified and ranked: ICP count, win rate, and addressable percentage (and/or avg deal size) must all appear; the output must identify which has the largest TAM/SOM swing
- [ ] Tornado chart data table present with at least 3 inputs, sorted by full swing descending
- [ ] Slide-ready exhibit format: TAM/SAM/SOM table present with both methods side-by-side; must include $ figures with appropriate M/B scale
- [ ] Source-cited assumptions table present: every numerical assumption has a source citation; any estimate-based assumption is flagged as Low confidence
- [ ] Output is labeled as "AI-assisted draft — requires lead consultant review before client delivery" or equivalent

## What failure looks like

A failing output would:
- Compute only one of the two models (bottoms-up only, or top-down only) without the parallel second model
- Present a single blended TAM figure without showing both estimates separately
- Miss or miscalculate the segment-level TAM/SOM arithmetic (e.g., applying the aggregate win rate to the TAM instead of segment-level win rates)
- Handle the conflicting Statista/Ardent Partners TAM figures by silently choosing one without documentation
- Omit the reconciliation narrative entirely or write only "the methods are aligned" without diagnosing why
- Produce a sensitivity section that lists assumptions but does not quantify the impact (e.g., "win rate is sensitive" without showing the TAM/SOM range under ±40%)
- Present SOM figures without showing the calculation chain from TAM → SAM → SOM
- Omit source citations from the assumptions table or present a generic list of sources not tied to specific assumptions
