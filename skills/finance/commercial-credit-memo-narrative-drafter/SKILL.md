---
name: commercial-credit-memo-narrative-drafter
description: Given a borrower's financial spread, credit agreement term sheet, and industry sector, drafts each named narrative section of a commercial credit memo — company overview, management, industry analysis, financial performance, credit strengths and risks, mitigants, and recommendation — with citations to input data and explicit flags where analyst judgment is required to complete the narrative — for Commercial Banking Credit Analysts and Underwriters.
industry: finance
role: Commercial Banking Credit Analyst / Underwriter
trigger: After spreading a borrower's financials and gathering the credit agreement term sheet, before writing the narrative sections of the credit memo; analyst has structured data in hand but faces 4–8 hours of blank-page drafting to complete the memo for credit committee submission.
---

## Context

The analyst has just completed the mechanical work of the underwriting process: financials are spread into the bank's template, key ratios are calculated, and the credit agreement term sheet is summarized. Now comes the highest-time-cost phase — drafting the prose narrative sections that constitute the bulk of the credit memorandum presented to the credit committee.

A commercial credit memo typically includes six to eight named narrative sections. Each section has a distinct analytical purpose, draws on different source inputs, and is held to a different standard of citation and judgment. The sections are not interchangeable:

- **Company Overview** — who the borrower is, what they do, ownership and legal structure
- **Management and Ownership** — key principals, tenure, succession, any ownership changes
- **Industry and Sector Analysis** — market dynamics, competitive position, sector-specific risks
- **Financial Performance** — historical trend analysis, ratio interpretation, key drivers commentary
- **Credit Strengths** — positive factors supporting repayment capacity and loan approval
- **Credit Risks and Concerns** — identified vulnerabilities, concentration risks, stress factors
- **Mitigants** — structural, collateral, and operational factors that offset the risks
- **Recommendation** — proposed loan action, approval conditions, and monitoring requirements

The critical failure mode in AI-assisted credit drafting is fabrication: generating plausible-sounding industry context, management biographies, or financial commentary that is not grounded in the provided inputs. This skill is designed specifically to prevent that failure mode by requiring explicit citations in every drafted section and explicit flags in sections where the provided inputs are insufficient.

The analyst retains full responsibility for reviewing, verifying, and signing off on all narratives before credit committee submission.

---

## Instructions

Follow these steps in sequence. Do not combine steps.

### Step 1 — Inventory the inputs

Before drafting any section, read all provided inputs and produce an **Input Inventory** that lists:

- Each input document or data block provided (e.g., financial spread, term sheet, borrower background questionnaire, site visit notes, SIC/NAICS code, management bios)
- For each input, the key data elements it contains relevant to the credit memo sections
- A **Section Coverage Assessment**: for each of the eight memo sections, state whether the provided inputs contain sufficient data to draft the section without analyst judgment, contain partial data requiring flagging, or contain no relevant data (section cannot be drafted from inputs alone)

Present the Input Inventory and Section Coverage Assessment before writing any narrative section. This forces explicit acknowledgment of data gaps before drafting begins.

### Step 2 — Draft each narrative section in sequence

For each section, follow this drafting protocol:

**A. State the section heading** using the bank's standard heading format (or the heading from the term sheet / memo template if provided).

**B. Write the narrative.** Prose must be written in the third person, past or present tense consistent with bank memo convention (e.g., "The Company operates..." or "Management reported..."). Use complete sentences. Do not use bullet points within narrative sections unless the analyst's template explicitly calls for them.

**C. After each factual claim, insert a parenthetical citation** in the format `[Source: {document or data block}, {specific field or line}]`. Citation must reference a specific data element from the input, not a general document. Acceptable: `[Source: Financial Spread, FY2024 Income Statement — Revenue line]`. Unacceptable: `[Source: provided financials]`.

**D. If a sentence requires information not present in the provided inputs**, replace the sentence with a bracketed flag in this exact format:

`[ANALYST INPUT REQUIRED: {describe the specific information needed and why it is required for this section}]`

Do not draft around the gap with vague language. Do not infer, approximate, or use industry averages to fill gaps unless the analyst has explicitly provided industry benchmarks as an input.

### Step 3 — Company Overview section

Draft 2–4 paragraphs covering:
- Legal name, state of incorporation or formation, business address (if provided)
- Business description: what the company does, primary products or services, customer base characterization (without fabricating specific customer names unless provided)
- Ownership structure: number of owners, ownership percentages, entity type
- Years in operation, any material history (acquisitions, rebranding, restructuring) if evidenced in inputs

If the borrower background questionnaire or term sheet does not provide ownership percentages or entity type, insert `[ANALYST INPUT REQUIRED]` flags at those specific points rather than omitting the paragraph.

### Step 4 — Management and Ownership section

Draft 1–3 paragraphs covering:
- Key principals: names, titles, relevant experience and tenure
- Management depth and succession: bench strength or key-person risk
- Any ownership changes, buyouts, or succession events in the loan term
- Guarantors, if specified in the term sheet

