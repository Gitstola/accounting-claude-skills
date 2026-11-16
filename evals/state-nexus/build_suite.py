"""Build cases.md and answer_key.json for state-nexus.
States are hypothetical and each case states the rule to apply, so answers do not
depend on any real state's current law."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import q, write_suite

YN = ["yes", "no"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
          "October", "November", "December"]


def pct(x):
    return round(100 * x, 4)


def weighted(factors, weights):
    """factors: list of (numerator, denominator); a zero denominator drops the factor."""
    num = den = 0.0
    for (n, d), w in zip(factors, weights):
        if d:
            num += w * n / d
            den += w
    return num / den


C = []

# 1 marketplace sales excluded
counted = 70000 + 25000
C.append(dict(n=1, title="Economic nexus, marketplace sales excluded", facts="""
State X rule (given): a remote seller has sales tax nexus when its gross sales into the state in the current or prior calendar year exceed 100,000. Exempt sales count toward the threshold. Sales made through a marketplace facilitator do not count.
The company has no physical presence in State X. Its sales into State X last year: direct taxable sales 70,000; direct exempt sales 25,000; sales through a marketplace 60,000. This year's sales are lower.""",
    questions=[q("1a", "Sales that count toward the threshold.", counted),
               q("1b", "Does the company have sales tax nexus in State X?", "yes" if counted > 100000 else "no", choices=YN)]))

# 2 marketplace sales included
counted = 70000 + 25000 + 60000
C.append(dict(n=2, title="Economic nexus, marketplace sales included", facts="""
State Y rule (given): a remote seller has sales tax nexus when its gross sales into the state in the current or prior calendar year exceed 100,000. Exempt sales and sales through a marketplace facilitator both count toward the threshold.
Same company and the same sales as Case 1, but into State Y: direct taxable 70,000; direct exempt 25,000; marketplace 60,000. No physical presence.""",
    questions=[q("2a", "Sales that count toward the threshold.", counted),
               q("2b", "Does the company have sales tax nexus in State Y?", "yes" if counted > 100000 else "no", choices=YN),
               q("2c", "Who collects the tax on the marketplace sales?", "marketplace facilitator", choices=["seller", "marketplace facilitator"])]))

# 3 or test
C.append(dict(n=3, title="Dollar or transaction test", facts="""
State Z rule (given): nexus when gross sales into the state exceed 100,000 OR the seller makes 200 or more separate transactions into the state, in the prior calendar year.
Last year the company made 260 separate sales into State Z totaling 42,000. No physical presence.""",
    questions=[q("3a", "Does the company have sales tax nexus in State Z?", "yes", choices=YN)]))

# 4 and test
C.append(dict(n=4, title="Dollar and transaction test", facts="""
State W rule (given): nexus only when gross sales into the state exceed 100,000 AND the seller makes more than 200 separate transactions into the state, in the prior calendar year.
Last year the company made 150 separate sales into State W totaling 180,000. No physical presence.""",
    questions=[q("4a", "Does the company have sales tax nexus in State W?", "no", choices=YN)]))

# 5 retail only
counted = 240000 - 170000
C.append(dict(n=5, title="Retail sales only", facts="""
State V rule (given): nexus when retail sales into the state exceed 100,000 in the prior calendar year. Sales for resale do not count.
Last year the company's sales into State V were 240,000, of which 170,000 were sales for resale to distributors holding valid resale certificates. No physical presence.""",
    questions=[q("5a", "Sales that count toward the threshold.", counted),
               q("5b", "Does the company have sales tax nexus in State V?", "yes" if counted > 100000 else "no", choices=YN)]))

# 6 trailing 12 months
monthly = 13000
cum = [monthly * (i + 1) for i in range(12)]
cross = next(i for i, c in enumerate(cum) if c > 100000)
start = cross + 2  # first day of the second month after the crossing month
exposure = monthly * (12 - start) * 0.06
C.append(dict(n=6, title="When the duty to collect starts", facts="""
State U rule (given): nexus when gross sales into the state exceed 100,000 in the trailing 12 months. A seller that crosses the threshold must register and start collecting on the first day of the second month after the month in which the threshold was crossed. The state rate is 6%.
The company made its first sale into State U in January of this year and sold exactly 13,000 of taxable goods there every month, January through December. It has no physical presence and never registered or collected.""",
    questions=[q("6a", "Month in which the threshold was crossed.", MONTHS[cross], choices=MONTHS),
               q("6b", "Month in which the duty to collect began (it begins on the first day of that month).", MONTHS[start], choices=MONTHS),
               q("6c", "Uncollected tax exposure for this calendar year, before interest and penalties.", exposure)]))

