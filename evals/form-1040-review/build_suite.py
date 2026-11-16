"""Build cases.md and answer_key.json for form-1040-review.
Yearly figures are stated in each case, so answers do not depend on memory of a tax year."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import q, write_suite

YN = ["yes", "no"]
SEV = ["Error", "Question", "Note"]
STATUS = ["single", "head of household", "married filing jointly", "married filing separately"]


def salt_cap(magi, cap=40400, start=505000, rate=0.30, floor=10000):
    return max(floor, cap - rate * max(0, magi - start))


def safe_harbor(cur_tax, prior_tax, prior_agi):
    return min(0.90 * cur_tax, (1.10 if prior_agi > 150000 else 1.00) * prior_tax)


def taxable_ss(other_income, exempt_int, ss, base, upper):
    pi = other_income + exempt_int + 0.5 * ss
    if pi <= base:
        return 0.0
    if pi <= upper:
        return min(0.5 * ss, 0.5 * (pi - base))
    return min(0.85 * ss, 0.85 * (pi - upper) + min(0.5 * ss, 0.5 * (upper - base)))


SALT_NOTE = ("For this tax year the SALT cap is 40,400 for a joint return, reduced by 30% of MAGI above 505,000, "
             "but not below 10,000.")
C = []

# 1 SALT phase-down
cap = salt_cap(560000)
C.append(dict(n=1, title="SALT cap in the phase-down range", facts=f"""
Joint return. {SALT_NOTE} MAGI is 560,000. State income tax paid 38,000; real estate tax paid 14,000. The return deducts 40,400 of state and local taxes.""",
    questions=[q("1a", "SALT cap that applies to this return.", cap),
               q("1b", "Correct SALT deduction.", min(52000, cap)),
               q("1c", "Amount by which the return overstates the deduction.", 40400 - min(52000, cap)),
               q("1d", "Severity of this finding.", "Error", choices=SEV)]))

# 2 SALT floor
cap = salt_cap(700000)
C.append(dict(n=2, title="SALT cap at the floor", facts=f"""
Joint return. {SALT_NOTE} MAGI is 700,000. State and local taxes paid total 30,000.""",
    questions=[q("2a", "Correct SALT deduction.", min(30000, cap))]))

# 3 SALT below cap
cap = salt_cap(300000)
C.append(dict(n=3, title="SALT below the cap", facts=f"""
Joint return. {SALT_NOTE} MAGI is 300,000. State and local taxes paid total 26,500.""",
    questions=[q("3a", "Correct SALT deduction.", min(26500, cap))]))

# 4 standard vs itemized
agi = 200000
charity = max(0, 6000 - 0.005 * agi)
medical = max(0, 18000 - 0.075 * agi)
itemized = 12000 + 14000 + charity + medical
C.append(dict(n=4, title="Standard or itemized", facts="""
Joint return for tax year 2026. The standard deduction for this return is 32,200. AGI is 200,000. For 2026, itemizers may deduct charitable gifts only above 0.5% of AGI, and joint filers who do not itemize may deduct up to 2,000 of cash gifts to public charities in addition to the standard deduction.
Documents show: state and local taxes 12,000 (under the cap); home mortgage interest per Form 1098 14,000; cash gifts to public charities 6,000, all acknowledged in writing; unreimbursed medical expenses 18,000.
The return claims the standard deduction and no deduction for the charitable gifts.""",
    questions=[q("4a", "Deductible charitable contributions if itemizing.", charity),
               q("4b", "Deductible medical expenses if itemizing.", medical),
               q("4c", "Total itemized deductions.", itemized),
               q("4d", "Should the return itemize?", "yes" if itemized > 32200 + min(6000, 2000) else "no", choices=YN),
               q("4e", "Additional deduction available compared with the return as prepared.", max(itemized, 32200 + min(6000, 2000)) - 32200)]))

# 5 safe harbor met
req = safe_harbor(30000, 21000, 140000)
C.append(dict(n=5, title="Underpayment safe harbor, prior-year AGI under 150,000", facts="""
Single filer. Prior-year AGI 140,000; prior-year total tax 21,000. Current-year total tax 30,000. Withholding for the year was 22,000 and there were no estimated payments.""",
    questions=[q("5a", "Required annual payment to avoid the underpayment penalty.", req),
               q("5b", "Is the safe harbor met?", "yes" if 22000 >= req else "no", choices=YN)]))

# 6 safe harbor 110%
req = safe_harbor(90000, 60000, 310000)
C.append(dict(n=6, title="Underpayment safe harbor, prior-year AGI over 150,000", facts="""
Joint return. Prior-year AGI 310,000; prior-year total tax 60,000. Current-year total tax 90,000. Total withholding and timely estimated payments were 64,000.""",
    questions=[q("6a", "Required annual payment to avoid the underpayment penalty.", req),
               q("6b", "Is the safe harbor met?", "yes" if 64000 >= req else "no", choices=YN),
               q("6c", "Shortfall against the required annual payment.", max(0, req - 64000))]))

# 7 under 1,000
C.append(dict(n=7, title="Small balance due", facts="""
Single filer. Current-year total tax 9,400. Withholding 8,700. No estimated payments. Prior-year total tax was 12,000 and prior-year AGI was 95,000.""",
    questions=[q("7a", "Balance due with the return.", 9400 - 8700),
               q("7b", "Does an underpayment penalty apply?", "no", choices=YN)]))

# 8 NIIT
niit = 0.038 * min(95000, 330000 - 250000)
C.append(dict(n=8, title="Net investment income tax", facts="""
Joint return. MAGI 330,000. Net investment income 95,000. Form 8960 on the return shows net investment income tax of 3,610.""",
    questions=[q("8a", "Correct net investment income tax.", niit, tol=0.5),
               q("8b", "Amount by which the return overstates the tax.", 3610 - niit, tol=0.5)]))

# 9 additional Medicare tax
amt = 0.009 * (240000 + 30000 - 200000)
C.append(dict(n=9, title="Additional Medicare tax", facts="""
Single filer. Medicare wages 240,000. Net self-employment income subject to Medicare tax 30,000. The employer withheld Additional Medicare Tax of 360 on the wages. The return includes no Form 8959.""",
    questions=[q("9a", "Total Additional Medicare Tax for the year.", amt, tol=0.5),
               q("9b", "Additional Medicare Tax still owed with the return after the employer's withholding.", amt - 360, tol=0.5),
               q("9c", "Is Form 8959 required?", "yes", choices=YN)]))

# 10 capital loss
C.append(dict(n=10, title="Capital loss limit", facts="""
Joint return. Net capital loss for the current year 9,000. Capital loss carryover from the prior-year return 5,500. No capital gains. The return deducts a capital loss of 14,500 against ordinary income and shows no carryover to next year.""",
    questions=[q("10a", "Capital loss deductible against ordinary income this year.", 3000),
               q("10b", "Capital loss carryover to next year.", 9000 + 5500 - 3000),
               q("10c", "Amount by which the return overstates the deduction.", 14500 - 3000)]))

# 11 head of household
C.append(dict(n=11, title="Head of household", facts="""
The taxpayer was divorced two years ago and did not remarry. Her 9-year-old son lived with her for 5 months of the year and with his father for 7 months. She paid 70% of the cost of keeping up her home. She has no other dependents or relatives living with her. The return uses head of household status.""",
    questions=[q("11a", "Does she qualify for head of household status?", "no", choices=YN),
               q("11b", "Correct filing status.", "single", choices=STATUS)]))

# 12 W-2 tie-out
w1 = [61200, 18450, 7900]
w2 = [7300, 2100, 640]
C.append(dict(n=12, title="W-2 tie-out", facts="""
Three Forms W-2 are in the file. Box 1 wages: 61,200; 18,450; 7,900. Box 2 federal withholding: 7,300; 2,100; 640.
The return shows wages of 79,650 on line 1a and federal withholding from Forms W-2 of 9,400.""",
    questions=[q("12a", "Correct wages for line 1a.", sum(w1)),
               q("12b", "Wages left off the return.", sum(w1) - 79650),
               q("12c", "Correct federal withholding from Forms W-2.", sum(w2)),
               q("12d", "Does the wage tie-out pass?", "no", choices=YN)]))

# 13 QCD
C.append(dict(n=13, title="Qualified charitable distribution", facts="""
The taxpayer is 74. Form 1099-R shows a gross IRA distribution of 40,000, code 7, with no basis in the IRA. Of that, 10,000 was paid directly from the IRA to a public charity as a qualified charitable distribution. The return reports 40,000 as taxable and also claims the 10,000 as an itemized charitable deduction.""",
    questions=[q("13a", "Correct taxable amount of the IRA distribution.", 30000),
               q("13b", "Correct itemized charitable deduction for the 10,000.", 0)]))

# 14 tips cap
C.append(dict(n=14, title="Qualified tips deduction", facts="""
Single filer, tax year 2026, working as a restaurant server (a listed tipped occupation). For this tax year the qualified tips deduction is capped at 25,000 and begins to phase out at MAGI of 150,000 for a single filer. MAGI is 120,000. Form W-2 reports qualified tips of 31,000. The return deducts 31,000.""",
    questions=[q("14a", "Correct qualified tips deduction.", min(31000, 25000)),
               q("14b", "Amount by which the return overstates the deduction.", 31000 - 25000)]))

# 15 overtime premium
C.append(dict(n=15, title="Qualified overtime deduction", facts="""
Joint return, tax year 2026. For this tax year the qualified overtime deduction is capped at 25,000 on a joint return and begins to phase out at MAGI of 300,000. MAGI is 250,000. The taxpayer's pay records show total overtime pay of 30,000, all paid at time-and-a-half as required by the Fair Labor Standards Act. The return deducts 30,000.""",
    questions=[q("15a", "Correct qualified overtime deduction.", 30000 / 1.5 * 0.5),
               q("15b", "Amount by which the return overstates the deduction.", 30000 - 30000 / 1.5 * 0.5)]))

