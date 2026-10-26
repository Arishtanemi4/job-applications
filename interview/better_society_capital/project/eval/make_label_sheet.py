"""Write LABEL_ME.md from cases.jsonl: a sheet for the human assessor to fill in blind."""
import json
from pathlib import Path

HERE = Path(__file__).parent
cases = [json.loads(l) for l in open(HERE / "cases.jsonl", encoding="utf-8")]
out = ["""# Label these 15 grants (blind: don't run the skill first)

Edit each `LABEL:` line: `theme | beneficiary | funding_type | outcome_stated | score`

- theme: housing, health_wellbeing, employment_skills, energy_environment, arts_culture, community_places, criminal_justice, youth_education, poverty_finance, other
- beneficiary: children_young_people, older_people, people_in_poverty, disabled_people, ethnic_minority_communities, general_community, organisations_sector, unclear
- funding_type: core_costs, project, social_investment, other
- outcome_stated: true only if the record states an intended change for people/places, not just an activity
- score 1-5: how clearly the RECORD supports an impact case (1 nothing stated; 3 beneficiary+activity clear, outcome vague; 5 beneficiary, outcome and scale clear)
- Judge only from the text shown. If the text says nothing, that is a 1.
"""]
for c in cases:
    out.append(f"## #{c['id']}  {c['funder']}  £{c['amount']:,.0f}  {c['award_date']}\n"
               f"**Recipient:** {c['recipient']}\n**Title:** {c['title']}\n**Description:** {c['description']}\n\n"
               f"LABEL: ? | ? | ? | ? | ?\n")
(HERE / "LABEL_ME.md").write_text("\n".join(out), encoding="utf-8")
print("ok", len(cases))
