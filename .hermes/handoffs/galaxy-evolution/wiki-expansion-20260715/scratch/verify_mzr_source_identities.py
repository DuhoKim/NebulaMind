import json
import os
import re
import time
import unicodedata
import urllib.parse
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
PACKET = AREA / "area1_mass_metallicity_DR_PACKET.md"
OUTPUT = AREA / "area1_mass_metallicity_DR_IDENTIFIER_VERIFICATION.json"
ADS_URL = "https://api.adsabs.harvard.edu/v1/search/query"
TOKEN = os.environ.get("ADS_API_TOKEN") or os.environ.get("ADS_DEV_KEY")
if not TOKEN:
    raise SystemExit("ADS token unavailable")
assert TOKEN is not None


def norm(value):
    value = unicodedata.normalize("NFKD", value or "")
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def ads(query):
    params = urllib.parse.urlencode({
        "q": query,
        "fl": "bibcode,title,author,year,doi,identifier,pub,pub_raw,abstract",
        "rows": 5,
    })
    request = urllib.request.Request(
        ADS_URL + "?" + params,
        headers={"Authorization": "Bearer " + TOKEN, "User-Agent": "NebulaMind-MZR-identifier-gate/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)["response"]["docs"]


text = PACKET.read_text()
start = text.index("6. Source identity ledger")
end = text.index("MZR_DR_PACKET_COMPLETE_REFERENCE_ONLY", start)
ledger = text[start:end]
line_re = re.compile(
    r"(?m)^(.+?) \((\d{4}), ([^)]+)\) \| (.+?) \| role=(established|debate|caveat|future) \| (.+)$"
)
rows = []
for match in line_re.finditer(ledger):
    authors, year, journal, identifiers, role, boundary = match.groups()
    after = ledger[match.end():]
    title_match = re.search(r"(?m)^Resolved Title: (.+)$", after)
    ids_match = re.search(r"(?m)^IDs: (.+)$", after)
    type_match = re.search(r"(?m)^Type: (.+)$", after)
    if not title_match or not ids_match or not type_match:
        raise RuntimeError(f"ledger block incomplete after {authors}")
    doi_match = re.search(r"DOI:([^;| ]+)", identifiers, re.I)
    arxiv_match = re.search(r"arXiv:([^;| ]+)", identifiers, re.I)
    bib_match = re.search(r"ADS:([^;| ]+)", identifiers, re.I)
    claimed = {
        "authors": authors,
        "year": year,
        "journal": journal,
        "identifiers": identifiers,
        "doi": doi_match.group(1).rstrip(".,") if doi_match else None,
        "arxiv": arxiv_match.group(1).rstrip(".,") if arxiv_match else None,
        "bibcode": bib_match.group(1).rstrip(".,") if bib_match else None,
        "role": role,
        "claim_boundary": boundary,
        "resolved_title": title_match.group(1),
        "used_by": [item.strip() for item in ids_match.group(1).split(",")],
        "epistemic_type": type_match.group(1),
    }
    queries = []
    if claimed["bibcode"]:
        queries.append(f'bibcode:"{claimed["bibcode"]}"')
    if claimed["doi"]:
        queries.append(f'doi:"{claimed["doi"]}"')
    if claimed["arxiv"]:
        arxiv = claimed["arxiv"].replace("arXiv:", "")
        queries.append(f'identifier:"arXiv:{arxiv}"')
    if not queries:
        raise RuntimeError(f"source has no identifier: {claimed}")
    candidates = {}
    for query in queries:
        for candidate in ads(query):
            candidates[candidate.get("bibcode")] = candidate
        time.sleep(0.2)
    exact = list(candidates.values())
    doc = exact[0] if len(exact) == 1 else None
    checks = {
        "single_authoritative_match": len(exact) == 1,
        "year_match": bool(doc and str(doc.get("year")) == year),
        "first_author_match": False,
        "title_match": False,
        "doi_match": None if not claimed["doi"] else False,
        "arxiv_match": None if not claimed["arxiv"] else False,
        "bibcode_match": None if not claimed["bibcode"] else False,
    }
    resolved = None
    if doc:
        first_claimed = norm(re.split(r",| & | and | et al\.", authors)[0]).split()[0]
        first_resolved = norm(doc.get("author", [""])[0]).split()[0]
        title = doc.get("title", [""])[0]
        title_score = SequenceMatcher(None, norm(claimed["resolved_title"]), norm(title)).ratio()
        checks.update({
            "first_author_match": first_claimed == first_resolved,
            "title_match": title_score >= 0.94,
            "doi_match": None if not claimed["doi"] else claimed["doi"].lower() in [str(value).lower() for value in doc.get("doi", [])],
            "arxiv_match": None if not claimed["arxiv"] else any(claimed["arxiv"] in value for value in doc.get("identifier", [])),
            "bibcode_match": None if not claimed["bibcode"] else doc.get("bibcode") == claimed["bibcode"],
        })
        resolved = {
            "bibcode": doc.get("bibcode"),
            "title": title,
            "authors": doc.get("author", []),
            "year": doc.get("year"),
            "doi": doc.get("doi", []),
            "identifiers": doc.get("identifier", []),
            "publication": doc.get("pub_raw") or doc.get("pub"),
            "abstract": doc.get("abstract"),
            "title_similarity": round(title_score, 4),
        }
    required_checks = [value for value in checks.values() if value is not None]
    status = "PASS" if required_checks and all(required_checks) else "FAIL"
    candidate_summaries = [
        {
            "bibcode": candidate.get("bibcode"),
            "title": candidate.get("title", [""])[0],
            "authors": candidate.get("author", []),
            "year": candidate.get("year"),
            "doi": candidate.get("doi", []),
            "identifiers": candidate.get("identifier", []),
        }
        for candidate in exact
    ]
    rows.append({
        "status": status,
        "claimed": claimed,
        "checks": checks,
        "resolved": resolved,
        "queries": queries,
        "match_count": len(exact),
        "candidate_summaries": candidate_summaries,
    })

summary = {
    "status": "PASS" if rows and all(row["status"] == "PASS" for row in rows) else "HOLD",
    "source_count": len(rows),
    "pass_count": sum(row["status"] == "PASS" for row in rows),
    "fail_count": sum(row["status"] == "FAIL" for row in rows),
    "packet_path": str(PACKET),
    "rows": rows,
}
OUTPUT.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
print(json.dumps({k: summary[k] for k in ("status", "source_count", "pass_count", "fail_count")}, sort_keys=True))
for row in rows:
    if row["status"] != "PASS":
        print(json.dumps({"claimed": row["claimed"], "checks": row["checks"], "resolved": row["resolved"]}, ensure_ascii=False, sort_keys=True))
raise SystemExit(0 if summary["status"] == "PASS" else 2)
