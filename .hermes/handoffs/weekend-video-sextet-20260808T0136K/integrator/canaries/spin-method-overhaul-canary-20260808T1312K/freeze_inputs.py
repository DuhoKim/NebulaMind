#!/usr/bin/env python3
"""Copy the exact authority/review inputs into this versioned canary and hash them."""
from __future__ import annotations

import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HANDOFF = ROOT.parents[2]
SPIN_SOURCE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/spin-parity-census-20260805T1922K")
INPUTS = {
    "HWAO_OVERHAUL_ORDER.md": HANDOFF / "HWAO_OVERHAUL_ORDER.md",
    "USER_DIRECTION_OVERHAUL_20260808T1258K.md": HANDOFF / "USER_DIRECTION_OVERHAUL_20260808T1258K.md",
    "REVIEW_BRIEFS.md": HANDOFF / "reviews" / "REVIEW_BRIEFS.md",
    "TORI_USER_WATCHED_ARTIFACT_CORRECTION.md": HANDOFF / "reviews" / "TORI_USER_WATCHED_ARTIFACT_CORRECTION.md",
    "HWAO_NARRATIVE_CORRECTION.md": HANDOFF / "reviews" / "HWAO_NARRATIVE_CORRECTION.md",
    "LANA_OVERHAUL.md": HANDOFF / "reviews" / "LANA_OVERHAUL.md",
    "GORU_OVERHAUL.md": HANDOFF / "reviews" / "GORU_OVERHAUL.md",
    "KUN_OVERHAUL.md": HANDOFF / "reviews" / "KUN_OVERHAUL.md",
    "TORI_OVERHAUL_PREBUILD.md": HANDOFF / "reviews" / "TORI_OVERHAUL.md",
    "SOURCE_FREEZE.json": HANDOFF / "lanes" / "spin" / "SOURCE_FREEZE.json",
    "STATUS.json": HANDOFF / "lanes" / "spin" / "STATUS.json",
    "T1_FUNNEL.json": SPIN_SOURCE / "T1_FUNNEL.json",
    "T1C_COLUMN_INTEGRITY.json": SPIN_SOURCE / "T1C_COLUMN_INTEGRITY.json",
    "AMENDMENT_A4_DRAFT.md": SPIN_SOURCE / "AMENDMENT_A4_DRAFT.md",
    "KUN_FRAME_REVIEW.md": SPIN_SOURCE / "KUN_FRAME_REVIEW.md",
    "WORKFLOW_CHECKLIST.json": SPIN_SOURCE / "WORKFLOW_CHECKLIST.json",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    destination = ROOT / "sources"
    destination.mkdir(parents=True, exist_ok=True)
    records = []
    for name, source in INPUTS.items():
        if not source.is_file():
            raise FileNotFoundError(source)
        target = destination / name
        if target.exists() and sha256(target) != sha256(source):
            raise RuntimeError(f"refusing to overwrite drifted frozen copy: {target}")
        if not target.exists():
            shutil.copy2(source, target)
        records.append(
            {
                "name": name,
                "source_path": str(source),
                "copied_path": str(target.relative_to(ROOT)),
                "bytes": source.stat().st_size,
                "sha256": sha256(source),
                "copy_sha256": sha256(target),
            }
        )
    manifest = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "candidate": ROOT.name,
        "records": records,
    }
    output = ROOT / "source_manifest_v2.json"
    output.write_text(json.dumps(manifest, indent=2) + "\n")
    print(output)
    for record in records:
        print(record["sha256"], record["copied_path"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
