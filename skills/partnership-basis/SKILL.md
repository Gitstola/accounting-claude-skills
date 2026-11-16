---
name: "partnership-basis"
description: "Use when computing or reviewing a partner's outside basis in a partnership or LLC interest (IRC 704(d), 705, 722, 731-733, 752): annual basis roll-forward, liability share changes, loss limitation and carryforwards, taxability of distributions, basis of distributed property."
---

# Partner's Outside Basis

## Modes
- **Prepare**: build the outside basis roll-forward and the loss limitation.
- **Review**: test an existing basis schedule against the tie-outs.
- **Explain / REG**: walk through the logic. On "quiz me", give a short problem, then grade.

## Inputs (list what's missing; state every assumption)
- Beginning outside basis. If no schedule exists, rebuild from the year the partner joined.
- How the interest was acquired: contribution, purchase, gift, inheritance, or services.
- Contributions for the year: cash, and the adjusted basis and any debt on contributed property.
- Schedule K-1 (Form 1065) items: ordinary income or loss, separately stated income and deductions, tax-exempt income, nondeductible expenses, guaranteed payments, distributions (box 19).
- The partner's share of liabilities at the beginning and end of the year (K-1 item K), split into recourse, nonrecourse, and qualified nonrecourse.
- For property distributions: the partnership's basis in each property and whether the distribution liquidates the interest.
- Suspended losses carried in, by type.

## Calculation rule
Compute in code when a code tool is available.
- Outside basis is the partner's number. The K-1 capital account (item L) is not basis: it leaves out the partner's share of liabilities.
- Outside basis never goes below zero.

