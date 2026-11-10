# Delivery plan / acceptance gates
## P0 — Evidence and requirements
- Inventory awards, agreements, states, entities, roles, payroll cycles and Xero capabilities.
- Preserve Deputy contract and complete exports; gap report.
- Confirm external open-source candidates and licences.

## P1 — Safe operational foundation
- Auth/RBAC, Postgres schema, append-only events, audit and backup/restore.
- Employee/applicant historical imports and data reconciliation.
- Tasks/projects, roster and timesheet read-only views.

## P2 — Calculation laboratory
- Effective-dated award/rule registry, explainable calculation trace, payroll-tax scenario engine.
- Synthetic fixtures, independently checked golden tests, exception queue.
- Xero read-only reconciliation.

## P3 — Controlled workflows
- Approvals, roster editing, leave, payroll-prep export, Xero staging integration.
- Parallel pay runs and human accountant/HR signoff.

## P4 — Cutover readiness
- Security/privacy review, accessibility, incident recovery drills, record retention, independent payroll verification.
- Written cutover and rollback plan; no production go-live without evidence.

Definition of done: code + tests + raw evidence + reproducible verification + documented operator signoff. GitHub is public system of record for non-sensitive design/code; private evidence remains private.
