# Grimoire — Skill Pipeline Queue

Signals are listed in order of priority. The autonomous agent works top-to-bottom, selecting the first unworked High signal, then Medium.

**Statuses**: `UNWORKED` → `DESIGNING` → `TESTING` → `PUBLISHED` | `DEPRIORITIZED`

---

<!-- New signals are appended below by the research skill -->

## Signal: Cross-Period Earnings Call Nuance Extraction
- **Type**: RESEARCH
- **Status**: PUBLISHED
- **Strength**: High
- **Source**: https://arxiv.org/pdf/2505.16090
- **Industry**: Finance
- **Role**: Equity Research Analyst
- **Workflow step**: Reading earnings call transcripts to extract forward guidance signals, detect management tone shifts, and flag hedged language that implies downside risk — a task where LLMs achieve only ~80% accuracy and confidently hallucinate sentiment conclusions
- **Proposed skill**: Given a raw earnings call transcript, extract and categorize forward-guidance statements by confidence level, flag language shifts vs. the prior quarter's call, and produce a structured analyst brief distinguishing confirmed guidance from hedged or ambiguous signals
- **Novelty rationale**: Generic summarization prompts flatten nuance; this skill requires quarter-over-quarter comparative analysis and explicit hedging-language detection, which is a distinct analytical move that basic prompts miss
- **Added**: 2026-06-03

## Signal: CIM Financial Input Extraction for Deal Screening
- **Type**: RESEARCH
- **Status**: PUBLISHED
- **Strength**: High
- **Source**: https://www.fe.training/free-resources/ai/confidential-information-memorandum-review-use-case-using-ai/
- **Industry**: Finance
- **Role**: Investment Banking Analyst / Private Equity Associate
- **Workflow step**: Extracting key financial metrics (interest coverage ratios, LTV data, EBITDA, comparable valuations) from 200–300 page CIM PDFs to populate deal screening models — a process taking 3+ hours per document because data is trapped in non-standardized tables, charts, and scanned images
- **Proposed skill**: Given a CIM document, systematically extract named financial metrics into a structured table with source page citations, flag data that required inference versus direct extraction, and output a model-ready data sheet for deal screening
- **Novelty rationale**: The skill must handle unstandardized document formats, distinguish direct extraction from interpolation, and cite sources — standard summarization does none of this and produces unverifiable outputs that cannot leave an analyst's desk
- **Added**: 2026-06-03

## Signal: Deposition Testimony Contradiction Mapper
- **Type**: RESEARCH
- **Status**: PUBLISHED
- **Strength**: High
- **Source**: https://brasstranscripts.com/blog/legal-deposition-contradiction-ai-prompt
- **Industry**: Legal
- **Role**: Litigation Associate / Trial Paralegal
- **Workflow step**: Manually reading 1,200-page deposition transcripts (8–14 associate hours per transcript) to find internal contradictions, inconsistencies across multiple witnesses, and deviations from prior sworn statements — then organizing findings by strategic importance for cross-examination
- **Proposed skill**: Given one or more deposition transcript(s) and optionally a set of prior sworn statements, identify internal contradictions and cross-witness inconsistencies, rank each by cross-examination value, and output a structured contradiction brief with exact page/line citations
- **Novelty rationale**: The task requires multi-document cross-referencing with strategic prioritization, not simple summarization; the ranking by cross-examination value requires legal reasoning about credibility impact, which generic AI prompts do not provide
- **Added**: 2026-06-03

