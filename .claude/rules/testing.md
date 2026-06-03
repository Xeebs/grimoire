# Skill Testing Protocol

Every skill must pass testing before it can be staged for publishing.

## Test Scenario File Format

Each file in `tests/` must follow this structure:

```markdown
# Scenario {N}: {Descriptive title}

## Context
[Background on the practitioner situation — who they are, what they're working on]

## Input
[The actual input the practitioner would provide — make it realistic, not toy-sized]

## Expected Output Criteria
- [ ] Criterion 1 (e.g. "Identifies all financial covenants by section number")
- [ ] Criterion 2 (e.g. "Flags ambiguous terms with a note, does not silently skip them")
- [ ] Criterion 3 (e.g. "Output is formatted as a table with columns: Covenant / Threshold / Trigger")

## What failure looks like
[Describe what a bad output would look like, so the evaluator can distinguish pass from borderline]
```

## Running Tests

1. Apply the skill's prompt to the scenario's Input
2. Evaluate the output against each Expected Output Criterion
3. Mark each criterion pass (✓) or fail (✗)
4. If any criterion fails, record the failure mode and iterate on the skill design
5. After iteration, re-run the full test — partial re-runs are not acceptable

## Pass Threshold

- All criteria must pass on both scenarios
- A skill that passes 90% of criteria on one scenario and 100% on the other is a **fail**
- Maximum 3 design-test iterations before marking a skill `DEPRIORITIZED`

## Realistic Inputs

Test inputs must reflect real professional documents and contexts:
- Finance: actual financial statement structure, loan agreement language, deal memo format
- Legal: real contract clause structure, regulatory filing language, discovery document types
- Consulting: actual slide/report structures, client briefing formats, analysis frameworks
