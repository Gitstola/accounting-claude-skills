"""Build copier-lease-workpaper.xlsx: an ASC 842 operating-lease workpaper with live formulas.

Run: python build_workpaper.py   (then recalculate, e.g. LibreOffice headless, before reading values)
Layout follows the excel-workpaper skill: Cover, Inputs, Lead, Detail, Entries, Tie-outs, Legend, Notes.
"""
from pathlib import Path

from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.workbook.defined_name import DefinedName

OUT = Path(__file__).parent / "copier-lease-workpaper.xlsx"

ACCT = '_(* #,##0.00_);_(* (#,##0.00);_(* "-"??_);_(@_)'
PCT = "0.0%"
F = "Arial"
BLACK = Font(name=F, size=10)
BOLD = Font(name=F, size=10, bold=True)
TITLE = Font(name=F, size=13, bold=True)
SUB = Font(name=F, size=9, italic=True, color="595959")
INPUT = Font(name=F, size=10, color="0000FF")
LINK = Font(name=F, size=10, color="008000")
INPUT_FILL = PatternFill("solid", fgColor="FFF2CC")
HEAD_FILL = PatternFill("solid", fgColor="D9E1F2")
RED_FILL = PatternFill("solid", fgColor="F8CBAD")
GREEN_FILL = PatternFill("solid", fgColor="C6EFCE")
THIN = Side(style="thin")
DOUBLE = Side(style="double")

wb = Workbook()


def sheet(title, widths):
    ws = wb.create_sheet(title)
    for col, w in widths.items():
        ws.column_dimensions[col].width = w
    ws.sheet_view.showGridLines = False
    ws.oddFooter.left.text = "&F"
    ws.oddFooter.center.text = "&A"
    ws.oddFooter.right.text = "Page &P of &N"
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    return ws


def put(ws, ref, value, font=BLACK, fmt=None, fill=None, align=None):
    c = ws[ref]
    c.value = value
    c.font = font
    if fmt:
        c.number_format = fmt
    if fill:
        c.fill = fill
    if align:
        c.alignment = Alignment(horizontal=align, vertical="top", wrap_text=True)
    return c


def header_row(ws, row, labels, start_col=1):
    for i, label in enumerate(labels):
        c = ws.cell(row=row, column=start_col + i, value=label)
        c.font = BOLD
        c.fill = HEAD_FILL
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)


def name(nm, ref):
    wb.defined_names[nm] = DefinedName(nm, attr_text=ref)


wb.remove(wb.active)

# ---------------------------------------------------------------- Inputs
inp = sheet("Inputs", {"A": 4, "B": 44, "C": 18, "D": 46})
put(inp, "B1", "L-0  Inputs", TITLE)
put(inp, "B2", "Blue cells on yellow are inputs; every other number in the workbook is a formula.", SUB)
header_row(inp, 4, ["Input", "Value", "Source"], start_col=2)
inputs = [
    ("Commencement date", "January 1, Year 1", None, "Lease agreement §2", None),
    ("Lease term (years)", 4, "0", "Lease agreement §3; no renewal or termination options", "Term"),
    ("Annual payment, in arrears (Dec 31)", 15000, ACCT, "Lease agreement §4", "Payment"),
    ("Discount rate (IBR; implicit rate not determinable)", 0.06, "0.00%", "Treasury IBR memo", "Rate"),
    ("Initial direct costs paid by lessee", 1000, ACCT, "Broker invoice", "IDC"),
    ("Lease incentive received at commencement", 2000, ACCT, "Lessor remittance", "Incentive"),
    ("Fair value of the copier fleet", 80000, ACCT, "Lessor quote", "FairValue"),
    ("Economic life (years)", 8, "0", "Fixed asset policy", "EconLife"),
    ("Ownership transfers by end of term? (Yes/No)", "No", None, "Lease agreement", "OwnershipTransfer"),
    ("Purchase option reasonably certain? (Yes/No)", "No", None, "No option in agreement", "PurchaseOption"),
    ("Specialized asset, no alternative use? (Yes/No)", "No", None, "Standard copiers", "Specialized"),
    ("Major-part threshold (policy)", 0.75, PCT, "Accounting policy manual", "MajorPart"),
    ("Substantially-all threshold (policy)", 0.90, PCT, "Accounting policy manual", "SubstantiallyAll"),
]
for i, (label, val, fmt, src, nm) in enumerate(inputs):
    r = 5 + i
    put(inp, f"B{r}", label)
    put(inp, f"C{r}", val, INPUT, fmt, INPUT_FILL, "right")
    put(inp, f"D{r}", src, SUB)
    if nm:
        name(nm, f"Inputs!$C${r}")