# 16 Form 8962
C.append(dict(n=16, title="Marketplace insurance", facts="""
The file contains a Form 1095-A showing advance premium tax credit payments of 3,600 for the year. The return has no Form 8962.""",
    questions=[q("16a", "Is Form 8962 required?", "yes", choices=YN),
               q("16b", "Severity of this finding.", "Error", choices=SEV)]))

# 17 Social Security
ts = taxable_ss(30000, 2000, 24000, 25000, 34000)
C.append(dict(n=17, title="Taxable Social Security benefits", facts="""
Single filer. Social Security benefits (Form SSA-1099 box 5) 24,000. Other income included in AGI 30,000. Tax-exempt interest 2,000. No adjustments to income. For a single filer the base amounts for taxing benefits are 25,000 and 34,000. The return reports taxable benefits of 20,400.""",
    questions=[q("17a", "Provisional income.", 30000 + 2000 + 12000),
               q("17b", "Correct taxable Social Security benefits.", ts),
               q("17c", "Amount by which the return overstates taxable benefits.", 20400 - ts)]))

# 18 state refund
C.append(dict(n=18, title="State tax refund", facts="""
The taxpayer received a Form 1099-G showing a state income tax refund of 1,200 for the prior year. On the prior-year federal return the taxpayer claimed the standard deduction. The current return reports the 1,200 as taxable income.""",
    questions=[q("18a", "Correct taxable amount of the state refund.", 0),
               q("18b", "Severity of this finding.", "Error", choices=SEV)]))

