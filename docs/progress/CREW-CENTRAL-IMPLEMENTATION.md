# CREW CENTRAL implementation progress

Updated: 2026-11-11.

## Source and publication boundary

The owner has requested that this public repository carry documentation and
verification summaries, with application code in a separate private repository.
The private application repository is created and its visibility verified:
`fr3k-d3v/fr3k-operations-app`. The first source commit is `2cd3052`.
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
