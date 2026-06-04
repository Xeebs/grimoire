# Deposition Contradiction Mapper

**Industry**: Legal
**Role**: Litigation Associate / Trial Paralegal
**Time saved**: 6–10 hours per deposition set

## What it does

Reads one or more deposition transcripts alongside any prior sworn statements (affidavits, interrogatory answers, prior testimony) and produces a structured contradiction brief: every identified inconsistency is classified by type (internal self-contradiction, cross-witness, or prior sworn statement deviation), supported by verbatim quote pairs with exact page/line citations, and ranked by cross-examination value so the litigator knows which impeachment points to lead with.

## When to use it

Use this skill when you have finished collecting depositions and are building cross-examination outlines. The trigger moment is: transcripts are in hand, trial or dispositive motion briefing is approaching, and an associate or paralegal needs to move from raw transcript to a prioritized impeachment kit. It is most powerful when multiple witnesses or prior sworn statements are in play, but it operates on single-witness depositions too.

## Prompt template

Paste the full prompt below into Claude (or any capable LLM) and replace the placeholder sections with your actual materials.

---

You are assisting a litigation associate preparing cross-examination materials. Your task is to analyze the deposition transcripts and any prior sworn statements provided below and produce a structured contradiction brief.

**Follow these steps in order:**

**Step 1 — Parse speaker attribution.**
Identify every named witness whose testimony appears in the materials. Delineate every block of testimony attributed to each witness. If any speaker attribution is ambiguous, flag it and do not use that testimony as a source for any finding.

**Step 2 — Build a factual claim map for each witness.**
Extract every specific, falsifiable factual assertion: dates, times, locations, sequences of events, identifications, statements about what someone said or did, and statements about the witness's own actions or knowledge. Exclude characterizations, opinions, legal conclusions, and emotional descriptions.

**Step 3 — Identify INTERNAL contradictions.**
Within a single witness's deposition, find pairs of factual assertions that cannot both be true simultaneously. Do not flag elaboration or greater specificity as contradiction.

**Step 4 — Identify CROSS-WITNESS contradictions.**
Find factual assertions by one witness that logically exclude factual assertions by another witness about the same specific observable event or fact.

**Step 5 — Compare against PRIOR SWORN STATEMENTS.**
For each witness, compare deposition testimony against any provided prior sworn statements (affidavits, declarations, interrogatory answers, prior deposition testimony). Flag every material inconsistency. Note the document type and date.

**Step 6 — Rank by cross-examination value.**
Assign each contradiction to one of three tiers:

- **Tier 1 — High value**: Direct, unambiguous contradiction on a material case fact; not susceptible to credible rehabilitation; usable for impeachment without opening the door to damaging redirect.
- **Tier 2 — Medium value**: Contradiction on a material fact but susceptible to plausible explanation; OR a direct contradiction on a collateral fact that undermines general credibility.
- **Tier 3 — Low value**: Contradiction on a peripheral fact; minor inconsistency within normal memory imprecision; or reconcilable with reasonable reading. Note for cumulative purposes only.

**Step 7 — Produce the contradiction brief.**
Use the output format below. Within each tier, order items from most to least directly linked to a key disputed issue.

---

**OUTPUT FORMAT:**

### CONTRADICTION BRIEF
**Case**: [case name]
**Witnesses analyzed**: [list]
**Prior sworn statements analyzed**: [list or "None provided"]
**Total contradictions found**: [N] (Tier 1: N | Tier 2: N | Tier 3: N)

---

### TIER 1 — HIGH CROSS-EXAMINATION VALUE
**[T1-N] [TYPE]: [Subject label]**
- **Type**: INTERNAL | CROSS-WITNESS | PRIOR SWORN
- **Witness(es)**: [Name(s)]
- **Subject**: [One clause]
- **Statement A**: "[Verbatim quote]" — [Citation]
- **Statement B**: "[Verbatim quote]" — [Citation or document]
- **Cross-examination note**: [One sentence on how to deploy]

### TIER 2 — MEDIUM CROSS-EXAMINATION VALUE
[Same format]

### TIER 3 — LOW CROSS-EXAMINATION VALUE
[Same format]

### NOTES AND CAVEATS
[Missing page/line numbers; ambiguous attributions; excluded near-contradictions]

