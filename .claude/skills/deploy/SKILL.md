---
name: grimoire-publish
description: Spawns the publisher subagent to run the final quality gate and publish a tested skill to Xeebs/grimoire on GitHub
---

This skill is invoked by the Grimoire orchestrator only after the quality-auditor subagent has returned a PASS verdict.

## Invocation

Spawn the `publisher` subagent (defined in `.claude/agents/publisher.md`) with a self-contained prompt that includes:

- The skill directory path: `skills/{industry}/{skill-name}/`
- The GitHub repo: `Xeebs/grimoire`
- The commit message format: `feat(skills): add {skill-name} for {industry}`
- The path to `pipeline/published.md` for logging
- The path to `pipeline/queue.md` for status update
- The path to `pipeline/state.json` for state update
- Instruction to create a GitHub Discussion in the `Announcements` category
- Instruction to send a push notification on success

## What the subagent produces

- Skill committed and pushed to `Xeebs/grimoire main`
- GitHub Discussion created in Announcements
- Push notification sent
- Entry appended to `pipeline/published.md`
- Signal marked `status: PUBLISHED` in `pipeline/queue.md`
- `pipeline/state.json` updated with `current_phase: FEEDBACK_CHECK`

## Orchestrator action after subagent returns

- If `AUTH_FAIL`: log to `pipeline/state.json`, send push notification, end cycle
- If `QUALITY_FAIL`: re-enter Phase 4 (Ideate) with the failure details
- If success: log the Discussion URL, end cycle cleanly
