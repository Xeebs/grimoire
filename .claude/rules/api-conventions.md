# Research Sources and Signal Protocol

## Source Priority and Search Patterns

### GitHub (Highest signal quality)
Search for practitioner friction in professional AI tools:
- `is:issue AI workflow` in repos tagged `legaltech`, `fintech`, `consulting`
- `is:discussion "claude" OR "chatgpt" workflow friction` in professional tool repos
- Trending repos in categories: legal-tech, financial-analysis, document-processing

### Hacker News
- Search `site:news.ycombinator.com` + `{industry} AI workflow`
- Focus on "Ask HN" threads where practitioners describe pain points
- Prioritize threads with 50+ comments — signals real practitioner engagement

### Reddit
Target subreddits: r/legaltech, r/fintech, r/consulting, r/BigLaw, r/finance, r/financialcareers
- Look for posts asking "does AI do X?" where the answer is "not well"
- Look for workflow descriptions with "manually" or "hours" — signs of automation opportunity

### Medium / Substack
- Search `"{industry}" AI workflow site:medium.com`
- Look for practitioner posts (not vendor marketing) describing their actual AI use
- Reverse-engineer the skill from what they describe doing manually

## Signal Scoring

| Strength | Criteria |
|----------|----------|
| **High** | A specific practitioner describes a named workflow step where AI falls short or is entirely absent |
| **Medium** | A tool/product solves this problem (reverse-engineer the underlying skill opportunity) |
| **Low** | General opinion that AI could be better in this space (mine for specific workflow details) |

Only High and Medium signals proceed to the design phase within the same cycle.

## Queue Entry Format

Append to `pipeline/queue.md`:

```markdown
## Signal: {title}
- **Type**: RESEARCH | FEEDBACK
- **Status**: UNWORKED
- **Strength**: High | Medium | Low
- **Source**: {URL}
- **Industry**: Finance | Legal | Consulting
- **Role**: {job title}
- **Workflow step**: {the specific task}
- **Proposed skill**: {one sentence}
- **Novelty rationale**: {why this isn't easily found elsewhere}
- **Added**: {YYYY-MM-DD}
```
