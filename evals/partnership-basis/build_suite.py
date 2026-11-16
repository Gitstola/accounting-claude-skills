"""Build cases.md and answer_key.json for partnership-basis.
Expected values come from the engine below (IRC 704(d), 705, 722, 731-733, 752)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import q, write_suite

YN = ["yes", "no"]
CHAR = ["capital", "ordinary", "none"]


def year(beg, contrib=0.0, liab_beg=0.0, liab_end=0.0, income=0.0, exempt=0.0, cash=0.0,
         prop=None, nonded=0.0, losses=None, carry=None):
    """One year of a partner's outside basis. prop = list of the partnership's bases in
    property distributed in a current distribution."""
    losses, carry = dict(losses or {}), dict(carry or {})
    r = {}
    d = liab_end - liab_beg
    basis = beg + contrib + max(d, 0) + income + exempt
    money = cash + max(-d, 0)
    r["basis_before_dist"] = basis
    r["money"] = money
    r["gain"] = max(0.0, money - basis)
    basis -= min(money, basis)
    r["prop_basis"] = []
    for inside in (prop or []):
        take = min(inside, basis)
        r["prop_basis"].append(take)
        basis -= take
    nd = min(nonded, basis); basis -= nd
    r["basis_before_loss"] = basis
    total = {k: losses.get(k, 0) + carry.get(k, 0) for k in set(losses) | set(carry)}
    tot = sum(total.values())
    allowed = min(tot, basis)
    ratio = allowed / tot if tot else 0
    r["allowed"] = {k: v * ratio for k, v in total.items()}
    r["allowed_total"] = allowed
    r["suspended"] = {k: total[k] - r["allowed"][k] for k in total}
    r["suspended_total"] = tot - allowed
    r["end"] = basis - allowed
    return r


C = []

# 1 formation
C.append(dict(n=1, title="Formation with cash and property", facts="""
Dana joins a new partnership as a 50% partner. She contributes cash of 20,000 and equipment with an adjusted basis of 35,000 and a fair value of 60,000. The partnership has no liabilities.""",
    questions=[q("1a", "Dana's initial outside basis.", 20000 + 35000),
               q("1b", "Gain Dana recognizes on the contribution.", 0)]))

# 2 contributed property with debt
net = 40000 - 30000 + 0.25 * 30000
C.append(dict(n=2, title="Contributed property subject to debt", facts="""
Avery contributes land to a partnership for a 25% interest. The land has an adjusted basis of 40,000 and a fair value of 100,000, and it is subject to a 30,000 mortgage that the partnership assumes. After the contribution Avery's share of that liability is 25%. The partnership has no other liabilities.""",
    questions=[q("2a", "Avery's outside basis right after the contribution.", net),
               q("2b", "Gain Avery recognizes.", 0)]))

# 3 debt relief above basis
relief = 40000 - 0.20 * 40000
C.append(dict(n=3, title="Debt relief above basis", facts="""
Blake contributes a building to a partnership for a 20% interest. Adjusted basis 10,000; fair value 90,000; subject to a 40,000 mortgage that the partnership assumes. After the contribution Blake's share of that liability is 20%. The partnership has no other liabilities.""",
    questions=[q("3a", "Net liability relief treated as money distributed to Blake.", relief),
               q("3b", "Gain Blake recognizes.", max(0, relief - 10000)),
               q("3c", "Blake's outside basis right after the contribution.", max(0, 10000 - relief))]))

# 4 basic year
r = year(30000, liab_beg=10000, liab_end=10000, income=18000, exempt=2000, cash=12000, nonded=1000,
         losses={"char": 3000})
C.append(dict(n=4, title="Ordinary year", facts="""
Beginning outside basis 30,000. Share of partnership liabilities is 10,000 at both the beginning and the end of the year.
K-1: ordinary income 18,000; tax-exempt interest 2,000; nondeductible expenses 1,000; cash charitable contributions 3,000; cash distributions 12,000.""",
    questions=[q("4a", "Gain recognized on the distributions.", r["gain"]),
               q("4b", "Ending outside basis.", r["end"])]))

# 5 loss limited
r = year(25000, cash=5000, losses={"ord": 40000})
C.append(dict(n=5, title="Loss limited by basis", facts="""
Beginning outside basis 25,000. Share of liabilities unchanged during the year.
K-1: ordinary loss 40,000; cash distributions 5,000.""",
    questions=[q("5a", "Basis available for the loss.", r["basis_before_loss"]),
               q("5b", "Ordinary loss allowed under the basis limit.", r["allowed"]["ord"]),
               q("5c", "Loss suspended.", r["suspended"]["ord"]),
               q("5d", "Ending outside basis.", r["end"])]))

# 6 pro rata
r = year(18000, losses={"ord": 24000, "ltcl": 6000, "s179": 6000})
C.append(dict(n=6, title="Several loss items exceed basis", facts="""
Beginning outside basis 18,000. Share of liabilities unchanged. No distributions.
K-1: ordinary loss 24,000; long-term capital loss 6,000; section 179 deduction 6,000.""",
    questions=[q("6a", "Ordinary loss allowed.", r["allowed"]["ord"]),
               q("6b", "Long-term capital loss allowed.", r["allowed"]["ltcl"]),
               q("6c", "Section 179 deduction allowed.", r["allowed"]["s179"]),
               q("6d", "Total suspended.", r["suspended_total"])]))

