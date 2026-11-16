---
name: "consolidation-intercompany"
description: "Use when preparing or reviewing consolidations, intercompany reconciliations and eliminations, NCI, acquisition-date differentials, or unrealized intercompany profit."
---

# Consolidations and Intercompany

## Modes
- **Prepare**: build the reconciliations, eliminations, and the consolidating worksheet.
- **Review**: check someone else's consolidation.
- **Explain/FAR**: when the user says "quiz me", give a short parent/sub problem and grade the eliminations.

## Inputs (list what's missing)
- Trial balances for each entity.
- Ownership percentage and acquisition date.
- Acquisition-date fair values: consideration paid, NCI fair value, fair value differentials by asset, and the lives of those assets.
- Intercompany transaction detail.
- How the parent carries the investment (equity method, cost method, or initial value).
- Functional currencies.

## Calculation rule
Build the worksheet in code or as a table. Every elimination must balance.

## Step 0 — Should it be consolidated?
- **Voting interest model**: the parent has a controlling financial interest, generally more than 50% of voting shares.
- **VIE model**: the parent is the primary beneficiary. That requires power over the activities that most significantly affect the entity's performance, AND an obligation to absorb losses or a right to receive benefits that could be significant.
- **Significant influence (roughly 20–50%)**: use the equity method, not consolidation.
- **Foreign-currency subsidiaries**: translate first and send the translation adjustment (CTA) to OCI. Flag this for review.

## Step 1 — Intercompany reconciliation
- Match each pair of reciprocal balances: the receivable from B against B's payable to A; intercompany revenue against intercompany expense.
- Classify each difference as timing (in transit), FX, a posting error, or a missing entry. State which entity needs to book the correction.
- Flag differences over the threshold, items older than 2 months, and one-sided entries.

## Step 2 — Eliminations
1. **Investment vs. sub equity (acquisition method).**
   - Eliminate the sub's equity and the investment account.
   - Book the fair value differentials to the identifiable assets and liabilities.
   - Goodwill = Consideration + NCI fair value − FV of net identifiable assets.
   - If that result is negative, it is a bargain purchase gain, but reassess the measurements first.
2. **Amortize the differentials.** Depreciate or amortize the fair value step-ups over their remaining lives.
3. **Intercompany balances.** Eliminate receivables and payables, loans and accrued interest, and interest income and expense.
4. **Intercompany sales.** Eliminate the full intercompany sale against COGS.
5. **Unrealized profit in ending inventory.**
   - Defer it: Dr COGS / Cr Inventory.
   - Recognize the prior year's deferred profit as that inventory is sold.
   - **Downstream** sales (parent to sub): charge the whole deferral to the parent.
   - **Upstream** sales (sub to parent): share the deferral with NCI in proportion to ownership.
6. **Intercompany fixed asset transfers.**
   - Eliminate the gain.
   - Restore the original cost and accumulated depreciation.
   - Reverse the excess depreciation each year.
7. **Intercompany dividends.** Eliminate them against investment income (equity method) or dividend income (cost method).

## Step 3 — Noncontrolling interest
- NCI share of income = NCI% × (sub net income − differential amortization ± upstream unrealized profit adjustments).
- NCI on the balance sheet = beginning balance + NCI share of income − NCI dividends.
- Present NCI within equity, separately from parent equity.

## Tie-outs (report PASS/FAIL)
- Each elimination entry balances.
- After eliminations, intercompany accounts net to zero.
- If the parent uses the equity method on its own books, consolidated net income attributable to the parent equals the parent's own net income.
- The goodwill calculation reconciles to the acquisition-date amounts.

## Output
1. The intercompany reconciliation, with actions for each difference.
2. The elimination entries, each with an explanation.
3. The consolidating worksheet: entity columns, eliminations, consolidated total.
4. The NCI calculation.
5. Tie-out results and any judgment flags.

## Worked example
The parent sells inventory costing 60 to its 80%-owned sub for 100. The sub still holds 25% of it at year-end.

- Unrealized profit = (100 − 60) × 25% = **10**.
- Elimination: Dr Sales 100 / Cr COGS 100. Then Dr COGS 10 / Cr Inventory 10.
- This sale is downstream, so the full 10 reduces income attributable to the parent.
- If the sale had been upstream (sub to parent), the entry would be the same, but NCI would absorb 20% × 10 = 2.

## Boundaries
Control and VIE conclusions, fair values, and FX are judgments. Flag them for reviewer sign-off.