inp.freeze_panes = "B5"

# ---------------------------------------------------------------- Detail
det = sheet("Detail", {"A": 22, "B": 16, "C": 14, "D": 14, "E": 14, "F": 16, "G": 16, "H": 16, "I": 16, "J": 16, "K": 6})
put(det, "A1", "L-2  Lease schedule: operating lease", TITLE)
put(det, "A2", "Copier fleet. Feeds L-1 Lead and L-3 Entries; checked on L-4 Tie-outs.", SUB)
put(det, "A4", "Initial measurement", BOLD)
put(det, "A5", "Lease liability at commencement = PV of 4 payments in arrears at the IBR")
put(det, "H5", "=PV(Rate,Term,-Payment)", BLACK, ACCT)
put(det, "I5", "©", BLACK, align="center")
put(det, "A6", "ROU asset = liability + initial direct costs − incentive received")
put(det, "H6", "=H5+IDC-Incentive", BLACK, ACCT)
put(det, "I6", "©", BLACK, align="center")
put(det, "A7", "Straight-line lease cost per year = (total payments + IDC − incentive) ÷ term")
put(det, "H7", "=(Payment*Term+IDC-Incentive)/Term", BLACK, ACCT)
put(det, "I7", "©", BLACK, align="center")
name("Liability0", "Detail!$H$5")
name("ROU0", "Detail!$H$6")
name("SLCost", "Detail!$H$7")

header_row(det, 9, ["Year", "Beg. liability", "Payment", "Accretion", "Principal", "End liability",
                    "Beg. ROU", "ROU amortization (plug)", "End ROU", "Lease expense", "Tick"])
det.row_dimensions[9].height = 30
for i in range(4):
    r = 10 + i
    put(det, f"A{r}", 1 if i == 0 else f"=A{r-1}+1", BLACK, "0", align="center")
    put(det, f"B{r}", "=Liability0" if i == 0 else f"=F{r-1}", BLACK, ACCT)
    put(det, f"C{r}", "=Payment", BLACK, ACCT)
    put(det, f"D{r}", f"=B{r}*Rate", BLACK, ACCT)
    put(det, f"E{r}", f"=C{r}-D{r}", BLACK, ACCT)
    put(det, f"F{r}", f"=B{r}-E{r}", BLACK, ACCT)
    put(det, f"G{r}", "=ROU0" if i == 0 else f"=I{r-1}", BLACK, ACCT)
    put(det, f"H{r}", f"=SLCost-D{r}", BLACK, ACCT)
    put(det, f"I{r}", f"=G{r}-H{r}", BLACK, ACCT)
    put(det, f"J{r}", f"=D{r}+H{r}", BLACK, ACCT)
    put(det, f"K{r}", "©", BLACK, align="center")
put(det, "A14", "Total", BOLD)
for col in "CDEHJ":
    c = put(det, f"{col}14", f"=SUM({col}10:{col}13)", BOLD, ACCT)
    c.border = Border(top=THIN, bottom=DOUBLE)
put(det, "K14", "∑", BLACK, align="center")
det.freeze_panes = "B10"

