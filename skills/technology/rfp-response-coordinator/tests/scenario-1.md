# Scenario 1: Enterprise Cloud Analytics RFP — Financial Services Prospect with Full Security and Compliance Section

## Context

A Sales Engineer at a mid-market B2B analytics SaaS company (call it "Lumina Analytics") is coordinating the response to an RFP from Westbrook Capital Management, a $12B AUM registered investment adviser. Westbrook's IT procurement team issued a 41-question RFP as part of a vendor evaluation for replacing their current BI platform with Lumina's platform.

The SE has Lumina's content library — a curated set of 18 approved prior responses organized by category. The RFP due date is 10 business days from receipt. Westbrook is a known SOC 2-required prospect; the RFP preamble states they operate under SEC Rule 17a-4 electronic records retention requirements. The SE needs to run the triage before the kickoff call with Product, Security, and Legal the next morning.

---

## Input

### RFP Due Date
2026-06-18

### Prospect Name
Westbrook Capital Management

### Prospect Context
Westbrook is a registered investment adviser (RIA) managing $12B AUM across long/short equity and fixed income strategies. They operate under SEC Rule 17a-4 for electronic records retention. Their current BI platform is Tableau; primary integration requirement is with their Bloomberg BVAL feed and an internal order management system (OMS) built on Advent Geneva. They have stated that SOC 2 Type II certification and a signed Data Processing Agreement are mandatory before contract execution.

### RFP / Questionnaire

**SECTION 1 — VENDOR OVERVIEW**

1.1 Provide a company overview including year founded, headquarters location, total employee count, and primary product offering.

1.2 Describe your funding status (public, private, PE-backed, bootstrap). Provide your most recent annual recurring revenue (ARR) figure or a range if exact figures are confidential.

1.3 List any material ownership changes, acquisitions, or restructuring events in the past 24 months.

**SECTION 2 — SECURITY AND COMPLIANCE**

2.1 Does your platform maintain SOC 2 Type II certification? If yes, provide the report date, audit period covered, and the name of the auditing firm.

2.2 Describe your encryption standards for customer data at rest and in transit. Specify the algorithm, key management approach, and rotation schedule.

2.3 Does your platform support role-based access control (RBAC)? Describe the granularity of permission settings available to administrators.

2.4 Describe your incident response process. What is your committed RTO and RPO? Provide your most recent Business Continuity Plan (BCP) test date.

2.5 Do you maintain a formal vendor risk management program for your sub-processors? List your top five sub-processors by data access scope.

2.6 Describe your data retention and deletion policies. Can customers initiate a verifiable data deletion request, and what is your confirmed deletion timeline?

2.7 Does your platform support immutable audit logging for all user actions? Can logs be exported and retained by the customer in a customer-controlled storage environment?

**SECTION 3 — TECHNICAL CAPABILITIES**

3.1 Describe your data ingestion architecture. What file formats, streaming protocols, and API types does your platform natively support for data import?

3.2 What is your platform's maximum supported data volume per tenant? Describe any throttling, rate limiting, or performance degradation thresholds.

3.3 Describe your visualization capabilities. Does the platform support custom chart types beyond standard bar, line, and pie charts?

3.4 Does your platform support scheduled report delivery? Describe the scheduling options (frequency, format, recipient management).

3.5 Describe your platform's alerting and threshold monitoring capabilities. Can alerts trigger external webhooks or API calls?

**SECTION 4 — INTEGRATION**

4.1 Does your platform offer a REST API? Provide a link to your API documentation or describe coverage.

4.2 Do you support SAML 2.0 for SSO? List the identity providers (IdPs) your platform has validated integrations with.

4.3 Describe your native or supported integration with Bloomberg data feeds (specifically BVAL pricing data).

4.4 Do you offer a pre-built connector or documented integration path for Advent Geneva OMS data?

4.5 Describe your Salesforce CRM integration capabilities, if any.

**SECTION 5 — COMPLIANCE AND REGULATORY**

5.1 Can your platform be configured to meet SEC Rule 17a-4 electronic records retention requirements (WORM storage, audit trail, non-erasure)? Describe the specific configuration steps required.

5.2 Do you have experience serving SEC-registered investment advisers (RIAs)? Provide reference accounts or describe your experience in the RIA vertical.

5.3 Are you willing to execute a Data Processing Agreement (DPA) prior to contract execution? Describe your standard DPA terms and any customization flexibility.

5.4 Do you maintain cyber liability insurance? Provide coverage amount and carrier name.

