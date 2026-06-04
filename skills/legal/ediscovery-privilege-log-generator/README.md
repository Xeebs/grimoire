# E-Discovery Privilege Log Generator

**Industry**: Legal
**Role**: Litigation Paralegal / Discovery Associate
**Time saved**: ~4–6 minutes per document (40–60% of manual review time on routine entries)

---

## What it does

Generates FRCP Rule 26(b)(5)-compliant privilege log entries from flagged e-discovery documents. For each document, it applies the four-element attorney-client privilege test and the two-element work product doctrine test, drafts a court-ready subject description, assigns a confidence tier for attorney review prioritization, and outputs a pipe-delimited row importable into Relativity, Everlaw, or similar review platforms.

## When to use it

Invoke this skill when you have one or more documents flagged as potentially privileged in your e-discovery review queue and need to produce log entries that:

- Identify and distinguish attorney-client privilege (ACP) from work product doctrine (WPD)
- Survive opposing counsel scrutiny under FRCP Rule 26(b)(5)(A)
- Are formatted for direct import into your review platform
- Flag borderline entries so attorneys can prioritize their review time

Do NOT use this skill on documents that have already been reviewed and logged by supervising counsel without their knowledge. The output is a draft for attorney review and sign-off — it does not replace attorney judgment on privilege determinations.

---

## Prompt template

Copy the full prompt below. Replace all `{PLACEHOLDER}` values with your actual document data before submitting.

---

You are assisting a litigation paralegal generating a privilege log for an e-discovery production. Apply FRCP Rule 26(b)(5) standards throughout. For each document provided, produce a complete privilege log entry following all steps below.

**Known attorneys in this matter** (use this list to identify attorney authors and recipients):
{ATTORNEY_LIST}
Format: Name | Role | Affiliation (e.g., "Sarah Chen | Outside Counsel | Morrison & Foerster LLP")
If this list is not available, work from document content alone and flag any uncertain attorney identifications.

**Litigation context** (use to assess work product doctrine triggering event):
{LITIGATION_CONTEXT}
Example: "DOJ antitrust subpoena issued 2024-03-15. Government investigation into pricing practices in the industrial fastener market."

**Documents to process**:
{DOCUMENT_BLOCK}
Provide each document as:

DOCUMENT [N]
Bates Range: [begin] – [end]
Metadata: [any available metadata from your review platform: date, document type, custodian, etc.]
Content:
[Full text of the document, including all headers, addressees, and body text. For email chains, include the full chain in chronological order with each message clearly delimited.]

---

**STEP 1 — Parse Metadata**
For each document, extract: Bates range, date (YYYY-MM-DD or UNDATED), document type (Email / Email Chain / Memorandum / Letter / Draft / Attachment / Spreadsheet / Presentation / Handwritten Note / Other), all authors, all recipients (To / CC / BCC), and subject line or title.

**STEP 2 — Identify Attorneys**
For every person named in the document, determine attorney status using these indicators (in order of reliability): "Esq." or "J.D." suffix; law firm email domain; title of General Counsel / Deputy GC / Associate GC / Chief Legal Officer / Legal Counsel / Attorney / Lawyer; in-house legal department affiliation; or context showing legal advisory role. Mark any person whose attorney status cannot be confirmed as "Attorney Status Unknown." Do not assume attorney status. Note when an attorney appears to be acting in a business rather than legal capacity.

**STEP 3 — Classify Privilege Basis**
Apply the following tests independently:

Attorney-Client Privilege (ACP) — all four elements required:
(1) Attorney-client relationship: at least one confirmed attorney communicating with their client
(2) Legal advice purpose: primary purpose is seeking or providing legal advice, not business direction
(3) Confidentiality: communication was made in confidence, not shared with unrelated third parties
(4) No waiver: privilege has not been waived by voluntary disclosure to adverse or unrelated third parties

Work Product Doctrine (WPD) — both elements required:
(1) Anticipation of litigation: document prepared when litigation was reasonably foreseeable (subpoena, demand letter, identified claim, or regulatory investigation are common triggers — note the specific trigger)
(2) Prepared by or for a party or representative: attorney, consultant, agent, or insurer — does not require attorney-client communication

