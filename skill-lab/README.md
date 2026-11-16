# Skill Lab

A weekly loop that makes one skill measurably better, or changes nothing. Corrections become permanent tests. A separate agent takes the full test blind, and an edit reaches the owner only after it beats the current skill without breaking a case that used to pass.

| Skill | Job |
|---|---|
| [`skill-feedback`](skill-feedback/SKILL.md) | When the user says "log it" about a wrong answer, write one clean row to the feedback log: the facts, the wrong number or rule, and the right one. |
| [`skill-improver`](skill-improver/SKILL.md) | The weekly run: turn new feedback into test cases, take a blind baseline, diagnose, draft one edit, re-test, and propose it only if it wins. |

## The run, step by step

1. **Collect feedback.** New rows from the log, plus a scan of the last week's chats for corrections the user stated but didn't log.
2. **Turn feedback into tests.** Verify each correction against the standard, with every number computed in Python. A correction that is wrong gets rejected with a reason. The skill never changes to match a wrong correction.
3. **Blind baseline on the smallest model.** A subagent on Haiku gets only the skill and the cases, never the answer key. A strong model fills a skill's gaps from its own knowledge and hides them; a small one shows what the skill actually teaches.
4. **Stop if nothing failed.** No invented edits.
5. **Diagnose.** Group the failures by root cause and take the one behind the most failures.
6. **Draft one edit**: the smallest change that fixes that cause, with no rules removed and growth kept under about 10%.
7. **Re-test blind** with a fresh subagent and the same cases.
8. **Accept only on a strict win**: total passes go up, and no check that passed before now fails.
9. **Propose** the full updated skill to the owner as a review card. Nothing changes without approval.

## Guardrails

- The test-taker never sees the answer key, the expected values, or earlier runs.
- One edit per run, so every change is easy to review and easy to roll back.
- Existing cases are never deleted or weakened. A wrong answer-key value is fixed only after recomputing it, and the fix is logged.
- A score that can't fail can't drive improvement. After two perfect runs in a row, harder edge cases get added.

## Results so far

See the [asc-842-lessee eval](../evals/asc-842-lessee/README.md): a blind Haiku baseline of 62/64 rose to 64/64 after one accepted edit, with no regressions. A second edit is proposed and awaiting approval.
