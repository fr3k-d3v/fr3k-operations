# Labour hire / industrial construction compliance profile (Australia)
Status: research, NOT legal certification. Industry reported by operator; legal entity, jurisdiction, award and agreements UNKNOWN.

## Key primary-source findings
- Building and Construction General On-site Award MA000020 clause 4.5 expressly covers some on-hire workers in covered classifications; coverage must be assessed for each role and host: https://awards.fairwork.gov.au/MA000020.html
- Fair Work's construction guidance lists alternative awards (electrical, plumbing, mobile crane, etc.) and enterprise agreements: https://www.fairwork.gov.au/find-help-for/building-and-construction-sector/working-in-building-and-construction
- Regulated labour hire arrangement orders can require a protected host rate; compare the employer instrument and applicable host protected rate where an order applies: https://www.fairwork.gov.au/find-help-for/labour-hire-and-supply-chains/protected-pay-rates-for-labour-hire-employees
- Queensland labour hire licensing can be mandatory for labour supply, with exemptions and distinctions for genuine subcontracting: https://www.labourhire.qld.gov.au/licensing

## New first-class records
HostClient, Site, Project, WorkPackage, Crew, CrewAssignment, RoleDuty, EmploymentStatus, HostInstrument, LabourHireOrder, AwardCoverageAssessment, SiteAllowance, Induction, LicenceTicket, CompetencyExpiry, FitForDutyRestriction, TravelArrangement, FatigueRule, WorkCoverClassification, ClientRateCard, ChargeOutLine, InvoiceReconciliation.

## Calculation pipeline
1. Resolve legal employing entity, employee/contractor status, actual duties, location, effective date and host.
2. Resolve employer award/agreement and classification with evidence and human signoff.
3. Check whether regulated labour hire arrangement order applies; where applicable calculate host protected rate and compare with employer instrument entitlements.
4. Apply shift, overtime, weekend, public holiday, break, travel, living-away, allowances, RDO and leave rules as applicable.
5. Separate employee gross wage, PAYG, super, workers compensation, payroll-tax wage base and client billable amount.
6. Preserve source citations, effective dates, versioned input and trace per pay line; block unknown classifications.
7. Human approval -> Xero supported workflow; reconcile employee, gross, tax, super and ledger totals.

## Site workflow
Client requests crew -> verify qualifications, inductions, availability and licensing -> suggest compliant roster -> dispatch -> immutable clock evidence -> supervisor and employee dispute/approval -> independently validated wage calculation -> client charge-out -> Xero reconciliation -> archived evidence.

## Specific test cases
- Two labourers on same site under different applicable instruments.
- Overnight shift crossing weekend/public holiday.
- Site change mid-week affecting allowance and host instrument.
- Expired high-risk work licence blocks assignment.
- Missing timesheet, duplicated clock event, offline sync and retroactive correction.
- Overtime and fatigue alerts, travel and distant-work allowances.
- Labour hire order applies/does not apply, effective-date transition.
- Contractor reclassification and payroll tax treatment require specialist review.

No real staff or host details in public repository.
