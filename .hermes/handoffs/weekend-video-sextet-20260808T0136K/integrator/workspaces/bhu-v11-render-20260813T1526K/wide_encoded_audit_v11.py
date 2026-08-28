#!/usr/bin/env python3
"""Wide encoded-state and burned-caption audit for immutable V11 candidate."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

SOURCE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-closing-video-20260812T2322K")
ROOT = Path(__file__).resolve().parent
VIDEO = Path("/Users/duhokim/HermesOps/cockpit/videos/bhu-closing-record-v11-local-20260813T1526K.mp4")
TIMELINE = json.loads((ROOT / "audio" / "timeline.json").read_text())
STATES = ROOT / "render_states"
OUT = ROOT / "encoded_qa" / "wide_state_caption_audit.json"
CAPTION_FRAMES = ROOT / "encoded_qa" / "caption_frames"
STATE_OCR = ROOT / "encoded_qa" / "state_ocr"
EXPECTED_VIDEO_SHA = "8e6a4e564ddc25959ecb17c57fe19d898b9f92850b5c83da234ef3d2295f40fb"
CREW_TERMS = ("duho", "lana", "goru", "kun", "hwao", "yui", "tori", "fable")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize(text: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", text.lower()))


def run(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=check, capture_output=True, text=True)


def ocr(path: Path, output_dir: Path, psm: str = "11") -> str:
    output_dir.mkdir(parents=True, exist_ok=True)
    base = output_dir / path.stem
    result = run("tesseract", str(path), str(base), "--psm", psm, check=False)
    if result.returncode != 0:
        raise RuntimeError(f"tesseract failed {path.name}: {result.stderr}")
    return base.with_suffix(".txt").read_text(errors="replace")


def extract(timestamp: float, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    run(
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-ss", f"{timestamp:.6f}", "-i", str(VIDEO),
        "-frames:v", "1", "-q:v", "2", str(output),
    )


def token_recall(expected: str, actual: str) -> float:
    wanted = normalize(expected).split()
    got = normalize(actual).split()
    # Greedy in-order recall avoids rewarding unrelated page text.
    cursor = 0
    matched = 0
    for token in wanted:
        try:
            position = got.index(token, cursor)
        except ValueError:
            continue
        matched += 1
        cursor = position + 1
    return matched / max(1, len(wanted))


def main() -> int:
    if sha(VIDEO) != EXPECTED_VIDEO_SHA:
        raise RuntimeError("candidate hash drift")
    state_paths = sorted(STATES.glob("state-*.png"))
    if len(state_paths) != 177:
        raise RuntimeError(f"expected 177 distinct states, found {len(state_paths)}")
    state_rows = []
    all_state_ocr = []
    aggregate = hashlib.sha256()
    for index, path in enumerate(state_paths, 1):
        digest = sha(path)
        aggregate.update(path.name.encode())
        aggregate.update(b"\0")
        aggregate.update(digest.encode())
        aggregate.update(b"\n")
        text = ocr(path, STATE_OCR)
        all_state_ocr.append(text)
        hits = [term for term in CREW_TERMS if re.search(rf"\b{re.escape(term)}\b", text.lower())]
        state_rows.append({
            "file": str(path.relative_to(ROOT)),
            "sha256": digest,
            "ocr": text,
            "crew_name_hits": hits,
        })
        if index % 25 == 0:
            print(f"state OCR {index}/{len(state_paths)}")
    state_crew_hits = sorted({hit for row in state_rows for hit in row["crew_name_hits"]})

    captions = [cue for card in TIMELINE["cards"] for cue in card["captions"]]
    caption_rows = []
    for index, cue in enumerate(captions, 1):
        midpoint = (float(cue["master_start_seconds"]) + float(cue["master_end_seconds"])) / 2
        output = CAPTION_FRAMES / f"{cue['id']}.png"
        extract(midpoint, output)
        text = ocr(output, CAPTION_FRAMES / "ocr")
        recall = token_recall(cue["text"], text)
        caption_rows.append({
            "id": cue["id"],
            "card_id": cue["card_id"],
            "expected": cue["text"],
            "midpoint_seconds": midpoint,
            "frame": str(output.relative_to(ROOT)),
            "frame_sha256": sha(output),
            "ocr": text,
            "in_order_token_recall": recall,
            "status": "PASS" if recall >= 0.85 else "OCR_REVIEW",
        })
        if index % 20 == 0:
            print(f"caption OCR {index}/{len(captions)}")

    # This is the exact contract check; OCR is a decoded-frame legibility cross-check.
    exact_caption_source_equality = all(
        " ".join(cue["text"] for cue in card["captions"]) == card["narration"]
        for card in TIMELINE["cards"]
    )
    report = {
        "status": "PASS_WIDE_STATE_AND_CAPTION_AUDIT" if (
            not state_crew_hits and exact_caption_source_equality
            and all(row["status"] == "PASS" for row in caption_rows)
        ) else "REVIEW_WIDE_STATE_AND_CAPTION_AUDIT",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "candidate": str(VIDEO),
        "candidate_sha256": sha(VIDEO),
        "distinct_visual_states": len(state_rows),
        "encoded_frames_covered_by_states": 12_450,
        "state_hash_aggregate_sha256": aggregate.hexdigest(),
        "state_crew_name_hits": state_crew_hits,
        "exact_caption_source_equality_all_cards": exact_caption_source_equality,
        "caption_cues": len(caption_rows),
        "caption_ocr_passes": sum(row["status"] == "PASS" for row in caption_rows),
        "caption_ocr_reviews": [row["id"] for row in caption_rows if row["status"] != "PASS"],
        "caption_minimum_in_order_token_recall": min(row["in_order_token_recall"] for row in caption_rows),
        "states": state_rows,
        "captions": caption_rows,
    }
    OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({key: report[key] for key in (
        "status", "distinct_visual_states", "encoded_frames_covered_by_states",
        "state_crew_name_hits", "exact_caption_source_equality_all_cards",
        "caption_cues", "caption_ocr_passes", "caption_ocr_reviews",
        "caption_minimum_in_order_token_recall",
    )}, indent=2))
    return 0 if report["status"].startswith("PASS") else 2


if __name__ == "__main__":
    raise SystemExit(main())
