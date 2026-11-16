"""Build cases.md and answer_key.json for s-corp-basis.
Every expected value comes from the engine below, which applies IRC 1366-1368
and Reg. 1.1367-1 / 1.1367-2 in the Form 7203 order."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import q, write_suite

YN = ["yes", "no"]
CHAR = ["long-term capital gain", "short-term capital gain", "ordinary income", "dividend", "not taxable"]


def year(stock, debt=0.0, face=0.0, contrib=0.0, income=0.0, exempt=0.0, dist=0.0, nonded=0.0,
         losses=None, carry=None, election=False):
    """One year for a shareholder with no accumulated E&P. Returns a dict."""
    losses, carry = dict(losses or {}), dict(carry or {})
    r = {}
    stock = stock + contrib + income + exempt
    r["stock_before_dist"] = stock
    nontax = min(dist, stock)
    r["dist_gain"] = dist - nontax
    stock -= nontax
    total = {k: losses.get(k, 0) + carry.get(k, 0) for k in set(losses) | set(carry)}
    tot = sum(total.values())

    def take_nonded(stock, debt):
        on_stock = min(nonded, stock); stock -= on_stock
        on_debt = min(nonded - on_stock, debt); debt -= on_debt
        return stock, debt, on_stock + on_debt

    def take_losses(stock, debt):
        avail = stock + debt
        allowed = min(tot, avail)
        ratio = (allowed / tot) if tot else 0
        al = {k: v * ratio for k, v in total.items()}
        on_stock = min(allowed, stock); stock -= on_stock
        debt -= (allowed - on_stock)
        return stock, debt, al

    if election:  # Reg. 1.1367-1(g): losses first, unused nondeductible carries forward
        stock, debt, al = take_losses(stock, debt)
        stock, debt, nd_used = take_nonded(stock, debt)
        r["nonded_carry"] = nonded - nd_used
    else:
        stock, debt, nd_used = take_nonded(stock, debt)
        stock, debt, al = take_losses(stock, debt)
        r["nonded_carry"] = 0.0
    r["nonded_used"] = nd_used
    r["allowed"] = al
    r["allowed_total"] = sum(al.values())
    r["suspended"] = {k: total[k] - al[k] for k in total}
    r["suspended_total"] = tot - r["allowed_total"]
    # Restoration of debt basis from the year's net increase (1367(b)(2)(B))
    net_increase = (income + exempt) - dist - nonded - tot
    restore = max(0.0, min(net_increase, face - debt, stock))
    stock -= restore; debt += restore
    r["restore"] = restore
    r["stock_end"], r["debt_end"] = stock, debt
    return r


def repayment(repaid, debt_basis, face):
    nontax = repaid * debt_basis / face
    return dict(nontax=nontax, gain=repaid - nontax, basis_end=debt_basis - nontax, face_end=face - repaid)


C = []

# 1 ordering, nothing limited
r = year(50000, income=20000, exempt=3000, dist=15000, nonded=2000, losses={"s179": 6000})
C.append(dict(n=1, title="Ordering with no limits", facts="""
Sole shareholder. Beginning stock basis 50,000. No shareholder loans. The corporation has never been a C corporation.
K-1 for the year: ordinary income 20,000; tax-exempt interest 3,000; nondeductible expenses 2,000; section 179 deduction 6,000; distributions 15,000.""",
    questions=[q("1a", "Taxable amount of the distribution.", r["dist_gain"]),
               q("1b", "Ending stock basis.", r["stock_end"]),
               q("1c", "Is Form 7203 required this year?", "yes", choices=YN)]))

# 2 distribution above basis
r = year(8000, income=5000, dist=20000)
C.append(dict(n=2, title="Distribution above stock basis", facts="""
Beginning stock basis 8,000. No shareholder loans. No accumulated E&P. Stock held for 3 years.
K-1: ordinary income 5,000; distributions 20,000.""",
    questions=[q("2a", "Gain recognized on the distribution.", r["dist_gain"]),
               q("2b", "Character of that gain.", "long-term capital gain", choices=CHAR),
               q("2c", "Ending stock basis.", r["stock_end"])]))

# 3 single loss limited
r = year(12000, losses={"ord": 30000})
C.append(dict(n=3, title="Loss limited by stock basis", facts="""
Beginning stock basis 12,000. No shareholder loans. K-1: ordinary loss 30,000. No distributions.""",
    questions=[q("3a", "Ordinary loss allowed this year under the basis limit.", r["allowed"]["ord"]),
               q("3b", "Loss suspended and carried forward.", r["suspended"]["ord"]),
               q("3c", "Ending stock basis.", r["stock_end"])]))

# 4 pro rata
r = year(20000, dist=4000, nonded=1000, losses={"ord": 30000, "char": 6000, "s1231": 4000})
C.append(dict(n=4, title="Several loss items exceed basis", facts="""
Beginning stock basis 20,000. No shareholder loans. No accumulated E&P.
K-1: ordinary loss 30,000; charitable contributions 6,000; net section 1231 loss 4,000; nondeductible expenses 1,000; distributions 4,000.""",
    questions=[q("4a", "Stock basis available for losses and deductions (after distributions and nondeductible expenses).", 20000 - 4000 - 1000),
               q("4b", "Ordinary loss allowed.", r["allowed"]["ord"]),
               q("4c", "Charitable contributions allowed.", r["allowed"]["char"]),
               q("4d", "Section 1231 loss allowed.", r["allowed"]["s1231"]),
               q("4e", "Total suspended and carried forward.", r["suspended_total"]),
               q("4f", "Ending stock basis.", r["stock_end"])]))

# 5 nondeductible first, excess lost
r = year(3000, nonded=5000, losses={"ord": 10000})
C.append(dict(n=5, title="Nondeductible expenses exceed basis (no election)", facts="""
Beginning stock basis 3,000. No shareholder loans. No election to change the ordering.
K-1: nondeductible expenses 5,000; ordinary loss 10,000. No income and no distributions.""",
    questions=[q("5a", "Ordinary loss allowed this year.", r["allowed"]["ord"]),
               q("5b", "Ordinary loss suspended.", r["suspended"]["ord"]),
               q("5c", "Nondeductible expenses carried forward to next year.", r["nonded_carry"])]))

# 6 election
r = year(3000, nonded=5000, losses={"ord": 10000}, election=True)
C.append(dict(n=6, title="Same facts with the ordering election", facts="""
Same facts as Case 5, except the shareholder has a valid election under Reg. 1.1367-1(g) in place.""",
    questions=[q("6a", "Ordinary loss allowed this year.", r["allowed"]["ord"]),
               q("6b", "Ordinary loss suspended.", r["suspended"]["ord"]),
               q("6c", "Nondeductible expenses carried forward to next year.", r["nonded_carry"])]))

# 7 debt basis absorbs loss
r = year(15000, debt=40000, face=40000, dist=5000, losses={"ord": 45000})
C.append(dict(n=7, title="Loss absorbed by debt basis", facts="""
Beginning stock basis 15,000. The shareholder lent the corporation 40,000 on a written note; debt basis is 40,000.
K-1: ordinary loss 45,000; distributions 5,000. No accumulated E&P. No repayments on the note.""",
    questions=[q("7a", "Ordinary loss allowed this year.", r["allowed"]["ord"]),
               q("7b", "Ending stock basis.", r["stock_end"]),
               q("7c", "Ending debt basis.", r["debt_end"]),
               q("7d", "Taxable amount of the distribution.", r["dist_gain"])]))

# 8 guarantee
r = year(10000, losses={"ord": 60000})
C.append(dict(n=8, title="Guaranteed bank loan", facts="""
Beginning stock basis 10,000. The shareholder has made no loans to the corporation, but personally guaranteed the corporation's 100,000 bank loan. The shareholder has paid nothing under the guarantee.
K-1: ordinary loss 60,000.""",
    questions=[q("8a", "Debt basis created by the guarantee.", 0),
               q("8b", "Ordinary loss allowed this year.", r["allowed"]["ord"]),
               q("8c", "Loss suspended.", r["suspended"]["ord"])]))

# 9 distribution with debt basis only
r = year(2000, debt=50000, face=50000, dist=12000)
C.append(dict(n=9, title="Distribution when only debt basis remains", facts="""
Beginning stock basis 2,000. Debt basis 50,000 on a 50,000 written note. No accumulated E&P. Stock held 6 years.
K-1: no income or loss items; distributions 12,000.""",
    questions=[q("9a", "Gain recognized on the distribution.", r["dist_gain"]),
               q("9b", "Ending stock basis.", r["stock_end"]),
               q("9c", "Ending debt basis.", r["debt_end"])]))

# 10 restoration
r = year(0, debt=18000, face=30000, income=25000, dist=9000)
assert r["restore"] == 12000 and r["stock_end"] == 4000
C.append(dict(n=10, title="Restoring reduced debt basis", facts="""
Beginning stock basis 0. One written note with a face amount of 30,000; prior losses reduced its basis to 18,000. No suspended losses.
K-1: ordinary income 25,000; distributions 9,000. No repayments on the note. No accumulated E&P.""",
    questions=[q("10a", "Taxable amount of the distribution.", r["dist_gain"]),
               q("10b", "Net increase for the year.", 25000 - 9000),
               q("10c", "Debt basis restored this year.", r["restore"]),
               q("10d", "Ending debt basis.", r["debt_end"]),
               q("10e", "Ending stock basis.", r["stock_end"])]))

# 11 carryover partly used
r = year(0, debt=0, face=20000, income=10000, carry={"ord": 14000})
C.append(dict(n=11, title="Using a suspended loss", facts="""
Beginning stock basis 0. One written note, face 20,000, with basis already reduced to 0. Suspended ordinary loss from prior years 14,000.
K-1 this year: ordinary income 10,000. No distributions and no repayments.""",
    questions=[q("11a", "Suspended loss allowed this year.", r["allowed"]["ord"]),
               q("11b", "Loss still suspended at year end.", r["suspended"]["ord"]),
               q("11c", "Ending stock basis.", r["stock_end"]),
               q("11d", "Ending debt basis.", r["debt_end"])]))

# 12 repayment on a note
p = repayment(10000, 12000, 30000)
C.append(dict(n=12, title="Repayment on a reduced-basis note", facts="""
Written note, face 30,000, held 4 years. Debt basis at the start of the year 12,000. Stock basis 0.
The corporation breaks even: no income, loss, or distribution items. It repays 10,000 of principal on the note.""",
    questions=[q("12a", "Nontaxable part of the repayment.", p["nontax"]),
               q("12b", "Gain recognized.", p["gain"]),
               q("12c", "Character of the gain.", "long-term capital gain", choices=CHAR),
               q("12d", "Ending debt basis.", p["basis_end"])]))

# 13 restoration before repayment
r = year(0, debt=10000, face=40000, income=20000)
p = repayment(40000, r["debt_end"], 40000)
assert r["debt_end"] == 30000 and p["gain"] == 10000
C.append(dict(n=13, title="Restoration applies before a repayment", facts="""
Beginning stock basis 0. One written note, face 40,000, held 5 years, with basis reduced to 10,000. No suspended losses.
K-1: ordinary income 20,000; no distributions. In July the corporation repays the note in full, 40,000.""",
    questions=[q("13a", "Debt basis immediately before the repayment.", r["debt_end"]),
               q("13b", "Gain recognized on the repayment.", p["gain"]),
               q("13c", "Ending stock basis.", r["stock_end"])]))

# 14 open account
p = repayment(8000, 5000, 20000)
C.append(dict(n=14, title="Open account repayment", facts="""
The shareholder's advances are an open account with no written note. Balance at the start of the year 20,000 (it was 20,000 at the end of last year too); debt basis 5,000. Stock basis 0.
No income, loss, or distribution items this year. Net repayments on the account for the year are 8,000.""",
    questions=[q("14a", "Gain recognized on the net repayment.", p["gain"]),
               q("14b", "Character of the gain.", "ordinary income", choices=CHAR),
               q("14c", "Ending debt basis.", p["basis_end"])]))

# 15 AAA then E&P
aaa = 12000 + 8000
from_aaa = min(35000, aaa)
div = min(35000 - from_aaa, 20000)
C.append(dict(n=15, title="Distribution with accumulated E&P", facts="""
The corporation was a C corporation years ago. Sole shareholder; beginning stock basis 30,000.
Beginning AAA 12,000. Accumulated E&P 20,000.
K-1: ordinary income 8,000; distributions 35,000. No other items.""",
    questions=[q("15a", "Amount of the distribution treated as a taxable dividend.", div),
               q("15b", "Amount of the distribution that is a tax-free return of basis.", from_aaa),
               q("15c", "Ending stock basis.", 30000 + 8000 - from_aaa),
               q("15d", "Ending AAA.", aaa - from_aaa),
               q("15e", "Ending accumulated E&P.", 20000 - div)]))

# 16 AAA in a net loss year
from_aaa = min(12000, 10000)
div = min(12000 - from_aaa, 6000)
C.append(dict(n=16, title="AAA in a net loss year", facts="""
Former C corporation. Sole shareholder; beginning stock basis 40,000.
Beginning AAA 10,000. Accumulated E&P 6,000.
K-1: ordinary loss 7,000; distributions 12,000. No other items.""",
    questions=[q("16a", "Amount of the distribution treated as a taxable dividend.", div),
               q("16b", "Ending AAA.", 10000 - from_aaa - 7000),
               q("16c", "Ordinary loss allowed.", 7000),
               q("16d", "Ending stock basis.", 40000 - from_aaa - 7000)]))

# 17 sale with suspended losses
C.append(dict(n=17, title="Sale of all stock with suspended losses", facts="""
Stock basis 0. Suspended ordinary losses from prior years 22,000. No shareholder loans.
On January 2 the shareholder sells all of the stock to an unrelated buyer for 50,000. Stock held 8 years. No K-1 items are allocated to the seller for the year.""",
    questions=[q("17a", "Gain on the sale.", 50000),
               q("17b", "Suspended loss the seller can deduct because of the sale.", 0),
               q("17c", "Is Form 7203 required this year?", "yes", choices=YN)]))

# 18 form requirement only
r = year(25000, income=9000)
C.append(dict(n=18, title="Income only", facts="""
Beginning stock basis 25,000. No shareholder loans. K-1: ordinary income 9,000 and nothing else. No distributions, no loan activity, no stock sold, and no losses claimed.""",
    questions=[q("18a", "Ending stock basis.", r["stock_end"]),
               q("18b", "Is Form 7203 required this year?", "no", choices=YN)]))

# 19 full deliverable
r = year(6000, debt=25000, face=25000, contrib=4000, income=3000, exempt=1000, dist=5000, nonded=2000,
         losses={"ord": 36000, "char": 4000}, carry={"ord": 5000})
C.append(dict(n=19, title="Full deliverable", facts="""
Prepare the complete basis package for this shareholder and save it as `deliverable.md`, following the skill's Output section. Also answer the questions below in `answers.json`.

Beginning stock basis 6,000. One written note, face 25,000, debt basis 25,000. Suspended ordinary loss from prior years 5,000. No accumulated E&P. No election to change the ordering.
During the year the shareholder contributed 4,000 of additional capital. No repayments on the note.
K-1: ordinary loss 36,000; interest income 3,000; tax-exempt interest 1,000; charitable contributions 4,000; nondeductible expenses 2,000; distributions 5,000.""",
    questions=[q("19a", "Stock basis before distributions.", r["stock_before_dist"]),
               q("19b", "Taxable amount of the distribution.", r["dist_gain"]),
               q("19c", "Total losses and deductions allowed.", r["allowed_total"]),
               q("19d", "Ordinary loss allowed (current year plus carryover).", r["allowed"]["ord"]),
               q("19e", "Charitable contributions allowed.", r["allowed"]["char"]),
               q("19f", "Total suspended and carried forward.", r["suspended_total"]),
               q("19g", "Ending stock basis.", r["stock_end"]),
               q("19h", "Ending debt basis.", r["debt_end"])]))

write_suite(Path(__file__).resolve().parent, "s-corp-basis",
            "Each case is one S corporation shareholder for one tax year. Amounts are in dollars.", C)