## Signal: Loan Covenant Compliance Certificate Spreader
- **Type**: RESEARCH
- **Status**: PUBLISHED
- **Strength**: High
- **Source**: https://www.datagrid.com/blog/ai-underwriters-covenant-compliance-monitoring
- **Industry**: Finance
- **Role**: Credit Analyst / Portfolio Manager
- **Workflow step**: Collecting quarterly borrower financials in varied formats, manually rebuilding per-loan covenant ratio formulas (since each credit agreement defines terms like DSCR and LTV differently), and checking each ratio against breach thresholds — a process that "swallows entire workdays" per analyst
- **Proposed skill**: Given a credit agreement and a borrower's quarterly financial submission, extract the specific covenant definitions from the agreement, calculate the required ratios against the submitted financials, and produce a compliance certificate with pass/fail status and a breach-proximity alert for each covenant
- **Novelty rationale**: The skill must interpret contract-specific ratio definitions (not universal formulas) and apply them to ad-hoc financial data — this is a document-to-calculation pipeline that requires legal reading plus financial modeling, which no generic prompt achieves
- **Added**: 2026-06-03

## Signal: Stakeholder Interview Synthesis to MECE Recommendation Structure
- **Type**: RESEARCH
- **Status**: PUBLISHED
- **Strength**: Medium
- **Source**: https://www.lyssna.com/reports/research-synthesis/
- **Industry**: Consulting
- **Role**: Management Consultant (Analyst / Associate)
- **Workflow step**: After conducting 10–30 stakeholder interviews, spending several days organizing raw notes into themes, identifying MECE issue buckets, and translating findings into strategically actionable recommendations — with 39% of practitioners calling the insight-to-recommendation translation the most frustrating step
- **Proposed skill**: Given a set of stakeholder interview notes or transcripts, cluster themes into a MECE issue tree, flag contradictions across stakeholder groups, and draft a recommendation brief structured as hypothesis-supported findings mapped to the original client question
- **Novelty rationale**: The skill must impose MECE logical structure on qualitative data and produce hypothesis-driven outputs, not just thematic summaries — standard AI tools produce flat theme lists that still require consultant restructuring before they are deliverable
- **Added**: 2026-06-03

## Signal: E-Discovery Privilege Log Generator
- **Type**: RESEARCH
- **Status**: PUBLISHED
- **Strength**: High
- **Source**: https://dredyson.com/the-definitive-guide-to-running-local-llms-for-e-discovery-how-legaltech-teams-can-deploy-ollama-on-premises-for-faster-legal-document-review-pii-detection-and-privilege-log-automation-a/
- **Industry**: Legal
- **Role**: Litigation Paralegal / Discovery Associate
- **Workflow step**: Manually reviewing each flagged document from e-discovery productions to classify privilege basis, identify attorneys, characterize the legal advice sought, and write FRCP Rule 26(b)(5)-compliant log entries — described as "the most tedious, soul-crushing task in e-discovery," with automation cutting review time by roughly 40% in multi-district litigation
- **Proposed skill**: Given a set of flagged e-discovery documents, generate a structured privilege log with per-document entries covering privilege type, author/recipient attorney names, date, subject-matter description, and legal basis, formatted as a CSV or load file ready for review platforms
- **Novelty rationale**: The skill must apply FRCP Rule 26(b)(5) standards, distinguish work product from attorney-client privilege, and produce court-ready log language — generic AI prompts produce informal descriptions that fail opposing counsel scrutiny and require full attorney rework
- **Added**: 2026-06-03

## Signal: LBO Model Assumption Audit and Firm-Convention Adapter
- **Type**: RESEARCH
- **Status**: PUBLISHED
- **Strength**: High
- **Source**: https://www.returncatalyst.ai/blog/ai-lbo-model-automation
- **Industry**: Finance
- **Role**: Private Equity Associate / Investment Banking Associate
- **Workflow step**: After AI tools generate a first-pass LBO model from CIM inputs, associates manually audit every formula for logic errors (circular reference resolution, revolver edge cases), stress-test extreme scenarios, validate assumptions against sector benchmarks, and reformat the entire model to match the firm's proprietary modeling conventions — the remaining ~20% of model-build time that represents the highest-risk work
- **Proposed skill**: Given an AI-generated LBO model and a firm's stated modeling conventions, systematically audit circular references and debt schedule logic, generate a stress-test scenario matrix (revenue decline, margin compression, rate shock), flag assumptions deviating from sector benchmarks, and produce a model-review checklist with pass/fail status per convention
- **Novelty rationale**: The skill operates on the output of other AI tools rather than raw inputs — a second-order workflow gap no public prompt addresses — and requires financial modeling knowledge to evaluate formula logic and sector-specific benchmarking judgment
- **Added**: 2026-06-03

