---
name: "stock-compensation"
description: "Use when measuring, expensing, or reviewing share-based payment awards (ASC 718): options, RSUs, SARs, grant-date fair value, vesting schedules, forfeitures, performance/market conditions, modifications, liability awards, exercises, and tax effects."
---

# Stock Compensation — ASC 718

## Modes
- **Prepare:** build the expense schedule and entries.
- **Review:** tie out an existing schedule.
- **Explain/FAR:** when the user says "quiz me", pose an award and grade each period's expense.

## Inputs (list what's missing)
- Award type: options, RSUs, SARs, ESPP.
- Grant date and number of awards.
- Grant-date fair value, or the valuation inputs: stock price, exercise price, expected term, volatility, risk-free rate, dividend yield.
- Vesting: cliff or graded; service, performance, or market conditions.
- Settlement: shares or cash.
- Forfeiture policy.
- Par value.
- Public or nonpublic entity.
- Tax status of the award: NQSO, ISO, or RSU.

## Calculation rule
Build the expense schedule in code or as a table. Work from cumulative expense: each period's expense = cumulative expense required to date − expense already recognized.

## Procedure
1. **Classification.**
   - **Equity-classified** (settled in shares): measured once, at grant-date fair value.
   - **Liability-classified** (cash-settled SARs, certain puttable shares): remeasured at each reporting date until settlement.
2. **Grant date.** Mutual understanding of the key terms, plus all required approvals.
3. **Fair value.**
   - Options: Black-Scholes or a lattice model. Show the inputs.
   - RSUs: share price at grant, less the PV of dividends the holder won't receive.
   - Nonpublic entities:
     - May use a calculated value based on an industry index if their own volatility can't be estimated.
     - May use the practical expedient for expected term.
     - May elect intrinsic value for liability awards.
4. **Recognition.**
   - Recognize over the requisite service period.
   - Graded vesting with service conditions only: policy choice between straight-line over the whole award or accelerated (tranche by tranche).
   - Either way, cumulative expense at any date must be at least the grant-date value of the portion already vested.
5. **Forfeitures.**
   - Policy election: estimate them, or account for them as they occur (ASU 2016-09).
   - Either way, true up through a cumulative catch-up.
6. **Conditions.**
   - **Service and performance conditions** affect whether the award vests.
     - Recognize expense only if achievement is probable.
     - Reassess each period and book a cumulative catch-up.
     - If the condition is not met, reverse the expense.
   - **Market conditions** (stock price targets, TSR) are built into the grant-date fair value.
     - Expense IS recognized if the service is rendered, even if the market condition is never met.
     - Do not reverse. (Common FAR trap.)
7. **Modifications.**
   - Incremental cost = fair value of the modified award − fair value of the original award immediately before the modification.
   - Recognize it immediately for vested awards and over the remaining service period for unvested ones.
   - Improbable-to-probable modifications (Type III) are measured at modification-date fair value.
8. **Exercise and expiration.**
   - Exercise: Dr Cash, Dr APIC–stock options / Cr Common stock (par), Cr APIC.
   - Vested options that expire unexercised: no reversal. Reclassify within APIC.
9. **Taxes.**
   - Record a DTA on book expense for awards that normally produce a tax deduction (NQSOs, RSUs).
   - ISOs: generally no DTA, unless a disqualifying disposition occurs.
   - Excess tax benefits and shortfalls go to income tax expense (ASU 2016-09).
10. **Other.**
    - An ESPP is noncompensatory only if the discount is 5% or less, it is broadly available, and it has no option features.
    - Nonemployee awards follow the employee model (ASU 2018-07).

## Tie-outs (report PASS/FAIL)
- Total expense over the vesting period = grant-date fair value × awards that vest, plus any modification increments.
- Cumulative expense ≥ the vested portion at every date.
- APIC–options roll-forward ties.

## Output
1. Classification and measurement.
2. Fair value inputs.
3. Expense schedule by period (cumulative required, prior recognized, current expense).
4. Journal entries for grant-period expense, forfeitures, and exercise.
5. Deferred tax effects.
6. Flags.

## Worked example
**Facts:** On 1/1/Y1, grant 10,000 options. Grant-date FV is $6. 3-year cliff vesting. Forfeitures are recorded as they occur. Par value is $1.

- **Y1:** total cost = 60,000, so expense = **20,000**. Entry: Dr Compensation expense / Cr APIC–options.
- **Y2:** 1,000 options are forfeited.
  - Cumulative required = 9,000 × $6 × 2/3 = 36,000.
  - Already recognized = 20,000.
  - Y2 expense = **16,000**.
- **Y3:** expense = 54,000 − 36,000 = **18,000**.
- **Exercise of 9,000 options at a $15 strike:**
  - Cash = 135,000.
  - APIC–options = 54,000.
  - Credit common stock 9,000 (par) and APIC 180,000.

## Boundaries
Valuation inputs, the probability of meeting performance conditions, and modification accounting are judgments. Flag them for reviewer sign-off.