# 7 liability increase
r = year(5000, liab_beg=20000, liab_end=50000, losses={"ord": 30000})
C.append(dict(n=7, title="Liability increase frees up a loss", facts="""
Beginning outside basis 5,000 (this already includes the beginning share of liabilities). K-1 item K shows the partner's share of liabilities at 20,000 at the beginning of the year and 50,000 at the end.
K-1: ordinary loss 30,000. No distributions.""",
    questions=[q("7a", "Basis available for the loss.", r["basis_before_loss"]),
               q("7b", "Ordinary loss allowed under the basis limit.", r["allowed"]["ord"]),
               q("7c", "Ending outside basis.", r["end"])]))

# 8 liability decrease, gain
r = year(8000, liab_beg=30000, liab_end=12000, income=4000)
C.append(dict(n=8, title="Liability decrease after a refinancing", facts="""
Beginning outside basis 8,000 (including the beginning share of liabilities). K-1 item K: share of liabilities 30,000 at the beginning of the year and 12,000 at the end, after the partnership paid down debt.
K-1: ordinary income 4,000. No cash distributions.""",
    questions=[q("8a", "Deemed cash distribution.", r["money"]),
               q("8b", "Gain recognized.", r["gain"]),
               q("8c", "Character of the gain (assume no hot assets).", "capital", choices=CHAR),
               q("8d", "Ending outside basis.", r["end"])]))

# 9 draws at year end
r = year(3000, income=25000, cash=20000)
C.append(dict(n=9, title="Draws during the year", facts="""
Beginning outside basis 3,000. Share of liabilities unchanged. The partner took draws against current-year earnings of 20,000, spread through the year. K-1: ordinary income 25,000; distributions 20,000.""",
    questions=[q("9a", "Gain recognized on the draws.", r["gain"]),
               q("9b", "Ending outside basis.", r["end"])]))

# 10 cash above basis, not a draw
gain10 = max(0, 22000 - 10000)
C.append(dict(n=10, title="Cash distribution above basis", facts="""
Beginning outside basis 10,000. Share of liabilities unchanged. On January 15 the partnership made a one-time cash distribution of 22,000 to the partner out of prior-year cash. It was not a draw or advance against current-year earnings, and no income had been earned yet. K-1 for the year: ordinary income 5,000. The partnership holds no unrealized receivables or inventory.""",
    questions=[q("10a", "Gain recognized.", gain10),
               q("10b", "Character of the gain.", "capital", choices=CHAR),
               q("10c", "Ending outside basis.", 0 + 5000)]))

# 11 property distribution limited by basis
r = year(14000, cash=4000, prop=[15000])
C.append(dict(n=11, title="Current distribution of property, basis-limited", facts="""
Outside basis just before the distribution, after all other items for the year, is 14,000. In a current (non-liquidating) distribution the partner receives cash of 4,000 and land. The partnership's adjusted basis in the land is 15,000 and its fair value is 25,000. Share of liabilities unchanged.""",
    questions=[q("11a", "Gain recognized by the partner.", r["gain"]),
               q("11b", "The partner's basis in the land.", r["prop_basis"][0]),
               q("11c", "Outside basis after the distribution.", r["end"]),
               q("11d", "Is Form 7217 required?", "yes", choices=YN)]))

# 12 property distribution, ample basis
r = year(50000, cash=5000, prop=[12000])
C.append(dict(n=12, title="Current distribution of property, ample basis", facts="""
Outside basis just before the distribution is 50,000. In a current distribution the partner receives cash of 5,000 and equipment. The partnership's adjusted basis in the equipment is 12,000 and its fair value is 30,000. Share of liabilities unchanged.""",
    questions=[q("12a", "The partner's basis in the equipment.", r["prop_basis"][0]),
               q("12b", "Outside basis after the distribution.", r["end"]),
               q("12c", "Gain recognized by the partner.", r["gain"])]))

# 13 liquidating, no loss
land = 60000 - 10000 - 8000
C.append(dict(n=13, title="Liquidating distribution with property", facts="""
A partner's interest is liquidated. Outside basis just before the distribution is 60,000. The partner receives cash of 10,000; inventory with a partnership basis of 8,000 and fair value of 12,000; and land with a partnership basis of 20,000 and fair value of 50,000. The partner has no share of liabilities. Assume section 751(b) does not apply.""",
    questions=[q("13a", "The partner's basis in the inventory.", 8000),
               q("13b", "The partner's basis in the land.", land),
               q("13c", "Gain or loss recognized (enter 0 if none).", 0)]))

# 14 liquidating loss
C.append(dict(n=14, title="Liquidating distribution with a loss", facts="""
A partner's interest is liquidated. Outside basis just before the distribution is 40,000. The partner receives only cash of 15,000 and inventory with a partnership basis of 9,000 and fair value of 11,000. The partner has no share of liabilities. Assume section 751(b) does not apply.""",
    questions=[q("14a", "Loss recognized (enter as a positive number).", 40000 - 15000 - 9000),
               q("14b", "Character of the loss.", "capital", choices=CHAR),
               q("14c", "The partner's basis in the inventory.", 9000)]))

