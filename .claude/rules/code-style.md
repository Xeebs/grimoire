# Skill Format Standards

## SKILL.md (Claude Code format)

Every skill must begin with YAML frontmatter:

```yaml
---
name: skill-name-in-kebab-case
description: One sentence — what this skill does and for whom. Used for matching at invocation time, so be specific.
industry: finance | legal | consulting
role: Target role title (e.g. "Investment Analyst", "Paralegal", "Management Consultant")
trigger: The specific workflow moment when a practitioner invokes this skill
---
```

The body must include:
- **Context block**: What situation the practitioner is in when using this
- **Instruction block**: Step-by-step what the skill does, written as directives to Claude
- **Output format**: Explicit description of the expected output structure
- **Constraints**: What the skill must NOT do (guardrails)

## README.md (Portable format)

Must be self-contained — no Claude Code knowledge assumed. Structure:

```markdown
# {Skill Name}

**Industry**: {Finance | Legal | Consulting}
**Role**: {Target role}
**Time saved**: {Estimated time saved vs. manual}

## What it does
[1-2 sentences]

## When to use it
[Specific workflow trigger]

## Prompt template
[The full prompt, with {PLACEHOLDER} variables in braces]

## Example output
[A short representative example]

## Tips
[1-3 tips for getting the best results]
```

## Naming Conventions

- Skill directory: `{verb}-{noun}` in kebab-case (e.g. `extract-covenants`, `draft-engagement-letter`)
- No generic names: `summarize`, `analyze`, `review` alone are not acceptable — must qualify the object
