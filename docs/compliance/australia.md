# Australian HR/payroll compliance control register
**Jurisdiction:** Australia; Queensland is an initial scenario, not a universal assumption. **Status:** research checklist; legal/accounting validation outstanding.

## Authorities to consult (primary sources)
- Fair Work Ombudsman: https://www.fairwork.gov.au/
- Fair Work Commission awards: https://www.fwc.gov.au/agreements-awards/awards
- Fair Work Act 2009: https://www.legislation.gov.au/C2009A00028/latest/text
- Fair Work Regulations 2009: https://www.legislation.gov.au/F2009L02356/latest/text
- ATO employer obligations: https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers
- Queensland payroll tax: https://qld.gov.au/payrolltax
- OAIC Australian Privacy Principles: https://www.oaic.gov.au/privacy/australian-privacy-principles
- Queensland WHS: https://www.worksafe.qld.gov.au/

## Must implement and validate
1. Identify applicable modern award, enterprise agreement or award-free status per employee and period; classifications, age, engagement type, duties, location, industry and effective dates.
2. Ordinary hours, overtime, penalties, breaks, minimum engagement, allowances, loadings, leave, public holidays, rostering notice and recordkeeping; never use a generic one-size-fits-all award calculator.
3. Fair Work employee records and payslips: design for at least seven-year preservation where legally required, accessible inspection, accurate change history and prompt payslip delivery; confirm all specific obligations against current rules.
4. National Employment Standards; casual conversion / employee choice where applicable; leave accrual and termination calculations.
5. PAYG withholding, tax tables, STP reporting, super guarantee and contribution deadlines, TFN handling, and state-based payroll tax (including grouping, interstate wages, contractors, thresholds, exemptions and annual reconciliation).
6. Queensland long service leave and any applicable portable schemes; workers compensation and WHS obligations.
7. Recruitment consent, data minimisation, restricted applicant access, retention/deletion schedules and adverse-action/discrimination controls.
8. Privacy Act/APP applicability depends on entity and exceptions; do not assume small-business exemptions universally apply or that employee-record exemptions cover applicants.
9. Award/rule changes: version source URL, publication date, effective date, approval, test cases and calculation engine version.
10. Human sign-off for payroll finalisation, super payments, STP lodgements, employee status changes and legal interpretations.

## Required tests before production
- Golden payroll fixtures from independently verified award interpretation and actual anonymised pay examples.
- Boundary tests for midnight, daylight saving where relevant, public holidays, overtime thresholds, breaks, overnight shifts, allowances, leave and retroactive rate changes.
- Parallel-run Deputy/Xero/FR3K calculations over multiple pay cycles, discrepancy register, accountant/HR review and sign-off.
- Restore test, evidence export, payslip traceability and audit-log tamper detection.

**UNKNOWN:** employer legal entity, industries, awards/agreements, states, headcount, payroll frequency, existing Xero product/subscription, applicable payroll-tax grouping and current contract terms. Do not set live rates until established.
