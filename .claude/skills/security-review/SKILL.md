---
name: grimoire-research
description: Spawns the researcher subagent to scan web sources for AI skill gap signals in Finance, Legal, and Consulting, and to monitor GitHub feedback on published skills
---

This skill is invoked by the Grimoire orchestrator to delegate research work to the researcher subagent.

## Invocation

Spawn the `researcher` subagent (defined in `.claude/agents/researcher.md`) with a self-contained prompt that includes:

- The task type: `RESEARCH` or `FEEDBACK_MONITORING`
- For RESEARCH: the target industries (Finance, Legal, Consulting), source priority list, and the path to `pipeline/queue.md`
- For FEEDBACK_MONITORING: the last cycle timestamp from `pipeline/state.json` and the GitHub repo (`Xeebs/grimoire`)
- The signal format from `.claude/rules/api-conventions.md`
- The duplicate-check instruction: read existing entries in `pipeline/queue.md` before appending

## What the subagent produces

- New signal entries appended to `pipeline/queue.md`
- For feedback tasks: GitHub issue comments posted, feedback signals appended
- A summary report returned to the orchestrator: N signals added, N skipped, N discarded

## Orchestrator action after subagent returns

Read the summary. If new High signals were added, advance to the ideate phase. Update `pipeline/state.json` with `current_phase: IDEATE` and `last_research: {datetime}`.
