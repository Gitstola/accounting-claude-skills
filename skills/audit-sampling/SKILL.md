---
name: "audit-sampling"
description: "Use when designing, selecting, or evaluating audit samples (AU-C 530 / AS 2315): attribute sampling for controls, monetary unit sampling, classical variables, nonstatistical samples, projecting misstatement, and upper limits."
---

# Audit Sampling (AU-C 530 / AS 2315)

## Modes
- **Design**: set the sample size and selection method.
- **Evaluate**: project results and reach a conclusion.
- **Explain/FAR-AUD**: when the user says "quiz me", pose a sampling problem and grade the answer.

## Inputs (list what's missing)
- Objective: a test of controls or a substantive test.
- Population: book value, item count, and evidence that it is complete.
- Sampling unit.
- Tolerable rate or tolerable misstatement.
- Expected deviation rate or expected misstatement.
- Risk level (confidence).
- Results: deviations found, or book value vs. audited value for each misstated item.

## Calculation rule
Compute sample sizes and upper limits in code. Use the binomial or Poisson distribution, or AICPA tables. Show the factors used. Never estimate an upper limit by eye.

## Step 0 — Population and selection
- Reconcile the population to the GL first.
- Define what counts as a deviation or a misstatement BEFORE testing.
- Selection methods:
  - Random, or systematic with a random start.
  - Haphazard selection is for nonstatistical samples only.
  - Block selection is not appropriate for projecting results.
- Sampling risk:
  - Incorrect acceptance or overreliance hurts effectiveness. This is the dangerous one.
  - Incorrect rejection or underreliance hurts efficiency.
- Nonsampling risk (wrong procedure, missed deviations) is controlled through quality, not sample size.

## A. Attribute sampling (tests of controls)
- **Sample size** rises as the risk of overreliance falls, as the expected rate rises, or as the tolerable rate falls. Population size barely matters for large populations.
- **Evaluation:**
  - Sample deviation rate = deviations ÷ n.
  - Upper deviation limit (UDL) comes from the binomial at the chosen confidence.
  - If UDL ≤ tolerable rate, the control can be relied on as planned.
  - If UDL > tolerable rate, reduce reliance and expand substantive work.
- Evaluate every deviation qualitatively: error or fraud, and its cause.

## B. Monetary unit sampling (MUS / PPS, substantive)
**Design**
- Sample size n = (Book value × reliability factor) ÷ (Tolerable misstatement − Expected misstatement × expansion factor).
- At 95% confidence: reliability factor (0 errors) = 3.0 and expansion factor = 1.6.
- Sampling interval = Book value ÷ n.
- Items at or above the interval are selected with certainty (the top stratum).
- MUS works best for overstatement. It is weak for understatements and cannot select zero-balance items.

**Evaluation**
- Tainting % = (book value − audited value) ÷ book value.
- Projected misstatement:
  - Items below the interval: tainting % × interval.
  - Top-stratum items: the actual misstatement.
- Basic precision = reliability factor (0 errors) × interval.
- Incremental allowance:
  - Rank the projected misstatements of items below the interval by tainting, largest first.
  - Multiply each by its incremental factor. At 95%, the factors are 0.75, 0.55, and 0.46 for the 1st, 2nd, and 3rd items.
- Upper misstatement limit (UML) = projected misstatement + basic precision + incremental allowance.
- If UML ≤ tolerable misstatement, accept. Otherwise, propose an adjustment or expand the test.

## C. Classical variables and nonstatistical sampling
- Classical variables sampling uses mean-per-unit, difference, or ratio estimation. It handles understatements and zero balances, but it needs a measure of variability.
- Nonstatistical samples still require projecting misstatement to the population, using the ratio or difference method. Compare the projection to tolerable misstatement, with judgment about the allowance for sampling risk.

## Output
1. Design memo: objective, population, sampling unit, parameters, sample size, selection method.
2. Results table.
3. Projection and upper limit calculation.
4. Conclusion: accept, reject, or expand.
5. Qualitative evaluation.
6. Flags.

## Worked examples
**Attribute sampling**
- Tolerable rate 6%, expected rate 1%, 5% risk of overreliance: n = 78 (AICPA table, or binomial in code).
- With 0 deviations, the UDL is about 3.8%, which is at or below 6%. Rely on the control as planned.

**MUS**
- Accounts receivable book value 1,000,000. Tolerable misstatement 50,000. Expected misstatement 10,000. 95% confidence.
- n = 1,000,000 × 3.0 ÷ (50,000 − 16,000) = 88.2, rounded up to **89**.
- Interval = 1,000,000 ÷ 89 = 11,236.
- Misstatements found:
  - Item with book value 5,000, audited at 4,000. Tainting is 20%, so the projection is 0.20 × 11,236 = 2,247.
  - Item with book value 15,000, which is in the top stratum, audited at 14,000. The actual misstatement of 1,000 is used.
- Projected misstatement = 2,247 + 1,000 = 3,247.
- Basic precision = 3.0 × 11,236 = 33,708.
- Incremental allowance = 0.75 × 2,247 = 1,685. The top-stratum item gets no allowance.
- UML = 3,247 + 33,708 + 1,685 = **38,640**. That is at or below 50,000, so **accept**.

## Boundaries
Tolerable amounts, risk levels, and the evaluation of qualitative factors are judgments for the engagement team. Follow the firm's methodology and tables where they differ from these defaults.