# Grimoire

> *A living library of AI skills for the modern information-economy workforce.*

```
  ██████╗ ██████╗ ██╗███╗   ███╗ ██████╗ ██╗██████╗ ███████╗
 ██╔════╝ ██╔══██╗██║████╗ ████║██╔═══██╗██║██╔══██╗██╔════╝
 ██║  ███╗██████╔╝██║██╔████╔██║██║   ██║██║██████╔╝█████╗
 ██║   ██║██╔══██╗██║██║╚██╔╝██║██║   ██║██║██╔══██╗██╔══╝
 ╚██████╔╝██║  ██║██║██║ ╚═╝ ██║╚██████╔╝██║██║  ██║███████╗
  ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝
```

---

## What is Grimoire?

Grimoire is an autonomous AI skill factory. It continuously researches, designs, tests, and publishes precision-crafted AI prompts — called **skills** — targeting the most time-intensive workflows in **Finance**, **Legal**, and **Consulting**.

Skills are not generic chatbot prompts. Each one is:

- **Role-specific** — written for a named practitioner (Credit Analyst, Litigation Associate, Strategy Consultant)
- **Workflow-anchored** — fires at a specific moment in a real professional workflow
- **Tested** — evaluated against realistic scenario inputs with pass/fail criteria before publishing
- **Dual-format** — ships as a Claude Code skill (`SKILL.md`) and a portable prompt template (`README.md`) usable in any AI tool

