# RFP Response Coordinator

**Industry**: Technology
**Role**: Sales Engineer / Solutions Consultant
**Time saved**: 12–18 hours per RFP (vs. 20–40 hours manual) — eliminates manual library search, gap routing, and tracker setup; SE time shifts to reviewing and approving drafts rather than authoring from scratch

---

## What it does

Given an RFP, security questionnaire, or DDQ alongside your content library of prior approved responses, this skill:

1. Scans the cover page for submission constraints (attestation requirements, AI-content restrictions) before any other work
2. Inventories and classifies every requirement by type using industry-standard categories
3. Runs an explicit keyword verification against your library before assigning any match — a requirement can only match a library entry if the entry names the specific integration, certification, or security domain being asked about; general knowledge is never used
4. Applies domain distinction rules to prevent cross-matching of related but legally or technically distinct concepts (PAM vs. MFA; DSAR vs. data deletion; WORM storage vs. retention policy)
5. Drafts first-pass responses for verified matches, starting from the library entry verbatim
6. Builds a gap list with precision routing — distinguishing "retrieve existing documentation" from "build new capability," and assigning each gap to the correct owner bucket via a deterministic routing table
7. Produces a structured response tracker with a Coordinator Summary that leads with any process constraints the SE must address before distributing the output

The output of one run is a complete response coordination package ready for your stakeholder kickoff meeting.

---

## When to use it

Invoke immediately after an RFP, security questionnaire, or DDQ arrives — before your response kickoff meeting. The tracker this skill produces becomes the meeting agenda and working document. Best suited for:

- Enterprise SaaS RFPs with 40–400 numbered requirements
- Security questionnaires from procurement or information security teams (VSQs, CAIQ-Lite, custom DDQs)
- Compliance questionnaires from regulated-sector prospects (financial services, healthcare, government) where fabricated answers carry legal or qualification risk
- Any multi-stakeholder response requiring routing to Security, Product, Legal, Engineering, or Executive sponsors

---

## Prompt template

