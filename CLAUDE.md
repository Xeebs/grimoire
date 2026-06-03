# Grimoire — AI Skills Lab

## Mission
Continuously research, design, test, and publish high-quality AI skills for the modern information-economy workforce. Target industries: **Finance & Banking**, **Legal**, **Consulting & Knowledge Work**.

Grimoire publishes to GitHub: `Xeebs/grimoire`

---

## Subagent Architecture

Every phase of the pipeline is executed by a **dedicated subagent** spawned by the orchestrator. The orchestrator reads state, delegates work, and advances the pipeline — it does not do research, design, testing, or publishing directly.

| Phase | Subagent | Definition |
|-------|----------|------------|
| Research + Feedback | `researcher` | `.claude/agents/researcher.md` |
| Ideate & Design | `skill-designer` | `.claude/agents/skill-designer.md` |
| Test & QA | `quality-auditor` | `.claude/agents/quality-auditor.md` |
| Publish | `publisher` | `.claude/agents/publisher.md` |

Each subagent receives a fully self-contained prompt including all file paths, signal details, and success criteria it needs. Results are written to files; the orchestrator reads them and advances pipeline state. Subagents do not share session context with each other — every handoff is explicit and file-mediated.

---

## Autonomous Heartbeat Protocol

This project runs on an **hourly heartbeat**. On every cycle, check `pipeline/state.json` first and resume from the recorded phase:

### Phase 1 — Resume Check
Read `pipeline/state.json`. Identify `current_phase` and `active_skill`. If a skill is mid-flight, resume from that phase. If the previous cycle completed cleanly, start at Phase 2.

### Phase 2 — Feedback Check
Spawn the **researcher subagent** with task: check `Xeebs/grimoire` GitHub Issues and Discussions for new comments or feedback since the last cycle. Log actionable items as signals in `pipeline/queue.md` with `type: FEEDBACK`. Post a response to any unanswered issues.

### Phase 3 — Research
Spawn the **researcher subagent** with task: scan GitHub, Hacker News, Reddit, and practitioner blogs for AI workflow gap signals in Finance, Legal, and Consulting. Append 3–5 new High/Medium signals to `pipeline/queue.md`. Skip duplicates.

### Phase 4 — Ideate & Design
Spawn the **skill-designer subagent** with task: select the top unworked High-strength signal from `pipeline/queue.md`, perform a novelty check, and produce `SKILL.md`, `README.md`, and 2 test scenario files in `skills/{industry}/{skill-name}/`. Mark the signal `status: DESIGNING` in the queue.

### Phase 5 — Test
Spawn the **quality-auditor subagent** with task: run the skill against both test scenarios, evaluate each criterion, and write a pass/fail report to `skills/{industry}/{skill-name}/tests/result.md`. If it fails, re-spawn the skill-designer with the failure notes attached (max 3 attempts total). Mark signal `status: TESTING`.

### Phase 6 — Publish
Spawn the **publisher subagent** with task: run the final quality gate, commit and push the skill to `Xeebs/grimoire main`, create a GitHub Discussion announcement, send a push notification, and log to `pipeline/published.md`. Mark signal `status: PUBLISHED`.

### Cycle Limit
Complete at most **1 full skill per cycle** to protect usage limits. If rate-limited mid-cycle, write current state to `pipeline/state.json` and exit cleanly — the next heartbeat will resume.

---

## Quality Bar — Non-Negotiable

A skill must meet **all** of the following before publishing:

1. **Novel** — Not a basic prompt easily found in public libraries. If 3+ similar skills exist publicly, this one must show a clear, demonstrable improvement.
2. **Specific** — Targets a named workflow step and named role, not broad tasks like "summarize a document."
3. **Industry-grounded** — Uses correct terminology, document types, and role titles from the target industry.
4. **Tested** — Passes at least 2 realistic scenario tests with pre-defined expected output criteria.
5. **Dual-format** — Ships both `SKILL.md` (Claude Code) and `README.md` (portable prompt template).

If a skill fails the quality bar after 3 design attempts, mark it `status: DEPRIORITIZED` and move to the next signal.

---

## Skill File Structure

```
skills/
  {industry}/
    {skill-name}/
      SKILL.md            # Claude Code format
      README.md           # Portable — self-contained prompt template for any AI tool
      tests/
        scenario-1.md     # Realistic test input + expected output criteria
        scenario-2.md
        result.md         # Written by the quality-auditor subagent after testing
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

- Use `claude-haiku-4-5` for the researcher and quality-auditor subagents (high volume, lower complexity)
- Use `claude-sonnet-4-6` for the skill-designer and publisher subagents (quality-critical)
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
