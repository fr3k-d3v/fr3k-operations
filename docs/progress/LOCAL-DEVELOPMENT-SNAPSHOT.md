# FR3K Operations — unpublished development progress

**Snapshot date:** 2026-11-11 (AEST). **Evidence classification:** locally observed file inventory + developer-reported tests. **Publication scope:** this document only; application code and test artefacts remain on Omarchy and are not part of the public repository. **Release state:** development pilot, not production-ready or compliance-certified.

## Observed implementation in the separate Omarchy development checkout

The working tree at `~/Work/fr3k-operations` contains a Django/PostgreSQL application, 17 sequential database migrations, models/services/API, authentication and entity membership, versioned operational records, audit history, staged encrypted imports, backup/restore commands, approval workflows, leave and roster views, immutable timesheet manifests, delivery queue with leases/fencing/retries, calculation rule manifests and historical reproduction, payroll-tax scenarios, and Xero OAuth/GET-only Accounting transport. It also contains Docker/Compose scaffolding, templates, tests, operator instructions and synthetic browser screenshots.

These features are **observed as local source files**, not independently validated as deployed capabilities. Project/task management and end-to-end payroll remain roadmap areas; do not infer their completeness from the general platform description.

## Developer-reported verification (not independently rerun for this snapshot)

The local implementation-status report records 96 PostgreSQL tests passing, 11 SQLite UI tests passing, and a Chromium acceptance flow covering leave submission/approval and synthetic delivery-queue interactions. It records use of an isolated PostgreSQL 17.6 instance because Docker execution was unavailable to the local account. No public CI run or independently reproduced test log is available in this public repository. Treat all counts as **CLAIM**, not independent verification.

## Known unverified or blocked gates

- No production deployment, real Deputy export reconciliation, or live Xero tenant/accounting/payroll validation.
- No verified award/PAYG/super/leave statutory calculation pack, payroll signoff, ATO/STP integration or payroll finalisation.
- No completed independent privacy, security, accessibility, retention or licence review; no proven production backup/PITR and recovery rehearsal.
- No client-specific requirements assessment, data migration completeness proof or written cutover authorisation.
- No evidence that local source is available in this public GitHub commit. Public agents must not cite this snapshot as proof of publicly inspectable code.

## Independent evaluation instructions

Agents should distinguish (1) published architecture and research, (2) locally observed but unpublished implementation, (3) developer-reported test outcomes, and (4) verified production capability. For reproducible source inspection and tests, request a separately authorised release or supervised demo using synthetic data. Never request real employee records or credentials through a public repository.

Next gates: complete and preserve test evidence; review the source for privacy/security and licensing; publish a sanitised implementation only after explicit approval; run public CI; independently validate legal rules and integration access; complete controlled pilot and recovery testing.
