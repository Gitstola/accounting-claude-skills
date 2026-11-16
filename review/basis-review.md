# Independent review: s-corp-basis and partnership-basis (skills + eval suites)

Reviewed 2026-11-16 against current law. Files read in full: both SKILL.md files, both build_suite.py files, both answer_key.json files (plus evals/common.py for the key format).

## Bottom line

- **No expected value in either answer key is wrong.** I recomputed all 19 S corporation cases (68 checks) and all 20 partnership cases (61 checks) by hand from the facts, without using the engines. Every number and choice matches the key.
- **No rule statement is flatly wrong.** The problems are overstated rules, missing rules, and a few cases whose facts leave a defensible alternative answer.
- Most serious: (1) S skill says suspended losses are always lost on disposition; (2) S skill has no rule for charitable gifts of appreciated property or for property distributions; (3) partnership skill tests every distribution at year end, which is only the rule for draws and liability shifts, and Case 10 depends on it; (4) partnership skill has nothing on section 736 or on 732(c) allocation among several properties; (5) partnership Cases 13 and 14 contain substantially appreciated inventory with no statement that 751(b) is out of play.

Sources fetched for this review:
- Reg. 1.1367-2: https://www.law.cornell.edu/cfr/text/26/1.1367-2
- Reg. 1.1368-2: https://www.law.cornell.edu/cfr/text/26/1.1368-2
- IRC 1367: https://www.law.cornell.edu/uscode/text/26/1367
- IRC 704: https://www.law.cornell.edu/uscode/text/26/704
- Reg. 1.731-1: https://codes.findlaw.com/cfr/title-26-internal-revenue/cfr-sect-26-1-731-1/
- Instructions for Form 7203 (Rev. 12/2022): https://www.irs.gov/instructions/i7203
- Instructions for Form 7217 (Rev. 12/2024): https://www.irs.gov/instructions/i7217

Not fetched (blocked or not found in the page returned), so stated from my own knowledge of the text: IRC 1366(d), IRC 1368(e), Reg. 1.1366-2, Reg. 1.1367-1, Reg. 1.704-1(d), IRC 731-737, 751, 752 and regs, Rev. Ruls. 64-162, 66-94, 68-537, 81-241/84-102, 94-4, 96-11. Items resting on these are marked "(not fetched)".

---

## A. Findings: skills/s-corp-basis/SKILL.md

