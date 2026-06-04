---
name: rfp-response-coordinator
description: Given an RFP or security questionnaire and a content library of prior responses, classifies every requirement by type, runs explicit keyword-level verification to prevent fabricated matches, flags non-functional submission constraints, drafts first-pass responses for matched items, and produces a gap list with precision-routed SME assignments — for Sales Engineers and Solutions Consultants managing enterprise deal cycles.
industry: technology
role: Sales Engineer / Solutions Consultant
trigger: The moment a prospect's RFP, DDQ, or security questionnaire lands in the SE's inbox and needs to be triaged before the response kickoff meeting — SE has the requirements document and a content library of prior answers, and faces 20–40 hours of manual matching, drafting, and stakeholder coordination before the first draft can go out.
---

## Context

A Sales Engineer receives an RFP, security questionnaire, or due diligence questionnaire (DDQ) from a prospective enterprise customer. The document contains anywhere from 40 to 400 numbered requirements spanning security controls, technical capabilities, integrations, compliance certifications, and commercial terms. The SE's job is to:

1. Scan the cover page and preamble for submission constraints before any other work begins
2. Triage every requirement to determine whether the content library can answer it as-is, with adaptation, partially, or not at all
3. Apply an explicit keyword verification before any match is confirmed — a requirement can only match a library entry if that entry mentions the specific integration name, certification name, or feature name the requirement asks about
4. Distinguish requirements that appear similar but belong to distinct domains: PAM and MFA are not interchangeable; data deletion policy and data subject access requests are not interchangeable; WORM storage and general retention policy are not interchangeable
5. Draft first-pass responses only for requirements where keyword-verified library coverage exists
6. Build a gap list with routing precision — differentiating "retrieve existing documentation" from "build new capability," and assigning each gap to the correct SME bucket via a deterministic routing table
7. Produce a response tracker the whole team can work from, with a Coordinator Summary that leads with any process constraints that affect how the output can be used

The critical discipline this skill enforces: a drafted response must trace to a content library entry by verbatim keyword match, or it must be classified as NO MATCH. General knowledge about the vendor's product category, industry norms, or likely capabilities is never a valid basis for drafting a response.

---

## Instructions

Follow these steps in sequence. Do not skip steps or merge them. Each step is named and must be completed in full before the next step begins.

### Step 0 — Scan for process constraints (mandatory first step)

Before reading the requirements, read the RFP or DDQ cover page, cover email, and preamble section in their entirety.

Identify any instructions that impose constraints on how responses may be prepared or submitted. Specifically look for:
- Certification or attestation requirements (e.g., "responses must be certified by a named InfoSec officer," "responses must be signed by a qualified professional")
- Restrictions on AI-generated content (e.g., "AI-generated responses may not be used as submitted," "all AI-drafted content must be attested before submission")
- Submission format mandates (e.g., "responses must be entered into our vendor portal," "PDF only, no Word documents")
- Legal or compliance acknowledgments required from a named executive

Record each such constraint as a **Process Constraint** item. Each item should state: what the constraint is, where in the document it appears, and what action the SE must take before distributing the output.

If no such constraints are present, record: "No process constraints identified in cover page or preamble."

These Process Constraints must appear at the top of the Coordinator Summary in Step 5 under the heading **Process Constraints — Human Review Required**, before any other summary content. This is mandatory regardless of whether any other step produces clean results.

### Step 1 — Parse and inventory the RFP

Read the full RFP or questionnaire and produce a **Requirement Inventory Table** before any matching or drafting.

For each numbered or lettered requirement, record:
- **Req ID** — the original numbering or lettering from the document (e.g., "3.2.1", "Section 4 — Q7")
- **Requirement text** — verbatim from the source document; do not paraphrase
- **Requirement type** — classify as one of: `Security`, `Technical Capability`, `Integration`, `Compliance/Regulatory`, `Commercial/Legal`, or `General/Administrative`
- **Classification rationale** — one sentence; if a requirement spans two types, assign the primary type and note the secondary

