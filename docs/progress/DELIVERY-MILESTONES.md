# CREW CENTRAL delivery milestones

Updated 2026-11-11. The delivery plan is implemented in a private application
repository. This public repository carries requirements and evidence summaries.
No legacy issue is closed solely because a related model or test exists.

| Milestone | Deliverable and acceptance | Existing issues |
|---|---|---|
| 1. Reproducible application baseline | Private source; clean Docker startup; pinned dependencies; synthetic fixtures; PostgreSQL/browser/security CI; current evidence index | #8; adoption review dependency in #5 |
| 2. Shared platform and recovery | Approved access/field policy; supported MFA identity; delegated approvals; document custody; observable jobs; off-host restore and measured recovery | #2; shared platform scope in #8/#9 |
| 3. HR and workforce | Vacancy-to-employment history; qualified scheduling; reviewed time and leave; period close; reconciled payroll preparation | #1, #9 |
| 4. Projects, administration and finance | Clients/jobs/tasks; budgets and allocations; traceable actual/forecast costs; variations/close; accountable registers and controlled documents; Xero-linked finance approvals | New work beyond the original issue set |
| 5. Rules, migration and Xero acceptance | Selected applicability; independently reviewed fixtures; preserved exports; verified tenant/scopes/mappings; replay safety; two accepted parallel payroll periods | #3, #4, #11, #13 |
| 6. Optional AI and production acceptance | Permission-filtered retrieval/drafts; independent reviews; monitored deployment; recovery/rollback drill; limited pilot and written cutover | #12, #13; optional vertical discovery in #6/#10 |

Each issue has one primary milestone for tracking, while its cross-cutting
acceptance criteria remain in force. #5 remains an explicit adoption-review
dependency rather than authorization to vendor external code. #6/#10 remain
optional industry-pack discovery, outside the industry-neutral release core.
Draft PR #7 remains research and is not implementation acceptance.

Use the [current implementation progress](CREW-CENTRAL-IMPLEMENTATION.md) for
source increments, verification and open gates. The private capability matrix
links implementation files, tests and remaining acceptance work. Named business,
operations and technical acceptance remains mandatory; developer CI cannot
substitute for it.
