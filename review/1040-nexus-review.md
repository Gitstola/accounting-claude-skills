# Independent review: form-1040-review and state-nexus (skills + eval suites)

Reviewed 2026-11-16 against law as of November 2026 (P.L. 119-21; Rev. Proc. 2025-32). Every test-case answer was recomputed by hand from the facts, not from the script functions. "Fetched" = I read the source this session; "not fetched" = stated from my knowledge of the Code/UDITPA and not re-read today.

Source URLs used
- [IRS-OBBB-DED] https://www.irs.gov/newsroom/one-big-beautiful-bill-act-tax-deductions-for-working-americans-and-seniors (fetched)
- [IRS-OBBB-PROV] https://www.irs.gov/newsroom/one-big-beautiful-bill-provisions (fetched)
- [IRS-2026] https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2026-including-amendments-from-the-one-big-beautiful-bill (fetched)
- [KPMG-RP] https://kpmg.com/kpmg-us/content/dam/kpmg/taxnewsflash/pdf/2025/10/25297.pdf (fetched; secondary summary of Rev. Proc. 2025-32)
- [I8962] https://www.irs.gov/pub/irs-prior/i8962--2025.pdf (fetched)
- [I8867] https://www.irs.gov/pub/irs-prior/i8867--2025.pdf (fetched)
- [IRS-ENERGY] https://www.irs.gov/newsroom/faqs-for-modification-of-sections-25c-25d-25e-30c-30d-45l-45w-and-179d-under-public-law-119-21-139-stat-72-july-4-2025-commonly-known-as-the-one-big-beautiful-bill-act-obbb (fetched)
- [USC164] https://www.customsmobile.com/uscode/26/164 (fetched; unofficial mirror of 26 U.S.C. 164(b)(7))
- [TAFT] https://www.taftlaw.com/news-events/law-bulletins/charitable-giving-after-the-obbba-the-2026-outlook/ (fetched; secondary)
- [WCPE] https://www.westerncpe.com/taxbyte/irs-premium-tax-credit-faq-update-what-to-know-for-2026/ (fetched; secondary)
- [QCD-Y] https://www.thinkadvisor.com/tax-facts/2026/07/24/irs-confirms-qcd-code-y-optional-in-2026/ (fetched; secondary)
- [MTC-FP] https://www.mtc.gov/wp-content/uploads/2022/12/Factor-Presence.pdf (fetched; model statute text)
- [MTC-86272] https://www.mtc.gov/wp-content/uploads/2023/02/Statement-of-Information-discussion-draft-7-2.pdf (fetched; a discussion draft of the revised Statement, not the final adopted text)
- [UT-305] https://law.counselstack.com/statute/ut/59-7-305 (fetched; a state enactment of UDITPA sec. 3)

---

## A. Findings: form-1040-review

### A1. Test case 4 (4d, 4e) - Wrong
- File: evals/form-1040-review/build_suite.py and answer_key.json, checks 4d ("yes") and 4e (1,800).
- Problem: the case is a 2026 joint return taking the standard deduction with 6,000 of acknowledged cash gifts to public charities. For 2026 a non-itemizer may deduct cash gifts up to 1,000 (2,000 joint) under sec. 170(p). The comparison is therefore:
  - Standard route: 32,200 + 2,000 = 34,200
  - Itemized route: 12,000 + 14,000 + (6,000 - 1,000) + (18,000 - 15,000) = 34,000
  - The standard route is better by 200. Correct 4d = "no".
  - 4e: itemizing gives no additional deduction. If the return as prepared omitted the 2,000 non-itemizer deduction (the facts do not say), the additional deduction available is 2,000, not 1,800.
