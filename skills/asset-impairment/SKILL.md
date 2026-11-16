---
name: "asset-impairment"
description: "Use when testing or reviewing impairment of long-lived assets (ASC 360), held-for-sale assets, indefinite-lived intangibles, or goodwill (ASC 350), including triggering events and the private-company alternative."
---

# Impairment — ASC 360 and ASC 350 (US GAAP)

## Modes
- **Test**: run the model for the user's facts.
- **Review**: check someone else's impairment analysis.
- **Explain/FAR**: when the user says "quiz me", give a scenario and grade their answer.

## Inputs (list anything missing)
- Asset or asset group, or reporting unit.
- Carrying amount.
- Undiscounted future cash flows, including eventual disposition.
- Fair value and how it was estimated.
- Costs to sell, if held for sale.
- Triggering events.
- Public or private company, and whether the private-company alternatives were elected.

## Order of testing
When more than one standard applies, test in this order:
1. Other assets (inventory, receivables).
2. ASC 360 long-lived assets and finite-lived intangibles.
3. Goodwill.

Later tests use the carrying amounts adjusted by earlier tests.

## A. Long-lived assets held and used (ASC 360), including finite-lived intangibles
1. **Indicators.** Test only when a triggering event exists:
   - A significant drop in market price.
   - An adverse change in how the asset is used or in its physical condition.
   - An adverse legal or business climate.
   - Cost overruns.
   - Current losses combined with projected losses.
   - Expected disposal well before the end of the useful life.
2. **Asset group.** Test at the lowest level with identifiable cash flows that are largely independent of other assets.
3. **Recoverability.** If the carrying amount exceeds the *undiscounted* future cash flows, the asset is NOT recoverable.
4. **Measure.** Loss = carrying amount − fair value. Allocate the loss pro rata across the group, but never take an individual asset below its own fair value.
5. **After the loss.** The written-down amount is the new cost basis. Reassess the remaining useful life. **No reversals.**

**FAR trap:** fair value below carrying amount does NOT mean impairment if the undiscounted cash flows still exceed the carrying amount.

## B. Held for sale
- **Criteria (all must be met):**
  - Management has committed to a plan.
  - The asset is available for immediate sale.
  - An active program to find a buyer has begun.
  - The sale is probable within 1 year.
  - The asset is marketed at a reasonable price.
  - Significant changes to the plan are unlikely.
- **Measurement:** lower of carrying amount or fair value less cost to sell.
- Stop depreciating.
- Later increases in fair value are recognized only up to the cumulative losses previously recognized.
- Present the asset separately on the balance sheet. Check whether it qualifies as a discontinued operation.

## C. Indefinite-lived intangibles (ASC 350)
- Test annually and whenever a triggering event occurs.
- An optional qualitative screen may be used first.
- Quantitative test: if carrying amount > fair value, loss = the excess. There is no recoverability step.
- No reversals.
- Reassess each period whether the life is still indefinite.

## D. Goodwill (ASC 350)
- Test at the reporting-unit level, annually and whenever a trigger occurs.
- Optional qualitative assessment (step 0): proceed to the quantitative test only if it is more likely than not that fair value < carrying amount.
- **Quantitative (ASU 2017-04):** loss = reporting unit carrying amount (including goodwill) − reporting unit fair value, **capped at the goodwill allocated to that unit**. The old step 2 no longer exists.
- If goodwill is tax-deductible, the loss changes deferred taxes, which in turn changes carrying value. Solve this simultaneously and flag it.
- No reversals.
- **Private-company alternative (if elected):**
  - Amortize goodwill straight-line over 10 years or less.
  - The test may be done at the entity level.
  - Test only when triggered.
  - Loss = the entity's carrying amount in excess of fair value, capped at goodwill.

## IFRS contrast (only if the user is on IFRS)
IAS 36 is a one-step test: compare carrying amount with recoverable amount, which is the higher of fair value less costs of disposal and value in use (a discounted measure). Reversals are allowed for assets other than goodwill.

## Tie-outs
- Allocated losses sum to the total loss.
- No individual asset goes below its fair value.
- Goodwill loss is no greater than the goodwill balance.
- Post-impairment depreciation is based on the new basis.

## Output
1. Triggering-event analysis.
2. Asset group or reporting unit definition.
3. Recoverability test (for ASC 360).
4. Loss measurement and allocation.
5. Journal entry.
6. Remaining useful life and depreciation going forward.
7. Judgment flags, such as fair value inputs and cash flow assumptions.

## Worked examples
**Equipment**
- Carrying amount 500, undiscounted cash flows 450, fair value 380.
- 500 > 450, so the asset is not recoverable.
- Loss = 500 − 380 = **120**.
- Entry: Dr Impairment loss 120 / Cr Accumulated depreciation (or the asset) 120.
- If undiscounted cash flows had been 520, there would be **no impairment**, even though fair value is only 380.

**Goodwill**
- Reporting unit fair value 900; carrying amount 1,000, including goodwill of 80.
- The excess is 100, but the loss is capped at goodwill.
- Loss = **80**.

## Boundaries
Fair values, cash flow projections, asset grouping, and reporting-unit determinations are judgments. Flag them for reviewer sign-off.