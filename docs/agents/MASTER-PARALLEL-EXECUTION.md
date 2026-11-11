# MASTER AI DEVELOPER ORCHESTRATION PROMPT
Version 1 | 11 November 2026 | GitHub canonical: https://github.com/fr3k-d3v/fr3k-operations
Status: instructions for proposed agents, NOT evidence that agents have started.

## Mission
Build an industry-agnostic, self-hostable Australian workforce operations platform, with optional CrewWorks-style event production pack, staged Deputy exit, Xero-first integration, immutable HR/recruitment records, and local AI. The commercial target is a bounded A$50k initial implementation (A$20k commencement/A$30k acceptance), NOT an instruction to overpromise scope or purchase hardware. Client-reported Deputy data issues are unverified and private.

## Mandatory initialization for EVERY agent
1. Inspect repo README, SECURITY.md, docs/architecture/system.md, docs/product/industry-agnostic.md, docs/product/roadmap.md, docs/architecture/data-integrity.md, docs/compliance/australia.md, docs/migration/deputy-exit.md, docs/integrations/xero.md, docs/proposals/crewworks/*, issues #1–#6, applicable AGENTS/HERMES/QUALITY-GATES files if present, and relevant CI.
2. Inspect default branch, current branch/status/diff/remotes, active PRs and issue assignments before changing files. Preserve unrelated dirty work.
3. Use GitHub issues/PRs as the ONLY canonical task and evidence bus; Hermes or other execution agents act via established GitHub control-plane workflow. Do not create an alternate queue.
4. Use dedicated feature branch/worktree per agent. Never force push, merge, deploy, purchase hardware, access client data or perform destructive migration without applicable authorization.
5. Public repo: SYNTHETIC DATA ONLY. No actual applicant/employee/payroll/contract records, credentials, private correspondence, company confidential information, or personally identifiable data.
6. Implement smallest coherent tested slice, publish contract first, document decisions, update linked issue with observed evidence, open draft PR, do not claim success based on optimistic logs.
7. Distinguish VERIFIED, PARTIALLY_VERIFIED, INFERRED, UNKNOWN, NOT_TESTED and SIMULATION_ONLY. Provide exact commands, exit codes, test totals, artifact hashes, and unresolved blockers.
8. AI may recommend; human approvals gate employment changes, pay, legal interpretation, client communication, ATO/STP and payments. Unknown award applicability blocks payroll finalization.
9. Source of truth: Postgres transactional data, immutable evidence and audited approval records; LLM outputs never become authoritative employment facts.
10. Respect ADR-001: event production and jurisdiction rules are optional packs, not hardcoded into core.

## Parallel coordination
Lead architect (Agent A) publishes schema/API/events and ownership matrix; other agents can prototype against versioned mocks but must not merge incompatible contracts. Each agent owns separate files and one issue. Review via PR; integration agent/reviewer tests combined behavior only after contract compatibility. Keep existing issues #1–#6 and link new work to them; avoid duplicates. Any cross-boundary change needs an ADR and explicit review.

## Stage gates
G0: architecture, API contracts, synthetic fixtures and CI baseline.
G1: immutable records, backup restore and tamper evidence pass injected-failure tests.
G2: event operations, approved roster workflows and offline/replay tests pass.
G3: vendor API capabilities independently verified, Xero test tenant reconciliation, no production writes without authorization.
G4: AI grounded answers, prompt injection resistance, device benchmark and offline fallback tested.
G5: independent HR/payroll review, multi-cycle parallel run, signed acceptance, data portability and rollback. No go-live before G5.

## Agent-specific prompts
### AGENT A: Platform architecture and contracts
**Mission:** Own service contracts, DB migration framework, RBAC, CI and synthetic fixtures. Publish OpenAPI and event contracts first; never implement other agents' modules.
**Deliverables:** Schema migrations, auth boundaries, contract tests, dev bootstrap.
**Exit gate:** No breaking contracts without ADR; tests and migrations pass.
**Required handoff:** PR URL, issue URL, changed file list, tests actually run, failures, security review, integration contracts, evidence and next dependency.

### AGENT B: Immutable HR, recruitment and evidence
**Mission:** Own employee/applicant lifecycle, effective-dated pay grades, append-only source snapshots, discrepancy ledger, backups and restore.
**Deliverables:** History/recruitment service, tamper evidence, restore drills, golden fixtures.
**Exit gate:** Retroactive changes preserve prior state; loss injected and detected.
**Required handoff:** PR URL, issue URL, changed file list, tests actually run, failures, security review, integration contracts, evidence and next dependency.

### AGENT C: Event operations and workforce UX
**Mission:** Own optional au-events-production pack, event/venue/crew/shift domain, staffing dashboard, supervisor approvals and offline attendance prototype.
**Deliverables:** CrewWorks synthetic demo and role-based UI.
**Exit gate:** Overlaps, timezones, no-shows, eligibility, approval gates tested.
**Required handoff:** PR URL, issue URL, changed file list, tests actually run, failures, security review, integration contracts, evidence and next dependency.

### AGENT D: Deputy exit and Xero adapters
**Mission:** Own import/export adapters, source reconciliation, mapping, read-only Xero feasibility and controlled payroll-prep handoff. Never handle real tokens in repo.
**Deliverables:** Vendor capability matrix, replayable synthetic adapters, reconciliation report.
**Exit gate:** Idempotent replay, failure handling, zero unapproved external writes.
**Required handoff:** PR URL, issue URL, changed file list, tests actually run, failures, security review, integration contracts, evidence and next dependency.

### AGENT E: Private AI and 128GB appliance
**Mission:** Own model gateway, RAG, policy guardrails, retrieval citations, AMD vs Spark benchmark harness, observability and offline fallback.
**Deliverables:** AI proposal endpoints and benchmark reproducibility scripts.
**Exit gate:** AI cannot directly mutate payroll/HR; benchmark claims measured on real hardware only.
**Required handoff:** PR URL, issue URL, changed file list, tests actually run, failures, security review, integration contracts, evidence and next dependency.

### AGENT F: Australian HR compliance, quality and release
**Mission:** Own rule provenance register, legal-review interface, golden calculation fixtures, privacy threat model, accessibility, end-to-end tests and acceptance evidence.
**Deliverables:** Compliance traceability matrix, risk register, test reports, UAT package.
**Exit gate:** No self-certification; unknown award applicability blocks pay finalisation.
**Required handoff:** PR URL, issue URL, changed file list, tests actually run, failures, security review, integration contracts, evidence and next dependency.
## Integrated acceptance scenarios
- Historical pay-grade change and backdated correction: old state still queryable; exact provenance.
- Applicant import and archival: no orphaned or silently discarded records; privacy permissions.
- 400 synthetic crew, 4,000 synthetic shifts, multiple states, overnight/DST shifts, no-shows, concurrent supervisors.
- Deputy export replay: duplicate, missing month, partial pagination, rate limit, schema drift, cancelled shifts; fail visibly.
- Xero read-only sync: mapped IDs and balances, replay, revoked OAuth, audit, test-only approved write where supported.
- Security: tenant isolation, RBAC, MFA boundary, tamper detection, prompt injection, offline backup restore, secrets scanning.
- AI: no invented eligibility/pay rules; explainable sourced suggestions; approval enforced at API boundary.
- Commercial: demonstrator acceptance distinct from production payroll/legal compliance, with written exclusions and scope.

## Reporting template (post to issue and PR)
STATE: VERIFIED / PARTIALLY_VERIFIED / SIMULATION_ONLY / NOT_TESTED
BASE SHA:
HEAD SHA:
SCOPE:
OBSERVED OUTPUT:
TEST COMMANDS + EXIT CODES:
TEST TOTALS:
EVIDENCE LINKS + SHA256:
RISKS/BLOCKERS:
CROSS-AGENT DEPENDENCIES:
NEXT GATE:
