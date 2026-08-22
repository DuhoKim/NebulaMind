#!/usr/bin/env python3
"""Diff the harvest against the known bibliography, weight every record by evidence tier.

Weights (Duho: "analyse with different weights") — evidence class, not importance:
  W1 = 1.0   peer-reviewed journal article (DOI + journal ref)
  W2 = 0.6   published venue, weaker form (proceedings, letters w/o resolved journal)
  W3 = 0.3   preprint only (arXiv, no journal ref, no DOI)
  W4 = 0.1   book / no locatable record
The weight says how much a claim may LEAN on the item, per the standing rule that
peer-reviewed is the base layer. It does not say the item is unimportant.
"""
import json, re, pathlib

HERE = pathlib.Path(__file__).parent
BIB = HERE.parent / "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md"

def norm(t): return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()

def known_keys():
    s = BIB.read_text()
    dois = {d.lower() for d in re.findall(r"\b(10\.\d{4,5}/[^\s)`,]+)", s)}
    arx  = {a.lower() for a in re.findall(r"arXiv:([a-z\-]*/?\d{4}\.?\d{4,5})", s)}
    # titles in quotes
    titles = {norm(t) for t in re.findall(r'"([^"]{15,120})[.,]?"', s)}
    return dois, arx, titles

def tier(r):
    has_doi = bool(r.get("doi")); jr = (r.get("journal_ref") or "").strip()
    if has_doi and jr: return "W1", 1.0
    if has_doi or (jr and not jr.lower().startswith("arxiv")): return "W2", 0.6
    if r.get("arxiv"): return "W3", 0.3
    return "W4", 0.1

BHU_HINT = re.compile(
    r"(universe (inside|in|as) a black hole|black.hole (universe|cosmolog|interior)|"
    r"cosmological natural selection|new universe|baby universe|bounce.*(torsion|cartan)|"
    r"(torsion|cartan).*(bounce|cosmolog)|white hole.*(big bang|cosmolog)|"
    r"holographic.*(big bang|origin)|inside (a )?black hole)", re.I)

def main():
    h = json.loads((HERE / "harvest.json").read_text())
    dois, arx, titles = known_keys()
    out = []
    for r in h["records"]:
        t, w = tier(r)
        kn = ((r.get("doi") or "").lower() in dois or
              (r.get("arxiv") or "").lower().replace("v1","") in arx or
              norm(r.get("title")) in titles)
        rel = bool(BHU_HINT.search(r.get("title") or ""))
        out.append({**r, "tier": t, "weight": w, "known": kn, "on_topic_by_title": rel})
    new_rel = [r for r in out if not r["known"] and r["on_topic_by_title"]]
    new_rel.sort(key=lambda r: (-r["weight"], -(int(r["year"]) if str(r.get("year","")).isdigit() else 0)))
    res = {"n_harvested": len(out),
           "n_known_matched": sum(1 for r in out if r["known"]),
           "n_new_on_topic": len(new_rel),
           "tier_tally_new_on_topic": {},
           "new_on_topic": new_rel,
           "all": out}
    for r in new_rel:
        res["tier_tally_new_on_topic"][r["tier"]] = res["tier_tally_new_on_topic"].get(r["tier"], 0) + 1
    (HERE / "weighted_diff.json").write_text(json.dumps(res, indent=1))
    print(f"  harvested {len(out)} | matched known {res['n_known_matched']} | NEW on-topic {len(new_rel)}")
    print(f"  new-by-tier: {res['tier_tally_new_on_topic']}")
    for r in new_rel[:20]:
        print(f"   {r['tier']} {r.get('year','?'):>4} {(r.get('title') or '')[:76]}")


if __name__ == "__main__":
    main()