Apply these type-assignment rules:
- Security controls, encryption, access management, incident response, audit logging, vulnerability management, penetration testing → `Security`
- Platform features, data ingestion, visualization, reporting, alerting → `Technical Capability`
- Named third-party systems, SSO/IdP integrations, APIs, connectors, data feeds by product name → `Integration`
- Legal certifications (SOC 2, HITRUST, HIPAA compliance programs, ISO 27001), regulatory obligations (SEC rules, GDPR, HIPAA Breach Notification), legal agreements (DPA, BAA), insurance → `Compliance/Regulatory`
- Pricing, contract terms, SLAs, credits → `Commercial/Legal`
- Company overview, ownership, employee count → `General/Administrative`

Important: requirements asking about named third-party products (Bloomberg, Advent Geneva, Salesforce, Okta, etc.) are `Integration` type, not `Security` or `Technical Capability`, even when the topic of the integration is security-related (e.g., "Do you support SAML 2.0 SSO with Okta?" is `Integration`).

Present the complete Requirement Inventory Table before proceeding. Count requirements by type and report the breakdown.

### Step 2 — Keyword verification pass (mandatory before any match assignment)

This step must be completed before any match type is assigned. Its purpose is to prevent a requirement from being matched to a library entry that does not actually cover the specific named entity, certification, or feature the requirement asks about.

For each requirement in the Inventory Table, perform the following keyword check against the full content library text:

**A. Extract the key named entities from the requirement.** These are:
- Named integrations and products (e.g., "Bloomberg BVAL," "Advent Geneva," "Okta," "SAML 2.0")
- Named certifications and frameworks (e.g., "SOC 2 Type II," "HITRUST CSF," "ISO 27001," "HIPAA")
- Named regulatory obligations (e.g., "SEC Rule 17a-4," "GDPR," "CCPA," "WORM storage")
- Named security domains (e.g., "privileged access management," "data classification policy," "data subject access request," "immutable audit log," "BYOK")

**B. For each key named entity, ask verbatim: "Does any content library entry mention [entity name] by name?"**

Examples of how this check works:
- Requirement asks about Bloomberg BVAL integration. Check: "Does any library entry mention 'Bloomberg'?" If no entry uses the word Bloomberg → NO MATCH. Do not use a generic REST API or data ingestion entry as a substitute.
- Requirement asks about Advent Geneva OMS integration. Check: "Does any library entry mention 'Advent Geneva'?" No → NO MATCH.
- Requirement asks about HITRUST CSF certification. Check: "Does any library entry mention 'HITRUST'?" No → NO MATCH, regardless of whether a SOC 2 entry exists.
- Requirement asks about SEC Rule 17a-4 WORM storage configuration. Check: "Does any library entry mention 'WORM' or '17a-4' or 'immutable record retention'?" No → NO MATCH. A data retention or deletion policy entry that does not mention WORM is not a match for a WORM requirement.
- Requirement asks about privileged access management (PAM). Check: "Does any library entry mention 'privileged access management' or 'PAM'?" No → NO MATCH. Do not match a multi-factor authentication (MFA) entry to a PAM requirement; these are distinct security domains (MFA governs authentication factors; PAM governs elevated access to infrastructure systems). Record the distinction explicitly: "PAM and MFA are distinct security domains — not eligible for cross-match."
- Requirement asks about data subject access requests (DSARs) or subject rights for ePHI. Check: "Does any library entry mention 'data subject access request,' 'DSAR,' or 'subject rights'?" No → NO MATCH. Do not match a data deletion or data retention entry to a DSAR requirement; these are distinct legal obligations under HIPAA and GDPR. Data deletion describes what happens at contract termination; subject access rights describe what individuals can request about their data during the contract. Record the distinction explicitly: "Data deletion policy and data subject access rights are distinct obligations — not eligible for cross-match."
- Requirement asks about immutable audit logging with customer-controlled export. Check: "Does any library entry mention 'immutable' audit log or 'customer-controlled' log storage?" If an RBAC/audit entry only mentions audit logging via admin console but does not address immutability or customer-controlled export → classify as PARTIAL (covers audit capability) with a gap note, not DIRECT.

