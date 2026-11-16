# Test cases: s-corp-basis

Each case is one S corporation shareholder for one tax year. Amounts are in dollars.

## How to answer
Write your answers to `answers.json` as one JSON object that maps each question ID to its answer.
- Number questions: a plain number, no commas or currency signs. Percentages as a number, for example 23.75 for 23.75%.
- Choice questions: exactly one of the listed choices, spelled as shown.
Answer every ID. Do the arithmetic in Python.

## Case 1: Ordering with no limits

Sole shareholder. Beginning stock basis 50,000. No shareholder loans. The corporation has never been a C corporation.
K-1 for the year: ordinary income 20,000; tax-exempt interest 3,000; nondeductible expenses 2,000; section 179 deduction 6,000; distributions 15,000.

Questions:
- **1a** Taxable amount of the distribution. (number)
- **1b** Ending stock basis. (number)
- **1c** Is Form 7203 required this year? Choices: yes, no.

## Case 2: Distribution above stock basis

Beginning stock basis 8,000. No shareholder loans. No accumulated E&P. Stock held for 3 years.
K-1: ordinary income 5,000; distributions 20,000.

Questions:
- **2a** Gain recognized on the distribution. (number)
- **2b** Character of that gain. Choices: long-term capital gain, short-term capital gain, ordinary income, dividend, not taxable.
- **2c** Ending stock basis. (number)

## Case 3: Loss limited by stock basis

Beginning stock basis 12,000. No shareholder loans. K-1: ordinary loss 30,000. No distributions.

Questions:
- **3a** Ordinary loss allowed this year under the basis limit. (number)
- **3b** Loss suspended and carried forward. (number)
- **3c** Ending stock basis. (number)

## Case 4: Several loss items exceed basis

Beginning stock basis 20,000. No shareholder loans. No accumulated E&P.
K-1: ordinary loss 30,000; charitable contributions 6,000; net section 1231 loss 4,000; nondeductible expenses 1,000; distributions 4,000.

Questions:
- **4a** Stock basis available for losses and deductions (after distributions and nondeductible expenses). (number)
- **4b** Ordinary loss allowed. (number)
- **4c** Charitable contributions allowed. (number)
- **4d** Section 1231 loss allowed. (number)
- **4e** Total suspended and carried forward. (number)
- **4f** Ending stock basis. (number)

## Case 5: Nondeductible expenses exceed basis (no election)

Beginning stock basis 3,000. No shareholder loans. No election to change the ordering.
K-1: nondeductible expenses 5,000; ordinary loss 10,000. No income and no distributions.

Questions:
- **5a** Ordinary loss allowed this year. (number)
- **5b** Ordinary loss suspended. (number)
- **5c** Nondeductible expenses carried forward to next year. (number)

## Case 6: Same facts with the ordering election

Same facts as Case 5, except the shareholder has a valid election under Reg. 1.1367-1(g) in place.

Questions:
- **6a** Ordinary loss allowed this year. (number)
- **6b** Ordinary loss suspended. (number)
- **6c** Nondeductible expenses carried forward to next year. (number)

## Case 7: Loss absorbed by debt basis

Beginning stock basis 15,000. The shareholder lent the corporation 40,000 on a written note; debt basis is 40,000.
K-1: ordinary loss 45,000; distributions 5,000. No accumulated E&P. No repayments on the note.

Questions:
- **7a** Ordinary loss allowed this year. (number)
- **7b** Ending stock basis. (number)
- **7c** Ending debt basis. (number)
- **7d** Taxable amount of the distribution. (number)

## Case 8: Guaranteed bank loan

Beginning stock basis 10,000. The shareholder has made no loans to the corporation, but personally guaranteed the corporation's 100,000 bank loan. The shareholder has paid nothing under the guarantee.
K-1: ordinary loss 60,000.

Questions:
- **8a** Debt basis created by the guarantee. (number)
- **8b** Ordinary loss allowed this year. (number)
- **8c** Loss suspended. (number)

## Case 9: Distribution when only debt basis remains

Beginning stock basis 2,000. Debt basis 50,000 on a 50,000 written note. No accumulated E&P. Stock held 6 years.
K-1: no income or loss items; distributions 12,000.

Questions:
- **9a** Gain recognized on the distribution. (number)
- **9b** Ending stock basis. (number)
- **9c** Ending debt basis. (number)

## Case 10: Restoring reduced debt basis

Beginning stock basis 0. One written note with a face amount of 30,000; prior losses reduced its basis to 18,000. No suspended losses.
K-1: ordinary income 25,000; distributions 9,000. No repayments on the note. No accumulated E&P.

Questions:
- **10a** Taxable amount of the distribution. (number)
- **10b** Net increase for the year. (number)
- **10c** Debt basis restored this year. (number)
- **10d** Ending debt basis. (number)
- **10e** Ending stock basis. (number)

