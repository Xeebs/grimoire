# Scenario 1: EU AI Act GPAI Obligations + SEC AI Disclosure Rule — FinTech Credit and Advisory Platform

## Context

A compliance attorney at a mid-size law firm is advising Meridian FinTech Solutions Inc., a US-headquartered company that operates two regulated business lines: (1) a consumer credit-decisioning platform that uses a proprietary third-party-licensed AI model to generate credit scores for EU consumers; (2) a registered investment advisory (RIA) division that uses an AI-powered portfolio recommendation engine to generate trade suggestions for retail clients, which advisors may accept or override. Meridian is publicly listed on NASDAQ. The attorney has been asked to produce a client impact memo covering the August 2026 EU AI Act GPAI model obligations and a hypothetical SEC AI Disclosure Rule that took effect January 2025. Two new regulatory updates landed on the same day and the attorney needs a single deliverable covering both.

## Input

---

### Instrument 1 — European Union: EU AI Act (Regulation (EU) 2024/1689) — General Purpose AI (GPAI) Model Obligations and High-Risk AI System Requirements (Phased Applicability: August 2026 tranche)

**Issuing authority**: European Commission / AI Office
**Effective date for GPAI model obligations and high-risk AI system requirements**: 2 August 2026

**Applicability — High-Risk AI Systems (Annex III):**
AI systems used in credit scoring and creditworthiness assessment of natural persons are listed as high-risk under Annex III, Category 5(b). A provider or deployer of such a system that places it on the EU market or puts it into service in the EU is subject to the requirements in Chapter III. A "deployer" is any natural or legal person that uses an AI system under its own responsibility in a professional context. A "provider" is any person that develops or places on the market an AI system under its own name or trademark. Where a deployer uses a third-party provider's model without modification, the deployer obligations under Chapter III apply but Article 25 allocates certain provider obligations to the provider, not the deployer — however, if the deployer makes available a high-risk system to end users in the EU, the deployer remains responsible for post-market monitoring (Art. 72) and fundamental rights impact assessment (Art. 27).

**Article 9 — Risk Management System (mandatory for high-risk AI system deployers):**
Deployers of high-risk AI systems must establish, implement, document, and maintain a risk management system throughout the AI system lifecycle. The system must include: identification and analysis of known and foreseeable risks; estimation and evaluation of risks that may emerge when used in accordance with its intended purpose; adoption of appropriate risk management measures. The risk management system must be reviewed and updated whenever the AI system is modified or new risks are identified.

**Article 26 — Obligations of Deployers of High-Risk AI Systems:**
Deployers must: (a) use the AI system in accordance with the instructions for use; (b) assign human oversight to qualified natural persons with the ability to understand the system's capacities and limitations and to intervene or halt the system; (c) monitor the AI system's operation and report any serious incidents to the provider or relevant authority within the timeframe set by national implementing rules; (d) provide affected persons with information about the use of the AI system where the AI system interacts with or makes decisions about them.

**Article 27 — Fundamental Rights Impact Assessment (FRIA) (mandatory for certain deployers):**
Deployers of high-risk AI systems listed under Annex III, points 5–8 (which includes credit scoring under point 5(b)) must carry out a fundamental rights impact assessment prior to putting the system into service. The FRIA must document: the processes in which the AI system will be used and its purpose; the period and frequency of use; the categories of natural persons likely to be affected; the specific fundamental rights risks identified; the measures taken to mitigate those risks. The FRIA must be registered in the EU AI Act database.

**Article 49 — Registration of High-Risk AI Systems:**
Before placing a high-risk AI system on the EU market or putting it into service, deployers of high-risk systems listed in Annex III, points 2, 5, and 6 must register the system (or their use of the system, if the provider has not registered it) in the EU database established under Article 71. Deployers must confirm registration is current before each material change to the system's use case.

