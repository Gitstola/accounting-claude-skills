---
name: "form-1040-review"
description: "Use when reviewing a prepared individual income tax return (Form 1040) before sign-off or filing: income completeness against source documents, filing status and dependents, deductions and credits, additional taxes, estimated tax and penalties, carryovers, and year-over-year reasonableness."
---

# Form 1040 — Return Review

## Modes
- **Review**: test a prepared return and write up findings. This is the default.
- **Self-check**: the same steps as a preparer's checklist before sending to review.
- **Explain / REG**: walk through a rule. On "quiz me", give a short problem, then grade.

## Inputs (list what's missing; state every assumption)
- The return as prepared, with all schedules and the state return.
- Source documents: Forms W-2, 1099, 1098, 1095-A, Schedules K-1, brokerage statements, and retirement and HSA forms.
- The prior-year return and carryover schedules.
- A record of estimated payments, with dates and amounts.
- The client's answers on life changes: marriage, divorce, a birth or death, a move, a home sale, a new job or business.

## Calculation rule
Compute in code when a code tool is available.
- **Never use a yearly figure from memory.** The standard deduction, brackets, phaseout ranges, contribution limits, the SALT cap, and credit amounts change every year. Look each one up in the IRS instructions or revenue procedure for the return's tax year, and cite the year.
- Recompute; don't just read. A number that agrees with the software is not yet a number that agrees with the documents.
- Every finding names the line, the amount on the return, the amount it should be, and the document that proves it.

## 1. Identity, status, dependents
- Names, SSNs, dates of birth, address, and bank details agree with the documents.
- Filing status meets its test. Head of household needs all three: unmarried or considered unmarried on the last day of the year, paid more than half the cost of the home, and a qualifying person lived there more than half the year. A dependent parent is the exception: the parent need not live with the taxpayer.
- Each dependent passes the qualifying child tests (relationship, age, residency, support, no joint return) or the qualifying relative tests (gross income, support). For divorced or separated parents, the child is the qualifying child of the parent the child lived with for more nights, unless that parent releases the claim on Form 8332; a release does not transfer head of household status.
- The digital asset question is answered.

## 2. Income completeness
- Tie every W-2, 1099, and K-1 to a line on the return. Compare payers to the prior year and ask about any that are missing.
- Form 1099-B: basis reported or not, wash sales, and the right Form 8949 category.
- Form 1099-R: distribution code, taxable amount, rollovers, and basis on Form 8606. A qualified charitable distribution is excluded from income, and it is not also an itemized deduction. It needs an owner aged 70½ or older and a payment made directly from the IRA to the charity.
- Form 1099-K: the gross amount ties to Schedule C gross receipts, with any personal payments removed.
- Social Security benefits: recompute the taxable part. Provisional income = other income + tax-exempt interest + half the benefits. Base amounts (not indexed): 25,000 and 34,000 single; 32,000 and 44,000 joint. Up to the first base, nothing is taxable. Between the two, the lesser of half the benefits or half the excess over the first base. Above the second, the lesser of 85% of benefits, or 85% of the excess over the second base plus the lesser of half the benefits or half the gap between the bases.
- State tax refund: taxable only to the extent the earlier deduction gave a tax benefit.
- Schedule K-1: read the footnotes for section 199A information, basis, at-risk and passive limits, and foreign items.
- Foreign accounts: Schedule B Part III, and flag FBAR and Form 8938.

## 3. Adjustments and deductions
- HSA: Form 8889 is present; contributions including the employer's (W-2 box 12, code W) are within the limit.
- IRA deduction: test the phaseout when the taxpayer or spouse is covered by a workplace plan.
- Self-employed: half of SE tax, health insurance, and retirement contributions.
- Temporary deductions for tax years 2025 through 2028 (tips, overtime, car loan interest, seniors): check each income phaseout. Tips, overtime, and the senior deduction need a valid SSN and, for married taxpayers, a joint return. Car loan interest needs the VIN on the return, a new vehicle bought for personal use with final assembly in the United States, and a loan made after 2024. The overtime deduction covers only the premium part of the pay: for time-and-a-half, the extra half, which is one third of total overtime pay.
- Standard or itemized: compute both and confirm the better one was used. From tax year 2026, add the non-itemizer deduction for cash gifts to the standard deduction side before comparing. A married-filing-separately taxpayer must itemize if the spouse itemizes.
- From tax year 2026, taxpayers in the 37% bracket have their itemized deductions reduced; check the limitation.
- SALT: apply the cap for the year, including the phase-down for high income and the floor.
- Mortgage interest: ties to Form 1098 and is within the acquisition debt limit.
- Charitable gifts: written acknowledgment for any gift of $250 or more, Form 8283 for noncash gifts over $500, and an appraisal over $5,000. From tax year 2026, itemizers deduct only the part above 0.5% of AGI, and non-itemizers get a limited deduction for cash gifts.
- Medical: only the part above 7.5% of AGI.
- QBI deduction: the right form (8995 or 8995-A), SSTB status, the wage and property limits above the threshold, and loss carryforwards.

