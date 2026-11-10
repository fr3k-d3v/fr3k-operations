# Industry-agnostic core — architectural decision ADR-001
Status: ACCEPTED for product design; implementation unverified.

FR3K Operations is a general-purpose, self-hostable operations platform. Labour hire and industrial construction are optional domain packs, not default assumptions.

## Core contracts
- People, engagements, contracts, versioned classifications, scheduling, attendance, leave, tasks/projects, approvals, calculation runs, finance, audit and integrations.
- Jurisdiction and industry are deployment configuration, not hard-coded assumptions.
- Rules are scoped by jurisdiction, legal entity, industry, employment instrument, role, location, effective date and source provenance.
- A rules pack may extend entities, validations, calculations, dashboards and tests without changing core schema semantics.
- Unknown legal applicability blocks payroll finalisation rather than falling back to an arbitrary industry award.

## Pack interface (proposal)
Pack manifest: id, version, jurisdiction, supported industries, licence, source references, effective dates, schema migrations, rule definitions, fixture set, capability flags and human review requirements.

## Initial optional packs
- au-employment-core: NES, employment records, leave and Australian payroll preparation controls.
- au-qld-payroll-tax: state-specific modelling (not PAYG).
- au-labour-hire-construction: host sites, crews, qualifications, labour hire orders and allowances.
- Generic projects and resource scheduling (no sector assumptions).

## Acceptance tests
1. Deploy with zero industry packs and manage projects, tasks and non-payroll schedules.
2. Add or remove a sector pack without corrupting historic records.
3. Multiple industries and legal entities coexist in one tenant with isolated rules.
4. Historical calculations remain reproducible after rules-pack upgrades.
5. Cross-jurisdiction and ambiguous award assignments require explicit review.
6. Public repository contains synthetic data only.

No sector-specific workflows are mandatory in the initial core.