- 4a (5,000), 4b (3,000), 4c (34,000) are correct.
- The result holds even if one reads the 0.5% floor into sec. 170(p) (6,000 - 1,000 = 5,000, still above the 2,000 cap). Whether the floor applies to the non-itemizer deduction I could not confirm from statute text today; IRS and practitioner summaries describe the floor as an itemizer rule.
- Fix options: change the expected answers, or change the facts so the answer is unambiguous (for example make the gifts noncash or to a donor-advised fund, which do not qualify under 170(p), or raise mortgage interest so itemizing wins by more than 2,000), and state whether the return claimed the non-itemizer deduction.
- Authority: sec. 170(p) as amended by P.L. 119-21; [IRS-OBBB-PROV] ("individuals who do not itemize may deduct up to $1,000 of cash contributions", 2,000 joint, from 2026); [TAFT] (cash only, to 170(b)(1)(A) organizations, not supporting organizations or donor-advised funds).

### A2. SKILL.md sec. 3, "Standard or itemized: compute both and confirm the larger one was used" - Misleading
- This is the rule that produces the wrong answer in case 4. From 2026 the comparison must be itemized total versus standard deduction plus the sec. 170(p) non-itemizer charitable deduction. The skill mentions the non-itemizer deduction two bullets later but never ties it into the comparison.
- Also not always "the larger": a married-filing-separately taxpayer whose spouse itemizes must itemize (sec. 63(c)(6)(A)), and a taxpayer may elect to itemize a smaller amount for state-tax reasons. Not fetched; Code.
- Authority: as A1.

### A3. SKILL.md sec. 5, "Premium tax credit: Form 8962 is required whenever there is a Form 1095-A" - Misleading (overstated), plus 2026 Omission
- Correct rule: Form 8962 is required if the taxpayer claims the PTC or APTC was paid for anyone in the tax family (or for someone the taxpayer told the Marketplace would be in the family). A 1095-A with no APTC and no PTC claim does not by itself require the form. [I8962]
- Omission for 2026 returns: the repayment caps on excess APTC are removed for tax years beginning after 2025, so the whole excess is repaid. A reviewer using pre-2026 cap tables will understate tax. [IRS-OBBB-PROV]; [WCPE].
- Not verified: whether the enhanced (above 400% of poverty line) subsidies were extended for 2026. I found no confirmation of an extension; check before relying on it.
- Case 16 (APTC of 3,600, no Form 8962) is still correct: required, Error.

### A4. SKILL.md sec. 3, temporary 2025-2028 deductions bullet - Misleading / Omission
- "check each income phaseout, the required SSN, the joint-return rule for married taxpayers, and the VIN for car loan interest" reads as if SSN and joint-return rules apply to all four. The IRS page lists the SSN and married-must-file-jointly conditions for tips, overtime, and seniors; for car loan interest it lists the VIN requirement and neither of the other two. Denying car loan interest to a married-filing-separately filer on this bullet would be wrong. [IRS-OBBB-DED] (the page is silent on SSN/joint for car loan interest; I did not re-read sec. 163(h)(4) today).
- The conditions that most often produce wrong amounts are missing from the skill, though cases 14 and 15 test two of them: [IRS-OBBB-DED]
  - Tips: cap 25,000 (per return, not doubled on a joint return); phaseout over 150,000 / 300,000 joint; occupation on the IRS list; no SSTB; self-employed limited to net income of the business; tips must be reported on a W-2/1099/Form 4137.
  - Overtime: only the premium portion required by the FLSA (the "half" of time-and-a-half); cap 12,500 / 25,000 joint; phaseout over 150,000 / 300,000.
  - Car loan interest: cap 10,000; phaseout over 100,000 / 200,000; new vehicle only, final assembly in the U.S., loan originated after 12/31/2024, personal use, secured by the vehicle, leases excluded.
  - Seniors: 6,000 per eligible individual age 65 by year end; phaseout over 75,000 / 150,000.
  - All four are available to itemizers and non-itemizers. They are deductions from taxable income, not adjustments to AGI, so they do not lower AGI-based tests (SALT phase-down MAGI, NIIT, IRA phaseouts, medical and charitable floors). Not fetched for the AGI point; Code structure (secs. 63(b), 224, 225).