If management bios or résumés are not provided as inputs, draft only what is explicitly stated in the term sheet or questionnaire and flag remaining items with `[ANALYST INPUT REQUIRED: management biography not provided — confirm years of industry experience, prior roles, and succession arrangements]`.

### Step 5 — Industry and Sector Analysis section

Draft 2–3 paragraphs covering:
- Industry definition: SIC/NAICS code or sector as provided, market size or growth characterization
- Competitive dynamics: fragmented vs. concentrated, barriers to entry, pricing power
- Sector-specific macro risks (e.g., input cost volatility, regulatory environment, cyclicality)
- The borrower's competitive positioning within the sector

**Critical constraint for this section**: The analyst must either provide industry context as an explicit input (e.g., a market overview note, an industry report excerpt, or explicit analyst-supplied benchmarks) or this section must be drafted only from the SIC/NAICS code and any sector characterization present in the term sheet, with all unsubstantiated market claims replaced by `[ANALYST INPUT REQUIRED: industry market data not provided — analyst should insert current sector outlook and relevant macro factors before credit committee submission]`.

Do not synthesize industry commentary from general knowledge and present it as grounded analysis. Every market characterization must either cite a provided input or be flagged.

### Step 6 — Financial Performance section

Draft 3–5 paragraphs covering:
- Revenue trend: period-over-period growth or decline with specific figures and calculated growth rates
- Gross margin trend: direction, magnitude, and driver commentary if supported by inputs
- EBITDA and EBITDA margin trend
- Debt service coverage and leverage: calculated ratios with the period they represent
- Liquidity: working capital, current ratio, cash position if available
- Any notable one-time items, restatements, or pro forma adjustments reflected in the spread

For every financial figure cited, include the citation format `[Source: Financial Spread, {period} {statement} — {line item}]`. For calculated ratios, show the inputs: e.g., `DSCR of 1.42x (FY2024) [Source: Financial Spread, FY2024 — EBITDA $2.1M / Total Debt Service $1.48M]`.

Do not characterize trend direction (e.g., "improving," "declining") without citing the specific figures that support the characterization. Do not attribute financial performance to management strategy unless the term sheet or questionnaire explicitly states such attribution.

### Step 7 — Credit Strengths section

Draft a structured list of 3–5 credit strengths. Each strength must:
- Be stated as a one-sentence affirmative claim
- Be followed by one to two sentences of evidentiary support citing specific inputs
- Include a citation to the source data

Do not list strengths that cannot be directly substantiated by the provided inputs. If the inputs support fewer than three strengths, list what is substantiated and add: `[ANALYST INPUT REQUIRED: additional strength factors may exist — analyst should confirm from site visit, industry knowledge, or sponsor diligence before credit committee submission]`.

### Step 8 — Credit Risks and Concerns section

Draft a structured list of 3–5 risks. Each risk must:
- Be stated as a one-sentence concern
- Be followed by one to two sentences quantifying or characterizing the risk with specific citations
- Be assigned a severity label: **High / Medium / Low** — with brief rationale for the label

Do not fabricate risks not evidenced by the inputs. If a standard risk category (e.g., customer concentration) cannot be assessed because the relevant data was not provided, flag it: `[ANALYST INPUT REQUIRED: customer concentration data not provided — confirm top-10 customer revenue concentration before finalizing risk assessment]`.

### Step 9 — Mitigants section

Draft a structured list corresponding to the risks identified in Step 8. For each risk:
- State the mitigant (structural, collateral, guaranty, operating covenant, or other)
- Cite the specific provision or data point that supports the mitigant claim
- Note if the mitigant only partially offsets the risk

If the term sheet does not contain a mitigant for a High-severity risk, flag this explicitly: `[ANALYST JUDGMENT REQUIRED: no structural mitigant identified for [risk name] — analyst should determine whether additional collateral, guaranty, or covenant protection is warranted before approval]`.

### Step 10 — Recommendation section

Draft 1–2 paragraphs covering:
- Proposed loan action (approval, approval with conditions, decline)
- Loan structure summary: amount, tenor, rate type, collateral, guarantors (from term sheet)
- Conditions to closing or ongoing monitoring requirements
- Risk rating if provided or calculable from spread inputs

If the term sheet does not specify a proposed loan action or if the financial data does not clearly support a recommendation, insert: `[ANALYST JUDGMENT REQUIRED: final credit recommendation requires analyst review of all risk factors and bank's internal credit policy thresholds — this draft does not constitute an independent credit opinion]`.

Close the section with: `This credit memorandum is an AI-assisted draft. All narratives, citations, and recommendations require analyst review and verification before credit committee submission.`

---

## Output Format

The output must follow this structure exactly:

