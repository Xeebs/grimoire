# Scenario 1: Corporate Antitrust Investigation — Three-Document Privilege Review

## Context

You are a discovery associate at Whitmore & Reid LLP, outside litigation counsel for Acme Industrial Holdings, Inc. ("Acme"). The DOJ's Antitrust Division issued a Civil Investigative Demand to Acme on March 15, 2024, concerning alleged price coordination in the industrial fastener market. Acme is required to produce a privilege log to the DOJ within 45 days.

You are reviewing a batch of three documents from Acme's custodian export. The review platform has flagged all three as potentially privileged. Your task is to generate privilege log entries for all three. The supervising partner has provided the following attorney list for the matter.

**Known attorneys in this matter:**
- Margaret Voss, Esq. | General Counsel | Acme Industrial Holdings, Inc. (in-house)
- David Lim, Esq. | Deputy General Counsel | Acme Industrial Holdings, Inc. (in-house)
- Rachel Patel, Esq. | Partner, Outside Counsel | Latham & Watkins LLP
- Evan Moore, Esq. | Associate, Outside Counsel | Latham & Watkins LLP

**Litigation context:** DOJ Civil Investigative Demand issued 2024-03-15. Investigation into alleged price coordination among industrial fastener manufacturers. Acme is a subject of the investigation, not a target. A prior internal compliance review flagged potential exposure in 2023.

---

## Input

DOCUMENT 1
Bates Range: ACME-0001 – ACME-0001
Metadata: Date: 2024-03-22; Custodian: James Harlow (CEO); Document type: Email

Content:
From: James Harlow <j.harlow@acmeindustrial.com>
To: Margaret Voss <m.voss@acmeindustrial.com>
Date: March 22, 2024, 9:14 AM
Subject: Antitrust exposure re: February pricing meeting

Margaret,

Now that we've received the DOJ subpoena, I need to understand where we stand legally. At the February 14th pricing strategy meeting, we had representatives from three competitors present — it was framed as an "industry roundtable," but I'm concerned that what was discussed may have crossed a line. Can you tell me what our legal exposure actually is? And what documentation from that meeting should we be preserving right now?

Jim

---

DOCUMENT 2
Bates Range: ACME-0002 – ACME-0005
Metadata: Date: 2024-03-19 (most recent message); Custodian: James Harlow (CEO); Document type: Email chain

Content:
[Message 1 — oldest]
From: James Harlow <j.harlow@acmeindustrial.com>
To: Robert Finch <r.finch@acmeindustrial.com>
CC: Linda Chow <l.chow@acmeindustrial.com>
Date: March 12, 2024, 2:30 PM
Subject: Q2 Pricing Strategy

Robert, Linda —

Following up on our conversation last week. We need to lock in the Q2 price sheet by March 20. I've attached the draft. My recommendation is to hold the 7% increase on fastener categories 3–7 and defer category 8. Let me know if you agree so we can move to finalization.

Jim

---

[Message 2]
From: Robert Finch <r.finch@acmeindustrial.com>
To: James Harlow <j.harlow@acmeindustrial.com>
CC: Linda Chow <l.chow@acmeindustrial.com>
Date: March 13, 2024, 11:05 AM
Subject: RE: Q2 Pricing Strategy

Jim —

Agreed on categories 3–7. On category 8, I'd push back — the margin squeeze there is real. Can we revisit at 2pm Thursday? I also want to make sure we're aligning on how we communicate the increase to distributors.

Robert

---

[Message 3 — most recent]
From: Margaret Voss <m.voss@acmeindustrial.com>
To: James Harlow <j.harlow@acmeindustrial.com>; Robert Finch <r.finch@acmeindustrial.com>
CC: Linda Chow <l.chow@acmeindustrial.com>
Date: March 19, 2024, 4:47 PM
Subject: RE: Q2 Pricing Strategy

Jim, Robert —

I've been looped in on this thread. From a legal standpoint, I want to flag something important before we finalize anything. Given the DOJ inquiry we received on March 15th, we need to be careful about how we document pricing decisions going forward. I strongly recommend we pause this process and get on a call with Rachel Patel at Latham before we finalize the Q2 price sheet. I can set that up for tomorrow morning.

Margaret

