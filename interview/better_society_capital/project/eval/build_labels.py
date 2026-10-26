"""Merge labels into cases.jsonl with provenance.

Cases 1-4 come from the human (parsed from LABEL_ME.md, kept verbatim in label_user).
Cases 5-15 were labelled by Claude from the record text only (label_by = "claude").
Cases 1-3: the human's funding_type "social_investment" is overridden to "project" because
those are plain grants (the sheet defines social_investment as an investment or loan);
the original is kept in label_user and the change is recorded in label_note.
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
KEYS = ["theme", "beneficiary", "funding_type", "outcome_stated", "impact_case_score"]

CLAUDE = {  # id -> (theme, beneficiary, funding_type, outcome_stated, score)
    5: ("other", "unclear", "core_costs", False, 1),
    6: ("arts_culture", "ethnic_minority_communities", "core_costs", False, 2),
    7: ("community_places", "general_community", "project", True, 3),
    8: ("health_wellbeing", "people_in_poverty", "project", True, 4),
    9: ("other", "unclear", "core_costs", False, 1),
    10: ("energy_environment", "unclear", "project", False, 1),
    11: ("other", "organisations_sector", "project", False, 1),
    12: ("other", "children_young_people", "project", False, 2),
    13: ("community_places", "unclear", "other", False, 1),
    14: ("community_places", "unclear", "other", False, 1),
    15: ("other", "unclear", "project", False, 1),
}


def parse(line: str) -> dict:
    t, b, f, o, s = [p.strip() for p in line.split(":", 1)[1].split("|")]
    return dict(zip(KEYS, [t, b, f, o.lower() == "true", int(s)]))


user_lines = [l for l in (HERE / "LABEL_ME.md").read_text(encoding="utf-8").splitlines() if l.startswith("LABEL:")]
user = {i + 1: parse(l) for i, l in enumerate(user_lines) if "?" not in l}

cases = [json.loads(l) for l in open(HERE / "cases.jsonl", encoding="utf-8")]
for c in cases:
    i = c["id"]
    notes = []
    if i in user:
        c["label_user"] = user[i]
        c["label"] = dict(user[i])
        c["label_by"] = "user"
        if user[i]["funding_type"] == "social_investment" and i <= 3:
            c["label"]["funding_type"] = "project"
            notes.append("funding_type social_investment -> project (plain grant, not an investment/loan)")
        if i == 4:
            notes.append("user scored outcome_stated=true/4 but the text states no outcome; kept as the user labelled it")
    else:
        c["label"] = dict(zip(KEYS, CLAUDE[i]))
        c["label_by"] = "claude"
    c["label_note"] = "; ".join(notes)
with open(HERE / "cases.jsonl", "w", encoding="utf-8") as f:
    for c in cases:
        f.write(json.dumps(c, ensure_ascii=False) + "\n")
print({c["id"]: c["label_by"] for c in cases})
print("score dist:", sorted(c["label"]["impact_case_score"] for c in cases))