# 7 inventory
C.append(dict(n=7, title="Inventory in a fulfillment warehouse", facts="""
State T rules (given): economic nexus when gross sales exceed 100,000 in the prior calendar year; inventory stored in the state counts as physical presence.
The company's sales into State T were 30,000 last year. It has no employees or office there, but it stores goods year-round in a marketplace's fulfillment warehouse located in State T.""",
    questions=[q("7a", "Does the company meet State T's economic nexus threshold?", "no", choices=YN),
               q("7b", "Does the company have sales tax nexus in State T?", "yes", choices=YN)]))

# 8 86-272 protected
C.append(dict(n=8, title="Solicitation only", facts="""
The company sells machine parts (tangible personal property). In State S, its only activity is two traveling sales reps who solicit orders. Every order is sent to the home office in another state for approval and is shipped from there by common carrier. The company owns and rents no property in State S, and the reps live elsewhere. Sales into State S are 600,000 a year. State S's economic nexus threshold for sales tax is 100,000 of gross sales.""",
    questions=[q("8a", "Can State S impose its net income tax on the company?", "no", choices=YN),
               q("8b", "Does the company have sales tax nexus in State S?", "yes", choices=YN)]))

# 9 86-272 lost
C.append(dict(n=9, title="Solicitation plus installation", facts="""
Same company and facts as Case 8, except that in State S the sales reps also install the parts at customer sites and perform repairs under warranty.""",
    questions=[q("9a", "Can State S impose its net income tax on the company?", "yes", choices=YN)]))

# 10 services
C.append(dict(n=10, title="Software as a service", facts="""
The company sells subscriptions to cloud software (not tangible personal property). It has no property or employees in State R. Sales to State R customers are 800,000 a year. State R rule (given): a business has income tax nexus when its sales in the state exceed 500,000.""",
    questions=[q("10a", "Does P.L. 86-272 protect the company from State R's net income tax?", "no", choices=YN),
               q("10b", "Does the company have income tax nexus in State R?", "yes", choices=YN)]))

# 11 factor presence 25%
share = 380000 / 1400000
C.append(dict(n=11, title="Factor presence, 25% test", facts="""
State Q rule (given): the Multistate Tax Commission factor presence standard at its original amounts. The company sells services, so P.L. 86-272 does not apply.
In State Q the company has property of 20,000, no payroll, and sales of 380,000. Everywhere, it has property of 400,000, payroll of 900,000, and sales of 1,400,000.""",
    questions=[q("11a", "State Q sales as a percentage of total sales.", pct(share), tol=0.05),
               q("11b", "Does the company have income tax nexus in State Q?", "yes", choices=YN)]))

# 12 factor presence none
C.append(dict(n=12, title="Factor presence, nothing exceeded", facts="""
State P rule (given): the Multistate Tax Commission factor presence standard at its original amounts. The company sells services.
In State P the company has property of 30,000, payroll of 45,000, and sales of 450,000. Everywhere, it has property of 1,000,000, payroll of 2,000,000, and sales of 10,000,000.""",
    questions=[q("12a", "Does the company have income tax nexus in State P under this standard?", "no", choices=YN)]))

# 13 single sales factor
f = 1200000 / 8000000
C.append(dict(n=13, title="Single sales factor", facts="""
State N uses a single sales factor. The company has nexus there. Sales sourced to State N are 1,200,000; total sales everywhere are 8,000,000. Apportionable income is 2,000,000.""",
    questions=[q("13a", "Apportionment percentage.", pct(f), tol=0.01),
               q("13b", "Income apportioned to State N.", 2000000 * f)]))

# 14 three factor
fac = [(2000000, 10000000), (1500000, 6000000), (3000000, 12000000)]
f = weighted(fac, [1, 1, 1])
C.append(dict(n=14, title="Equally weighted three-factor formula", facts="""
State M uses an equally weighted three-factor formula (property, payroll, sales). In-state and total amounts: property 2,000,000 of 10,000,000; payroll 1,500,000 of 6,000,000; sales 3,000,000 of 12,000,000. Apportionable income is 900,000.""",
    questions=[q("14a", "Apportionment percentage.", pct(f), tol=0.01),
               q("14b", "Income apportioned to State M.", 900000 * f)]))

# 15 double weighted
f = weighted(fac, [1, 1, 2])
C.append(dict(n=15, title="Double-weighted sales", facts="""
State L uses a three-factor formula with sales weighted twice. Same factors as Case 14: property 2,000,000 of 10,000,000; payroll 1,500,000 of 6,000,000; sales 3,000,000 of 12,000,000. Apportionable income is 900,000.""",
    questions=[q("15a", "Apportionment percentage.", pct(f), tol=0.01),
               q("15b", "Income apportioned to State L.", 900000 * f)]))

# 16 zero denominator
f = weighted([(300000, 1000000), (0, 0), (500000, 5000000)], [1, 1, 1])
C.append(dict(n=16, title="A factor with no denominator", facts="""
State K uses an equally weighted three-factor formula. The company has no employees anywhere; all work is done by independent contractors, so total payroll is zero. In-state and total amounts: property 300,000 of 1,000,000; sales 500,000 of 5,000,000.""",
    questions=[q("16a", "Apportionment percentage.", pct(f), tol=0.01)]))