# 19 mortgage interest
C.append(dict(n=19, title="Mortgage interest tie-out", facts="""
Form 1098 shows mortgage interest received of 16,480 on acquisition debt of 410,000 for the taxpayer's main home. Schedule A on the return shows home mortgage interest of 14,680. The return itemizes.""",
    questions=[q("19a", "Correct mortgage interest deduction.", 16480),
               q("19b", "Amount by which the return understates the deduction.", 16480 - 14680)]))

# 20 payments and refund
pay = 19800 + 4 * 1500 + 900
C.append(dict(n=20, title="Payments and refund", facts="""
Total tax on the return is 24,310. Documents show federal withholding of 19,800; four estimated payments of 1,500 each, all confirmed on the client's bank statements; and a prior-year overpayment of 900 that was applied to this year. The return shows total payments of 25,800 and a refund of 1,490.""",
    questions=[q("20a", "Correct total payments.", pay),
               q("20b", "Correct refund.", pay - 24310),
               q("20c", "Payment left off the return.", pay - 25800)]))

# 21 deliverable
cap = salt_cap(520000)
niit = 0.038 * min(60000, 520000 - 250000)
C.append(dict(n=21, title="Full deliverable", facts=f"""
Review this return and save your review memo as `deliverable.md`, following the skill's Output section. Also answer the questions below in `answers.json`.

Joint return, tax year 2026. {SALT_NOTE} The standard deduction is 32,200. MAGI and AGI are both 520,000.
Documents:
- Two Forms W-2: box 1 wages 310,000 and 150,000; box 2 withholding 62,000 and 27,000.
- Form 1099-INT interest 12,000; Form 1099-DIV ordinary dividends 48,000, of which 40,000 are qualified. Net investment income is 60,000.
- State income tax paid 36,000; real estate tax 15,000. Form 1098 mortgage interest 22,000.
- Prior-year return: AGI 470,000; total tax 104,000.
The return as prepared shows: wages 460,000; taxable interest 12,000; ordinary dividends 48,000; a SALT deduction of 40,400; mortgage interest 22,000; a correct Form 8959; no Form 8960; total tax 118,000; federal withholding 89,000; no estimated payments.""",
    questions=[q("21a", "Correct SALT deduction.", min(51000, cap)),
               q("21b", "Net investment income tax that should be on the return.", niit, tol=0.5),
               q("21c", "Required annual payment to avoid the underpayment penalty, based on the total tax as prepared.", safe_harbor(118000, 104000, 470000)),
               q("21d", "Is the underpayment safe harbor met?", "yes" if 89000 >= safe_harbor(118000, 104000, 470000) else "no", choices=YN),
               q("21e", "Does the wage tie-out pass?", "yes", choices=YN),
               q("21f", "Is the return ready to sign as prepared, with no changes?", "no", choices=YN)]))

write_suite(Path(__file__).resolve().parent, "form-1040-review",
            "Each case is one individual return under review. Amounts are in dollars. Use the yearly figures stated in the case.", C)
