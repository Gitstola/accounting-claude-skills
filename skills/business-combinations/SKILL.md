---
name: "business-combinations"
description: "Use when accounting for an acquisition under ASC 805: business vs asset acquisition, purchase price allocation, intangibles, goodwill or bargain purchase, contingent consideration, NCI, step acquisitions, and measurement-period adjustments."
---

# Business Combinations — ASC 805

## Modes
- **Prepare**: build the purchase price allocation (PPA) and the entries.
- **Review**: tie out an existing PPA.
- **Explain/FAR**: when the user says "quiz me", give an acquisition and grade the PPA.

## Inputs (list what's missing)
- Consideration: cash, shares (with acquisition-date price), and contingent consideration (terms and fair value).
- Percentage acquired and any previously held interest.
- Fair value of the NCI.
- Book values and fair values of the target's assets and liabilities.
- Identified intangibles.
- Deal costs.
- Tax structure (stock deal with carryover basis, or asset deal with stepped-up basis) and the tax rate.

## Calculation rule
Build the PPA in code or as a table. It must balance.

## Procedure
1. **Business or asset acquisition?**
   - Screen: if substantially all of the fair value of gross assets is in one asset or one group of similar assets, it is an **asset acquisition**. In that case: no goodwill, transaction costs are capitalized, and cost is allocated by relative fair value.
   - Otherwise it is a business only if it includes an input plus a substantive process.
2. **Identify the acquirer and the acquisition date.** The acquisition date is when control transfers.
3. **Measure consideration** at acquisition-date fair value.
   - Contingent consideration classified as a liability is remeasured to fair value through earnings. If classified as equity, it is not remeasured.
   - Acquisition-related costs are **expensed**. Debt and equity issuance costs follow their own standards.
   - Payments for post-combination services (for example, to selling shareholders who stay on as employees) are compensation, not consideration.
4. **Recognize identifiable assets and liabilities** at fair value.
   - Recognize an intangible if it is contractual-legal OR separable. Examples: customer relationships, trade names, technology, noncompetes, backlog.
   - Assembled workforce is never separately recognized; it goes into goodwill.
   - IPR&D is capitalized as an indefinite-lived asset until the project is completed or abandoned.
   - Exceptions to fair value:
     - Deferred taxes (ASC 740).
     - Leases where the acquiree is the lessee: measured as if they were new leases.
     - Contract assets and liabilities: measured under ASC 606 as if the acquirer had originated them (ASU 2021-08).
     - Employee benefits.
     - Indemnification assets.
5. **Deferred taxes.** In a stock deal with carryover tax basis, the fair value step-ups create DTLs. Those DTLs reduce net assets and therefore increase goodwill.
6. **Previously held interest (step acquisition).** Remeasure it to fair value and recognize the gain or loss in earnings. Include it in the goodwill calculation.
7. **Goodwill.**
   - Goodwill = Consideration + FV of NCI + FV of previously held interest − net identifiable assets.
   - If the result is negative, first reassess every measurement. If it is still negative, recognize a **bargain purchase gain** in earnings.
8. **Measurement period** (up to 1 year after the acquisition date).
   - Provisional amounts are adjusted for new information about facts that existed at the acquisition date.
   - Recognize the adjustment in the period it is determined, including the cumulative effect on depreciation and amortization (ASU 2015-16). Do not restate prior periods.
9. **Private-company alternative (if elected).** Certain customer-related intangibles and noncompetes may be subsumed into goodwill. Note any related goodwill-amortization election.

## Tie-outs (report PASS/FAIL)
- Consideration + NCI + previously held interest = net identifiable assets + goodwill (or − bargain gain).
- Every fair value step-up has a deferred tax effect where the tax basis carries over.
- Deal costs are expensed, not included in goodwill.

## Output
1. Business vs. asset conclusion, with reasoning.
2. Consideration schedule.
3. PPA table: item, book value, fair value, step-up, deferred tax, useful life.
4. Goodwill or bargain purchase calculation.
5. Acquisition-date entry.
6. Amortization of step-ups going forward.
7. Judgment flags: valuations, contingent consideration, provisional amounts.

## Worked example
**Facts**
- Pays 1,000 cash for 80%.
- NCI fair value: 240.
- Identifiable net assets: book value 900, fair value 1,050 (150 PP&E step-up).
- Deal costs: 30.
- Stock deal with carryover tax basis; tax rate 21%.

**Calculation**
- DTL on the step-up = 150 × 21% = 31.5.
- Net identifiable assets = 1,050 − 31.5 = 1,018.5.
- Goodwill = 1,000 + 240 − 1,018.5 = **221.5**. Without the DTL it would be 190, a common miss.
- The 30 of deal costs is expensed.

**Tie-out**: 1,000 + 240 = 1,018.5 + 221.5 = 1,240. PASS.

## Boundaries
Valuations, intangible identification, contingent consideration fair value, and the business determination are judgments. Flag them for reviewer sign-off.