# Sample deliverable: copier fleet lease (ASC 842, lessee)

This is the full client-file output the `asc-842-lessee` skill is built to produce, run on eval Case 21. Every number below is computed in `build_example.py`; the matching Excel workpaper with live formulas is `copier-lease-workpaper.xlsx`.

**Facts.** Copier fleet. Commencement January 1, Year 1. Term 4 years; payments of $15,000 annually in arrears (December 31). IBR 6% (implicit rate not determinable). Initial direct costs $1,000 paid by the lessee; $2,000 cash incentive received from the lessor at commencement. Fair value $80,000; economic life 8 years. No options, guarantees, or ownership transfer; not specialized. Year-end December 31.

## 1. Classification memo

| Test | Numbers | Result |
|---|---|---|
| 1. Ownership transfer | None | Not met |
| 2. Purchase option reasonably certain | None | Not met |
| 3. Major part of economic life (75%) | 4 / 8 yrs = 50.0% | Not met |
| 4. PV ≥ substantially all of fair value (90%) | 51,976.58 / 80,000.00 = 65.0% | Not met |
| 5. Specialized asset | Copiers have alternative use | Not met |

**Conclusion: operating lease.** None of the five finance-lease criteria is met.

## 2. Initial measurement

- PV factor, ordinary annuity, 4 periods at 6%: 3.465106
- Lease liability = 15,000 × 3.465106 = **51,976.58**
- ROU asset = 51,976.58 + 1,000.00 IDC − 2,000.00 incentive = **50,976.58**
- Straight-line lease cost = (60,000.00 + 1,000.00 − 2,000.00) ÷ 4 = **14,750.00** per year

## 3. Schedule

Operating lease: the liability accretes at 6%, and ROU amortization is the plug (straight-line cost − accretion), not straight-line.

| Year | Beg. liability | Payment | Accretion | Principal | End liability | Beg. ROU | ROU amortization | End ROU | Lease expense |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 51,976.58 | 15,000.00 | 3,118.60 | 11,881.40 | 40,095.18 | 50,976.58 | 11,631.40 | 39,345.18 | 14,750.00 |
| 2 | 40,095.18 | 15,000.00 | 2,405.71 | 12,594.29 | 27,500.89 | 39,345.18 | 12,344.29 | 27,000.89 | 14,750.00 |
| 3 | 27,500.89 | 15,000.00 | 1,650.05 | 13,349.95 | 14,150.94 | 27,000.89 | 13,099.95 | 13,900.94 | 14,750.00 |
| 4 | 14,150.94 | 15,000.00 | 849.06 | 14,150.94 | 0.00 | 13,900.94 | 13,900.94 | 0.00 | 14,750.00 |
| Total |  | 60,000.00 | 8,023.42 | 51,976.58 |  |  | 50,976.58 |  | 59,000.00 |

Rounding: computed at full precision and displayed to cents, so no final-period plug is needed.

## 4. Journal entries

**January 1, Year 1 (commencement)**

| Account | Dr | Cr |
|---|---|---|
| ROU asset | 50,976.58 |  |
| Cash (incentive received) | 2,000.00 |  |
| Lease liability |  | 51,976.58 |
| Cash (initial direct costs paid) |  | 1,000.00 |

**December 31, Year 1 (payment and lease cost)**

| Account | Dr | Cr |
|---|---|---|
| Lease expense (straight-line) | 14,750.00 |  |
| Lease liability (payment − accretion) | 11,881.40 |  |
| Cash |  | 15,000.00 |
| ROU asset (straight-line cost − accretion) |  | 11,631.40 |

## 5. Presentation

Current portion = principal reduction over the next 12 months, not the next 12 months of payments.

| Balance sheet date | Current | Noncurrent | Total liability |
|---|---|---|---|
| January 1, Year 1 | 11,881.40 | 40,095.18 | 51,976.58 |
| December 31, Year 1 | 12,594.29 | 27,500.89 | 40,095.18 |

**Maturity table at commencement**

| Year | Undiscounted payment |
|---|---|
| Year 1 | 15,000.00 |
| Year 2 | 15,000.00 |
| Year 3 | 15,000.00 |
| Year 4 | 15,000.00 |
| Total undiscounted | 60,000.00 |
| Less imputed interest | (8,023.42) |
| Lease liability | 51,976.58 |

Cash flow statement: operating-lease payments are operating cash outflows.

## 6. Flags for the reviewer

- **Discount rate (judgment):** 6% IBR; implicit rate not determinable. Support the IBR with a lender quote or rate curve for a 4-year secured borrowing.
- **Lease term (judgment):** 4 years; no renewal or termination options. Confirm none exist in side letters or the master agreement.
- **Components:** confirm whether the payments include service or toner charges (nonlease components) and whether the combine expedient is elected.
- **Expiration:** lease ends December 31, Year 4; flag for the renewal-or-replace decision in Year 4.

## 7. Tie-outs and assumptions

| Tie-out | Result |
|---|---|
| 1. Liability roll-forward ends at 0 | PASS |
| 2. ROU roll-forward ends at 0 | PASS |
| 3. Total lease cost = payments + IDC − incentives | PASS |
| 4. Finance-lease lifetime total | N/A (operating lease) |
| 5. Maturity table less imputed interest = liability | PASS |

Assumptions: commencement January 1, Year 1; payments on December 31; annual compounding; the $1,000 is an initial direct cost (incremental, incurred only because the lease was obtained); the $2,000 incentive was received at commencement.