If both apply, designate dual basis (ACP; WPD) and explain each basis separately in the Notes field.
If a document was shared under a joint defense or common interest agreement, note this as an extension of ACP or WPD.
If neither doctrine applies, do NOT assert privilege — log as NONE — FLAG FOR REVIEW with a specific explanation.

**STEP 4 — Draft Privilege Log Description**
Write one to two sentences that:
- Characterize the nature and purpose of the communication at a general level
- Identify the legal matter or subject area (not the specific advice or strategy)
- Use standard log phrasing: "seeking legal advice regarding," "providing legal advice concerning," "reflecting attorney mental impressions regarding," "prepared in anticipation of litigation arising from"
- Do NOT quote or paraphrase the privileged content
- Do NOT reveal specific legal advice, conclusions, vulnerabilities, or strategy
- Are specific enough to satisfy FRCP Rule 26(b)(5)(A) — vague boilerplate ("legal advice") fails the specificity test

**STEP 5 — Assign Confidence Tier**
- CLEAR: All privilege elements unambiguously satisfied, attorney status confirmed for all relevant parties, no identified waiver risk
- REVIEW: One or more elements uncertain; requires attorney confirmation before log is served (document the specific uncertainty in Notes)
- BORDERLINE: Significant doubt about privilege; attorney must make an affirmative judgment call (document the specific risk in Notes)

**STEP 6 — Format Output**

Produce both of the following for every document:

FORMAT A — Pipe-delimited (Relativity/Everlaw import-ready):
One row per document. Output a header row first, then one data row per document.
Columns: Bates_Begin|Bates_End|Date|Document_Type|Author|Recipients|Attorney_Authors|Attorney_Recipients|Privilege_Basis|Subject_Description|Confidence|Notes
Rules: Separate multiple values within a field with semicolons. Enclose any field containing a pipe character in double quotes. Enclose the Notes field in double quotes.

FORMAT B — Human-readable (for attorney review and sign-off):
Labeled list format, one label per line, as shown:
Bates Range:      [begin] – [end]
Date:             [date]
Document Type:    [type]
Author:           [author]
Recipients:       [To / CC / BCC parties]
Attorney Authors: [confirmed attorney authors or "None confirmed"]
Atty Recipients:  [confirmed attorney recipients or "None confirmed"]
Privilege Basis:  [ACP / WPD / ACP; WPD / NONE — FLAG FOR REVIEW]
Description:      [one to two sentence log description]
Confidence:       [CLEAR / REVIEW / BORDERLINE]
Notes:            [explanation of confidence tier, waiver risks, email chain scope, dual-basis explanation, or other attorney-attention items]

After all individual entries, output a Processing Summary:
- Total documents processed
- Count by confidence tier (CLEAR / REVIEW / BORDERLINE)
- Count of entries where privilege was NOT asserted (list Bates numbers)
- List of documents requiring attorney attention before log can be served, with reason

**Critical constraints**:
- Never assert privilege where the elements are clearly not met
- Never reveal privileged substance in the log description
- Flag every uncertain attorney identification explicitly
- Add a waiver-risk note for any document with non-attorney third-party recipients whose relationship to the privilege group is unclear
- For email chains, analyze each message separately; specify in Notes which messages in the chain are covered by the privilege assertion

{DOCUMENT_BLOCK}

---

## Example output (pipe-delimited)

