# Test cases: partnership-basis

Each case is one partner for one tax year unless it says otherwise. Amounts are in dollars.

## How to answer
Write your answers to `answers.json` as one JSON object that maps each question ID to its answer.
- Number questions: a plain number, no commas or currency signs. Percentages as a number, for example 23.75 for 23.75%.
- Choice questions: exactly one of the listed choices, spelled as shown.
Answer every ID. Do the arithmetic in Python.

## Case 1: Formation with cash and property

Dana joins a new partnership as a 50% partner. She contributes cash of 20,000 and equipment with an adjusted basis of 35,000 and a fair value of 60,000. The partnership has no liabilities.

Questions:
- **1a** Dana's initial outside basis. (number)
- **1b** Gain Dana recognizes on the contribution. (number)

## Case 2: Contributed property subject to debt

Avery contributes land to a partnership for a 25% interest. The land has an adjusted basis of 40,000 and a fair value of 100,000, and it is subject to a 30,000 mortgage that the partnership assumes. After the contribution Avery's share of that liability is 25%. The partnership has no other liabilities.

Questions:
- **2a** Avery's outside basis right after the contribution. (number)
- **2b** Gain Avery recognizes. (number)

## Case 3: Debt relief above basis

Blake contributes a building to a partnership for a 20% interest. Adjusted basis 10,000; fair value 90,000; subject to a 40,000 mortgage that the partnership assumes. After the contribution Blake's share of that liability is 20%. The partnership has no other liabilities.

Questions:
- **3a** Net liability relief treated as money distributed to Blake. (number)
- **3b** Gain Blake recognizes. (number)
- **3c** Blake's outside basis right after the contribution. (number)

## Case 4: Ordinary year

Beginning outside basis 30,000. Share of partnership liabilities is 10,000 at both the beginning and the end of the year.
K-1: ordinary income 18,000; tax-exempt interest 2,000; nondeductible expenses 1,000; cash charitable contributions 3,000; cash distributions 12,000.

Questions:
- **4a** Gain recognized on the distributions. (number)
- **4b** Ending outside basis. (number)

## Case 5: Loss limited by basis

Beginning outside basis 25,000. Share of liabilities unchanged during the year.
K-1: ordinary loss 40,000; cash distributions 5,000.

Questions:
- **5a** Basis available for the loss. (number)
- **5b** Ordinary loss allowed under the basis limit. (number)
- **5c** Loss suspended. (number)
- **5d** Ending outside basis. (number)

## Case 6: Several loss items exceed basis

Beginning outside basis 18,000. Share of liabilities unchanged. No distributions.
K-1: ordinary loss 24,000; long-term capital loss 6,000; section 179 deduction 6,000.

Questions:
- **6a** Ordinary loss allowed. (number)
- **6b** Long-term capital loss allowed. (number)
- **6c** Section 179 deduction allowed. (number)
- **6d** Total suspended. (number)

## Case 7: Liability increase frees up a loss

Beginning outside basis 5,000 (this already includes the beginning share of liabilities). K-1 item K shows the partner's share of liabilities at 20,000 at the beginning of the year and 50,000 at the end.
K-1: ordinary loss 30,000. No distributions.

Questions:
- **7a** Basis available for the loss. (number)
- **7b** Ordinary loss allowed under the basis limit. (number)
- **7c** Ending outside basis. (number)

## Case 8: Liability decrease after a refinancing

Beginning outside basis 8,000 (including the beginning share of liabilities). K-1 item K: share of liabilities 30,000 at the beginning of the year and 12,000 at the end, after the partnership paid down debt.
K-1: ordinary income 4,000. No cash distributions.

Questions:
- **8a** Deemed cash distribution. (number)
- **8b** Gain recognized. (number)
- **8c** Character of the gain (assume no hot assets). Choices: capital, ordinary, none.
- **8d** Ending outside basis. (number)

## Case 9: Draws during the year

Beginning outside basis 3,000. Share of liabilities unchanged. The partner took draws against current-year earnings of 20,000, spread through the year. K-1: ordinary income 25,000; distributions 20,000.

Questions:
- **9a** Gain recognized on the draws. (number)
- **9b** Ending outside basis. (number)

## Case 10: Cash distribution above basis

Beginning outside basis 10,000. Share of liabilities unchanged. On January 15 the partnership made a one-time cash distribution of 22,000 to the partner out of prior-year cash. It was not a draw or advance against current-year earnings, and no income had been earned yet. K-1 for the year: ordinary income 5,000. The partnership holds no unrealized receivables or inventory.

Questions:
- **10a** Gain recognized. (number)
- **10b** Character of the gain. Choices: capital, ordinary, none.
- **10c** Ending outside basis. (number)

## Case 11: Current distribution of property, basis-limited

Outside basis just before the distribution, after all other items for the year, is 14,000. In a current (non-liquidating) distribution the partner receives cash of 4,000 and land. The partnership's adjusted basis in the land is 15,000 and its fair value is 25,000. Share of liabilities unchanged.

