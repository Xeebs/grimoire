# Patent Office Action Response Drafter

**Industry**: Legal
**Role**: Patent Attorney / Patent Agent
**Time saved**: 6–12 hours per Office Action response (vs. 8–15 hours manual drafting)

## What it does

Given a USPTO Office Action and the pending claims, this skill inventories every rejection ground, performs a limitation-by-limitation gap analysis against each cited prior art reference, and drafts a complete Arguments/Remarks section organized by rejection type (35 U.S.C. §102 anticipation, §103 obviousness, §112 written description/enablement/definiteness) in USPTO prosecution brief format — ready for practitioner markup and filing authorization.

## When to use it

Invoke immediately after receiving a Non-Final or Final Office Action from the USPTO, before beginning the response drafting process. Provide the full Office Action text, the pending claims as currently numbered, and the text of the cited prior art references if available.

## Prompt template

```
You are assisting a patent attorney preparing a response to a USPTO Office Action. This is a first draft only — all arguments, claim amendments, and filing decisions require practitioner review and authorization before filing.

**APPLICATION INFORMATION**
Application Number: {APPLICATION_NUMBER}
Art Unit: {ART_UNIT}
Examiner: {EXAMINER_NAME}
Office Action Date: {OA_DATE}
Office Action Type: {NON-FINAL | FINAL}

**PENDING CLAIMS**
{PASTE FULL TEXT OF ALL PENDING CLAIMS — include claim numbers exactly as they appear in the application}

**OFFICE ACTION — EXAMINER'S REJECTIONS**
{PASTE THE FULL TEXT OF THE EXAMINER'S GROUNDS OF REJECTION SECTION — include all cited references, the examiner's argument text, and the claim-by-claim rejection breakdown}

**CITED PRIOR ART REFERENCES**
{PASTE OR SUMMARIZE THE RELEVANT PORTIONS OF EACH CITED REFERENCE — if you have the full reference, paste the sections the examiner cited; if you do not have the reference, note "Reference not available — draft placeholder arguments only"}

**OPTIONAL: PROSECUTION HISTORY NOTES**
{OPTIONAL: Paste any prior claim amendments, arguments, or examiner's reasons for allowance from earlier prosecution that are relevant to the current rejection — helps avoid repeating surrendered argument positions}

---

Using this information, perform the following:

1. Parse the Office Action header (application number, examiner, deadline, claim status inventory).

2. Inventory every ground of rejection with a summary table: rejection number, statutory basis (§102 / §103 / §112 subsection), claims affected, references cited, and a one-sentence summary of the examiner's argument.

3. For each §102 anticipation rejection:
   - Parse each rejected claim into its discrete limitations
   - Identify which limitations the examiner maps to the cited reference
   - Identify any limitation NOT clearly and explicitly disclosed in the reference (the argument hook)
   - Draft a full argument distinguishing the claim from the reference, citing exact claim language and reference text

4. For each §103 obviousness rejection:
   - Perform the same limitation mapping across the combination of references
   - Evaluate the examiner's motivation to combine: does it cite a specific teaching, suggestion, or motivation in the references, or does it rely on hindsight reconstruction?
   - Identify the strongest argument against combination (teaching away, destruction of functionality, conclusory rationale)
   - Flag any available secondary considerations for practitioner evaluation (commercial success, long-felt need, unexpected results)

5. For each §112 rejection:
   - Identify the specific sub-section (written description, enablement, or definiteness)
   - Locate the closest specification support for the challenged limitation
   - Apply the applicable legal standard (Ariad for written description, Wands factors for enablement, Nautilus for definiteness)
   - Draft a full argument and, if necessary, propose a targeted claim amendment with specification support cited

6. For any rejection where arguments alone cannot overcome the rejection, recommend specific claim amendments. Label every proposed amendment: "[PRACTITIONER AUTHORIZATION REQUIRED]" and identify the prosecution history estoppel consequence.

7. Draft the complete Response in USPTO Remarks format: one section per rejection type, each opening with the standard rejection header and closing with the standard withdrawal request.

8. Produce a Practitioner Review Checklist at the end listing: all proposed amendments requiring authorization, factual assertions requiring inventor verification, secondary considerations requiring evidence, claim construction positions creating estoppel, and any rejection where an examiner interview or continuation may be preferable to filing the drafted response.

Format the output as:
- DRAFT header with application number, examiner, deadline
- REJECTION INVENTORY (table)
- RESPONSE TO OFFICE ACTION (one section per rejection type, organized §102 → §103 → §112)
- CLAIM AMENDMENTS (with authorization flags)
- STATUS OF CLAIMS
- PRACTITIONER REVIEW CHECKLIST

Include this warning on the first page: "DRAFT — FOR ATTORNEY REVIEW AND AUTHORIZATION BEFORE FILING. This document does not constitute legal advice."
```

## Example output

The following excerpt shows the argument structure for a single §103 rejection:

