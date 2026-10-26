"""Run the impact-screen skill over eval/cases.jsonl and score it.

  python eval/run_eval.py --skill skills/impact_screen/SKILL_v1.md --tag v1

Scores:
  * exact match per field (theme, beneficiary, funding_type, outcome_stated)
  * impact_case_score: exact, within +/-1, mean absolute error
  * evidence quotes that are verbatim in the record (deterministic)
  * groundedness judged by a DIFFERENT model than the one that ran the skill
  * judge sanity check: the judge must catch planted fabrications and not flag clean outputs
Writes eval/results/<tag>.json and prints a summary.
"""
import argparse
import json
import os
import random
import re
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI, RateLimitError

HERE = Path(__file__).parent
ROOT = HERE.parent
load_dotenv(ROOT / ".env")

FIELDS = ["theme", "beneficiary", "funding_type", "outcome_stated"]
client = OpenAI(base_url="https://integrate.api.nvidia.com/v1", api_key=os.environ["NVIDIA_API_KEY"], timeout=180, max_retries=1)


# Listed-but-404 on this account: nemotron-3-super, kimi-k2.6, mistral-large. These two answered in a probe.
SKILL_MODEL = "nvidia/nemotron-3-ultra-550b-a55b"
JUDGE_MODEL = "minimaxai/minimax-m3.1-flash"


def chat(model: str, system: str, user: str, max_tokens: int = 1500) -> str:
    for attempt in range(6):  # NIM's free tier rate-limits (429): back off and retry
        try:
            r = client.chat.completions.create(
                model=model,
                messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
                temperature=0,
                max_tokens=max_tokens,
            )
            return r.choices[0].message.content or ""
        except RateLimitError:
            time.sleep(5 * 2**attempt)
    raise RuntimeError(f"{model}: still rate-limited after retries")


