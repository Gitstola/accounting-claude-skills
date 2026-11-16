"""Grade a test-taker's answers against the asc-842-lessee answer key.

answers.json maps check IDs to answers, e.g. {"1.1": "Operating", "1.2": 50548.37, ...}.
Check IDs are "<case>.<n>", numbered in answer_key.json order within each case
(run `python grade.py --ids` to list them).

Numeric checks are graded automatically within tolerance. Concept checks pass on an exact
(case-insensitive) match and are otherwise listed for a human to grade by meaning.

Usage:  python grade.py answers.json
        python grade.py --ids
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
KEY = json.loads((HERE / "answer_key.json").read_text())


def with_ids(checks):
    counter = defaultdict(int)
    out = []
    for row in checks:
        counter[row["case"]] += 1
        out.append({**row, "id": f"{row['case']}.{counter[row['case']]}"})
    return out


CHECKS = with_ids(KEY["checks"])


def to_number(x):
    if isinstance(x, (int, float)):
        return float(x)
    try:
        return float(str(x).replace(",", "").replace("$", "").replace("+", "").strip())
    except ValueError:
        return None


def grade(answers):
    passed, failed, manual = [], [], []
    for row in CHECKS:
        got = answers.get(row["id"])
        exp = row["expected"]
        if got is None:
            failed.append((row, "no answer"))
        elif isinstance(exp, (int, float)):
            n = to_number(got)
            if n is not None and abs(n - exp) <= row["tolerance"]:
                passed.append(row)
            else:
                failed.append((row, f"got {got}, expected {exp:,.2f} ± {row['tolerance']}"))
        elif str(got).strip().lower() == str(exp).strip().lower():
            passed.append(row)
        else:
            manual.append((row, got))
    return passed, failed, manual


def main():
    if "--ids" in sys.argv:
        for row in CHECKS:
            print(f"{row['id']:6s} {row['check']}")
        return
    answers = json.loads(Path(sys.argv[1]).read_text())
    passed, failed, manual = grade(answers)
    for row, why in failed:
        print(f"FAIL   {row['id']:6s} {row['check']}: {why}")
    for row, got in manual:
        print(f"REVIEW {row['id']:6s} {row['check']}: answer {got!r} vs expected {row['expected']!r}")
    print(f"\nAuto-graded: {len(passed)} passed, {len(failed)} failed, {len(manual)} need a human read "
          f"(of {len(CHECKS)} checks).")


if __name__ == "__main__":
    main()