| # | Statement | Severity | What is correct | Authority |
|---|---|---|---|---|
| S1 | Sec. 3: "Suspended losses are lost when the shareholder disposes of all the stock." | Misleading (overstated) | True for a sale, gift or death. Two exceptions: (a) a transfer to a spouse, or to a former spouse incident to divorce under section 1041, carries the suspended loss to the transferee; (b) after the S election ends, suspended losses can still be used against stock basis (not debt basis) through the end of the post-termination transition period. Also only a pro rata part is lost on a partial transfer to a spouse; a partial sale loses nothing. The rule covers only basis-suspended losses; passive losses are released by a fully taxable disposition under 469(g). | IRC 1366(d)(2)(B), 1366(d)(3); Reg. 1.1366-2(a)(6), (b) (not fetched) |
| S2 | No rule for charitable contributions of appreciated property | Omission | Stock basis falls only by the shareholder's share of the corporation's adjusted basis in the property, not its fair value, and the basis limit does not apply to the appreciation part of the deduction. The partnership skill has the matching rule; this one does not. A model following the sheet would reduce basis by the full K-1 deduction. | IRC 1367(a)(2) flush sentence (fetched); IRC 1366(d)(4) (not fetched) |
| S3 | No rule for property distributions | Omission | The distribution amount is the property's fair value, the corporation recognizes gain under 311(b) as if it sold the property, and that gain flows through and raises basis before the distribution is tested. | IRC 301(b), 311(b), 1368 (not fetched) |
| S4 | Sec. 5: restoration is "effective immediately before the repayment", with nothing said about reductions | Omission | Restoration is accelerated to just before the first repayment of the year. Reductions for the year's losses are not: they take effect at year end. So in a loss year, a repayment is measured against basis before that year's loss, and the loss then reduces what is left. A model could wrongly cut basis first and overstate gain. | Reg. 1.1367-2(d)(1) (fetched) |
| S5 | Sec. 4 restoration | Omission | Restoration applies only to debt held at the beginning of the year in which the net increase arises. A loan made during the year cannot be "restored" that year. Restoration is also capped at the prior reduction (the skill says this) and Form 7203 caps it at face. | Reg. 1.1367-2(c)(1) (fetched); Form 7203 instructions (fetched) |
| S6 | Sec. 4: net increase = "income items minus distributions, nondeductible expenses, and losses" | Nit | Correct in substance. Precisely, only distributions that are tax-free under 1368 count (1367(a)(2)(A)), not the part taxed as dividend or gain. The engine subtracts the full distribution; I checked that this cannot change a result in the current cases because restoration is also capped by remaining stock basis. | IRC 1367(a)(2)(A), (b)(2)(B) (fetched) |
| S7 | Sec. 5: "An open account balance above $25,000 at year end is treated as a written note from the next year on" combined with "Written note: capital gain" | Nit / could not fully verify | Timing is right. The regulation treats the balance like a written instrument "for purposes of this section", meaning the basis tracking rules. The Form 7203 instructions tie capital gain to a "formal note" and ordinary gain to open account debt. Whether a reclassified balance with no actual note produces capital gain is not settled by the text I fetched; Rev. Rul. 68-537 rests ordinary treatment on the absence of a note. Suggest the skill say reclassification changes tracking (a separate loan, no more netting) and flag character for review. | Reg. 1.1367-2(a)(2)(ii), (d)(2) (fetched); Form 7203 instructions (fetched); Rev. Rul. 68-537 (not fetched) |
| S8 | Sec. 2 distribution ordering with E&P | Nit | Omits the previously-taxed-income layer (pre-1983 S years) between AAA and E&P, the elections to distribute E&P first or make a deemed dividend, and that AAA is a corporate account allocated pro rata when distributions exceed it. Rare, but a model would not know to ask. | IRC 1368(c), (e)(3); Reg. 1.1368-1(f), 1.1368-2(b) (not fetched) |
| S9 | Sec. 2: "In a year with a net loss, apply distributions to AAA before that year's net loss." | Nit | Correct. Clearer wording: "net negative adjustment" means the year's AAA reductions (other than distributions) exceed its AAA increases. Income is added and losses up to that income are subtracted before distributions; only the net excess comes after. | Reg. 1.1368-2(a)(5) (fetched) |
| S10 | Sec. 6: "allocate items per share, per day, unless the corporation elects to close the books" | Nit | The closing-of-the-books election is available only when a shareholder's entire interest terminates (with consent of the affected shareholders) or on a qualifying disposition. | IRC 1377(a)(2); Reg. 1.1368-1(g) (not fetched) |
| S11 | Sec. 1 inputs / starting basis | Omission (minor) | No statement of initial basis rules: cost, carryover for gifts, and date-of-death value reduced by income in respect of a decedent for inherited stock. Also no mention that excluded cancellation-of-debt income does not raise basis, or that basis is tracked share by share with a spillover rule. | IRC 1367(b)(4) (fetched); IRC 108(d)(7)(A); Reg. 1.1367-1(b)(2), (c)(3) (not fetched) |
| S12 | Sec. 4: "Only a direct loan from the shareholder" | Nit | Correct. Worth adding that a loan from the shareholder's other entity does not count, while a genuine back-to-back loan (shareholder borrows, then lends) does. | Reg. 1.1366-2(a)(2) (not fetched) |

## B. Findings: evals/s-corp-basis (build_suite.py, answer_key.json)

No wrong expected values. Case-level notes:

| Case | Severity | Note |
|---|---|---|
| 4, 19 | Nit | "Charitable contributions" should say cash, so finding S2 cannot change the answer. |
| 14 | Nit | Correct as written (6,000 ordinary; ending basis 3,000). The balance is at or below 25,000 at both year ends, so the character issue in S7 does not arise. Keep it that way. |
| 17 | Nit | A January 2 sale would normally leave the seller with one or two days of items under the per-day rule. The case stipulates none, so the answer stands. |
| 15, 16 | Coverage gap | Sole-shareholder facts hide the pro rata AAA allocation. Fine for now. |
| Engine | Nit | `net_increase` subtracts the full distribution rather than the tax-free part (see S6). No effect on current cases. |
| Coverage gaps | Omission | Nothing tests: a loss-year repayment (S4), two loans with restoration priority, a spousal transfer of suspended losses (S1), appreciated-property charitable gift (S2), a property distribution (S3), or a net increase year with a loan made mid-year (S5). |

## C. Findings: skills/partnership-basis/SKILL.md

