# Pitchbook Comparable Companies Commentary Writer

**Industry**: Finance
**Role**: Investment Banking Analyst
**Time saved**: 2–4 hours per pitchbook comps section

## What it does

Takes a completed comparable companies table (peer names, financial metrics, and valuation multiples) plus a target company description, and drafts the full interpretive narrative for the pitchbook comps page: peer set rationale, outlier analysis table, target positioning argument, and slide-ready callout bullets.

## When to use it

After your comps table is finalized and populated with multiples — at the moment you would normally open a blank text box in PowerPoint and stare at 7 rows of numbers trying to figure out what to say about them.

## Prompt template

```
You are helping draft the narrative sections of a comparable companies (trading comps) page for an investment banking pitchbook. The data table is complete. Your job is to produce the interpretive commentary that accompanies it.

## Comparable Companies Table

{PASTE_COMPS_TABLE_HERE}

Example format:
Company | EV ($M) | EV/LTM Revenue | EV/LTM EBITDA | EV/NTM Revenue | EV/NTM EBITDA | LTM Revenue Growth | LTM EBITDA Margin
Peer A  | 2,400   | 6.2x           | 28.1x         | 5.4x           | 23.7x         | 34%                | 22%
[...]

## Target Company Description

{TARGET_DESCRIPTION}

Include: company name, business description, key financial characteristics relevant to valuation (revenue growth rate, EBITDA margin, gross margin, customer mix, retention/NRR, geographic concentration, or any other characteristics that differentiate the target from peers).

## Additional Context (optional)

{OPTIONAL_PEER_NOTES}

Include any known information about specific peers that explains anomalous multiples: pending acquisitions, recent earnings beats or misses, restructuring, sector-specific news.

---

Using only the data and descriptions above, produce four sections:

### A. Peer Set Rationale
One paragraph (4–7 sentences) explaining why these peers were selected. For each peer, one clause or sentence on the specific business characteristic justifying inclusion.

### B. Outlier Analysis
A table with columns: Peer | Multiple | vs. Median | Proposed Rationale | Confidence (High/Low)
Flag any outlier where no rationale is apparent as "Rationale Unclear — verify with recent news."

### C. Target Positioning
3–5 sentences grounding the target's implied valuation range in its stated characteristics. Each sentence names a specific characteristic and links it to a specific multiple. End with a stated implied valuation range.

### D. Slide Callouts
3–5 numbered one-sentence callouts formatted for direct copy-paste into a PowerPoint text box. Present tense, active voice. Each must include at least one specific number from the table.

Rules:
- Do not invent peer companies, multiples, or metrics not in the input
- Do not make positioning arguments about characteristics not stated in the target description
- Flag data gaps inline rather than omitting them
- Do not add disclaimers or hedging language
```

## Example output

**Input**: 6-peer SaaS comps set, EV/NTM Revenue range 4.2x–14.8x, median 7.1x. Target described as vertical SaaS, 18% revenue growth, 92% NRR, but below-peer-median growth.

**Section D — Slide Callouts (excerpt)**:
1. The peer set trades at a median 7.1x NTM Revenue, with a wide 10.6-turn spread reflecting significant growth dispersion across the group.
2. Veeva Systems trades at 14.8x NTM Revenue — a 108% premium to the peer median — reflecting its dominant vertical-SaaS market position and 30%+ operating margins.
3. The target's 92% NRR supports a premium to low-retention peers but its 18% growth rate, below the peer median of 26%, argues for a discount to high-growth names — implying a 5.5x–7.0x NTM Revenue range.
4. Applying the implied 5.5x–7.0x NTM Revenue range to the target's $185M NTM Revenue estimate implies an enterprise value of $1,018M–$1,295M.

## Tips

1. **Provide the full table, not a summary.** The skill needs raw multiples per peer to calculate medians and identify outliers. Do not pre-summarize.

2. **Be specific in the target description.** The quality of Section C depends entirely on the characteristics you provide. "High-growth SaaS" produces generic output. "22% NTM revenue growth, 91% gross margins, 88% net revenue retention, 60% mid-market / 40% enterprise revenue split" produces a precise positioning argument.

3. **Use the optional context field for known peer stories.** If you know why a peer is trading at a premium or discount (pending acquisition, recent guidance cut), put it in the context field. The skill will incorporate it as the rationale rather than guessing.
