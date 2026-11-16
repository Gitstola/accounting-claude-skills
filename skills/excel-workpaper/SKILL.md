---
name: "excel-workpaper"
description: "Use when turning an accounting calculation, schedule, reconciliation, or analysis into a real Excel workpaper (.xlsx) with live formulas, tie-out checks, tickmarks, cross-references, and preparer/reviewer sign-off."
---

# Excel Workpaper Builder

## Order of work
1. Content first. If an accounting skill covers the topic (cash flow, ASC 842, bank rec, flux, and so on), run its procedure and confirm the numbers before building anything.
2. Then read the xlsx skill's SKILL.md and build the file with it (openpyxl).
3. Recalculate the workbook and verify it before delivering.

## Workbook layout
One tab per purpose:
1. **Cover.** Client or entity ID, period, workpaper reference (e.g., A-1), objective, source documents with dates, preparer and date, reviewer and date (left blank for sign-off), and the conclusion.
2. **Lead / Summary.** Key balances and results, linked by formula to the detail tabs.
3. **Detail / Calc.** The working schedule (e.g., amortization table, rec, roll-forward).
4. **Tie-outs.** Each check is a formula that should equal 0, such as `=Detail!F40-Lead!C8`. Add conditional formatting: red if the absolute value is above 0.01, green otherwise. Add one overall status cell that reads ALL TIED or N ISSUES.
5. **Tickmark legend.** List the tickmarks used, for example:
   - ✓ agreed to source document
   - ∑ footed
   - ⊕ cross-footed
   - ^ traced to GL
   - © recalculated
   Place tickmarks in a column next to the numbers they support.
6. **Notes / Open items.** Assumptions, questions, and follow-ups, each with an owner.

## Formula rules
- Use **live formulas, not pasted values.** Every calculated cell must be a formula that recalculates when its inputs change.
- Never hardcode a number inside a formula. Put each input in its own labeled cell and use named ranges for key inputs, such as the rate, term, and materiality.
- Color-code cells:
  - Inputs: blue font, light yellow fill.
  - Formulas: black font.
  - Links to other tabs: green font.
- Use ROUND only where the presentation requires it. Never round in the middle of a calculation chain.
- Do not use volatile functions (INDIRECT, OFFSET) unless they are necessary.

## Formatting
- Freeze header rows.
- Use accounting number format. Show negatives in parentheses.
- Bold subtotals, with single and double underlines on totals.
- Use consistent column widths.
- Set print area and fit to one page wide.
- Add a footer with the file name, tab name, and page number.
- Cross-reference with workpaper refs (e.g., "see A-2") wherever a number comes from another tab.

## Verification (required before delivering)
1. Recalculate the workbook, for example with LibreOffice headless.
2. Scan every cell for errors: #REF!, #DIV/0!, #VALUE!, #NAME?
3. Confirm every tie-out check equals 0.
4. Spot-check that changing one input changes every dependent output.

If any check fails, fix it and run the verification again. Never deliver a file with a failing tie-out without stating so.

## Delivery
Send the .xlsx file. In one line, state the overall status and anything the reviewer must look at.

## Example layout (ASC 842 operating lease)
- **Inputs:** commencement date, term, payment, timing, rate, IDC, incentives.
- **Detail:** one row per period with the beginning liability, payment, accretion, ending liability, ROU amortization (as a plug), ROU balance, and straight-line expense.
- **Lead:** current and noncurrent liability, ROU, and period expense.
- **Tie-outs:** liability ends at 0; total expense equals total payments plus IDC minus incentives; the maturity table less imputed interest equals the liability.

## Boundaries
The workpaper prepares numbers for review. The reviewer signs off. Use client IDs rather than names if firm policy requires it.