## Signal: Multi-Jurisdiction Regulatory Change to Client Impact Memo
- **Type**: RESEARCH
- **Status**: PUBLISHED
- **Strength**: High
- **Source**: https://www.whitecase.com/insight-alert/2026-horizon-scanning-what-general-counsel-and-company-secretaries-need-know-2026
- **Industry**: Legal
- **Role**: Compliance Attorney / Regulatory Counsel
- **Workflow step**: When new regulations are issued across multiple jurisdictions (e.g., EU AI Act, UK Employment Rights Act, SEC AI disclosure rules), compliance attorneys manually read each regulatory text, identify which client business units or contract provisions are affected, and draft tailored client impact memos — consuming days per regulatory update across a multi-jurisdictional portfolio
- **Proposed skill**: Given one or more regulatory update texts and a client's business description or contract portfolio, identify affected provisions and obligations, map each to the relevant client business unit or contract clause, and draft a structured impact memo with a prioritized action checklist and compliance deadline table
- **Novelty rationale**: The skill must perform two-sided legal reasoning — reading regulatory intent and mapping it against client-specific facts — producing a deliverable document rather than a general summary; generic AI produces flat regulation summaries that still require attorneys to perform the client-mapping step manually
- **Added**: 2026-06-03

## Signal: Quality of Earnings EBITDA Normalization Schedule
- **Type**: RESEARCH
- **Status**: PUBLISHED
- **Strength**: Medium
- **Source**: https://finance.yahoo.com/news/finsider-ai-launches-quality-earnings-195900205.html
- **Industry**: Finance
- **Role**: M&A Analyst / Transaction Advisory Associate
- **Workflow step**: During buy-side due diligence, manually reviewing 3–5 years of target financials to identify and categorize non-recurring items (owner compensation adjustments, one-time legal costs, COVID-era impacts), rebuild normalized EBITDA bridges line by line in Excel, and produce a QofE schedule — work that traditionally required teams of analysts over multiple weeks using statistical sampling
- **Proposed skill**: Given a target company's historical income statements and a list of flagged unusual items, classify each item as recurring or non-recurring with documented rationale, calculate an adjusted EBITDA bridge for each period, flag items requiring management confirmation, and output a formatted QofE normalization schedule with narrative justification per adjustment
- **Novelty rationale**: The skill must apply M&A quality-of-earnings judgment (not just accounting rules) to distinguish defensible adjustments from aggressive ones and produce a deal-room-standard schedule; Finsider.ai's product confirms the manual gap but requires full system integration — a prompt-based skill is accessible for single-deal use
- **Added**: 2026-06-03

## Signal: Competitive Benchmarking Data-to-Slide Synthesis
- **Type**: RESEARCH
- **Status**: PUBLISHED
- **Strength**: Medium
- **Source**: https://elevatedsignal.com/insights/competitor-benchmarking-guide/
- **Industry**: Consulting
- **Role**: Strategy Consultant / Business Analyst
- **Workflow step**: Spending an average of 32 hours per competitive analysis cycle manually pulling competitor metrics from disparate sources (annual reports, press releases, industry databases), normalizing definitions across companies, and reformatting findings into slide-ready comparison tables and insight callouts — consuming junior analyst capacity without adding strategic value
- **Proposed skill**: Given a set of competitor data extracts and a client's named benchmarking dimensions, normalize the data across sources, build a structured comparison table with variance callouts, identify the two to three most strategically significant gaps, and output a slide-ready benchmarking brief with a recommended narrative headline
- **Novelty rationale**: The skill must handle definition inconsistency across sources (e.g., different EBITDA margin definitions), apply strategic prioritization to select decision-relevant gaps, and produce output in consulting deliverable format — generic AI produces flat data tables that require consultant interpretation and reformatting before client use
- **Added**: 2026-06-03