put(det, "A16", "Maturity table at commencement (see L-1)", BOLD)
header_row(det, 17, ["Year", "Undiscounted payment"])
for i in range(4):
    r = 18 + i
    put(det, f"A{r}", f"=A{10+i}", BLACK, "0", align="center")
    put(det, f"B{r}", f"=C{10+i}", BLACK, ACCT)
put(det, "A22", "Total", BOLD)
c = put(det, "B22", "=SUM(B18:B21)", BOLD, ACCT)
c.border = Border(top=THIN)
put(det, "A23", "Less imputed interest")
put(det, "B23", "=-D14", BLACK, ACCT)
put(det, "A24", "Lease liability", BOLD)
c = put(det, "B24", "=B22+B23", BOLD, ACCT)
c.border = Border(top=THIN, bottom=DOUBLE)
put(det, "C22", "∑", BLACK, align="center")

# ---------------------------------------------------------------- Lead
lead = sheet("Lead", {"A": 4, "B": 50, "C": 18, "D": 16, "E": 14, "F": 6})
put(lead, "B1", "L-1  Lead: classification and key balances", TITLE)
put(lead, "B2", "Green = linked from another tab (see the Ref column).", SUB)
header_row(lead, 4, ["Classification test (ASC 842-10-25-2)", "Measure", "Threshold", "Result"], start_col=2)
tests = [
    ("1. Ownership transfers by end of term", "=OwnershipTransfer", None, '=IF(C5="Yes","Met","Not met")'),
    ("2. Purchase option reasonably certain", "=PurchaseOption", None, '=IF(C6="Yes","Met","Not met")'),
    ("3. Term ÷ economic life (major part)", "=Term/EconLife", "=MajorPart", '=IF(C7>=D7,"Met","Not met")'),
    ("4. PV of payments ÷ fair value (L-2)", "=Liability0/FairValue", "=SubstantiallyAll", '=IF(C8>=D8,"Met","Not met")'),
    ("5. Specialized, no alternative use", "=Specialized", None, '=IF(C9="Yes","Met","Not met")'),
]
for i, (label, meas, thr, res) in enumerate(tests):
    r = 5 + i
    put(lead, f"B{r}", label)
    is_pct = thr is not None
    put(lead, f"C{r}", meas, LINK, PCT if is_pct else None, align="right")
    if thr:
        put(lead, f"D{r}", thr, LINK, PCT, align="right")
    put(lead, f"E{r}", res, BLACK, align="center")
put(lead, "B10", "Classification", BOLD)
put(lead, "E10", '=IF(COUNTIF(E5:E9,"Met")>0,"Finance","Operating")', BOLD, align="center")

header_row(lead, 12, ["Key balances", "Amount", "Ref"], start_col=2)
balances = [
    ("Lease liability at commencement", "=Liability0", "L-2"),
    ("ROU asset at commencement", "=ROU0", "L-2"),
    ("Current portion at commencement (next 12 months' principal)", "=Detail!E10", "L-2"),
    ("Noncurrent portion at commencement", "=Liability0-Detail!E10", "L-2"),
    ("Lease liability at Dec 31, Year 1", "=Detail!F10", "L-2"),
    ("  Current portion at Dec 31, Year 1", "=Detail!E11", "L-2"),
    ("  Noncurrent portion at Dec 31, Year 1", "=Detail!F10-Detail!E11", "L-2"),
    ("ROU asset at Dec 31, Year 1", "=Detail!I10", "L-2"),
    ("Year 1 lease expense (single straight-line cost)", "=Detail!J10", "L-2"),
    ("Year 1 operating cash outflow", "=Detail!C10", "L-2"),
]
for i, (label, f, ref) in enumerate(balances):
    r = 13 + i
    put(lead, f"B{r}", label)
    put(lead, f"C{r}", f, LINK, ACCT)
    put(lead, f"D{r}", ref, SUB, align="center")
lead.freeze_panes = "B5"

