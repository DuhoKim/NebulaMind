import json
import re
import time
import unicodedata
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional

P = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/area3_gas_depletion_CURATED_SOURCE_REGISTRY.json")
old = json.loads(P.read_text())
fix = {
    "Decarli2020": {"doi": "10.3847/1538-4357/abaa3b"},
    "Walter2020": {"arxiv": "2009.11126"},
    "Bolatto2013": {"arxiv": "1301.3498"},
    "Ellison2020": {"doi": "10.1093/mnrasl/slz179", "arxiv": "1911.11887"},
    "Saintonge2011b": {"doi": "10.1111/j.1365-2966.2011.18823.x", "arxiv": "1104.0019"},
    "Daddi2010": {"arxiv": "1003.3889"},
    "Lada2012": {"arxiv": "1112.4466"},
    "Martig2009": {"arxiv": "0905.4669"},
    "Catinella2010": {"doi": "10.1111/j.1365-2966.2009.16180.x"},
    "Scoville2016": {"arxiv": "1511.05149"},
    "Bigiel2011": {"arxiv": "1102.1720"},
}


def norm(value):
    return re.sub(r"[^a-z0-9]+", "", unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower())


def words(value):
    ignored = {"from", "with", "that", "this", "galaxy", "galaxies", "star", "formation"}
    return {word for word in re.findall(r"[a-z0-9]+", unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()) if len(word) > 3 and word not in ignored}


def similarity(a, b):
    left, right = words(a), words(b)
    return len(left & right) / max(1, len(left | right))


def get_json(url):
    request = urllib.request.Request(url, headers={"User-Agent": "NebulaMind-GAS-curation/1.1 (mailto:research@example.invalid)"})
    error: Optional[Exception] = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=40) as response:
                return json.load(response)
        except Exception as exc:
            error = exc
            time.sleep(2**attempt)
    assert error is not None
    raise error


sources = []
ads = {}
for row in old["rows"]:
    source = dict(row["source"])
    source["authors"] = re.sub(r"^\d+\|", "", source["authors"])
    source.update(fix.get(source["key"], {}))
    sources.append(source)
    ads[source["key"]] = row["evidence"]["public_ads"]

ids = ",".join(source["arxiv"] for source in sources)
url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": ids, "max_results": len(sources)})
request = urllib.request.Request(url, headers={"User-Agent": "NebulaMind-GAS-curation/1.1"})
with urllib.request.urlopen(request, timeout=60) as response:
    root = ET.fromstring(response.read())
namespace = {"a": "http://www.w3.org/2005/Atom"}
arxiv = {}
for entry in root.findall("a:entry", namespace):
    arxiv_id = entry.findtext("a:id", default="", namespaces=namespace).split("/abs/")[-1].split("v")[0]
    arxiv[arxiv_id] = {
        "id": entry.findtext("a:id", default="", namespaces=namespace),
        "title": " ".join(entry.findtext("a:title", default="", namespaces=namespace).split()),
        "first_author": entry.findtext("a:author/a:name", default="", namespaces=namespace),
        "published": entry.findtext("a:published", default="", namespaces=namespace)[:4],
    }

rows = []
for source in sources:
    checks = {}
    evidence = {}
    try:
        record = get_json("https://api.crossref.org/works/" + urllib.parse.quote(source["doi"], safe=""))["message"]
        title = (record.get("title") or [""])[0]
        first_author = ((record.get("author") or [{}])[0].get("family") or "")
        year = ((record.get("issued") or {}).get("date-parts") or [[None]])[0][0]
        expected_author = norm(source["authors"].split()[0])
        checks.update(
            crossref_doi=norm(record.get("DOI", "")) == norm(source["doi"]),
            crossref_author=expected_author in norm(first_author),
            crossref_year=int(year or 0) == int(source["year"]),
        )
        evidence["crossref"] = {"doi": record.get("DOI"), "title": title, "first_author": first_author, "issued_year": year}
    except Exception as exc:
        title = ""
        checks.update(crossref_doi=False, crossref_author=False, crossref_year=False)
        evidence["crossref_error"] = f"{type(exc).__name__}: {exc}"
    arxiv_record = arxiv.get(source["arxiv"])
    if arxiv_record:
        expected_author = norm(source["authors"].split()[0])
        checks["arxiv_id"] = norm(source["arxiv"]) in norm(arxiv_record["id"])
        checks["arxiv_author"] = expected_author in norm(arxiv_record["first_author"])
        checks["arxiv_title_match"] = similarity(title, arxiv_record["title"]) >= 0.30
        evidence["arxiv"] = arxiv_record
    else:
        checks.update(arxiv_id=False, arxiv_author=False, arxiv_title_match=False)
        evidence["arxiv_error"] = "missing from batch API result"
    ads_record = ads[source["key"]]
    ads_title = ads_record.get("title") or ""
    expected_path = urllib.parse.quote(source["bibcode"], safe="")
    checks["public_ads_exact_route"] = expected_path in (ads_record.get("url") or "") and not ads_record.get("error")
    checks["ads_crossref_title_match"] = similarity(ads_title.replace(" - ADS", "").replace(" - Astrophysics Data System", ""), title) >= 0.30
    evidence["public_ads"] = {
        "url": ads_record.get("url"),
        "title": ads_title,
        "error": ads_record.get("error"),
        "exact_bibcode_route": checks["public_ads_exact_route"],
    }
    source["title"] = title
    rows.append({"status": "PASS" if all(checks.values()) else "FAIL", "source": source, "checks": checks, "evidence": evidence})
    time.sleep(0.12)

out = {
    "status": "PASS" if all(row["status"] == "PASS" for row in rows) else "HOLD",
    "method": "Composite identity reconciliation using exact public ADS abstract routes/titles, Crossref DOI records, and arXiv export metadata. Eleven cross-wired raw identifiers were corrected before promotion. No ADS API claim is made; Hwao's ADS API verifier and jury remain the live-wiki gate.",
    "source_count": len(rows),
    "pass_count": sum(row["status"] == "PASS" for row in rows),
    "fail_count": sum(row["status"] == "FAIL" for row in rows),
    "corrected_raw_tuples": fix,
    "rows": rows,
}
P.write_text(json.dumps(out, indent=2, ensure_ascii=False, sort_keys=True) + "\n")
print(json.dumps({"status": out["status"], "source_count": out["source_count"], "pass_count": out["pass_count"], "fail_count": out["fail_count"]}, sort_keys=True))
for row in rows:
    if row["status"] == "FAIL":
        print(json.dumps({"key": row["source"]["key"], "checks": row["checks"], "evidence": row["evidence"]}, ensure_ascii=False, sort_keys=True))
raise SystemExit(0 if out["status"] == "PASS" else 2)