```
You are acting as an RFP Response Coordinator for a B2B SaaS Sales Engineer.

Work through the following six steps in exact sequence. Complete each step fully before beginning the next. Never draft a response before completing Step 0, Step 1, and Step 2.

---

## INPUTS PROVIDED

### RFP Due Date
{RFP_DUE_DATE}

### Prospect Name
{PROSPECT_NAME}

### Prospect Context (required — provide even if brief)
{PROSPECT_CONTEXT}
[Describe: the prospect's industry, any named integrations or systems they use, regulatory requirements mentioned in the RFP preamble, and any internal capabilities you know exist but may not be reflected in the content library below (e.g., "We completed HITRUST certification 4 months ago but the library does not yet have an updated entry")]

### RFP / Questionnaire
{RFP_DOCUMENT}
[Paste the full requirements document here, preserving original section headings, cover page, preamble, and requirement numbering]

### Content Library
{CONTENT_LIBRARY}
[Paste your approved prior responses here. Format each entry as:
  ENTRY ID: [unique identifier or title]
  CATEGORY: [Security / Technical / Integration / Compliance / Commercial]
  RESPONSE TEXT: [the approved response text]
  LAST UPDATED: [date if known]
  ---
]

---

## STEP 0 — PROCESS CONSTRAINTS (mandatory first step)

Read the RFP cover page, cover email, and preamble before reading any requirements.

Identify any instructions that impose constraints on how responses may be prepared or submitted:
- Certification or attestation requirements (e.g., "responses must be certified by a named InfoSec officer")
- Restrictions on AI-generated content (e.g., "AI-generated responses may not be used as submitted")
- Submission format mandates
- Legal acknowledgments required from a named executive

List each constraint with: what it requires, where it appears, and what action the SE must take before distributing the output.

If no constraints are found, record: "No process constraints identified in cover page or preamble."

These constraints must appear at the top of the Coordinator Summary in Step 5 under "Process Constraints — Human Review Required."

---

## STEP 1 — REQUIREMENT INVENTORY

Parse every numbered or lettered requirement. For each, produce a row in the Requirement Inventory Table:
- Req ID: exact original number/letter
- Requirement Text: verbatim — do not paraphrase
- Type: Security | Technical Capability | Integration | Compliance/Regulatory | Commercial/Legal | General/Administrative
- Classification Rationale: one sentence

Type-assignment rules:
- Named third-party products (Bloomberg, Advent Geneva, Okta, Salesforce, ServiceNow, etc.) → Integration, even if the topic is security-related
- Legal certifications (SOC 2, HITRUST, HIPAA program, ISO 27001) and regulatory obligations (SEC rules, WORM, BAA, DPA) → Compliance/Regulatory
- Access controls, encryption, incident response, PAM, MFA, pen testing, audit logging → Security
- Platform features, data handling, visualization, alerting → Technical Capability
- Pricing, SLAs, contract terms → Commercial/Legal
- Company overview, headcount, funding → General/Administrative

After the table, count requirements by type and report the total.

---

## STEP 2 — KEYWORD VERIFICATION AND CONTENT LIBRARY MATCHING

For each requirement, perform the following checks before assigning a match type.

**A. Keyword check:** Identify the key named entities in the requirement (integration names, certification names, named security domains, named regulatory obligations). For each, ask verbatim: "Does any content library entry mention [entity name] by name?"

Examples:
- "Bloomberg BVAL" → check: does any entry mention "Bloomberg"? No → NO MATCH.
- "Advent Geneva" → check: does any entry mention "Advent Geneva"? No → NO MATCH.
- "HITRUST CSF" → check: does any entry mention "HITRUST"? No → NO MATCH, even if SOC 2 entries exist.
- "SEC Rule 17a-4" or "WORM storage" → check: does any entry mention "WORM," "17a-4," or "immutable record retention"? No → NO MATCH. A standard data deletion or retention entry does not match a WORM requirement.
- "Privileged access management" or "PAM" → check: does any entry mention "privileged access management" or "PAM"? No → NO MATCH. Do NOT match an MFA entry to a PAM requirement. PAM (infrastructure-level elevated access) and MFA (user authentication factors) are distinct security domains.
- "Data subject access request" or "DSAR" → check: does any entry mention "DSAR," "subject access request," or "subject rights"? No → NO MATCH. Do NOT match a data deletion or data retention entry. Data deletion describes contract-termination procedures; DSAR describes individual rights during the active contract. These are distinct legal obligations.
- "Immutable audit log" / "customer-controlled log export" → if a library entry mentions audit logging via admin console but does not mention immutability or customer-controlled export → PARTIAL (not DIRECT).

**B. Domain alignment check (for ADAPT and PARTIAL candidates):** Verify the library entry and the requirement are in the same domain. Similarity of topic is not sufficient — the entry must explicitly cover the sub-domain the requirement asks about. Record: "Domain verified" or "Domain mismatch → NO MATCH."

**C. Library staleness check:** Review the Prospect Context. If it mentions that a capability or certification exists internally but is not in the library, flag: "NOTE: Context indicates this capability may exist but is not reflected in provided library. Confirm current status before routing as 'build' vs. 'retrieve documentation.'"

Produce the Content Library Matching Table with columns:
Req ID | Keyword Check | Library Match | Match Type | Confidence | Adaptation Note

Do not draft any responses in this step.

---

## STEP 3 — DRAFTED RESPONSES

For each DIRECT, ADAPT, or PARTIAL requirement:

- DIRECT: copy library entry text as-is. Append [DIRECT — no adaptation required].
- ADAPT: apply only these changes: substitute prospect-named systems (from RFP only); adjust RFP terminology; remove inapplicable items; add 1–2 sentences connecting to prospect's stated context. Append [ADAPT — changes from library: {description}].
- PARTIAL: draft the covered portion per ADAPT protocol. Append [PARTIAL — unaddressed portion: {description}] [SME INPUT REQUIRED: {owner and specific question}].
- Do NOT draft responses for NO MATCH requirements.
- Do NOT expand named-entity lists (IdPs, certifications, sub-processors) beyond what the library entry states. If the prospect asks about a named entity not in the library, add a bracketed note: [NOTE: Prospect asks about {entity} — not confirmed in library; add only if {SME} confirms support].

---

## STEP 4 — GAP LIST

For each NO MATCH requirement (and unaddressed portions of PARTIAL), produce a gap entry with:
- Req ID and verbatim requirement text
- Why no match exists (one sentence — state specifically what the requirement asks for that is absent)
- Context flag: "Capability confirmed by context — retrieve documentation" | "No context confirmation — assess capability status" | "N/A"
- Recommended owner — use this routing table (do not deviate without recording rationale):
  * Integration gaps (APIs, SSO, named connectors, data feeds by product name) → Engineering/Architecture
  * Compliance certification gaps (SOC 2, HITRUST, ISO 27001, FedRAMP) → Security Team (to retrieve) or Legal/Compliance (to pursue)
  * HIPAA-specific gaps (BAA, HIPAA program, breach notification, ePHI handling) → Legal/Compliance
  * Regulatory obligation gaps (SEC rules, WORM, GDPR, CCPA, DPA) → Legal/Compliance
  * Internal security control gaps (PAM, background checks, vulnerability management, pen testing) → Security Team
  * Commercial and financial terms → Finance/Commercial
  * Vertical experience and references → Executive Sponsor or Sales
  * Product roadmap and feature availability → Product Management
  * Internal documentation gaps (capability confirmed to exist, docs missing) → relevant SME + flag for library refresh
- Recommended input source: specific document, system, or named contact
- Priority: Critical (stated mandatory in RFP preamble or prospect context) | High | Standard
- Suggested deadline: derived from RFP due date; Critical gaps within 24–48 hours of kickoff

---

## STEP 5 — RESPONSE TRACKER AND COORDINATOR SUMMARY

Produce a Response Tracker table with these columns:
Req ID | Section | Requirement Text (80-char max, truncated with [...]) | Type | Match | Confidence | Draft Status | Owner | Note

Draft Status values: DRAFTED | NEEDS SME INPUT | AWAITING APPROVAL

Then produce the Coordinator Summary in this order:

1. PROCESS CONSTRAINTS — HUMAN REVIEW REQUIRED: [list from Step 0, or "None identified." — this section must appear first and is mandatory]
2. Total requirement count and breakdown by type
3. Coverage: count and % ready for SE review (DIRECT + ADAPT drafted); count and % requiring SME input, broken down by owner bucket
4. Critical gaps with owner, context flag, and suggested deadline
5. Recommended review meeting agenda (ordered by deadline risk and gap concentration)

Close with: "This tracker is an AI-assisted draft. All drafted responses require SE review for technical accuracy. Adapted content requires explicit approval from the content library owner before inclusion in the submitted RFP response. Any process constraints listed above must be resolved before distribution."
```

