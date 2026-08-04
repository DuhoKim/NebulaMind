import json
import re
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
IDENTITIES = AREA / "scratch/review_base08_ads_identities.json"
OUT = AREA / "area_review_08_tumlinson_peeples_werk_2017_CURATED_SOURCE_REGISTRY.json"
SUPPORTING = {"P010"}
QUARANTINE = {
    "P031": "AGN_CENTERED_NOT_USABLE: ADS resolves this as a mechanical AGN-feedback simulation of massive early-type galaxies, outside the non-AGN core harvest",
    "P039": "AGN_CENTERED_NOT_USABLE: black-hole growth and AGN-feedback simulation, explicitly outside the non-AGN core harvest",
    "P049": "AGN_CENTERED_NOT_USABLE: Milky Way nuclear/Fermi-bubble outflow attributed to Galactic-center activity; not used in the non-AGN core",
    "P051": "UNCITED_NOT_USABLE: Heckman et al. 2000 is absent from the review bibliography",
    "P067": "UNCITED_NOT_USABLE: Thom & Chen 2008 is absent from the review bibliography",
}
ROLE_MAP = {"observation":"measurement","analytic_theory":"analytic_theory","hydrodynamic_simulation":"hydrodynamic_simulation","semi_analytic_model":"semi_analytic_model","calibration":"calibration","review_synthesis":"supporting_review"}

def norm(v):
    if v is None or str(v).strip().lower()=="none": return None
    return str(v).strip()
def eq(a,b):
    aa,bb=norm(a),norm(b)
    if aa is None or bb is None: return aa is None and bb is None
    return re.sub(r"\s+"," ",aa).casefold()==re.sub(r"\s+"," ",bb).casefold()

rows=json.loads(IDENTITIES.read_text())["sources"]
sources=[]
for row in rows:
    key=row["key"]; ads=row["ads_direct"]
    assert ads["status"]=="PASS", (key,ads)
    title=norm(ads["title"]); doi=norm(ads["doi"]); arxiv=norm(ads["arxiv"]); bib=norm(ads["bibcode"])
    role="supporting_review" if key in SUPPORTING else ROLE_MAP[row["role_raw"]]
    corrections=[]
    for field,raw,canonical in (("title",row["title_raw"],title),("doi",row["doi_raw"],doi),("arxiv",row["arxiv_raw"],arxiv),("ads_bibcode",row["ads_raw"],bib)):
        if not eq(raw,canonical): corrections.append({"field":field,"raw":norm(raw),"canonical":canonical})
    if row["role_raw"]!=role: corrections.append({"field":"role","raw":row["role_raw"],"canonical":role})
    status="QUARANTINED" if key in QUARANTINE else "PASS"
    if status=="PASS":
        membership="PASS_AR5IV_2016_PREPRINT_REFERENCE" if key=="P007" else "PASS_AR5IV_AUTHOR_YEAR_JOURNAL_PAGE"
    else:
        membership="PASS_BUT_TOPIC_EXCLUDED" if key in {"P031","P039","P049"} else "FAIL_NOT_IN_AR5IV_REVIEW_BIBLIOGRAPHY"
    sources.append({
        "key":f"REV08-{key}","authors":row["authors_raw"],"year":row["year"],"journal":ads["publication"] or row["journal_raw"],
        "title":title,"doi":doi,"arxiv":arxiv,"ads_bibcode":bib,"role":role,"review_locator":row["review_locator_raw"],"boundary":row["boundary_raw"],
        "source_status":status,"identity_verification":{"status":"PASS_ADS_DIRECT" if status=="PASS" else "QUARANTINED","ads_url":ads["url"],"review_membership":membership},
        "raw_tuple_corrected":bool(corrections),"corrections":corrections,"quarantine_reason":QUARANTINE.get(key),
    })
usable=[s for s in sources if s["source_status"]=="PASS"]
primary=[s for s in usable if s["role"]!="supporting_review"]
supporting=[s for s in usable if s["role"]=="supporting_review"]
quarantined=[s for s in sources if s["source_status"]!="PASS"]
assert len(sources)==73
assert len(primary)==67
assert len(supporting)==1
assert len(quarantined)==5
assert len({s["key"] for s in sources})==73
assert all(s["year"]<=2017 for s in usable)
assert all(s["ads_bibcode"] for s in usable)
registry={
 "status":"PASS_COMPOSITE_IDS_AND_REVIEW_MEMBERSHIP",
 "mission_id":"GALAXY_REVIEW_BASE_DR_20260715","queue_item":8,
 "review":{"key":"REV08-R00","authors":"Tumlinson J, Peeples MS & Werk JK","year":2017,"title":"The Circumgalactic Medium","journal":"Annual Review of Astronomy and Astrophysics","doi":"10.1146/annurev-astro-091916-055240","arxiv":"1709.09180","ads_bibcode":"2017ARA&A..55..389T","identity_status":"PASS_ADS_CROSSREF_ARXIV"},
 "review_bibliography_basis":{"source":"https://ar5iv.labs.arxiv.org/html/1709.09180","status":"PASS_COMPLETE_REVIEW_TEXT_AND_REFERENCE_LIST_WEB_ONLY","local_raw_source_extraction_used":False},
 "counts":{"raw_harvest_rows":73,"total_registry_rows":73,"usable_primary_sources":67,"usable_supporting_reviews":1,"quarantined_sources":5,"corrected_raw_rows":sum(1 for s in sources if s["raw_tuple_corrected"])},
 "sources":sources,
}
OUT.write_text(json.dumps(registry,indent=2,ensure_ascii=False)+"\n")
print(json.dumps(registry["counts"],sort_keys=True))