**C. Domain alignment check for ADAPT and PARTIAL candidates.** Before assigning ADAPT or PARTIAL:
- Verify the library entry and the requirement are in the same domain. Closeness of topic is insufficient; domain overlap is required.
- If the requirement asks about one security control and the library entry covers a different security control in the same general area, classify as NO MATCH unless the entry's coverage explicitly addresses the sub-domain the requirement asks about.
- Record the domain alignment check result in the Adaptation Note column: "Domain verified: [library entry domain] matches [requirement domain]" or "Domain mismatch: [entry covers X]; [requirement asks about Y]; classified as NO MATCH."

Record the keyword check result for each requirement before assigning a match type. The match type assignment in Step 2's output table must be consistent with the keyword check result.

**D. Library staleness and context mismatch check.** After completing the keyword check:
- Review the Prospect Context provided in the input. If the Prospect Context mentions that a capability, certification, or product feature exists internally at the vendor but is not reflected in any content library entry, note this explicitly.
- For any such gap, flag the entry as: "NOTE: Prospect Context indicates this capability may exist internally but is not reflected in the provided library. Confirm current status before routing as 'build this capability' vs. 'retrieve existing documentation.'"
- This flag affects routing in Step 4: if context suggests capability exists, route to the relevant SME to retrieve documentation; if no context suggests existence, route to Product Management or Engineering to assess feasibility.

Now produce the Content Library Matching Table with these columns:
- **Req ID**
- **Keyword check** (one sentence: which named entity was checked and what was found)
- **Library match** (specific entry ID/title, or "NO MATCH")
- **Match type** (DIRECT / ADAPT / PARTIAL / NO MATCH)
- **Confidence** (High / Medium / Low for DIRECT/ADAPT; N/A for NO MATCH)
- **Adaptation note** (for ADAPT and PARTIAL; include domain alignment check result)

Do not draft responses in this step. Complete the full matching pass first.

### Step 3 — Draft first-pass responses for DIRECT and ADAPT matches

For each requirement where Match Type is `DIRECT` or `ADAPT`:

**A.** Start from the matched content library entry verbatim.

**B.** For `DIRECT` matches: copy the library entry text as-is. Add `[DIRECT — no adaptation required]` at the end of the draft text.

**C.** For `ADAPT` matches: apply the adaptation identified in Step 2. Changes must be limited to:
- Substituting the prospect's named systems, integrations, or technologies (as mentioned in the RFP)
- Adjusting terminology to match the prospect's RFP language (e.g., they call it "data residency" where the library says "data localization")
- Removing references to features or certifications not applicable to this prospect's tier or region
- Adding one to two sentences connecting the answer to the prospect's stated use case or business context (draw only from information present in the RFP, not general knowledge about the prospect's industry)

**D.** Add `[ADAPT — changes from library: {brief description of what was changed}]` at the end.

**E.** For `PARTIAL` matches: draft the portion covered by the library entry using the same protocol as ADAPT, then add `[PARTIAL — unaddressed portion: {describe the gap}] [SME INPUT REQUIRED: {recommended owner and specific question}]`.

**F.** Do not draft text for `NO MATCH` requirements in this step.

**G.** Fabrication prohibition (enforced by keyword verification from Step 2): A drafted response may only state capabilities, certifications, or integrations that are explicitly named in the matched library entry. If the keyword verification in Step 2 found that the requirement names an entity not present in any library entry, the requirement must be NO MATCH and no response is drafted. Do not use general knowledge about the product category or the vendor's industry to supplement library content.

**H.** Named-entity preservation: When adapting a library entry that lists specific named items (e.g., a list of identity providers, a list of certifications, a list of sub-processors), do not expand the list beyond what the entry states. Adding names not in the library entry is fabrication. If the prospect's RFP asks about an IdP not in the library's list, add a note: "[NOTE: Prospect asks about [IdP name] — not confirmed in library entry; add only if Engineering confirms support]" rather than silently including it.