**GPAI Model Obligations (Chapter V, Articles 51–56) — applicable to providers of GPAI models:**
A "general purpose AI model" (GPAI model) is an AI model trained on large amounts of data, capable of serving multiple purposes. A "provider" of a GPAI model places it on the EU market or puts it into service. All GPAI model providers must: (Art. 53) prepare technical documentation; prepare information and documentation for downstream providers; comply with copyright law and publish a summary of training data. GPAI models with systemic risk (training compute above 10^25 FLOPs) face additional obligations including model evaluation, adversarial testing, and incident reporting to the AI Office (Art. 55). If a company deploys a GPAI model developed by a third party without placing it on the EU market under its own name, it is a deployer, not a provider, for GPAI purposes.

**Safe harbors and de minimis:**
The high-risk system requirements do not apply to AI systems used solely for national security, military, or defense purposes, or to AI systems used exclusively in personal non-professional activity. No revenue or size threshold applies to the high-risk deployer obligations — they apply regardless of company size.

---

### Instrument 2 — United States: SEC Artificial Intelligence Disclosure Rule (Hypothetical Release No. 34-99876, effective 1 January 2025)

**Issuing authority**: U.S. Securities and Exchange Commission
**Effective date**: 1 January 2025 (registered investment advisers with AUM above $1 billion had until 1 January 2025; advisers with AUM between $100 million and $1 billion have until 1 July 2025; advisers below $100 million have until 1 January 2026)

**Scope**: Applies to all registered investment advisers (RIAs) subject to the Investment Advisers Act of 1940 that use AI systems to generate, screen, or rank investment recommendations presented to clients.

**Rule 206(4)-X — Disclosure obligations:**
An RIA using an AI system in its advisory process must:
(a) Disclose to clients, in Form ADV Part 2A brochure, a plain-language description of: the AI system's role in generating recommendations; any material limitations of the AI system; the extent to which human advisors review, modify, or override AI-generated recommendations before presentation to clients; and whether the AI system is operated by the RIA or a third-party vendor.
(b) Provide a transaction-level disclosure notice to affected clients within 30 days of any trade executed primarily on the basis of an AI recommendation where the human advisor did not substantively modify the recommendation.
(c) Maintain books and records sufficient to demonstrate compliance, including logs of AI recommendations, human override decisions, and the basis for override or acceptance, retained for five years.

**Interpretive note on "primarily on the basis of":**
The SEC staff guidance (issued 15 March 2025) states that a recommendation is "primarily on the basis of" an AI recommendation when the AI system's output was the material driver of the trade decision and the human advisor's contribution was limited to formal approval without substantive analysis. The SEC has indicated it will consider the adviser's own characterization, the advisor's training and qualifications, the time spent in review, and documentation of the advisor's independent analysis in determining whether the human override was substantive.

**Exemptions**: The rule does not apply to AI systems used solely for back-office operations (settlement, reconciliation, compliance monitoring) or to quantitative models that predate 1 January 2020 and have not been materially updated since.

**Penalty framework**: Violations are subject to enforcement under the Investment Advisers Act, including civil money penalties up to $250,000 per violation.

---

### Client Profile

**Client name**: Meridian FinTech Solutions Inc.
**Business description**: Meridian operates two regulated business lines. (1) Meridian Credit Platform: a B2B SaaS product offered to EU-based consumer lenders. Meridian licenses a third-party AI model (CreditAI Pro v3.2, provided by CreditAI Ltd., a UK-registered company) and deploys it within its own platform to generate creditworthiness scores for EU consumers on behalf of its lender clients. Meridian's contracts with lender clients specify that Meridian is responsible for operating the model and for compliance with applicable AI regulations. Meridian does not develop or modify the model itself. (2) Meridian Investment Advisory (MIA): a registered investment adviser with the SEC, AUM of approximately $2.3 billion. MIA uses a proprietary AI recommendation engine ("PortfolioAI") to generate trade recommendations for approximately 4,200 retail client accounts. The current workflow is: PortfolioAI generates a trade recommendation; the assigned advisor receives it via the platform; the advisor clicks "Accept" or "Reject" and can add notes. Meridian's internal data shows that advisors accept PortfolioAI recommendations without modification approximately 87% of the time; average review time logged is 3.2 minutes per recommendation.
**Geographic footprint**: United States (primary), European Union (via Meridian Credit Platform, serving lender clients in France, Germany, and the Netherlands)
**Entity characteristics**: Publicly listed (NASDAQ). AUM $2.3 billion (investment advisory division). Approximately 340 employees. Meridian does not develop or train AI models — it deploys third-party models under commercial licenses in both business lines.
**Key contracts or policies**: (1) Master Services Agreement with CreditAI Ltd. (the GPAI model provider) — assigns compliance responsibility for the model's technical documentation and copyright compliance to CreditAI Ltd., but states that Meridian is responsible for deployer obligations under applicable regulations. (2) Form ADV Part 2A brochure last updated December 2023 — does not currently mention PortfolioAI.
**Role titles**: Chief Compliance Officer (CCO), Head of EU Regulatory Affairs, General Counsel, Head of Investment Advisory Operations
**Memo date**: 2026-06-03

