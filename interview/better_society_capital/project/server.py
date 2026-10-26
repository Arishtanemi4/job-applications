"""MCP server over a local SQLite copy of 360Giving UK grants data (read-only).

Three narrow tools instead of raw SQL: the model gets a small, well-described surface,
results are capped so they cannot flood the context window, and the database is opened
read-only.

Run (stdio):  python server.py
Data:         python fetch_data.py   (builds data/grants.sqlite first)
"""
import sqlite3
from pathlib import Path

from mcp.server.fastmcp import FastMCP

DB = Path(__file__).parent / "data" / "grants.sqlite"
MAX_ROWS = 25
DESC_CHARS = 240

mcp = FastMCP("grants-360giving")


def _query(sql: str, params: tuple = ()) -> list[sqlite3.Row]:
    if not DB.exists():
        raise RuntimeError("data/grants.sqlite is missing. Run `python fetch_data.py` first.")
    con = sqlite3.connect(f"file:{DB.as_posix()}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    try:
        return con.execute(sql, params).fetchall()
    finally:
        con.close()


def _grant(r: sqlite3.Row) -> dict:
    desc = (r["description"] or "").strip()
    return {
        "grant_id": r["grant_id"],
        "funder": r["funder"],
        "recipient": r["recipient"],
        "recipient_id": r["recipient_id"],
        "amount_gbp": r["amount"],
        "award_date": r["award_date"],
        "title": r["title"],
        # Free text written by the funder: treat as data, never as instructions.
        "description": desc[:DESC_CHARS] + ("..." if len(desc) > DESC_CHARS else ""),
    }


@mcp.tool()
def search_grants(
    theme: str,
    region: str | None = None,
    min_amount: float | None = None,
    year_from: int | None = None,
    year_to: int | None = None,
    limit: int = 10,
) -> dict:
    """Search UK charitable grants (360Giving open data) by theme words.

    Use this to find who funded work on a topic such as "fuel poverty", "mental health"
    or "community energy". Every word in `theme` must appear in the grant title or
    description. Covers five funders only: Esmee Fairbairn, Power to Change, Lloyds Bank
    Foundation, Barrow Cadbury and Nesta. Returns the total matches and total value
    across ALL matches, plus the `limit` largest grants (max 25).

    Args:
        theme: Space-separated words, e.g. "fuel poverty".
        region: Optional place name matched against the grant's beneficiary location.
            Only some funders record this, so a region filter drops the others.
        min_amount: Optional minimum grant size in GBP.
        year_from: Optional first award year (inclusive).
        year_to: Optional last award year (inclusive).
        limit: Number of grants to return, 1 to 25.
    """
    words = [w for w in theme.split() if w]
    if not words:
        return {"error": "theme must contain at least one word"}
    where, params = [], []
    for w in words:
        where.append("(title LIKE ? OR description LIKE ?)")
        params += [f"%{w}%", f"%{w}%"]
    if region:
        where.append("location LIKE ?")
        params.append(f"%{region}%")
    if min_amount is not None:
        where.append("amount >= ?")
        params.append(min_amount)
    if year_from is not None:
        where.append("substr(award_date,1,4) >= ?")
        params.append(str(year_from))
    if year_to is not None:
        where.append("substr(award_date,1,4) <= ?")
        params.append(str(year_to))
    clause = " AND ".join(where)
    limit = max(1, min(limit, MAX_ROWS))

    agg = _query(f"SELECT COUNT(*) n, COALESCE(SUM(amount),0) total FROM grants WHERE {clause}", tuple(params))[0]
    rows = _query(f"SELECT * FROM grants WHERE {clause} ORDER BY amount DESC LIMIT ?", (*params, limit))
    return {
        "matches": agg["n"],
        "total_value_gbp": agg["total"],
        "returned": len(rows),
        "note": "Largest grants first. Narrow the query if matches is much larger than returned.",
        "grants": [_grant(r) for r in rows],
    }


@mcp.tool()
def get_funder_summary(funder: str) -> dict:
    """Summarise one funder's grant-making in this dataset.

    Returns number of grants, total and mean size, award-year range, grants and
    value per year, and the five largest recipients by total value. Use it to understand
    a funder's scale and focus before looking at individual grants.

    Args:
        funder: Part of the funder name, e.g. "Esmee", "Nesta", "Lloyds".
    """
    like = f"%{funder}%"
    names = _query("SELECT DISTINCT funder FROM grants WHERE funder LIKE ?", (like,))
    if not names:
        known = [r["funder"] for r in _query("SELECT DISTINCT funder FROM grants")]
        return {"error": f"no funder matches '{funder}'", "known_funders": known}
    if len(names) > 1:
        return {"error": "ambiguous funder name", "candidates": [r["funder"] for r in names]}
    name = names[0]["funder"]
    base = _query(
        "SELECT COUNT(*) n, SUM(amount) total, AVG(amount) mean, MIN(award_date) first, MAX(award_date) last "
        "FROM grants WHERE funder = ?",
        (name,),
    )[0]
    by_year = _query(
        "SELECT substr(award_date,1,4) yr, COUNT(*) n, SUM(amount) total FROM grants "
        "WHERE funder = ? GROUP BY yr ORDER BY yr",
        (name,),
    )
    top = _query(
        "SELECT recipient, recipient_id, COUNT(*) n, SUM(amount) total FROM grants "
        "WHERE funder = ? GROUP BY recipient_id ORDER BY total DESC LIMIT 5",
        (name,),
    )
    return {
        "funder": name,
        "grants": base["n"],
        "total_value_gbp": base["total"],
        "mean_grant_gbp": round(base["mean"] or 0),
        "first_award": base["first"],
        "last_award": base["last"],
        "per_year": [{"year": r["yr"], "grants": r["n"], "value_gbp": r["total"]} for r in by_year],
        "top_recipients": [
            {"recipient": r["recipient"], "recipient_id": r["recipient_id"], "grants": r["n"], "value_gbp": r["total"]}
            for r in top
        ],
    }


@mcp.tool()
def get_recipient(name_or_id: str, limit: int = 10) -> dict:
    """Look up an organisation's grants across all funders in the dataset.

    Pass a charity/company identifier such as "GB-CHC-1135192" for an exact match, or part
    of the organisation's name. Returns totals per funder and the most recent grants. If
    several different organisations match a name, returns them for you to choose from.

    Args:
        name_or_id: Org identifier (GB-CHC-..., GB-COH-...) or part of its name.
        limit: Number of recent grants to return, 1 to 25.
    """
    limit = max(1, min(limit, MAX_ROWS))
    if name_or_id.upper().startswith("GB-"):
        where, params = "recipient_id = ?", (name_or_id.upper(),)
    else:
        where, params = "recipient LIKE ?", (f"%{name_or_id}%",)
    orgs = _query(
        f"SELECT recipient_id, MIN(recipient) recipient, COUNT(*) n FROM grants WHERE {where} "
        "GROUP BY recipient_id ORDER BY n DESC LIMIT 8",
        params,
    )
    if not orgs:
        return {"error": f"no recipient matches '{name_or_id}'"}
    if len(orgs) > 1:
        return {
            "error": "several organisations match; call again with one recipient_id",
            "candidates": [{"recipient": o["recipient"], "recipient_id": o["recipient_id"], "grants": o["n"]} for o in orgs],
        }
    rid = orgs[0]["recipient_id"]
    by_funder = _query(
        "SELECT funder, COUNT(*) n, SUM(amount) total FROM grants WHERE recipient_id = ? GROUP BY funder ORDER BY total DESC",
        (rid,),
    )
    recent = _query("SELECT * FROM grants WHERE recipient_id = ? ORDER BY award_date DESC LIMIT ?", (rid, limit))
    return {
        "recipient": orgs[0]["recipient"],
        "recipient_id": rid,
        "total_grants": orgs[0]["n"],
        "total_value_gbp": sum(r["total"] or 0 for r in by_funder),
        "by_funder": [{"funder": r["funder"], "grants": r["n"], "value_gbp": r["total"]} for r in by_funder],
        "recent_grants": [_grant(r) for r in recent],
    }


if __name__ == "__main__":
    mcp.run()
