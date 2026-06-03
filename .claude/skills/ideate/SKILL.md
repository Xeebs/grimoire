---
name: grimoire-ideate
description: Spawns the skill-designer subagent to design a complete novel skill from the top-priority signal in the pipeline queue
---

This skill is invoked by the Grimoire orchestrator to delegate skill design to the skill-designer subagent.

## Invocation

Read the top unworked High-strength signal from `pipeline/queue.md`. Spawn the `skill-designer` subagent (defined in `.claude/agents/skill-designer.md`) with a self-contained prompt that includes:

- The full signal text (industry, role, workflow step, proposed direction, novelty rationale)
- The output directory: `skills/{industry}/{skill-name}/`
- The skill format rules from `.claude/rules/code-style.md`
- The test scenario format from `.claude/rules/testing.md`
- The quality criteria from `CLAUDE.md` (all 5 criteria, verbatim)
- Instruction to mark the signal `status: DESIGNING` in `pipeline/queue.md`

## If re-spawning after a failed test

Pass the skill-designer the additional context:
- Path to `skills/{industry}/{skill-name}/tests/result.md`
- Instruction: do not modify test scenarios, only revise `SKILL.md` and `README.md`
- Attempt number (max 3)

## What the subagent produces

- `skills/{industry}/{skill-name}/SKILL.md`
- `skills/{industry}/{skill-name}/README.md`
- `skills/{industry}/{skill-name}/tests/scenario-1.md`
- `skills/{industry}/{skill-name}/tests/scenario-2.md`
- Queue updated with `status: DESIGNING`

## Orchestrator action after subagent returns

If subagent returns `NOVELTY_FAIL`: mark signal `status: DEPRIORITIZED`, select next signal, re-invoke this skill. Otherwise advance to the test phase. Update `pipeline/state.json` with `current_phase: TEST`.
