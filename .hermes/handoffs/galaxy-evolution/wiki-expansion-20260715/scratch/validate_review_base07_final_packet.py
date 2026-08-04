import hashlib
import json
import re
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
PACKET = AREA / "area_review_07_peroux_howk_2020_DR_PACKET.md"
RAW = AREA / "area_review_07_peroux_howk_2020_DR_RAW_PACKET.md"
REG = AREA / "area_review_07_peroux_howk_2020_CURATED_SOURCE_REGISTRY.json"
OUT = AREA / "area_review_07_peroux_howk_2020_VALIDATION.json"
s = PACKET.read_text(); r = json.loads(REG.read_text()); failures=[]
def check(name, ok, detail):
    if not ok: failures.append({"check":name,"detail":detail})
counts=r["counts"]
check("registry_status",r.get("status")=="PASS_COMPOSITE_IDS_AND_REVIEW_MEMBERSHIP",r.get("status"))
check("primary_count",counts.get("usable_primary_sources")==40,counts)
check("supporting_count",counts.get("usable_supporting_reviews")==4,counts)
check("quarantine_count",counts.get("quarantined_sources")==3,counts)
check("claim_counts",(len(re.findall(r"\| REV07-E\d{2} \|",s)),len(re.findall(r"\| REV07-D\d{2} \|",s)),len(re.findall(r"\| REV07-N\d{2} \|",s)),len(re.findall(r"\| REV07-U\d{2} \|",s)))==(12,8,8,6),"expected 12/8/8/6")
claim=s[s.index("## 2."):s.index("## 6.")]
claim_refs=set(re.findall(r"\[(REV07-P\d{3})\]",claim)); usable={x["key"] for x in r["sources"] if x["source_status"]=="PASS"}; quarantined={x["key"] for x in r["sources"] if x["source_status"]!="PASS"}
check("claim_refs_resolve",claim_refs<=usable,sorted(claim_refs-usable))
check("quarantine_not_load_bearing",not (claim_refs & quarantined),sorted(claim_refs & quarantined))
harvest=s[s.index("## 6."):s.index("## 7.")]; ledger=s[s.index("## 8."):]
check("harvest_primary_rows",len(re.findall(r"^\[REV07-P\d{3}\].*role=(?!supporting_review)",harvest,re.M))==40,"primary harvest row count")
check("harvest_supporting_rows",len(re.findall(r"^\[REV07-P\d{3}\].*role=supporting_review",harvest,re.M))==4,"supporting harvest row count")
check("ledger_rows",len(re.findall(r"^\[REV07-(?:R00|P\d{3})\]",ledger,re.M))==45,"review plus 44 usable sources")
check("ledger_complete",all(f"[{k}]" in ledger for k in usable),"usable source absent from ledger")
check("review_identity",all(x in s for x in ["10.1146/annurev-astro-021820-120014","2011.01935","2020ARA&A..58..363P"]),"review DOI/arXiv/ADS")
check("raw_hash",hashlib.sha256(RAW.read_bytes()).hexdigest() in s,"raw custody hash")
check("terminal_marker",s.rstrip().endswith("REVIEW_BASE_07_DR_COMPLETE_REFERENCE_ONLY"),"terminal marker")
check("temporal_boundary",all(x["year"]<=2020 for x in r["sources"] if x["source_status"]=="PASS"),"usable source later than 2020")
check("no_frb_load_bearing","FRB" not in claim and "Fast Radio" not in claim,"uncited FRB result in canonical claims")
check("dnu_present","UNCITED_NOT_USABLE" in s and all(f"[{k}]" in s[s.index("## 7."):s.index("## 8.")] for k in quarantined),"quarantine coverage")
status="PASS" if not failures else "FAIL"; result={"status":status,"failed_checks":failures,"packet_sha256":hashlib.sha256(PACKET.read_bytes()).hexdigest(),"counts":{"established":12,"debates":8,"measurements":8,"unknowns":6,"usable_primary":40,"supporting_reviews":4,"quarantined":3,"claim_source_keys":len(claim_refs),"ledger_rows":45},"raw_packet_sha256":hashlib.sha256(RAW.read_bytes()).hexdigest(),"registry_sha256":hashlib.sha256(REG.read_bytes()).hexdigest()}; OUT.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n"); print(json.dumps(result,sort_keys=True)); raise SystemExit(0 if status=="PASS" else 1)
