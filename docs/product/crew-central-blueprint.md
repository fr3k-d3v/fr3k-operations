# CREW CENTRAL — business requirements crosswalk and implementation blueprint

**Prepared:** 2026-11-11 (Australia/Brisbane)  
**Purpose:** translate the business owner's visual planning model into an implementable, industry-agnostic FR3K Operations product plan.  
**Authority:** this is a design/requirements blueprint, not a claim that every module exists. The source planning workbook is a user-provided Google Sheet and is not reproduced here. This public document deliberately excludes personal names, employee information, private commercial terms and pricing.

## 1. Executive direction

Preserve the owner's information architecture and workflows while building a coherent application, not a literal spreadsheet clone. The workbook establishes a top-level hierarchy of **Parent → Child → Subtopic → Content → Pages**, with two broad domains visible: **Admin & Finance** and **HR**. It includes an explicit recruitment pipeline and a broad business administration catalogue. Projects are not yet designed in the workbook and must remain a co-designed discovery area rather than an invented finished specification.

FR3K should implement a configurable module/page/workflow catalogue over shared business entities, identity, permissions, audit, evidence and integrations. This keeps navigation recognisable to the owner while avoiding duplicated databases and disconnected applications.

## 2. Source-derived business map

The workbook's first tab groups these areas (labels normalised for readability):

| Parent domain | Child area | Subtopics evidenced in the planning model |
|---|---|---|
| Admin & Finance | Brand | Website, brand kit, newsletter, social channels, PR/local media, content calendar and allocations |
| Admin & Finance | Systems | Deputy, Xero, Google Drive, access/login, permissions, SOPs, billing, contacts, applications and integrations |
| Admin & Finance | Company documents | Constitution, registration, shareholders, ASIC, addresses, director details, access and agreements |
| Admin & Finance | Finance | Award wage tables, payroll tax, estimates, state calculators, accounts payable/receivable, BAS, superannuation, wages, reporting, reconciliations and forecasts |
| Admin & Finance | Licensing | State-specific licences, permits, reporting, renewals and login/record references |
| Admin & Finance | Insurance | Workers compensation, public liability, professional indemnity and renewal tracking |
| HR | Database | Deputy/SOP references, employee records, onboarding, payroll, superannuation, ATO, Xero, timesheets, employee advice, documents, expenses and approvals |
| HR | Recruitment | Job descriptions, guidelines/templates, job postings, SOPs, job boards, social media, subscriptions, login, screening, interviews, questions, scoring, evaluation and communications |
| HR | Recruitment lifecycle | Candidate progression and successful/unsuccessful applicant outcomes |

The second tab documents a recruitment sequence: position description intake; check award grade and duties against the proposal; prepare public and full internal job-description variants; configure and publish the job; promote through the website, existing workforce and external job boards; then screen, interview, score and evaluate applicants. This sequence is an initial workflow specification, not proof of current software functionality.

## 3. Current implementation crosswalk (local Omarchy checkout, not the public GitHub code)

**Evidence boundary:** the following was checked against the local development tree at `~/Work/fr3k-operations` on 2026-11-11, including `operations/models.py`, services/workflows/views/API, migrations, templates, tests, `docs/operator/implementation-status.md`, requirements inventory and architecture docs. This code is not thereby present in the public GitHub commit. The public repository must not be represented as containing this unpublished application source.

Status vocabulary: **FOUNDATION** = relevant code exists; **PARTIAL** = only part of the business workflow is implemented; **GAP** = no complete feature found in the inspected tree; **UNKNOWN** = requires further source or live-system verification.

