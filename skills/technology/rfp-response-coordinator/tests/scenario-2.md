# Scenario 2: Security-Heavy DDQ — Healthcare SaaS Prospect with Sparse Content Library Coverage

## Context

A Solutions Consultant at a B2B workflow automation SaaS company (call it "Nexus Workflow") is responding to a Due Diligence Questionnaire (DDQ) from MidWest Health System (MWHS), a 12-hospital integrated delivery network evaluating Nexus for automating clinical operations workflows. MWHS's information security team issued the DDQ; it is separate from the main RFP (commercial evaluation is happening in parallel with a different team).

The DDQ has 28 questions, heavily weighted toward HIPAA, data handling, and infrastructure security. MWHS's security team stated in the cover email that any "No" answer to a HIPAA-related question is an automatic disqualification. The SC's content library for Nexus has 14 approved entries — a known gap is that Nexus only completed their HITRUST CSF certification 4 months ago and the content library does not yet have updated entries reflecting the new certification. The SE needs the triage complete before a call with Nexus's InfoSec team and the MWHS procurement contact in 36 hours.

The SC also notes that MWHS explicitly included this instruction in the DDQ cover page: "All responses must be prepared and certified by a qualified information security professional. AI-generated responses may not be used as submitted; all AI-drafted content must be reviewed and attested by a named certifying officer before submission."

---

## Input

### RFP Due Date
2026-06-12

### Prospect Name
MidWest Health System (MWHS)

### Prospect Context
MWHS operates 12 hospitals and 40+ ambulatory care sites across Illinois, Indiana, and Wisconsin. They are a HIPAA-covered entity and process ePHI. Their current workflow automation vendor is ServiceNow (which they are partially replacing). Primary concern stated in cover email: data residency must be US-only, and they require a signed Business Associate Agreement (BAA) before any ePHI data enters the Nexus platform. HITRUST CSF certification is preferred but not mandatory per their stated criteria; SOC 2 Type II is mandatory.

### DDQ / Questionnaire

**SECTION A — ORGANIZATIONAL AND COMPLIANCE POSTURE**

A.1 Is your company HIPAA compliant? Describe your HIPAA compliance program, including the date of your most recent HIPAA risk assessment.

A.2 Are you willing to execute a Business Associate Agreement (BAA) with covered entities prior to any ePHI being transmitted to or processed by your platform?

A.3 Do you maintain SOC 2 Type II certification? Provide the most recent report period, trust service criteria covered, and auditor name.

A.4 Do you hold HITRUST CSF certification? If yes, provide the validated assessment date, scope, and certification level (e1, i1, r2).

A.5 Do you maintain HIPAA training requirements for all employees who may have access to ePHI? Describe your training frequency and format.

**SECTION B — DATA HANDLING AND RESIDENCY**

B.1 Where is customer data physically stored? List all data center regions used for production data storage. Confirm whether US-only data residency is achievable and describe the configuration required.

B.2 Describe your data classification policy. How is ePHI identified, labeled, and handled differently from non-PHI data within your platform?

B.3 Describe your encryption standards for ePHI at rest and in transit. Specify algorithms, key management, and whether customers can provide their own encryption keys (BYOK/CMEK).

B.4 Describe your data minimization practices. Do you collect or retain any ePHI beyond what is required for service delivery?

B.5 What is your process for handling data subject access requests (DSARs) related to ePHI? What is your committed response timeline?

B.6 Describe your data backup procedures for ePHI. What is your backup frequency, retention period, and recovery testing cadence?

**SECTION C — ACCESS CONTROL AND IDENTITY**

C.1 Describe your multi-factor authentication (MFA) requirements. Is MFA mandatory for all user accounts, or only for privileged accounts?

C.2 Describe your privileged access management (PAM) controls for infrastructure-level access to systems that store or process ePHI.

C.3 Do you conduct background checks on all employees and contractors with access to ePHI? Describe the scope and frequency.

C.4 Does your platform support SAML 2.0 or OIDC for enterprise SSO? List supported identity providers.

**SECTION D — VULNERABILITY AND INCIDENT MANAGEMENT**

D.1 Describe your vulnerability management program. What is your SLA for patching Critical and High severity CVEs?