## 1. Starting basis
- Contribution: cash plus the adjusted basis of property contributed, not its fair value.
- Purchase: cost. Gift: the donor's basis. Inheritance: fair value at death.
- Interest received for services: the amount included in income.
- Then add the partner's share of the partnership's other liabilities.
- Debt on contributed property that the partnership takes over: subtract the full debt, then add back the contributor's share of it. Count that share once only. Example: basis 40,000, debt 30,000, share 25%: 40,000 − 30,000 + 7,500 = 17,500.
- The net relief (the debt minus the contributor's share of it) is treated as money distributed. If it exceeds the basis of what was contributed, the excess is gain and basis is zero.

## 2. Annual roll-forward, in this order
1. Beginning basis.
2. **Add** contributions and any increase in the share of liabilities.
3. **Add** income: ordinary income, separately stated income and gains, tax-exempt income, excess depletion.
4. **Subtract** distributions: cash and any decrease in the share of liabilities first, then the basis of property distributed. See section 5.
5. **Subtract** nondeductible, noncapital expenses.
6. **Subtract** losses and deductions, limited as in section 3.

- Draws against the year's earnings, and liability decreases, count as distributions on the last day of the year, so the year's income is added first. Any other distribution is tested against basis on the date it is made, before later income is added.
- A guaranteed payment is not a distribution and does not itself change basis.
- Charitable contributions reduce basis by the partner's share of the partnership's adjusted basis in the property given, not its fair value. The appreciation in donated property is not subject to the basis limit.

## 3. Loss limitation (704(d))
- Losses and deductions are allowed only up to basis after step 5. This includes capital losses, section 179, charitable contributions, and foreign taxes.
- Combine current-year items with suspended carryovers before applying the limit.
- If the total exceeds basis, allow each item pro rata: item × (basis available ÷ total losses and deductions).
- Suspended amounts keep their character and carry forward with no time limit. They become deductible when basis is restored by income, a contribution, or a larger liability share.
- Suspended losses do not pass to a buyer or donee. Flag any that remain when the interest is disposed of.
- After the basis limit, apply in order: at-risk (Form 6198), passive activity (Form 8582), excess business loss (Form 461).
- At-risk is narrower than basis: it leaves out nonrecourse debt, except qualified nonrecourse financing on real estate.
- A loss that passes the basis limit reduces outside basis in full, even when the at-risk or passive rules then defer part of it.

## 4. Liabilities (752)
- An increase in the partner's share is treated as a cash contribution. A decrease is treated as a cash distribution.
- Measure the change from K-1 item K: ending share minus beginning share.
- Recourse debt goes to the partner who bears the economic risk of loss. A partner's guarantee counts only when that partner has no right to be repaid by the partnership or the other partners.
- Nonrecourse debt is generally shared by profit percentage, after any minimum gain allocations.
- In an LLC, debt is nonrecourse to the members unless a member guarantees it.
- Paying down partnership debt, refinancing, or admitting a new partner can each create a deemed distribution. Test it against basis like cash.

## 5. Distributions
**Current (non-liquidating):**
- Gain only when money exceeds outside basis just before the distribution. Money includes cash, liability relief, and most marketable securities at fair value. The gain is capital, subject to the hot-asset rules.
- No loss is recognized.
- Apply money first, then property.
- Distributed property takes the partnership's basis, limited to the outside basis left after money. Outside basis drops by that amount.
- When several properties are received and basis is short, give unrealized receivables and inventory their partnership basis first, then spread the shortfall over the other properties, starting with those whose value is below basis.

**Liquidating:**
- Property basis = outside basis minus money received.
- Allocate to unrealized receivables and inventory first, at no more than the partnership's basis, then to other property.
- Loss is recognized only when the partner receives nothing but money, unrealized receivables, and inventory, and outside basis exceeds the money plus the partnership's basis in those items. The loss is capital.

**Flags:**
- Disproportionate distributions of hot assets (751(b)).
- Property contributed with built-in gain that goes to a different partner within 7 years (704(c)(1)(B)), or other property going to the contributing partner within 7 years (737).
- Marketable securities, which usually count as money.
- Payments to a retiring partner or a deceased partner's successor (section 736): part may be ordinary income, not a distribution.
- Form 7217 is required for each date a partner receives property other than money.

## 6. Sale of the interest
- Amount realized includes the liabilities the seller is relieved of.
- Gain or loss = amount realized − outside basis, after the year's items through the sale date.
- The part tied to unrealized receivables and inventory is ordinary (751(a)); the rest is capital.

## Tie-outs (report PASS/FAIL)
1. Roll-forward: Beginning + contributions + liability increase + income − money distributed − liability decrease − basis of property distributed − nondeductible expenses − losses allowed = Ending, and Ending ≥ 0.
2. Liability change in the roll-forward = ending K-1 item K − beginning item K.
3. Losses: current year + carryover in = allowed + suspended out, in total and for each type.
4. Gain on distribution = money − basis before the distribution, when positive.
5. Reconcile to the K-1: tax-basis capital account + share of liabilities = outside basis, or list each difference.

## Output
1. Outside basis roll-forward in the order above.
2. Liability share analysis.
3. Loss allocation table: item, current, carryover, allowed, suspended.
4. Distribution analysis: gain recognized and the basis of each property received.
5. Reconciliation to the K-1 capital account.
6. Flags and assumptions.
7. Tie-out results.

## Worked example
Facts: beginning outside basis 40,000, which includes a 15,000 share of liabilities. K-1: ordinary loss 60,000, tax-exempt income 1,000, nondeductible expenses 500, cash distributions 6,000. Ending share of liabilities 25,000. No carryovers.

| Step | Amount | Basis |
|---|---|---|
| Beginning | | 40,000 |
| Liability increase (25,000 − 15,000) | +10,000 | 50,000 |
| Tax-exempt income | +1,000 | 51,000 |
| Cash distributions (no gain) | −6,000 | 45,000 |
| Nondeductible expenses | −500 | 44,500 |
| Ordinary loss, limited | −44,500 | 0 |

- Loss allowed 44,500. Suspended ordinary loss 15,500.
- If the ending share of liabilities had instead fallen to 5,000, the 10,000 decrease is a deemed cash distribution: basis before losses would be 40,000 + 1,000 − 6,000 − 10,000 − 500 = 24,500, the loss allowed 24,500, and the suspended loss 35,500.

## Boundaries
Liability classification, who bears the economic risk of loss, at-risk amounts, passive activity status, and hot-asset allocations are judgments: present the evidence and flag them for reviewer sign-off. State conformity is not covered. Use client IDs if firm policy requires.