---

DOCUMENT 3
Bates Range: ACME-0006 – ACME-0012
Metadata: Date: 2024-04-08; Custodian: Margaret Voss (GC); Document type: Memorandum

Content:
LATHAM & WATKINS LLP
PRIVILEGED AND CONFIDENTIAL
ATTORNEY-CLIENT COMMUNICATION — WORK PRODUCT

MEMORANDUM

TO: Margaret Voss, Esq., General Counsel, Acme Industrial Holdings, Inc.
    David Lim, Esq., Deputy General Counsel, Acme Industrial Holdings, Inc.
FROM: Rachel Patel, Esq.; Evan Moore, Esq. — Latham & Watkins LLP
DATE: April 8, 2024
RE: Preliminary Litigation Assessment — DOJ Civil Investigative Demand (Acme Industrial Holdings)

I. EXECUTIVE SUMMARY

This memorandum sets forth our preliminary assessment of Acme's legal exposure arising from the DOJ Civil Investigative Demand issued March 15, 2024, and our recommended litigation posture for the investigative phase. This memorandum reflects our mental impressions, legal analysis, and strategic recommendations and is protected as attorney work product.

II. FACTUAL SUMMARY

[Body text omitted — contains counsel's factual analysis and legal strategy]

III. LEGAL ANALYSIS

[Body text omitted — contains counsel's legal analysis and conclusions]

IV. RECOMMENDED LITIGATION POSTURE

[Body text omitted — contains counsel's strategic recommendations]

---

## Expected Output Criteria

- [ ] Document 1 is classified as ACP with Confidence: CLEAR. The description characterizes it as seeking legal advice regarding antitrust compliance or legal exposure, without quoting or paraphrasing Harlow's specific questions. All four ACP elements are identified as satisfied.
- [ ] Document 1's Subject_Description does not reveal that competitors were present at the February meeting or that Harlow is worried about having "crossed a line" — these are privileged substance.
- [ ] Document 2 is analyzed as an email chain, not as a single document. The output distinguishes: Messages 1 and 2 (Harlow-Finch-Chow exchange) are identified as NOT privileged — no attorney involved, no legal advice, pure business communication. Message 3 (Voss reply) is identified as ACP-eligible for that message only.
- [ ] Document 2's Confidence tier is REVIEW (not CLEAR), because privilege applies only to a portion of the chain, and the log entry must specify that Messages 1 and 2 are not covered — this requires attorney review to ensure proper redaction and scoping before the log is served.
- [ ] Document 2's Notes field explicitly states that Messages 1 and 2 predating GC involvement are not privileged and should not be logged as privileged without redaction of the prior thread, or separate production.
- [ ] Document 3 is classified as WPD (and optionally ACP; WPD dual basis) with Confidence: CLEAR. The description references the DOJ CID as the litigation trigger and characterizes the memo as reflecting attorney mental impressions, legal analysis, and litigation strategy — without revealing specific conclusions or recommendations.
- [ ] The pipe-delimited output is correctly formatted with all 12 columns in the specified order, a header row, and one data row per document.
- [ ] The human-readable output uses the labeled-list format with all 11 fields populated.
- [ ] A Processing Summary appears at the end listing document counts, confidence tier breakdown, and attorney-attention items.
- [ ] No entry reveals the substance of any privileged communication — the descriptions satisfy the FRCP Rule 26(b)(5) specificity test without disclosing protected content.

## What failure looks like

- Treating all three messages in Document 2's email chain as uniformly privileged without distinguishing the pre-GC messages from Voss's reply — this is a critical doctrinal error and represents the most common failure mode on chain documents
- Classifying Document 2 as CLEAR rather than REVIEW — the partial-chain privilege issue requires attorney judgment before the log is served
- Describing Document 1 in a way that mentions competitors at the pricing meeting, the "crossed a line" concern, or the specific documents Harlow asked about — these are privileged substance
- Classifying Document 3 as ACP only, ignoring WPD, when the document's header and content clearly indicate it was prepared in anticipation of litigation
- Missing the DOJ CID (March 15) as the WPD triggering event for Document 3
- Producing pipe-delimited output with fewer than 12 columns, wrong column order, or no header row
- Processing Summary absent or incomplete