## Signal: Playbook-Driven Contract Redline Applier
- **Type**: RESEARCH
- **Status**: DEPRIORITIZED
- **Strength**: High
- **Source**: https://spellbook.com/learn/contract-playbook
- **Industry**: Legal
- **Role**: In-House Counsel / Commercial Attorney
- **Workflow step**: After a negotiation playbook is defined (preferred language, fallback positions, walk-away floors per clause type), attorneys still manually apply those standards clause-by-clause when reviewing third-party paper — spending an average of 2 hours per NDA and proportionally more for MSAs and SaaS agreements — because generic AI redlines without knowledge of firm-specific standards, forcing lawyers to reconcile AI output against playbook rules manually
- **Proposed skill**: Given a contract in third-party paper format and a firm's negotiation playbook (preferred positions, acceptable fallbacks, and hard limits per clause type), systematically redline each relevant clause to match playbook standards, flag clauses requiring escalation beyond playbook authority, and output a tracked-changes document with a deviation summary table showing accepted, modified, and escalated positions
- **Novelty rationale**: The skill encodes the two-document reasoning that specialized platforms like Spellbook and DraftWise charge SaaS fees to provide — cross-referencing counterparty language against organizational standards and surfacing a structured deviation report — which generic AI prompts cannot do because they lack awareness of firm-specific risk thresholds and fallback hierarchies
- **Added**: 2026-06-04

## Signal: Commercial Credit Memo Narrative Drafter
- **Type**: RESEARCH
- **Status**: PUBLISHED
- **Strength**: High
- **Source**: https://iacpm.org/wp-content/uploads/2025/03/IACPM-McKinsey-Gen-AI-Webinar-2025.pdf
- **Industry**: Finance
- **Role**: Commercial Banking Credit Analyst / Underwriter
- **Workflow step**: After spreading a borrower's financials, analysts manually write the narrative sections of the credit memo — company background, industry and sector outlook, financial performance commentary, and risk/mitigant discussion — a process that takes 4–8 hours per deal and constitutes the primary throughput bottleneck in commercial lending pipelines; IACPM-McKinsey research confirms only ~30% of North American FIs have implemented GenAI for this task despite 80% expecting to do so, citing unstructured data challenges and the need for auditable sourcing
- **Proposed skill**: Given a borrower's financial spread, credit agreement term sheet, and industry sector, draft each named narrative section of a commercial credit memo (company overview, ownership and management, industry analysis, financial performance, credit strengths and risks, mitigants, and recommendation) with citations to input data, flagging any section where source data is insufficient to support the narrative without analyst judgment
- **Novelty rationale**: The skill must write structured, bank-standard narrative across multiple distinct sections with grounded citations — not a general summary — and must flag gaps where analyst judgment is required rather than hallucinating unsupported conclusions; this mirrors what bank-specific AI deployments at global institutions achieve but is not accessible via any public prompt skill
- **Added**: 2026-06-04

