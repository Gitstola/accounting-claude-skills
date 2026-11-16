# Test cases: form-1040-review

Each case is one individual return under review. Amounts are in dollars. Use the yearly figures stated in the case.

## How to answer
Write your answers to `answers.json` as one JSON object that maps each question ID to its answer.
- Number questions: a plain number, no commas or currency signs. Percentages as a number, for example 23.75 for 23.75%.
- Choice questions: exactly one of the listed choices, spelled as shown.
Answer every ID. Do the arithmetic in Python.

## Case 1: SALT cap in the phase-down range

Joint return. For this tax year the SALT cap is 40,400 for a joint return, reduced by 30% of MAGI above 505,000, but not below 10,000. MAGI is 560,000. State income tax paid 38,000; real estate tax paid 14,000. The return deducts 40,400 of state and local taxes.

Questions:
- **1a** SALT cap that applies to this return. (number)
- **1b** Correct SALT deduction. (number)
- **1c** Amount by which the return overstates the deduction. (number)
- **1d** Severity of this finding. Choices: Error, Question, Note.

## Case 2: SALT cap at the floor

Joint return. For this tax year the SALT cap is 40,400 for a joint return, reduced by 30% of MAGI above 505,000, but not below 10,000. MAGI is 700,000. State and local taxes paid total 30,000.

Questions:
- **2a** Correct SALT deduction. (number)

## Case 3: SALT below the cap

Joint return. For this tax year the SALT cap is 40,400 for a joint return, reduced by 30% of MAGI above 505,000, but not below 10,000. MAGI is 300,000. State and local taxes paid total 26,500.

Questions:
- **3a** Correct SALT deduction. (number)

## Case 4: Standard or itemized

Joint return for tax year 2026. The standard deduction for this return is 32,200. AGI is 200,000. For 2026, itemizers may deduct charitable gifts only above 0.5% of AGI, and joint filers who do not itemize may deduct up to 2,000 of cash gifts to public charities in addition to the standard deduction.
Documents show: state and local taxes 12,000 (under the cap); home mortgage interest per Form 1098 14,000; cash gifts to public charities 6,000, all acknowledged in writing; unreimbursed medical expenses 18,000.
The return claims the standard deduction and no deduction for the charitable gifts.

Questions:
- **4a** Deductible charitable contributions if itemizing. (number)
- **4b** Deductible medical expenses if itemizing. (number)
- **4c** Total itemized deductions. (number)
- **4d** Should the return itemize? Choices: yes, no.
- **4e** Additional deduction available compared with the return as prepared. (number)

## Case 5: Underpayment safe harbor, prior-year AGI under 150,000

Single filer. Prior-year AGI 140,000; prior-year total tax 21,000. Current-year total tax 30,000. Withholding for the year was 22,000 and there were no estimated payments.

Questions:
- **5a** Required annual payment to avoid the underpayment penalty. (number)
- **5b** Is the safe harbor met? Choices: yes, no.

## Case 6: Underpayment safe harbor, prior-year AGI over 150,000

Joint return. Prior-year AGI 310,000; prior-year total tax 60,000. Current-year total tax 90,000. Total withholding and timely estimated payments were 64,000.

Questions:
- **6a** Required annual payment to avoid the underpayment penalty. (number)
- **6b** Is the safe harbor met? Choices: yes, no.
- **6c** Shortfall against the required annual payment. (number)

## Case 7: Small balance due

Single filer. Current-year total tax 9,400. Withholding 8,700. No estimated payments. Prior-year total tax was 12,000 and prior-year AGI was 95,000.

Questions:
- **7a** Balance due with the return. (number)
- **7b** Does an underpayment penalty apply? Choices: yes, no.

## Case 8: Net investment income tax

Joint return. MAGI 330,000. Net investment income 95,000. Form 8960 on the return shows net investment income tax of 3,610.

Questions:
- **8a** Correct net investment income tax. (number)
- **8b** Amount by which the return overstates the tax. (number)

## Case 9: Additional Medicare tax

Single filer. Medicare wages 240,000. Net self-employment income subject to Medicare tax 30,000. The employer withheld Additional Medicare Tax of 360 on the wages. The return includes no Form 8959.

Questions:
- **9a** Total Additional Medicare Tax for the year. (number)
- **9b** Additional Medicare Tax still owed with the return after the employer's withholding. (number)
- **9c** Is Form 8959 required? Choices: yes, no.

## Case 10: Capital loss limit

Joint return. Net capital loss for the current year 9,000. Capital loss carryover from the prior-year return 5,500. No capital gains. The return deducts a capital loss of 14,500 against ordinary income and shows no carryover to next year.

Questions:
- **10a** Capital loss deductible against ordinary income this year. (number)
- **10b** Capital loss carryover to next year. (number)
- **10c** Amount by which the return overstates the deduction. (number)

## Case 11: Head of household

The taxpayer was divorced two years ago and did not remarry. Her 9-year-old son lived with her for 5 months of the year and with his father for 7 months. She paid 70% of the cost of keeping up her home. She has no other dependents or relatives living with her. The return uses head of household status.

Questions:
- **11a** Does she qualify for head of household status? Choices: yes, no.
- **11b** Correct filing status. Choices: single, head of household, married filing jointly, married filing separately.

## Case 12: W-2 tie-out

