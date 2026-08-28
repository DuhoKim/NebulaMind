#!/usr/bin/env python3
"""Fail-closed content and architecture contract before any render."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
H = ROOT.parents[2]
EXPECTED = {
    "mzr-anchor": {
        "base": H / "integrator/canaries/mzr-anchor-method-overhaul-canary-20260809T1406K/spec.json",
        "ids": ["i05q", "i05u"],
        "quotes": ["The absolute metallicity scale (y-int) varies up to 0.7 dex, depending on the calibration used."],
        "source": ROOT / "sources/ARXIV_0801.1849V1_EXACT_ABSTRACT.txt",
        "closing_tokens": ["reported", "disputed", "adopts no answer", "its finding"],
    },
    "brightend": {
        "base": H / "integrator/canaries/brightend-method-overhaul-canary-20260809T1345K/spec.json",
        "ids": ["i05a", "i05b", "i05u"],
        "quotes": ["Early data from JWST have revealed a bevy of high-redshift galaxy candidates with unexpectedly high stellar masses.", "the most massive galaxy candidates in JWST observations at z∼7-10 lie at the very edge of these limits, indicating an important unresolved issue with the properties of galaxies derived from the observations, how galaxies form at early times in ΛCDM, or within this standard cosmology itself."],
        "source": ROOT / "sources/ARXIV_2208.01611V2_EXACT_ABSTRACT.txt",
        "closing_tokens": ["reported", "unresolved", "contested", "neither claim nor explanation", "its finding"],
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    spec = json.loads((ROOT / "spec.json").read_text())
    lane = spec["slug"]
    config = EXPECTED[lane]
    base = json.loads(config["base"].read_text())
    records = spec["sentences"]
    by_id = {r["id"]: r for r in records}
    checks = {}
    checks["only_expected_literature_ids"] = [r["id"] for r in records if r["section"] == "literature"] == config["ids"]
    actual_quotes = [by_id[i]["text"] for i in config["ids"] if i != "i05u"]
    checks["quotes_exact_in_spec"] = actual_quotes == config["quotes"]
    source_text = config["source"].read_text()
    checks["quotes_exact_in_primary_source_receipt"] = all(q in source_text for q in config["quotes"])
    lana = (ROOT / "sources/LANA_FOUR_LANE_LITERATURE_BEAT_20260810.md").read_text()
    lana_unwrapped = lana.replace("\n> ", " ")
    checks["quotes_exact_in_lana_ruling"] = all(q in lana_unwrapped for q in config["quotes"])
    closing = by_id["i05u"]["text"].lower()
    checks["closing_sentence_safety_pattern"] = all(token in closing for token in config["closing_tokens"])
    checks["card_header_names_claim_type"] = all(by_id[i]["params"].get("study_header") for i in config["ids"] if i != "i05u")
    checks["exact_abstract_citation_on_every_quote"] = all("exact abstract sentence" in by_id[i]["params"].get("source_line", "") for i in config["ids"] if i != "i05u")
    renderer = (ROOT / "render.py").read_text()
    checks["attribution_footer_exact"] = "ATTRIBUTED TO ANOTHER STUDY · NOT THIS VIDEO'S FINDING" in renderer
    checks["running_no_answer_selected"] = "LITERATURE CONTEXT · NO ANSWER SELECTED" in renderer
    checks["closing_card_no_answer_selected"] = "NO ANSWER SELECTED" in renderer
    checks["claimed_disputed_unsettled_card"] = "CLAIMED · DISPUTED · UNSETTLED" in renderer
    checks["serif_quote_face"] = "serif=True" in renderer and "STIXTwoText" in renderer
    checks["symbol_complete_serif_for_unicode_quote"] = lane != "brightend" or (next(r for r in records if r["id"] == "i05b")["params"].get("serif_font") == "STIX Two Math" and "STIXTwoMath.otf" in renderer)
    checks["long_quote_accessible_type_size"] = lane != "brightend" or (next(r for r in records if r["id"] == "i05b")["params"].get("quote_font_size") >= 30 and next(r for r in records if r["id"] == "i05b")["params"].get("caption_font_size") >= 24)
    checks["rail_scan_removed"] = "scan_start" not in renderer and "WHY IT MATTERS" in renderer
    checks["local_active_rail_capsule"] = "max(20,x-145)" in renderer and "min(W-20,x+145)" in renderer
    checks["forbidden_curve_hardening"] = spec.get("forbidden_icon_primitives") == ["curve"] and "forbidden icon primitive: curve" in renderer
    checks["source_freeze_absent"] = spec.get("source_freeze_status") == "ABSENT_FAIL_CLOSED" and not (ROOT / "sources/SOURCE_FREEZE.json").exists()
    checks["video_reportable_false"] = spec.get("video_reportable_now") is False
    base_records = base["sentences"]
    filtered = [r for r in records if r["id"] not in config["ids"]]
    checks["all_predecessor_records_byte_semantics_unchanged"] = filtered == base_records
    checks["new_versioned_filename"] = spec["candidate_filename"] != base["candidate_filename"] and "literature-beat-canary-20260810T" in spec["candidate_filename"]
    checks["fesc_and_census_not_in_spec"] = all(x not in json.dumps(spec).lower() for x in ("fesc-method", "mzr-census-method"))
    report = {"status": "PASS" if all(checks.values()) else "HOLD", "lane": lane, "spec_sha256": sha256(ROOT / "spec.json"), "primary_source_receipt_sha256": sha256(config["source"]), "base_spec_sha256": sha256(config["base"]), "checks": checks, "passed": sum(checks.values()), "total": len(checks)}
    (ROOT / "CONTRACT_QA.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    if report["status"] != "PASS":
        raise RuntimeError("contract HOLD: " + str([k for k, v in checks.items() if not v]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
