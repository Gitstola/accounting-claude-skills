"""Grade a test-taker's answers.json against a suite's answer_key.json.
Usage: python grade.py <answer_key.json> <answers.json> [--quiet]"""
import json, sys

def norm(s):
    return " ".join(str(s).strip().lower().replace("_", " ").split())

def to_num(v):
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).replace(",", "").replace("$", "").replace("%", "").strip()
    if s.startswith("(") and s.endswith(")"):
        s = "-" + s[1:-1]
    return float(s)

def grade(key_path, ans_path):
    key = json.load(open(key_path))["checks"]
    ans = json.load(open(ans_path))
    rows = []
    for c in key:
        got = ans.get(c["id"], None)
        ok = False
        if got is not None:
            if c["type"] == "number":
                try:
                    ok = abs(to_num(got) - c["expected"]) <= c["tolerance"]
                except Exception:
                    ok = False
            else:
                ok = norm(got) == norm(c["expected"])
        rows.append((c["id"], c["case"], ok, c["expected"], got, c["check"]))
    return rows

if __name__ == "__main__":
    rows = grade(sys.argv[1], sys.argv[2])
    passed = sum(r[2] for r in rows)
    print(f"SCORE {passed}/{len(rows)}")
    for r in rows:
        if not r[2]:
            print(f"  FAIL {r[0]} (case {r[1]}): expected {r[3]!r}, got {r[4]!r} | {r[5]}")