**SECTION 6 — COMMERCIAL**

6.1 Describe your pricing model. Is pricing per seat, per data volume, per query, or a platform fee?

6.2 What is your standard contract term? Do you offer month-to-month, annual, or multi-year options?

6.3 Describe your SLA commitments for platform uptime. What is your credited remedy if SLA is breached?

---

### Content Library

ENTRY ID: ENTRY-CORP-001
CATEGORY: General/Administrative
RESPONSE TEXT: Lumina Analytics was founded in 2018 and is headquartered in Austin, Texas. We employ approximately 210 full-time staff across product, engineering, customer success, and go-to-market functions. Our primary product is the Lumina Analytics Platform, a cloud-native business intelligence and data visualization solution designed for mid-market and enterprise B2B companies.
LAST UPDATED: 2026-01-15
---

ENTRY ID: ENTRY-CORP-002
CATEGORY: Commercial/Legal
RESPONSE TEXT: Lumina Analytics is a privately held company backed by Series B venture capital investment from Tier 1 and Tier 2 growth equity investors. We do not publicly disclose ARR figures. Upon request and under NDA, we can provide audited financial statements or a financial health summary to qualified enterprise prospects during advanced diligence stages.
LAST UPDATED: 2026-02-01
---

ENTRY ID: ENTRY-SEC-001
CATEGORY: Security
RESPONSE TEXT: Yes. Lumina Analytics maintains SOC 2 Type II certification. Our most recent report covers the period October 1, 2024 through September 30, 2025 and was issued by Armanino LLP. A copy of the full SOC 2 Type II report is available under NDA upon request. Please contact your Account Executive to initiate the NDA process.
LAST UPDATED: 2026-01-10
---

ENTRY ID: ENTRY-SEC-002
CATEGORY: Security
RESPONSE TEXT: All customer data at rest is encrypted using AES-256. All data in transit is encrypted using TLS 1.2 or higher; TLS 1.0 and 1.1 are disabled at the load balancer level. Encryption keys are managed through AWS Key Management Service (KMS) with per-tenant key isolation. Encryption keys are rotated on a 90-day automated schedule. Customer-managed key (CMK) options are available on Enterprise tier plans.
LAST UPDATED: 2025-11-20
---

ENTRY ID: ENTRY-SEC-003
CATEGORY: Security
RESPONSE TEXT: Lumina Analytics supports role-based access control (RBAC) at the workspace, dashboard, dataset, and row level. Administrators can define custom roles with granular permissions including view-only, edit, share, export, and admin. Row-level security (RLS) allows data access restrictions based on user attributes. RBAC configurations are auditable through the admin console.
LAST UPDATED: 2025-12-05
---

ENTRY ID: ENTRY-SEC-004
CATEGORY: Security
RESPONSE TEXT: Our incident response process is governed by our formally documented Incident Response Plan, reviewed annually. Our committed RTO is 4 hours and RPO is 1 hour for Tier 1 incidents (platform outage). Our Business Continuity Plan was last tested in Q3 2025. We notify affected customers within 1 hour of declaring a Tier 1 incident and provide status updates every 30 minutes via our status page.
LAST UPDATED: 2026-01-20
---

ENTRY ID: ENTRY-SEC-005
CATEGORY: Security
RESPONSE TEXT: Lumina Analytics maintains a formal vendor risk management program. All sub-processors are assessed prior to onboarding and annually thereafter. Our primary sub-processors with material data access are: (1) Amazon Web Services (compute, storage, networking), (2) Snowflake (data warehousing for certain analytics workloads), (3) Twilio SendGrid (transactional email delivery), (4) Zendesk (customer support ticketing), (5) Datadog (infrastructure monitoring). A complete sub-processor list is available upon request.
LAST UPDATED: 2026-03-01
---

ENTRY ID: ENTRY-SEC-006
CATEGORY: Security
RESPONSE TEXT: Lumina Analytics retains customer data for the duration of the active subscription. Upon contract termination, customer data is deleted from production systems within 30 days and from backup systems within 90 days. Customers may submit a verifiable data deletion request through the admin console or via written notice to privacy@lumina.io. Deletion is confirmed in writing within 5 business days of completion.
LAST UPDATED: 2025-10-15
---

ENTRY ID: ENTRY-TECH-001
CATEGORY: Technical Capability
RESPONSE TEXT: Lumina Analytics supports data ingestion via REST API, native file upload (CSV, JSON, Parquet, Excel), S3-compatible object storage connectors, and real-time streaming via Kafka and Kinesis integrations. Batch ingestion jobs can be scheduled at intervals as granular as 15 minutes.
LAST UPDATED: 2025-09-01
---

