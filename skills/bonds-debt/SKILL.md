---
name: "bonds-debt"
description: "Use when pricing bonds or notes, building effective-interest amortization schedules, or accounting for debt issuance costs, extinguishments, modifications, troubled debt restructurings, or debt with warrants/conversion features."
---

# Bonds and Debt (Issuer)

## Modes
- **Prepare**: price the debt, build the schedule, and draft the entries.
- **Review**: tie out an existing schedule.
- **Explain/FAR**: on "quiz me", pose a problem, then grade the answer line by line.

## Inputs (list what's missing)
- Face amount, coupon rate, market (yield) rate.
- Term, payment frequency, issue date, and interest payment dates.
- Issuance costs.
- Features: call or conversion terms, detachable warrants, covenants.
- For extinguishments or modifications: the reacquisition price, the new terms, and the date of the change.

## Calculation rule
Price and amortize in code when it's available. Convert both rates to the payment period (e.g., semiannual = annual ÷ 2, with periods = years × 2). Show the PV factors used. Plug rounding only in the final period.

## Procedure
1. **Price**
   - Issue price = PV of the face at the market rate + PV of the coupon annuity at the market rate.
   - Coupon below market gives a discount; coupon above market gives a premium.
2. **Issued between interest dates**
   - The buyer also pays the interest accrued since the last coupon date.
   - Record it as interest payable (or as a credit to interest expense), not as part of the issue price.
3. **Effective interest method** (required unless straight-line is not materially different)
   - Interest expense = beginning carrying value × market rate per period.
   - Cash = face × coupon rate per period.
   - Amortization = expense − cash.
   - A discount's carrying value rises toward face; a premium's falls toward face.
4. **Issuance costs**
   - Present them as a direct deduction from the debt's carrying amount.
   - Amortize them as interest expense through an effective rate recomputed to include the costs.
   - Exception: costs for a revolving line of credit may be presented as an asset.
5. **Year-end accrual**
   - Accrue interest from the last payment date to year-end, at the effective rate on the carrying value.
   - Amortize the discount or premium for the same partial period.
6. **Extinguishment**
   - First update amortization to the extinguishment date.
   - Gain or loss = net carrying amount (including unamortized costs and discount or premium) − reacquisition price.
   - Report it in ordinary income.
7. **Modification of non-troubled debt (10% test)**
   - Compare the PV of the new cash flows with the PV of the remaining old cash flows, both discounted at the original effective rate.
   - A difference of 10% or more is an extinguishment: derecognize the old debt, record the new debt at fair value, and recognize a gain or loss.
   - A difference under 10% is a modification: no gain or loss, and a new effective rate applies prospectively.
8. **Troubled debt restructuring** (the debtor is in financial difficulty AND the creditor grants a concession)
   - **Settlement with assets**:
     - Restructuring gain = carrying value of the debt − FV of the assets transferred.
     - Separately, gain or loss on the asset = FV − book value.
   - **Modification of terms**: compare the total *undiscounted* future cash payments with the carrying value.
     - If undiscounted payments are less than the carrying value: write the debt down to the undiscounted total and recognize a gain. All later payments reduce principal, with no interest expense.
     - If undiscounted payments are more than or equal to the carrying value: no gain; use a new effective rate prospectively.
9. **Equity features**
   - Detachable warrants: allocate the proceeds by relative fair value. If only one fair value is known, use the incremental method.
   - Convertible debt: under ASU 2020-06, it is generally a single liability with no separated equity component, unless the feature must be bifurcated as a derivative or was issued at a substantial premium.
   - On conversion: the book value method, with no gain or loss.
   - Flag any use of the fair value option.
10. **Classification**
    - The current portion is principal due within 12 months.
    - Debt that is callable because of a covenant violation is current, unless a waiver covers more than one year or a refinancing exception is met.

## Tie-outs (report PASS/FAIL)
- Carrying value equals face at maturity.
- Total interest expense = total cash interest + original discount − original premium (+ issuance costs).
- Each period: beginning CV + amortization = ending CV.

## Output
1. Pricing calculation.
2. Full amortization schedule (period, beginning CV, interest expense, cash, amortization, ending CV).
3. Entries for the requested dates.
4. Gain/loss or TDR calculation if relevant.
5. Current/noncurrent split.
6. Flags.

## Worked example
Facts: 5-year, 100,000 face, 6% coupon paid annually, 8% market rate.

Pricing:
- PV of face = 100,000 × 0.68058 = 68,058.32.
- PV of interest = 6,000 × 3.99271 = 23,956.26.
- Issue price = **92,014.58**, a discount of 7,985.42.

Year 1:
- Interest expense = 92,014.58 × 8% = 7,361.17.
- Cash = 6,000.
- Amortization = 1,361.17.
- Ending CV = 93,375.75.

Entry: Dr Interest expense 7,361.17 / Cr Cash 6,000, Cr Discount 1,361.17.

## Boundaries
TDR and modification conclusions, bifurcation, and covenant classification are judgments. Flag them for reviewer sign-off.