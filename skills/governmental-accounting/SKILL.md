---
name: "governmental-accounting"
description: "Use for state and local government accounting under GASB: fund types, modified accrual, nonexchange revenue, fund balance classes, government-wide statements, and the fund-to-government-wide reconciliation."
---

# Governmental Accounting (GASB)

## Modes
- **Prepare**: draft fund and government-wide entries and statements.
- **Review**: check someone else's work against the rules below.
- **Explain/FAR**: when the user says "quiz me", pose a transaction and ask how it is recorded in the fund statements AND in the government-wide statements. Grade both.

## Inputs (list what's missing)
- Which fund the transaction belongs to.
- Transaction details and dates.
- Fiscal year-end.
- The government's availability period (the default for property taxes is 60 days).
- Any donor, grantor, or legal restrictions.

## 1. Fund types and basis of accounting
- **Governmental funds** (general, special revenue, capital projects, debt service, permanent):
  - Current financial resources measurement focus.
  - **Modified accrual** basis.
- **Proprietary funds** (enterprise, internal service):
  - Economic resources measurement focus.
  - Full accrual basis.
- **Fiduciary funds** (pension/OPEB trust, investment trust, private-purpose trust, custodial):
  - Full accrual basis.
  - Excluded from the government-wide statements.

## 2. Modified accrual rules (governmental funds)
**Revenues** are recognized when measurable AND available. Available means collected within the period or soon enough afterward to pay current liabilities.

**Expenditures** are recognized when the liability is incurred, with these exceptions:
- Debt service principal and interest are recognized when **due**. Unmatured interest is not accrued.
- Compensated absences and claims/judgments are recognized only when due and payable.
- Capital purchases are recorded as **capital outlay expenditures**. They are not capitalized in the fund.
- Bond proceeds are an **other financing source**, not a liability. Transfers in and out are other financing sources and uses.

## 3. Nonexchange revenue (GASB 33)
- **Derived taxes** (sales, income): recognize when the underlying exchange occurs. In governmental funds, they must also be available.
- **Imposed taxes** (property taxes):
  - Record the receivable when there is an enforceable legal claim.
  - Recognize revenue in the period for which the tax is levied, if available. Amounts not available go to deferred inflows.
- **Grants** (mandated and voluntary): recognize when all eligibility requirements are met, including time requirements. For reimbursement-type grants, that is when the qualifying expenditure is incurred.

## 4. Fund balance (GASB 54)
- **Nonspendable**: inventory, prepaids, permanent fund principal.
- **Restricted**: externally imposed by creditors, grantors, or law, or by enabling legislation.
- **Committed**: formal action by the highest decision-making authority.
- **Assigned**: intent of an authorized body or official.
- **Unassigned**: residual. A positive unassigned balance appears only in the general fund. Other funds can show negative unassigned.
- Encumbrances outstanding at year-end are reported within restricted, committed, or assigned. They are never a separate class.

## 5. Government-wide statements
- Economic resources focus, full accrual.
- Columns for governmental activities, business-type activities, and component units.
- **Statement of net position**: net position is split into net investment in capital assets, restricted, and unrestricted.
- **Statement of activities**:
  - Net (expense) revenue by function = expenses − program revenues.
  - Program revenues are charges for services, operating grants, and capital grants.
  - Taxes are general revenues.

## 6. Reconciliation: fund balance → net position
Reconcile both the balance sheet and the operating statement. Typical reconciling items:
- Capital outlay is capitalized; subtract depreciation.
- Bond proceeds become a liability; principal repayments reduce that liability.
- Accrue interest on long-term debt.
- Record long-term liabilities: compensated absences, net pension and OPEB liabilities, leases (GASB 87), and SBITAs (GASB 96).
- Recognize deferred inflows for unavailable revenue as revenue.
- Add internal service fund net position (usually to governmental activities).
- Eliminate interfund activity.

## 7. Other
- **Major funds**:
  - The general fund is always major.
  - Any other fund is major if it is at least 10% of its fund type's total for assets + deferred outflows, liabilities + deferred inflows, revenues, or expenditures/expenses, AND at least 5% of the governmental + enterprise combined total for the same element.
- **Budgetary comparison schedule**: required (as RSI) for the general fund and each major special revenue fund. Encumbrance accounting is used for budgetary control.
- **Infrastructure**: depreciate it, or use the modified approach if the government qualifies.

## Tie-outs (report PASS/FAIL)
- The change in fund balance, adjusted by every reconciling item, equals the change in governmental activities net position.
- Each fund's balance sheet balances, including deferred outflows and inflows.

## Output
1. Fund-level entries and statements.
2. Government-wide entries.
3. The reconciliation schedule.
4. Fund balance classification.
5. Flags for judgment items.

## Worked example
A city issues 1,000,000 in bonds for a library. During the year it:
- Spends 800,000 on construction.
- Pays 100,000 of bond principal and 40,000 of interest when due.
- Records 20,000 of depreciation on the library.

**Fund statements**
- Other financing source: 1,000,000.
- Capital outlay expenditure: 800,000.
- Debt service expenditure: 140,000.
- Change in fund balance: 1,000,000 − 800,000 − 140,000 = **+60,000**.

**Reconciliation to the government-wide statements**
- Add capital outlay: +800,000.
- Subtract depreciation: −20,000.
- Subtract bond proceeds: −1,000,000.
- Add principal repaid: +100,000.
- Change in net position: 60,000 + 800,000 − 20,000 − 1,000,000 + 100,000 = **−60,000**.

**Check directly**: government-wide expenses are 40,000 interest + 20,000 depreciation = 60,000. That matches the reconciled change. PASS.

## Boundaries
Reporting-entity and component-unit decisions, revenue availability periods, and fund classification are judgments. Flag them for reviewer sign-off.