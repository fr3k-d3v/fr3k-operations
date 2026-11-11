# Workstream ownership and sequencing
- **A: Platform architecture and contracts**. Schema migrations, auth boundaries, contract tests, dev bootstrap. Gate: No breaking contracts without ADR; tests and migrations pass.
- **B: Immutable HR, recruitment and evidence**. History/recruitment service, tamper evidence, restore drills, golden fixtures. Gate: Retroactive changes preserve prior state; loss injected and detected.
- **C: Event operations and workforce UX**. CrewWorks synthetic demo and role-based UI. Gate: Overlaps, timezones, no-shows, eligibility, approval gates tested.
- **D: Deputy exit and Xero adapters**. Vendor capability matrix, replayable synthetic adapters, reconciliation report. Gate: Idempotent replay, failure handling, zero unapproved external writes.
- **E: Private AI and 128GB appliance**. AI proposal endpoints and benchmark reproducibility scripts. Gate: AI cannot directly mutate payroll/HR; benchmark claims measured on real hardware only.
- **F: Australian HR compliance, quality and release**. Compliance traceability matrix, risk register, test reports, UAT package. Gate: No self-certification; unknown award applicability blocks pay finalisation.
## Dependency order
A contracts before integration; B and C build against contracts; D requires B data lineage; E requires read-only APIs; F reviews all and owns go/no-go evidence. Work may proceed concurrently using mocks, but merging depends on tests. Core existing issues: #1 B, #2 B/F, #3 F, #4 D, #5 A/F, #6 C. 
## Release phases
0 architecture/synthetic fixtures; 1 records custody; 2 crew/event workflows; 3 Deputy/Xero adapters; 4 local AI; 5 parallel migration and independent compliance. No hardware procurement or deployment without authorization.
