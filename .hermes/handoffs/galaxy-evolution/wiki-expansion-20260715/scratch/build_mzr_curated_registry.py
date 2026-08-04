import json
import os
import urllib.parse
import urllib.request
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
OUT = AREA / "area1_mass_metallicity_CURATED_SOURCE_REGISTRY.json"
TOKEN = os.environ.get("ADS_API_TOKEN") or os.environ.get("ADS_DEV_KEY")
if not TOKEN:
    raise SystemExit("ADS token unavailable")
assert TOKEN is not None

SOURCES = [
    {"key":"Tremonti2004","bibcode":"2004ApJ...613..898T","doi":"10.1086/423264","arxiv":"astro-ph/0405537","type":"primary observation","boundary":"Local SDSS star-forming galaxies; gas-phase oxygen abundance and stellar mass; MZR shape and approximately 0.1 dex scatter."},
    {"key":"Gallazzi2005","bibcode":"2005MNRAS.362...41G","doi":"10.1111/j.1365-2966.2005.09321.x","arxiv":"astro-ph/0506539","type":"primary observation / stellar-population inference","boundary":"Local SDSS optical spectra; stellar metallicity estimates carry age-metallicity and model-systematic limitations."},
    {"key":"FinlatorDave2008","bibcode":"2008MNRAS.385.2181F","doi":"10.1111/j.1365-2966.2008.12991.x","arxiv":"0704.3100","type":"simulation/model","boundary":"Model interpretation of MZR through enrichment-dilution equilibrium and outflows; not a unique causal proof."},
    {"key":"Cooper2008","bibcode":"2008MNRAS.390..245C","doi":"10.1111/j.1365-2966.2008.13714.x","arxiv":"0805.0308","type":"primary observation","boundary":"Local SDSS star-forming galaxies; weak residual metallicity-environment association after controls."},
    {"key":"KewleyEllison2008","bibcode":"2008ApJ...681.1183K","doi":"10.1086/587500","arxiv":"0801.1849","type":"calibration/method","boundary":"Local strong-line metallicity calibrations; establishes large absolute-scale differences and conversion limits."},
    {"key":"Ellison2009","bibcode":"2009MNRAS.396.1257E","doi":"10.1111/j.1365-2966.2009.14817.x","arxiv":"0903.4684","type":"primary observation","boundary":"Local SDSS cluster/control samples; metallicity enhancement up to about 0.04-0.05 dex associated mainly with local overdensity."},
    {"key":"Mannucci2010","bibcode":"2010MNRAS.408.2115M","doi":"10.1111/j.1365-2966.2010.17291.x","arxiv":"1005.0006","type":"primary observation / empirical relation","boundary":"Local SDSS-derived gas-phase mass-SFR-metallicity surface; redshift invariance is not established beyond the tested regime."},
    {"key":"Yates2012","bibcode":"2012MNRAS.422..215Y","doi":"10.1111/j.1365-2966.2012.20595.x","arxiv":"1107.3145","type":"observation plus semi-analytic model","boundary":"Local SDSS and model comparison; reverse SFR-metallicity trend at high mass is a conditional result, not a universal law."},
    {"key":"Peng2015","bibcode":"2015Natur.521..192P","doi":"10.1038/nature14439","arxiv":"1505.03143","type":"stellar-population inference / quenching model","boundary":"Local stellar metallicity offsets interpreted through simplified chemical-evolution models; supports starvation but does not uniquely prove it."},
    {"key":"BarreraBallesteros2016","bibcode":"2016MNRAS.463.2513B","doi":"10.1093/mnras/stw1984","arxiv":"1609.01740","type":"primary resolved observation","boundary":"MaNGA disc galaxies and star-forming spaxels; local surface-density-metallicity relation with stated low-mass/high-sSFR exceptions."},
    {"key":"Trussler2020","bibcode":"2020MNRAS.491.5406T","doi":"10.1093/mnras/stz3286","arxiv":"1811.09283","type":"stellar-population inference / chemical-evolution model","boundary":"Local SDSS star-forming, green-valley and passive populations; quenching mechanisms and timescales are model-dependent inferences."},
    {"key":"Curti2020","bibcode":"2020MNRAS.491..944C","doi":"10.1093/mnras/stz2910","arxiv":"1910.00597","type":"calibration plus primary observation","boundary":"Local fully Te-anchored abundance scale; MZR/FMR parameters are tied to sample selection and this calibration family."},
    {"key":"Sanders2021","bibcode":"2021ApJ...914...19S","doi":"10.3847/1538-4357/abf4c1","arxiv":"2009.07292","type":"primary observation","boundary":"MOSDEF z about 2.3 and 3.3 plus consistently calibrated lower-redshift comparisons; exact evolution depends on diagnostic matching."},
    {"key":"Langeroodi2023","bibcode":"2023ApJ...957...39L","doi":"10.3847/1538-4357/acdbc1","arxiv":"2212.02491","type":"primary observation","boundary":"Small lensed JWST/NIRSpec sample at z about 8; early constraint with strong selection and calibration uncertainty."},
    {"key":"Nakajima2023","bibcode":"2023ApJS..269...33N","doi":"10.3847/1538-4365/acd556","arxiv":"2301.12825","type":"primary observation / calibration","boundary":"JWST/NIRSpec public-program sample at z=4-10; direct-method anchor exists for a subset and strong-line calibrations cover the remainder."},
    {"key":"Hirschmann2023","bibcode":"2023MNRAS.526.3504H","doi":"10.1093/mnras/stad2745","arxiv":"2305.03753","type":"simulation/model / calibration","boundary":"IllustrisTNG line-emission modeling; demonstrates possible high-z calibration biases but is not itself an empirical abundance census."},
    {"key":"Curti2024JADES","bibcode":"2024A&A...684A..75C","doi":"10.1051/0004-6361/202346698","arxiv":"2304.08516","type":"primary observation","boundary":"JADES JWST/NIRSpec sample at 3<z<10; low-mass MZR/FMR conclusions remain selection- and calibration-sensitive."},
    {"key":"Garcia2024","bibcode":"2024MNRAS.531.1398G","doi":"10.1093/mnras/stae1252","arxiv":"2403.08856","type":"simulation/model","boundary":"Illustris, IllustrisTNG and EAGLE comparison; supports an evolving weak FMR in simulations, not direct observational proof."},
    {"key":"Looser2024","bibcode":"2024MNRAS.532.2832L","doi":"10.1093/mnras/stae1581","arxiv":"2401.08769","type":"stellar-population inference","boundary":"Local MaNGA sample; evidence for a stellar mass-SFR-metallicity relation, with interpretation tied to spectral reconstruction and weighting."},
]