- The skill puts the cap/phaseout numbers under "never from memory", which is fine, but it should at least name the conditions.

### A5. SKILL.md sec. 3 - Omission: 2026 limitation on itemized deductions for the 37% bracket
- From 2026, new sec. 68 reduces the tax benefit of itemized deductions for taxpayers in the 37% bracket (benefit effectively capped at 35%). The skill has no check for it; high-income itemized returns for 2026 will be overstated. [KPMG-RP]; [TAFT].

### A6. SKILL.md sec. 4, AMT bullet - Omission (outdated trigger list for 2026)
- For 2026 the AMT exemption phaseout starts at 500,000 single / 1,000,000 joint (down from the 2025 indexed levels) [IRS-2026], and P.L. 119-21 doubles the phaseout rate (rate change not fetched). More returns in the 500,000-1,000,000+ range need an AMT test even without ISOs. The skill's trigger list (ISOs, large itemized deductions, private activity bond interest) should add "income above the exemption phaseout threshold" and note that SALT is the main itemized add-back.

### A7. SKILL.md sec. 1, head of household - Misleading / Omission
- "a qualifying person lived there more than half the year" has a standard exception: a dependent parent need not live with the taxpayer (the taxpayer must pay more than half the cost of the parent's home). Also missing: temporary absences count as time lived in the home; a qualifying relative who is a dependent only because they lived with the taxpayer all year (unrelated person) is not a qualifying person; a custodial parent keeps HOH even after releasing the dependency claim on Form 8332; "considered unmarried" requires the spouse to be out of the home for the last six months and the qualifying person to be the taxpayer's child. Authority: sec. 2(b), sec. 7703(b); Pub. 501 (not fetched today).
- Case 11 is unaffected (child lived with her 5 months; answer "no"/"single" is right).

### A8. SKILL.md sec. 2, QCD - Omission (statement itself is correct)
- Correct as far as it goes: excluded from income, no itemized deduction. Missing conditions that decide whether it is a QCD at all: owner age 70 1/2 or older on the date of distribution; paid directly by the trustee to an eligible charity (not a donor-advised fund, supporting organization, or private non-operating foundation); annual limit (111,000 for 2026 [QCD-Y]); reduced by deductible IRA contributions made after age 70 1/2; not from an ongoing SEP/SIMPLE. Also the Form 1099-R does not reliably identify a QCD (code Y is optional for 2025 and 2026 [QCD-Y]), so the reviewer must ask and see the acknowledgment. Authority: sec. 408(d)(8) (not fetched).

### A9. SKILL.md sec. 5, Form 8867 "education credit" - Nit
- Due diligence covers the EIC, CTC/ACTC/ODC, the American Opportunity Tax Credit, and HOH status. It does not cover the Lifetime Learning Credit. Say "AOTC". [I8867]

### A10. SKILL.md sec. 4, Additional Medicare Tax "0.9% of wages and self-employment income above the same thresholds" - Misleading in one fact pattern
- Works when both are positive (case 9). It is wrong if read as netting: a self-employment loss does not reduce wages for this tax; the threshold for SE income is the filing-status threshold reduced (not below zero) by wages; RRTA compensation is tested separately. Also worth stating: the employer withholds once wages pass 200,000 regardless of filing status, so joint filers are often under- or over-withheld and Form 8959 reconciles. Authority: sec. 3101(b)(2), sec. 1401(b)(2); Form 8959 instructions (not fetched).

### A11. SKILL.md sec. 6, underpayment penalty - Omissions (stated rules are correct)
- Missing: no penalty when the prior year had no tax liability (full 12-month year, U.S. citizen or resident); the prior-year safe harbor needs a 12-month prior year; the required annual payment is tested per installment (25% by each due date), so meeting the annual total with late estimates does not avoid the penalty (the skill hints at this with "estimates count on the date paid" but never says it); farmers and fishermen use 66 2/3%; the taxpayer may elect to treat withholding as paid when actually withheld. Authority: sec. 6654(d), (e), (g), (i) (not fetched).

### A12. SKILL.md sec. 3, charitable bullet - Nit / Omission
- Stated rules are right (250 acknowledgment; Form 8283 over 500; qualified appraisal over 5,000, with the publicly traded securities exception unstated; 0.5% floor from 2026; non-itemizer deduction). Missing: the non-itemizer amounts are capped at 1,000 / 2,000 joint and exclude noncash gifts, donor-advised funds, and supporting organizations [TAFT]; the 35% benefit limit in A5.

### A13. SKILL.md sec. 2 - Omission: Form 1099-DA
- Digital asset sales by brokers are reported on Form 1099-DA starting with 2025 transactions (gross proceeds; basis for covered assets from 2026). The skill checks only the yes/no question and Form 1099-B. Not fetched.

### A14. SKILL.md sec. 3 - smaller omissions (Nit)
- Schedule 1-A is the form on which the four temporary deductions are claimed; the skill never names it. Not fetched.
- Mortgage interest: the 750,000 acquisition-debt limit (1,000,000 for pre-12/16/2017 debt) is now permanent, home-equity interest is deductible only when the loan bought, built, or improved the home, and mortgage insurance premiums are again treated as interest from 2026. Not fetched.
- QBI: from 2026 the phase-in range widens and a minimum deduction applies. Not fetched.
- Qualifying relative tests listed as "(gross income, support)" leave out relationship/member-of-household and not-a-qualifying-child; tie-breaker rules are not mentioned.

### A15. Case 21 - Ambiguous case (answers as keyed are correct)
- Recomputed: SALT cap 40,400 - 30% x 15,000 = 35,900 (21a); NIIT 3.8% x min(60,000, 270,000) = 2,280 (21b); required payment min(106,200, 114,400) = 106,200 (21c); 89,000 short (21d no); wages 310,000 + 150,000 = 460,000 ties (21e yes); 21f no.
- Gap: joint Medicare wages of 460,000 exceed 250,000, so Additional Medicare Tax of 0.9% x 210,000 = 1,890 is due and Form 8959 is required. The facts say "no Form 8960" but are silent on Form 8959, and the key has no check for it. A good deliverable will raise it; a grader comparing memos to the key may treat it as noise. Either state that Form 8959 is on the return or add a check.
- "Based on the total tax as prepared" in 21c is a necessary hedge and is there; corrected tax would be higher.

### A16. Case 10 - Nit
- 10b (11,500 carryover) assumes taxable income before the loss deduction is at least 3,000; the Capital Loss Carryover Worksheet gives a larger carryover otherwise. Add "taxable income is positive" to the facts.

### A17. Severity checks 1d, 16b, 18b - no change needed
- All three are computational or required-form errors with complete facts; "Error" is the only reasonable label under the skill's own scale. Not ambiguous.

---

## B. Findings: state-nexus

No expected value in the state-nexus suite is wrong. All 22 cases recomputed and agree with the key. Findings below are rule statements and omissions.

### B1. SKILL.md sec. 3.3, throwback trigger "not taxable, because it has no nexus there or is protected by P.L. 86-272" - Misleading / Omission
- Under UDITPA sec. 3 a taxpayer is "taxable in another state" if it is subject there to a net income tax, a franchise tax measured by net income, a franchise tax for the privilege of doing business, or a corporate stock tax, or if that state has jurisdiction to impose a net income tax whether or not it actually does. So sales into a state with no corporate income tax are not thrown back when the company's activities there exceed P.L. 86-272 protection. A model following the skill could throw back sales to a no-income-tax state where the company has an office. [UT-305]
- Also missing from the throwback rule: sales to the U.S. government shipped from the state are thrown back regardless of taxability (UDITPA sec. 16(b), not fetched); drop shipments from a third state; states differ on Joyce vs. Finnigan for combined groups; some states apply throwout to services and intangibles, not just goods.

### B2. SKILL.md sec. 2, P.L. 86-272 - Omissions (statements made are correct)
- Missing rules that commonly flip the answer: [MTC-86272], and 15 U.S.C. 381-384 (statute not fetched)
  - Independent contractors may solicit, make sales, and keep an office in the state without ending protection (but may not hold the company's stock of goods beyond samples).
  - De minimis unprotected activity does not end protection; activities "entirely ancillary" to solicitation are protected (Wrigley).
  - The law covers interstate commerce only; a state may choose whether to extend it to foreign commerce. It does not protect a corporation in its state of incorporation.
  - A sales employee's in-home office used only for solicitation is protected; any other office is not.
  - "Customer training" is overbroad as written: the unprotected item is training for personnel other than those involved only in solicitation; training the company's own sales staff is protected.
  - A non-sales remote employee in the state (case 21 pattern) ends protection for a goods seller for that state.
- The skill's unprotected list (repairs, installation, collections, inventory, office, approving orders, services, digital products, non-income taxes, post-sale chat in some states) checks out against [MTC-86272].

### B3. SKILL.md sec. 2, order of tests - Misleading
- "Property or payroll in the state creates nexus" and the factor-presence bullet come before P.L. 86-272 with no statement that 86-272 overrides both for a seller of goods. The MTC model says so expressly: a state without jurisdiction under P.L. 86-272 does not gain it because a threshold is exceeded. Add one sentence. Case 22b depends on getting this right. [MTC-FP] subsection E.

### B4. SKILL.md sec. 2, MTC factor presence thresholds - correct, with one Omission
- 50,000 property, 50,000 payroll, 500,000 sales, or 25% of total property, payroll, or sales; any one "exceeded during the tax period". Confirmed. The model also adjusts the dollar amounts when the CPI has moved 5% or more since 2003, so "the MTC amounts" today are not necessarily the original ones. The cases say "at its original amounts", which avoids the problem. [MTC-FP]

### B5. SKILL.md worked example - Nit
- The throwback/throwout example never says the company is taxable in State B. If it were not, B's 2,400,000 would also be thrown back (or out). Add "it has nexus in B". Arithmetic is right: 1,600,000 / 4,000,000 = 40% and 200,000; 1,000,000 / 3,400,000 = 29.41% and 147,058.82.

### B6. SKILL.md sec. 1, economic nexus and marketplace - Omissions
- "Exceeds" versus "meets or exceeds": state statutes differ, and it decides boundary cases. The skill says only "compare".
- Step 5 ("tax is owed from that date forward") is the usual rule but the start point varies from the next transaction to a fixed lead time; fine as written since it says to record the state's rule.
- Physical-presence bullet: some states carve out inventory held in a marketplace facilitator's warehouse for sellers that sell only through that marketplace. Stated as an absolute. Check the state. Not fetched.
- Marketplace-only sellers may still have registration or zero-return filing duties in some states; exposure should also exclude sales covered by valid exemption or resale certificates and should use the combined state and local rate. Home-rule local jurisdictions are out of scope per Boundaries, which is acceptable if flagged in output.

### B7. SKILL.md sec. 3.4, property factor - Nit
- Correct: owned property at original cost, average of beginning and ending; rented property at 8 x net annual rent. Missing details: rent is net of subrents; the state may require monthly averaging when balances fluctuate; construction in progress is normally excluded. UDITPA secs. 10-12 (not fetched).

### B8. SKILL.md sec. 3.2, cost of performance - Nit
- Correct for the UDITPA all-or-nothing rule ("greater proportion ... than in any other state, based on costs of performance"). Some states use a pro rata version. The skill says "use the state's method", which covers it.

### B9. Case 7 - Ambiguous case (minor)
- 7b "yes" rests on the general rule that stored inventory is physical presence. The case gives only State T's economic rule. Correct in most states, but see B6 on marketplace-inventory carve-outs. Add a given rule ("State T treats inventory stored in the state as physical presence").

### B10. Case 22 - Nit
- 22b is "no" for two independent reasons (sales of exactly 500,000 do not "exceed" 500,000; P.L. 86-272 protects solicitation of goods), so it cannot tell whether the model applied 86-272. Make State D sales 600,000 if the intent is to test the override in B3.
- 22a is "yes" on the economic threshold and also on the visiting rep's physical presence; fine.

---

## C. Checked and found correct

Form 1040 skill
- SALT 2026: cap 40,400, threshold 505,000, 30% reduction, 10,000 floor; worked example 28,400 and 12,000 overstatement. [USC164] for 40,400 / 505,000; the 30% rate and 10,000 floor are from the statute as I know it (the mirror page did not show that clause).
- 2026 standard deduction 32,200 joint. [IRS-2026]
- Medical floor 7.5% of AGI. Charitable 0.5% floor for itemizers from 2026; 5-year carryover.
- NIIT 3.8%, thresholds 200,000 / 250,000 / 125,000, not indexed.
- Additional Medicare Tax rate and thresholds (see A10 for mechanics).
- Safe harbor: lesser of 90% current or 100% / 110% prior (150,000; 75,000 MFS); 1,000 rule measured after withholding; withholding deemed paid evenly. Worked example 105,600 and 4,600 shortfall.
- Capital loss 3,000 / 1,500 MFS.
- QCD excluded and not deductible. State refund tax-benefit rule. Form 8283 / appraisal / 250 thresholds.
- Energy and clean vehicle terminations exist and differ by section: 25C and 25D after 12/31/2025; 25E, 30D, 45W vehicles acquired after 9/30/2025; 30C after 6/30/2026. [IRS-ENERGY]
- Form 8867 scope apart from A9. [I8867]

Form 1040 cases (all recomputed): 1 (23,900 / 23,900 / 16,500), 2 (10,000), 3 (26,500), 4a-4c, 5 (21,000; yes), 6 (66,000; no; 2,000), 7 (700; no), 8 (3,040; 570), 9 (630; 270; yes), 10 (3,000; 11,500; 11,500), 11 (no; single), 12 (87,550; 7,900; 10,040; no), 13 (30,000; 0), 14 (25,000; 6,000), 15 (10,000; 20,000), 16, 17 (44,000; 13,000; 7,400), 18, 19 (16,480; 1,800), 20 (26,700; 2,390; 900), 21a-21f. Only 4d and 4e are wrong.

State nexus skill
- MTC factor presence amounts and "any one exceeded". [MTC-FP]
- P.L. 86-272 core statement and the unprotected list. [MTC-86272]
- Economic nexus steps; marketplace facilitator collects while seller collects on direct sales; throwback adds to the numerator and throwout removes from the denominator; destination sourcing for goods; zero-denominator factor dropped; 8 x rent; nonbusiness income allocated.

State nexus cases (all recomputed): 1 (95,000; no), 2 (155,000; yes; facilitator), 3 (yes), 4 (no), 5 (70,000; no), 6 (August; October; 3 x 13,000 x 6% = 2,340), 7 (no; yes), 8 (no; yes), 9 (yes), 10 (no; yes), 11 (27.14%; yes), 12 (no), 13 (15%; 300,000), 14 (23.33%; 210,000), 15 (23.75%; 213,750), 16 (20%), 17 (900,000; 4,600,000; 19.57%), 18 (3,000,000; 37.5%; 600,000), 19 (7,000,000; 28.57%; 457,142.86), 20 (500,000; 500,000; 0), 21 (yes; 85,000), 22 (yes; no; 33.33%; 400,000; 40.83%; 490,000).

## D. Not verified
- Statute text of sec. 170(p) and sec. 170(b)(1)(I) (the Code site was not reachable); relied on IRS and practitioner summaries.
- Whether the enhanced ACA premium subsidies were extended for 2026.
- Any 2026 legislation or guidance after mid-2026 that changes the items above.
- Items marked "not fetched" in the findings.
