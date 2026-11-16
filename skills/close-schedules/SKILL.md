---
name: "close-schedules"
description: "Use when preparing or reviewing month-end support schedules: accrual completeness, prepaid and deferred revenue amortization, and fixed asset roll-forwards with depreciation and disposals."
---

# Month-End Close Schedules

This skill covers three schedules. Use whichever one the request needs. Every schedule must tie to the GL; report each tie as PASS/FAIL.

## Calculation rule
Recalculate everything in code when a tool is available. Never accept a schedule's own math without recomputing it.

## A. Accruals
**Inputs**
- Recurring vendor list or prior-month accrual schedule.
- Invoices received.
- Contracts and POs.
- Disbursements after period end, for the search for unrecorded liabilities.

**Procedure**
1. Completeness. For each recurring vendor or contract, determine whether the invoice was received for the period. If it wasn't, accrue.
2. Search for unrecorded liabilities. Review payments made after period end; any that relate to the period should be accrued.
3. Estimate basis. Use the contract rate, usage multiplied by rate, or the prior-month run rate, in that order of preference, and state which one was used.
4. Prior accruals. Each prior-month accrual should reverse or be trued up against the actual invoice. Flag stale accruals older than about 90 days.
5. Flag:
   - Month-over-month changes over 15% or above the materiality threshold.
   - New vendors or contracts.
   - Accruals with no support.

**Output columns**: Vendor | Basis | Prior month | Current estimate | Change | Support | Action.

## B. Prepaids and deferred revenue
**Inputs**: Item, original amount, service start and end dates, monthly amortization, remaining balance.

**Checks**
1. Amortization math. Monthly amount = original ÷ months in the service period. Remaining balance = original − months elapsed × monthly amount.
2. Start dates. Amortization begins when the service period begins, not when the invoice is paid.
3. Expired items. An item past its end date should have a zero balance.
4. Stuck balances. Flag balances unchanged from last month, and any negative balances.
5. Missing items. Look for known policies or contracts that aren't on the schedule (e.g., insurance renewals, annual software).
6. Classification. Split current (12 months or less) from noncurrent.
7. Deferred revenue. Release should follow the actual performance pattern; cross-check against the asc-606-revenue skill if the terms are complex.

**Output**: Recalculated schedule, exceptions, correcting JEs, and the tie to the GL.

## C. Fixed asset roll-forward
**Inputs**: Asset register (cost, in-service date, life, method, salvage, accumulated depreciation), additions, disposals (with proceeds), and CIP.

**Procedure**
1. Cost roll-forward: Beginning + Additions − Disposals ± Transfers from CIP = Ending. Tie to the GL by category.
2. Accumulated depreciation roll-forward: Beginning + Depreciation − AD on disposals = Ending. Tie to the GL.
3. Recalculate depreciation by method:
   - Straight-line: (cost − salvage) ÷ life.
   - Declining balance: rate × beginning NBV, never going below salvage.
   - State the convention used (full-month, mid-month, or half-year).
4. Disposals. Gain or loss = Proceeds − NBV. Depreciate the asset up to the disposal date first.
5. Additions. Test against the capitalization threshold, separate repairs (expense) from improvements (capitalize), and check the in-service date.
6. CIP. No depreciation until the asset is placed in service. Flag CIP older than about 12 months.
7. Flag:
   - Fully depreciated assets still on the register (confirm they still exist).
   - Unusual useful lives.
   - Impairment indicators under ASC 360 (significant decline in use, physical damage, losses). Indicators trigger the recoverability test; they are not a conclusion.

**Output**: Roll-forward table by category (cost, AD, NBV), depreciation recalculation versus booked amount, disposal gain/loss, exceptions, and JEs.

## Worked example (fixed assets)
**Facts**
- Machinery cost 500 to 560.
- Additions 100.
- Disposal: cost 40, accumulated depreciation 30, proceeds 15.
- Accumulated depreciation 200 to 220.
- Booked depreciation 50.

**Cost tie**: 500 + 100 − 40 = 560. PASS.

**Accumulated depreciation tie**: 200 + 50 − 30 = 220. PASS.

**Disposal**: NBV = 40 − 30 = 10. Gain = 15 − 10 = 5.

## Boundaries
Estimates, capitalization calls, and impairment conclusions go to the reviewer. Use client IDs if firm policy requires it.