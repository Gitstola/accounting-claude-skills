---
name: "quickbooks-cleanup"
description: "Use when reviewing, diagnosing, or cleaning up a QuickBooks Online file: catch-up bookkeeping, uncategorized items, undeposited funds, opening balance equity, aging problems, reconciliations, and year-end readiness."
---

# QuickBooks Online Cleanup and Health Check

## Data source
**If the QuickBooks connector is available, pull these reports read-only:**
- Company info, including accounting basis.
- Balance sheet at period end and at prior year-end.
- P&L by month.
- AR aging detail and AP aging detail.
- Sales by customer.

**If it isn't available, ask for these exports (Excel/CSV):**
- Balance sheet and P&L by month.
- AR and AP aging detail.
- General ledger.
- Reconciliation reports.
- The transaction list for Undeposited Funds and for Uncategorized accounts.

**Calculation rule:** load the data and run every test in code. Report each finding with its amount and supporting transactions.

## Action rule
Diagnose and draft only.
- Never create, edit, delete, send, or post anything in QuickBooks (invoices, payments, payroll, entries) without the user's explicit approval for that specific action.
- Default to giving the user the fix steps.

## Health tests
Run all of these and report each as CLEAN or ISSUE.

1. **Uncategorized income, expense, or asset accounts, and "Ask My Accountant."** Any balance means work is unfinished.
2. **Undeposited Funds (Payments to deposit).** A stale balance usually means:
   - Customer payments were never grouped into bank deposits, AND
   - The bank-feed deposit was categorized to income instead.
   - Result: revenue is double counted. Age the items.
3. **Opening Balance Equity.** It should be zero after setup. Close it to owner equity or retained earnings once the opening balances have been verified.
4. **Accounts receivable.**
   - Old open invoices.
   - Unapplied payments or credits (negative aging).
   - Duplicate invoices.
   - Invoices left open even though the cash was recorded as income through the bank feed.
   - Tie-out: the AR aging total must equal AR on the balance sheet.
5. **Accounts payable.**
   - Old open bills.
   - Unapplied vendor credits.
   - Bills left open because payment was recorded as an expense in the bank feed instead of as a bill payment, so the expense is double counted.
   - Tie-out: the AP aging total must equal AP on the balance sheet.
6. **Bank and credit card reconciliations.**
   - Last reconciled date.
   - Old uncleared items.
   - Discrepancies from edits to already-reconciled transactions.
   - Tie-out: the reconciled balance must equal the statement balance.
7. **Negative balances where they shouldn't exist.** For example: negative cash with no overdraft, negative inventory, negative payroll liabilities, a negative loan balance.
8. **Liabilities that don't clear.**
   - Payroll liabilities should zero out after remittance.
   - Sales tax payable should tie to the filed returns.
9. **Loans.**
   - Payments booked fully to expense instead of split between principal and interest.
   - Tie-out: the balance must equal the lender's statement.
10. **Equity.**
    - The change in retained earnings must equal prior-year net income ± distributions. A mismatch means closed periods were edited; check whether a closing date and password are set.
    - Owner draws and contributions are coded correctly.
    - No personal expenses in operating accounts.
11. **Fixed assets.**
    - Capital purchases that were expensed.
    - No depreciation entries.
    - Tie-out: the fixed asset register must agree to the books.
12. **Clearing and suspense accounts.** These should be zero.
13. **Data hygiene.**
    - Duplicate customers or vendors.
    - A bloated chart of accounts.
    - 1099 vendors not flagged.
    - Accounting basis (cash vs. accrual) inconsistent with reporting needs.

## Fix order
Work in this order, because later fixes depend on earlier ones:
1. Bank and credit card reconciliations.
2. Undeposited Funds, AR, and AP.
3. Uncategorized items.
4. Liabilities: payroll, sales tax, loans.
5. Fixed assets and depreciation.
6. Opening Balance Equity and retained earnings.
7. Set a closing date.

## Output
1. **Health summary:** CLEAN/ISSUE for each test, with total dollars at issue.
2. **Findings table:** issue | account | amount | evidence (transaction IDs or dates) | likely cause | fix steps in QBO | priority.
3. **Proposed adjusting entries** for the user to review and post.
4. **Questions for the client:** missing statements, unknown deposits, owner activity.
5. **Tie-out results:** AR, AP, bank, and retained earnings.

## Worked example
Undeposited Funds shows 12,400 of payments going back 8 months. The bank feed shows matching deposits coded to Sales.

- **Finding:** revenue is likely overstated by up to 12,400, and AR may also be understated.
- **Fix:**
  1. Match each bank-feed deposit to its received payments by recording a bank deposit that groups them, rather than coding the deposit to income.
  2. Recode or exclude the duplicate income entries.
  3. Re-run the P&L and confirm Undeposited Funds is zero.
- **Priority:** high, because it affects revenue and tax.

## Boundaries
Client-facing changes, write-offs, equity entries, and anything in payroll require the user's approval. Prefer that the user executes fixes in QBO. Use client IDs rather than names if firm policy requires it.