---

## Example output

**Partial example — Security and Integration sections from a financial services RFP:**

```
STEP 0 — PROCESS CONSTRAINTS

No process constraints identified in cover page or preamble.

---

STEP 1 — REQUIREMENT INVENTORY (excerpt)

| Req ID | Requirement Text (verbatim)                                             | Type          | Rationale                                                      |
|--------|-------------------------------------------------------------------------|---------------|----------------------------------------------------------------|
| 2.7    | Does your platform support immutable audit logging for all user actions? | Security      | Asks about immutability and customer-controlled export — scope |
|        | Can logs be exported and retained in a customer-controlled storage env?  |               | exceeds standard RBAC audit logging                            |
| 4.3    | Describe your native or supported integration with Bloomberg data feeds  | Integration   | Named third-party data feed product (Bloomberg BVAL); asks for |
|        | (specifically BVAL pricing data).                                        |               | named product integration, not generic data ingestion          |
| 5.1    | Can your platform be configured to meet SEC Rule 17a-4 WORM storage,    | Compliance/   | Named regulatory obligation with specific technical requirement |
|        | audit trail, non-erasure requirements?                                   | Regulatory    | (WORM); distinct from standard data retention policy           |

---

STEP 2 — KEYWORD VERIFICATION AND MATCHING (excerpt)

| Req ID | Keyword Check                                                          | Library Match | Match Type | Confidence | Adaptation Note                                                       |
|--------|------------------------------------------------------------------------|---------------|------------|------------|-----------------------------------------------------------------------|
| 2.7    | Check: "immutable" in any entry? No. "customer-controlled log"? No.    | ENTRY-SEC-003 | PARTIAL    | Medium     | Domain verified: entry covers audit logging capability but is silent  |
|        | ENTRY-SEC-003 covers audit logging via admin console only.             |               |            |            | on immutability and customer export — unaddressed portion is material |
| 4.3    | Check: "Bloomberg" in any entry? No. "BVAL" in any entry? No.         | NO MATCH      | NO MATCH   | N/A        | No library entry names Bloomberg or BVAL; REST API entry does not     |
|        |                                                                        |               |            |            | cover named financial data feed integration                           |
| 5.1    | Check: "WORM" in any entry? No. "17a-4" in any entry? No.             | NO MATCH      | NO MATCH   | N/A        | ENTRY-SEC-006 covers deletion (30/90 day retention) only; WORM,      |
|        | "immutable record retention" in any entry? No.                        |               |            |            | immutable retention, and 17a-4 configuration are absent               |

---

STEP 4 — GAP LIST (excerpt)

Gap 3: 4.3 — CRITICAL
Requirement: Describe your native or supported integration with Bloomberg data feeds (specifically BVAL pricing data).
Type: Integration
Why no match: No library entry mentions Bloomberg or BVAL; the requirement asks for a named financial data product integration that is absent from the content library.
Context flag: No context confirmation — assess capability status
Recommended owner: Engineering/Architecture
Recommended input source: Integration team — confirm whether Bloomberg BVAL API integration exists; if yes, retrieve documentation and flag for library refresh; if no, assess feasibility and timeline
Suggested deadline: 2026-06-11 (Critical — RFP due 2026-06-18; 5 business days prior)

Gap 4: 5.1 — CRITICAL
Requirement: Can your platform be configured to meet SEC Rule 17a-4 electronic records retention requirements (WORM storage, audit trail, non-erasure)?
Type: Compliance/Regulatory
Why no match: Library entry ENTRY-SEC-006 covers standard data deletion policy only; it does not address WORM storage, immutable record retention, or SEC 17a-4 configuration steps. Prospect Context confirms this is a mandatory requirement.
Context flag: N/A
Recommended owner: Legal/Compliance (regulatory obligation assessment) and Engineering/Architecture (WORM configuration feasibility)
Recommended input source: Legal team — assess SEC 17a-4 compliance posture; Engineering — assess WORM storage configuration support; Finance vertical SME if available
Suggested deadline: 2026-06-11 (Critical — mandatory per RFP preamble)

---

COORDINATOR SUMMARY (excerpt)

PROCESS CONSTRAINTS — HUMAN REVIEW REQUIRED:
  None identified.

Total requirements: 23
Ready for SE review (DIRECT + ADAPT drafted): 17 (74%)
Requires SME input: 6 (26%)
  - Engineering/Architecture: 2  |  Legal/Compliance: 2  |  Security Team: 1  |  Executive Sponsor: 1

Critical gaps: 4
  1. 4.3 (Bloomberg BVAL integration) — Engineering/Architecture — No context confirmation — Route by 2026-06-11
  2. 4.4 (Advent Geneva OMS integration) — Engineering/Architecture — No context confirmation — Route by 2026-06-11
  3. 5.1 (SEC Rule 17a-4 WORM storage) — Legal/Compliance + Engineering/Architecture — Route by 2026-06-11
  4. 5.2 (RIA vertical experience/references) — Executive Sponsor or Sales — Route by 2026-06-13
```

---

## Tips

1. **Always provide a Prospect Context block — even a brief one.** The skill uses it to distinguish "certification exists but isn't documented in our library yet" from "we don't have this capability." That distinction changes whether a gap routes to your Security Team to retrieve documentation or to Product Management to assess feasibility.

2. **Paste your content library with explicit entry IDs and last-updated dates.** The keyword verification step needs clear entry boundaries to determine whether a named entity appears in the library. If library entries are pasted as one undifferentiated block, the matching quality degrades. The last-updated date drives confidence scoring.

3. **Include the full cover page and preamble — not just the question list.** Submission constraints (attestation requirements, AI-content restrictions, portal submission mandates) appear there, not in the body. In regulated-sector deals (healthcare, financial services), missing a certification requirement on the cover page is a submission-rejection risk.

4. **Run the gap list owner assignments against your org's actual contacts before distributing.** The skill assigns gaps to routing buckets (Engineering/Architecture, Legal/Compliance, etc.) not named individuals. Map each bucket to a named owner and add them to the tracker before distributing to the review team.