| # | Statement | Severity | What is correct | Authority |
|---|---|---|---|---|
| P1 | Sec. 2 ordering places all income (step 3) before all distributions (step 4); only the bullet below limits this to "draws and advances" | Misleading | Year-end testing applies to advances or drawings against the partner's share of income, and to deemed distributions from liability decreases. Any other cash distribution is tested against basis immediately before that distribution, on its date. A large one-off mid-year distribution can produce gain even though year-end basis would have covered it. The skill should tell the model to ask whether a distribution was a draw. | Reg. 1.731-1(a)(1)(ii) (fetched); IRC 731(a)(1); Rev. Rul. 94-4 (not fetched) |
| P2 | No treatment of section 736 | Omission | Payments liquidating a retiring or deceased partner's interest split into 736(b) payments (distribution rules) and 736(a) payments (distributive share or guaranteed payment, ordinary). For a general partner in a service partnership, payments for unrealized receivables and unstated goodwill fall under 736(a). The skill's liquidating section would treat the whole payment as a distribution. | IRC 736 (not fetched) |
| P3 | Sec. 5: basis allocation described only for liquidating distributions | Omission | The same allocation applies in a current distribution when outside basis is too small for all the property received: receivables and inventory first, then other property. Where a shortfall or excess must be spread across several properties, it goes first by unrealized depreciation or appreciation, then by relative basis or value. The engine just walks the list in order; no current case has two properties, so no key value is affected. | IRC 732(a)(2), 732(c) (not fetched) |
| P4 | Sec. 3: 704(d) "includes ... charitable contributions, and foreign taxes" | Correct but incomplete | Right for years beginning after 2017. Missing the exception: for a gift of appreciated property, the limit does not apply to the partner's share of the appreciation. | IRC 704(d)(3)(A), (B) (fetched) |
| P5 | Sec. 2 step 5: "Subtract nondeductible, noncapital expenses" with no rule for an excess over basis | Omission / unsettled | The basis limit in 704(d) does not by its terms cover these expenses, and no authority I know of says whether an excess carries forward to reduce later basis. The engine silently drops it. The skill should say this is unsettled and flag it. | IRC 705(a)(2)(B) (not fetched); could not verify any authority resolving it |
| P6 | Sec. 4: "Recourse debt goes to the partner who bears the economic risk of loss, including a partner who guarantees it." | Misleading (overstated) | A guarantee shifts the debt only if the guarantor would bear the loss with no right of reimbursement from another partner. A limited partner's guarantee of general-partnership recourse debt usually does not, and bottom-dollar guarantees are disregarded. | Reg. 1.752-2(b)(3), (b)(5), (f) (not fetched) |
| P7 | Sec. 4: "In an LLC, debt is nonrecourse to the members unless a member guarantees it." | Nit | Also recourse to a member who is (or is related to) the lender. | Reg. 1.752-2(c) (not fetched) |
| P8 | Sec. 4: nonrecourse debt "generally shared by profit percentage, after any minimum gain allocations" | Nit | Three tiers: partnership minimum gain, then 704(c) minimum gain (gain the contributor would be allocated if the property were given up for the debt), then profits. The second tier matters for contributed encumbered property (see Case 3 note). | Reg. 1.752-3(a) (not fetched) |
| P9 | Sec. 5: "most marketable securities at fair value" | Nit | The amount treated as money is reduced by the partner's share of the partnership's net gain in securities of that type; several exceptions apply. | IRC 731(c)(3)(B) (not fetched) |
| P10 | Sec. 6 sale | Omission (minor) | No mention of look-through for collectibles and unrecaptured 1250 gain, the three-year holding rule for carried interests, or the seller's statement. Also the capital piece is a residual and can be a loss alongside ordinary income. | Reg. 1.1(h)-1, 1.751-1(a)(2); IRC 1061 (not fetched) |
| P11 | Sec. 1: "Gift: the donor's basis. Inheritance: fair value at death." | Nit | Gift: lower of donor basis or value for loss purposes, and a gift of an interest with debt above basis is part sale. Inheritance: reduced by income in respect of a decedent. | IRC 1015, 1014(c) (not fetched) |
| P12 | Flags list | Omission (minor) | Add disguised sales (contribution and related distribution within two years) and 743(b)/754 adjustments, which are not part of outside basis but often explain K-1 reconciliation differences. Form 7217 statement is correct; the exceptions are money-only distributions and securities treated as money. | IRC 707(a)(2)(B); Form 7217 instructions (fetched) |
| P13 | Sec. 3: at-risk "leaves out nonrecourse debt, except qualified nonrecourse financing on real estate" | Nit | Correct. Also excludes amounts borrowed from a person with an interest in the activity and amounts protected by guarantees or stop-loss arrangements. | IRC 465(b) (not fetched) |

## D. Findings: evals/partnership-basis (build_suite.py, answer_key.json)

No wrong expected values. Case-level notes:

