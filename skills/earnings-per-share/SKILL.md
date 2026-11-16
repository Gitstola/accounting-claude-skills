---
name: "earnings-per-share"
description: "Use when computing or reviewing basic and diluted EPS (ASC 260): weighted-average shares, preferred dividends, stock splits/dividends, treasury stock method, if-converted method, contingent shares, and antidilution sequencing."
---

# Earnings Per Share — ASC 260

## Modes
- **Compute**: work out basic and diluted EPS from the user's numbers.
- **Review**: check an existing EPS calculation.
- **Explain/FAR**: when the user says "quiz me", pose a problem and grade each step.

## Inputs (list what's missing)
- Net income, split between continuing operations and discontinued operations. Use the amount attributable to the parent if there is a noncontrolling interest.
- Preferred stock terms: cumulative or not, and the dividend amount.
- Common share activity with dates: issuances, buybacks, splits, stock dividends.
- Options and warrants: number, exercise price, average market price for the period.
- Convertible debt: interest, tax rate, conversion shares, issue date.
- Convertible preferred: dividends and conversion shares.
- Contingent share arrangements.

## Calculation rule
Compute in code when a tool is available. Show the weighted-average share table and the incremental per-share figure for every potential common share.

## Step 1: Numerator for basic EPS
Income available to common = Net income − preferred dividends.
- Cumulative preferred: subtract the current year's dividend whether or not it was declared.
- Noncumulative preferred: subtract only if declared.
- Never subtract dividends in arrears from prior years.

## Step 2: Weighted-average shares (WASO)
- Weight each issuance and buyback by the fraction of the period the shares were outstanding.
- Stock splits and stock dividends apply retroactively to the start of the period and to all prior periods presented. This includes splits and stock dividends that occur after year-end but before the statements are issued.
- Shares issued in a business combination are weighted from the acquisition date.
- Contingently issuable shares count in basic EPS only once all conditions have been met.

## Step 3: Diluted EPS
**Options and warrants (treasury stock method)**
- Incremental shares = shares under option − (exercise proceeds ÷ average market price).
- Proceeds include unrecognized compensation cost for unvested awards.
- An option is dilutive only if it is in the money, meaning the average price exceeds the exercise price.

**Convertible debt (if-converted method)**
- Add back interest, net of tax, to the numerator.
- Add the conversion shares to the denominator, weighted from the issue date if the debt was issued during the period.

**Convertible preferred (if-converted method)**
- Add back the preferred dividends to the numerator.
- Add the conversion shares to the denominator.

**Other rules**
- Under ASU 2020-06, the if-converted method is required for convertibles. Instruments that can be settled in cash or shares are presumed to settle in shares.
- Contingent shares are included if the conditions would be met if the end of the period were the end of the contingency period.

## Step 4: Antidilution sequencing
1. Compute each security's incremental EPS: numerator effect divided by incremental shares. Options have a numerator effect of zero, so they come first.
2. Rank securities from the lowest incremental EPS (most dilutive) to the highest.
3. Add them one at a time. Skip any security whose incremental EPS is higher than the running diluted EPS, because it would increase EPS.
4. The **control number** is income from continuing operations. If it is a loss, every potential share is antidilutive and diluted EPS equals basic EPS, even if net income is positive.

## Presentation
- Public entities present basic and diluted EPS on the face of the income statement, for both continuing operations and net income.
- Discontinued operations per share may be shown on the face or in the notes.
- Nonpublic entities are not required to present EPS.

## Tie-outs
- Diluted EPS must be less than or equal to basic EPS. If it isn't, the sequencing is wrong.
- The WASO table must match the share roll-forward.
- Splits must be applied to every period presented.

## Output
1. WASO table.
2. Basic EPS.
3. Table of potential common shares, with incremental EPS and rank.
4. Sequential dilution build.
5. Diluted EPS.
6. Flags.

## Worked example
**Facts**
- Net income: 1,000,000.
- Cumulative preferred dividend of 100,000, undeclared but still subtracted.
- 400,000 shares outstanding at 1/1, plus 120,000 issued on 7/1.
- 50,000 options at $20 exercise price; average market price $25.
- Convertible bonds: interest of 80,000, tax rate 21%, convertible into 40,000 shares.

**Basic EPS**
- WASO = 400,000 + 120,000 × 6/12 = 460,000.
- Basic EPS = 900,000 ÷ 460,000 = **1.96**.

**Options**
- Proceeds = 50,000 × $20 = 1,000,000.
- Shares repurchased = 1,000,000 ÷ $25 = 40,000.
- Incremental shares = 10,000, with incremental EPS of 0.
- Running EPS: 900,000 ÷ 470,000 = 1.915.

**Bonds**
- Interest net of tax = 80,000 × (1 − 0.21) = 63,200.
- Incremental EPS = 63,200 ÷ 40,000 = 1.58. That is below 1.915, so the bonds are dilutive.

**Diluted EPS** = 963,200 ÷ 510,000 = **1.89**.

## Boundaries
Treat the result as review-ready work. Flag complex instruments, such as participating securities under the two-class method, for technical review.