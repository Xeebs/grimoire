# Scenario 2: Employment Litigation — Wrongful Termination Claim

## Context

You are a discovery associate at Crane Seligman LLP, representing Northfield Logistics Group ("Northfield") in a wrongful termination lawsuit filed by former regional sales manager Derek Hollis. Hollis filed suit on January 9, 2025, claiming his termination was pretextual and retaliatory. Northfield's HR and operations leadership generated a series of documents in the months before and after the termination. Two documents have been flagged as potentially privileged by the review platform. You must determine whether privilege applies and generate log entries accordingly.

**Known attorneys in this matter:**
- Patricia Okafor, Esq. | Partner, Outside Employment Counsel | Crane Seligman LLP
- Michael Torres, Esq. | Associate, Outside Employment Counsel | Crane Seligman LLP
- (No in-house counsel at Northfield — the company has no legal department)

**Litigation context:** Derek Hollis filed a wrongful termination and retaliation complaint in the Northern District of Illinois on January 9, 2025 (Case No. 25-cv-0312). Northfield terminated Hollis on November 18, 2024. No demand letter or pre-suit claim was received before the termination. Northfield first engaged outside counsel (Crane Seligman) on December 3, 2024, after receiving a litigation hold letter from Hollis's attorney dated November 27, 2024.

---

## Input

DOCUMENT 1
Bates Range: NLG-0044 – NLG-0044
Metadata: Date: 2024-10-31; Custodian: Sandra Park (HR Director); Document type: Email

Content:
From: Sandra Park <s.park@northfieldlogistics.com>
To: Kevin Marsh <k.marsh@northfieldlogistics.com>
Date: October 31, 2024, 3:22 PM
Subject: Derek Hollis — performance concerns and next steps

Kevin,

Following up on our conversation this morning. I wanted to put in writing where things stand with Derek. His Q3 numbers came in at 61% of target — third consecutive underperforming quarter. Beyond the numbers, we've had two customer complaints escalated to me directly in the past month, and his manager (Brad Simmons) has flagged ongoing issues with team communication.

I think we need to move toward a separation. From a process standpoint, I'd recommend we document the performance issues formally before we take any action — a written PIP or a documented counseling session. That gives us a clean record if this gets challenged down the road.

One more thing: I'd like to see what legal thinks about the timing and approach before we pull the trigger. But based on what I've seen, I think we're well within our rights here.

Sandra

---

DOCUMENT 2
Bates Range: NLG-0117 – NLG-0124
Metadata: Date: 2024-12-10; Custodian: Sandra Park (HR Director); Document type: Email with attachment

Content:
[Email body]
From: Patricia Okafor <p.okafor@craneseligman.com>
To: Sandra Park <s.park@northfieldlogistics.com>
CC: Michael Torres <m.torres@craneseligman.com>
Date: December 10, 2024, 5:45 PM
Subject: RE: Hollis matter — draft termination letter for your review

Sandra,

Please find attached a draft termination letter for Derek Hollis. I want to flag a few things:

First, I've drafted the letter to focus exclusively on performance — I've intentionally excluded any reference to the customer complaints because invoking those in a termination letter could open the door to a retaliation argument if Hollis claims the complaints were in fact his attempts to report something. Given the litigation hold letter we received, we need to be careful.

Second, the letter should NOT reference the PIP that was contemplated in October — the fact that no PIP was actually issued weakens our position if we now claim progressive discipline was followed.

Please review, discuss with Kevin, and get back to me with any changes before we finalize. Do not circulate this draft outside of HR and legal.

Patricia

[Attachment: NLG-0118 – NLG-0124]
File name: Hollis_TerminationLetter_DRAFT_v1_PRIVILEGED.docx

[Attachment content — draft letter]
[On Crane Seligman LLP letterhead — "DRAFT — PRIVILEGED AND CONFIDENTIAL"]

December [__], 2024

Derek Hollis
[Address]

Re: Separation of Employment

Dear Mr. Hollis:

This letter confirms that your employment with Northfield Logistics Group is terminated, effective [DATE], due to sustained failure to meet established performance targets over three consecutive quarters despite having had the opportunity to demonstrate improvement.