D.2 Do you conduct annual third-party penetration testing? Provide the most recent test date, scope, and the name of the testing firm.

D.3 Describe your HIPAA Breach Notification procedures. What is your committed notification timeline to covered entities in the event of a breach involving ePHI?

D.4 Describe your incident response program. Provide your most recent tabletop exercise date and a summary of the scenario tested.

**SECTION E — SUBPROCESSORS AND SUPPLY CHAIN**

E.1 List all subprocessors that may access, process, or store ePHI. Confirm whether each subprocessor has executed a BAA with your organization.

E.2 Do you conduct annual security assessments of subprocessors with access to ePHI?

E.3 Describe your process for notifying customers of subprocessor changes. What advance notice do you provide?

**SECTION F — BUSINESS CONTINUITY**

F.1 Describe your disaster recovery architecture for ePHI systems. Provide your committed RTO and RPO for healthcare-tier workloads.

F.2 When was your Business Continuity Plan (BCP) most recently tested? Describe the test scenario and outcome.

F.3 Do you maintain a separate disaster recovery environment geographically isolated from your primary data center? Describe the architecture.

---

### Content Library

ENTRY ID: ENTRY-HIPAA-001
CATEGORY: Compliance/Regulatory
RESPONSE TEXT: Nexus Workflow is HIPAA compliant. We maintain a comprehensive HIPAA compliance program administered by our Chief Privacy Officer. Our most recent HIPAA risk assessment was conducted in Q1 2026 per 45 CFR § 164.308(a)(1) requirements. The risk assessment was performed by a qualified third-party firm and covers all systems that create, receive, maintain, or transmit ePHI.
LAST UPDATED: 2026-02-15
---

ENTRY ID: ENTRY-HIPAA-002
CATEGORY: Compliance/Regulatory
RESPONSE TEXT: Yes. Nexus Workflow will execute a Business Associate Agreement (BAA) with covered entities and business associates prior to any ePHI being transmitted to or processed by our platform. Our standard BAA is available upon request. BAA negotiations should be directed to legal@nexusworkflow.com. We have executed BAAs with over 40 healthcare customers.
LAST UPDATED: 2026-01-20
---

ENTRY ID: ENTRY-SEC-001
CATEGORY: Security
RESPONSE TEXT: Yes. Nexus Workflow maintains SOC 2 Type II certification. Our most recent report covers the period July 1, 2024 through June 30, 2025 and was issued by BDO USA, LLP. The report covers Security, Availability, and Confidentiality trust service criteria. A copy is available under NDA. Contact your Account Executive to initiate the NDA process.
LAST UPDATED: 2025-10-01
---

ENTRY ID: ENTRY-SEC-002
CATEGORY: Security
RESPONSE TEXT: All customer data at rest, including ePHI, is encrypted using AES-256. Data in transit is encrypted using TLS 1.3; TLS 1.2 is supported for legacy compatibility; TLS 1.1 and 1.0 are disabled. Encryption keys are managed via AWS Key Management Service (KMS) with per-tenant key isolation. Bring Your Own Key (BYOK) is supported on Enterprise and Enterprise Plus tiers using AWS KMS custom key stores. Key rotation is performed on a 90-day automated schedule.
LAST UPDATED: 2026-01-10
---

ENTRY ID: ENTRY-SEC-003
CATEGORY: Security
RESPONSE TEXT: Multi-factor authentication (MFA) is mandatory for all user accounts on the Nexus platform, including standard users and administrators. We support TOTP authenticator apps, hardware security keys (FIDO2/WebAuthn), and SMS as a fallback (configurable by enterprise administrators). MFA cannot be disabled at the instance level; individual user exemptions require administrator approval and are logged.
LAST UPDATED: 2025-12-01
---

ENTRY ID: ENTRY-SEC-004
CATEGORY: Security
RESPONSE TEXT: Nexus Workflow performs annual third-party penetration testing. Our most recent test was conducted in March 2026 by NCC Group, covering our full production web application and API infrastructure. Findings are remediated per our vulnerability SLA: Critical CVEs within 24 hours, High CVEs within 7 days, Medium CVEs within 30 days. A summary of findings and remediation status is available under NDA.
LAST UPDATED: 2026-04-01
---

