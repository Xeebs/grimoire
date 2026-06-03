# Grimoire — AI Skills Lab

## Mission
Continuously research, design, test, and publish high-quality AI skills for the modern information-economy workforce. Target industries: **Finance & Banking**, **Legal**, **Consulting & Knowledge Work**.

Grimoire publishes to GitHub: `Xeebs/grimoire`

---

## Autonomous Heartbeat Protocol

This project runs on an **hourly heartbeat**. On every cycle, check `pipeline/state.json` first and resume from the recorded phase:

### Phase 1 — Resume Check
Read `pipeline/state.json`. Identify `current_phase` and `active_skill`. If a skill is mid-flight, continue it from where it left off. If the previous cycle completed cleanly, start at Phase 2.

### Phase 2 — Feedback Check
Check `Xeebs/grimoire` GitHub Issues and Discussions for new activity. Log actionable feedback as new signals in `pipeline/queue.md` with `type: FEEDBACK`. Respond to any open issues with status updates.

### Phase 3 — Research
Invoke the `grimoire-research` skill. Scan configured sources for signals on AI workflow gaps in Finance, Legal, and Consulting. Append findings to `pipeline/queue.md`. Target 3–5 new signals per cycle. Skip duplicates.

### Phase 4 — Ideate & Design
Select the highest-strength unworked signal from `pipeline/queue.md`. Invoke `grimoire-ideate` to design the skill. Write output into `skills/{industry}/{skill-name}/`. Mark the signal `status: DESIGNING`.

### Phase 5 — Test
Write 2+ realistic test scenarios in `skills/{industry}/{skill-name}/tests/`. Run each scenario and verify output meets the pre-defined criteria. On failure, iterate on the skill (max 3 attempts). Mark signal `status: TESTING`.

### Phase 6 — Publish
If all tests pass, run `/project:deploy`. Push skill to `Xeebs/grimoire`, create a GitHub Discussion announcement, send a push notification, and log to `pipeline/published.md`. Mark signal `status: PUBLISHED`.

### Cycle Limit
Complete at most **1 full skill per cycle** to protect usage limits. If rate-limited mid-cycle, write current state to `pipeline/state.json` and exit — the next heartbeat will resume.

---

## Quality Bar — Non-Negotiable

A skill must meet **all** of the following before it is published:

1. **Novel** — Not a basic prompt easily found in public libraries. If 3+ similar skills exist publicly, this one must offer a clear, demonstrable improvement.
2. **Specific** — Targets a named workflow step and named role, not broad tasks like "summarize a document."
3. **Industry-grounded** — Uses correct terminology, document types, and role titles from the target industry.
4. **Tested** — Passes at least 2 realistic scenario tests with pre-defined expected output criteria.
5. **Dual-format** — Ships both `SKILL.md` (Claude Code format) and `README.md` (portable prompt template).

If a skill fails the quality bar after 3 design attempts, mark it `status: DEPRIORITIZED` and move to the next signal.

---

## Skill File Structure

```
skills/
  {industry}/
    {skill-name}/
      SKILL.md          # Claude Code format (triggers via /project:skill-name)
      README.md         # Portable — self-contained prompt template for any AI tool
      tests/
        scenario-1.md   # Realistic test input + expected output criteria
        scenario-2.md
```

Industries: `finance/`, `legal/`, `consulting/`

---

## Research Sources (Priority Order)

1. **GitHub** — issues and discussions in legaltech, fintech, and consulting repos mentioning AI friction
2. **Hacker News** — threads about AI in professional/knowledge work
3. **Reddit** — r/legaltech, r/fintech, r/consulting practitioner pain points
4. **Medium/Substack** — practitioners describing manual workflows that should be AI-assisted

---

## Usage Limit Rules

- Use `claude-haiku-4-5` for research, signal triage, and iterative drafting
- Use `claude-sonnet-4-6` for final skill design and quality review only
- **Never enable consumption-based overflow**
- If approaching rate limits mid-cycle, save state to `pipeline/state.json` and halt gracefully
- Batch web searches; avoid many small individual calls

---

## GitHub Setup

- Repo: `Xeebs/grimoire` (public)
- Branch: `main`
- Commit format: `feat(skills): add {skill-name} for {industry}`
- After each publish: create a GitHub Discussion in the `Announcements` category
- Send push notification to active Claude Code session
- Verify `gh auth status` before any push. If unauthenticated, skip publish and notify.