# ---------------------------------------------------------------- Entries
je = sheet("Entries", {"A": 4, "B": 46, "C": 16, "D": 16})
put(je, "B1", "L-3  Journal entries", TITLE)
put(je, "B2", "Amounts link to L-0 Inputs and L-2 Detail.", SUB)
header_row(je, 4, ["Jan 1, Year 1: commencement", "Dr", "Cr"], start_col=2)
rows = [("ROU asset", "=ROU0", None), ("Cash (incentive received)", "=Incentive", None),
        ("Lease liability", None, "=Liability0"), ("Cash (initial direct costs paid)", None, "=IDC")]
for i, (acct, dr, cr) in enumerate(rows):
    r = 5 + i
    put(je, f"B{r}", acct if dr else "      " + acct)
    if dr:
        put(je, f"C{r}", dr, LINK, ACCT)
    if cr:
        put(je, f"D{r}", cr, LINK, ACCT)
put(je, "B9", "Totals", BOLD)
for col in "CD":
    c = put(je, f"{col}9", f"=SUM({col}5:{col}8)", BOLD, ACCT)
    c.border = Border(top=THIN, bottom=DOUBLE)

header_row(je, 11, ["Dec 31, Year 1: payment and lease cost", "Dr", "Cr"], start_col=2)
rows = [("Lease expense (straight-line)", "=Detail!J10", None),
        ("Lease liability (payment − accretion)", "=Detail!E10", None),
        ("Cash", None, "=Detail!C10"),
        ("ROU asset (straight-line cost − accretion)", None, "=Detail!H10")]
for i, (acct, dr, cr) in enumerate(rows):
    r = 12 + i
    put(je, f"B{r}", acct if dr else "      " + acct)
    if dr:
        put(je, f"C{r}", dr, LINK, ACCT)
    if cr:
        put(je, f"D{r}", cr, LINK, ACCT)
put(je, "B16", "Totals", BOLD)
for col in "CD":
    c = put(je, f"{col}16", f"=SUM({col}12:{col}15)", BOLD, ACCT)
    c.border = Border(top=THIN, bottom=DOUBLE)

# ---------------------------------------------------------------- Tie-outs
tie = sheet("Tie-outs", {"A": 4, "B": 56, "C": 16, "D": 10})
put(tie, "B1", "L-4  Tie-outs", TITLE)
put(tie, "B2", "Each check is a difference that should be 0. Red if |difference| > 0.01.", SUB)
header_row(tie, 4, ["Check", "Difference", "Flag"], start_col=2)
checks = [
    ("1. Liability roll-forward ends at 0 (L-2 F13)", "=Detail!F13"),
    ("2. ROU roll-forward ends at 0 (L-2 I13)", "=Detail!I13"),
    ("3. Total lease cost − (payments + IDC − incentive)", "=Detail!J14-(Payment*Term+IDC-Incentive)"),
    ("4. Finance lease: interest + amortization = lifetime total", "N/A (operating)"),
    ("5. Maturity table less imputed interest − liability", "=Detail!B24-Liability0"),
    ("6. Commencement entry balances (L-3)", "=Entries!C9-Entries!D9"),
    ("7. Year 1 entry balances (L-3)", "=Entries!C16-Entries!D16"),
    ("8. Principal over the term = initial liability", "=Detail!E14-Liability0"),
]
for i, (label, f) in enumerate(checks):
    r = 5 + i
    put(tie, f"B{r}", label)
    put(tie, f"C{r}", f if not f.startswith("=") else f"=ROUND({f[1:]},2)", BLACK, ACCT, align="right")
    put(tie, f"D{r}", f"=IF(ISNUMBER(C{r}),IF(ABS(C{r})>0.01,1,0),0)", BLACK, "0", align="center")
