# Test cases: state-nexus

States are hypothetical. Apply the rule stated in each case. Amounts are in dollars.

## How to answer
Write your answers to `answers.json` as one JSON object that maps each question ID to its answer.
- Number questions: a plain number, no commas or currency signs. Percentages as a number, for example 23.75 for 23.75%.
- Choice questions: exactly one of the listed choices, spelled as shown.
Answer every ID. Do the arithmetic in Python.

## Case 1: Economic nexus, marketplace sales excluded

State X rule (given): a remote seller has sales tax nexus when its gross sales into the state in the current or prior calendar year exceed 100,000. Exempt sales count toward the threshold. Sales made through a marketplace facilitator do not count.
The company has no physical presence in State X. Its sales into State X last year: direct taxable sales 70,000; direct exempt sales 25,000; sales through a marketplace 60,000. This year's sales are lower.

Questions:
- **1a** Sales that count toward the threshold. (number)
- **1b** Does the company have sales tax nexus in State X? Choices: yes, no.

## Case 2: Economic nexus, marketplace sales included

State Y rule (given): a remote seller has sales tax nexus when its gross sales into the state in the current or prior calendar year exceed 100,000. Exempt sales and sales through a marketplace facilitator both count toward the threshold.
Same company and the same sales as Case 1, but into State Y: direct taxable 70,000; direct exempt 25,000; marketplace 60,000. No physical presence.

Questions:
- **2a** Sales that count toward the threshold. (number)
- **2b** Does the company have sales tax nexus in State Y? Choices: yes, no.
- **2c** Who collects the tax on the marketplace sales? Choices: seller, marketplace facilitator.

## Case 3: Dollar or transaction test

State Z rule (given): nexus when gross sales into the state exceed 100,000 OR the seller makes 200 or more separate transactions into the state, in the prior calendar year.
Last year the company made 260 separate sales into State Z totaling 42,000. No physical presence.

Questions:
- **3a** Does the company have sales tax nexus in State Z? Choices: yes, no.

## Case 4: Dollar and transaction test

State W rule (given): nexus only when gross sales into the state exceed 100,000 AND the seller makes more than 200 separate transactions into the state, in the prior calendar year.
Last year the company made 150 separate sales into State W totaling 180,000. No physical presence.

Questions:
- **4a** Does the company have sales tax nexus in State W? Choices: yes, no.

## Case 5: Retail sales only

State V rule (given): nexus when retail sales into the state exceed 100,000 in the prior calendar year. Sales for resale do not count.
Last year the company's sales into State V were 240,000, of which 170,000 were sales for resale to distributors holding valid resale certificates. No physical presence.

Questions:
- **5a** Sales that count toward the threshold. (number)
- **5b** Does the company have sales tax nexus in State V? Choices: yes, no.

## Case 6: When the duty to collect starts

State U rule (given): nexus when gross sales into the state exceed 100,000 in the trailing 12 months. A seller that crosses the threshold must register and start collecting on the first day of the second month after the month in which the threshold was crossed. The state rate is 6%.
The company made its first sale into State U in January of this year and sold exactly 13,000 of taxable goods there every month, January through December. It has no physical presence and never registered or collected.

Questions:
- **6a** Month in which the threshold was crossed. Choices: January, February, March, April, May, June, July, August, September, October, November, December.
- **6b** Month in which the duty to collect began (it begins on the first day of that month). Choices: January, February, March, April, May, June, July, August, September, October, November, December.
- **6c** Uncollected tax exposure for this calendar year, before interest and penalties. (number)

## Case 7: Inventory in a fulfillment warehouse

State T rules (given): economic nexus when gross sales exceed 100,000 in the prior calendar year; inventory stored in the state counts as physical presence.
The company's sales into State T were 30,000 last year. It has no employees or office there, but it stores goods year-round in a marketplace's fulfillment warehouse located in State T.

Questions:
- **7a** Does the company meet State T's economic nexus threshold? Choices: yes, no.
- **7b** Does the company have sales tax nexus in State T? Choices: yes, no.

## Case 8: Solicitation only

The company sells machine parts (tangible personal property). In State S, its only activity is two traveling sales reps who solicit orders. Every order is sent to the home office in another state for approval and is shipped from there by common carrier. The company owns and rents no property in State S, and the reps live elsewhere. Sales into State S are 600,000 a year. State S's economic nexus threshold for sales tax is 100,000 of gross sales.

Questions:
- **8a** Can State S impose its net income tax on the company? Choices: yes, no.
- **8b** Does the company have sales tax nexus in State S? Choices: yes, no.

## Case 9: Solicitation plus installation

Same company and facts as Case 8, except that in State S the sales reps also install the parts at customer sites and perform repairs under warranty.

Questions:
- **9a** Can State S impose its net income tax on the company? Choices: yes, no.

## Case 10: Software as a service

The company sells subscriptions to cloud software (not tangible personal property). It has no property or employees in State R. Sales to State R customers are 800,000 a year. State R rule (given): a business has income tax nexus when its sales in the state exceed 500,000.

Questions:
- **10a** Does P.L. 86-272 protect the company from State R's net income tax? Choices: yes, no.
- **10b** Does the company have income tax nexus in State R? Choices: yes, no.

## Case 11: Factor presence, 25% test

State Q rule (given): the Multistate Tax Commission factor presence standard at its original amounts. The company sells services, so P.L. 86-272 does not apply.
In State Q the company has property of 20,000, no payroll, and sales of 380,000. Everywhere, it has property of 400,000, payroll of 900,000, and sales of 1,400,000.