| Business requirement | Local implementation evidence | Assessment / next work |
|---|---|---|
| Shared entities, roles, access | Entity and membership models, scoped access, role/action matrix, immutable membership-change evidence, throttled login | FOUNDATION. Complete field-level policy, MFA/SSO, named access reviews and independent security review. |
| Historical business records | Versioned immutable `Record`, typed payload contracts, audit events, entity-local references | FOUNDATION. Define formal domain entities and validated relationships for each module. |
| Imports and source preservation | Encrypted import batches/ciphertext versions, replay, promotion, reconciliation and API redaction | FOUNDATION. Add off-host encrypted evidence custody, retention and source completeness proofs. |
| Approval and decision history | Immutable decisions and workflow services | FOUNDATION. Add domain-specific approval matrices, delegation and escalation. |
| Job orchestration | Durable jobs/events/lineage, leases, fencing, bounded retries and immutable terminal states | FOUNDATION. Reuse as shared workflow execution, not as a substitute for business-specific process models. |
| Recruitment and applicant lifecycle | Generic records and workflow foundations; no complete applicant pipeline/UI identified | GAP. Build candidate, vacancy, screening, interview, evaluation and offer lifecycle. |
| Employee lifecycle | Generic records and HR workflow foundation | PARTIAL. Define employee, engagement, contract, classification and lifecycle events with effective dates. |
| Leave | Submission, independent approval, overlap checks, cancellation as a superseding version, views and tests | FOUNDATION. Complete balances/accruals, evidence, policy configuration and end-to-end lifecycle. |
| Rostering and scheduling | Foundational shift/leave records, overlap checks, approved roster views | PARTIAL. Add availability, qualifications, fatigue/working-time constraints, assignment and change notifications. |
| Timesheets | Immutable manifests, approved-hours reconciliation and controlled export queue | FOUNDATION. Complete capture, supervisor correction, exceptions, project/job costing and pay-period close. |
| Payroll calculations | Versioned rule manifests, pinned runs, decimal traces, historical reproduction, explicit-input tax scenarios | PARTIAL. No production legal rule packs or payroll finalisation; independent award/PAYG/super/leave fixtures and signoff remain blocked. |
| Xero | OAuth vault, consent/state validation, tenant selection, GET-only Accounting transport, timesheet reconciliation and guarded draft staging | PARTIAL. Live tenant, scopes, eligibility, mappings and end-to-end reconciliation remain unverified. |
| Finance/admin | Calculation scenarios and supporting records | PARTIAL/GAP. Build accounts payable/receivable workflow, budget controls, management reporting and forecasts only after source requirements are defined. |
| Licensing and insurance | No complete lifecycle modules identified | GAP. Add registers, entities/locations, responsible owners, effective dates, renewals, evidence and escalation. |
| Company documents and SOPs | Generic versioned records and encrypted imports | PARTIAL. Add document types, version approval, obligations, access classes and renewal/review workflows. |
| Brand and communications | Generic jobs/alerts and SMTP adapter | GAP. Add content calendar, approval, channel-specific publishing adapters and campaign reporting; keep optional to core workforce operations. |
| Projects | No complete project-management domain/UI identified | GAP / DISCOVERY. Design jointly; see section 6. |

### Verification note

The local implementation-status report records a full PostgreSQL suite of **118 tests** and a focused SQLite UI suite of **12 tests** passing on 2026-11-11. These are local reported results, not independently reproduced in this public repository or public CI. The same report says there has been no live Deputy/Xero interaction, production deployment, payroll finalisation or independent compliance verification. See the local status report for its full scope and limitations; do not convert test counts into a production-readiness claim.

## 4. Target application architecture

### 4.1 Navigation and configuration

Represent the workbook hierarchy as configuration:

- **Module**: top-level domain, e.g. Admin & Finance, HR, Projects.
- **Section**: child area, e.g. Recruitment, Finance, Licensing.
- **Capability**: a bounded business function, e.g. vacancy management or licence register.
- **Page**: role-aware view over one or more capabilities.
- **Workflow**: versioned state machine with explicit transitions, owners, deadlines, evidence and approvals.
- **Content asset**: SOP, template, policy, form, guide or controlled document.

The navigation tree is not the data model. Pages may present multiple related entities; one entity may appear in multiple role-specific pages. Admins can configure labels/order/visibility without changing core schema. Keep stable internal identifiers separate from display labels.

### 4.2 Shared platform services

All modules use shared tenant/entity boundaries, people and organisations, locations, identity/roles, effective-dated records, document/evidence storage, audit history, notifications, workflow jobs, search, reporting and integration adapters. Every important action records actor, authority, before/after version, timestamp, reason and evidence reference.

### 4.3 Role-specific experiences

- **Owner/executive:** whole-business exceptions, cash/labour exposure, compliance deadlines and approvals.
- **Administrator/finance:** entity setup, finance records, integrations, reconciliation and reporting.
- **HR/recruiter:** applicants, offers, employee files, onboarding, leave and HR exceptions.
- **Supervisor/crew leader:** crew allocation, availability, rosters, time capture, approvals and project progress.
- **Worker:** own profile, documents, availability, roster, leave, timesheets and notifications.
- **Auditor/adviser:** explicitly scoped read-only evidence and history.