# 17 property factor with rent
instate = (400000 + 600000) / 2 + 8 * 50000
total = 3000000 + 8 * 200000
C.append(dict(n=17, title="Property factor with rented property", facts="""
State J's property factor uses the standard rules. In State J the company owned property with an original cost of 400,000 at the beginning of the year and 600,000 at the end, and paid annual rent of 50,000 for a warehouse there. Everywhere, average owned property at original cost is 3,000,000 and total annual rent is 200,000.""",
    questions=[q("17a", "State J property factor numerator.", instate),
               q("17b", "Property factor denominator.", total),
               q("17c", "Property factor percentage.", pct(instate / total), tol=0.01)]))

# 18 throwback
f = (2000000 + 1000000) / 8000000
C.append(dict(n=18, title="Throwback", facts="""
The company ships all goods from its warehouse in State A. Sales by destination: State A 2,000,000; State B 5,000,000; State C 1,000,000. It has income tax nexus in A and B. In State C it has no nexus and is not taxable. State A uses a single sales factor and has a throwback rule. Apportionable income is 1,600,000.""",
    questions=[q("18a", "State A sales factor numerator.", 3000000),
               q("18b", "State A apportionment percentage.", pct(f), tol=0.01),
               q("18c", "Income apportioned to State A.", 1600000 * f)]))

# 19 throwout
f = 2000000 / (8000000 - 1000000)
C.append(dict(n=19, title="Throwout", facts="""
Same facts as Case 18, except State A has a throwout rule in place of throwback.""",
    questions=[q("19a", "State A sales factor denominator.", 7000000),
               q("19b", "State A apportionment percentage.", pct(f), tol=0.01),
               q("19c", "Income apportioned to State A.", 1600000 * f, tol=2)]))

# 20 sourcing of services
C.append(dict(n=20, title="Sourcing a service", facts="""
A consulting firm earns a 500,000 fee from one client. The client is located in State G and receives all the benefit of the service there. The firm's staff performed 60% of the work (measured by cost) in State H and 40% in State G. The firm has income tax nexus in both states. State G uses market-based sourcing. State H uses cost of performance, under which the whole sale goes to the state with the greatest share of the work.""",
    questions=[q("20a", "Amount of the fee in State G's sales factor numerator.", 500000),
               q("20b", "Amount of the fee in State H's sales factor numerator.", 500000),
               q("20c", "If State G instead used the same cost of performance rule as State H, the amount in State G's numerator.", 0)]))

# 21 remote employee
C.append(dict(n=21, title="One remote employee", facts="""
The company sells consulting services and has no customers, office, or property in State F. During the year it hired one full-time software developer who lives and works from home in State F, with wages of 85,000. State F has no minimum threshold for income tax nexus.""",
    questions=[q("21a", "Does the company have income tax nexus in State F?", "yes", choices=YN),
               q("21b", "State F payroll factor numerator.", 85000)]))

# 22 deliverable
fa = (1500000 + 700000) / 6000000
fb = weighted([(200000, 2000000), (300000, 1500000), (3800000, 6000000)], [1, 1, 2])
C.append(dict(n=22, title="Full deliverable", facts="""
Prepare the nexus study and apportionment schedule for this company and save it as `deliverable.md`, following the skill's Output section. Also answer the questions below in `answers.json`.

The company sells furniture (tangible personal property) and ships everything from its only warehouse, in State A. Apportionable income is 1,200,000. Total sales are 6,000,000: State A 1,500,000; State B 3,800,000; State D 700,000. All sales are direct and taxable.
- State A: headquarters, warehouse, and most employees. Single sales factor, with a throwback rule.
- State B: a leased showroom and 4 employees. Three-factor formula with sales weighted twice. In-state and total amounts: property 200,000 of 2,000,000; payroll 300,000 of 1,500,000; sales 3,800,000 of 6,000,000.
- State D: no property or employees. One sales rep visits to solicit orders, which are approved and shipped from State A. State D rules (given): sales tax economic nexus when gross sales exceed 100,000 in the prior calendar year (last year's sales into State D were also 700,000); income tax nexus under a factor presence standard when sales exceed 500,000.""",
    questions=[q("22a", "Does the company have sales tax nexus in State D?", "yes", choices=YN),
               q("22b", "Can State D impose its net income tax on the company?", "no", choices=YN),
               q("22c", "State A apportionment percentage.", pct(fa), tol=0.01),
               q("22d", "Income apportioned to State A.", 1200000 * fa, tol=2),
               q("22e", "State B apportionment percentage.", pct(fb), tol=0.01),
               q("22f", "Income apportioned to State B.", 1200000 * fb, tol=2)]))

write_suite(Path(__file__).resolve().parent, "state-nexus",
            "States are hypothetical. Apply the rule stated in each case. Amounts are in dollars.", C)