Questions:
- **11a** State Q sales as a percentage of total sales. (number)
- **11b** Does the company have income tax nexus in State Q? Choices: yes, no.

## Case 12: Factor presence, nothing exceeded

State P rule (given): the Multistate Tax Commission factor presence standard at its original amounts. The company sells services.
In State P the company has property of 30,000, payroll of 45,000, and sales of 450,000. Everywhere, it has property of 1,000,000, payroll of 2,000,000, and sales of 10,000,000.

Questions:
- **12a** Does the company have income tax nexus in State P under this standard? Choices: yes, no.

## Case 13: Single sales factor

State N uses a single sales factor. The company has nexus there. Sales sourced to State N are 1,200,000; total sales everywhere are 8,000,000. Apportionable income is 2,000,000.

Questions:
- **13a** Apportionment percentage. (number)
- **13b** Income apportioned to State N. (number)

## Case 14: Equally weighted three-factor formula

State M uses an equally weighted three-factor formula (property, payroll, sales). In-state and total amounts: property 2,000,000 of 10,000,000; payroll 1,500,000 of 6,000,000; sales 3,000,000 of 12,000,000. Apportionable income is 900,000.

Questions:
- **14a** Apportionment percentage. (number)
- **14b** Income apportioned to State M. (number)

## Case 15: Double-weighted sales

State L uses a three-factor formula with sales weighted twice. Same factors as Case 14: property 2,000,000 of 10,000,000; payroll 1,500,000 of 6,000,000; sales 3,000,000 of 12,000,000. Apportionable income is 900,000.

Questions:
- **15a** Apportionment percentage. (number)
- **15b** Income apportioned to State L. (number)

## Case 16: A factor with no denominator

State K uses an equally weighted three-factor formula. The company has no employees anywhere; all work is done by independent contractors, so total payroll is zero. In-state and total amounts: property 300,000 of 1,000,000; sales 500,000 of 5,000,000.

Questions:
- **16a** Apportionment percentage. (number)

## Case 17: Property factor with rented property

State J's property factor uses the standard rules. In State J the company owned property with an original cost of 400,000 at the beginning of the year and 600,000 at the end, and paid annual rent of 50,000 for a warehouse there. Everywhere, average owned property at original cost is 3,000,000 and total annual rent is 200,000.

Questions:
- **17a** State J property factor numerator. (number)
- **17b** Property factor denominator. (number)
- **17c** Property factor percentage. (number)

## Case 18: Throwback

The company ships all goods from its warehouse in State A. Sales by destination: State A 2,000,000; State B 5,000,000; State C 1,000,000. It has income tax nexus in A and B. In State C it has no nexus and is not taxable. State A uses a single sales factor and has a throwback rule. Apportionable income is 1,600,000.

Questions:
- **18a** State A sales factor numerator. (number)
- **18b** State A apportionment percentage. (number)
- **18c** Income apportioned to State A. (number)

## Case 19: Throwout

Same facts as Case 18, except State A has a throwout rule in place of throwback.

Questions:
- **19a** State A sales factor denominator. (number)
- **19b** State A apportionment percentage. (number)
- **19c** Income apportioned to State A. (number)

## Case 20: Sourcing a service

A consulting firm earns a 500,000 fee from one client. The client is located in State G and receives all the benefit of the service there. The firm's staff performed 60% of the work (measured by cost) in State H and 40% in State G. The firm has income tax nexus in both states. State G uses market-based sourcing. State H uses cost of performance, under which the whole sale goes to the state with the greatest share of the work.

Questions:
- **20a** Amount of the fee in State G's sales factor numerator. (number)
- **20b** Amount of the fee in State H's sales factor numerator. (number)
- **20c** If State G instead used the same cost of performance rule as State H, the amount in State G's numerator. (number)

## Case 21: One remote employee

The company sells consulting services and has no customers, office, or property in State F. During the year it hired one full-time software developer who lives and works from home in State F, with wages of 85,000. State F has no minimum threshold for income tax nexus.

Questions:
- **21a** Does the company have income tax nexus in State F? Choices: yes, no.
- **21b** State F payroll factor numerator. (number)

## Case 22: Full deliverable

Prepare the nexus study and apportionment schedule for this company and save it as `deliverable.md`, following the skill's Output section. Also answer the questions below in `answers.json`.

The company sells furniture (tangible personal property) and ships everything from its only warehouse, in State A. Apportionable income is 1,200,000. Total sales are 6,000,000: State A 1,500,000; State B 3,800,000; State D 700,000. All sales are direct and taxable.
- State A: headquarters, warehouse, and most employees. Single sales factor, with a throwback rule.
- State B: a leased showroom and 4 employees. Three-factor formula with sales weighted twice. In-state and total amounts: property 200,000 of 2,000,000; payroll 300,000 of 1,500,000; sales 3,800,000 of 6,000,000.
- State D: no property or employees. One sales rep visits to solicit orders, which are approved and shipped from State A. State D rules (given): sales tax economic nexus when gross sales exceed 100,000 in the prior calendar year (last year's sales into State D were also 700,000); income tax nexus under a factor presence standard when sales exceed 500,000.

Questions:
- **22a** Does the company have sales tax nexus in State D? Choices: yes, no.
- **22b** Can State D impose its net income tax on the company? Choices: yes, no.
- **22c** State A apportionment percentage. (number)
- **22d** Income apportioned to State A. (number)
- **22e** State B apportionment percentage. (number)
- **22f** Income apportioned to State B. (number)
