# CREW CENTRAL implementation progress

Updated: 2026-11-11.

## Source and publication boundary

At the owner's direction, this public repository carries requirements,
documentation and verification summaries. Application code is in the separately
created private `fr3k-d3v/fr3k-operations-app` repository; PRIVATE visibility was
checked before every push. No application source or business records were
published here.

The original local tracked changes and untracked application were preserved in
a checksummed archive before editing. The private source begins with a fresh
history from research commit `f8b0739` plus existing unpublished Django work
through migration 0021. Public documentation baseline:
`826db1f45407b3cc3b532166103db136a4f53413`. The original checkout remains intact.

## Delivered private increments

| Commit | Implemented and developer-verified |
|---|---|
| `2cd3052` | Reproducible baseline, automatic development migration/seed ordering, disabled-login synthetic fixtures and one-command verification |
| `32fddfc` | Clients/milestones, reviewed budgets, exact dated-rate work allocation across jobs, expenses/commitments and immutable source-preserving cost forecasts |
| `cdb5f6e` | Separate vacancy/application histories, interviews/evaluations/offers, replay-safe employment draft preparation, reviewed onboarding and separation records |
| `4fc98cf` | Reviewed availability/qualifications, configured engagement/shift eligibility, server-time mobile capture, reviewed attendance preparation and immutable period close |
| `cf6e2ca` | Encrypted controlled documents, independently approved internal publication, company/licence/insurance/obligation registers and accountable renewal queue |
| `2043556` | Owner/finance/supervisor roles, access-review listing, modular workspace/search, assigned/delegated reviews and a complete application-table restore drill |
| `fc7876a` | Reviewed manual leave balances, budget variations, invoice/close controls, time disputes, versioned event contract and enforced production acceptance gates |
| `d48393a` | Reserved server-capture command references and authenticated immutable replay receipts |

Cost reports cover operational base hourly labour and expenses; payroll
on-costs, tax and accounting reconciliation are excluded. Recruitment preparation
creates drafts for separate human review. Legacy shifts without configured
eligibility requirements remain supported and are not proof of full eligibility.
Period close freezes approved time, with separately reviewed closed-period
adjustments still to be designed. Register escalation is an in-app owner queue,
not verified external notification delivery.

Document uploads use bounded memory and independent versioned encryption keys.
Workers receive current approved internal documents only; changing the approved
audience removes prior internal publication. Retention classes are metadata;
retention schedules, key rotation, malware scanning and off-host custody remain
acceptance work.

## Current verification

At private commit `d48393a`, local PostgreSQL 18.6 verification passed:

- 195 Django tests, no skips, plus four standalone export-inspector tests.
- Migration drift check and warning-free validated OpenAPI.
- Four Chromium journeys with no page errors: leave/review and delivery recovery;
  roster → timesheet → split-job cost forecast; accepted offer → reviewed
  onboarding → hired application → approved work → payroll-preparation export;
  encrypted document upload → independent publication → worker download.
- Desktop/mobile checks, including mobile time capture and document library.
- Runtime dependency scan: no known vulnerabilities.
- Bandit: 7,802 lines scanned, no skipped files or medium/high findings; 46 low
  notices remain for review. The baseline CI scan initially scanned no files
  because of an incorrect path argument; it was corrected and is not relied on.

Private hosted CI includes both full application/browser/security checks and a
fresh Docker Compose build/startup with migrations, idempotent seed and reachable
login. Runs `43016402929` (projects) and `43017095832` (recruitment) passed.
Run `43025348286` passed application and clean Compose/recovery checks for `fc7876a`. Run `43026318548` passed **both application and clean Compose/recovery jobs**
for final private source `d48393a1302f1d48a220d2a184f835b8d6752bd8`.
[View private CI evidence](https://github.com/fr3k-d3v/fr3k-operations-app/actions/runs/43026318548).

The isolated PostgreSQL restore drill now compares counts and complete serialized
data digests for all 27 operations models, including encrypted evidence, approved
cost inputs and outstanding assignments. All 46 triggers across 23 immutable
tables restored, mutation was rejected and the document decrypted with its key
kept outside the dump. The final 155,301-byte synthetic dump took 0.037 seconds to dump
and 0.053 seconds to restore. These tiny local timings are not production RTO/RPO
or off-host/PITR evidence.

These are developer-run synthetic checks, not independent acceptance, payroll
certification, production deployment or live Xero evidence.

## Milestones and remaining gates

[Six delivery milestones](DELIVERY-MILESTONES.md) consolidate the original
overlapping issues. Their unresolved acceptance criteria remain open; draft
PR #7 remains research rather than implementation acceptance.

The full application plan remains in progress. Actual approved field policy, supported MFA identity, verified external notification delivery,
independently accepted opening balances and legal accrual/rule packs, actual
Xero/accounting read reconciliation, source completeness, live tenant/mapping evidence, two accepted
parallel payroll periods, off-host recovery and independent reviews remain
unfinished. The owner will advise the identity provider and approved recovery targets later.
Production HTTP and production Xero staging are blocked in code by explicit
activation and current-revision, independently approved evidence gates. No real
acceptance record has been created. Production still requires named operational
acceptance and written cutover authority. No live payroll, vendor-write activation or cutover is claimed.
