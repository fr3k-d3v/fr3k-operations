# Client discovery update: Deputy exit, historical integrity, Xero-first
Status: CLIENT-REPORTED REQUIREMENTS, 11 November 2026. Paraphrased to protect private correspondence. Reports are not independently verified, and do not establish breach of contract.

## Reported needs
- Client wishes to investigate exiting Deputy contract, citing reported data-loss incidents and support dissatisfaction. Contract rights and terms UNKNOWN.
- Reports historical pay-grade/classification information sometimes requires re-entry, applicant records can go missing, and data can be temporarily unavailable.
- Values Deputy's inclusive, thoughtful HR workflows and cross-module data reuse; replacement must retain those strengths, not merely duplicate a roster.
- HR compliance and dependable audit evidence are overriding requirements.
- Prefers Xero as payroll/accounting and supported ATO/STP interface rather than relying on Deputy integrations; Xero product, subscription, API and actual supported tax/super workflows must be verified.

## Revised product priorities
P0 preservation and forensic reconciliation: collect approved complete exports, identify gaps by employee/applicant/period, source hash, timestamp, historical classification/rate version; independent immutable snapshots and restore evidence. Missing data BLOCKED, never guessed.
P1 HR lifecycle and recruitment: applicant pipeline, archived applicants, employment engagement, contracts, onboarding, award/classification versioning, consent and permissions, records retention.
P2 workforce operations: event crew pools, multi-site rostering, shift offers/replacements, mobile attendance, supervisor approvals, fatigue/credential checks.
P3 Xero-first payroll preparation: controlled timesheet export and read-only reconciliation, OAuth and API entitlement verification, explicit human approvals. Xero remains source for actual payroll, STP and super workflows only to extent verified.
P4 audited transition: parallel operation and payroll comparison over multiple periods, legally reviewed termination strategy, written rollback and export plan, independent Australian employment/payroll review.

## Critical nonfunctional requirements
- No silent loss of approved records, tamper-evident audit, append-only import history, effective-dated supersession, encrypted off-host backups, point-in-time recovery, independently measured restore RPO/RTO.
- Accessibility and inclusive UX; least-privilege RBAC, applicant privacy and retention, tenant isolation, source provenance, portable exports.
- Explicit discrepancy queue, notifications and fail-closed calculation gates.
- No production payroll finalisation, ATO submissions or automated employment decisions by AI.

## Thursday 12 Nov decision interview
1. Deputy contract renewal/notice date and exact data export rights? Preserve evidence before any termination.
2. Which pay-grade history and applicant data were lost, and when? Are vendor incident records and exports available?
3. Which Deputy features does the team most value and must not lose?
4. Which Xero products/features are enabled, and who owns payroll/ATO/super approvals?
5. Which awards, enterprise agreements, employing entities, states, EOR arrangements and HR advisors are involved?
6. Which first workflow would demonstrate value without risking payroll: historic-data integrity, applicant tracking, or replacement shifts?
7. Who will approve acceptance, migration and operational signoff? Include head of operations.

## Commercial scope control
A$20k/A$30k are target milestones, not yet validated implementation prices. Full replacement of Deputy + compliant Australian HR/payroll + migration may exceed A$50k; define explicit MVP, phase gates and separately priced expansion. Do not represent data recovery as guaranteed if source records no longer exist. Offer independent records custody and robust reconciliation, not absolute zero-data-loss promises.

## Traceability
Read docs/migration/deputy-exit.md, docs/architecture/data-integrity.md, docs/integrations/xero.md, docs/compliance/australia.md, issues #1–#6. No private messages, names, credentials, contract terms or employee data should be committed to this public repo.
