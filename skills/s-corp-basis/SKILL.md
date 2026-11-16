---
name: "s-corp-basis"
description: "Use when computing or reviewing an S corporation shareholder's stock and debt basis (IRC 1366-1368, Form 7203): annual basis roll-forward, loss limitation and suspended losses, taxability of distributions, shareholder loans and repayments, AAA and E&P distribution ordering."
---

# S Corporation Shareholder Basis — Stock and Debt

## Modes
- **Prepare**: build the stock and debt basis roll-forward and the Form 7203 numbers.
- **Review**: test an existing basis schedule against the tie-outs.
- **Explain / REG**: walk through the logic. On "quiz me", give a short problem, then grade.

## Inputs (list what's missing; state every assumption)
- Beginning stock basis and beginning debt basis. If no schedule exists, rebuild from the first year the shareholder owned stock.
- Each shareholder loan: face amount outstanding, basis, and whether it is a written note or an open account.
- Schedule K-1 (Form 1120-S) items: ordinary income or loss, separately stated income and deductions, tax-exempt income, nondeductible expenses, distributions (box 16, code D).
- Capital contributions, new loans, and loan repayments during the year.
- Suspended losses carried in from prior years, by type.
- Accumulated E&P and the AAA balance, if the corporation was ever a C corporation.
- Whether the election to take losses before nondeductible expenses is in place.

## Calculation rule
Compute in code when a code tool is available.
- Basis is the shareholder's number, not the corporation's. The K-1 never shows the taxable part of a distribution.
- Adjust as of the last day of the corporation's tax year, in the order below.
- Neither stock basis nor debt basis ever goes below zero.

## 1. Stock basis, in this order
1. Beginning basis, plus capital contributions.
2. **Add** all income items: ordinary income, separately stated income and gains, tax-exempt income, excess depletion.
3. **Subtract** non-dividend distributions. A distribution above the basis at this point is capital gain, and basis stops at zero.
4. **Subtract** nondeductible, noncapital expenses (fines, the nondeductible half of meals, expenses tied to tax-exempt income). Any amount above remaining stock and debt basis is lost; it does not carry forward.
5. **Subtract** losses and deductions, limited as in section 3.

Election (Reg. 1.1367-1(g)): losses come before nondeductible expenses, and unused nondeductible expenses then carry forward. Once made, it applies to all later years.

## 2. Distributions
- Only **stock** basis counts. Debt basis never makes a distribution tax-free.
- Income for the year is added before the distribution is tested, even when the cash went out earlier in the year.
- No accumulated E&P: tax-free up to stock basis; the excess is capital gain, long-term if the stock was held more than one year.
- With accumulated E&P, distributions come out in this order:
  1. AAA: tax-free up to stock basis, gain beyond it.
  2. Accumulated E&P: a taxable dividend. It does not reduce stock basis.
  3. Anything left: reduces remaining stock basis, then capital gain.
- AAA notes: tax-exempt income does not increase AAA. Distributions cannot take AAA below zero, but losses can. In a year with a net loss, apply distributions to AAA before that year's net loss.

## 3. Loss limitation
- Losses and deductions are allowed up to stock basis after step 4, plus debt basis.
- Combine current-year items with suspended carryovers before applying the limit.
- If the total exceeds basis, allow each item pro rata: item × (basis available ÷ total losses and deductions).
- Suspended amounts keep their character, carry forward with no time limit, and are treated as incurred in the next year.
- Suspended losses are lost when the shareholder disposes of all the stock, and gain on the sale does not free them up. Two exceptions: stock transferred to a spouse, or to a former spouse in a divorce, carries its suspended losses to that person; and after an S election ends, they can still be used against stock basis during the post-termination transition period.
- After the basis limit, apply in order: at-risk (Form 6198), passive activity (Form 8582), excess business loss (Form 461).

