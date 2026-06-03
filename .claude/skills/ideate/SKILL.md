---
name: grimoire-ideate
description: Design a complete, novel AI skill based on a researched signal from the Grimoire pipeline queue
---

You are the Grimoire skill designer. Given a High-strength signal from `pipeline/queue.md`, design a complete, production-quality skill.

## Design Steps

1. **Select signal**: Pick the top unworked High-strength signal from `pipeline/queue.md`. If none exist, take the top Medium signal.

2. **Novelty check**: Search GitHub, PromptBase, and public prompt libraries for similar skills. If 3+ close matches exist, either differentiate clearly or select a different signal.

3. **Design the skill**:
   - Identify the exact trigger moment (when does a practitioner invoke this?)
   - Define required inputs (what context must they provide?)
   - Write step-by-step instructions that Claude will follow
   - Define the output format precisely
   - Define what the skill must NOT do (guardrails)

4. **Write SKILL.md**: Follow the format in `.claude/rules/code-style.md`. Place in `skills/{industry}/{skill-name}/SKILL.md`.

5. **Write README.md**: Write the portable prompt template version. Must be self-contained. Place in `skills/{industry}/{skill-name}/README.md`.

6. **Write test scenarios**: Write 2 realistic test scenarios in `skills/{industry}/{skill-name}/tests/scenario-1.md` and `scenario-2.md`. Follow the format in `.claude/rules/testing.md`.

7. **Update queue**: Mark the signal `status: DESIGNING` in `pipeline/queue.md`.

After completing all files, summarize: skill name, industry, target role, and the novelty rationale.
