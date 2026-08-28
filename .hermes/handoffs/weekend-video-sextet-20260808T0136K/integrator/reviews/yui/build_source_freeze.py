#!/usr/bin/env python3
"""Build review-only source and artifact custody freeze."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
HANDOFFS = REPO / ".hermes/handoffs"
OUT = HANDOFFS / "weekend-video-sextet-20260808T0136K/integrator/reviews/yui/SOURCE_FREEZE.json"

STORYBOARDS = {
    "fesc-zsweep-photon-budget": HANDOFFS / "fesc-zsweep-merged-paper-20260804T1040K/storyboard_fesc_zsweep.json",
    "spin-parity-census": HANDOFFS / "spin-parity-census-20260805T1922K/storyboard_spin_parity.json",
    "mzr-archive-census": HANDOFFS / "mzr-archive-census-20260805T1857K/storyboard_mzr_census.json",
    "c41-brightend-uvlf-archival-gap": HANDOFFS / "c41-trackb-shape1-uvlf-20260804/storyboard_c41_gap.json",
    "c41-highz-mzr-calibration-anchored": HANDOFFS / "c41-trackb-shape2-mzr-20260804T1452K/storyboard_c41_anchor_gap.json",
}

PUBLIC = {
    slug: REPO / "frontend/public/videos" / f"{slug}.mp4"
    for slug in STORYBOARDS
}
CANDIDATES = {
    "spin-parity-census-narrated-20260808T0149": Path("/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4"),
    "mzr-archive-census-narrated-20260808T0155": Path("/Users/duhokim/HermesOps/cockpit/videos/mzr-archive-census-narrated-20260808T0155.mp4"),
}
STATUS_EVIDENCE = {
    "weekend-run-plan": HANDOFFS / "video-structure-consult-20260807T1700K/WEEKEND_RUN_PLAN_20260808.md",
    "hwao-status": HANDOFFS / "weekend-video-sextet-20260808T0136K/status.json",
    "hwao-order": HANDOFFS / "weekend-video-sextet-20260808T0136K/HWAO_WEEKEND_ORDER.md",
    "coordination-update": HANDOFFS / "weekend-video-sextet-20260808T0136K/COORDINATION_UPDATE.md",
    "fesc-referee": HANDOFFS / "fesc-zsweep-merged-paper-20260804T1040K/KUN_MERGED_REFEREE.md",
    "fesc-merit-panel": HANDOFFS / "fesc-zsweep-merged-paper-20260804T1040K/MERIT_PANEL_MERGED.md",
    "spin-frame-review": HANDOFFS / "spin-parity-census-20260805T1922K/KUN_FRAME_REVIEW.md",
    "mzr-science-ruling": HANDOFFS / "mzr-archive-census-20260805T1857K/LANA_MZR_SCIENCE_RULING.md",
    "uvlf-rereferee": HANDOFFS / "c41-trackb-shape1-uvlf-20260804/MIRU_GAP_PAPER_REREFEREE.md",
    "c41-mzr-referee": HANDOFFS / "c41-trackb-shape2-mzr-20260804T1452K/KUN_ANCHORGAP_REFEREE.md",
}
CONSULTS = {
    "yui": HANDOFFS / "video-scipres-consult-20260808T0108K/YUI_SCIPRES_REVIEW.md",
    "goru": HANDOFFS / "video-scipres-consult-20260808T0108K/GORU_SCIPRES_REVIEW.md",
    "lana": HANDOFFS / "video-scipres-consult-20260808T0108K/LANA_SCIPRES_REVIEW.md",
}


def file_record(path: Path) -> dict:
    record = {"path": str(path), "exists": path.is_file()}
    if path.is_file():
        data = path.read_bytes()
        record.update({"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
    return record


def resolve_ref(base: Path, raw: str) -> Path | None:
    token = raw.strip().split(" §", 1)[0].split("#", 1)[0]
    if " + " in token or not token:
        return None
    candidate = Path(token)
    options = [candidate] if candidate.is_absolute() else [base / candidate, REPO / candidate]
    for option in options:
        resolved = option.resolve()
        if resolved.is_file():
            return resolved
    return None


storyboards = {}
referenced = {}
for slug, path in STORYBOARDS.items():
    data = json.loads(path.read_text())
    refs = []
    for index, card in enumerate(data.get("cards", []), start=1):
        for field in ("source", "figure"):
            raw = card.get(field)
            if not raw:
                continue
            resolved = resolve_ref(path.parent, str(raw))
            item = {"card": index, "field": field, "raw": str(raw), "resolved": str(resolved) if resolved else None}
            if resolved:
                key = str(resolved)
                if key not in referenced:
                    referenced[key] = file_record(resolved)
            refs.append(item)
    storyboards[slug] = {**file_record(path), "card_count": len(data.get("cards", [])), "references": refs}

reportability = {
    "spin-parity-census": {
        "source_status": "GATE: PASS; freeze decision — DUHO",
        "video_reportable_now": None,
        "review_disposition": "UNRESOLVED",
        "reason": "Weekend run plan lines 29 and 33 require Duho's freeze decision; no explicit video_reportable_now record was found. Do not infer approval from GATE: PASS or from an existing candidate.",
    },
    "mzr-archive-census": {
        "source_status": "GATE: PASS; freeze decision — DUHO",
        "video_reportable_now": None,
        "review_disposition": "UNRESOLVED",
        "reason": "Weekend run plan lines 30 and 33 require Duho's freeze decision; no explicit video_reportable_now record was found.",
    },
    "c41-highz-mzr-calibration-anchored": {
        "source_status": "GATE: APPROVED; freeze decision — DUHO",
        "video_reportable_now": None,
        "review_disposition": "UNRESOLVED",
        "reason": "Weekend run plan lines 31 and 33 require Duho's freeze decision; no explicit video_reportable_now record was found. The read referee report itself says MINOR, so the plan's APPROVED label is not a substitute for a freeze receipt.",
    },
    "fesc-zsweep-photon-budget": {
        "source_status": "crew-owned; referee MINOR followed by a post-revision merit panel",
        "video_reportable_now": None,
        "review_disposition": "UNRESOLVED",
        "reason": "No explicit video_reportable_now or final human freeze receipt was found in the read source/status records. Review can audit existing media but cannot authorize a new candidate.",
    },
    "c41-brightend-uvlf-archival-gap": {
        "source_status": "REFEREE VERDICT: ESTABLISHED with two wording findings remaining",
        "video_reportable_now": None,
        "review_disposition": "UNRESOLVED",
        "reason": "The source verdict supports the central archival-gap claim but does not explicitly authorize video reportability; two wording findings remain and no video_reportable_now receipt was found.",
    },
}

payload = {
    "scope": "review custody only; no candidate, shared renderer, shared source, public media, or TTS mutation",
    "renderer": file_record(REPO / "tools/nm_paper_video.py"),
    "storyboards": storyboards,
    "referenced_sources_and_figures": list(referenced.values()),
    "public_mp4s": {name: file_record(path) for name, path in PUBLIC.items()},
    "authoritative_candidates_seen": {name: file_record(path) for name, path in CANDIDATES.items()},
    "status_evidence": {name: file_record(path) for name, path in STATUS_EVIDENCE.items()},
    "consults": {name: file_record(path) for name, path in CONSULTS.items()},
    "reportability": reportability,
    "hard_gate": "All five reportability fields remain UNRESOLVED because no explicit video_reportable_now record was found; this review does not infer a human freeze or publication authorization.",
}
OUT.write_text(json.dumps(payload, indent=2) + "\n")
print(f"wrote {OUT}")
print(f"referenced files frozen: {len(referenced)}")