# 15 carryover
r = year(0, contrib=5000, income=12000, carry={"ord": 20000})
C.append(dict(n=15, title="Using a suspended loss", facts="""
Beginning outside basis 0. Suspended ordinary loss from prior years 20,000. Share of liabilities unchanged.
This year the partner contributes cash of 5,000. K-1: ordinary income 12,000. No distributions.""",
    questions=[q("15a", "Suspended loss allowed this year.", r["allowed"]["ord"]),
               q("15b", "Loss still suspended at year end.", r["suspended"]["ord"]),
               q("15c", "Ending outside basis.", r["end"])]))

# 16 basis vs at-risk
r = year(50000, liab_beg=40000, liab_end=40000, losses={"ord": 30000})
at_risk = 50000 - 40000
C.append(dict(n=16, title="Basis limit and at-risk limit", facts="""
Beginning outside basis 50,000. Of that, 40,000 is the partner's share of a nonrecourse equipment loan that is not qualified nonrecourse financing; the share is unchanged at year end. The other 10,000 came from cash the partner contributed. The partner has no other amounts at risk.
K-1: ordinary loss 30,000. No distributions.""",
    questions=[q("16a", "Ordinary loss allowed under the basis limit.", r["allowed"]["ord"]),
               q("16b", "Loss deductible after also applying the at-risk limit.", min(r["allowed"]["ord"], at_risk)),
               q("16c", "Ending outside basis.", r["end"])]))

# 17 sale
ar = 70000 + 15000
C.append(dict(n=17, title="Sale of the interest", facts="""
A partner sells her entire interest for cash of 70,000. Her outside basis at the sale date is 45,000, which includes her 15,000 share of partnership liabilities; the buyer takes over that share. Her share of the partnership's unrealized receivables is 10,000, with a zero basis. The partnership has no inventory.""",
    questions=[q("17a", "Amount realized.", ar),
               q("17b", "Total gain.", ar - 45000),
               q("17c", "Ordinary income portion.", 10000),
               q("17d", "Capital gain portion.", ar - 45000 - 10000)]))

# 18 charitable contribution of property
r = year(20000, losses={"char": 4000})
C.append(dict(n=18, title="Partnership gives appreciated property to charity", facts="""
Beginning outside basis 20,000. Share of liabilities unchanged. The only item this year: the partnership donated stock to a public charity. The partner's share of the stock's fair value is 10,000 and her share of the partnership's adjusted basis in it is 4,000.""",
    questions=[q("18a", "Reduction in outside basis for the contribution.", 4000),
               q("18b", "Ending outside basis.", r["end"])]))

# 19 guaranteed payment
r = year(10000, income=6000, cash=4000)
C.append(dict(n=19, title="Guaranteed payment", facts="""
Beginning outside basis 10,000. Share of liabilities unchanged. The partner received a guaranteed payment for services of 30,000 during the year. K-1: guaranteed payment 30,000; ordinary income 6,000 (the partner's share after the partnership deducted the guaranteed payments); cash distributions 4,000, separate from the guaranteed payment.""",
    questions=[q("19a", "Change in outside basis caused by the guaranteed payment itself.", 0),
               q("19b", "Ending outside basis.", r["end"])]))

# 20 deliverable
r = year(22000, contrib=3000, liab_beg=18000, liab_end=10000, income=2500, exempt=500, cash=6000,
         nonded=1000, losses={"ord": 20000, "s179": 5000}, carry={"ord": 7000})
C.append(dict(n=20, title="Full deliverable", facts="""
Prepare the complete outside basis package for this partner and save it as `deliverable.md`, following the skill's Output section. Also answer the questions below in `answers.json`.

Beginning outside basis 22,000 (including the beginning share of liabilities). K-1 item K: share of liabilities 18,000 at the beginning of the year and 10,000 at the end. Suspended ordinary loss from prior years 7,000.
During the year the partner contributed cash of 3,000.
K-1: ordinary loss 20,000; interest income 2,500; tax-exempt interest 500; section 179 deduction 5,000; nondeductible expenses 1,000; cash distributions 6,000. The partnership has no unrealized receivables or inventory.""",
    questions=[q("20a", "Total money treated as distributed (cash plus liability decrease).", r["money"]),
               q("20b", "Gain recognized on distributions.", r["gain"]),
               q("20c", "Basis available for losses and deductions.", r["basis_before_loss"]),
               q("20d", "Ordinary loss allowed (current year plus carryover).", r["allowed"]["ord"]),
               q("20e", "Section 179 deduction allowed.", r["allowed"]["s179"]),
               q("20f", "Total suspended and carried forward.", r["suspended_total"]),
               q("20g", "Ending outside basis.", r["end"])]))

write_suite(Path(__file__).resolve().parent, "partnership-basis",
            "Each case is one partner for one tax year unless it says otherwise. Amounts are in dollars.", C)
