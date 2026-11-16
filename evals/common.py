"""Shared helpers: turn a list of cases into cases.md (what the test-taker sees)
and answer_key.json (what it never sees). Every expected number is computed in
the build script that calls this, not typed in."""
import json
from pathlib import Path


def q(qid, prompt, expected, tol=1.0, choices=None):
    """One graded question. Numbers are graded within `tol`; choices by exact match."""
    if choices:
        assert expected in choices, (qid, expected, choices)
        return dict(id=qid, prompt=prompt, type="choice", expected=expected, choices=choices)
    return dict(id=qid, prompt=prompt, type="number", expected=round(float(expected), 2), tol=tol)


def write_suite(here, skill, intro, cases):
    here = Path(here)
    md = [f"# Test cases: {skill}", "", intro, "",
          "## How to answer",
          "Write your answers to `answers.json` as one JSON object that maps each question ID to its answer.",
          "- Number questions: a plain number, no commas or currency signs. Percentages as a number, for example 23.75 for 23.75%.",
          "- Choice questions: exactly one of the listed choices, spelled as shown.",
          "Answer every ID. Do the arithmetic in Python.", ""]
    key = []
    for c in cases:
        md += [f"## Case {c['n']}: {c['title']}", "", c["facts"].strip(), "", "Questions:"]
        for item in c["questions"]:
            if item["type"] == "choice":
                md.append(f"- **{item['id']}** {item['prompt']} Choices: {', '.join(item['choices'])}.")
                key.append(dict(id=item["id"], case=c["n"], check=item["prompt"], type="choice",
                                expected=item["expected"]))
            else:
                md.append(f"- **{item['id']}** {item['prompt']} (number)")
                key.append(dict(id=item["id"], case=c["n"], check=item["prompt"], type="number",
                                expected=item["expected"], tolerance=item["tol"]))
        md.append("")
    (here / "cases.md").write_text("\n".join(md))
    (here / "answer_key.json").write_text(json.dumps(dict(skill=skill, checks=key), indent=2))
    ids = [k["id"] for k in key]
    assert len(ids) == len(set(ids)), "duplicate question id"
    print(f"{skill}: {len(cases)} cases, {len(key)} checks")
