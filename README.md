# FR3K Operations ⚡
**Open, evidence-driven Australian workforce and business operations platform.**

Status: **RESEARCH / ARCHITECTURE ONLY** — not production payroll software and not certified compliant.

## Mission
Replace fragmented workforce management, project management and payroll preparation with a self-hostable operational system: connect machines, measure reality, delegate work, verify results. Keep payroll finalisation, payments, lodgement and sensitive changes under human approval.

## Product boundaries
- Workforce: employee lifecycle, applicants, award/classification history, availability, rostering, attendance, leave, timesheets.
- Work: projects, tasks, dependencies, assignments, budgets, agent jobs.
- Finance: wage estimates, PAYG/super projections, payroll-tax scenarios, variance and labour-cost forecasts.
- Xero: preferred accounting/payroll handoff; never imply API access or ATO/STP capability without verification.
- Compliance: effective-dated rules, provenance, exceptions, approvals, reproducible calculations.
- Integrity: immutable audit events, snapshots, backups, restores and independent reconciliation.

## Start here
- [Architecture](docs/architecture/system.md)
- [Australian compliance register](docs/compliance/australia.md)
- [Data integrity requirements](docs/architecture/data-integrity.md)
- [Deputy exit and migration](docs/migration/deputy-exit.md)
- [Xero integration](docs/integrations/xero.md)
- [Open-source research](docs/research/repositories.md)
- [Delivery plan](docs/product/roadmap.md)
- [Security and privacy](SECURITY.md)

## Evidence discipline
CLAIM = reported, OBSERVATION = directly observed, VERIFIED FACT = corroborated by evidence, HYPOTHESIS = to test, UNKNOWN = not checked. A commit is not deployment. A modelled payslip is not a legally verified payslip.

## Public/private separation
This repository contains no employee records, recruitment applications, payroll exports, customer details, API tokens, real company-specific pay rates, Deputy contract or private hostnames. Use synthetic fixtures only.

## Licence
Apache-2.0; third-party code must be assessed for licence compatibility before incorporation.

## Industrial construction / labour hire vertical
Optional reference vertical: Australian labour hire, industrial construction and mobile crews. See [sector-specific compliance and data model](docs/compliance/labour-hire-construction.md). Do not assume one award or that all host-site conditions automatically apply.

## Industry-neutral core
Core architecture is industry-agnostic; sector rules are optional, versioned packs. See [ADR-001](docs/product/industry-agnostic.md).
