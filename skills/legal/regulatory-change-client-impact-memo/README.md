# Regulatory Change to Client Impact Memo

**Industry**: Legal
**Role**: Compliance Attorney / Regulatory Counsel
**Time saved**: 2–4 attorney days per multi-jurisdiction regulatory update cycle

## What it does

Maps new regulatory obligations across one or more jurisdictions against a specific client's business units, operations, and contract provisions, then drafts a client-deliverable impact memo with a jurisdiction-by-jurisdiction obligation table, a prioritized action checklist with hard deadlines, and a cross-jurisdiction conflict analysis.

The key differentiator: this skill performs two-sided reasoning — reading regulatory intent and mapping it against your client's specific facts — so the output is a draft deliverable, not a regulation summary that still requires you to do the client-mapping step manually.

## When to use it

Invoke this skill when:
- A new regulation or legislative instrument has been enacted (or a phased obligation has become actionable) in one or more jurisdictions
- The regulation may affect a client whose business you know well enough to describe (business lines, geographic footprint, entity size, relevant contracts or policies)
- You need to produce a client-facing memo advising them what they must do and by when
- You are covering multiple jurisdictions in the same update cycle and need a single structured document, not parallel siloed summaries

Not suitable for: advisory opinions on regulatory strategy, litigation risk analysis, or instruments where you do not have the regulatory text or a reliable précis.

## Prompt template

```
You are a compliance attorney drafting a client impact memo. Perform the following two-sided regulatory analysis and produce a client-deliverable memo using the exact structure specified below.

---

## REGULATORY INSTRUMENTS

{PASTE EACH REGULATORY TEXT OR RELIABLE PRÉCIS BELOW — LABEL EACH WITH JURISDICTION AND INSTRUMENT NAME}

Instrument 1 — {JURISDICTION}: {INSTRUMENT NAME}
{FULL TEXT OR PRÉCIS}

Instrument 2 — {JURISDICTION}: {INSTRUMENT NAME}
{FULL TEXT OR PRÉCIS}

[Add more instruments as needed]

---

## CLIENT PROFILE

Client name: {CLIENT NAME}
Business description: {DESCRIBE THE CLIENT'S BUSINESS LINES, OPERATIONS, AND RELEVANT ACTIVITIES IN 3–10 SENTENCES}
Geographic footprint: {LIST THE JURISDICTIONS IN WHICH THE CLIENT OPERATES}
Entity characteristics: {STATE ANY FACTS RELEVANT TO APPLICABILITY THRESHOLDS — e.g., employee count, AUM, sector classification, revenue, whether publicly listed}
Key contracts or policies: {OPTIONALLY LIST SPECIFIC CONTRACT TYPES, INTERNAL POLICIES, OR AGREEMENTS RELEVANT TO THE REGULATORY AREAS COVERED}
Role titles used internally: {OPTIONALLY PROVIDE ROLE TITLES SO THE ACTION CHECKLIST USES CLIENT TERMINOLOGY — e.g., "Chief Risk Officer," "Head of EU Operations"}
Memo date: {DATE}
Firm/attorney name: {FIRM NAME OR ATTORNEY NAME, OR LEAVE BLANK}

---

## INSTRUCTIONS

Work through the following steps in order:

**Step 1 — Parse each regulatory instrument.**
For each instrument, identify: issuing authority and jurisdiction; formal name and citation; enacted/effective date; all applicability thresholds; each distinct obligation (numbered, organized by article/section); the compliance deadline for each obligation (hard statutory, phased, or TBD); any safe harbor, exemption, or de minimis carve-out and its conditions; the designated competent authority.

If you have a summary rather than full text, flag this limitation and identify obligations that may be incomplete.

**Step 2 — Assess in-scope status for the client.**
Apply each instrument's applicability thresholds to the client's described facts. Show the threshold test and how the client's facts satisfy or fail it. Flag any threshold fact not provided in the client profile — state both the in-scope and out-of-scope outcome for ambiguous facts. For out-of-scope instruments, record this in one sentence and do not expand on their obligations.

**Step 3 — Map each obligation to the client's specific business units, operations, or contract provisions.**
For each obligation in each in-scope instrument, identify which specific element of the client's described business it affects. Name it explicitly using the client's terminology. If an obligation has no footprint in the client's business, state "No mapped exposure — [reason]" rather than omitting it.

**Step 4 — Classify each obligation as MANDATORY, DISCRETIONARY, or INTERPRETIVELY UNCERTAIN.**
MANDATORY = legally enforceable with a deadline; non-compliance creates regulatory liability.
DISCRETIONARY = only triggered if the client voluntarily engages in a specific optional activity.
INTERPRETIVELY UNCERTAIN = applicability or scope is genuinely unclear; text awaits implementing regulations; or the client's facts fall in a threshold grey zone.

**Step 5 — Build the obligation table.**
Columns: Jurisdiction | Instrument | Article/Section | Obligation Summary | Client Business Unit / Provision | Classification | Compliance Deadline | Safe Harbor?
Sort: MANDATORY first, then DISCRETIONARY, then INTERPRETIVELY UNCERTAIN; within each tier, sort by earliest deadline.

**Step 6 — Write the executive summary.**
3–5 sentences: total instruments and jurisdictions; number of mandatory obligations due in the next 12 months; single highest-priority action and its deadline; any material uncertainty requiring client input. Plain English for a general counsel audience.

**Step 7 — Write the jurisdiction-by-jurisdiction analysis.**
One section per jurisdiction. Overview paragraph (why client is in scope). Then for each MANDATORY and INTERPRETIVELY UNCERTAIN obligation: plain-language obligation description; specific affected client element; required action; deadline; uncertainty note if applicable.

**Step 8 — Write the prioritized action checklist.**
Columns: # | Action | Responsible Party | Deadline | Regulatory Basis | Priority (HIGH / MEDIUM / LOW)
HIGH = MANDATORY within 90 days, or INTERPRETIVELY UNCERTAIN with severe non-compliance cost.
MEDIUM = MANDATORY, 91–365 days.
LOW = MANDATORY beyond 12 months, or DISCRETIONARY likely to be triggered.
Sort by deadline.

**Step 9 — Flag cross-jurisdiction conflicts and tensions.**
If two instruments impose conflicting obligations on the same operation, describe the conflict, cite the specific provisions in tension, and note any practitioner guidance on the conflict. Do not resolve it.

---

## OUTPUT STRUCTURE

Produce the memo using these exact section headers:

**[CLIENT NAME] — MULTI-JURISDICTION REGULATORY IMPACT MEMO**
Prepared by: [Firm/attorney if provided]
Date: [Date if provided]
Instruments analyzed: [List]
Confidentiality: This memorandum is attorney-client privileged and prepared in anticipation of legal advice.

### EXECUTIVE SUMMARY
### APPLICABILITY ANALYSIS
### OBLIGATION TABLE
### JURISDICTION-BY-JURISDICTION ANALYSIS
### CROSS-JURISDICTION CONFLICTS AND TENSIONS
### PRIORITIZED ACTION CHECKLIST
### OPEN ITEMS REQUIRING CLIENT INPUT

---

## GUARDRAILS

- Every obligation in the memo must be mapped to a named element of the client's described business. Do not include obligations purely for completeness.
- Never omit compliance deadlines. If unknown, write "TBD — to be set by [authority]; monitor [official source]."
- Never assert compliance positions on uncertain obligations. Classify them as INTERPRETIVELY UNCERTAIN and describe the ambiguity precisely.
- Never invent regulatory text. If the input is a summary and you are uncertain whether an obligation exists, say so.
- Never conflate mandatory and discretionary obligations in the action checklist.
- Never omit out-of-scope findings from the Applicability Analysis.
- Define all regulatory abbreviations on first use.
- Do not resolve cross-jurisdiction conflicts — flag them for attorney judgment.
- The Open Items section must always appear. If none exist, state "None."
```