## 4. Tax and additional taxes
- Qualified dividends and long-term gains were taxed with the capital gains worksheet.
- Net investment income tax (Form 8960): 3.8% of the lesser of net investment income or MAGI above $200,000 single, $250,000 joint, $125,000 married filing separately. These thresholds are not indexed.
- Additional Medicare tax (Form 8959): 0.9% of wages and self-employment income above the same thresholds.
- Self-employment tax, household employment tax, and the 10% early distribution tax (Form 5329) where they apply.
- AMT (Form 6251): the exemption phaseout thresholds changed for 2026, so look them up. Test when there are incentive stock option exercises, large itemized deductions, or private activity bond interest.
- Kiddie tax (Form 8615) for a child with unearned income.

## 5. Credits
- Child tax credit and credit for other dependents: age at year end, SSN rules, and the income phaseout.
- Dependent care (Form 2441), education credits (Form 1098-T, no double benefit with a 529 withdrawal), and the earned income credit.
- Premium tax credit: Form 8962 is required when Form 1095-A shows advance credit payments, or when the credit is claimed.
- Foreign tax credit: Form 1116, or the election to skip it for small amounts.
- Energy and clean vehicle credits: check the termination dates in the 2025 law before allowing any.
- Paid preparers: Form 8867 due diligence for the EIC, child tax credit, American Opportunity credit, and head of household status.

## 6. Payments and penalties
- Withholding ties to the W-2s and 1099s.
- Estimated payments tie to the client's record by date and amount. The prior-year overpayment applied and any extension payment are included.
- Underpayment penalty (Form 2210). No penalty if the balance due after withholding is under $1,000. Otherwise the safe harbor is the smaller of:
  - 90% of the current-year tax, or
  - 100% of the prior-year tax, raised to 110% when prior-year AGI was above $150,000 ($75,000 married filing separately).
- Withholding counts as paid evenly through the year. Estimates count on the date paid.

## 7. Carryovers
- Capital loss: $3,000 a year against ordinary income ($1,500 married filing separately); the rest carries forward.
- Also check net operating losses, passive losses (Form 8582), suspended basis and at-risk losses, charitable contributions (5 years), foreign tax credits, the AMT credit (Form 8801), and depreciation continuity.
- Each carryover ties to the prior-year return.

## 8. Reasonableness and close-out
- Explain every large change from the prior year.
- The effective tax rate makes sense for the income level.
- The state return starts from the right federal number, and residency and credits for tax paid to other states are right.
- E-file diagnostics are cleared, and Form 8879 and the bank details are ready.
- Next year's estimates are computed with the safe harbor above.

## Tie-outs (report PASS/FAIL)
1. Total of W-2 box 1 = wages on line 1a.
2. Total federal withholding on all documents = the withholding line.
3. Totals of Forms 1099-INT and 1099-DIV = Schedule B.
4. Form 1099-B proceeds = Form 8949 and Schedule D proceeds.
5. Each K-1 = the lines it feeds.
6. Recomputed taxable income and tax = the return.
7. Total payments − total tax = the refund or balance due.

## Output
1. Findings table: number, area, finding, severity (Error, Question, or Note), evidence, fix.
2. Tie-out results.
3. Yearly figures used, each with its source and tax year.
4. Open questions for the client.
5. Sign-off status: Ready, Ready after fixes, or Not ready.

## Worked example
Facts for a 2026 joint return, with 2026 figures taken from IRS guidance: the SALT cap is $40,400, reduced by 30% of MAGI above $505,000, with a floor of $10,000. MAGI is $545,000. State income tax paid is $31,000 and property tax is $14,000. The return deducts $40,400. Prior-year AGI was $480,000, prior-year tax was $96,000, current-year tax is $118,000, and total payments were $101,000, all made evenly.

- SALT: paid 45,000. Cap = 40,400 − 30% × (545,000 − 505,000) = **28,400**. The return is overstated by 12,000. **Error.**
- Safe harbor: 90% × 118,000 = 106,200. Prior-year AGI is above 150,000, so 110% × 96,000 = 105,600. Required = the smaller, **105,600**. Paid 101,000, short by 4,600. **Question:** compute Form 2210 and consider the annualized method.

## Boundaries
This is a review aid, not a substitute for the preparer's judgment or the firm's review policy. Positions that turn on facts, such as residency, material participation, dependency, or valuation, are flagged for the reviewer with the evidence. Use client IDs if firm policy requires.