---

## Expected Output Criteria

- [ ] Executive summary correctly identifies Meridian as subject to EU AI Act high-risk deployer obligations (not provider/GPAI obligations) and to the SEC AI Disclosure Rule, and correctly states the number of mandatory obligations with near-term deadlines
- [ ] Applicability analysis shows the threshold reasoning for both instruments: Meridian is a "deployer" not a "provider" under the EU AI Act because it deploys CreditAI Pro under a commercial license without placing it on the market under Meridian's own name; and Meridian MIA is a covered RIA under the SEC rule because its AUM ($2.3 billion) exceeds the $1 billion threshold with a January 2025 deadline already passed
- [ ] Obligation table includes at minimum: Art. 9 risk management system, Art. 26 deployer obligations, Art. 27 FRIA, Art. 49 registration, SEC Rule 206(4)-X Form ADV disclosure, SEC Rule 206(4)-X transaction-level disclosure, and SEC books-and-records requirement — each row includes the correct classification (MANDATORY or INTERPRETIVELY UNCERTAIN), a specific client business unit mapping, and a compliance deadline
- [ ] The SEC Rule 206(4)-X transaction-level disclosure obligation (and potentially the "primarily on the basis of" classification of MIA's workflow) is classified as INTERPRETIVELY UNCERTAIN, given that the 87% acceptance rate and 3.2 minute average review time creates a genuine grey zone under the SEC staff guidance definition of "substantive" human review — the memo must not resolve this as clearly compliant or clearly non-compliant
- [ ] The jurisdiction-by-jurisdiction analysis correctly distinguishes that Meridian's GPAI provider obligations (Art. 53–56) are CreditAI Ltd.'s responsibility under the MSA and EU Act provider definitions, not Meridian's — but does NOT omit the deployer obligations that remain with Meridian
- [ ] The prioritized action checklist assigns HIGH priority to at least: Art. 49 EU database registration (deadline August 2026), Art. 27 FRIA completion and registration (deadline August 2026), Form ADV Part 2A update under SEC Rule 206(4)-X (deadline already passed — January 2025), and the open item of obtaining data from Meridian to resolve the "substantive human review" question
- [ ] The Open Items section explicitly asks Meridian to provide documentation of advisors' actual review process to determine whether the 3.2-minute average review constitutes "substantive analysis" under SEC staff guidance, and asks whether lender clients in France, Germany, and the Netherlands have received the Art. 26(d) disclosure
- [ ] The memo uses correct EU AI Act terminology throughout: "deployer," "provider," "in-scope entity," "high-risk AI system," "GPAI model," "competent authority," "AI Office," "transposition" (if applicable), "Annex III," rather than informal descriptions
- [ ] No obligations are asserted as applying to Meridian based purely on regulatory intent — every obligation cited traces back to a specific article or rule number in the input instruments

## What failure looks like

A failing output treats Meridian as a GPAI model "provider" and assigns it Art. 53–56 technical documentation obligations that belong to CreditAI Ltd. under the Act's definitions. Alternatively, a failing output produces a flat summary of EU AI Act requirements without showing which Meridian business unit each obligation maps to. A failing output resolves the SEC "substantive human review" ambiguity by declaring Meridian compliant or non-compliant rather than flagging it as INTERPRETIVELY UNCERTAIN. A failing output omits the Form ADV update as already-overdue. A failing output omits the FRIA and Art. 49 database registration from the action checklist. A failing output uses generic language like "credit operations" instead of naming "Meridian Credit Platform" and "Meridian Investment Advisory."
