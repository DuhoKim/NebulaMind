import json
import re
import time
import unicodedata
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Dict, List, Optional

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
RAW = AREA / "area_review_02_madau_dickinson_2014_DR_RAW_PACKET.md"
OUT = AREA / "area_review_02_madau_dickinson_2014_SOURCE_VERIFICATION.json"
NED = Path("/Users/duhokim/.hermes/cache/web/ned.ipac.caltech.edu-6373b53fc0.md")
UA = "NebulaMind-review-source-verifier/1.0 (local advisory curation)"


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def sim(a: str, b: str) -> float:
    return SequenceMatcher(None, norm(a), norm(b)).ratio()


def get_json(url: str) -> Dict[str, Any]:
    last: Optional[Exception] = None
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=30) as response:
                return json.load(response)
        except Exception as exc:
            last = exc
            time.sleep(1.5 * (attempt + 1))
    assert last is not None
    raise last


raw = RAW.read_text()
body = raw.split("## Deep Research review-base result\n\n", 1)[1].split("\n\n## Captured external source anchors", 1)[0]
harvest = body.split("6. Primary-citation harvest", 1)[1].split("\n\n7. DO_NOT_USE_UNVERIFIED", 1)[0]
pattern = re.compile(
    r"^\[(REV02-P\d{3})\] (.+?) \((\d{4}), (.+?)\) \| title=(.+?) \| DOI:(.+?); arXiv:(.+?); ADS:(\S+) \| role=(\w+) \| review_locator=(.+?) \| (.+)$",
    re.M,
)
rows: List[Dict[str, Any]] = []
for match in pattern.finditer(harvest):
    key, authors, year, journal, title, doi, arxiv, bibcode, role, locator, boundary = match.groups()
    rows.append({"key": key, "authors": authors, "first_author": authors.split(",", 1)[0].split()[0], "year": int(year), "journal": journal, "title": title, "doi": doi, "arxiv": arxiv, "ads_bibcode": bibcode, "role": role, "review_locator": locator, "boundary": boundary})
if len(rows) != 40:
    raise SystemExit(f"expected 40 harvest rows, parsed {len(rows)}")

ned_text = NED.read_text()


def crossref_for(row: Dict[str, Any]) -> Dict[str, Any]:
    if row["doi"] == "none":
        return {"status": "not_supplied"}
    try:
        item = get_json("https://api.crossref.org/works/" + urllib.parse.quote(row["doi"], safe=""))["message"]
        title = " ".join(item.get("title") or [])
        authors = item.get("author") or []
        first = authors[0].get("family", "") if authors else ""
        date_parts = (item.get("published-print") or item.get("published-online") or item.get("issued") or {}).get("date-parts", [[]])
        year = date_parts[0][0] if date_parts and date_parts[0] else None
        return {"status": "resolved", "title": title, "first_author": first, "year": year, "doi": item.get("DOI"), "title_similarity": sim(row["title"], title), "author_pass": norm(row["first_author"]) in norm(first) or norm(first) in norm(row["first_author"]), "year_pass": year == row["year"]}
    except Exception as exc:
        return {"status": "error", "error": f"{type(exc).__name__}: {exc}"}


crossref: Dict[str, Dict[str, Any]] = {}
with ThreadPoolExecutor(max_workers=4) as pool:
    futures = {pool.submit(crossref_for, row): row["key"] for row in rows}
    for future in as_completed(futures):
        crossref[futures[future]] = future.result()

arxiv_ids = [row["arxiv"] for row in rows if row["arxiv"] != "none"]
query = "https://export.arxiv.org/api/query?id_list=" + urllib.parse.quote(",".join(arxiv_ids)) + "&max_results=100"
req = urllib.request.Request(query, headers={"User-Agent": UA})
with urllib.request.urlopen(req, timeout=60) as response:
    root = ET.fromstring(response.read())
ns = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
arxiv_map: Dict[str, Dict[str, Any]] = {}
for entry in root.findall("a:entry", ns):
    aid = entry.findtext("a:id", default="", namespaces=ns).rsplit("/", 1)[-1].split("v", 1)[0]
    arxiv_map[aid] = {
        "title": " ".join(entry.findtext("a:title", default="", namespaces=ns).split()),
        "authors": [node.findtext("a:name", default="", namespaces=ns) for node in entry.findall("a:author", ns)],
        "year": int(entry.findtext("a:published", default="0000", namespaces=ns)[:4]),
        "doi": entry.findtext("arxiv:doi", default="", namespaces=ns),
        "journal_ref": entry.findtext("arxiv:journal_ref", default="", namespaces=ns),
    }

verified = []
for row in rows:
    cr = crossref[row["key"]]
    av = None if row["arxiv"] == "none" else arxiv_map.get(row["arxiv"])
    membership = row["ads_bibcode"] in ned_text or row["ads_bibcode"].replace("&", "%26") in ned_text
    cr_pass = cr["status"] == "not_supplied" or (cr["status"] == "resolved" and cr["title_similarity"] >= 0.72 and cr["author_pass"] and cr["year_pass"])
    if av is None and row["arxiv"] != "none":
        av_pass = False
    elif av is None:
        av_pass = True
    else:
        author_pass = norm(row["first_author"]) in norm(" ".join(av["authors"]))
        doi_pass = not av["doi"] or row["doi"] == "none" or norm(av["doi"]) == norm(row["doi"])
        av_pass = sim(row["title"], av["title"]) >= 0.72 and author_pass and av["year"] == row["year"] and doi_pass
    status = "PASS" if membership and cr_pass and av_pass else "FAIL"
    verified.append({"source": row, "evidence": {"review_membership_via_ned_ads_bibcode": membership, "crossref": cr, "arxiv": av}, "checks": {"crossref_pass": cr_pass, "arxiv_pass": av_pass}, "status": status})

fails = [row["source"]["key"] for row in verified if row["status"] != "PASS"]
output = {"status": "PASS" if not fails else "FAIL", "verified_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "method": "NED review bibliography ADS-bibcode membership plus Crossref DOI and arXiv composite author/year/title reconciliation", "source_count": len(verified), "pass_count": len(verified) - len(fails), "fail_count": len(fails), "failures": fails, "rows": verified}
OUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
print(json.dumps({k: output[k] for k in ("status", "source_count", "pass_count", "fail_count", "failures")}, sort_keys=True))
raise SystemExit(0 if not fails else 2)