| Case | Severity | Note |
|---|---|---|
| 10 | Ambiguous case | "Cash distributions 22,000" with beginning basis 10,000 and income 5,000. Key: gain 7,000, which assumes year-end testing. Nothing says the cash was a draw against income (compare Case 9, which does). If it was a single distribution early in the year, gain is up to 12,000 and ending basis 5,000. Fix by stating the distributions were draws against current-year income, or by giving the date and asking for date-of-distribution testing. Reg. 1.731-1(a)(1)(ii). |
| 13, 14 | Ambiguous case | Both hand a liquidating partner inventory that is substantially appreciated (12,000 vs 8,000 basis is 150%; 11,000 vs 9,000 is 122%, over the 120% line). If the partner received more or less than a proportionate share, 751(b) recharacterizes part of the distribution as a sale, changing gain, character and basis. Add "the partner receives exactly a proportionate share of the partnership's inventory; 751(b) does not apply." IRC 751(b), (b)(3) (not fetched). |
| 3 | Nit (stipulated) | Answer is right given the stipulated 20% share. A careful practitioner would note that if the mortgage is nonrecourse, the contributor is first allocated the 30,000 excess of debt over basis, giving a 32,000 share, 8,000 net relief and no gain. Say the mortgage is recourse and shared 20/80, or keep the stipulation and add "under section 752." |
| 8 | Nit | Title says "after a refinancing"; facts say the partnership paid down debt. Answer (18,000 deemed distribution, 6,000 capital gain, basis 0) is correct with the year's income added first, per Rev. Rul. 94-4. |
| 16 | Correct | Ending outside basis 20,000 is right: basis falls by the full loss allowed under 704(d) even though at-risk defers 20,000 of it. Good trap. |
| 18 | Correct | 4,000 reduction per Rev. Rul. 96-11. Could add a question on the deduction amount (10,000 share of fair value) to test the 704(d)(3)(B) exception. |
| 4 | Nit | Says "cash charitable contributions": good. |
| Engine | Nit | Property bases are assigned in list order, not under 732(c); excess nondeductible expenses are dropped silently (P5). Neither affects a current case. |
| Coverage gaps | Omission | Nothing tests: a non-draw mid-year distribution, two properties with insufficient basis, a 736 payout, marketable securities, a recourse versus nonrecourse share change, or nondeductible expenses above basis. |

## E. Checked and found correct

S corporation skill:
- Ordering: income, then distributions, then nondeductible expenses, then losses. Matches Form 7203 Part I.
- Nondeductible expenses above stock and debt basis are lost without the election; with the Reg. 1.1367-1(g) election, losses go first and the unused expenses carry forward; the election binds later years (Form 7203 instructions, fetched).
- Distributions tested against stock basis only; debt basis never shelters a distribution; distributions never reduce debt basis (IRC 1367(b)(2)(A), fetched).
- Pro rata allowance of loss items; carryover indefinite and treated as incurred next year.
- Net increase definition, debt restored before stock, repaid loan restored first then others in proportion to reductions (Reg. 1.1367-2(c), fetched).
- Restoration effective immediately before the first repayment (Reg. 1.1367-2(d)(1), fetched).
- Repayment gain = repayment × (1 − basis ÷ face); capital on a note, ordinary on open account (Form 7203 instructions, fetched).
- Open account netting at year end and the 25,000 threshold timing (Reg. 1.1367-2(a)(2), (d)(2), fetched).
- AAA: tax-exempt income excluded; distributions cannot make it negative, losses can; distributions applied before the net negative adjustment (Reg. 1.1368-2(a)(2), (a)(5), fetched).
- E&P dividend does not reduce stock basis.
- Guarantee creates no debt basis until paid.
- Order of limits: basis, at-risk, passive, excess business loss.
- Form 7203 filing triggers (fetched).
- Worked example, all three stages, including the 7,000 net increase after counting the 13,000 carryover and the 2,333.33 / 7,666.67 split.

Partnership skill:
- Initial basis for contributions (adjusted basis, not value) and netting of debt relief against the contributor's liability share.
- Ordering: distributions and nondeductible expenses before losses (Reg. 1.704-1(d)(2), Rev. Rul. 66-94, not fetched).
- 704(d) covers capital losses, section 179, charitable contributions and foreign taxes under current law (IRC 704(d)(3)(A), fetched).
- Pro rata allowance; indefinite carryover; no transfer to a buyer or donee.
- Liability increase as a cash contribution, decrease as a cash distribution.
- Current distribution: gain only if money exceeds basis, no loss, money first, carryover basis capped at remaining outside basis.
- Liquidating distribution: substituted basis, receivables and inventory capped at partnership basis, loss only when nothing but money, receivables and inventory is received (Reg. 1.731-1(a)(2), fetched).
- Seven-year periods for 704(c)(1)(B) and 737.
- Form 7217: one per distribution date, not for money-only distributions (fetched).
- Sale: amount realized includes liability relief; 751(a) covers all inventory, not only substantially appreciated inventory.
- Charitable gift reduces basis by share of adjusted basis (Rev. Rul. 96-11, not fetched).
- At-risk excludes nonrecourse debt other than qualified nonrecourse financing.
- Worked example and its alternative.

Answer keys: every check in both files recomputed and matched (S corp 1a-19h; partnership 1a-20g), including the fractional values 29,155.56 / 2,844.44 and 10,968.75 / 2,031.25, and the negative ending AAA of −7,000 in S corp Case 16.