---

**GUARDRAILS — the model must follow these without exception:**
- Quote testimony verbatim. Never paraphrase.
- Do not flag elaboration, greater specificity, or hedged language as contradiction.
- Do not attribute testimony from ambiguously labeled transcript sections.
- Distinguish factual contradictions from opinion/characterization differences — do not include the latter.
- If only one witness is analyzed, explicitly state "No cross-witness contradictions exist."
- Do not render credibility verdicts or use terms like "lied" or "perjury."
- If transcripts lack page/line numbers, flag this in Notes and use the best available positional reference.

---

**MATERIALS:**

### DEPOSITION TRANSCRIPTS

{DEPOSITION_TRANSCRIPTS}

*(Paste the full transcript text here. Label each transcript clearly: "DEPOSITION OF [WITNESS NAME], [DATE]". Include page:line numbers if available, e.g., "47:12 A: I was turning left.")*

---

### PRIOR SWORN STATEMENTS (optional)

{PRIOR_SWORN_STATEMENTS}

*(Paste any affidavits, interrogatory answers, or prior deposition excerpts here. Label each clearly: document type, witness name, and date. Example: "INTERROGATORY ANSWER NO. 4 — Sandra Okafor, signed 2024-11-02.")*

---

### CASE SUMMARY (optional)

{CASE_SUMMARY}

*(Provide 2–4 sentences describing the key disputed facts and legal theories at issue. This helps the model apply the materiality standard correctly when ranking contradictions.)*

## Example output

**CONTRADICTION BRIEF**
Case: Webb v. Hargrove (personal injury, vehicular)
Witnesses analyzed: Marcus Webb (defendant driver), Carol Finch (eyewitness pedestrian)
Prior sworn statements analyzed: Webb Police Statement (03/14/2024)
Total contradictions found: 3 (Tier 1: 1 | Tier 2: 1 | Tier 3: 1)

---

**TIER 1 — HIGH CROSS-EXAMINATION VALUE**

**[T1-1] PRIOR SWORN: Webb's phone use prior to collision**
- **Type**: PRIOR SWORN
- **Witness(es)**: Marcus Webb
- **Subject**: Whether Webb used his phone in the minutes before the collision
- **Statement A**: "I checked a map briefly, maybe five minutes before — just a quick glance." — Webb Dep. 93:4–6
- **Statement B**: "I had not used my phone in the ten minutes prior to the collision." — Webb Police Statement, 03/14/2024
- **Cross-examination note**: Confront Webb with his police statement before introducing the deposition admission to lock him into the prior denial, then read the deposition excerpt to establish the material inconsistency on distracted driving.

---

**TIER 2 — MEDIUM CROSS-EXAMINATION VALUE**

**[T2-1] INTERNAL: Webb's turning direction at point of collision**
- **Type**: INTERNAL
- **Witness(es)**: Marcus Webb
- **Subject**: Which direction Webb was turning when the collision occurred
- **Statement A**: "I was making a left turn onto Granger when I heard the impact." — Webb Dep. 47:12–14
- **Statement B**: "Looking at the diagram — yes, I was going right. Turning right onto Granger." — Webb Dep. 114:8–9
- **Cross-examination note**: Present the diagram used in the afternoon session first, confirm Webb's afternoon answer, then read the morning testimony to highlight the inconsistency — anticipate the defense explanation that the diagram changed Webb's spatial orientation.

## Tips

1. **Label transcripts clearly before pasting.** The model cannot distinguish witnesses from formatting alone in multi-witness depositions. A header like "DEPOSITION OF CAROL FINCH, May 6, 2025" at the top of each transcript block eliminates attribution errors.

2. **Include your case summary.** Even two sentences on the core disputed facts (e.g., "The central question is whether defendant was distracted by his phone and whether he had the right-of-way") sharpen the materiality ranking. Without it, the model applies a generic materiality standard and may place a Tier 1 fact in Tier 2.

3. **Use verbatim transcript text, not summaries.** The skill requires quoting the record directly. If you paste a summary of testimony rather than the actual Q&A transcript, the output will either paraphrase (violating the guardrail) or produce unreliable citations. Paste the real transcript, including Q: / A: formatting and page:line numbers.
