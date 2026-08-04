import json
import os
import time
import urllib.parse
import urllib.request
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
OUT = AREA / "area2_chemical_evolution_DR_RAW_IDENTIFIER_VERIFICATION.json"
TOKEN = os.environ.get("ADS_API_TOKEN") or os.environ.get("ADS_DEV_KEY")
if not TOKEN:
    raise SystemExit("ADS token unavailable")
TOKEN_VALUE = str(TOKEN)

CLAIMED = [
    {"key":"Tinsley1980","authors":"Tinsley","year":"1980","doi":None,"arxiv":None,"bibcode":"1980FCPh....5..287T"},
    {"key":"Mannucci2010","authors":"Mannucci","year":"2010","doi":"10.1111/j.1365-2966.2010.17291.x","arxiv":"1005.0006","bibcode":"2010MNRAS.408.2115M"},
    {"key":"Lilly2013","authors":"Lilly","year":"2013","doi":"10.1088/0004-637X/772/2/119","arxiv":"1303.5059","bibcode":"2013ApJ...772..119L"},
    {"key":"Kewley2019","authors":"Kewley","year":"2019","doi":"10.1146/annurev-astro-081817-051832","arxiv":"1910.09730","bibcode":"2019ARA&A..57..511K"},
    {"key":"MaozBrandt2012","authors":"Maoz","year":"2012","doi":"10.1111/j.1365-2966.2012.21871.x","arxiv":None,"bibcode":"2012MNRAS.426.3282M"},
    {"key":"MaozNelemans2014","authors":"Maoz","year":"2014","doi":"10.1146/annurev-astro-082812-140956","arxiv":None,"bibcode":"2014ARA&A..52..107M"},
    {"key":"KarakasLattanzio2014","authors":"Karakas","year":"2014","doi":"10.1017/pasa.2014.21","arxiv":None,"bibcode":"2014PASA...31...30K"},
    {"key":"Vincenzo2016","authors":"Vincenzo","year":"2016","doi":"10.1093/mnras/stw532","arxiv":None,"bibcode":"2016MNRAS.458.3466V"},
    {"key":"Curti2020","authors":"Curti","year":"2020","doi":"10.1093/mnras/stz2910","arxiv":"1910.00597","bibcode":"2020MNRAS.491..944C"},
    {"key":"Cameron2023","authors":"Cameron","year":"2023","doi":"10.1093/mnras/stad1579","arxiv":"2302.10142","bibcode":"2023MNRAS.523.3516C"},
    {"key":"Yates2022","authors":"Yates","year":"2022","doi":"10.1093/mnras/stac2205","arxiv":None,"bibcode":"2022MNRAS.516.1275Y"},
    {"key":"Belfiore2017","authors":"Belfiore","year":"2017","doi":"10.1093/mnras/stx789","arxiv":None,"bibcode":"2017MNRAS.469..151B"},
    {"key":"SellwoodBinney2002","authors":"Sellwood","year":"2002","doi":"10.1046/j.1365-8711.2002.05806.x","arxiv":None,"bibcode":"2002MNRAS.336..785S"},
    {"key":"Stott2013","authors":"Stott","year":"2013","doi":"10.1093/mnras/stt1836","arxiv":"1309.6321","bibcode":"2013MNRAS.436.1130S"},
    {"key":"Cowan1991","authors":"Cowan","year":"1991","doi":"10.1016/0370-1573(91)90070-3","arxiv":None,"bibcode":"1991PhR...208..267C"},
]


def search(query):
    params = urllib.parse.urlencode({"q": query, "fl": "bibcode,title,author,year,doi,identifier,pub_raw,abstract", "rows": 5})
    request = urllib.request.Request(
        "https://api.adsabs.harvard.edu/v1/search/query?" + params,
        headers={"Authorization": "Bearer " + TOKEN_VALUE, "User-Agent": "NebulaMind-CHEM-raw-identity-gate/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)["response"]["docs"]

rows = []
for source in CLAIMED:
    queries = [f'bibcode:"{source["bibcode"]}"']
    if source["doi"]:
        queries.append(f'doi:"{source["doi"]}"')
    if source["arxiv"]:
        queries.append(f'identifier:"arXiv:{source["arxiv"]}"')
    candidates = {}
    for query in queries:
        for doc in search(query):
            candidates[doc.get("bibcode")] = doc
        time.sleep(0.2)
    docs = list(candidates.values())
    doc = docs[0] if len(docs) == 1 else None
    checks = {
        "single_composite_record": len(docs) == 1,
        "bibcode_match": bool(doc and doc.get("bibcode") == source["bibcode"]),
        "year_match": bool(doc and str(doc.get("year")) == source["year"]),
        "first_author_match": bool(doc and doc.get("author") and doc["author"][0].lower().startswith(source["authors"].lower())),
        "doi_match": None if not source["doi"] else bool(doc and source["doi"].lower() in [value.lower() for value in doc.get("doi", [])]),
        "arxiv_match": None if not source["arxiv"] else bool(doc and ("arXiv:" + source["arxiv"]) in doc.get("identifier", [])),
    }
    status = "PASS" if all(value for value in checks.values() if value is not None) else "FAIL"
    summaries = [{
        "bibcode": candidate.get("bibcode"),
        "title": candidate.get("title", [""])[0],
        "authors": candidate.get("author", []),
        "year": candidate.get("year"),
        "doi": candidate.get("doi", []),
        "identifiers": candidate.get("identifier", []),
    } for candidate in docs]
    rows.append({"status": status, "claimed": source, "checks": checks, "candidates": summaries})
summary = {
    "status": "PASS" if all(row["status"] == "PASS" for row in rows) else "HOLD",
    "source_count": len(rows),
    "pass_count": sum(row["status"] == "PASS" for row in rows),
    "fail_count": sum(row["status"] == "FAIL" for row in rows),
    "rows": rows,
}
OUT.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
print(json.dumps({key: summary[key] for key in ("status", "source_count", "pass_count", "fail_count")}, sort_keys=True))
for row in rows:
    if row["status"] == "FAIL":
        print(json.dumps({"claimed": row["claimed"], "checks": row["checks"], "candidates": row["candidates"]}, ensure_ascii=False, sort_keys=True))
raise SystemExit(0 if summary["status"] == "PASS" else 2)
