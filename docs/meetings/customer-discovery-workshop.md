# Customer discovery workshop — workforce operations platform
**Purpose:** prepare a structured discovery conversation with a prospective Australian workforce-services customer. This is a reusable, non-customer-specific public template.

> Public repository hygiene: this document deliberately excludes customer names, contact details, private financial information, commercial prices, proposals, contracts, employee data, credentials and confidential operational details. Keep customer-specific answers in an approved private workspace.

## 1. Meeting outcome
Do not sell features before understanding the operating model. Leave the meeting with:
1. A map of how work enters the business and becomes a paid, delivered shift/project.
2. A ranked list of business problems, their frequency, impact and current workaround.
3. A clear system-of-record map (HR, recruitment, rostering, time, payroll, accounting, projects, communications).
4. Data ownership, access, retention, privacy and migration expectations.
5. A compliance discovery plan with named professional reviewers.
6. A bounded pilot scope, success measures, decision owners and next actions.

## 2. Publicly observable context — validate with customer
A public website may publish headcount, hours, shifts, attendance, geographic reach, service lines and testimonials. Treat all website figures as **CLAIMS**, not verified operating facts. Ask what period, definition and data source each metric uses. Do not infer revenue, profit, active users or software spend from public marketing metrics.

## 3. Start with the operating model
Ask the customer to walk through one recent job from first enquiry to final invoice:
- Who is the customer/client and who approves the work?
- What is sold: people, hours, shifts, a project, a production package, or an outcome?
- How are quote, purchase order, scope, budget and changes controlled?
- How are roles, skills, availability, location and crew size determined?
- Who recruits, selects, offers, onboards and verifies workers?
- How are workers engaged (employee types, contractors, subcontractors, labour hire)?
- Who creates and publishes rosters? How are changes, cancellations and replacements handled?
- How do workers clock on/off, record breaks, travel and allowances?
- Who checks timesheets and resolves disputes?
- How are client hours/rates converted to invoices?
- How are employee hours converted to payroll inputs and reconciled to accounting?
- What reports are needed daily, weekly, per pay cycle and monthly?

## 4. Current systems and failure modes
For each system capture: product, purpose, owner, contract/subscription owner, users, authoritative data, integrations, export options, API access, retention, known limitations and exit date.
- HR/personnel and applicant tracking.
- Rostering, attendance, timesheets and leave.
- Payroll, superannuation, PAYG and STP.
- Accounting, invoicing, expenses and bank reconciliation.
- Project/task management, CRM, quoting and procurement.
- Documents, e-signatures, training/induction and qualification registers.
- Email, chat, SMS, calendars and identity management.

For every reported failure ask:
- What exactly happened? Which records, dates and people were affected?
- How was it detected and how much work did recovery require?
- Is there a ticket, export, screenshot, invoice or written vendor response?
- Was data deleted, hidden, overwritten, delayed, or merely unavailable in a view?
- Can the source system provide a complete historical export and audit log?
- What is the business consequence and how often does it recur?

## 5. HR, employment and compliance discovery
Do not assume one award, one state or one employment model. Establish:
- Employing legal entities and operating jurisdictions.
- Industries and actual work performed by each worker cohort.
- Applicable modern awards, enterprise agreements, individual arrangements and award-free cohorts; who has professionally assessed coverage?
- Employment types, classifications, pay grades, effective dates and approval process.
- Ordinary hours, overtime, penalties, breaks, minimum engagements, allowances, travel, accommodation, on-call, RDO and public holiday rules.
- Leave types, accruals, balances, evidence and termination treatment.
- Super fund choice/default fund, contribution workflow, clearing house and reconciliation.
- PAYG withholding, STP reporting, payroll tax jurisdictions/grouping and workers compensation.
- Labour hire licensing, host arrangements and protected-rate orders where relevant.
- Work health and safety, site induction, licences/tickets, competency expiry and incident reporting.
- Employee records, payslips, privacy notices, access requests, retention and deletion.
- Who signs off award interpretation and payroll calculations (external accountant, payroll specialist, employment lawyer)?

**Control:** the software can calculate and explain configured rules, but cannot determine legal coverage by guesswork. Unresolved applicability or missing source evidence must block payroll finalisation.

## 6. Recruitment and people lifecycle
Map vacancy/request -> applicant -> screening -> interview -> offer -> onboarding -> engagement -> availability -> assignment -> performance/incident -> offboarding.
- Where do applicants currently arrive? Can historical applicants and attachments be exported?
- What causes applicants or employee records to be lost or duplicated?
- Which documents, consents, checks and credentials are required?
- Which data is sensitive and who may see it?
- How are unsuccessful applicants retained/deleted?
- How do qualifications, training, inductions and expiry reminders work?
- Can former employees and their historical pay conditions be reconstructed accurately?

## 7. Finance and commercial operations
- What determines client charge-out rates and worker pay rates?
- Are rates client-, role-, site-, shift-, project- or worker-specific?
- How are minimum call-outs, overtime billing, cancellation fees, travel and expenses treated?
- How are timesheets approved before invoicing and payroll?
- How are gross margin, labour cost, utilisation, unfilled shifts and cost-to-complete measured?
- What is the accounting system's role as financial system of record?
- Which reports are trusted, which are manually rebuilt, and why?
- What reconciliations must tie between operations, payroll, invoices, bank and general ledger?