def fetch(bibcode):
    params = urllib.parse.urlencode({"q": f'bibcode:"{bibcode}"', "fl": "bibcode,title,author,year,doi,identifier,pub_raw,abstract", "rows": 2})
    req = urllib.request.Request(
        "https://api.adsabs.harvard.edu/v1/search/query?" + params,
        headers={"Authorization": "Bearer " + TOKEN, "User-Agent": "NebulaMind-MZR-curated-gate/1.0"},
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)["response"]["docs"]

rows = []
for source in SOURCES:
    docs = fetch(source["bibcode"])
    doc = docs[0] if len(docs) == 1 else None
    checks = {
        "single_ads_match": len(docs) == 1,
        "bibcode_match": bool(doc and doc.get("bibcode") == source["bibcode"]),
        "doi_match": bool(doc and source["doi"].lower() in [value.lower() for value in doc.get("doi", [])]),
        "arxiv_match": bool(doc and any(("arXiv:" + source["arxiv"]) == value for value in doc.get("identifier", []))),
        "abstract_present": bool(doc and doc.get("abstract")),
    }
    rows.append({
        **source,
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "resolved": None if not doc else {
            "title": doc.get("title", [""])[0],
            "authors": doc.get("author", []),
            "year": doc.get("year"),
            "publication": doc.get("pub_raw"),
            "doi": doc.get("doi", []),
            "identifiers": doc.get("identifier", []),
            "abstract": doc.get("abstract"),
        },
    })
summary = {
    "verification_route": "NASA ADS API exact-bibcode lookup; DOI and arXiv reconciled against ADS identifiers; abstracts retained for claim-boundary review",
    "status": "PASS" if all(row["status"] == "PASS" for row in rows) else "HOLD",
    "source_count": len(rows),
    "pass_count": sum(row["status"] == "PASS" for row in rows),
    "fail_count": sum(row["status"] == "FAIL" for row in rows),
    "sources": rows,
}
OUT.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
print(json.dumps({key: summary[key] for key in ("status", "source_count", "pass_count", "fail_count")}, sort_keys=True))
for row in rows:
    if row["status"] != "PASS":
        print(json.dumps({"key": row["key"], "checks": row["checks"], "resolved": row["resolved"]}, ensure_ascii=False, sort_keys=True))
raise SystemExit(0 if summary["status"] == "PASS" else 2)
