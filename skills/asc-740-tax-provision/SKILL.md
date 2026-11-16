---
name: "asc-740-tax-provision"
description: "Use when computing or reviewing an income tax provision under ASC 740: current and deferred tax, temporary vs permanent differences, DTAs/DTLs, valuation allowance, uncertain tax positions, ETR reconciliation."
---

# ASC 740 — Income Tax Provision

## Modes
- **Prepare**: build the provision.
- **Review**: tie out an existing provision.
- **Explain/FAR**: when asked to "quiz me", give a provision problem, then grade the answer.

## Inputs (list what's missing)
- Pretax book income.
- Permanent differences.
- Temporary differences: book basis and tax basis of each item, at the beginning and end of the period.
- Enacted tax rates by year and jurisdiction. Federal is 21%; state rates are net of the federal benefit.
- Tax credits.
- NOLs and their vintages.
- Evidence relevant to a valuation allowance.
- Uncertain tax positions.

## Calculation rule
Compute the provision in code when a code tool is available. Use only enacted rates, never proposed ones.

## Procedure
1. **Classify each difference.**
   - **Permanent** differences never reverse. Examples: fines and penalties, 50% of meals, municipal bond interest, life insurance premiums where the company is the beneficiary.
   - **Temporary** differences reverse in future periods. Examples: depreciation, accrued warranty, bad debt allowance, deferred revenue, prepaid expenses, stock compensation, operating lease ROU assets and liabilities.
2. **Current tax.**
   - Taxable income = Pretax book income ± permanent differences ± current-year changes in temporary differences.
   - Current tax = Taxable income × rate − credits, after applying any NOLs.
   - Post-2017 NOLs carry forward indefinitely but can offset only 80% of taxable income.
3. **Deferred taxes.** For each item, compute book basis − tax basis.
   - An asset with book basis greater than tax basis produces a **DTL** (example: accelerated tax depreciation).
   - A liability with book basis greater than tax basis produces a **DTA** (example: accrued warranty).
   - Deferred balance = temporary difference × the enacted rate expected to apply when it reverses.
   - Deferred expense = the change in the net DTL. Exclude amounts that go through OCI or arise from a business combination.
4. **Valuation allowance.**
   - Record one if it is more likely than not that some or all of the DTA won't be realized.
   - Weigh positive and negative evidence. A cumulative 3-year loss is significant negative evidence.
   - Possible sources of taxable income to support realization: reversing DTLs, carrybacks, tax-planning strategies, and future income.
5. **Uncertain tax positions.**
   - Step 1, recognition: is the position more likely than not to be sustained?
   - Step 2, measurement: record the largest amount that has a greater than 50% likelihood of being realized.
   - Note the company's policy for classifying interest and penalties.
6. **Rate changes.** Remeasure deferred balances in the period the change is enacted. Run the effect through continuing operations.
7. **Presentation.**
   - All DTAs and DTLs are noncurrent.
   - Net them within each jurisdiction.
   - Flag intraperiod allocation issues (discontinued operations, OCI).

## ETR reconciliation (must tie)
Start with statutory rate × pretax income. Then add or subtract each of these:
- Permanent differences × rate.
- State taxes, net of the federal benefit.
- Credits.
- Change in the valuation allowance.
- Rate-change effects.
- UTP changes.
- Other items.

The result must equal total tax expense. Report PASS/FAIL.

## Tie-outs
- Current tax plus deferred tax equals total provision.
- DTA and DTL roll-forward: beginning balance + deferred expense = ending balance.
- The ETR reconciliation ties to total tax expense.

## Output
1. A schedule classifying every difference.
2. The current tax computation.
3. The deferred tax inventory: item, book basis, tax basis, difference, rate, DTA/DTL.
4. Valuation allowance analysis.
5. Uncertain tax positions.
6. The ETR reconciliation.
7. Journal entries.
8. Flags.

## Worked example
Facts:
- Pretax income: 1,000.
- Fines (nondeductible): 50.
- Muni bond interest (nontaxable): 30.
- Excess tax depreciation this year: 100.
- Tax rate: 21%.

Current tax:
- Taxable income = 1,000 + 50 − 30 − 100 = 920.
- Current tax = 920 × 21% = **193.2**.

Deferred tax:
- DTL increases by 100 × 21% = **21.0**.

Total provision = **214.2**.

ETR reconciliation:
- Statutory: 1,000 × 21% = 210.0.
- Add fines: 50 × 21% = 10.5.
- Subtract muni interest: 30 × 21% = 6.3.
- Total = 214.2. PASS. ETR = 21.42%.

The depreciation difference shifts tax between current and deferred, but it does not change the ETR.

Entry: Dr Tax expense 214.2 / Cr Taxes payable 193.2, Cr DTL 21.0.

## Boundaries
Valuation allowance and UTP conclusions are judgments. Present the evidence and flag them for tax reviewer sign-off. This is not tax return preparation advice.