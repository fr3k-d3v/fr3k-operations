# System architecture
## Bounded contexts
Identity & RBAC; People & Recruitment; Contracts & Classifications; Scheduling; Time & Attendance; Leave; Projects & Work; Rules & Calculations; Payroll Preparation; Finance & Forecasting; Integrations; Audit & Evidence; Agent Orchestration.

## Data model (initial)
Person, Employee, Applicant, EmploymentEngagement, ContractVersion, AwardAssignment, ClassificationVersion, PayRateVersion, Location, RosterShift, ShiftChange, ClockEvent, TimesheetVersion, LeaveRequest, Approval, PayrollPeriod, CalculationRun, CalculationLine, TaxRuleVersion, SuperRuleVersion, PayrollTaxScenario, Project, Task, Job, IntegrationCursor, ExternalMapping, AuditEvent, EvidenceArtifact, ReconciliationResult.

Every historical pay rate and classification is effective-dated and immutable after approval; corrections are superseding records, not destructive edits. Clock events are append-only; approved timesheets are versioned. Calculations pin rule set, source data versions and software revision.

## Infrastructure
PostgreSQL as authoritative transactional store; object storage for encrypted source evidence; durable queue/orchestrator with stable IDs, dependencies, leases, fencing, idempotency and immutable terminal states. API-first web/mobile clients. Agents propose; policy engine gates consequential actions. Local self-hosting remains viable without hosted AI.

## Authority
OBSERVE read-only; AUTO bounded low-risk operations; APPROVAL human-authorised payroll/employee changes; PHYSICAL device-specific. No agent can silently elevate authority.

## Integrations
Adapter interfaces for Deputy import, Xero, calendars and communications. Explicit reconciliation of imported IDs, timestamps, counts and totals. External sync is not the source of historical truth.

## Non-goals for first milestone
Direct bank disbursements, ATO/STP lodgement, automated legal advice, unattended employment decisions and production award interpretation.
