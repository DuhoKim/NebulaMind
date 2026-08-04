#!/usr/bin/env python3
"""Use the already-authorized single wording retry for narration vo_06.

This repair exists because three independent managed transcribers found an
extra spoken token after "encyclopedia" in the first vo_06 attempt. It also
reclassifies the selected vo_07 attempt after domain-aware transcript
normalization (speech recognizers write "nebula mind dot net" as
"NebulaMind.net"). No shared ledger is opened or written directly.
"""
from __future__ import annotations

import importlib.util
import json
import os
import shutil
import time
from pathlib import Path
from typing import Any

PACKET = Path(__file__).resolve().parents[1]
RUNNER = PACKET / "canaries" / "yui_flow_narration_batch_02_07.py"
_spec = importlib.util.spec_from_file_location("narration_runner", RUNNER)
assert _spec and _spec.loader
M = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(M)


def refresh_attempt(spoken_line: str, attempt: dict[str, Any]) -> None:
    analysis = attempt["analysis"]
    full_wording = M.assess_wording(spoken_line, analysis["full_transcript"])
    mid_wording = M.assess_wording(spoken_line, analysis["mid_transcript"])
    if mid_wording["token_similarity"] > full_wording["token_similarity"]:
        best_wording = mid_wording
        analysis["best_transcript"] = analysis["mid_transcript"]
        analysis["best_transcript_source"] = "mid"
    else:
        best_wording = full_wording
        analysis["best_transcript"] = analysis["full_transcript"]
        analysis["best_transcript_source"] = "full"
    analysis["full_wording"] = full_wording
    analysis["mid_wording"] = mid_wording
    analysis["wording_pass"] = bool(best_wording["pass"])
    voice_pass = bool(analysis["reference_comparison"]["voice_consistency_pass"])
    analysis["quality_pass"] = bool(analysis["wording_pass"] and voice_pass and analysis["media"].get("audio_codec"))
    analysis["quality_score"] = round(
        (100.0 if analysis["wording_pass"] else 0.0)
        + 10.0 * float(best_wording["token_similarity"])
        + float(analysis["reference_comparison"]["timbre_signature_cosine"])
        + (1.0 if voice_pass else 0.0),
        4,
    )


def main() -> int:
    manifest = json.loads(M.MANIFEST.read_text())
    by_clip = {row["clip_num"]: row for row in manifest["clips"]}
    clip6 = by_clip[6]
    if clip6["attempt_count"] != 1 or clip6["retry_used"]:
        raise RuntimeError("vo_06 retry is no longer available or was already used")
    final = Path(clip6["path"])
    if not final.exists() or M.sha256_file(final) != clip6["sha256"]:
        raise RuntimeError("vo_06 selected artifact drift before retry")

    # Refresh every recorded attempt under the corrected exact-wording rules.
    for clip in manifest["clips"]:
        for attempt in clip["attempts"]:
            refresh_attempt(clip["spoken_line"], attempt)
        selected = next(row for row in clip["attempts"] if row["attempt"] == clip["selected_attempt"])
        clip["quality_gate_pass"] = selected["analysis"]["quality_pass"]

    # Persist the exact reason for consuming vo_06's one authorized retry.
    clip6["post_batch_transcription_recheck"] = {
        "attempt_1": {
            "whisper-1": "The result is a living encyclopedia, TEGA, evidence-linked, self-correcting and always growing.",
            "gpt-4o-mini-transcribe": "The result is a living encyclopedia, tethered, evidence-linked, self-correcting, and always growing.",
            "gpt-4o-transcribe": "The result is a living encyclopedia, Tedia, evidence-linked, self-correcting, and always growing.",
        },
        "verdict": "three managed transcribers agree on an extra utterance after encyclopedia; consume the one authorized wording retry",
    }
    by_clip[7]["post_batch_transcription_recheck"] = {
        "selected_attempt_1": {
            "whisper-1": "The cosmos, mapped, sourced, and understood by AI. Explore it at nebulamind.net.",
            "gpt-4o-mini-transcribe": "The cosmos, mapped, sourced, and understood by AI. Explore it at nebulamind.net.",
            "gpt-4o-transcribe": "The cosmos, mapped, sourced, and understood by AI. Explore it at NebulaMind.net",
        },
        "verdict": "exact semantic wording; recognizers normalize spoken nebula mind dot net to the written domain",
    }
    manifest["status"] = "in_progress_vo06_authorized_retry"
    manifest["updated_utc"] = M.utc_now()
    M.write_manifest(manifest)

    run_id = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    work_dir = Path("/tmp") / f"yui-flow-narration-vo06-retry-{run_id}-{os.getpid()}"
    work_dir.mkdir(parents=True, exist_ok=False)
    reference = M.analyze_reference(work_dir)
    rows = M.parse_brief()
    retry = M.generate_attempt(
        6,
        2,
        rows[6]["prompt"],
        rows[6]["spoken_line"],
        reference["features"],
        work_dir,
    )
    clip6["attempts"].append(retry)
    selected = M.choose_attempt(clip6["attempts"])
    selected_attempt = selected["attempt"]

    if selected_attempt == 2:
        M.REJECTED_DIR.mkdir(parents=True, exist_ok=True)
        rejected = M.REJECTED_DIR / "vo_06_attempt1_not_selected.mp4"
        if rejected.exists():
            raise RuntimeError(f"refusing to overwrite {rejected}")
        shutil.move(str(final), str(rejected))
        old = clip6["attempts"][0]
        old["artifact_rejected_path"] = str(rejected)
        old["artifact_rejected_sha256"] = M.sha256_file(rejected)
        retry_path = Path(retry.pop("artifact_temp"))
        if final.exists():
            raise RuntimeError(f"refusing to overwrite {final}")
        shutil.move(str(retry_path), str(final))
    else:
        retry_path = Path(retry.pop("artifact_temp"))
        M.REJECTED_DIR.mkdir(parents=True, exist_ok=True)
        rejected = M.REJECTED_DIR / "vo_06_attempt2_not_selected.mp4"
        if rejected.exists():
            raise RuntimeError(f"refusing to overwrite {rejected}")
        shutil.move(str(retry_path), str(rejected))
        retry["artifact_rejected_path"] = str(rejected)
        retry["artifact_rejected_sha256"] = M.sha256_file(rejected)

    clip6["attempt_count"] = 2
    clip6["retry_used"] = True
    clip6["selected_attempt"] = selected_attempt
    clip6["quality_gate_pass"] = selected["analysis"]["quality_pass"]
    clip6["sha256"] = M.sha256_file(final)
    manifest["submit_count"] = int(manifest["submit_count"]) + 1
    manifest["expected_credit_cost"] = int(manifest["submit_count"]) * 100
    failures = [row["clip_num"] for row in manifest["clips"] if not row["quality_gate_pass"]]
    manifest["quality_failure_clips"] = failures
    manifest["status"] = "completed" if not failures else "completed_with_quality_failures"
    manifest["completed_utc"] = M.utc_now()
    manifest["updated_utc"] = M.utc_now()
    M.write_manifest(manifest)
    print(
        json.dumps(
            {
                "status": manifest["status"],
                "quality_failure_clips": failures,
                "vo06_selected_attempt": selected_attempt,
                "vo06_transcript": selected["analysis"]["best_transcript"],
                "vo06_quality_pass": selected["analysis"]["quality_pass"],
                "vo07_quality_pass": by_clip[7]["quality_gate_pass"],
                "submit_count": manifest["submit_count"],
                "expected_credit_cost": manifest["expected_credit_cost"],
            },
            sort_keys=True,
        ),
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