ENTRY ID: ENTRY-SEC-005
CATEGORY: Security
RESPONSE TEXT: Nexus Workflow maintains a formal Incident Response Plan reviewed and updated annually. Our most recent tabletop exercise was conducted in January 2026 and simulated a ransomware attack on our primary data processing environment. Our committed RTO is 4 hours and RPO is 1 hour for Priority 1 incidents. Customer notifications are issued within 1 hour of incident declaration via our status page and direct email to named technical contacts.
LAST UPDATED: 2026-02-01
---

ENTRY ID: ENTRY-DATA-001
CATEGORY: Security
RESPONSE TEXT: Customer data is stored in AWS US-East-1 (primary) and AWS US-West-2 (disaster recovery replica). All production ePHI data is processed and stored within the continental United States. International data residency options are not available. Customers requiring US-only data residency do not require additional configuration — US-only storage is the default for all tenants.
LAST UPDATED: 2026-01-15
---

ENTRY ID: ENTRY-DATA-002
CATEGORY: Security
RESPONSE TEXT: Nexus Workflow maintains a formal data retention policy. ePHI is retained for the duration of the active subscription. Upon contract termination, ePHI is purged from production systems within 30 days and from backup systems within 90 days. Customers may request expedited deletion of ePHI via written notice to privacy@nexusworkflow.com; deletion is confirmed in writing within 5 business days of completion.
LAST UPDATED: 2025-11-15
---

ENTRY ID: ENTRY-DATA-003
CATEGORY: Security
RESPONSE TEXT: Nexus Workflow maintains data backup for all ePHI-containing systems with a 4-hour backup frequency. Backups are encrypted at rest using AES-256 and stored in geographically isolated AWS regions. Backup recovery is tested quarterly as part of our disaster recovery program. Backup retention period is 90 days.
LAST UPDATED: 2025-12-20
---

ENTRY ID: ENTRY-ACCESS-001
CATEGORY: Security
RESPONSE TEXT: Nexus Workflow supports SAML 2.0 and OIDC for enterprise SSO. Validated identity provider integrations include Okta, Microsoft Azure Active Directory (Entra ID), Google Workspace, and Ping Identity. SCIM 2.0 user provisioning is supported for Okta and Azure AD. Custom SAML and OIDC configurations are supported for any standard-compliant IdP.
LAST UPDATED: 2026-03-01
---

ENTRY ID: ENTRY-SUPPLY-001
CATEGORY: Compliance/Regulatory
RESPONSE TEXT: Nexus Workflow's subprocessors with potential access to ePHI include: (1) Amazon Web Services — compute, storage, and database infrastructure (BAA executed); (2) Datadog — application performance monitoring (BAA executed); (3) PagerDuty — incident alerting for on-call engineering (BAA executed); (4) Zendesk — customer support ticketing (BAA executed). Customers are notified of subprocessor changes with 30 days' advance notice via email to the named security contact.
LAST UPDATED: 2026-02-28
---

ENTRY ID: ENTRY-COMP-001
CATEGORY: Compliance/Regulatory
RESPONSE TEXT: Nexus Workflow provides HIPAA compliance training to all employees annually. Training covers HIPAA Privacy Rule, Security Rule, and Breach Notification Rule requirements. Training is delivered via our LMS platform with completion tracking. New hires complete HIPAA training within 30 days of joining. Completion records are maintained and available for audit upon request.
LAST UPDATED: 2025-09-15
---

ENTRY ID: ENTRY-DR-001
CATEGORY: Technical Capability
RESPONSE TEXT: Nexus Workflow operates a geographically isolated disaster recovery environment in AWS US-West-2, separate from our primary production environment in AWS US-East-1. The DR environment receives continuous data replication for all ePHI-containing systems. In the event of a primary site failure, automated failover initiates within 15 minutes. Our committed RTO for healthcare-tier customers is 4 hours; RPO is 1 hour.
LAST UPDATED: 2026-01-25
---