```
Bates_Begin|Bates_End|Date|Document_Type|Author|Recipients|Attorney_Authors|Attorney_Recipients|Privilege_Basis|Subject_Description|Confidence|Notes
ACME-001|ACME-003|2024-04-02|Email|James Harlow (CEO)|Margaret Voss, Esq. (GC)|None confirmed|Margaret Voss, Esq. (GC — In-House)|ACP|Email communication from corporate executive to in-house General Counsel seeking legal advice regarding antitrust compliance obligations arising from an internal pricing meeting.|CLEAR|All four ACP elements satisfied. Communication is solely between client executive and in-house GC. No third-party recipients. GC acting in legal advisory capacity confirmed by subject matter and title.
ACME-004|ACME-007|2024-04-10|Memorandum|R. Patel, Esq. (outside counsel — Latham & Watkins)|M. Voss, Esq. (GC); Legal Department|R. Patel, Esq.|M. Voss, Esq.|WPD|Attorney memorandum reflecting outside litigation counsel's mental impressions, case assessment, and preliminary litigation strategy prepared in anticipation of DOJ antitrust investigation following subpoena issued 2024-03-15.|CLEAR|WPD elements satisfied: prepared by outside counsel in anticipation of litigation (DOJ subpoena is triggering event); contains attorney mental impressions and strategy. ACP also considered but not separately logged because document flows attorney-to-attorney within the privilege group. WPD designation is sufficient and broader.
```

---

## Example output (human-readable)

```
--- DOCUMENT 1 ---
Bates Range:      ACME-001 – ACME-003
Date:             2024-04-02
Document Type:    Email
Author:           James Harlow (CEO, Acme Corp.)
Recipients:       To: Margaret Voss, Esq. (General Counsel, Acme Corp.)
Attorney Authors: None confirmed (Harlow is client, not attorney)
Atty Recipients:  Margaret Voss, Esq. — General Counsel, Acme Corp. (in-house; confirmed by title and department)
Privilege Basis:  ACP
Description:      Email communication from corporate executive to in-house General Counsel seeking legal advice regarding antitrust compliance obligations arising from an internal pricing meeting.
Confidence:       CLEAR
Notes:            All four ACP elements satisfied. Sole recipient is in-house GC acting in legal advisory capacity. Subject matter is legal compliance advice, not operational business direction. No non-attorney recipients. No waiver risk identified.

--- DOCUMENT 2 ---
Bates Range:      ACME-004 – ACME-007
Date:             2024-04-10
Document Type:    Memorandum
Author:           R. Patel, Esq. (Outside Counsel, Latham & Watkins LLP)
Recipients:       To: M. Voss, Esq. (GC, Acme Corp.); Legal Department, Acme Corp.
Attorney Authors: R. Patel, Esq. (Outside Counsel — Latham & Watkins LLP)
Atty Recipients:  M. Voss, Esq. (In-House GC, Acme Corp.)
Privilege Basis:  WPD
Description:      Attorney memorandum reflecting outside litigation counsel's mental impressions, case assessment, and preliminary litigation strategy prepared in anticipation of DOJ antitrust investigation following subpoena issued 2024-03-15.
Confidence:       CLEAR
Notes:            WPD elements satisfied. Litigation trigger: DOJ subpoena dated 2024-03-15, predating memo by 26 days. Document contains attorney mental impressions and litigation strategy — core WPD. "Legal Department" as a recipient is within the privilege group (in-house legal). No non-attorney third-party recipients. No waiver risk identified.
```

---

## Tips

1. **Always supply the attorney list.** The `{ATTORNEY_LIST}` placeholder is the most important input for accuracy. Pull the full list of attorneys from your matter's contact sheet or the firm's case management system before running the prompt. The skill can infer attorney status from document content alone, but explicit confirmation eliminates REVIEW-tier entries caused by uncertain attorney identification.

2. **Feed email chains as complete threads.** Paste the entire email chain in chronological order — do not extract only the privileged reply. The skill needs the full chain context to determine which messages in a thread are covered by privilege and which are not. Submitting only the privileged reply causes the skill to miss the analysis of the earlier non-privileged thread.

3. **Run BORDERLINE and REVIEW entries past a supervising attorney before finalizing the log.** The skill is designed so that CLEAR entries require only QC review; REVIEW and BORDERLINE entries require substantive attorney judgment. Sorting the output by the Confidence column before importing into Relativity or Everlaw lets you route documents efficiently: CLEAR entries to the QC queue, REVIEW and BORDERLINE entries to the attorney review queue.
