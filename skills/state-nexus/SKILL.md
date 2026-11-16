---
name: "state-nexus"
description: "Use when determining whether a business has sales and use tax nexus or income tax nexus in a state, and how much income to apportion there: physical and economic nexus thresholds, P.L. 86-272 protection, marketplace sales, apportionment factors, market-based sourcing, throwback and throwout."
---

# State Nexus and Apportionment

## Modes
- **Prepare**: build the nexus study and the apportionment schedule.
- **Review**: test an existing nexus conclusion or apportionment against the tie-outs.
- **Explain / REG**: walk through the logic. On "quiz me", give a short problem, then grade.

## Inputs (list what's missing; state every assumption)
- Sales by destination state, by month, split into goods, services, and digital products, and into direct sales and marketplace sales.
- Exempt sales and sales for resale, by state.
- Number of separate transactions by state, for states that still count them.
- Property by state: owned at original cost, rented at annual rent, and inventory held by third parties or marketplaces.
- Payroll by state, including remote employees and where each one works.
- What people do in each state: selling, installing, repairing, training, collecting, or attending trade shows.
- Where orders are approved and where goods ship from.
- Each state's current rules: thresholds, measurement period, what sales count, factor formula, sourcing method, and whether it has throwback or throwout.

## Calculation rule
Compute in code when a code tool is available.
- **Never use a state threshold or formula from memory.** They differ by state and change often. Pull each rule from the state's statute or revenue department, and record the citation and the date checked. When the rule is given in the facts, use it as given.
- Sales tax nexus and income tax nexus are separate tests with separate answers. Run both.

## 1. Sales and use tax nexus
**Physical presence** creates nexus on its own: an office, employees or sales reps working in the state, owned or leased property, or inventory stored there, including inventory in a marketplace or third-party warehouse.

**Economic nexus** applies with no physical presence. For each state:
1. Find the measurement period: prior calendar year, current calendar year, or the trailing 12 months.
2. Find what counts toward the threshold: gross sales, retail sales only, or taxable sales only. Check whether exempt sales, sales for resale, and marketplace sales are included.
3. Compare the measured sales to the dollar threshold.
4. If the state still has a transaction-count test, apply it. Note whether the tests are joined by "or" (either one creates nexus) or "and" (both are needed).
5. Record when the duty to collect starts after the threshold is crossed. Tax is owed on sales from that date forward, not on earlier sales.

**Marketplace sales:** the marketplace facilitator collects on sales made through it. Those sales still count toward the seller's threshold where the state says so, and the seller still collects on its own direct sales.

**Exposure** = taxable direct sales made after the collection start date × the tax rate, plus interest and penalties. Flag a voluntary disclosure agreement when prior periods are exposed.

## 2. Income tax nexus
- Property or payroll in the state creates nexus. One remote employee is enough in most states.
- Economic or factor-presence nexus: apply the state's own thresholds. Under the Multistate Tax Commission model, nexus exists when any one of these is exceeded in the state: $50,000 of property, $50,000 of payroll, $500,000 of sales, or 25% of total property, total payroll, or total sales. States that adopt it often change the amounts.

**P.L. 86-272** bars a state from taxing net income when the only in-state activity is soliciting orders for tangible personal property, and the orders are approved and shipped from outside the state. It does not protect:
- Sales of services, digital products, or intangibles.
- Taxes that are not on net income: sales tax, gross receipts taxes, and franchise taxes on net worth.
- Activities beyond solicitation: repairs, installation, collections, customer training, keeping inventory or an office in the state, or approving orders there.
- Some states also treat certain website activities, such as post-sale help through chat, as beyond solicitation. Check the state.

Where it applies, P.L. 86-272 overrides nexus that property-free factor presence or economic thresholds would otherwise create. Solicitation by independent contractors is also protected, and they may keep an office in the state.

A protected company still has sales into the state, so check throwback in the state it ships from.

## 3. Apportionment
1. **Formula.** Use the state's formula: single sales factor, equally weighted three-factor, or a formula that weights sales more heavily.
   - Apportionment % = the weighted average of the factors the state uses.
   - If a factor's denominator is zero, drop that factor and divide by the weights that remain.
2. **Sales factor** = in-state sales ÷ total sales.
   - Goods: the destination state.
   - Services and intangibles: market-based sourcing (where the customer gets the benefit) or cost of performance (the state where the largest share of the work is done, and it gets all of the sale). Use the state's method.
3. **Throwback and throwout.** These apply to goods shipped from the state to a state where the company is not taxable, because it has no nexus there or is protected by P.L. 86-272. The test is whether the destination state has the power to tax the company, not whether it actually has an income tax. Many throwback states also throw back sales to the U.S. government.
   - Throwback: add those sales to the shipping state's numerator.
   - Throwout: remove those sales from the denominator.
4. **Property factor** = in-state property ÷ total property. Owned property is the average of the beginning and ending balances at original cost. Rented property is 8 × annual rent.
5. **Payroll factor** = in-state compensation ÷ total compensation.
6. **State taxable income** = apportionable income × apportionment %, plus any nonbusiness income allocated to the state.

## Tie-outs (report PASS/FAIL)
1. Sales by state add up to total sales.
2. Every factor is between 0% and 100%.
3. Each threshold used has a citation and a date checked.
4. Sales tax exposure = taxable direct sales after the start date × rate.
5. The apportionment percentages across all states are added up, and any total above or below 100% is explained by differences in formulas, sourcing, throwback, or states with no nexus.

## Output
1. Nexus table by state: sales tax nexus (yes or no, the reason, the start date) and income tax nexus (yes or no, the reason, whether P.L. 86-272 applies).
2. Threshold tests with the numbers.
3. Apportionment schedule by state: each factor, the weights, the percentage, and the taxable income.
4. Exposure estimate for prior periods.
5. Registration and filing steps.
6. Flags and assumptions, with each rule's citation and date checked.
7. Tie-out results.

## Worked example
Facts: total sales 4,000,000, all goods shipped from State A. Sales to customers in State A are 1,000,000, in State B 2,400,000, and in State C 600,000. The company's only activity in State C is sales reps soliciting orders that are approved in State A. State A uses a single sales factor and has a throwback rule. Apportionable income is 500,000.

- State C: protected by P.L. 86-272, so the company is not taxable there.
- State A sales factor with throwback = (1,000,000 + 600,000) ÷ 4,000,000 = **40%**.
- State A taxable income = 500,000 × 40% = **200,000**.
- If State A instead used throwout: 1,000,000 ÷ (4,000,000 − 600,000) = **29.41%**, and taxable income of **147,058.82**.

## Boundaries
Whether an activity goes beyond solicitation, where a service's benefit is received, and whether to register or seek a voluntary disclosure agreement are judgments: present the evidence and flag them for reviewer sign-off. Local taxes and non-U.S. rules are not covered. Use client IDs if firm policy requires.
