# FR3K Operations ⚡
**Open, evidence-driven Australian workforce and business operations platform.**

Status: **PUBLIC DOCUMENTATION + PRIVATE APPLICATION DEVELOPMENT** — application code is maintained in a separate private repository at the owner's direction. This public repository carries requirements, progress and verification summaries. Production acceptance remains incomplete.

## Mission
Replace fragmented workforce management, project management and payroll preparation with a self-hostable operational system: connect machines, measure reality, delegate work, verify results. Keep payroll finalisation, payments, lodgement and sensitive changes under human approval.

## Product boundaries
- Workforce: employee lifecycle, applicants, award/classification history, availability, rostering, attendance, leave, timesheets.
- Work: projects, tasks, dependencies, assignments, budgets, agent jobs.
- Finance: wage estimates, PAYG/super projections, payroll-tax scenarios, variance and labour-cost forecasts.
- Xero: preferred accounting/payroll handoff; never imply API access or ATO/STP capability without verification.
- Compliance: effective-dated rules, provenance, exceptions, approvals, reproducible calculations.
- Integrity: immutable audit events, snapshots, backups, restores and independent reconciliation.

## For clients and AI agents

**Give your AI assistant this repository URL:** https://github.com/fr3k-d3v/fr3k-operations

- [Client-ready AI evaluation prompt](docs/agent/CLIENT-SHARE.md)
- [Independent AI agent evaluation protocol](docs/agent/AGENT-START-HERE.md)
- [Agent entrypoint](AGENTS.md)

These guides evaluate the *published* repository only. Private implementation cannot be independently inspected from this public checkout; published verification summaries must be distinguished from independently reproduced evidence.

## CREW CENTRAL business blueprint

The business-owner visual plan has been translated into a sanitised requirements crosswalk, local implementation assessment, recruitment lifecycle design, Projects discovery model, AI authority boundaries and phased delivery gates. [Read the CREW CENTRAL blueprint](docs/product/crew-central-blueprint.md). The source workbook and local application source are not published here.

## Current engineering progress

The Django/PostgreSQL application has been preserved and pushed to the new private `fr3k-d3v/fr3k-operations-app` repository. The baseline was rerun against PostgreSQL with browser checks; private CI is configured. See the [current capability and acceptance matrix](docs/progress/CAPABILITY-MATRIX.md), [implementation progress](docs/progress/CREW-CENTRAL-IMPLEMENTATION.md), and [six delivery milestones](docs/progress/DELIVERY-MILESTONES.md). The [older development snapshot](docs/progress/LOCAL-DEVELOPMENT-SNAPSHOT.md) is retained as dated history; use the current progress page for updated counts and source references.

## Start here
- [Architecture](docs/architecture/system.md)
- [Australian compliance register](docs/compliance/australia.md)
- [Data integrity requirements](docs/architecture/data-integrity.md)
- [Deputy exit and migration](docs/migration/deputy-exit.md)
- [Xero integration](docs/integrations/xero.md)
- [Open-source research](docs/research/repositories.md)
- [Comparable systems and open suggestions](docs/research/COMPARABLE-SYSTEMS.md)
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