ENTRY ID: ENTRY-DR-002
CATEGORY: Technical Capability
RESPONSE TEXT: Our Business Continuity Plan was most recently tested in Q4 2025. The test scenario simulated loss of access to our primary AWS US-East-1 region and validated full failover to US-West-2. Recovery time for critical systems was achieved within the 4-hour RTO commitment. Lessons learned from the test were incorporated into a revised BCP published in January 2026.
LAST UPDATED: 2026-02-10
---

---

## Expected Output Criteria

- [ ] The Requirement Inventory identifies all 28 DDQ requirements, correctly classifying Section A requirements as Compliance/Regulatory (not Security), Section B requirements as Security or Compliance/Regulatory based on content (B.3 encryption is Security; B.1 data residency spans Security and Compliance), and Section C–F requirements appropriately
- [ ] Requirement A.4 (HITRUST CSF certification) is matched to NO MATCH or is explicitly flagged as requiring updated information from the Security team — the content library has no HITRUST entry despite the SC's note that certification was completed 4 months ago; a response drafted from any existing library entry claiming HITRUST certification is a fabrication failure
- [ ] Requirement C.2 (Privileged Access Management) is classified as NO MATCH — no content library entry covers PAM controls; an adapted response from ENTRY-SEC-003 (MFA) that conflates MFA with PAM is a failing output
- [ ] Requirement C.3 (background checks for ePHI-access staff) is classified as NO MATCH — no library entry addresses HR background check policy; routing to Legal/Compliance or HR is correct
- [ ] Requirement B.2 (data classification policy and ePHI labeling) is classified as NO MATCH — ENTRY-DATA-001 covers data residency but does not describe a classification policy or ePHI labeling system
- [ ] Requirement B.5 (DSAR response process and timeline for ePHI) is classified as PARTIAL or NO MATCH — ENTRY-DATA-002 covers data deletion but does not address data subject access requests or response timelines; a DIRECT match from ENTRY-DATA-002 is incorrect
- [ ] Requirement D.1 (vulnerability management SLA for Critical/High CVEs) is matched to ENTRY-SEC-004 as an ADAPT match — the library entry states the pen test was by NCC Group (March 2026) and includes the CVE patching SLAs; the response must use these specific figures verbatim and must not substitute different SLA timeframes
- [ ] The Coordinator Summary prominently flags the DDQ cover page certification requirement — that AI-drafted content cannot be submitted as-is and requires attestation by a named information security officer — as a process constraint the SC must communicate to the review team
- [ ] Critical-priority gaps include at minimum: A.4 (HITRUST — information exists internally but not in library), C.2 (PAM controls), C.3 (background checks), B.2 (data classification), and at least one other; all are routed to the correct owner bucket (Security Team or Legal/Compliance; not Product Management)
- [ ] The gap list for A.4 (HITRUST) specifically notes the distinction between "no certification exists" and "certification exists but is not reflected in the content library" — the SC's context note must inform this characterization, and the gap should be routed to the Security Team to pull the current certification documentation, not treated as a new capability development request

## What failure looks like

A failing output would:
- Draft an affirmative HITRUST response for Requirement A.4 by interpolating from the SOC 2 entry or by citing general knowledge that the company "recently completed HITRUST certification," without a content library entry as the source — this is a fabrication failure that could cause a false compliance claim in a healthcare procurement
- Match Requirement C.2 (Privileged Access Management) to ENTRY-SEC-003 (MFA policy) and draft a response conflating MFA requirements with PAM controls — these are distinct security domains and the conflation would be caught immediately by MWHS's InfoSec team
- Produce a Coordinator Summary that does not mention the human certification requirement from the DDQ cover page, leaving the SC to discover this constraint only when the MWHS contact rejects the submission
- Classify all Section A requirements as Security rather than Compliance/Regulatory, causing HIPAA program questions to be routed to the Security Team instead of Legal/Compliance, delaying the review cycle
- Mark Requirement B.5 (DSAR for ePHI) as DIRECT using ENTRY-DATA-002, because that entry discusses data deletion and privacy@nexusworkflow.com — conflating deletion policy with subject access rights, which are legally distinct HIPAA obligations
- Assign the HITRUST gap (A.4) to Product Management with a note to "build this capability," rather than to the Security Team with a note to retrieve the existing certification documentation that the SC's context confirms already exists
