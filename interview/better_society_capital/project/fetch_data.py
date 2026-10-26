"""Download a few 360Giving funder files and load them into one SQLite table.

The 360Giving registry (https://registry.threesixtygiving.org/data.json) lists every
publisher's file. We pick a handful of funders close to social-impact work, normalise the
two shapes we meet (360Giving xlsx/csv with "Recipient Org:Name"-style headers, and the
JSON grants array) and write data/grants.sqlite for server.py to query.

Run:  python fetch_data.py
"""
import io
import json
import re
import sqlite3
from pathlib import Path

import httpx
import pandas as pd

HERE = Path(__file__).parent
RAW = HERE / "data" / "raw"
DB = HERE / "data" / "grants.sqlite"
REGISTRY = "https://registry.threesixtygiving.org/data.json"

# (publisher substring, title substring) -> one dataset each
WANTED = [
    ("Esm", "grants and social investments"),
    ("Power to Change", "Grants awarded since 2015"),
    ("Lloyds Bank Foundation", "Grants awarded from 2010"),
    ("Barrow Cadbury", "Grants awarded since April 2012"),
    ("Nesta", "Nesta grants awarded"),
]

# 360Giving column name (lower-cased, spaces stripped) -> our column
COLS = {
    "identifier": "grant_id",
    "title": "title",
    "description": "description",
    "amountawarded": "amount",
    "awarddate": "award_date",
    "recipientorg:identifier": "recipient_id",
    "recipientorg:name": "recipient",
    "fundingorg:name": "funder",
    "beneficiarylocation:name": "location",
    "grantprogramme:title": "programme",
}


def pick_datasets(registry: list[dict]) -> list[dict]:
    chosen = []
    for pub, title in WANTED:
        for ds in registry:
            if pub in ds["publisher"]["name"] and title.lower() in ds["title"].lower():
                chosen.append(ds)
                break
        else:
            print(f"!! not in registry: {pub} / {title}")
    return chosen


def from_json(payload: dict, funder: str) -> pd.DataFrame:
    rows = []
    for g in payload.get("grants", []):
        recip = (g.get("recipientOrganization") or [{}])[0]
        loc = (g.get("beneficiaryLocation") or [{}])[0]
        prog = g.get("grantProgramme") or [{}]
        rows.append(
            {
                "grant_id": g.get("id"),
                "title": g.get("title"),
                "description": g.get("description"),
                "amount": g.get("amountAwarded"),
                "award_date": g.get("awardDate"),
                "recipient_id": recip.get("id"),
                "recipient": recip.get("name"),
                "funder": ((g.get("fundingOrganization") or [{}])[0]).get("name") or funder,
                "location": loc.get("name"),
                "programme": prog[0].get("title"),
            }
        )
    return pd.DataFrame(rows)


def from_sheet(content: bytes, url: str, funder: str) -> pd.DataFrame:
    if re.search(r"\.csv", url, re.I):
        sheets = {"csv": pd.read_csv(io.BytesIO(content), dtype=str)}
    else:
        sheets = pd.read_excel(io.BytesIO(content), sheet_name=None, dtype=str)
    best = pd.DataFrame()
    for df in sheets.values():
        df = df.rename(columns=lambda c: re.sub(r"\s+", "", str(c)).lower())
        df = df.rename(columns={k: v for k, v in COLS.items() if k in df.columns})
        if "amount" in df.columns and "title" in df.columns and len(df) > len(best):
            best = df
    for c in COLS.values():
        if c not in best.columns:
            best[c] = None
    best["funder"] = best["funder"].fillna(funder)
    return best[list(COLS.values())]


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    with httpx.Client(follow_redirects=True, timeout=120, headers={"User-Agent": "Mozilla/5.0"}) as http:
        registry = http.get(REGISTRY).json()
        frames = []
        for ds in pick_datasets(registry):
            funder = ds["publisher"]["name"]
            url = ds["distribution"][0]["downloadURL"]
            print(f"{funder}: {url}")
            resp = http.get(url)
            resp.raise_for_status()
            (RAW / re.sub(r"\W+", "_", funder)).with_suffix(".bin").write_bytes(resp.content)
            if "json" in resp.headers.get("content-type", "") or resp.content[:1] in (b"{", b"["):
                df = from_json(json.loads(resp.content), funder)
            else:
                df = from_sheet(resp.content, url, funder)
            df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
            df["award_date"] = df["award_date"].astype(str).str[:10]
            print(f"  {len(df)} grants, {df['amount'].notna().sum()} with amounts")
            frames.append(df)
    grants = pd.concat(frames, ignore_index=True)
    grants["funder"] = grants["funder"].str.replace(r"^Esm.e ", "Esmée ", regex=True)  # registry mangles the accent
    with sqlite3.connect(DB) as con:
        grants.to_sql("grants", con, if_exists="replace", index=False)
    print(f"wrote {len(grants)} grants to {DB}")


if __name__ == "__main__":
    main()
