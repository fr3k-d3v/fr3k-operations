# Xero integration strategy
Preferred approach: FR3K owns operational history and approved timesheet/payroll-prep outputs; Xero remains the accounting/payroll and supported ATO/STP workflow boundary where available.

- Verify Xero Australia product features, subscription, API scopes, payroll API eligibility, rate limits, webhooks and terms before implementation: https://developer.xero.com/
- OAuth 2.0 with least-privilege scopes, encrypted token storage and explicit tenant selection; never commit tokens.
- Map employee IDs, earnings rates, leave types, tracking categories, pay calendars and timesheets.
- First implement read-only reconciliation; then staged write to test organisation if permitted; require human approval for production changes.
- Reconcile payroll period, employee count, gross, PAYG, super, leave and journal totals; retain immutable export manifest.
- Super clearing and STP status must be confirmed in Xero/ATO records, not inferred from successful API calls.
- Idempotency keys, retries, backoff, dead-letter queue and alerts for stale syncs.
- Never promise that Xero APIs support every UI workflow. Document verified capability matrix.