These are proposed personas; final role boundaries require owner approval and field-level security tests.

## 5. Recruitment and employee lifecycle specification

### 5.1 Vacancy-to-hire workflow

1. Client/job request and vacancy approval.
2. Position description intake and versioning.
3. Award/instrument and classification review by an authorised human; record the source, effective date and rationale. Never let an AI infer binding coverage unaided.
4. Generate two linked artefacts: public job advertisement and full internal position description/crew agreement attachment.
5. Configure location, proposed rate reference, screening questions and publishing approvals.
6. Publish through approved website/job-board adapters; track external posting IDs and sync status.
7. Candidate application and consent/privacy notice; deduplicate carefully without destructive merges.
8. Screening, interview scheduling, structured questions and evidence-based scoring.
9. Human decision, reason, conflict-of-interest declaration and candidate communication.
10. Offer, acceptance, pre-employment checks and conversion to an employee/engagement record.
11. Onboarding tasks: identity/right-to-work evidence, contracts, qualifications, inductions, licences, emergency contacts and payroll setup, with strict access and retention controls.

### 5.2 Candidate state model

`DRAFT → APPROVED → PUBLISHED → APPLICATION_RECEIVED → SCREENING → INTERVIEW → EVALUATION → OFFER → ACCEPTED → ONBOARDING → HIRED`

Alternative terminal/holding states: `WITHDRAWN`, `UNSUCCESSFUL`, `ON_HOLD`, `EXPIRED`. Every transition requires an authorised actor, timestamp and reason. Candidate rejection and employment decisions remain human-authorised; AI may summarise or suggest but cannot autonomously decide.

### 5.3 Employee lifecycle

`PREBOARDING → ACTIVE → LEAVE_OR_SUSPENDED (where applicable) → EXITING → SEPARATED → ARCHIVED`

Use effective-dated employment engagements, contracts, locations, instruments, classifications, rates, qualifications and reporting lines. Corrections create superseding versions. Keep candidate, person and employee identities related but distinct; a person can have multiple engagements and a candidate can reapply.

## 6. Projects — discovery-first design

Projects are explicitly not yet specified in the source workbook. Do not assume a generic kanban board is sufficient. Start with a discovery workshop and synthetic workflow prototype. Candidate domain concepts:

- Client/customer and contract/work order.
- Project/job, site/location, cost centre and budget baseline/revisions.
- Work package, task, dependency, milestone and deliverable.
- Crew/role/qualification requirement and assignment.
- Planned versus actual labour hours, timesheets and approved expenses.
- Materials/equipment/subcontractor commitments (optional industry extensions).
- Risks, issues, variations, approvals, site instructions and evidence.
- Progress reporting, forecast final cost, margin and schedule variance.

### Proposed project lifecycle (hypothesis, validate with owner)

`OPPORTUNITY → ESTIMATE → PROPOSED → APPROVED → MOBILISATION → ACTIVE → ON_HOLD (optional) → PRACTICAL_COMPLETION → FINANCIAL_CLOSE → ARCHIVED`

A project must link to the same workforce, roster, timesheet, leave, qualification, document, finance and audit records. Labour costing should use the approved rate/rule version effective at the work date and distinguish estimate, commitment, actual and forecast. Never silently rewrite historical budgets or timesheets; use approved revisions and adjustment records.

### Discovery questions

1. Is a project primarily a client contract, a job/work order, an internal initiative, or a hierarchy of all three?
2. Can one worker split a shift across multiple jobs/sites/cost codes?
3. What are the required project states, approval gates and variation rules?
4. Which roles create/approve budgets, assignments, timesheets, expenses and completion?
5. What does the owner need daily: crew status, schedule, labour cost, margin, progress, risk or client reporting?
6. Which artefacts are mandatory: SWMS/JSA, permits, inductions, drawings, site diaries, photos, QA and handover packs?
7. Are materials, plant, subcontractors and purchase orders in scope for the first release?
8. What external systems must exchange job, cost code and actuals data?

## 7. Finance, compliance and evidence controls

