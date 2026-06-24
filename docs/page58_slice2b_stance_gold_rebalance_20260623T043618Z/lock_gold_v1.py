#!/usr/bin/env python3
"""Materialize the LOCKED page-58 stance gold from the v3 draft + Papa's adjudication.
Deterministic merge: final_label := Papa override (by gold_id) else draft_label.
Stage labels derived uniformly from final_label so they never drift."""
import json, hashlib, datetime, collections, pathlib

BASE = pathlib.Path("/Users/duhokim/NebulaMind/NebulaMind/docs/page58_slice2b_stance_gold_rebalance_20260623T043618Z")
DRAFT = BASE / "stance_gold_draft_for_papa_v3.jsonl"
ADJ = BASE / "papa_adjudication_v3.json"
OUT = BASE / "stance_gold_LOCKED_v1.jsonl"
MANIFEST = BASE / "stance_gold_LOCKED_v1.manifest.json"
DRAFT_SHA = "14ae8ea1640662e5005d26536694ca8f179edcbfad1cac9d3c2aeab220d57e4b"

def stage_from_final(lbl):
    if lbl == "unrelated":
        return "unrelated", None
    return "related", lbl  # supports / contradicts / related_different_facet

adj = json.loads(ADJ.read_text())
overrides = {d["gold_id"]: d["final_label"] for d in adj["decisions"]}

rows = []
for line in DRAFT.read_text().splitlines():
    line = line.strip()
    if not line:
        continue
    r = json.loads(line)
    gid = r["gold_id"]
    if gid in overrides:
        r["final_label"] = overrides[gid]
        r["label_source"] = "papa"
    else:
        r["final_label"] = r.get("draft_label")
    s1, s2 = stage_from_final(r["final_label"])
    r["final_stage1_label"] = s1
    r["final_stage2_label"] = s2
    rows.append(r)

OUT.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
locked_sha = hashlib.sha256(OUT.read_bytes()).hexdigest()
hist = collections.Counter(r["final_label"] for r in rows)
hist1 = collections.Counter(r["final_stage1_label"] for r in rows)

manifest = {
    "locked_artifact": "stance_gold_LOCKED_v1.jsonl",
    "locked_sha256": locked_sha,
    "locked_by": "Papa (Duho Kim); materialized + relayed by HwaO",
    "locked_at_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "source_draft": "stance_gold_draft_for_papa_v3.jsonl",
    "source_draft_sha256": DRAFT_SHA,
    "adjudication": "papa_adjudication_v3.json",
    "papa_overrides": overrides,
    "final_label_histogram": dict(hist),
    "final_stage1_histogram": dict(hist1),
    "total_rows": len(rows),
    "contradicts_handling": "n=1 (stance2b-001) -> SENTINEL only; excluded from scored P/R/F1 (n=1 meaningless). Documented corpus limit: slice-2b exhausted (see contradicts_mine_20260623T062201Z/papa_adjudication_contradicts_mine.json).",
    "excluded_from_set": "mine-024, mine-066 (Papa-certified related_different_facet, expert-ambiguous, kept out of scored set).",
    "nm_head": "4ba9675",
    "containment": {"db_write_count": 0, "paid_lane_touched": False, "page57_swapped": False},
}
MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False))

print("LOCKED_SHA", locked_sha)
print("final_label", dict(hist))
print("stage1", dict(hist1))
print("total", len(rows))
print("overrides", overrides)
expected = {"supports": 21, "contradicts": 1, "related_different_facet": 88, "unrelated": 19}
print("MATCH_EXPECTED", dict(hist) == expected and len(rows) == 129)
