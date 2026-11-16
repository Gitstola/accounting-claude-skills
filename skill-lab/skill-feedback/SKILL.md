---
name: "skill-feedback"
description: "Use when the user says \"log it\", \"log that\", or flags that an answer from one of their skills was wrong: record the correction in the Skill Lab feedback log for the weekly improver."
---

# Skill feedback ("log it")

The Skill Lab loop only improves what gets logged. This skill writes one clean row per correction so the weekly improver can turn it into a permanent test case.

Skill Lab doc: the shared Skill Lab doc (tab **Feedback log**). Put its link here. Read and write it with the Docs connector, following that connector's own instructions.

## When to use
- The user says "log it", "log that", "add that to the log", or "that's wrong, log it" about an answer in the current chat.
- Only on an explicit flag. Don't log disagreements they didn't ask to record.

## Steps
1. **Identify the skill.** Use the skill that produced the answer in this chat. If no skill was loaded, use the skill that should have covered it (e.g., a lease question → asc-842-lessee). If it's genuinely unclear, ask one short question.
2. **Get the correct answer.** Use what they said. If they flagged an error without saying what's right, ask for it in one line. Never invent the correction. If their correction conflicts with the standard, say so plainly, and log it anyway with your note in the same cell; the improver will verify it.
3. **Write the row** at the end of the Feedback log table:
   - **Date:** today (YYYY-MM-DD).
   - **Skill:** the skill's name.
   - **What went wrong:** one or two sentences with the facts needed to rebuild the case (amounts, term, rate, timing) and the wrong number or rule. Example: "3-yr lease, $10,000/yr arrears, 5%, lessor-held 2-yr extension: treated the term as 3 years; liability 27,232.48."
   - **Correct answer or rule:** the right number or rule. Example: "Lessor-controlled extensions are in the lease term: 5 years, liability 43,294.77."
   - **Source:** Logged.
   - **Status:** New.
   If the table still holds the "No feedback logged yet" placeholder row, replace that row instead of appending.
4. **Keep client data out.** No client names, entity names, or account numbers; describe the facts generically.
5. **Confirm in one line:** "Logged for <skill>: <what was wrong>. The weekly run will turn it into a test."

If the Docs connector isn't available, give them the row as text and say it wasn't written.