last = 4 + len(checks)
put(tie, f"B{last+2}", "Overall status", BOLD)
put(tie, f"C{last+2}", f'=IF(SUM(D5:D{last})=0,"ALL TIED",SUM(D5:D{last})&" ISSUES")', BOLD, align="center")
rng = f"C5:C{last}"
tie.conditional_formatting.add(rng, FormulaRule(formula=["AND(ISNUMBER(C5),ABS(C5)>0.01)"], fill=RED_FILL))
tie.conditional_formatting.add(rng, FormulaRule(formula=["AND(ISNUMBER(C5),ABS(C5)<=0.01)"], fill=GREEN_FILL))
tie.conditional_formatting.add(f"C{last+2}", FormulaRule(formula=[f'C{last+2}="ALL TIED"'], fill=GREEN_FILL))
tie.conditional_formatting.add(f"C{last+2}", FormulaRule(formula=[f'C{last+2}<>"ALL TIED"'], fill=RED_FILL))
name("TieStatus", f"'Tie-outs'!$C${last+2}")

# ---------------------------------------------------------------- Legend
leg = sheet("Legend", {"A": 4, "B": 8, "C": 50})
put(leg, "B1", "Tickmark legend", TITLE)
for i, (t, d) in enumerate([("✓", "Agreed to source document"), ("∑", "Footed"), ("⊕", "Cross-footed"),
                            ("^", "Traced to GL"), ("©", "Recalculated")]):
    put(leg, f"B{3+i}", t, BOLD, align="center")
    put(leg, f"C{3+i}", d)

# ---------------------------------------------------------------- Notes
notes = sheet("Notes", {"A": 4, "B": 70, "C": 18})
put(notes, "B1", "Notes and open items", TITLE)
header_row(notes, 3, ["Item", "Owner"], start_col=2)
for i, (item, owner) in enumerate([
    ("IBR of 6%: support with a lender quote or rate curve for a 4-year secured borrowing.", "Preparer"),
    ("Lease term: confirm no renewal or termination options in side letters or the master agreement.", "Preparer"),
    ("Components: confirm whether payments include service or toner charges and whether the combine expedient is elected.", "Preparer"),
    ("Schedule rows are built for a 4-year term; extend Detail rows if the term input changes.", "Preparer"),
    ("Expiration Dec 31, Year 4: flag the renew-or-replace decision in Year 4.", "Reviewer"),
]):
    put(notes, f"B{4+i}", item, align="left")
    put(notes, f"C{4+i}", owner)

# ---------------------------------------------------------------- Cover (first tab)
cov = sheet("Cover", {"A": 4, "B": 26, "C": 70})
wb.move_sheet("Cover", offset=-(len(wb.sheetnames) - 1))
put(cov, "B1", "ASC 842 lessee workpaper: copier fleet lease", TITLE)
put(cov, "B2", "Sample file built by the asc-842-lessee and excel-workpaper skills (eval Case 21). Illustrative facts.", SUB)
cover = [
    ("Entity / client ID", "SAMPLE-001"),
    ("Period", "Fiscal Year 1 (year-end December 31)"),
    ("Workpaper ref", "L-1 to L-4"),
    ("Objective", "Classify the copier fleet lease, measure the lease liability and ROU asset, and support Year 1 entries and presentation."),
    ("Source documents", "Lease agreement; broker invoice; lessor remittance; treasury IBR memo (see L-0 Inputs)"),
    ("Prepared by / date", "[Preparer] / [date]"),
    ("Reviewed by / date", ""),
    ("Conclusion", '="Classification: "&Lead!E10&". Liability at commencement "&TEXT(Liability0,"#,##0.00")'
                   '&"; Year 1 lease expense "&TEXT(Detail!J10,"#,##0.00")&". Tie-outs: "&TieStatus&"."'),
]
for i, (k, v) in enumerate(cover):
    r = 4 + i
    put(cov, f"B{r}", k, BOLD, align="left")
    put(cov, f"C{r}", v, LINK if str(v).startswith("=") else BLACK, align="left")

order = ["Cover", "Inputs", "Lead", "Detail", "Entries", "Tie-outs", "Legend", "Notes"]
wb._sheets = [wb[n] for n in order]
wb.active = 0
wb.save(OUT)
print(f"wrote {OUT}")
