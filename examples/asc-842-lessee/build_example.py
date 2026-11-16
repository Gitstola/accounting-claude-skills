"""Build the copier-lease sample deliverable (eval Case 21) with every number computed here.

Run: python build_example.py   -> writes copier-lease-deliverable.md and schedule.json
"""
import json
from pathlib import Path

HERE = Path(__file__).parent

# Facts
TERM, PMT, RATE = 4, 15_000.00, 0.06
IDC, INCENTIVE = 1_000.00, 2_000.00
FV, LIFE = 80_000.00, 8


def c(x):
    return round(x + 0.0, 2)


def m(x):
    return f"{0.0 if abs(x) < 0.005 else x:,.2f}"


# Initial measurement (full precision throughout; rounded only for display, same as the workbook)
df = [1 / (1 + RATE) ** t for t in range(1, TERM + 1)]
pv_factor = sum(df)
liability0 = PMT * pv_factor
rou0 = liability0 + IDC - INCENTIVE
total_cost = PMT * TERM + IDC - INCENTIVE
sl_cost = total_cost / TERM

# Classification tests
pv_pct = liability0 / FV
term_pct = TERM / LIFE
tests = [
    ("1. Ownership transfer", "None", "Not met"),
    ("2. Purchase option reasonably certain", "None", "Not met"),
    ("3. Major part of economic life (75%)", f"{TERM} / {LIFE} yrs = {term_pct:.1%}", "Not met"),
    ("4. PV ≥ substantially all of fair value (90%)", f"{m(liability0)} / {m(FV)} = {pv_pct:.1%}", "Not met"),
    ("5. Specialized asset", "Copiers have alternative use", "Not met"),
]
classification = "Operating" if term_pct < 0.75 and pv_pct < 0.90 else "Finance"

# Schedule at full precision (no plug needed: balances land on zero)
rows = []
L, R = liability0, rou0
for yr in range(1, TERM + 1):
    accr = L * RATE
    amort = sl_cost - accr               # operating lease: ROU amortization is the plug
    principal = PMT - accr
    end_L, end_R = L - principal, R - amort
    rows.append(dict(year=yr, beg_liab=L, payment=PMT, accretion=accr, principal=principal,
                     end_liab=end_L, beg_rou=R, rou_amort=amort, end_rou=end_R, expense=accr + amort))
    L, R = end_L, end_R

# Tie-outs (each difference should be 0 within half a cent)
tie = []
tie.append(("1. Liability roll-forward ends at 0", abs(rows[-1]["end_liab"]) < 0.005))
tie.append(("2. ROU roll-forward ends at 0", abs(rows[-1]["end_rou"]) < 0.005))
tie.append(("3. Total lease cost = payments + IDC − incentives",
            abs(sum(r["expense"] for r in rows) - total_cost) < 0.005))
tie.append(("4. Finance-lease lifetime total", None))   # N/A for an operating lease
undiscounted = PMT * TERM
imputed = sum(r["accretion"] for r in rows)              # total interest over the term
tie.append(("5. Maturity table less imputed interest = liability", abs(undiscounted - imputed - liability0) < 0.005))

# Current / noncurrent
cur0 = rows[0]["principal"]
non0 = liability0 - cur0
cur1 = rows[1]["principal"]
non1 = rows[0]["end_liab"] - cur1

# Journal entries must balance to the cent as displayed
assert c(rou0) + c(INCENTIVE) == c(liability0) + c(IDC)
assert c(rows[0]["expense"]) + c(rows[0]["principal"]) == c(PMT) + c(rows[0]["rou_amort"])

json.dump(dict(liability0=liability0, rou0=rou0, sl_cost=sl_cost, rows=rows, imputed=imputed,
               current0=cur0, noncurrent0=non0), open(HERE / "schedule.json", "w"), indent=2)


def table(header, body):
    out = ["| " + " | ".join(header) + " |", "|" + "|".join("---" for _ in header) + "|"]
    out += ["| " + " | ".join(r) + " |" for r in body]
    return "\n".join(out)


md = []
md.append("# Sample deliverable: copier fleet lease (ASC 842, lessee)\n")
md.append("This is the full client-file output the `asc-842-lessee` skill is built to produce, run on eval Case 21. "
          "Every number below is computed in `build_example.py`; the matching Excel workpaper with live formulas is "
          "`copier-lease-workpaper.xlsx`.\n")
md.append("**Facts.** Copier fleet. Commencement January 1, Year 1. Term 4 years; payments of $15,000 annually in "
          "arrears (December 31). IBR 6% (implicit rate not determinable). Initial direct costs $1,000 paid by the lessee; "
          "$2,000 cash incentive received from the lessor at commencement. Fair value $80,000; economic life 8 years. "
          "No options, guarantees, or ownership transfer; not specialized. Year-end December 31.\n")

