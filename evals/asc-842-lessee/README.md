# Eval: asc-842-lessee

21 cases and 64 pass/fail checks covering classification, initial measurement, operating vs finance patterns, remeasurement, impairment, presentation, and one full client deliverable.

| File | What it is |
|---|---|
| [`cases.md`](cases.md) | The questions. The only file the blind test-taker sees besides the skill. |
| [`answer_key.json`](answer_key.json) | 64 checks with expected values and tolerances. Never shown to the test-taker. |
| [`compute_key.py`](compute_key.py) | Derives every numeric expected value from first principles. `--verify` compares them to the key. |
| [`grade.py`](grade.py) | Grades an `answers.json`: numbers within tolerance automatically, concepts flagged for a human read. |

## What the cases cover

| Area | Cases |
|---|---|
| Classification, including the last-25%-of-life rule and third-party RVGs | 1, 3, 4, 5, 9, 20 |
| Initial measurement: escalations, payments in advance, IDC, incentives, RVGs, purchase options, penalties | 1, 2, 4, 5, 11, 12, 13, 19, 21 |
| What stays out of the liability: CPI changes, percentage rent, variable utilities | 7, 8, 13 |
| Operating-lease pattern: ROU amortization as the plug | 1, 2, 18, 21 |
| Short-term exemption and lease term judgments | 6, 12, 19 |
| Remeasurement: modification, RVG change, resolved contingency, and which discount rate applies | 14, 15, 17 |
| Impairment of an operating ROU asset | 16 |
| Presentation: current portion, maturity table, cash flows | 3, 10, 21 |
| Full deliverable graded on structure | 21 |

## Run history

Each run gives a test-taker only the skill and `cases.md`, then grades its answers against the key.

| Date | Test-taker | Cases | Baseline | Edit tested | New score | Decision |
|---|---|---|---|---|---|---|
| 2026-11-09 | Haiku | 1–21 | 64/64 raw, counted 62/64 (a watch item repeated, which the rules count as two failures) | One line: which discount rate to use for each kind of remeasurement | 64/64, no regressions | Proposed, awaiting approval |
| 2026-11-03 | Haiku | 1–21 | 62/64: missed both Case 19 checks (lessor-controlled extension left out of the term) | One line in Inputs: lessor-controlled options are always in the term | 64/64, no regressions | Accepted |
| 2026-11-03 | Opus | 16–21 (hard round) | 25/25 | None needed | — | No edit |
| 2026-11-03 | Opus | 1–15 | 39/39 | None needed | — | No edit |

A **watch item** is a case the test-taker got right while saying the skill didn't cover it. One appearance is a note. Two runs in a row count as failures, because a right answer the skill didn't teach is luck that a smaller model may not repeat.

Open watch items from the last run: which RVG amount the 90% test uses (Case 4); incentives paid after commencement and termination penalties, which aren't in the skill's payment list (Cases 11 and 12); and fixed nonlease charges under the combine expedient (Case 13).

## Run it

```bash
python compute_key.py --verify      # 38/38 numeric values recomputed and matched
python grade.py --ids               # list check IDs
python grade.py answers.json        # grade a test-taker's answers
```