Three Forms W-2 are in the file. Box 1 wages: 61,200; 18,450; 7,900. Box 2 federal withholding: 7,300; 2,100; 640.
The return shows wages of 79,650 on line 1a and federal withholding from Forms W-2 of 9,400.

Questions:
- **12a** Correct wages for line 1a. (number)
- **12b** Wages left off the return. (number)
- **12c** Correct federal withholding from Forms W-2. (number)
- **12d** Does the wage tie-out pass? Choices: yes, no.

## Case 13: Qualified charitable distribution

The taxpayer is 74. Form 1099-R shows a gross IRA distribution of 40,000, code 7, with no basis in the IRA. Of that, 10,000 was paid directly from the IRA to a public charity as a qualified charitable distribution. The return reports 40,000 as taxable and also claims the 10,000 as an itemized charitable deduction.

Questions:
- **13a** Correct taxable amount of the IRA distribution. (number)
- **13b** Correct itemized charitable deduction for the 10,000. (number)

## Case 14: Qualified tips deduction

Single filer, tax year 2026, working as a restaurant server (a listed tipped occupation). For this tax year the qualified tips deduction is capped at 25,000 and begins to phase out at MAGI of 150,000 for a single filer. MAGI is 120,000. Form W-2 reports qualified tips of 31,000. The return deducts 31,000.

Questions:
- **14a** Correct qualified tips deduction. (number)
- **14b** Amount by which the return overstates the deduction. (number)

## Case 15: Qualified overtime deduction

Joint return, tax year 2026. For this tax year the qualified overtime deduction is capped at 25,000 on a joint return and begins to phase out at MAGI of 300,000. MAGI is 250,000. The taxpayer's pay records show total overtime pay of 30,000, all paid at time-and-a-half as required by the Fair Labor Standards Act. The return deducts 30,000.

Questions:
- **15a** Correct qualified overtime deduction. (number)
- **15b** Amount by which the return overstates the deduction. (number)

## Case 16: Marketplace insurance

The file contains a Form 1095-A showing advance premium tax credit payments of 3,600 for the year. The return has no Form 8962.

Questions:
- **16a** Is Form 8962 required? Choices: yes, no.
- **16b** Severity of this finding. Choices: Error, Question, Note.

## Case 17: Taxable Social Security benefits

Single filer. Social Security benefits (Form SSA-1099 box 5) 24,000. Other income included in AGI 30,000. Tax-exempt interest 2,000. No adjustments to income. For a single filer the base amounts for taxing benefits are 25,000 and 34,000. The return reports taxable benefits of 20,400.

Questions:
- **17a** Provisional income. (number)
- **17b** Correct taxable Social Security benefits. (number)
- **17c** Amount by which the return overstates taxable benefits. (number)

## Case 18: State tax refund

The taxpayer received a Form 1099-G showing a state income tax refund of 1,200 for the prior year. On the prior-year federal return the taxpayer claimed the standard deduction. The current return reports the 1,200 as taxable income.

Questions:
- **18a** Correct taxable amount of the state refund. (number)
- **18b** Severity of this finding. Choices: Error, Question, Note.

## Case 19: Mortgage interest tie-out

Form 1098 shows mortgage interest received of 16,480 on acquisition debt of 410,000 for the taxpayer's main home. Schedule A on the return shows home mortgage interest of 14,680. The return itemizes.

Questions:
- **19a** Correct mortgage interest deduction. (number)
- **19b** Amount by which the return understates the deduction. (number)

## Case 20: Payments and refund

Total tax on the return is 24,310. Documents show federal withholding of 19,800; four estimated payments of 1,500 each, all confirmed on the client's bank statements; and a prior-year overpayment of 900 that was applied to this year. The return shows total payments of 25,800 and a refund of 1,490.

Questions:
- **20a** Correct total payments. (number)
- **20b** Correct refund. (number)
- **20c** Payment left off the return. (number)

## Case 21: Full deliverable

Review this return and save your review memo as `deliverable.md`, following the skill's Output section. Also answer the questions below in `answers.json`.

Joint return, tax year 2026. For this tax year the SALT cap is 40,400 for a joint return, reduced by 30% of MAGI above 505,000, but not below 10,000. The standard deduction is 32,200. MAGI and AGI are both 520,000.
Documents:
- Two Forms W-2: box 1 wages 310,000 and 150,000; box 2 withholding 62,000 and 27,000.
- Form 1099-INT interest 12,000; Form 1099-DIV ordinary dividends 48,000, of which 40,000 are qualified. Net investment income is 60,000.
- State income tax paid 36,000; real estate tax 15,000. Form 1098 mortgage interest 22,000.
- Prior-year return: AGI 470,000; total tax 104,000.
The return as prepared shows: wages 460,000; taxable interest 12,000; ordinary dividends 48,000; a SALT deduction of 40,400; mortgage interest 22,000; a correct Form 8959; no Form 8960; total tax 118,000; federal withholding 89,000; no estimated payments.

Questions:
- **21a** Correct SALT deduction. (number)
- **21b** Net investment income tax that should be on the return. (number)
- **21c** Required annual payment to avoid the underpayment penalty, based on the total tax as prepared. (number)
- **21d** Is the underpayment safe harbor met? Choices: yes, no.
- **21e** Does the wage tie-out pass? Choices: yes, no.
- **21f** Is the return ready to sign as prepared, with no changes? Choices: yes, no.
