# Competitive Benchmarking Slide Synthesizer

**Industry**: Consulting
**Role**: Strategy Consultant / Business Analyst
**Time saved**: 6–10 hours per benchmarking cycle (vs. manual normalization, variance flagging, and narrative drafting from raw data extracts)

## What it does

Takes raw competitor data extracts from multiple sources — annual reports, press releases, analyst estimates, industry databases — normalizes metric definitions across companies, builds a sourced comparison table, identifies the 2–3 gaps most relevant to the client's stated strategic question, and outputs a slide-ready brief with a narrative headline, callout boxes, and a recommended presentation arc.

Unlike generic data aggregation, this skill explicitly documents definition mismatches (e.g., one company's gross margin includes D&A while another's does not), flags stale and estimated data points in every table cell, and ties each selected gap back to the client question — not just the largest numerical variance.

## When to use it

Invoke after you have gathered raw competitor metrics from your sources and before you begin building the actual slide. You need the data normalized and the strategic point identified before you can write the headline or structure the visual.

Typical trigger: you have a folder of downloaded competitor filings and analyst notes, a list of metrics the client cares about, and a client question like "where are we losing?" or "are we priced to win?" You need to go from raw extracts to slide-ready brief without spending a day reformatting tables.

## Prompt template

Copy and paste the full block below. Replace everything in `{CURLY BRACES}` with your actual inputs.

---

You are a strategy consultant assistant helping synthesize a competitive benchmarking brief for a client deck. Work through the following steps in order. Do not skip definition normalization or source citation.

**CLIENT CONTEXT**
- Client company: {CLIENT_COMPANY_NAME}
- Strategic question: {THE_SPECIFIC_QUESTION_THE_CLIENT_IS_TRYING_TO_ANSWER — e.g., "Where are we losing profitable customers to digital-first competitors?"}
- Memo date: {TODAY_DATE — used to determine staleness of data points older than 18 months}
- Benchmarking dimensions (metrics that matter): {LIST_OF_METRICS — e.g., NPS, digital adoption rate, customer acquisition cost, net interest margin}

**COMPETITOR DATA EXTRACTS**
{PASTE YOUR RAW COMPETITOR DATA BELOW — for each data point include: company name, metric name, value, source document name, source type (annual report / press release / analyst estimate / industry database), and data date}

Example format:
- Company: Acme Bank | Metric: NPS | Value: 42 | Source: J.D. Power 2024 Banking Study | Source type: Industry database | Date: March 2024
- Company: Acme Bank | Metric: Digital adoption rate | Value: 67% | Source: 2023 Annual Report | Source type: Annual report | Date: Feb 2024
- Company: RiverFirst Digital | Metric: Active users (monthly) | Value: 2.1M | Source: Q3 2024 earnings release | Source type: Press release | Date: Oct 2024
[continue for all data points]

