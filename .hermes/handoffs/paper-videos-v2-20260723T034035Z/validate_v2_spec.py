#!/usr/bin/env python3
"""Validate source, structure, semantics, and metadata of the V2 paper spec."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

BASE = Path(__file__).resolve().parent
SPEC = json.loads((BASE/"paper_video_specs_v2.json").read_text())
FREEZE = json.loads((BASE/"source_freeze.json").read_text())
V1_PATH = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-videos-20260722T121412Z/paper_video_specs.json")
V1 = json.loads(V1_PATH.read_text())
SOURCE_DIR = BASE/"sources"

CRITICAL = {
    "z9-metallicity": ["five strictly unlensed", "one fifth", "g n z eleven", "roughly fifteen hundred", "not a detection"],
    "scaling-relations": ["four hundred ninety thousand", "two hundred thousand", "nearly ninety times", "forty percent", "selection"],
    "massive-abundance": ["factor of two point seven", "zero point two eight dex", "one hundredfold", "does not confirm"],
    "mzr-framework": ["factor of five", "twenty percent", "thirty to sixty percent", "not a new metallicity measurement"],
    "tng-validation": ["one point three to one point six", "zero point nine to one point zero", "not significant", "scale-limited"],
}


def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):
            h.update(chunk)
    return h.hexdigest()


def words(text: str) -> int:
    return len(re.findall(r"[a-z0-9]+", text.lower().replace("’", "'")))


def resolve_citation(label: str) -> tuple[Path,int,int]:
    match=re.fullmatch(r"([^:]+):(\d+)-(\d+)",label)
    if not match:
        raise RuntimeError(f"invalid citation {label}")
    filename,start,end=match.group(1),int(match.group(2)),int(match.group(3))
    path=V1_PATH if filename=="paper_video_specs.json" else SOURCE_DIR/filename
    if not path.is_file():
        raise RuntimeError(f"citation source missing {path}")
    total=len(path.read_text().splitlines())
    if not (1<=start<=end<=total):
        raise RuntimeError(f"citation out of range {label} total={total}")
    return path,start,end

old_titles={paper["youtube_title"] for paper in V1["papers"]}
rows=[]
seen=set()
for paper in SPEC["papers"]:
    key=paper["key"]
    if key in seen:
        raise RuntimeError(f"duplicate key {key}")
    seen.add(key)
    title=paper["youtube_title"]
    if title in old_titles or len(title)>100:
        raise RuntimeError(f"unsafe title {title}")
    if len(paper["description"])>5000 or "not validated" not in paper["description"] or "not journal or human peer review" not in paper["description"]:
        raise RuntimeError(f"description boundary failed {key}")
    scenes=paper["scenes"]
    counts=[words(scene["narration"]) for scene in scenes]
    if len(scenes)!=8 or any(not 26<=count<=52 for count in counts) or not 250<=sum(counts)<=340:
        raise RuntimeError(f"narration structure failed {key}: {counts}")
    full=" ".join(scene["narration"] for scene in scenes).lower()
    for phrase in CRITICAL[key]:
        if phrase not in full:
            raise RuntimeError(f"{key}: missing critical phrase {phrase}")
    final=scenes[-1]["narration"].lower()
    if not all(term in final for term in ["machine-generated","not validated","journal","human peer review"]):
        raise RuntimeError(f"{key}: spoken status boundary failed")
    citations=[]
    for scene in scenes:
        if not 2<=len(scene["cards"])<=3 or not scene.get("callout"):
            raise RuntimeError(f"{key}: card/callout structure failed")
        for citation in scene.get("source_lines",[]):
            path,start,end=resolve_citation(citation)
            citations.append({"citation":citation,"path":str(path),"start":start,"end":end})
    if not citations:
        raise RuntimeError(f"{key}: no citations")
    rows.append({"key":key,"scene_words":counts,"total_words":sum(counts),"title_chars":len(title),"description_chars":len(paper["description"]),"citations":len(citations),"critical_phrases":"PASS","status_boundary":"PASS"})

freeze_rows={row["key"]:row for row in FREEZE["sources"]}
if not FREEZE.get("all_live_pdfs_match_v1_freeze"):
    raise RuntimeError("source freeze did not record live/V1 equality")
for key,row in freeze_rows.items():
    path=SOURCE_DIR/f"{key}.pdf"
    if sha256(path)!=row["sha256"]:
        raise RuntimeError(f"source freeze drift {key}")

result={
    "marker":"NEBULAMIND_FIVE_PAPER_V2_SCRIPT_QA_PASS",
    "completed_at_utc":datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "paper_count":len(rows),
    "source_hashes":"PASS",
    "metadata_uniqueness":"PASS",
    "rows":rows,
}
(BASE/"script_qa.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n")
print(json.dumps(result,indent=2,ensure_ascii=False))
