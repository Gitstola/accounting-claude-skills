---
name: "flux-variance-analysis"
description: "Use when explaining fluctuations in a trial balance, P&L, or balance sheet vs prior period or budget: flux analysis, budget-vs-actual, price/volume/mix, analytical review."
---

# Flux and Variance Analysis

## Inputs (list what's missing)
- Current and comparison balances: prior month, prior year, and/or budget.
- The threshold policy. The default is to flag a change only if it is BOTH greater than 10% AND greater than a dollar floor, with the floor set from materiality. State which threshold you used.
- Driver data where available: units, prices, headcount, rates.
- Any business context the user can give.

## Calculation rule
Compute every change and ratio in code when a code tool is available. Every number in a narrative must trace back to a table.

## Procedure
1. **Compute.** Calculate the dollar change and percentage change for each account. Flag accounts that cross the threshold. Show percentage as n/m when the base is zero.
2. **Review mode (audit analytics, AS 2305 / AU-C 520).** Set an expectation BEFORE looking at the actual number, using the related-account relationships in step 3. Compare the actual to the expectation and investigate any difference above the tolerable threshold.
3. **Relate accounts.** Never explain a balance in isolation.
   - AR vs. revenue: days sales outstanding (DSO).
   - Inventory vs. COGS: days inventory outstanding (DIO).
   - AP vs. purchases or COGS: days payable outstanding (DPO).
   - Depreciation vs. average PP&E: the implied rate.
   - Interest expense vs. average debt: the implied rate.
   - Tax expense vs. pretax income: the effective tax rate (ETR).
   - Accrued payroll vs. payroll run dates.
   - Gross margin percentage trend.
   A ratio that breaks from its trend is often more telling than the raw change.
4. **Decompose P&L variances.**
   - Volume variance = (Actual qty − Budget qty) × Budget price.
   - Price variance = (Actual price − Budget price) × Actual qty.
   - Mix variance (multiple products): (Actual mix % − Budget mix %) × Actual total qty × Budget contribution per unit.
   - The components must sum to the total variance.
5. **Write explanations.**
   - Make them specific and quantified, e.g., "+$120k; about $95k from the new X contract starting in March."
   - Never write bare "timing" or "business activity" without saying what the activity was.
   - Label each explanation as either confirmed (with its source) or a hypothesis.
   - Note one-time items that distort the comparison.
6. **Follow-up.** For each unexplained or hypothesized item, state the support to request and who to ask.

## Output
1. A flux table: account, current, comparison, dollar change, % change, flag.
2. A ratio table showing trend breaks.
3. The variance decomposition, which must sum to the total. Report PASS/FAIL.
4. Narrative explanations grouped by statement section.
5. Open questions with owners.

## Worked example
Budget: 1,000 units at $50, for revenue of 50,000.
Actual: 1,100 units at $48, for revenue of 52,800.

- Volume variance = (1,100 − 1,000) × 50 = **5,000 F**.
- Price variance = (48 − 50) × 1,100 = **2,200 U**.
- Total = **2,800 F**, which equals 52,800 − 50,000. PASS.

Narrative: Revenue beat budget by 2.8k because units were 10% higher. A $2 average price decrease partly offset this. Ask sales whether the price decrease was a discount program.

## Boundaries
Drafts are for review. The person who owns the account confirms the drivers. Do not state causation without support.