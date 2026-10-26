# 360Giving MCP server + impact-screen skill + tiny eval

A weekend learning build, not production software. It has three parts:

1. **`server.py`**: an MCP server (official Python SDK, stdio) over a local SQLite copy of UK grants data from the [360Giving registry](https://registry.threesixtygiving.org/). Five funders, 20,867 grants: Esmée Fairbairn, Power to Change, Lloyds Bank Foundation, Barrow Cadbury, Nesta. Three narrow, read-only tools: `search_grants`, `get_funder_summary`, `get_recipient`.
2. **`skills/impact_screen/`**: a first-pass impact-screen skill (v1 and v2) that turns one grant record into structured JSON with evidence quotes. Always a draft for a human.
3. **`eval/`**: 15 labelled cases, a runner, and results for v1 and v2.

## Run it
```
pip install -r requirements.txt
python fetch_data.py                 # builds data/grants.sqlite
python smoke_test.py                 # starts the server over stdio and calls each tool
claude mcp add grants-360giving -- python /abs/path/server.py
cp .env.example .env                 # add NVIDIA_API_KEY
python eval/run_eval.py --skill skills/impact_screen/SKILL_v1.md --tag v1
python eval/run_eval.py --skill skills/impact_screen/SKILL.md --tag v2
```

## Eval results (n = 15, one run each, temperature 0)
The skill runs on `nvidia/nemotron-3-ultra-550b-a55b`; groundedness is judged by a different model, `minimaxai/minimax-m3.1-flash`. Both are on NVIDIA NIM's free tier.

| Metric | v1 | v2 |
|---|---|---|
| Valid JSON | 15/15 | 14/15 |
| Theme / beneficiary / funding type match | 67 / 73 / 73% | 71 / 79 / 79% |
| outcome_stated match | 87% | 93% |
| Score exact / within ±1 / MAE | 60 / 87% / 0.60 | 71 / 93% / 0.43 |
| Evidence quotes verbatim in the record | 100% | 100% |
| Judge: clean outputs judged grounded | 9/11 | 9/10 |
| Judge: planted fabrications caught | 4/4 | 4/4 |

Percentages for v2 are over the 14 valid outputs. **v2 changed the prompt once** (full list in `SKILL.md`): defined score levels 2 and 4, a tie-break for `outcome_stated`, "recipient name is not evidence", "write outcomes as intentions, not results".

### How much to trust this
- **n = 15 is tiny.** One case is about 7 points. v1 moved by a case or two between two runs, so differences between v1 and v2 are within noise. Read the table as "v2 is not worse and is probably a little better", not as a proven gain.
- **The labels are not all mine.** Cases 1 to 4 were labelled by the human; cases 5 to 15 were labelled by Claude from the record text only (`label_by` in `cases.jsonl`). For cases 1 to 3 the human's `funding_type` of `social_investment` was changed to `project` (plain grants) and the original is kept in `label_user`. Case 4's label looks like it used knowledge from outside the text and was left as given. An independent human assessor would be the first thing to add.
- **The judge is a different small model, checked in one way only:** it caught all 4 planted fabrications in both runs and flagged 2 of 11 (v1) and 1 of 10 (v2) clean outputs. I read those flags for #1 and #2 in v1: they were about intended versus achieved outcomes, which is a fair catch of loose wording. This does not show the judge is reliable in general.
- **The data is thin by design.** Most records are one line, so most correct answers are "unclear" and a score of 1. That makes the task partly about not inventing detail, which the skill does well (quotes are verbatim and nothing was fabricated), and gives little room to see subtler quality differences.
- **One v2 case never produced valid JSON** after 3 tries (#2), which counts against v2.

## What I learned
- The prompt and the labels matter more than the model. Clear score anchors fixed more than anything else.
- Return caps and narrow tools keep MCP results small and the model on task; the grant text itself is untrusted input (prompt-injection risk), so descriptions are truncated and labelled as data.
- Free-tier model APIs rate-limit and sometimes truncate output: validate, retry, and report the retries.
- The 360Giving registry moved; GrantNav and the old registry sit behind a browser check. Use `registry.threesixtygiving.org/data.json` and the funders' own file links.

## Next
- A second human rater and more cases, then report agreement between raters as the ceiling for the model.
- A permission-aware version for internal data (delegated auth, per-user access) instead of open data.
- Regression-test every prompt change against the whole set before shipping it.
