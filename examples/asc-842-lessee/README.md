# Example: copier fleet lease

The full deliverable the `asc-842-lessee` skill produces for eval Case 21, plus the Excel workpaper the `excel-workpaper` skill builds from it.

| File | What it is |
|---|---|
| [`copier-lease-deliverable.md`](copier-lease-deliverable.md) | Classification memo, initial measurement, 10-column schedule, journal entries, current/noncurrent split, maturity table, reviewer flags, tie-outs |
| [`copier-lease-workpaper.xlsx`](copier-lease-workpaper.xlsx) | Workpaper L-0 to L-4: Cover, Inputs, Lead, Detail, Entries, Tie-outs, tickmark Legend, Notes. 110 live formulas, 16 named ranges, no hardcoded results. |
| [`build_example.py`](build_example.py) | Computes every number in the deliverable |
| [`build_workpaper.py`](build_workpaper.py) | Builds the workbook with openpyxl |

**Headline numbers:** operating lease (term 50% of economic life; PV 65% of fair value). Liability 51,976.58, ROU asset 50,976.58, straight-line cost 14,750.00 a year. Year 1 ROU amortization is 11,631.40, the plug of 14,750.00 minus 3,118.60 accretion, not straight-line.

**Checks run before publishing:**
- The workbook was recalculated in LibreOffice with zero formula errors.
- Its schedule matches the Python schedule to within 0.0000001 in every cell.
- All seven numeric tie-outs equal zero (the eighth, a finance-lease check, is N/A).
- Changing the payment and rate inputs flows through every output and still ties.