---

**DRAFT — FOR ATTORNEY REVIEW AND AUTHORIZATION BEFORE FILING**
Application No.: 17/234,891 | Examiner: J. Smith, Art Unit 2153 | Response Deadline: March 15, 2026

---

**REJECTION INVENTORY**

| # | Statutory Basis | Claims Affected | References | Examiner's Argument |
|---|---|---|---|---|
| 1 | 35 U.S.C. §103 | 1–5, 10 | Smith (US 10,123,456) in view of Jones (US 2019/0123456) | Claim 1 limitation "dynamically adjusting threshold based on historical access patterns" is obvious over Smith's static threshold combined with Jones's historical-log processing module |

---

**RESPONSE TO §103 REJECTION**

**Rejection 1: Claims 1–5 and 10 Rejected Under 35 U.S.C. §103 as Obvious Over Smith in View of Jones**

Applicant respectfully traverses this rejection. The Examiner proposes combining Smith's static threshold module with Jones's historical-log processing module to arrive at the claimed "dynamically adjusting threshold based on historical access patterns." This combination is improper for at least two independent reasons.

**First, Smith teaches away from the proposed combination.** Smith explicitly discloses that its threshold is "fixed at system initialization and not modified during operation" (Smith, col. 8, ll. 32–34) and further states that "dynamic threshold modification would introduce unacceptable latency in high-frequency access environments" (Smith, col. 9, ll. 1–4). A reference teaches away from a combination when it specifically criticizes or discourages the modification proposed by the examiner. *In re Gurley*, 27 F.3d 551, 553 (Fed. Cir. 1994). Smith's explicit warning against dynamic modification is a direct teaching away from incorporating Jones's dynamic log-processing approach.

**Second, the Examiner's motivation to combine is conclusory and relies on hindsight.** The Office Action states only that it "would have been obvious to one of ordinary skill to incorporate well-known dynamic adjustment techniques to improve system performance." This rationale does not identify any specific teaching, suggestion, or motivation within Smith or Jones for making the proposed combination, nor does it articulate why a PHOSITA would have selected Jones's specific historical-log module over other available approaches. Such a conclusory rationale is insufficient under *KSR Int'l Co. v. Teleflex Inc.*, 550 U.S. 398, 418 (2007) and MPEP § 2142, which require that the examiner "articulate the reasoning with some rational underpinning."

**Limitation mapping confirms no reference discloses "dynamically adjusting threshold."** The claimed limitation recites "dynamically adjusting the access threshold value based on historical access patterns stored in a pattern database, wherein the adjusting occurs at each access event." Smith discloses only static thresholds set at initialization (Smith, col. 8, ll. 28–40). Jones discloses processing historical access logs to generate periodic reports (Jones, ¶¶ [0045]–[0052]) but does not disclose using those logs to adjust any threshold value, let alone adjusting at each access event. Neither reference, alone or in combination, discloses this limitation.

Accordingly, Applicant respectfully requests that the rejection of claims 1–5 and 10 under 35 U.S.C. §103 be withdrawn.

---

**PRACTITIONER REVIEW CHECKLIST**

1. [CLAIM AMENDMENT — NONE PROPOSED: Arguments only. If arguments are not persuasive, consider narrowing "each access event" to "each unauthorized access event" — written description support at col. 12, ll. 3–8. REQUIRES AUTHORIZATION before any amendment is filed.]
2. [FACTUAL ASSERTION: The teaching-away argument relies on the specific Smith passages cited above. Confirm with inventor that no other prior art or internal documentation suggests dynamic adjustment was a known design choice in this field.]
3. [SECONDARY CONSIDERATIONS: If the product embodying this invention has achieved commercial success or was recognized by industry awards, that evidence could further support non-obviousness. Evidence must be submitted with a declaration under 37 C.F.R. § 1.132.]
4. [CLAIM CONSTRUCTION: By arguing that "dynamically adjusting" requires adjustment "at each access event," Applicant is taking a claim construction position that narrows the term. This creates prosecution history estoppel that may limit the doctrine of equivalents.]
5. [RESPONSE DEADLINE: Verify response deadline against actual mailing date on PAIR/Patent Center — deadline calculated as 3 months from mailing date.]

---

## Tips

1. **Provide the full cited reference text when possible.** The skill produces significantly stronger §103 teaching-away arguments when it can quote the reference's own language rather than relying on the examiner's characterization. Even pasting the 2–3 most relevant columns is sufficient.

2. **Include prior prosecution history if available.** If claims were previously amended or arguments were previously made, paste those excerpts. This prevents the draft from taking positions that are barred by prior prosecution history estoppel and alerts you to surrendered argument territory.

3. **Treat the Practitioner Review Checklist as your filing checklist.** Every item on it represents a decision or verification that must happen before the response leaves your desk. The checklist is designed so you can work through it top-to-bottom as your final pre-filing review.
