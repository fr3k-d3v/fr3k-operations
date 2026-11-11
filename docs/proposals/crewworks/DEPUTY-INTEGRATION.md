# Deputy-first integration strategy for CrewWorks
Status: User-confirmed 2026-11-11: CrewWorks uses Deputy. Product tier, account owner, API entitlements, integrations, data export, and workflow specifics remain UNKNOWN.

## Decision
Deputy stays authoritative for existing roster, people and timesheet workflows during discovery and pilot. FR3K Operations is an additive intelligence layer; do not promise replacement or bidirectional write access before vendor capability and client authorization are demonstrated. See repo issue #4 for adapter feasibility gates.

## Read-only MVP
1. Obtain client-approved access path (official API, supported export or approved integration). Never request credentials in GitHub.
2. Import synthetic fixtures matching documented fields: employees, locations, rostered shifts, actual timesheets, leave/availability if available, and stable external identifiers.
3. Snapshot source payload hashes, timestamps, timezone, pagination/cursors, mapping versions and reconciliation results.
4. Build coverage dashboard and identify unfilled shifts, overlap conflicts, cancellation risk, location/travel constraints, attendance discrepancies.
5. AI can summarize and propose replacements using deterministic eligibility checks; Amy or authorised manager approves any external communication or roster changes.
6. Reconcile import counts and times against Deputy, handle DST, Australian state time zones, cancelled/deleted shifts, late edits, rate limits, duplicate events, replay and outage recovery.

## Possible later write workflows (subject to verified access)
Crew offer drafts, approved roster changes, approved shift communications, timesheet exception resolution. Every write requires explicit human approval, idempotency, dry-run comparison, audit trail, rollback and least-privilege scoped credentials. No payroll finalisation.

## Thursday discovery prompts
- Which Deputy plan and integrations? Who controls admin/API access?
- How many locations, teams, roles and shifts are managed concurrently?
- Does Amy schedule in Deputy end-to-end, or coordinate changes via SMS/WhatsApp/email?
- Where do event brief, client quote, charge-out, staff documents and EOR obligations live?
- What happens after a no-show? How long to fill and who approves?
- Which payroll/accounting product receives Deputy timesheets? Xero remains UNKNOWN.
- Would read-only shadow analytics for one event be a useful first pilot?

## Acceptance
Client-approved data access; verified vendor terms; no missing records after replay; stable ID mapping; timezone correctness; read-only default; source reconciliation; 100% approval enforcement for writes; no employee data in public repository; tested backup/restore and outage behavior. Document measured baseline before promising ROI.
