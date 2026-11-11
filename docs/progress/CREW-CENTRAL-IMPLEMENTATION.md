# CREW CENTRAL implementation progress

Updated: 2026-11-11.

## Source and publication boundary

The owner has requested that this public repository carry documentation and
verification summaries, with application code in a separate private repository.
The private application repository is created and its visibility verified:
`fr3k-d3v/fr3k-operations-app`. The baseline source commit is `2cd3052`; the project-costing increment is
`32fddfc`.
Application source has not been published here. Earlier public snapshots remain dated developer observations.

The local starting application is based on research commit
`f8b0739`, with unpublished Django source and migrations through 0021.
The public documentation baseline is `826db1f45407b3cc3b532166103db136a4f53413`.
Before editing, the local tracked changes and untracked source were preserved in
a checksummed archive. Existing changes are being retained.

## Delivery sequence

1. Reproducible private application baseline: clean startup, migrations,
   synthetic fixtures, automated PostgreSQL and browser verification.
2. Shared identity, permissions, approvals, evidence, notifications and recovery.
3. Recruitment, employment, scheduling, time, leave and payroll preparation.
4. Clients, projects/jobs, tasks, budgets, costing, registers and finance.
5. Independently validated rules, source migration and reconciled Xero handoff.
6. Optional grounded AI, independent reviews, pilot and controlled production.

## Current verification

The private baseline at `2cd3052` was verified locally on 2026-11-11:

- PostgreSQL 18.6: 118 Django tests passed, with no skips.
- Three standalone export-inspector tests passed.
- Migration drift check and OpenAPI validation passed.
- Chromium: worker leave submission, separate reviewer approval, mobile layout,
  and HR retry/replacement of approved synthetic export jobs passed with no page
  errors.
- SQLite smoke: 118 tests passed with five PostgreSQL-specific tests skipped.

At private commit `32fddfc`, project costing adds clients, milestones, reviewed
project budgets, dated-rate work allocations across jobs, approved expenses and
commitments, and immutable cost/forecast snapshots preserving all selected source
versions. Allocations reconcile every date/rate to the approved timesheet.
Duplicate approved allocations and stale corrected sources are blocked.
The job-cost report remains operational base labour costing; payroll on-costs,
tax, full source completeness and accounting reconciliation are not claimed.

The expanded local verification passed 131 PostgreSQL tests (no skips), three
standalone tests, migration drift and OpenAPI validation, and two Chromium
journeys including roster → timesheet → split allocation → saved cost report.
Desktop/mobile checks passed with no page errors. Runtime dependency scanning
reported no known vulnerabilities. The corrected Bandit scan covered 5,607 lines
with no skipped files and no medium/high findings; 38 low notices remain for
review. The earlier baseline CI scan invocation scanned no files; it has been
corrected and is not relied on as static-analysis evidence.

Private baseline hosted CI run `43015213006` passed application/browser checks.
Hosted CI run `43016402929` passed both the expanded application job and the
clean Docker Compose startup job for private commit `32fddfc`.

The recruitment increment at private commit `cdb5f6e` adds separate vacancy and
application histories, interviews, evaluations, offers, onboarding and separation
records. An approved accepted offer prepares linked employment drafts once;
separate reviewers must approve the engagement, contract and rate and completed
onboarding before a hired application can be approved. Candidate identity and
earlier application versions are retained. Changed offers block silent rewrites.
This does not automate employment decisions, account provisioning, final pay or
notifications.

Local verification passed 142 PostgreSQL tests (no skips), three standalone
tests, migration drift and OpenAPI checks, runtime dependency scanning and the
corrected static scan (5,863 lines, no skipped files, no medium/high findings).
Three Chromium journeys passed, including accepted offer → reviewed onboarding →
hired application → approved first timesheet → payroll-preparation export.
Recruitment hosted CI run `43017095832` passed.

The workforce increment at private commit `4fc98cf` adds reviewed availability,
qualification/expiry checks, optional shift engagement requirements, server-time
mobile capture with replay-safe commands, preparation of dated timesheet drafts
from reviewed clock/break events, immutable corrections and reviewed period
closure. Closing rechecks source IDs/hours, pending events, overlapping periods
and stale drafts, then blocks later time changes. Existing legacy shifts without
configured eligibility requirements remain supported and do not establish full
workforce eligibility. Legal paid-time rounding, leave balances, disputes and
closed-period adjustments still require further work and acceptance.

The local full run passed 155 PostgreSQL tests without skips, three standalone
tests, migration drift/OpenAPI validation, runtime vulnerability and actual
static-analysis scans, plus all three Chromium journeys and mobile clock in/out.
Workforce hosted CI is pending.

The baseline adds automatic migration/seed ordering in development Compose and a
single verification command. CI is configured for PostgreSQL 17, browser checks,
dependency scanning and static analysis; hosted CI status and a clean Docker
build are still being checked. Local verification is developer evidence,
not independent acceptance. No production, live payroll or live Xero claim is
made.

## Open release gates

Client-specific applicability and access policy, independent calculation review,
two reconciled parallel payroll periods, security/privacy/accessibility review,
off-host recovery, named operational acceptance and written cutover authority
remain open. Synthetic implementation work may proceed; dependent production
capabilities remain disabled until their evidence and approvals are recorded.