## 8. Data migration and resilience
Request a private, controlled data inventory before any migration:
- Entity/record counts by month and status.
- Employee, applicant, contract, classification and pay-rate history.
- Rosters, clock events, timesheets, approvals, leave and balances.
- Attachments, notes, documents and audit/change logs.
- External IDs and relationships between modules.
- Export formats, API scopes, pagination/limits, timestamps and timezone semantics.
- Known missing periods, duplicates, corrections and retention policies.

Acceptance requires raw source preservation, checksums, source manifests, count reconciliation, relationship checks, gap reports, repeatable import and tested restore. Never silently fill gaps or treat a successful export as proof of completeness.

## 9. Xero and integration discovery
- Which Xero organisation/product and payroll subscription are in use?
- Is the organisation connected to the required Australian payroll features and ATO/STP services?
- Who owns the Xero tenant and developer app?
- Which API scopes and endpoints are actually available to this tenant?
- What data should FR3K read, stage or write?
- Are employee, pay item, leave, calendar, tracking category and account mappings documented?
- Which process currently handles super and ATO obligations?
- What does a successful end-to-end reconciliation look like?
- What must remain a human-approved action?

Do not promise a feature based solely on Xero UI availability or API documentation. Verify tenant entitlement, endpoint access, scopes and a test-tenant transaction before committing scope.

## 10. Projects, tasks and management
- Is project/task management required to replace a current tool, or should it integrate initially?
- What are the work hierarchy, dependencies, recurring tasks, approvals and notifications?
- How are responsibility, deadlines, blockers and evidence tracked?
- Which managers need dashboards, mobile access and scheduled reports?
- What must work during poor connectivity or offline operation?

## 11. Security, privacy and ownership
Agree principles before architecture:
- Customer owns and controls its business and employee data.
- Least-privilege role access, MFA/SSO and privileged-access review.
- Encryption in transit and at rest; secrets held outside source control.
- Tenant isolation and explicit support-access approval/audit.
- Data residency, backups, recovery objectives and restore tests.
- Retention schedule, privacy impact assessment and breach response.
- Full documented exports and exit/transition support.
- Clear distinction between customer data/configuration and reusable platform IP.
- No production employee data in public repositories, developer fixtures or unapproved AI services.

## 12. Pilot and acceptance measures
Agree baseline and target before implementation. Candidate measures:
- Completeness of migrated employee/applicant/history records.
- Number and age of unexplained data gaps.
- Roster publication lead time and shift-fill rate.
- Clock/timesheet exception rate and approval turnaround.
- Payroll variance against independently checked results.
- Invoice/payroll reconciliation differences.
- Time spent on manual administration and report preparation.
- Successful backup restore and recovery time.
- Integration failures, retries and unresolved exceptions.
- User adoption and support response.

Pilot gates: synthetic demonstration -> controlled data import -> read-only parallel operation -> independently verified calculations -> limited approved staging -> production cutover only after written signoffs and rollback rehearsal.

## 13. Decisions to record
| Decision | Owner | Evidence required | Status |
|---|---|---|---|
| Business entities and jurisdictions | Customer | Entity/jurisdiction inventory | UNKNOWN |
| Workforce cohorts and engagement models | Customer + adviser | Cohort map | UNKNOWN |
| Award/agreement coverage | Qualified adviser | Written coverage assessment | BLOCKED |
| Current systems and contracts | Customer | System inventory/contracts | UNKNOWN |
| Complete historical exports | Customer/vendor | Export manifest and gap report | BLOCKED |
| Xero capabilities and tenant access | Customer + integration lead | Test-tenant evidence | UNKNOWN |
| Security, hosting and data access | Customer + FR3K | Approved architecture/security plan | UNKNOWN |
| Pilot scope and success measures | Joint | Signed acceptance criteria | UNKNOWN |
| Operational owner and approvers | Customer | Responsibility matrix | UNKNOWN |
| Cutover and rollback authority | Joint | Approved runbook | BLOCKED |

## 14. Suggested meeting close
Summarise the three most expensive or risky problems in the customer's own words. Confirm what evidence will be shared, who owns each action, and when a technical discovery workshop will happen. Do not promise delivery dates or legal compliance until scope, source data, integrations and professional validation are established.

## 15. Internal follow-up checklist
- [ ] Convert notes into a private requirements register.
- [ ] Request system inventory and sample synthetic/anonymised exports through an approved secure channel.
- [ ] Request current contracts and vendor export/API documentation privately.
- [ ] Obtain award/agreement and entity coverage review from qualified professionals.
- [ ] Verify Xero tenant, API scopes and test-tenant eligibility.
- [ ] Produce a gap analysis against the current FR3K Operations app.
- [ ] Propose a phased pilot, acceptance tests, responsibilities and rollback.
- [ ] Keep commercial pricing, customer-specific financial analysis and negotiations in private proposal materials.