```
COMMERCIAL CREDIT MEMORANDUM — NARRATIVE DRAFT
===============================================
Borrower:           [Name from inputs]
Prepared by:        AI-assisted draft — requires analyst review
Draft date:         [today's date]
Input basis:        [list the input documents used]

────────────────────────────────────────────────
PRE-DRAFT: INPUT INVENTORY AND SECTION COVERAGE
────────────────────────────────────────────────

Input Documents Received:
  1. [Document name] — [key data elements]
  2. ...

Section Coverage Assessment:
  | Section                    | Coverage Status                          |
  |----------------------------|------------------------------------------|
  | Company Overview           | FULL / PARTIAL / INSUFFICIENT            |
  | Management and Ownership   | FULL / PARTIAL / INSUFFICIENT            |
  | Industry and Sector        | FULL / PARTIAL / INSUFFICIENT            |
  | Financial Performance      | FULL / PARTIAL / INSUFFICIENT            |
  | Credit Strengths           | FULL / PARTIAL / INSUFFICIENT            |
  | Credit Risks               | FULL / PARTIAL / INSUFFICIENT            |
  | Mitigants                  | FULL / PARTIAL / INSUFFICIENT            |
  | Recommendation             | FULL / PARTIAL / INSUFFICIENT            |

  [PARTIAL: note what is missing]
  [INSUFFICIENT: section will contain primarily [ANALYST INPUT REQUIRED] flags]

────────────────────────────────────────────────
I. COMPANY OVERVIEW
────────────────────────────────────────────────

[Narrative — 2–4 paragraphs, citations inline]

────────────────────────────────────────────────
II. MANAGEMENT AND OWNERSHIP
────────────────────────────────────────────────

[Narrative — 1–3 paragraphs, citations inline]

────────────────────────────────────────────────
III. INDUSTRY AND SECTOR ANALYSIS
────────────────────────────────────────────────

[Narrative — 2–3 paragraphs, citations inline, or [ANALYST INPUT REQUIRED] flags]

────────────────────────────────────────────────
IV. FINANCIAL PERFORMANCE
────────────────────────────────────────────────

[Narrative — 3–5 paragraphs, all financial figures cited]

────────────────────────────────────────────────
V. CREDIT STRENGTHS
────────────────────────────────────────────────

Strength 1: [One-sentence claim]
  [Supporting evidence] [Source: ...]

Strength 2: [One-sentence claim]
  [Supporting evidence] [Source: ...]

[Continue for each strength]

────────────────────────────────────────────────
VI. CREDIT RISKS AND CONCERNS
────────────────────────────────────────────────

Risk 1 [HIGH / MEDIUM / LOW]: [One-sentence concern]
  [Quantified characterization] [Source: ...]
  Severity rationale: [brief explanation]

Risk 2 [HIGH / MEDIUM / LOW]: ...

[Continue for each risk]

────────────────────────────────────────────────
VII. MITIGANTS
────────────────────────────────────────────────

Mitigant for Risk 1: [Mitigant claim]
  [Supporting provision or data] [Source: ...]
  Offset assessment: FULL / PARTIAL

[Continue for each risk]

────────────────────────────────────────────────
VIII. RECOMMENDATION
────────────────────────────────────────────────

[Narrative — 1–2 paragraphs]

This credit memorandum is an AI-assisted draft. All narratives, citations, and
recommendations require analyst review and verification before credit committee
submission.
```

---

## Constraints

- **Do not fabricate financial figures.** Every number in the Financial Performance section must be traceable to a specific line in the provided financial spread. If a ratio requires a calculation, show the inputs.
- **Do not synthesize industry commentary from general knowledge.** The Industry and Sector section must cite a provided input for every market characterization, or flag the gap. Never present training-data knowledge about an industry as sourced analysis.
- **Do not draft around data gaps.** When required information is absent, insert the exact `[ANALYST INPUT REQUIRED: ...]` flag. Do not substitute vague hedge language ("as may be applicable," "typically in this sector") for missing data.
- **Do not provide a credit opinion.** The Recommendation section presents the term sheet's proposed action and conditions; it does not independently adjudicate whether the loan should be approved. The analyst and credit committee make that determination.
- **Do not omit citations in narrative prose.** Every factual claim in sections I through VIII must carry a parenthetical citation. Descriptive language about the borrower (e.g., a characterization of their market position) that cannot be cited must be flagged.
- **Do not use passive attribution.** Do not write "it is understood that" or "it is believed that." Either cite the source or flag the gap.
- **Do not apply bank-specific credit policy thresholds.** Risk ratings, approval thresholds, and required DSCR minimums vary by institution. Do not state or imply what the bank's internal policy requires unless the analyst has provided that policy as an input.
- **Do not conflate fiscal periods.** If the financial spread covers multiple years, use the specific year when citing any figure. Do not reference "recent" or "latest" figures without specifying the period.
- **Do not produce the Input Inventory and Section Coverage Assessment as a separate document.** It must appear inline at the top of the credit memo draft, before Section I.