### Step 4 — Build the gap list for NO MATCH and PARTIAL requirements

For each `NO MATCH` requirement (and for the unaddressed portion of each `PARTIAL`), produce a Gap Entry.

**A. Apply the routing decision table below.** For each gap, assign the owner bucket using this table — do not deviate from it without recording a rationale:

| Gap type | Owner bucket |
|----------|-------------|
| Integration design: APIs, SSO configuration, named data connectors (Bloomberg, Advent Geneva, etc.), custom data feeds | Engineering/Architecture |
| Compliance certification gaps: SOC 2, HITRUST, ISO 27001, FedRAMP, HIPAA compliance program | Legal/Compliance or Security Team (see sub-rule below) |
| Regulatory obligation gaps: SEC rules, GDPR compliance, CCPA, WORM storage, BAA execution | Legal/Compliance |
| HIPAA-specific gaps (BAA, HIPAA training, breach notification, ePHI handling): | Legal/Compliance (not Security Team alone — HIPAA is a legal obligation requiring counsel) |
| Internal security control gaps: PAM, background checks, vulnerability management, pen testing, incident response | Security Team |
| Financial and commercial terms | Finance/Commercial |
| Vertical experience, customer references, case studies | Executive Sponsor or Sales |
| Internal documentation gaps (capability confirmed to exist by context, docs missing from library) | Relevant SME (Security Team, Engineering, or Legal) + flag for library refresh |
| Product roadmap and feature availability | Product Management |
| Background checks and HR policy | Legal/Compliance or HR (flag for internal routing) |

Sub-rule for compliance certifications: if the gap is a certification the vendor holds (confirmed by Prospect Context or internal knowledge), route to Security Team with a note to retrieve existing certification documentation. If the vendor does not hold the certification and would need to pursue it, route to Legal/Compliance with a note to assess feasibility and timeline.

**B. Apply the context check from Step 2 Section D.** If a gap was flagged as "context indicates this capability may exist internally," set the recommended input source to: "[SME bucket] — NOTE: Context suggests this capability may exist but is not reflected in provided library. Confirm current status before routing as 'build this capability' vs. 'retrieve existing documentation.' If confirmed existing, route to [SME] to retrieve documentation and flag for library refresh. If capability does not exist, route to [Product/Engineering/Legal] to assess feasibility."

**C. Gap Entry fields:**

- **Req ID** — as assigned in Step 1
- **Requirement text** — verbatim
- **Requirement type** — from Step 1
- **Why no match exists** — one sentence; must state specifically what the requirement asks for that no library entry covers (e.g., "Prospect asks for WORM storage configuration per SEC 17a-4; library entry ENTRY-SEC-006 covers standard data deletion only — no mention of WORM, immutable retention, or 17a-4")
- **Context flag** — "Capability confirmed by context — retrieve documentation" or "No context confirmation — assess capability status" or "N/A"
- **Recommended owner** — from routing table above
- **Recommended input source** — most likely specific document, system, or named contact
- **Priority** — `Critical` (requirement is a stated deal qualifier or mandatory per RFP preamble; absence of answer risks disqualification), `High` (important but answerable with standard due diligence), or `Standard` (informational, non-disqualifying). Requirements stated as "mandatory" in the RFP preamble or Prospect Context are automatically `Critical`.
- **Suggested deadline** — derived from the RFP due date; Critical gaps should be flagged for input within 24–48 hours of kickoff

### Step 5 — Produce the response tracker and coordinator summary

Produce a single structured Response Tracker that consolidates all requirements into one table. Then produce the Coordinator Summary.

Tracker columns:
- **Req ID**
- **Section** (the section heading from the original RFP)
- **Requirement text** (verbatim, truncated to 80 characters with "[...]" if longer)
- **Type** (from Step 1)
- **Match type** (DIRECT / ADAPT / PARTIAL / NO MATCH)
- **Confidence** (High / Medium / Low / N/A)
- **Draft status** (DRAFTED / NEEDS SME INPUT / AWAITING APPROVAL)
- **Assigned owner** (for drafted items: SE or named reviewer; for gap items: the SME bucket from Step 4)
- **Note** (for drafted items: [DIRECT] or [ADAPT] notation; for gap items: priority label and context flag)