Some skills are **Level 3** — they bundle executable Python scripts and reference databases alongside the prompt, enabling deterministic calculation and authoritative lookups within the same workflow. See [Skill levels](#skill-levels) below.

---

## Who are these skills for?

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   FINANCE                 LEGAL                  CONSULTING     │
│   ───────                 ─────                  ──────────     │
│                                                                 │
│   Investment Bankers      Litigation Associates  Strategy       │
│   Credit Analysts         Patent Attorneys       Consultants    │
│   Private Equity          Paralegals             PMO Managers   │
│   M&A Advisors            Compliance Counsel     Analysts       │
│   Equity Researchers      Discovery Teams                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

These are knowledge workers who spend hours on structured, high-stakes documents — loan agreements, deposition transcripts, pitch decks, client memos — where the cost of error is high and the workflow is well-defined enough for a precise AI skill to do the heavy lifting.

---

## Skills Library

### Finance

| Skill | Level | Role | What it does |
|-------|-------|------|--------------|
| [`loan-covenant-compliance-spreader`](skills/finance/loan-covenant-compliance-spreader/) | L2 | Credit Analyst | Extracts covenant definitions, calculates ratios from submitted financials, produces compliance certificate with breach-proximity alerts |
| [`earnings-call-guidance-extractor`](skills/finance/earnings-call-guidance-extractor/) | L2 | Equity Research Analyst | Pulls quantitative guidance, qualitative signals, and management tone shifts from earnings call transcripts |
| [`cim-financial-data-extractor`](skills/finance/cim-financial-data-extractor/) | L2 | IB Analyst / PE Associate | Structures raw CIM financials into a model-ready data package with quality flags |
| [`lbo-model-assumption-auditor`](skills/finance/lbo-model-assumption-auditor/) | L2 | PE / IB Associate | Stress-tests LBO assumptions against deal comps and flags unrealistic inputs |
| [`qoe-ebitda-normalization-schedule`](skills/finance/qoe-ebitda-normalization-schedule/) | L2 | M&A / Transaction Advisory | Builds EBITDA bridge from reported to normalized, category by category |
| [`commercial-credit-memo-narrative-drafter`](skills/finance/commercial-credit-memo-narrative-drafter/) | L2 | Commercial Credit Analyst | Drafts structured credit memo narrative from borrower financials and underwriting inputs |
| [`pitchbook-comps-commentary-writer`](skills/finance/pitchbook-comps-commentary-writer/) | L2 | IB Analyst | Generates market commentary and positioning narrative around a comps table |
| [`transfer-pricing-benchmarking-study-generator`](skills/finance/transfer-pricing-benchmarking-study-generator/) | **L3** | Transfer Pricing Analyst | Screens comparables against OECD criteria, runs PLI calculations (Berry/TNMM) and IQR analysis, produces audit-ready benchmarking study |
| [`fpa-variance-commentary-builder`](skills/finance/fpa-variance-commentary-builder/) | **L3** | FP&A Analyst | Runs P/V/M decomposition via Python script, flags material variances, drafts CFO-ready commentary grounded in verified calculations |
| [`ma-working-capital-peg-analyzer`](skills/finance/ma-working-capital-peg-analyzer/) | **L3** | M&A Associate | Extracts NWC formula from SPA language, computes trailing-average peg against historical balance sheets, flags dispute-prone items |
| [`bank-regulatory-exam-response-packager`](skills/finance/bank-regulatory-exam-response-packager/) | **L3** | Bank Compliance Officer | Classifies MRAs/MRIAs against OCC/FDIC framework, drafts root cause analysis and corrective action plans, calculates response deadlines |

### Legal

| Skill | Level | Role | What it does |
|-------|-------|------|--------------|
| [`deposition-contradiction-mapper`](skills/legal/deposition-contradiction-mapper/) | L2 | Litigation Associate | Identifies and ranks contradictions across deposition transcripts and prior sworn statements |
| [`ediscovery-privilege-log-generator`](skills/legal/ediscovery-privilege-log-generator/) | L2 | Litigation Paralegal | Generates privilege log entries from document metadata and content summaries |
| [`regulatory-change-client-impact-memo`](skills/legal/regulatory-change-client-impact-memo/) | L2 | Compliance Attorney | Translates regulatory changes into client-specific impact analysis and action items |
| [`patent-office-action-response-drafter`](skills/legal/patent-office-action-response-drafter/) | L2 | Patent Attorney / Agent | Drafts substantive responses to USPTO office actions, claim by claim |
| [`playbook-driven-contract-redline-applier`](skills/legal/playbook-driven-contract-redline-applier/) | L2 | Contract Counsel | Applies a negotiation playbook to a counterparty draft, generating tracked-change redlines |
| [`warn-act-rif-compliance-analyzer`](skills/legal/warn-act-rif-compliance-analyzer/) | **L3** | Employment Attorney | Checks federal WARN + 11 state mini-WARN thresholds, calculates notice deadlines, flags AI-disclosure requirements, drafts jurisdiction-specific notices |

### Consulting

| Skill | Level | Role | What it does |
|-------|-------|------|--------------|
| [`stakeholder-interview-mece-synthesizer`](skills/consulting/stakeholder-interview-mece-synthesizer/) | L2 | Management Consultant | Synthesizes 10–30 interview notes into a MECE issue tree with hypothesis-driven recommendation brief |
| [`competitive-benchmarking-slide-synthesizer`](skills/consulting/competitive-benchmarking-slide-synthesizer/) | L2 | Strategy Consultant | Converts raw competitive data into a slide-ready benchmarking narrative with so-what commentary |
| [`pmi-workstream-status-synthesizer`](skills/consulting/pmi-workstream-status-synthesizer/) | L2 | PMO / Integration Manager | Aggregates workstream status inputs into an executive-ready integration dashboard narrative |
| [`market-entry-sizing-model-builder`](skills/consulting/market-entry-sizing-model-builder/) | **L3** | Strategy Consultant | Builds dual bottoms-up/top-down TAM models, triangulates and explains the reconciliation gap, produces slide-ready exhibit with sensitivity analysis |

---

## Skill levels

Skills come in two levels, reflecting increasing complexity and capability:

```
  Level 2 — Prompt + Instructions          Level 3 — Prompt + Scripts + Reference Data
  ─────────────────────────────            ────────────────────────────────────────────

  skills/{industry}/{skill-name}/          skills/{industry}/{skill-name}/
    ├── SKILL.md                             ├── SKILL.md          ← orchestrates everything
    ├── README.md                            ├── README.md
    └── tests/                               ├── SUB-WORKFLOW.md   ← phase-specific guidance
        ├── scenario-1.md                    ├── reference/
        ├── scenario-2.md                    │   └── database.md  ← lookup tables, taxonomies,
        └── result.md                        │                       regulatory catalogs
                                             ├── scripts/
                                             │   └── calc.py      ← deterministic computation
                                             └── tests/
                                                 ├── scenario-1.md
                                                 ├── scenario-2.md
                                                 └── result.md
```

**Level 2 skills** use SKILL.md instructions alone — suitable for judgment-heavy drafting and analysis tasks where AI reasoning is the bottleneck.

**Level 3 skills** bundle additional resources loaded on demand:
- **Sub-workflow files** (e.g. `SCREENING.md`, `NOTICE-DRAFTING.md`) — phase-specific guidance for complex multi-step workflows
- **Reference databases** (e.g. `warn-jurisdiction-database.md`, `oecd-criteria.md`) — authoritative lookup tables that would be too large to hold in context permanently
- **Executable scripts** (e.g. `variance_calc.py`, `warn_calculator.py`) — Python scripts for deterministic calculations where AI arithmetic is insufficient; the script code never enters the context window, only its output does

Level 3 is used when a workflow requires the combination of AI judgment and verifiable computation — e.g. applying OECD tax criteria then running IQR statistics, or checking 11 state employment laws then calculating notice deadlines.

---

## How a skill is structured

**`SKILL.md`** is built for [Claude Code](https://claude.ai/code) — drop it in your `.claude/skills/` directory and invoke it by name.

**`README.md`** is tool-agnostic — copy the prompt template into ChatGPT, Gemini, Cursor, or any AI assistant. For Level 3 skills, the README includes a manual fallback mode that doesn't require running the Python scripts.

---

## How the pipeline works

Grimoire runs an autonomous 4-phase pipeline that continuously ships new skills:

```
  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
  │   RESEARCH   │────▶│    DESIGN    │────▶│     TEST     │────▶│   PUBLISH   │
  │              │     │              │     │              │     │             │
  │ Scan GitHub, │     │ Select top   │     │ Run against  │     │ Commit to   │
  │ HN, Reddit,  │     │ signal. Novelty    │ 2 realistic  │     │ GitHub.     │
  │ Substack for │     │ check. Write │     │ scenarios.   │     │ Announce.   │
  │ AI gap       │     │ SKILL.md +   │     │ Must pass    │     │ Notify.     │
  │ signals      │     │ README.md    │     │ all criteria │     │             │
  └──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
        ▲                                          │
        │              (up to 3 redesign attempts) │
        └──────────────────────────────────────────┘
```

Each phase is executed by a dedicated subagent. Skills that fail testing after 3 iterations are deprioritized. Only skills that pass all test criteria are published.

---

## Using a skill

**In Claude Code:**
```bash
# From your project root
cp skills/finance/loan-covenant-compliance-spreader/SKILL.md .claude/skills/

# Then in a Claude Code session:
/loan-covenant-compliance-spreader
```

**As a standalone prompt:**  
Open any skill's `README.md`, copy the prompt template, fill in the `{PLACEHOLDER}` variables, and paste into your AI tool of choice.

---

## Quality bar

No skill ships without passing all of the following:

- **Novel** — not a basic prompt found in public libraries
- **Specific** — targets a named workflow step for a named role
- **Industry-grounded** — uses correct terminology, document types, and role titles
- **Tested** — passes both scenario tests with pre-defined criteria
- **Dual-format** — ships both `SKILL.md` and `README.md`

---

*Grimoire is continuously updated. New skills ship as signals are discovered.*

[![GitHub](https://img.shields.io/badge/GitHub-Xeebs%2Fgrimoire-181717?style=flat&logo=github)](https://github.com/Xeebs/grimoire)