def parse_json(text: str) -> dict | None:
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.S)
    m = re.search(r"\{.*\}", text, flags=re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return None


def record_text(c: dict) -> str:
    return (
        f"Funder: {c['funder']}\nRecipient: {c['recipient']}\nAmount: GBP {c['amount']:,.0f}\n"
        f"Award date: {c['award_date']}\nTitle: {c['title']}\nDescription: {c['description']}"
    )


def norm(s: str) -> str:
    return re.sub(r"\W+", " ", s.lower()).strip()


JUDGE_SYSTEM = """You check an automated impact screen of a grant record for unsupported claims.
You get the RECORD and the SCREEN OUTPUT. List every statement in the output's "impact" fields
(what, who, how_much, contribution, risk) that asserts a fact, number, place, group or outcome
that is NOT in the record. "not stated" and cautious wording are fine. Reasonable restatement
of the record is fine. Reply with JSON only: {"unsupported": ["..."], "grounded": true|false}
where grounded is false if and only if the list is non-empty."""


def judge(model: str, c: dict, out: dict) -> dict:
    payload = f"RECORD:\n{record_text(c)}\n\nSCREEN OUTPUT:\n{json.dumps(out, ensure_ascii=False)}"
    v = parse_json(chat(model, JUDGE_SYSTEM, payload, 2500))
    return v if v and isinstance(v.get("grounded"), bool) else {"unsupported": [], "grounded": None, "error": "judge returned invalid JSON"}


def run_case(c: dict, skill: str, model: str) -> dict:
    # Validate and retry: the model occasionally truncates or loops. Retries are reported, not hidden.
    for retries in range(3):
        raw = chat(model, skill, "Screen this record.\n\n" + record_text(c))
        out = parse_json(raw)
        if out and all(k in out for k in ("theme", "beneficiary", "funding_type", "outcome_stated", "impact_case_score")):
            return {"id": c["id"], "raw": raw, "out": out, "retries": retries}
    return {"id": c["id"], "raw": raw, "out": None, "retries": retries}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill", required=True)
    ap.add_argument("--tag", required=True)
    ap.add_argument("--model", default=SKILL_MODEL)
    ap.add_argument("--judge-model", default=JUDGE_MODEL)
    a = ap.parse_args()

    skill = re.sub(r"\A---.*?---\s*", "", Path(a.skill).read_text(encoding="utf-8"), flags=re.S)
    cases = [json.loads(l) for l in open(HERE / "cases.jsonl", encoding="utf-8")]
    by_id = {c["id"]: c for c in cases}

    cache = HERE / "results" / f"{a.tag}_raw.json"  # skill outputs are cached so a judge failure doesn't redo them
    (HERE / "results").mkdir(exist_ok=True)
    if cache.exists():
        runs = json.loads(cache.read_text(encoding="utf-8"))
    else:
        with ThreadPoolExecutor(4) as pool:
            runs = list(pool.map(lambda c: run_case(c, skill, a.model), cases))
        cache.write_text(json.dumps(runs, ensure_ascii=False, indent=1), encoding="utf-8")

    rows, planted = [], []
    random.seed(0)
    for r in runs:
        c, out = by_id[r["id"]], r["out"]
        row = {"id": c["id"], "label_by": c["label_by"], "valid_json": out is not None}
        if out:
            lab = c["label"]
            for f in FIELDS:
                row[f] = out.get(f) == lab[f]
            s = out.get("impact_case_score")
            row["pred_score"], row["true_score"] = s, lab["impact_case_score"]
            row["score_exact"] = s == lab["impact_case_score"]
            row["score_within1"] = isinstance(s, int) and abs(s - lab["impact_case_score"]) <= 1
            quotes = out.get("evidence_quotes") or []
            hay = norm(record_text(c))
            row["quotes_total"] = len(quotes)
            row["quotes_verbatim"] = sum(norm(q) in hay for q in quotes)
            row["pred"] = {f: out.get(f) for f in FIELDS}
            row["true"] = {f: lab[f] for f in FIELDS}
        rows.append(row)

    # Judge: clean outputs (+ planted fabrications on 4 of them)
    valid = [r for r in runs if r["out"]]
    plant_ids = {r["id"] for r in random.sample(valid, min(4, len(valid)))}
    fabrications = [
        "serves 5,000 refugees across Yorkshire each year",
        "has reduced reoffending by 40% according to an independent evaluation",
        "is a partnership with the NHS covering 12 hospitals",
        "was matched by a GBP 2m government grant",
    ]
    jobs = []
    for r in valid:
        out = json.loads(json.dumps(r["out"]))
        is_planted = r["id"] in plant_ids
        if is_planted:
            out.setdefault("impact", {})["how_much"] = "The programme " + fabrications[len(planted) % 4]
            planted.append(r["id"])
        jobs.append((r["id"], is_planted, out))
    with ThreadPoolExecutor(2) as pool:
        verdicts = list(pool.map(lambda j: judge(a.judge_model, by_id[j[0]], j[2]), jobs))
    judged = [{"id": j[0], "planted": j[1], "grounded": v.get("grounded"), "unsupported": v.get("unsupported")} for j, v in zip(jobs, verdicts)]
    for row in rows:
        for j in judged:
            if j["id"] == row["id"] and not j["planted"]:
                row["judge_grounded"] = j["grounded"]
                row["judge_unsupported"] = j["unsupported"]

    n = len(rows)
    ok = [r for r in rows if r["valid_json"]]
    pct = lambda k, rs=ok: round(100 * sum(bool(r[k]) for r in rs) / max(len(rs), 1))
    qt = sum(r["quotes_total"] for r in ok)
    clean = [j for j in judged if not j["planted"]]
    plant = [j for j in judged if j["planted"]]
    summary = {
        "tag": a.tag, "skill": a.skill, "model": a.model, "judge_model": a.judge_model, "n": n,
        "valid_json_pct": round(100 * len(ok) / n),
        "cases_needing_retry": sum(r.get("retries", 0) > 0 for r in runs),
        **{f"{f}_pct": pct(f) for f in FIELDS},
        "score_exact_pct": pct("score_exact"), "score_within1_pct": pct("score_within1"),
        "score_mae": round(sum(abs(r["pred_score"] - r["true_score"]) for r in ok if isinstance(r["pred_score"], int)) / max(len(ok), 1), 2),
        "quotes_verbatim_pct": round(100 * sum(r["quotes_verbatim"] for r in ok) / max(qt, 1)),
        "judge_grounded_clean": f"{sum(j['grounded'] is True for j in clean)}/{len([j for j in clean if j['grounded'] is not None])}",
        "judge_errors": sum(j["grounded"] is None for j in judged),
        "judge_caught_planted": f"{sum(j['grounded'] is False for j in plant)}/{len(plant)}",
        "by_label_author": {
            who: {"n": len([r for r in ok if r["label_by"] == who]), "fields_exact_pct": round(100 * sum(r[f] for r in ok if r["label_by"] == who for f in FIELDS) / max(4 * len([r for r in ok if r["label_by"] == who]), 1))}
            for who in ("user", "claude")
        },
    }
    (HERE / "results").mkdir(exist_ok=True)
    (HERE / "results" / f"{a.tag}.json").write_text(
        json.dumps({"summary": summary, "rows": rows, "judge": judged, "raw": {r["id"]: r["raw"] for r in runs}}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2))
    for row in rows:
        if row["valid_json"]:
            bad = [f for f in FIELDS if not row[f]]
            print(f"#{row['id']:>2} pred_score={row['pred_score']} true={row['true_score']} wrong_fields={bad}")
        else:
            print(f"#{row['id']:>2} INVALID JSON")


if __name__ == "__main__":
    main()