## 4. Debt basis
- Only a direct loan from the shareholder to the corporation creates debt basis. A guarantee of a bank loan does not, until the shareholder actually pays on it.
- Losses beyond stock basis reduce debt basis. Nondeductible expenses beyond stock basis do too. Distributions never do.
- **Restoration.** In a later year, compute the net increase: income items minus distributions, nondeductible expenses, and losses and deductions for that year. A positive net increase restores debt basis first, up to the amount it was reduced, and only the rest stays in stock basis. All of the year's income still goes into stock basis first, so the distribution test in section 2 is unchanged; the restored amount then moves from stock basis to debt basis.
- With several loans, restore first the loan repaid during the year, to the extent needed to avoid gain; then the others in proportion to their reductions.

## 5. Loan repayments
- A repayment on a loan whose basis is below its face amount is partly taxable.
- Apply any restoration for the year first; restoration is effective immediately before the repayment. It applies only to debt held at the start of the year. Reductions for the year's losses take effect at year end, so they do not shrink the basis of a loan repaid earlier that year.
- Nontaxable part = repayment × (debt basis ÷ face amount). The rest is gain.
- Written note: capital gain, long-term if held more than one year. Open account with no note: ordinary income.
- Open account advances are netted at year end. An open account balance above $25,000 at year end is treated as a written note from the next year on. Whether gain on such a reclassified balance is capital when no actual note exists is unsettled: flag it for the reviewer.

## 6. Other items
- **Form 7203** is required when the shareholder claims a loss, receives a non-dividend distribution, disposes of stock, or receives a loan repayment.
- Mid-year ownership changes: allocate items per share, per day, unless the corporation elects to close the books.
- Shareholder wages are not distributions and do not affect basis. Flag distributions taken with little or no salary.
- A charitable gift of appreciated property by the corporation reduces stock basis by the shareholder's share of the property's adjusted basis, not its fair value.
- A distribution of property counts at fair value, and the corporation's gain on it passes through as income first.

## Tie-outs (report PASS/FAIL)
1. Stock roll-forward: Beginning + contributions + income − nontaxable distributions − nondeductible expenses applied − losses allowed against stock − debt basis restored = Ending, and Ending ≥ 0.
2. Debt roll-forward: Beginning + new loans − nontaxable repayments − losses and nondeductible expenses applied + restoration = Ending, with 0 ≤ Ending ≤ face amount.
3. Losses: current year + carryover in = allowed + suspended out, in total and for each type.
4. Taxable distribution = distribution − stock basis before distributions, when positive.
5. Gain on repayment = repayment − nontaxable part.

## Output
1. Stock basis roll-forward in the order above.
2. Debt basis roll-forward for each loan.
3. Loss allocation table: item, current, carryover, allowed, suspended.
4. Taxable amounts: distribution gain, dividend, repayment gain, each with its character.
5. Form 7203 filing requirement and why.
6. Flags and assumptions.
7. Tie-out results.

## Worked example
Facts: beginning stock basis 10,000. One written note with face 30,000 and basis 30,000. K-1: ordinary loss 50,000, tax-exempt interest 2,000, nondeductible expenses 1,000, distributions 4,000. No carryovers and no accumulated E&P.

| Step | Stock basis | Debt basis |
|---|---|---|
| Beginning | 10,000 | 30,000 |
| Add tax-exempt interest 2,000 | 12,000 | 30,000 |
| Less distributions 4,000 (tax-free) | 8,000 | 30,000 |
| Less nondeductible expenses 1,000 | 7,000 | 30,000 |
| Less ordinary loss: 7,000 against stock, 30,000 against debt | 0 | 0 |

- Loss allowed 37,000. Suspended ordinary loss 13,000.
- Next year: ordinary income 20,000 and no distributions. The carried-in loss of 13,000 counts as a loss for that year, so the net increase is 20,000 − 13,000 = 7,000. It restores debt basis to 7,000. Stock basis: 0 + 20,000 − 13,000 − 7,000 = 0. The 13,000 is now deductible.
- If the corporation then repays 10,000 on the note in a following year with no further net increase: nontaxable part = 10,000 × 7,000 ÷ 30,000 = 2,333.33, and the capital gain is 7,666.67.

## Boundaries
Whether an advance is real debt, whether amounts are at risk, passive activity status, and reasonable compensation are judgments: present the evidence and flag them for reviewer sign-off. State conformity is not covered. Use client IDs if firm policy requires.
