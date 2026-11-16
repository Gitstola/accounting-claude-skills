---
name: "journal-entry-review"
description: "Use when reviewing, testing, or screening journal entries or GL detail for errors, control issues, or fraud-risk indicators: close review, SOX review, or audit JE testing (AS 2401 / AU-C 240)."
---

# Journal Entry Review and Risk Screening

A flag is a request for support, never a conclusion. Never label an entry as fraud or an error.

## Inputs (list what's missing)
- JE population with these fields:
  - JE ID, line, posted date, effective date.
  - Preparer, approver.
  - Account, debit, credit, description.
  - Source (manual, system, top-side).
- Beginning and ending trial balance for the period.
- Chart of accounts, user/role list, close calendar (period-end and close dates), approval matrix and thresholds, materiality.

## Calculation rule
When a file is provided and a code tool is available, load it with pandas and run every test in code. Report counts and totals so the work is reproducible.

## Step 1 — Population completeness (do this first)
- For every account: Beginning TB + net JE activity = Ending TB.
- Record the count of entries and total debits/credits.
- If the population does not reconcile, STOP and report the difference by account. Screening an incomplete population is worthless.

## Step 2 — Integrity
- Each JE balances (debits = credits).
- No duplicate JE IDs, and no duplicate lines (same amount, account, and date) without explanation.
- Effective dates fall within the period.

## Step 3 — Risk criteria (tag every entry that hits; each tag needs a stated reason)
**Timing**
- Posted after period end or after the close date.
- Posted on weekends or holidays, or in the last days of the period.
- Effective date ≠ posted date (possible backdating).

**People / segregation of duties**
- Preparer = approver, or no approver.
- Approver lacks authority for the amount.
- Preparer doesn't normally post to the account.
- Senior management posting directly.
- Generic, admin, or terminated user IDs.

**Amount**
- Round amounts (e.g., exact thousands).
- Just below an approval threshold.
- Large relative to the account's normal activity or to materiality.
- First-digit (Benford) deviations. Use only with large populations and note the limitation.

**Accounts**
- Unusual pairings: revenue ↔ expense; revenue ↔ cash bypassing AR; revenue ↔ reserves.
- Entries to estimates and reserves, suspense or clearing accounts, intercompany, or equity.
- Seldom-used accounts.

**Description and pattern**
- Blank or vague descriptions ("adj", "misc", "reclass", "per [name]").
- Entries reversed shortly after posting or at the start of the next period.
- Recurring entries whose amount changed materially.
- Manual top-side or consolidation entries.

## Step 4 — Rank
Score = sum of tag severities.
- High = 3: post-close; SoD failure; revenue/reserve manipulation patterns; top-side.
- Medium = 2: threshold-avoidance; unusual pairing; senior-management posting.
- Low = 1: round amount; vague description; weekend posting.

State the scoring so the reviewer can change it.

## Step 5 — Follow-up
For each flagged entry, state:
- The support to obtain (invoice, calculation, contract, approval evidence).
- The specific question for the preparer.
- What evidence would clear it.

## Output
1. Population reconciliation (PASS/FAIL), counts and totals.
2. Summary: entries tested, entries flagged by criterion, total dollars flagged.
3. Risk-ranked table: JE ID, posted/effective date, preparer/approver, accounts, amount, tags with reasons, score, support needed.
4. Patterns across entries (same user, same account, same week).
5. Open questions and limitations (e.g., missing approver field).

## Worked example
JE 1047:
- Effective 12/31, posted 1/6, after the 1/5 close.
- Dr AR 50,000 / Cr Revenue 50,000.
- Description "per CFO".
- Prepared and approved by the same controller ID.

Tags:
- Post-close (3).
- SoD failure (3).
- Revenue entry near period end (3).
- Round amount (1).
- Vague description (1).

Score 11, HIGH.

Obtain the contract, shipping/delivery evidence dated before 12/31, and independent approval. Ask why it was booked after close and who requested it.

## Boundaries
Screening only. The reviewer or audit team decides dispositions, proposed adjustments, and any escalation. Use client IDs rather than names if firm policy requires.