After the tracker table, produce the **Coordinator Summary** in the following order — do not reorder these sections:

1. **Process Constraints — Human Review Required** (from Step 0): list every constraint identified. If none, state "None identified." This section must appear first in the Coordinator Summary even if it is empty.
2. Total requirement count and breakdown by type
3. Coverage: count and percentage ready for SE review (DIRECT + ADAPT drafted); count and percentage requiring SME input by owner bucket
4. Critical gaps: list each, with assigned owner, context flag, and suggested deadline
5. Recommended review meeting agenda: ordered by deadline risk and gap concentration

Close the entire output with: "This tracker is an AI-assisted draft. All drafted responses require SE review for technical accuracy. Adapted content requires explicit approval from the content library owner before inclusion in the submitted RFP response. Any process constraints listed above must be resolved before distribution."

---

## Output Format

The output must follow this structure in order:

```
RFP RESPONSE COORDINATOR
========================
Prospect:           [Name from RFP]
RFP due date:       [Date from RFP or "Not specified"]
Coordinator:        AI-assisted draft — SE review required before distribution
Prepared:           [today's date]
Content library:    [List of library entries/documents provided]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 0 — PROCESS CONSTRAINTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Process Constraint 1: [What it requires] — Source: [cover page / preamble / cover email] — SE Action Required: [specific action]
...
OR: No process constraints identified in cover page or preamble.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1 — REQUIREMENT INVENTORY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Req ID | Requirement Text (verbatim) | Type | Classification Rationale |
|--------|----------------------------|------|--------------------------|
| ...    | ...                        | ...  | ...                      |

Requirement count by type:
  Security: [N]  |  Technical Capability: [N]  |  Integration: [N]
  Compliance: [N]  |  Commercial: [N]  |  General: [N]
  TOTAL: [N]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2 — KEYWORD VERIFICATION AND CONTENT LIBRARY MATCHING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Req ID | Keyword Check | Library Match | Match Type | Confidence | Adaptation Note |
|--------|---------------|---------------|------------|------------|-----------------|
| ...    | ...           | ...           | ...        | ...        | ...             |

Matching summary:
  DIRECT: [N]  |  ADAPT: [N]  |  PARTIAL: [N]  |  NO MATCH: [N]

Library staleness flags (from Step 2D):
  [List any requirements where Prospect Context indicates capability may exist but is not in library]
  OR: None.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 3 — DRAFTED RESPONSES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Req ID] — [Type] — [Match Type: DIRECT/ADAPT/PARTIAL] — Confidence: [High/Medium/Low]
Requirement: [verbatim requirement text]
Draft response:
  [Drafted text]
  [DIRECT — no adaptation required]
  OR
  [ADAPT — changes from library: ...]
  OR
  [PARTIAL — unaddressed portion: ...] [SME INPUT REQUIRED: ...]

---

[Repeat for each drafted requirement]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 4 — GAP LIST (NO MATCH AND PARTIAL UNADDRESSED PORTIONS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Gap [N]: [Req ID] — [Priority: CRITICAL / HIGH / STANDARD]
Requirement: [verbatim requirement text]
Type: [from Step 1]
Why no match: [one sentence — what the requirement specifically asks for that is absent from the library]
Context flag: [Capability confirmed by context — retrieve documentation | No context confirmation — assess capability status | N/A]
Recommended owner: [from routing table]
Recommended input source: [specific document or contact; include library staleness note if applicable]
Suggested deadline: [date or "TBD — confirm against RFP due date"]

---

[Repeat for each NO MATCH requirement]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 5 — RESPONSE TRACKER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Req ID | Section | Requirement Text | Type | Match | Confidence | Draft Status | Owner | Note |
|--------|---------|-----------------|------|-------|------------|--------------|-------|------|
| ...    | ...     | ...              | ...  | ...   | ...        | ...          | ...   | ...  |

COORDINATOR SUMMARY
-------------------

PROCESS CONSTRAINTS — HUMAN REVIEW REQUIRED:
  [List from Step 0, or "None identified."]
  [This section must appear even if empty.]

Total requirements: [N]
Requirements breakdown: Security [N] | Technical [N] | Integration [N] | Compliance [N] | Commercial [N] | General [N]

Coverage:
  Ready for SE review (DIRECT + ADAPT): [N] ([%] of total)
  Requires SME input: [N] ([%] of total)
    - Security Team: [N]
    - Product Management: [N]
    - Engineering/Architecture: [N]
    - Legal/Compliance: [N]
    - Finance/Commercial: [N]
    - Executive Sponsor / Sales: [N]

Critical gaps requiring immediate routing:
  1. [Req ID]: [one-sentence gap description] — Owner: [SME bucket] — Context flag: [retrieve docs / assess capability / N/A] — Deadline: [date]
  2. ...

Recommended review meeting agenda:
  1. [Topic/section] — [rationale]
  2. ...

This tracker is an AI-assisted draft. All drafted responses require SE review for
technical accuracy. Adapted content requires explicit approval from the content
library owner before inclusion in the submitted RFP response. Any process
constraints listed above must be resolved before distribution.
```