- Finance functions must separate estimates, approved commitments, actuals, accruals and forecasts.
- Payroll preparation is not payroll finalisation. No bank payment, ATO/STP lodgement or unattended pay run is in scope without separate legal, operational and human approval.
- Award, agreement, tax, superannuation and leave rules must be versioned, effective-dated, traceable to authoritative sources and validated by qualified reviewers.
- State-specific licences/insurance require owner, entity/site scope, issuer, reference, issue/expiry dates, renewal evidence and escalation; never store passwords in free-text notes.
- Company documents and SOPs need version, owner, reviewer, approval/effective date, supersession, audience and retention class.
- Keep private employee, applicant, payroll, company and vendor data out of public GitHub. Public fixtures must be synthetic and non-identifying.

## 8. AI agent operating model

AI agents may search, summarise, draft, compare, classify with confidence labels, identify missing evidence and propose workflow actions. They must not make final hiring/rejection decisions, change pay or employment conditions, approve timesheets/payroll, issue payments, lodge statutory returns, or alter source records without the designated human authority.

Expose typed, tenant-scoped tools with read/write scopes, policy checks, idempotency keys, stable job IDs, approval leases, audit evidence and bounded retries. Default to read-only. Clearly distinguish CLAIM, OBSERVATION, EVIDENCE, VERIFIED FACT, HYPOTHESIS, SIMULATION and UNKNOWN. A model response is not an audit record or legal determination.

## 9. Delivery plan and acceptance gates

| Phase | Deliverables | Exit criteria |
|---|---|---|
| A — Validate requirements | Confirm workbook hierarchy, roles, entities, jurisdictions, instruments, current system exports and owner priorities | Signed requirements baseline; private evidence register; unresolved items explicitly UNKNOWN/BLOCKED |
| B — Navigation and shared shell | Configurable module tree, role-aware dashboard, page registry, search, notifications and document library | Owner validates navigation prototype; permission tests pass; keyboard/mobile usability reviewed |
| C — HR/recruitment | Vacancy, candidate pipeline, structured evaluation, offer, onboarding and employee lifecycle | Synthetic end-to-end tests; immutable decision history; human-only hiring decisions; retention/access review |
| D — Workforce operations | Availability, qualifications, roster, leave, time capture, approvals and job costing dimensions | Cross-module workflow tests; no overlapping/invalid assignments; corrections preserve history |
| E — Admin/compliance/finance | Company register, documents/SOPs, licensing, insurance, finance registers and forecasts | Renewal/escalation tests; reconciled finance definitions; evidence ownership and permissions signed off |
| F — Projects discovery and pilot | Owner-approved project domain, job hierarchy, work packages, labour budget, progress and variation prototype | Discovery decisions documented; synthetic project scenario reconciles roster → timesheet → cost → forecast |
| G — Integrations and controlled pilot | Deputy preservation/import, Xero read/reconciliation and explicitly approved staging | Real authorised test tenant evidence, mapping approval, parallel reconciliation, rollback and recovery drill |
| H — Production readiness | Independent security/privacy/accessibility/legal review, monitoring, retention, backup/PITR and support | Named signoffs, measured recovery, incident drill, no unresolved critical/high blockers and written cutover authority |

Definition of done for each capability: source code + automated tests + synthetic fixtures + raw evidence + reproducible verification + operator documentation + named acceptance. A commit is not deployment; a passing test suite is not legal compliance; mocked integration is not live integration.

## 10. Immediate engineering backlog

1. Create a formal requirements traceability matrix mapping each workbook node to module, entity, page, workflow, permission, evidence and acceptance test.
2. Implement the module/page registry and role-aware navigation without encoding the spreadsheet's repeated display columns into database tables.
3. Add first-class Applicant, Vacancy, Interview, Evaluation and Offer domain records/workflows.
4. Define Person, Employee and EmploymentEngagement relationships and effective-dated contract/classification/rate records.
5. Prototype the recruitment pipeline with synthetic candidates and owner review.
6. Add qualification/licence and document expiry registers with evidence-backed reminders.
7. Run a Projects discovery workshop; do not implement a generic project board until the domain questions are answered.
8. Extend cross-module integration tests from recruitment/onboarding through roster → approved timesheet → project cost → finance forecast.
9. Refresh public documentation only with sanitised, accurate status; publish application source separately after explicit approval and secret/privacy review.

## 11. Known limits and source integrity

This blueprint was derived from the owner-provided planning workbook and a local code/document inventory on 2026-11-11. The workbook contains operational labels and internal structure; personal names and private values have intentionally been omitted. No changes were made to the workbook. The local code inventory is not a public GitHub release. The workbook does not yet define Projects. The plan is therefore a structured proposal and crosswalk, not a final signed specification or proof of completed features.