ENTRY ID: ENTRY-TECH-002
CATEGORY: Technical Capability
RESPONSE TEXT: Each Lumina tenant supports up to 50TB of active data in production. Query performance is optimized through columnar storage and automatic query caching. For workloads exceeding 50TB, dedicated infrastructure options are available on Enterprise Plus tier. Rate limiting applies to API endpoints at 1,000 requests per minute per tenant; batch ingestion is not rate-limited.
LAST UPDATED: 2025-11-15
---

ENTRY ID: ENTRY-TECH-003
CATEGORY: Technical Capability
RESPONSE TEXT: Lumina Analytics supports 40+ visualization types including standard bar, line, pie, scatter, heat map, treemap, waterfall, funnel, Gantt, geographic map, and custom chart types built using our Vega-Lite extension layer. Custom chart definitions can be imported via JSON schema.
LAST UPDATED: 2026-01-05
---

ENTRY ID: ENTRY-TECH-004
CATEGORY: Technical Capability
RESPONSE TEXT: Scheduled report delivery is supported with the following options: delivery frequency from hourly to monthly, output formats including PDF, Excel, and CSV, recipient lists managed at the workspace level with individual opt-out capability, and delivery via email or webhook. Scheduled reports can be conditionally triggered based on data thresholds.
LAST UPDATED: 2025-12-20
---

ENTRY ID: ENTRY-TECH-005
CATEGORY: Technical Capability
RESPONSE TEXT: Lumina Analytics provides real-time alerting based on user-defined thresholds applied to any monitored metric or KPI. Alert delivery channels include email, Slack, and PagerDuty. Alerts can trigger outbound webhook calls to any HTTPS endpoint, enabling integration with external ticketing, automation, or SIEM systems.
LAST UPDATED: 2026-02-10
---

ENTRY ID: ENTRY-INTEG-001
CATEGORY: Integration
RESPONSE TEXT: Lumina Analytics offers a fully documented REST API covering all platform resources including datasets, dashboards, users, and scheduled jobs. API documentation is publicly available at docs.lumina.io/api. Authentication uses OAuth 2.0 bearer tokens. The API supports pagination, filtering, and bulk operations. An OpenAPI 3.0 specification is available for download.
LAST UPDATED: 2026-01-01
---

ENTRY ID: ENTRY-INTEG-002
CATEGORY: Integration
RESPONSE TEXT: Lumina Analytics supports SAML 2.0 for single sign-on. Validated identity provider integrations include Okta, Microsoft Azure Active Directory (Entra ID), and Google Workspace. Additional IdPs supporting the SAML 2.0 standard can be configured via our generic IdP setup flow. SCIM 2.0 provisioning is supported for Okta and Azure AD.
LAST UPDATED: 2026-03-15
---

ENTRY ID: ENTRY-INTEG-003
CATEGORY: Integration
RESPONSE TEXT: Lumina Analytics integrates with Salesforce CRM via a native connector supporting bidirectional data sync of Accounts, Opportunities, Contacts, and Activities objects. The Salesforce connector supports scheduled sync at 15-minute intervals and real-time sync via Salesforce Streaming API. Available on Professional tier and above.
LAST UPDATED: 2026-02-28
---

ENTRY ID: ENTRY-COMP-001
CATEGORY: Compliance/Regulatory
RESPONSE TEXT: Lumina Analytics is willing to execute a Data Processing Agreement (DPA) prior to contract execution. Our standard DPA incorporates EU GDPR Standard Contractual Clauses (SCCs) and CCPA-compliant data subject rights provisions. We offer customization flexibility on data subject rights response timelines, sub-processor notification periods, and breach notification deadlines. DPA requests should be directed to legal@lumina.io.
LAST UPDATED: 2025-12-01
---

ENTRY ID: ENTRY-COMP-002
CATEGORY: Compliance/Regulatory
RESPONSE TEXT: Lumina Analytics maintains cyber liability insurance with a coverage limit of $5,000,000 per occurrence and $10,000,000 aggregate. Our current carrier is Chubb Group. A certificate of insurance is available upon request.
LAST UPDATED: 2026-01-15
---

ENTRY ID: ENTRY-COMM-001
CATEGORY: Commercial/Legal
RESPONSE TEXT: Lumina Analytics pricing is structured as an annual platform fee based on the number of workspace users (viewer and editor seats) and data volume tier. Volume discounts apply at 50+ seats. Month-to-month, annual, and multi-year contract options are available. Multi-year agreements (2–3 year terms) include rate-lock provisions and enhanced SLA terms.
LAST UPDATED: 2026-03-01
---