md.append("## 1. Classification memo\n")
md.append(table(["Test", "Numbers", "Result"], tests))
md.append(f"\n**Conclusion: {classification.lower()} lease.** None of the five finance-lease criteria is met.\n")

md.append("## 2. Initial measurement\n")
md.append(f"- PV factor, ordinary annuity, 4 periods at 6%: {pv_factor:.6f}")
md.append(f"- Lease liability = 15,000 × {pv_factor:.6f} = **{m(liability0)}**")
md.append(f"- ROU asset = {m(liability0)} + {m(IDC)} IDC − {m(INCENTIVE)} incentive = **{m(rou0)}**")
md.append(f"- Straight-line lease cost = ({m(PMT*TERM)} + {m(IDC)} − {m(INCENTIVE)}) ÷ 4 = **{m(sl_cost)}** per year\n")

md.append("## 3. Schedule\n")
md.append("Operating lease: the liability accretes at 6%, and ROU amortization is the plug (straight-line cost − accretion), "
          "not straight-line.\n")
md.append(table(
    ["Year", "Beg. liability", "Payment", "Accretion", "Principal", "End liability",
     "Beg. ROU", "ROU amortization", "End ROU", "Lease expense"],
    [[str(r["year"]), m(r["beg_liab"]), m(r["payment"]), m(r["accretion"]), m(r["principal"]), m(r["end_liab"]),
      m(r["beg_rou"]), m(r["rou_amort"]), m(r["end_rou"]), m(r["expense"])] for r in rows] +
    [["Total", "", m(PMT*TERM), m(sum(r["accretion"] for r in rows)), m(sum(r["principal"] for r in rows)), "",
      "", m(sum(r["rou_amort"] for r in rows)), "", m(sum(r["expense"] for r in rows))]]))
md.append("\nRounding: computed at full precision and displayed to cents, so no final-period plug is needed.\n")

md.append("## 4. Journal entries\n")
md.append("**January 1, Year 1 (commencement)**\n")
md.append(table(["Account", "Dr", "Cr"], [
    ["ROU asset", m(rou0), ""],
    ["Cash (incentive received)", m(INCENTIVE), ""],
    ["Lease liability", "", m(liability0)],
    ["Cash (initial direct costs paid)", "", m(IDC)],
]))
r1 = rows[0]
md.append("\n**December 31, Year 1 (payment and lease cost)**\n")
md.append(table(["Account", "Dr", "Cr"], [
    ["Lease expense (straight-line)", m(r1["expense"]), ""],
    ["Lease liability (payment − accretion)", m(r1["principal"]), ""],
    ["Cash", "", m(PMT)],
    ["ROU asset (straight-line cost − accretion)", "", m(r1["rou_amort"])],
]))
md.append("")

md.append("## 5. Presentation\n")
md.append("Current portion = principal reduction over the next 12 months, not the next 12 months of payments.\n")
md.append(table(["Balance sheet date", "Current", "Noncurrent", "Total liability"], [
    ["January 1, Year 1", m(cur0), m(non0), m(liability0)],
    ["December 31, Year 1", m(cur1), m(non1), m(rows[0]["end_liab"])],
]))
md.append("\n**Maturity table at commencement**\n")
md.append(table(["Year", "Undiscounted payment"],
                [[f"Year {y}", m(PMT)] for y in range(1, TERM + 1)] +
                [["Total undiscounted", m(undiscounted)], ["Less imputed interest", f"({m(imputed)})"],
                 ["Lease liability", m(liability0)]]))
md.append("\nCash flow statement: operating-lease payments are operating cash outflows.\n")

md.append("## 6. Flags for the reviewer\n")
md.append("- **Discount rate (judgment):** 6% IBR; implicit rate not determinable. Support the IBR with a lender quote or rate curve for a 4-year secured borrowing.")
md.append("- **Lease term (judgment):** 4 years; no renewal or termination options. Confirm none exist in side letters or the master agreement.")
md.append("- **Components:** confirm whether the payments include service or toner charges (nonlease components) and whether the combine expedient is elected.")
md.append("- **Expiration:** lease ends December 31, Year 4; flag for the renewal-or-replace decision in Year 4.\n")

md.append("## 7. Tie-outs and assumptions\n")
md.append(table(["Tie-out", "Result"],
                [[n, "N/A (operating lease)" if ok is None else ("PASS" if ok else "FAIL")] for n, ok in tie]))
md.append("\nAssumptions: commencement January 1, Year 1; payments on December 31; annual compounding; the $1,000 is an "
          "initial direct cost (incremental, incurred only because the lease was obtained); the $2,000 incentive was "
          "received at commencement.\n")

(HERE / "copier-lease-deliverable.md").write_text("\n".join(md))
print("\n".join(md))