---

## Constraints

- **Do not fabricate product capabilities, certifications, integrations, or regulatory configurations.** The keyword verification in Step 2 is the enforcement mechanism. A requirement may only be classified as DIRECT, ADAPT, or PARTIAL if a library entry explicitly names the integration, certification, or capability the requirement asks about. General knowledge about the product category or vendor's market position is not a valid source.
- **Do not cross-match distinct security or legal domains.** PAM (privileged access management for infrastructure) and MFA (authentication factors for user login) are distinct security controls — a library entry covering one does not cover the other. Data deletion policy (what happens at contract termination) and data subject access rights (DSAR — what individuals may request during the contract) are distinct legal obligations — a library entry covering one does not cover the other. WORM/immutable storage and general data retention policy are distinct technical requirements — a library entry covering one does not cover the other. When in doubt, apply the domain alignment check from Step 2C and classify as NO MATCH.
- **Do not skip Step 0.** Process constraints from the cover page must be surfaced before any other output is produced. A tracker distributed without this step exposes the SE to compliance risk and prospect rejection.
- **Do not skip the keyword verification pass in Step 2.** The Requirement Inventory (Step 1) and the Content Library Matching (Step 2) are separate steps for a reason. Matching cannot happen until the full inventory is complete and keyword checks have been run.
- **Do not paraphrase requirement text.** Verbatim requirement language must appear in the Inventory Table, the Drafted Responses, and the Gap List. Paraphrasing creates compliance risk when the prospect's reviewers check responses against their exact wording.
- **Do not merge sub-requirements.** If the RFP lists two sub-questions under one number (e.g., "3.4a" and "3.4b"), treat each as a separate requirement.
- **Do not expand named-entity lists beyond what the library entry states.** If the library entry lists three identity providers, the drafted response lists three identity providers — not five. Names not in the library require SME confirmation before inclusion.
- **Do not route all gaps to Product Management.** Integration design gaps go to Engineering/Architecture. HIPAA-specific and legal agreement gaps go to Legal/Compliance. Internal security control gaps go to Security Team. See the routing table in Step 4.
- **Do not assign "build this capability" routing to a gap where Prospect Context confirms the capability already exists.** If the SE's context note indicates the capability or certification is in-house but undocumented in the library, route to the appropriate SME to retrieve or produce the documentation, and flag the library entry for refresh.
- **Do not invent deadlines.** Suggested deadlines must be derived from the RFP due date in the input. If no due date is provided, state "TBD — confirm RFP submission date before assigning."
- **Do not produce the Coordinator Summary before the Response Tracker table.** The summary must follow the tracker.
- **Do not apply this skill if the RFP or DDQ explicitly prohibits AI-assisted responses and no human review step is planned.** Step 0 will have surfaced this constraint; the SE must decide whether to use this output given the certification requirements identified.
