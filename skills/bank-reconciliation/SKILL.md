---
name: "bank-reconciliation"
description: "Use when preparing or reviewing a bank reconciliation, matching bank statement activity to the GL cash account, or finding why cash doesn't tie."
---

# Bank Reconciliation

## Inputs (list what's missing)
- Bank statement activity and ending balance.
- GL cash detail and ending balance.
- Prior-period reconciliation, which supplies the outstanding items carried forward.
- Statement period and close date.

## Calculation rule
When files are provided and a code tool is available, match in code (pandas). Report match counts and unmatched totals for each side.

## Procedure
1. **Roll forward prior items.** For each outstanding check and deposit in transit from last period, check whether it cleared this period. If an item is still open, carry it forward and age it.
2. **Match.** Run three passes, in this order:
   - Pass 1: exact amount plus check number.
   - Pass 2: exact amount within a ±5-day window.
   - Pass 3: one-to-many (batched deposits, split payments).
   Never force a match on amount alone when there are several candidates. List those as ambiguous instead.
3. **Classify unmatched items.**
   - Bank side (no entry needed): deposits in transit, outstanding checks, bank errors.
   - Book side (needs a JE): bank fees, NSF items, interest earned, collections or ACH not recorded, book errors.
4. **Build the two-sided reconciliation.**
   - Adjusted bank = Balance per bank + Deposits in transit − Outstanding checks ± Bank errors.
   - Adjusted book = Balance per books + Unrecorded credits (interest, collections) − Unrecorded debits (fees, NSF) ± Book errors.
   - Adjusted bank MUST equal adjusted book, to the cent.
5. **Propose journal entries** for every book-side item. Bank-side items get no entry.

## Difference diagnostics (when it won't tie)
- Difference divisible by 9: likely a transposition (e.g., 540 entered as 450).
- Difference equals 2 × one item: a sign flip (a debit posted as a credit).
- Difference equals one item exactly: a missing or duplicate entry.
- Voided checks still in the GL, cutoff errors (deposits recorded in the wrong period), and checks recorded at the wrong amount.

## Flags
- Deposits in transit older than ~5 business days.
- Outstanding checks older than 90 days. These are stale; consider voiding, and escheatment rules at roughly 1–5 years depending on the state.
- Recurring unexplained differences.
- Transfers between company accounts that don't appear on both sides (possible kiting).

## Output
1. The reconciliation in standard two-sided format, with PASS/FAIL on the tie.
2. Schedules of outstanding checks and deposits in transit, with ages.
3. Proposed journal entries.
4. Unmatched and ambiguous items with next steps.
5. Assumptions.

## Worked example
Bank side:
- Balance per bank: 10,000.
- Deposit in transit: +2,000.
- Outstanding checks: −3,500.
- Adjusted bank balance: **8,500**.

Book side:
- Balance per books: 8,820.
- Bank service charge: −40.
- NSF customer check: −300.
- Interest earned: +20.
- Adjusted book balance: **8,500**. PASS.

Proposed JEs:
- Dr Bank fees 40 / Cr Cash 40.
- Dr AR 300 / Cr Cash 300.
- Dr Cash 20 / Cr Interest income 20.

## Boundaries
This prepares work for review. The reviewer approves the JEs and any write-off of stale items.