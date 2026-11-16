# Tax skill pack: test results

Four tax skills, each tested blind on the smallest model (Haiku), which saw only the skill and the cases. Every expected answer is computed in code (`evals/<skill>/build_suite.py`).

| Skill | Cases | Checks | First blind run | After fixes |
|---|---|---|---|---|
| s-corp-basis | 19 | 72 | 72 / 72 | 72 / 72 |
| partnership-basis | 20 | 63 | 60 / 63 | 63 / 63 |
| form-1040-review | 21 | 56 | 56 / 56* | 56 / 56 |
| state-nexus | 22 | 49 | 49 / 49 | 49 / 49 |

*One answer key entry in this suite was itself wrong on the first run (the 2026 non-itemizer charitable deduction). An independent reviewer caught it; the key and the skill were corrected before the second run.

## What the testing changed
- **partnership-basis:** the rule for debt on contributed property let the test-taker count the partner's share twice (basis overstated by 15,000 in one case, gain understated by 16,000 in another). Rewritten with a worked number.
- **form-1040-review:** added the Social Security benefit formula, the premium-only rule for the overtime deduction, the custodial-parent rule, and the non-itemizer charitable deduction in the standard-vs-itemized comparison.
- **Independent review:** two reviewers recomputed all 82 cases and checked each rule against the Code, regulations and IRS instructions. Their findings are in `review/`.

## Run it yourself
```bash
python evals/s-corp-basis/build_suite.py        # rebuild cases.md and answer_key.json
python evals/grade.py evals/s-corp-basis/answer_key.json answers.json
```

State thresholds and yearly federal figures change. The skills tell the model to look them up, and the test cases state the figures they use.