ENTRY ID: ENTRY-COMM-002
CATEGORY: Commercial/Legal
RESPONSE TEXT: Lumina Analytics commits to 99.9% monthly platform uptime (excluding scheduled maintenance windows, communicated with 72-hour advance notice). In the event of an SLA breach, customers receive service credits of 10% of their monthly subscription fee for each full hour below the committed uptime threshold, up to 30% of the monthly fee in any given month. SLA credits are applied to the next invoice cycle.
LAST UPDATED: 2026-02-15
---

---

## Expected Output Criteria

- [ ] The Requirement Inventory correctly identifies all 23 requirements (Sections 1–6) with verbatim text and assigns each to the correct type — specifically: Section 2 requirements as Security, Section 4 requirements as Integration (not Security), and Section 5.1 (SEC Rule 17a-4) as Compliance/Regulatory rather than Technical Capability
- [ ] Requirement 4.3 (Bloomberg BVAL integration) and Requirement 4.4 (Advent Geneva OMS integration) are both classified as NO MATCH, because no content library entry covers either Bloomberg or Advent Geneva; no fabricated integration capability is drafted for either
- [ ] Requirement 5.1 (SEC Rule 17a-4 WORM storage) is classified as NO MATCH with a clear rationale — the content library's data retention entry (ENTRY-SEC-006) covers standard deletion policy but does not address WORM storage, immutable record retention, or SEC 17a-4 configuration steps
- [ ] Requirement 5.2 (RIA vertical experience and references) is classified as NO MATCH because no content library entry covers RIA customer references or financial services vertical experience
- [ ] Requirement 2.7 (immutable audit logging with customer-exportable logs) is classified as PARTIAL or NO MATCH — ENTRY-SEC-003 mentions audit logging via admin console but does not address immutability or customer-controlled export storage; a response drafted as DIRECT from ENTRY-SEC-003 is a failing output
- [ ] The gap list assigns Bloomberg BVAL (4.3) and Advent Geneva (4.4) to Engineering/Architecture as owner, not Product Management, with Priority: Critical, reflecting that integration gaps are deal-qualifier risks for a prospect whose primary data source is Bloomberg
- [ ] Requirement 5.1 (SEC 17a-4) gap is assigned to Legal/Compliance or Engineering/Architecture (not General/Administrative) with Priority: Critical and a note that this is a stated mandatory requirement in the RFP preamble
- [ ] ENTRY-INTEG-002 is used for Requirement 4.2 (SAML 2.0 SSO) as an ADAPT match — the library entry lists Okta, Azure AD, and Google Workspace; the response must retain this list verbatim and must NOT expand it to include IdPs (e.g., Ping, ADFS, OneLogin) not present in the library entry
- [ ] The Coordinator Summary correctly counts at least 5 Critical-priority gaps (4.3, 4.4, 5.1, 5.2 are minimum; 2.7 may be Critical or High depending on the skill's confidence assessment) and routes them to the correct owner buckets
- [ ] The response tracker table is sorted or organized so all NO MATCH / NEEDS SME INPUT requirements are clearly distinguishable from DRAFTED requirements — the tracker does not intermix drafted and gap items without differentiation

## What failure looks like

A failing output would:
- Draft an affirmative response to Requirement 4.3 (Bloomberg BVAL) stating that Lumina supports Bloomberg integrations, drawing on general knowledge about Bloomberg API availability, when no such entry exists in the provided content library
- Mark Requirement 2.7 (immutable audit logging with customer-exportable logs) as DIRECT using ENTRY-SEC-003, because that entry mentions audit logging — even though the entry makes no claim about log immutability or customer-controlled export
- Classify SEC Rule 17a-4 (5.1) as a Technical Capability question rather than Compliance/Regulatory, causing it to be routed to Product Management instead of Legal/Compliance
- Expand the SAML 2.0 IdP list in the drafted response for Requirement 4.2 to include Ping Identity or OneLogin, which are not present in ENTRY-INTEG-002
- Assign both Bloomberg BVAL and Advent Geneva gap questions to Product Management (because they look like "product feature" questions) rather than Engineering/Architecture (where integration design knowledge lives)
- Produce a Coordinator Summary that counts only 2–3 Critical gaps, missing the SEC 17a-4 and RIA-reference requirements that the RFP preamble flags as mandatory