**CLIENT COMPANY DATA**
{SAME FORMAT AS ABOVE FOR THE CLIENT'S OWN METRICS — include source and date for each}

---

Now produce a full competitive benchmarking brief with the following sections:

**Section 1: Normalized Comparison Table**
Rows = metrics, Columns = Client + each competitor + Peer Median. For each cell, include: normalized value, source tag (abbreviated source + year), and markers: [R] = Reported in filing/press release, [E] = Estimated from analyst/database, [STALE] = data older than 18 months from memo date, [NC] = not comparable due to definition mismatch. Peer Median uses reported values only; mark [Insufficient data] if fewer than two reported values exist.

**Section 2: Definition Notes**
For each metric: document the definition used by each company, identify any mismatches, state whether reconciliation was applied or whether figures are not directly comparable. If all definitions are consistent, confirm this explicitly.

**Section 3: Strategic Gap Analysis**
Select the 2–3 variances most material to the stated strategic question. For each gap: name the metric, state the magnitude (client vs. peer median or vs. the most relevant competitor), explain in one sentence why it matters for the client's specific decision. List any excluded large variances and explain why they are not strategically relevant to this question.

**Section 4: Narrative Outputs**
- Headline: one sentence stating the most important strategic implication. Must be falsifiable — a specific claim, not a generic observation.
- Callout boxes (one per gap): gap title, magnitude, strategic implication (1–2 sentences), any data quality notes.
- Narrative arc: 3–5 bullet points recommending how to sequence these findings in a client meeting, including what pushback to pre-empt.

---

## Example output

Below is a partial example to show the expected format and specificity.

---

**Client**: MidWest Regional Bank
**Strategic question**: Where are we losing profitable customers to digital-first competitors?
**Memo date**: 2024-11-15
**Competitors covered**: NationalFirst Bank, Consolidated US Bank, Apex Digital, NeoBank One

#### Section 1: Normalized Comparison Table (excerpt)

| Metric | MidWest Regional [R] | NationalFirst [R] | Consolidated US [R] | Apex Digital [R] | NeoBank One [E] | Peer Median |
|---|---|---|---|---|---|---|
| NPS | 31 (J.D. Power '24) | 38 (J.D. Power '24) | 29 (J.D. Power '24) | 54 (J.D. Power '24) | 61 [STALE] (NeoBank PR '22) | 38 |
| Digital Adoption Rate | 58% (AR '24) | 71% (AR '24) | 66% (AR '23) | 89% (AR '24) | [NC] See Def. Notes | [Insufficient data — only 3 reported values, NeoBank NC] |
| Customer Acquisition Cost | $312 (AR '24) | $287 (AR '24) | $301 [E] (IBD Est. '24) | $94 [E] (IBD Est. '24) | $71 [E] (IBD Est. '24) | $294 [reported only] |

**Table notes:**
[R] = Reported | [E] = Estimated | [STALE] = >18 months old | [NC] = Not comparable

#### Section 2: Definition Notes (excerpt)

**Digital Adoption Rate**
- MidWest Regional, NationalFirst, Consolidated US: % of retail customers who logged into online or mobile banking at least once in the prior 90 days (per annual report disclosures)
- NeoBank One: Reports "monthly active users" (MAU) as a total user count, not as a % of customer base. No denominator disclosed.
- Normalization applied: None — NeoBank One's figure is not comparable to a penetration rate. Marked [NC].
- Impact on variance: NeoBank One cannot be included in peer median for this metric.

#### Section 3: Strategic Gap Analysis

*Selected gaps most relevant to: "Where are we losing profitable customers to digital-first competitors?"*

**Gap 1: Digital Adoption Rate — MidWest trails digital-first peers by 31 percentage points**
Why it matters: The client's question centers on customer loss to digital-first players. A 31pp gap in digital adoption is a direct measure of engagement channel mismatch — customers who do not use digital channels are at higher churn risk when a digital-first competitor makes an acquisition offer.
Data quality: NeoBank One excluded (NC). Apex Digital reported figure.

**Gap 2: Customer Acquisition Cost — MidWest's CAC is 3.3x Apex Digital's ($312 vs. $94)**
Why it matters: At current CAC, MidWest cannot profitably match fintech acquisition economics in overlapping segments. This gap constrains the client's ability to run a counter-offensive acquisition strategy.
Data quality: Apex Digital CAC is estimated [E] from an industry database, not a reported figure — actual gap may differ.

**Gaps excluded from strategic analysis:**
NIM gap of 80bps vs. NationalFirst excluded: NIM reflects funding mix and rate positioning, not digital customer acquisition dynamics directly relevant to this strategic question.

#### Section 4: Narrative Outputs

**Headline:**
MidWest's digital engagement deficit — not product quality — is the primary structural advantage ceding customers to Apex and NeoBank, and closing it at current CAC economics is not viable without a channel strategy reset.

**Callout Boxes:**

> **Digital Adoption: 31pp behind digital-first peers**
> MidWest 58% vs. Apex Digital 89%
> Customers not engaged digitally are the most vulnerable to fintech acquisition. The gap is not narrowing — Apex grew digital adoption 7pp YoY while MidWest grew 2pp.
> *Data note: NeoBank One excluded from comparison (definition mismatch — active users vs. penetration rate)*

> **CAC Asymmetry: 3.3x cost disadvantage vs. leading fintech**
> MidWest $312 vs. Apex $94 (estimated)
> Even if MidWest matches fintech product features, it cannot win a customer acquisition price war at current cost structure. The implication is that retention, not acquisition, is the defensible near-term strategy.
> *Data note: Apex CAC is an industry database estimate, not a reported figure*

**Narrative Arc:**
1. Open with the client question restated as a hypothesis: "We believe we are losing profitable customers primarily to digital-first competitors — let's test whether that's a product problem, a channel problem, or an economics problem."
2. Show the comparison table: walk the audience through digital adoption and CAC gaps first — these are the tier-1 metrics for this question. Confirm that NIM and NPS gaps exist but are secondary.
3. Name the implication: this is a channel engagement problem, not a product problem. The NPS gap is smaller than the digital adoption gap, which means customers who engage digitally are relatively satisfied.
4. Pre-empt the pushback: "Are we sure the CAC figures are right?" — acknowledge the estimation caveat, but note the order-of-magnitude difference makes the strategic read robust to a 20–30% data error.
5. Close with the decision framing: the strategic question is not "how do we match fintech acquisition economics" but "which customer segments are worth defending and through which channel."

---

## Tips

1. **Front-load the strategic question.** The skill produces better gap selection when the strategic question is specific and decision-oriented. "Where are we losing profitable customers to digital-first competitors?" works. "How do we compare to competitors?" does not — it gives the skill no basis for prioritizing gaps over each other.

2. **Always provide source type and date for every data point.** The staleness flag and the reported/estimated distinction depend entirely on the metadata you provide. If you omit the date, the skill cannot flag stale data and you lose one of the core quality checks.

3. **Provide your client's own metrics in the same format as competitors.** The comparison table is only as useful as the client's own position is clearly defined. If you paste competitor data but describe the client's metrics loosely ("roughly 65%"), the variance computation will be imprecise and the strategic gap selection less reliable.
