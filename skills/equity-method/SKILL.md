---
name: "equity-method"
description: "Use when accounting for equity method investments (ASC 323): significant influence, basis differences, investee income and dividends, intra-entity profit, losses below zero, and changes to or from the equity method."
---

# Equity Method Investments — ASC 323

## Modes
- **Prepare**: build the investment roll-forward and the entries.
- **Review**: tie out an existing roll-forward.
- **Explain/FAR**: when the user says "quiz me", pose a problem and grade the roll-forward.

## Inputs (list what's missing)
- Cost of the investment and percentage owned.
- Acquisition date.
- Investee's book value of net assets, plus fair values of any assets that differ, with their remaining lives.
- Investee net income and OCI for the period.
- Investee dividends declared.
- Investee preferred stock terms.
- Intra-entity sales, with the margin and the amount still held at period end.
- Other investments in the investee (loans, preferred shares) and any guarantees.

## Calculation rule
Build the roll-forward in code or as a table.

## Procedure
1. **Significant influence?**
   - Presumed at 20–50% ownership. The presumption can be rebutted.
   - Indicators: a board seat, participation in policy-making, material intra-entity transactions, interchange of personnel, technological dependency.
   - Note whether the fair value option was elected.
2. **Initial measurement.**
   - Record at cost, including transaction costs.
   - Basis difference = cost − (ownership % × investee book value of net assets).
   - Allocate it first to fair value differences on identifiable assets, at the investor's share.
   - Treat any remainder as equity-method goodwill. It is not amortized (unless the private-company alternative applies) and is not tested for impairment separately.
3. **Each period, adjust the carrying amount:**
   - Add the investor's % × investee net income. Use income available to common: subtract cumulative preferred dividends whether declared or not, and noncumulative preferred dividends only if declared.
   - Subtract amortization of the basis difference:
     - Depreciable assets: over their remaining life.
     - Inventory: as the inventory is sold.
     - Land: none.
   - Subtract dividends received. These reduce the investment and are NOT income.
   - Add or subtract the investor's share of investee OCI, recorded in the investor's OCI.
   - Eliminate the investor's share of unrealized intra-entity profit in assets still held. This applies to both upstream and downstream sales.
4. **Losses.**
   - Once the investment reaches zero, stop recording losses.
   - Exceptions: the investor has guaranteed obligations, committed further support, or holds other investments in the investee. Those absorb further losses in order of seniority.
   - Track suspended losses. Resume recording income only after the investor's share of income exceeds those suspended losses.
5. **Impairment.**
   - Test the investment as a whole.
   - A decline in fair value below the carrying amount that is other than temporary requires a write-down.
   - No reversal.
6. **Changes in ownership.**
   - **Becoming equity method (ASU 2016-07):** prospective. Add the cost of the new interest to the existing basis. No retroactive restatement.
   - **Losing significant influence:** stop applying the equity method. The carrying amount becomes the basis under ASC 321, and the investment is then measured at fair value.
   - **Gaining control:** this is a step acquisition. Remeasure the previously held interest to fair value through earnings, then apply ASC 805.
   - **Selling part of the stake:** gain or loss = proceeds − the proportional carrying amount.
7. **Other items.**
   - A reporting lag of up to about 3 months is allowed if applied consistently.
   - Cash flow classification of distributions: use the cumulative-earnings approach or the nature-of-distribution approach (policy election).
   - Flag deferred taxes on outside basis differences.

## Tie-outs (report PASS/FAIL)
- Beginning + share of income − basis amortization − dividends ± OCI − unrealized profit = Ending.
- Basis difference allocation: fair value differences + goodwill = total basis difference.
- No loss is recorded below zero unless one of the exceptions applies.

## Output
1. Significant influence conclusion.
2. Basis difference allocation table.
3. Investment roll-forward.
4. Equity in earnings calculation.
5. Journal entries.
6. Flags.

## Worked example
Facts:
- Buy 30% for 400 on 1/1.
- Investee book value of net assets is 1,000. Fair value is 1,200, with the 200 difference in equipment that has a 10-year remaining life.
- Investee net income 150. Dividends 50.

Basis difference:
- Share of book value = 30% × 1,000 = 300, so the basis difference is 100.
- Equipment: 30% × 200 = 60, amortized at 6 per year.
- Goodwill: 100 − 60 = 40, not amortized.

Year 1:
- Equity in earnings = 30% × 150 − 6 = **39**.
- Dividends = 30% × 50 = 15, which reduces the investment.
- Ending investment = 400 + 45 − 6 − 15 = **424**.

Entries:
- Dr Investment 39 / Cr Equity in earnings 39.
- Dr Cash 15 / Cr Investment 15.

## Boundaries
The significant influence determination, fair value allocations, and impairment are judgments. Flag them for reviewer sign-off.