## Signal: Patent Office Action Response Drafter
- **Type**: RESEARCH
- **Status**: PUBLISHED
- **Strength**: High
- **Source**: https://www.deepip.ai/blog/ai-native-patent-practice-workflows
- **Industry**: Legal
- **Role**: Patent Attorney / Patent Agent
- **Workflow step**: When the USPTO issues an Office Action (rejection or objection), patent practitioners manually reconstruct the claim-prior art mapping from scratch — reading the examiner's rejection arguments, identifying each cited prior art reference, locating the specific claims and limitations at issue, and drafting arguments distinguishing the invention from the cited art — a process that takes 8–15 hours per response and is described as "repetition without accumulation" because the same reasoning must be rebuilt each time without carry-over from prior prosecution history
- **Proposed skill**: Given a USPTO Office Action (with examiner rejection arguments and cited prior art references) and the pending claims, identify each rejection ground and its cited basis, map the claimed limitations against the cited art, draft a structured response distinguishing the claims with legal argument and claim amendment recommendations where necessary, and produce a first-draft response brief organized by rejection type (102 anticipation, 103 obviousness, 112 written description)
- **Novelty rationale**: The skill must apply patent prosecution legal reasoning — distinguishing claims from prior art under 35 U.S.C. 102/103/112 — and produce court-standard argument structure; existing AI tools (Patlytics, DeepIP) provide this at SaaS platform cost, but no public prompt skill makes this reasoning accessible for single-matter use without platform subscription
- **Added**: 2026-06-04

## Signal: Pitchbook Comparable Companies Commentary Writer
- **Type**: RESEARCH
- **Status**: PUBLISHED
- **Strength**: Medium
- **Source**: https://www.auxi.ai/blog/ai-in-investment-banking-pitchbooks-generation
- **Industry**: Finance
- **Role**: Investment Banking Analyst
- **Workflow step**: After pulling trading comps data and building the comps table, analysts manually write the strategic narrative for the comparable companies section — selecting the peer set rationale, flagging outliers, contextualizing multiples against the target's specific business mix, and drafting the 3–5 insight callouts that accompany the table — work that requires domain judgment and takes 2–4 hours per section; AI tools automate the data pull and table formatting but leave the interpretive narrative entirely to the analyst
- **Proposed skill**: Given a completed comparable companies data table (peer names, metrics, multiples) and a target company description, draft the peer set rationale explaining inclusion/exclusion decisions, identify and explain outlier observations, contextualize the implied valuation range against the target's specific business characteristics, and produce slide-ready commentary callouts formatted for insertion into a pitchbook comps page
- **Novelty rationale**: The skill addresses the interpretive, judgment-heavy layer that sits above formatted comps data — the "why these peers, what do these multiples mean for this specific target" reasoning that distinguishes a senior banker's narrative from a junior analyst's raw table; this analytical translation step is explicitly identified as the remaining manual bottleneck after AI handles formatting and data aggregation
- **Added**: 2026-06-04

## Signal: Post-Merger Integration Workstream Status Synthesizer
- **Type**: RESEARCH
- **Status**: PUBLISHED
- **Strength**: Medium
- **Source**: https://www.haptiq.com/post/ai-platforms-for-post-merger-integration-from-roll-ups-to-operational-integration
- **Industry**: Consulting
- **Role**: PMO Consultant / Integration Manager
- **Workflow step**: During post-merger integration, PMO consultants spend 6–10 hours per week manually collecting status updates from 20–50 workstream leads across HR, IT, finance, operations, and legal tracks, reconciling inconsistent RAG statuses, identifying at-risk milestones, and producing the weekly executive steering committee dashboard — a process that requires judgment about which risks are truly critical and which status updates are overly optimistic, but that current enterprise AI tools handle only at full-system integration cost
- **Proposed skill**: Given a set of workstream status updates (in varied free-text or template formats from individual track leads), normalize each to a consistent RAG status with defined criteria, identify cross-workstream dependencies at risk, flag milestones where self-reported status appears inconsistent with described blockers, and produce a structured executive steering committee dashboard with a prioritized escalation list and recommended discussion agenda
- **Novelty rationale**: The skill must impose consistent criteria on subjective self-reported statuses, detect optimism bias in status descriptions, and produce a prioritized escalation view — analytical moves requiring PMO judgment that raw consolidation tools skip; enterprise platforms (Haptiq, Amafi.ai) provide this at platform cost, but no prompt skill addresses it for consultants working lean on single-integration mandates
- **Added**: 2026-06-04
