---
name: "skill-improver"
description: "Use when running the Skill Lab loop or improving one of your skills from feedback (the weekly Skill Lab run, \"run the improver\", \"improve asc-842-lessee\"): turn feedback into tests, blind-test, and propose one proven edit."
---

# Skill improver (the Skill Lab loop)

Each run makes one skill measurably better, or changes nothing. An edit reaches the skill owner only after it beats the current skill on a blind test without breaking a case that used to pass.

## Where things live
Skill Lab doc: a shared doc with four tabs (How it works, Feedback log, Tests: <skill>, Run history). Put its link here. Read and write it with the Docs connector, following that connector's own instructions.
- **How it works:** the loop, and the "Skills in the loop" table of enrolled skills with their latest score.
- **Feedback log:** one row per correction. Status is New, Turned into test, or Rejected.
- **Tests: <skill>:** a Cases section the test-taker sees, then an Answer key it never sees.
- **Run history:** one row per run.

Work in a scratch folder in the working directory, e.g. `skilllab/<date>/`.

## Steps (per enrolled skill, or only the one named)
1. **Get the current skill.** Find its SKILL.md under the skills folder (`find / -name SKILL.md -path "*<skill-name>*" 2>/dev/null`) and copy it to `current/SKILL.md`. Never edit the original in place.
2. **Collect feedback.**
   - Feedback log rows for this skill with Status New.
   - Chat scan: if past-chat search tools are available, search the last 7 days for the skill's topic plus correction language ("wrong", "should be", "actually", "log it"). Count a correction only if the user stated the right answer. Add each as a Feedback log row with Source Chat scan. If the tools aren't available, note that in Run history and skip.
3. **Turn feedback into tests.** For each New row:
   - Verify the correction against the standard. Compute every number in Python.
   - If it holds, append a new Case to the Cases section (facts plus questions, written like the existing cases) and add its checks to the Answer key with expected values and tolerances. Set the row's Status to Turned into test.
   - If it's wrong, set Status to Rejected and give the reason in the row. Never change a skill to match a wrong correction.
   - Never delete or weaken an existing case or check. If an answer-key value proves wrong, fix it only after recomputing, and note the fix in Run history.
4. **Baseline (blind, on Haiku).** Copy only the Cases section to `cases.md`. Launch one subagent on the smallest model (`model: "haiku"`) with only the paths to `current/SKILL.md` and `cases.md`. Tell it to follow the skill as if a user invoked it, read nothing else, compute in Python, and write `answers.md`.
   - Why Haiku: a strong model fills a skill's gaps from its own knowledge and hides them. Haiku shows what the skill itself teaches, which keeps the skill reliable on any model.
   - Grade every Answer-key check pass or fail: amounts within tolerance, concepts by meaning.
   - Note any case the test-taker passed while saying the skill didn't cover it, or while doubting the skill. Record these as watch items in Run history.
   - If no subagent tool exists, answer `cases.md` yourself before reading the Answer key, and note the weaker isolation in Run history.
5. **Stop if nothing to fix.** If every check passes, log "No edit" with the score and any watch items, and stop. Don't invent edits.
6. **Diagnose.** Group the failed checks by root cause and pick the single cause behind the most failures. On a tie, take the one the user logged. A watch item that appeared in two straight runs counts as a failure.
7. **Draft one edit.** Make the smallest change to `current/SKILL.md` that fixes that cause, such as one rule line, a clarified step, or one example line, saved as `candidate/SKILL.md`.
   - Keep the frontmatter name and description, unless triggering is the cause.
   - Keep the existing structure and rules. Don't remove any rule.
   - Keep growth under about 10% of the skill's length.
8. **Re-test (blind).** Use a fresh Haiku subagent with `candidate/SKILL.md` and the same `cases.md`, and grade it. If the edit changes or removes existing text, rather than only adding to it, also re-test on the default model to check for regressions there.
9. **Accept or discard.** Accept only if total passes are strictly higher AND no check that passed at baseline now fails. Otherwise discard it. You may try one alternative edit, then stop.
10. **Propose.** If accepted, call `propose_skills` with kind "improvement", target = the skill's name, and the complete candidate SKILL.md, and state the before and after scores in your message. The review card is the owner's approval step. If `propose_skills` isn't available in this session, add a section "Pending edit: <skill>, <date>" at the end of the Run history tab with the full candidate SKILL.md in a code block, and say so.
11. **Log the run** as a new top row in Run history: Date, Skill, Model, Cases, Baseline, Edit tested (one line; put watch items here when there's no edit), New score, Regressions, Decision (Proposed, Discarded, or No edit). Update the skill's row in "Skills in the loop".
12. **Report** in three lines: scores, the edit and why, and what's waiting for approval.

## Enrolling another skill
Build a Tests tab for it with at least 15 cases whose expected answers are computed in code. Include cases at the skill's edges, and one full-deliverable case graded on structure. Run a baseline, then add the skill to "Skills in the loop".

## Guardrails
- The test-taker never sees the Answer key, the expected values, or earlier runs.
- One edit per run, and nothing changes without the owner's approval.
- A score that can't fail can't drive improvement. When a skill passes everything twice in a row, add harder edge cases before the next run.