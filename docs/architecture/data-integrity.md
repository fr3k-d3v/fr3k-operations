# No silent data loss
- Immutable raw imports with source, collection timestamp, SHA-256, counts and custody.
- Versioned effective-dated pay grades, awards, applicants, contracts and employee changes.
- Daily encrypted off-host backups plus point-in-time recovery; periodic restore drills and measured RPO/RTO.
- Change data capture or outbox for reliable downstream delivery; idempotent sync with cursors and replay.
- Reconcile record counts, pay totals, missing periods, orphaned applicants, grade histories and external identifiers.
- Missing source data is a BLOCKER, never filled by model-generated guesses.
- Audit trail includes actor, authority, reason, before/after hashes and approval evidence.
- Export in documented open formats; no single SaaS should own the only recoverable copy.
