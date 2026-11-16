---
name: "asc-842-lessee"
description: "Use when classifying, measuring, booking, or reviewing lessee lease accounting under ASC 842: PV of payments, ROU assets, amortization schedules, monthly/annual entries, roll-forwards, modifications."
---

# ASC 842 — Lessee Accounting

## Modes
- **Prepare**: build classification, schedules, and entries.
- **Review**: test an existing schedule against the tie-outs.
- **Explain / FAR**: walk through the logic. On "quiz me", give a short problem, then grade.

## Inputs (list what's missing; state every assumption)
- Commencement date and lease term. Include renewals the lessee is reasonably certain to exercise, periods covered by termination options it is reasonably certain NOT to exercise, and periods covered by any extension or termination option that only the lessor controls (always included; no "reasonably certain" test).
- Payment schedule:
  - Amounts and escalations.
  - Timing: in advance or in arrears.
  - Index-based variable payments, measured at the commencement index.
- Discount rate. Use the implicit rate if readily determinable, otherwise the IBR. Private companies may elect the risk-free rate by asset class.
- Initial direct costs, lease incentives received, payments made at or before commencement.
- Residual value guarantee, purchase option (and whether reasonably certain).
- Asset fair value and economic life (needed for classification).
- Elections: short-term exemption; practical expedient to combine lease and nonlease components.

## Calculation rule
Compute PVs and schedules in code when a code tool is available.
- State the period convention (e.g., monthly rate = annual ÷ 12).
- Payments in advance are an annuity due: the first payment reduces the liability at commencement and carries no interest.
- Plug rounding only in the final period, and say so.

## 1. Classification
It is a **finance lease** if ANY of these is met; otherwise it is operating.
1. Ownership transfers by the end of the term.
2. A purchase option the lessee is reasonably certain to exercise.
3. The term is a major part of the remaining economic life. 75% is the common policy threshold. Skip this test if commencement falls in the last ~25% of the asset's life.
4. PV of lease payments + lessee RVG ≥ substantially all of fair value. 90% is the common threshold.
5. The asset is so specialized it has no alternative use to the lessor.

Show each test with its numbers.

## 2. Initial measurement
- Lease liability = PV of unpaid lease payments (fixed + index-based + probable RVG amount + reasonably certain purchase option).
- ROU asset = Liability + payments at or before commencement + IDC − incentives received.
- Usage- or performance-based variable payments are excluded and expensed as incurred.

## 3. Subsequent measurement
**Finance lease** (front-loaded expense):
- Interest = beginning liability × rate (effective interest).
- ROU amortization is straight-line over the shorter of term or useful life. Use useful life if ownership transfers or the purchase option is reasonably certain.
- Entries: Dr Interest expense, Dr Lease liability / Cr Cash. Dr Amortization expense / Cr ROU asset.

**Operating lease** (single straight-line cost; this is where most errors happen):
- Straight-line lease cost = (total payments + IDC − incentives) ÷ term.
- The liability still accretes by effective interest, exactly like a finance lease.
- **ROU amortization is a plug**: straight-line cost − liability accretion for the period. It is NOT straight-line.
- Entry per period: Dr Lease expense (SL cost), Dr Lease liability (payment − accretion) / Cr Cash (payment), Cr ROU asset (SL cost − accretion).
- After an operating ROU impairment, the pattern changes: the remaining ROU is amortized straight-line, plus accretion, so expense becomes front-loaded.

**Short-term leases** (≤ 12 months, no reasonably certain purchase option, if elected): straight-line expense, with no ROU asset or liability.

## 4. Remeasurement and modifications
- A modification that grants an additional right of use priced at standalone price is accounted for as a separate contract.
- Otherwise, remeasure the liability at the modification date using an updated discount rate, and adjust the ROU.
- A partial termination reduces the ROU proportionately and recognizes a gain or loss.
- Other remeasurement triggers:
  - A change in the term or purchase-option assessment.
  - A change in the amount probable under the RVG.
  - A contingency resolving so variable payments become fixed.
- Index changes alone do NOT trigger remeasurement; the difference is a variable expense.

## 5. Presentation
- Current portion of the liability = principal reduction over the next 12 months, NOT the next 12 months of payments.
- Maturity table: undiscounted payments by year, less imputed interest, equals the liability.
- Cash flow statement: operating-lease payments are operating. Finance-lease principal is financing; finance-lease interest is operating.

## Tie-outs (report PASS/FAIL)
1. Liability roll-forward: Beginning + accretion − payments = Ending. It ends at 0 (or at the RVG or purchase-option amount).
2. ROU roll-forward ends at 0 (or at the expected residual for ownership-transfer cases).
3. Operating: total lease cost over the term = total payments + IDC − incentives.
4. Finance: total interest + amortization = the same lifetime total.
5. The maturity-table total, less imputed interest, equals the balance-sheet liability.

## Output
1. Classification memo with each test and its numbers.
2. Initial measurement (PV calculation shown).
3. Full schedule: period, beginning liability, payment, accretion/interest, principal, ending liability, beginning ROU, ROU amortization, ending ROU, expense.
4. Journal entries for the requested period(s).
5. Current/noncurrent split and maturity table.
6. Flags: upcoming expirations, modification triggers, judgment items.
7. Tie-out results and assumptions.

## Worked example (operating lease)
Facts: 3-year term; payments of 10,000 per year in arrears; 5% IBR; no IDC or incentives.

Liability = ROU = 10,000 × 2.72325 = 27,232.48.

| Yr | Accretion | Payment | End liability | SL cost | ROU amort (plug) | End ROU |
|---|---|---|---|---|---|---|
| 1 | 1,361.62 | 10,000 | 18,594.10 | 10,000 | 8,638.38 | 18,594.10 |
| 2 | 929.71 | 10,000 | 9,523.81 | 10,000 | 9,070.29 | 9,523.81 |
| 3 | 476.19 | 10,000 | 0.00 | 10,000 | 9,523.81 | 0.00 |

If this were a finance lease:
- Year 1 expense = 1,361.62 interest + 9,077.49 amortization (27,232.48 ÷ 3) = 10,439.11.
- The lifetime total is the same 30,000; only the pattern differs.

## Boundaries
Term, discount rate, and "reasonably certain" assessments are judgments: present the evidence and a recommendation, and flag them for reviewer sign-off. Use client IDs if firm policy requires.