Questions:
- **11a** Gain recognized by the partner. (number)
- **11b** The partner's basis in the land. (number)
- **11c** Outside basis after the distribution. (number)
- **11d** Is Form 7217 required? Choices: yes, no.

## Case 12: Current distribution of property, ample basis

Outside basis just before the distribution is 50,000. In a current distribution the partner receives cash of 5,000 and equipment. The partnership's adjusted basis in the equipment is 12,000 and its fair value is 30,000. Share of liabilities unchanged.

Questions:
- **12a** The partner's basis in the equipment. (number)
- **12b** Outside basis after the distribution. (number)
- **12c** Gain recognized by the partner. (number)

## Case 13: Liquidating distribution with property

A partner's interest is liquidated. Outside basis just before the distribution is 60,000. The partner receives cash of 10,000; inventory with a partnership basis of 8,000 and fair value of 12,000; and land with a partnership basis of 20,000 and fair value of 50,000. The partner has no share of liabilities. Assume section 751(b) does not apply.

Questions:
- **13a** The partner's basis in the inventory. (number)
- **13b** The partner's basis in the land. (number)
- **13c** Gain or loss recognized (enter 0 if none). (number)

## Case 14: Liquidating distribution with a loss

A partner's interest is liquidated. Outside basis just before the distribution is 40,000. The partner receives only cash of 15,000 and inventory with a partnership basis of 9,000 and fair value of 11,000. The partner has no share of liabilities. Assume section 751(b) does not apply.

Questions:
- **14a** Loss recognized (enter as a positive number). (number)
- **14b** Character of the loss. Choices: capital, ordinary, none.
- **14c** The partner's basis in the inventory. (number)

## Case 15: Using a suspended loss

Beginning outside basis 0. Suspended ordinary loss from prior years 20,000. Share of liabilities unchanged.
This year the partner contributes cash of 5,000. K-1: ordinary income 12,000. No distributions.

Questions:
- **15a** Suspended loss allowed this year. (number)
- **15b** Loss still suspended at year end. (number)
- **15c** Ending outside basis. (number)

## Case 16: Basis limit and at-risk limit

Beginning outside basis 50,000. Of that, 40,000 is the partner's share of a nonrecourse equipment loan that is not qualified nonrecourse financing; the share is unchanged at year end. The other 10,000 came from cash the partner contributed. The partner has no other amounts at risk.
K-1: ordinary loss 30,000. No distributions.

Questions:
- **16a** Ordinary loss allowed under the basis limit. (number)
- **16b** Loss deductible after also applying the at-risk limit. (number)
- **16c** Ending outside basis. (number)

## Case 17: Sale of the interest

A partner sells her entire interest for cash of 70,000. Her outside basis at the sale date is 45,000, which includes her 15,000 share of partnership liabilities; the buyer takes over that share. Her share of the partnership's unrealized receivables is 10,000, with a zero basis. The partnership has no inventory.

Questions:
- **17a** Amount realized. (number)
- **17b** Total gain. (number)
- **17c** Ordinary income portion. (number)
- **17d** Capital gain portion. (number)

## Case 18: Partnership gives appreciated property to charity

Beginning outside basis 20,000. Share of liabilities unchanged. The only item this year: the partnership donated stock to a public charity. The partner's share of the stock's fair value is 10,000 and her share of the partnership's adjusted basis in it is 4,000.

Questions:
- **18a** Reduction in outside basis for the contribution. (number)
- **18b** Ending outside basis. (number)

## Case 19: Guaranteed payment

Beginning outside basis 10,000. Share of liabilities unchanged. The partner received a guaranteed payment for services of 30,000 during the year. K-1: guaranteed payment 30,000; ordinary income 6,000 (the partner's share after the partnership deducted the guaranteed payments); cash distributions 4,000, separate from the guaranteed payment.

Questions:
- **19a** Change in outside basis caused by the guaranteed payment itself. (number)
- **19b** Ending outside basis. (number)

## Case 20: Full deliverable

Prepare the complete outside basis package for this partner and save it as `deliverable.md`, following the skill's Output section. Also answer the questions below in `answers.json`.

Beginning outside basis 22,000 (including the beginning share of liabilities). K-1 item K: share of liabilities 18,000 at the beginning of the year and 10,000 at the end. Suspended ordinary loss from prior years 7,000.
During the year the partner contributed cash of 3,000.
K-1: ordinary loss 20,000; interest income 2,500; tax-exempt interest 500; section 179 deduction 5,000; nondeductible expenses 1,000; cash distributions 6,000. The partnership has no unrealized receivables or inventory.

Questions:
- **20a** Total money treated as distributed (cash plus liability decrease). (number)
- **20b** Gain recognized on distributions. (number)
- **20c** Basis available for losses and deductions. (number)
- **20d** Ordinary loss allowed (current year plus carryover). (number)
- **20e** Section 179 deduction allowed. (number)
- **20f** Total suspended and carried forward. (number)
- **20g** Ending outside basis. (number)
