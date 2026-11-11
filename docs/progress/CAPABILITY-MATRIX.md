# CREW CENTRAL capability and acceptance matrix

Updated 2026-11-11. Source: private application commit `ec94886`. This public
page summarizes developer evidence; inspecting/reproducing the source requires
private-repository access. Passing CI is not independent business acceptance.

| Capability | Current implementation | Verification | Remaining acceptance |
|---|---|---|---|
| Connected web workspace | Live overview, company/module navigation, record search/form actions, owner settings and access review | Dashboard role/isolation tests and full web browser journey | Independent accessibility and operator acceptance; production hosting remains gated |\n| Reproducible application | Clean Docker initialization, synthetic seed, pinned runtime dependencies and one-command checks | PostgreSQL, OpenAPI, migration, browser/security and clean Compose CI | Independent operator install review |
| Identity and access | Owner/admin/finance/HR/supervisor/worker/auditor plus legacy manager; tenant isolation; access review; modular workspace | Role/action matrix and cross-entity tests | Approved provider/MFA, actual role/field policy and provisioning review |
| Shared review | Independent decisions, assigned reviewers, delegation, deadlines and in-app queues | Assignment, replay, immutable history and authorization tests | Verified external notification delivery and escalation process |
| Recruitment | Vacancies, applications, interviews/evaluations/offers, linked draft employment, onboarding and separation records | Recruitment-to-approved-work browser journey | Real HR acceptance, employment/classification applicability and broader contract variants |
| Workforce | Configured qualification/availability/engagement checks, roster review, mobile capture and dated preparation | Overnight, expiry/revocation, replay and ownership tests | Complete real requirement policy and independently accepted paid-time rules |
| Time and disputes | Reviewed corrections, source-bound disputes and period closure | Source movement/ownership bypass and stale-close tests | Reviewed closed-period adjustments and real payroll-period acceptance |
| Leave | Reviewed manual ledger, policy binding, reservations and cancellations | Ledger/source uniqueness, balance and access tests | Independent source balances and jurisdiction/instrument accrual packs |
| Projects and finance | Clients/jobs/tasks/milestones, approved budgets/variations, exact hour allocations, immutable forecasts, invoice references and close | Project-cost browser journey and financial controls tests | Live invoice/accounting reconciliation and business acceptance |
| Administration/evidence | Encrypted uploads, approved audiences, controlled versions, company/licence/insurance/obligation registers and owner queues | Upload/publication/download browser journey and isolation tests | Retention schedule, malware scanning, key rotation, off-host custody and delivery escalation |
| Migration/calculations/Xero | Existing preserved import/reconciliation engine, versioned synthetic calculation packs, read transport and gated draft staging | Mocked transport/retry/conflict tests | Actual applicability, exports, tenant/scopes/mappings and two accepted parallel periods |
| Recovery | Complete application-table digest comparison, restored triggers, rejected mutation and evidence decryption | Real disposable PostgreSQL dump/restore plus CI rehearsal | Off-host/PITR, representative volumes, approved RPO/RTO and operator drill |
| Production | Explicit activation and independently approved evidence gates; HTTP/vendor writes blocked while unaccepted | Missing/expired/withdrawn/revision mismatch and production-blocking tests | All named release signoffs, monitored deployment, pilot and written cutover |
| Optional AI/brand extensions | Deferred; permission-filtered ordinary search exists | No released AI generation or automated publishing claim | Separate optional implementation/acceptance |

Current local checks passed **203 PostgreSQL tests without skips, four standalone
tests and five Chromium journeys**, plus migration/OpenAPI, vulnerability and
static checks. See the [progress page](CREW-CENTRAL-IMPLEMENTATION.md) for hosted
CI state and source increments, and [delivery milestones](DELIVERY-MILESTONES.md)
for issue ownership.

The owner will advise the identity provider and recovery targets later.
Production remains disabled. No actual acceptance gate, live payroll,
independently certified calculation or production cutover is claimed.