[Remaining letter text omitted — contains counsel's draft language and strategic framing for the termination communication]

---

## Expected Output Criteria

- [ ] Document 1 is NOT asserted as privileged. The skill must log it as `NONE — FLAG FOR REVIEW` with a specific explanation: no attorney is on the communication, no attorney-client relationship exists as of October 31 (outside counsel was not engaged until December 3), and the phrase "see what legal thinks" alone does not establish ACP or WPD.
- [ ] Document 1's Notes field explicitly states that WPD does not apply: there is no indication litigation was reasonably anticipated at the time of writing (October 31, 2024), which predates the litigation hold letter (November 27, 2024) and outside counsel engagement (December 3, 2024) by at least 27 days. The termination decision had not yet been made.
- [ ] Document 1's Notes field explicitly states that the phrase "see what legal thinks" is not sufficient to establish privilege — it indicates an intent to seek legal advice but is not itself a privileged communication, and no attorney received or was part of this email.
- [ ] Document 1's Confidence tier is not used to assert privilege — NONE — FLAG FOR REVIEW is the correct Privilege_Basis entry, and the Notes field explains the basis for the non-privilege determination clearly enough that a supervising attorney can confirm without re-reading the full document.
- [ ] Document 2 is classified with dual basis: ACP for the email body (Patricia Okafor's advice to Sandra Park) and WPD for the attached draft termination letter (NLG-0118 – NLG-0124).
- [ ] Document 2's Privilege_Basis entry in the pipe-delimited output is `ACP; WPD` and the Notes field distinguishes which basis applies to which component: ACP for the email body (outside counsel providing legal advice regarding termination approach and litigation risk); WPD for the draft attachment (prepared by outside counsel in anticipation of litigation following the November 27 litigation hold letter).
- [ ] Document 2's Subject_Description does NOT reveal: (a) that Okafor advised excluding the customer complaints, (b) that the absence of a PIP weakens the company's position, (c) that Okafor flagged a retaliation argument risk, or (d) the specific strategic framing of the termination letter. The description characterizes the communication as providing legal advice regarding the termination approach and the draft as prepared in anticipation of litigation — without revealing the substance.
- [ ] Document 2's Confidence tier is CLEAR for both the email body and the attachment, given that all elements are satisfied: outside counsel is confirmed, the litigation hold letter establishes litigation anticipation as of November 27, and the document is within the attorney-client privilege group (Park is the client contact, Torres is copied as co-counsel).
- [ ] Document 2's Bates range in the pipe-delimited output correctly reflects the full document range including the attachment (NLG-0117 through NLG-0124), with Notes indicating the email body is NLG-0117 and the attachment is NLG-0118 – NLG-0124.
- [ ] The pipe-delimited output has a header row and two data rows, correctly formatted with all 12 columns.
- [ ] The Processing Summary identifies Document 1 as a document where privilege was not asserted, lists it with its Bates number and reason, and flags it for attorney attention.
- [ ] No entry for Document 2 reveals the content of Okafor's legal advice or the strategic drafting decisions reflected in the termination letter.

## What failure looks like

- Asserting ACP or WPD for Document 1 on the basis of the "see what legal thinks" comment — this is a significant doctrinal error and the exact failure mode the skill is designed to prevent
- Claiming WPD for Document 1 based on Park's forward-looking comment about anticipating a challenge "down the road" — this is insufficient to establish litigation anticipation; the skill must apply the more rigorous standard (specific, identifiable litigation trigger)
- Classifying Document 2 as ACP-only, failing to recognize that the attached draft is independently protected as WPD
- Describing Document 2 in a way that reveals Okafor's advice about excluding customer complaints, the PIP weakness, or the retaliation argument risk — all of these are privileged substance and their disclosure in a log description would constitute partial waiver
- Treating the attachment (NLG-0118 – NLG-0124) and the email body (NLG-0117) as a single undifferentiated entry without noting the dual-basis breakdown between the two components
- Assigning BORDERLINE to Document 2 when all elements are clearly satisfied — misidentifying a clear privilege claim as borderline creates unnecessary attorney work and signals doctrinal uncertainty that does not exist here
- Producing a Processing Summary that lists Document 1 as privileged or omits it from the non-asserted-privilege list