## Example output

Below is an abbreviated excerpt showing the Obligation Table and one Action Checklist entry — not a full memo.

---

**ACME FINTECH INC. — MULTI-JURISDICTION REGULATORY IMPACT MEMO**
Prepared by: Thornton & Associates LLP
Date: 2026-06-01
Instruments analyzed: EU AI Act (Regulation (EU) 2024/1689) — European Union; SEC AI Disclosure Rule (Release No. 34-XXXXX) — United States

### EXECUTIVE SUMMARY

This memo analyzes two regulatory instruments across two jurisdictions affecting Acme FinTech Inc.'s credit-decisioning and investment advisory operations. Of the eight mapped obligations identified, five are mandatory with deadlines falling before August 2027. The single highest-priority action is registration of Acme's credit-scoring model under the EU AI Act's Article 49 high-risk AI system database by 2 August 2026. One obligation — applicability of the SEC AI Disclosure Rule to Acme's hybrid human-AI advisory workflow — is interpretively uncertain and requires Acme's input on the percentage of client accounts in which AI output is presented without human override before a compliance position can be finalized.

### OBLIGATION TABLE

| Jurisdiction | Instrument | Article/Section | Obligation Summary | Client Impact | Classification | Deadline | Safe Harbor? |
|---|---|---|---|---|---|---|---|
| EU | EU AI Act | Art. 49 | Register high-risk AI system in EU database before deployment | Credit Decisioning Unit (AI scoring model) | MANDATORY | 2 Aug 2026 | No |
| EU | EU AI Act | Art. 9 | Implement risk-management system for high-risk AI system | Credit Decisioning Unit | MANDATORY | 2 Aug 2026 | No |
| US | SEC AI Disclosure | Rule 206(4)-X | Disclose AI use in client-facing investment advice | Registered Investment Advisory Division | INTERPRETIVELY UNCERTAIN | 1 Jan 2027 | Limited — human-override threshold applies |

### PRIORITIZED ACTION CHECKLIST

| # | Action | Responsible Party | Deadline | Regulatory Basis | Priority |
|---|---|---|---|---|---|
| 1 | Register credit-scoring AI model in EU AI Act high-risk system database | Head of EU Compliance | 2 Aug 2026 | EU AI Act, Art. 49 | HIGH |
| 2 | Document risk-management system covering credit-scoring model per Art. 9 requirements | Chief Risk Officer | 2 Aug 2026 | EU AI Act, Art. 9 | HIGH |
| 3 | Confirm with Acme operations team: percentage of advisory accounts where AI recommendation is delivered without human review override | General Counsel | ASAP — needed to resolve SEC uncertainty | SEC AI Disclosure Rule, preliminary analysis | HIGH |

---

## Tips

1. **Front-load the client profile.** The quality of the client-to-regulation mapping depends entirely on how specifically you describe the client's business. Name the specific operations affected, give the entity size and sector, and provide actual contract types if you have them. Vague profiles produce generic output.

2. **Provide the regulatory text or a reliable official summary, not a news article.** News coverage routinely omits threshold tests, phased deadlines, and safe harbor conditions — the details that determine whether a specific client is in scope. Official regulator websites, Official Journal (EU), Federal Register (US), and Legislation.gov.uk (UK) are preferred sources.

3. **Use the INTERPRETIVELY UNCERTAIN classification actively.** Regulatory grey zones are common and professionally important. If the output classifies an obligation as INTERPRETIVELY UNCERTAIN, treat that as an action item: it is telling you exactly what client facts you need to gather to finalize the advice. The Open Items section will list these gaps explicitly.
