---
name: "cash-flow-indirect"
description: "Use when preparing, reviewing, or explaining a statement of cash flows or operating cash flow by the indirect method, or reconciling net income to cash from operations (US GAAP, ASC 230)."
---

# Statement of Cash Flows — Indirect Method (ASC 230)

## Modes
- **Prepare**: build the statement from the user's numbers.
- **Review**: check a statement someone else prepared against the tie-outs below.
- **Explain / FAR**: walk through why each adjustment has its sign. If the user says "quiz me", give a small problem, wait for their answer, then grade it line by line.

## Inputs (list what's missing before starting; never plug a number to force a tie)
- Beginning and ending balance sheets (include restricted cash).
- Income statement for the period.
- PP&E / intangible detail: purchases, disposals (cost, accumulated depreciation, proceeds), impairments.
- Debt activity: issuances, repayments, discount/premium amortization, extinguishment costs.
- Equity activity: stock issued, treasury stock, dividends declared.
- Noncash transactions: assets acquired with debt or stock, conversions, finance-lease ROU assets.
- Framework (US GAAP vs IFRS). Default to US GAAP and say so.

## Calculation rule
When a code tool is available, compute in code (Python/pandas) and show the tables. Otherwise show every arithmetic step. Never estimate.

## Procedure
1. **Start with net income.** Consolidated net income includes the noncontrolling interest.
2. **Remove noncash items and non-operating gains/losses.**
   - Add: depreciation, amortization, impairment, stock-based compensation, amortization of bond discount, operating-lease ROU amortization (noncash lease cost), losses on sale/extinguishment.
   - Subtract: gains on sale, amortization of bond premium, equity-method income (then add distributions received that are returns on investment).
   - Deferred taxes: add an increase in the DTL, subtract an increase in the DTA.
   - Bad debts: if you use the change in *net* AR, do not add bad-debt expense separately (double count).
3. **Working capital (operating items only).** An increase in a current operating asset is subtracted; an increase in a current operating liability is added.
   - Operating: AR, inventory, prepaids, AP, accrued liabilities, interest payable, income taxes payable, deferred revenue.
   - NOT operating: short-term notes to banks, current portion of LTD, dividends payable (financing); non-trading short-term investments (investing).
4. **Investing.**
   - PP&E purchases come from the roll-forward: Purchases = Ending gross PP&E − Beginning + Cost of disposals.
   - Disposal proceeds = NBV + gain (or − loss).
   - Also includes investments bought or sold and loans made or collected.
5. **Financing.**
   - Debt issued or repaid, stock issued, treasury stock, finance-lease principal payments, debt extinguishment costs.
   - Dividends paid = Beginning dividends payable + Declared − Ending dividends payable.
6. **Noncash investing/financing disclosure.** Report these separately, never in the body.
7. **Supplemental disclosures** (required under the indirect method).
   - Interest paid = Interest expense − discount amortization + premium amortization − increase in interest payable.
   - Taxes paid = Tax expense − increase in taxes payable − increase in DTL + increase in DTA (+ increase in prepaid taxes).

## Classification traps (US GAAP)
- Interest paid, interest received, and dividends received are operating; dividends paid are financing. IFRS allows choices, so flag if the user is on IFRS.
- Debt prepayment/extinguishment costs are financing.
- Contingent consideration paid more than ~3 months after an acquisition: up to the acquisition-date fair value is financing, and the excess is operating.
- Insurance proceeds are classified by the nature of the loss.
- Restricted cash is included in the beginning and ending cash totals.
- Trading securities are classified by their purpose (usually operating).
- Finance leases: principal is financing, interest is operating. Operating-lease payments are operating.

## Tie-outs (all must pass; report each as PASS/FAIL)
1. CFO + CFI + CFF = change in cash, cash equivalents, and restricted cash, to the dollar.
2. **Account-coverage table**: every balance sheet line's change is used exactly once (or explained as noncash).
3. Retained earnings: Beginning + NI − Dividends declared = Ending.
4. Accumulated depreciation: Beginning + Depreciation − AD on disposals = Ending.

If a tie-out fails, stop and show the unexplained difference by account. Do not adjust a line to force it.

## Output
1. Statement of cash flows (operating, investing, financing, net change, beginning and ending cash).
2. Noncash investing/financing disclosure and supplemental cash paid for interest and taxes.
3. Account-coverage table: account, change, where it landed.
4. Tie-out results.
5. Assumptions and open questions.

## Worked example
Facts:
- NI 100; depreciation 30.
- Sold equipment: cost 40, AD 25 (NBV 15), proceeds 20, so the gain is 5.
- AR +15, inventory −10, AP +8, accrued liabilities −3.
- Gross PP&E 200 → 260.
- New debt 50. Dividends declared 40; dividends payable 10 → 15.

CFO = 100 + 30 − 5 − 15 + 10 + 8 − 3 = **125**

CFI:
- Purchases = 260 − 200 + 40 = 100.
- CFI = 20 − 100 = **−80**.

CFF:
- Dividends paid = 10 + 40 − 15 = 35.
- CFF = 50 − 35 = **15**.

Net change in cash = 125 − 80 + 15 = **60**. This must equal the balance sheet change in cash.

## Boundaries
This prepares work for review. Final classification judgments on unusual items go to the reviewer. Use client IDs, not names, if firm policy requires it.