## Case 11: Using a suspended loss

Beginning stock basis 0. One written note, face 20,000, with basis already reduced to 0. Suspended ordinary loss from prior years 14,000.
K-1 this year: ordinary income 10,000. No distributions and no repayments.

Questions:
- **11a** Suspended loss allowed this year. (number)
- **11b** Loss still suspended at year end. (number)
- **11c** Ending stock basis. (number)
- **11d** Ending debt basis. (number)

## Case 12: Repayment on a reduced-basis note

Written note, face 30,000, held 4 years. Debt basis at the start of the year 12,000. Stock basis 0.
The corporation breaks even: no income, loss, or distribution items. It repays 10,000 of principal on the note.

Questions:
- **12a** Nontaxable part of the repayment. (number)
- **12b** Gain recognized. (number)
- **12c** Character of the gain. Choices: long-term capital gain, short-term capital gain, ordinary income, dividend, not taxable.
- **12d** Ending debt basis. (number)

## Case 13: Restoration applies before a repayment

Beginning stock basis 0. One written note, face 40,000, held 5 years, with basis reduced to 10,000. No suspended losses.
K-1: ordinary income 20,000; no distributions. In July the corporation repays the note in full, 40,000.

Questions:
- **13a** Debt basis immediately before the repayment. (number)
- **13b** Gain recognized on the repayment. (number)
- **13c** Ending stock basis. (number)

## Case 14: Open account repayment

The shareholder's advances are an open account with no written note. Balance at the start of the year 20,000 (it was 20,000 at the end of last year too); debt basis 5,000. Stock basis 0.
No income, loss, or distribution items this year. Net repayments on the account for the year are 8,000.

Questions:
- **14a** Gain recognized on the net repayment. (number)
- **14b** Character of the gain. Choices: long-term capital gain, short-term capital gain, ordinary income, dividend, not taxable.
- **14c** Ending debt basis. (number)

## Case 15: Distribution with accumulated E&P

The corporation was a C corporation years ago. Sole shareholder; beginning stock basis 30,000.
Beginning AAA 12,000. Accumulated E&P 20,000.
K-1: ordinary income 8,000; distributions 35,000. No other items.

Questions:
- **15a** Amount of the distribution treated as a taxable dividend. (number)
- **15b** Amount of the distribution that is a tax-free return of basis. (number)
- **15c** Ending stock basis. (number)
- **15d** Ending AAA. (number)
- **15e** Ending accumulated E&P. (number)

## Case 16: AAA in a net loss year

Former C corporation. Sole shareholder; beginning stock basis 40,000.
Beginning AAA 10,000. Accumulated E&P 6,000.
K-1: ordinary loss 7,000; distributions 12,000. No other items.

Questions:
- **16a** Amount of the distribution treated as a taxable dividend. (number)
- **16b** Ending AAA. (number)
- **16c** Ordinary loss allowed. (number)
- **16d** Ending stock basis. (number)

## Case 17: Sale of all stock with suspended losses

Stock basis 0. Suspended ordinary losses from prior years 22,000. No shareholder loans.
On January 2 the shareholder sells all of the stock to an unrelated buyer for 50,000. Stock held 8 years. No K-1 items are allocated to the seller for the year.

Questions:
- **17a** Gain on the sale. (number)
- **17b** Suspended loss the seller can deduct because of the sale. (number)
- **17c** Is Form 7203 required this year? Choices: yes, no.

## Case 18: Income only

Beginning stock basis 25,000. No shareholder loans. K-1: ordinary income 9,000 and nothing else. No distributions, no loan activity, no stock sold, and no losses claimed.

Questions:
- **18a** Ending stock basis. (number)
- **18b** Is Form 7203 required this year? Choices: yes, no.

## Case 19: Full deliverable

Prepare the complete basis package for this shareholder and save it as `deliverable.md`, following the skill's Output section. Also answer the questions below in `answers.json`.

Beginning stock basis 6,000. One written note, face 25,000, debt basis 25,000. Suspended ordinary loss from prior years 5,000. No accumulated E&P. No election to change the ordering.
During the year the shareholder contributed 4,000 of additional capital. No repayments on the note.
K-1: ordinary loss 36,000; interest income 3,000; tax-exempt interest 1,000; charitable contributions 4,000; nondeductible expenses 2,000; distributions 5,000.

Questions:
- **19a** Stock basis before distributions. (number)
- **19b** Taxable amount of the distribution. (number)
- **19c** Total losses and deductions allowed. (number)
- **19d** Ordinary loss allowed (current year plus carryover). (number)
- **19e** Charitable contributions allowed. (number)
- **19f** Total suspended and carried forward. (number)
- **19g** Ending stock basis. (number)
- **19h** Ending debt basis. (number)
