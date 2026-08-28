#!/usr/bin/env python3
"""Freeze V12 candidate, source, asset, caption, and encoded-QA lineage."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

SOURCE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-closing-video-20260812T2322K")
ROOT = Path(__file__).resolve().parent
VIDEO_DIR = Path("/Users/duhokim/HermesOps/cockpit/videos")
VIDEO = VIDEO_DIR / "bhu-closing-record-v12-local-20260813T1657K.mp4"
SRT = VIDEO_DIR / "bhu-closing-record-v12-captions-20260813T1657K.srt"
VTT = VIDEO_DIR / "bhu-closing-record-v12-captions-20260813T1657K.vtt"
FREEZE_JSON = SOURCE / "V12_FREEZE_FOR_FULL_THREE_SEAT_GATE.json"
FREEZE_MD = SOURCE / "V12_FREEZE_FOR_FULL_THREE_SEAT_GATE.md"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def item(path: Path, role: str) -> dict:
    if not path.exists():
        raise RuntimeError(f"missing freeze target {path}")
    return {"role": role, "path": str(path), "bytes": path.stat().st_size, "sha256": sha(path)}


def main() -> int:
    qa = json.loads((ROOT / "encoded_qa" / "V12_ENCODED_QA.json").read_text())
    manifest = json.loads((ROOT / "render_manifest.json").read_text())
    ledger = json.loads((ROOT / "V12_GENERATION_SPEND_LEDGER.json").read_text())
    if qa["status"] != "PASS_V12_ENCODED_QA_READY_FOR_THREE_SEAT_VISUAL_GATE" or qa["candidate_sha256"] != sha(VIDEO) or qa["checks_passed"] != qa["checks_total"]:
        raise RuntimeError("encoded QA is not an exact-current all-PASS gate input")
    if manifest["output_sha256"] != sha(VIDEO) or not manifest["subtitle_stream_presence_asserted"]:
        raise RuntimeError("render manifest is not bound to current candidate or subtitle gate")
    if ledger["generation_call_count"] != 10 or ledger["new_calls_permitted_after_ledger"]:
        raise RuntimeError("generation ledger not closed")
    frozen_files = [
        item(SOURCE / "LANA_VISUAL_REDESIGN_SPEC.md", "redesign_authority"),
        item(SOURCE / "NARRATION_DRAFT_V11.md", "base_frozen_narration_authority"),
        item(SOURCE / "STORYBOARD_DRAFT_V11.json", "base_frozen_storyboard_authority"),
        item(SOURCE / "NARRATION_DRAFT_V12.md", "v12_exact_narration_projection"),
        item(SOURCE / "STORYBOARD_DRAFT_V12.json", "v12_storyboard_visual_contract"),
        item(SOURCE / "V12_VISUAL_TEXT_CONTRACT.json", "closed_world_viewer_text_contract"),
        item(SOURCE / "V12_SOURCE_FREEZE_RECEIPT.json", "source_materialization_receipt"),
        item(ROOT / "build_v12_sources.py", "source_builder"),
        item(ROOT / "build_audio_v12.py", "audio_and_caption_builder"),
        item(ROOT / "prepare_v12_generated_assets.py", "generated_asset_auditor_and_cropper"),
        item(ROOT / "render_v12.py", "renderer"),
        item(ROOT / "encoded_qa_v12.py", "encoded_qa_program"),
        item(ROOT / "audit_v12_rendered_text_projection.py", "closed_world_rendered_text_audit_program"),
        item(ROOT / "V12_RENDERED_TEXT_PROJECTION_AUDIT.json", "closed_world_rendered_text_audit_result"),
        item(ROOT / "audio" / "timeline.json", "audio_timing_and_cue_authority"),
        item(ROOT / "audio" / "narration_master.wav", "audio_master"),
        item(ROOT / "captions_v12.srt", "source_exact_srt"),
        item(ROOT / "captions_v12.vtt", "source_exact_vtt"),
        item(ROOT / "V12_GENERATION_SPEND_LEDGER.json", "generation_attempt_and_spend_ledger"),
        item(ROOT / "render_manifest.json", "render_manifest"),
        item(ROOT / "encoded_qa" / "V12_ENCODED_QA.json", "encoded_qa_receipt_json"),
        item(ROOT / "encoded_qa" / "V12_ENCODED_QA.md", "encoded_qa_receipt_md"),
        item(ROOT / "encoded_qa" / "encoded-contact-all11.png", "decoded_candidate_review_contact_sheet"),
        item(VIDEO, "exact_candidate_for_three_seat_gate"),
        item(SRT, "delivery_srt_sidecar"),
        item(VTT, "delivery_vtt_sidecar"),
    ]
    raw_assets = sorted((ROOT / "generated_assets").glob("*.png"))
    prepared_assets = sorted((ROOT / "assets" / "generated_prepared").glob("*.png"))
    raw_rows = [item(path, "raw_generated_attempt_retained_for_audit") for path in raw_assets]
    prepared_rows = [item(path, "prepared_generated_region_retained_for_audit") for path in prepared_assets]
    candidate_usage = manifest["generated_asset_usage"]
    used_names = sorted({name for names in candidate_usage.values() for name in names})
    prepared_names = sorted(path.name for path in prepared_assets)
    if not set(used_names).issubset(prepared_names):
        raise RuntimeError("manifest uses an untracked generated prepared asset")
    if candidate_usage["01"] or candidate_usage["04"] or candidate_usage["05"]:
        raise RuntimeError("Card 01/04/05 final generated-asset usage must be empty")
    v11 = VIDEO_DIR / "bhu-closing-record-v11-local-20260813T1526K.mp4"
    v11_custody = item(v11, "immutable_v11_predecessor_not_part_of_v12")
    if v11_custody["sha256"] != "8e6a4e564ddc25959ecb17c57fe19d898b9f92850b5c83da234ef3d2295f40fb":
        raise RuntimeError("V11 custody drift")
    freeze = {
        "status": "FROZEN_V12_AWAITING_FULL_THREE_SEAT_EXACT_HASH_GATE",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "candidate": {"path": str(VIDEO), "sha256": sha(VIDEO), "bytes": VIDEO.stat().st_size, "duration_seconds": 402.0, "frame_count": 12060, "resolution": "1920x1080", "fps": 30, "streams": ["h264 video", "aac mono audio", "mov_text eng default subtitle"]},
        "three_seat_gate": {"required": ["Lana", "Goru", "Kun"], "state": "NOT_RUN", "prior_version_verdicts_carry_forward": False, "any_hold_blocks": True},
        "local_preflight": {"encoded_qa_status": qa["status"], "checks": f"{qa['checks_passed']}/{qa['checks_total']}", "rendered_text_projection": json.loads((ROOT / "V12_RENDERED_TEXT_PROJECTION_AUDIT.json").read_text())["status"], "visual_preflight": "PASS_FOR_ROUTING_NOT_A_THREE_SEAT_OR_SCIENTIFIC_VERDICT"},
        "caption_gate": {"embedded_stream_present": True, "embedded_stream_extracted": True, "cue_count": 64, "exact_source_payloads_and_timings": True, "srt_sidecar_sha256": sha(SRT), "vtt_sidecar_sha256": sha(VTT), "youtube_serving_state": "NOT_APPLICABLE_PRE_UPLOAD_AND_MUST_BE_CHECKED_SEPARATELY"},
        "generation": {"call_count": ledger["generation_call_count"], "generated_video_calls": ledger["generated_video_call_count"], "monetary_cost": ledger["monetary_cost"], "final_asset_usage_by_card": candidate_usage, "quantitative_cards_with_generated_assets": manifest["quantitative_cards_with_generated_assets"], "card01_final_generated_assets": candidate_usage["01"], "generation_closed": not ledger["new_calls_permitted_after_ledger"]},
        "frozen_files": frozen_files,
        "raw_generated_attempts": raw_rows,
        "prepared_generated_regions": prepared_rows,
        "prepared_regions_used_in_final": used_names,
        "prepared_regions_not_used_in_final_retained_for_audit": sorted(set(prepared_names)-set(used_names)),
        "v11_custody": v11_custody,
        "not_authorized": ["V12 file edits", "re-render", "audio rebuild", "caption rebuild", "new generation", "upload", "publication", "YouTube mutation", "git commit", "git push", "DB write", "deploy", "restart"],
        "note": "This freeze routes exact bytes for independent full three-seat review. It does not self-approve the scientific, visual, or release gate.",
    }
    FREEZE_JSON.write_text(json.dumps(freeze, indent=2, ensure_ascii=False) + "\n")
    lines = [
        "# BHU V12 — full three-seat exact-hash freeze", "", f"Status: `{freeze['status']}`", "",
        "V12 is built and locally encoded-QA clean. This freeze is not a Lana/Goru/Kun verdict and does not authorize upload, publication, re-render, or any mutation.", "",
        "## Exact candidate", "", f"- `{VIDEO}`", f"- SHA-256 `{freeze['candidate']['sha256']}`", f"- {freeze['candidate']['bytes']:,} bytes · 402.000 s · 12,060 frames · 1920×1080 at 30 fps", f"- Streams: H.264 video, AAC mono audio, one default English `mov_text` subtitle stream", "",
        "## Exact caption sidecars", "", f"- SRT `{SRT}`", f"  - SHA-256 `{sha(SRT)}`", f"- VTT `{VTT}`", f"  - SHA-256 `{sha(VTT)}`", "- Embedded stream was extracted from the candidate and matched all 64 exact source payloads/timings.", "- YouTube caption serving is a separate post-upload gate and is not inferred here.", "",
        "## Local QA", "", f"- Encoded QA: `{qa['status']}`", f"- Checks: {qa['checks_passed']}/{qa['checks_total']} PASS", f"- Encoded QA JSON SHA-256 `{sha(ROOT / 'encoded_qa' / 'V12_ENCODED_QA.json')}`", f"- Closed-world rendered-text projection: `{json.loads((ROOT / 'V12_RENDERED_TEXT_PROJECTION_AUDIT.json').read_text())['status']}`", f"- Rendered-text audit JSON SHA-256 `{sha(ROOT / 'V12_RENDERED_TEXT_PROJECTION_AUDIT.json')}`", f"- Decoded 11-card contact sheet SHA-256 `{sha(ROOT / 'encoded_qa' / 'encoded-contact-all11.png')}`", "- Visual preflight: pass for routing only; not scientific acceptance and not a three-seat verdict.", "",
        "## Generation boundary and spend", "", f"- 10 managed FLUX still calls; zero generated-video calls.", "- Monetary amount was not reported by the tool; no cost was invented.", "- Raw accepted/rejected attempts are retained in the ledger.", "- Card 01's generated final-state still was removed from final usage after its pre-closed gate conflicted with reveal chronology.", "- Cards 04 and 05 contain no generated assets; all quantitative geometry is local and deterministic.", "- Generation is closed for these frozen bytes.", "",
        "## Required full gate", "", "- Lana: picture-first redesign, exhaustive keep lists, pacing, assertion-heading retirement, metaphor continuity, all-card blur test.", "- Goru: mechanical exact-hash, stream/caption, text-deletion, generated-boundary, no-95.4-terminus, and artifact-lineage audit.", "- Kun: reproducibility, claim safety, rendering/encoding, quantitative geometry, and audience-projection audit.", "- Every seat must bind the candidate, SRT, VTT, storyboard, narration, visual-text contract, generation ledger, renderer, and encoded-QA hashes.", "- Any HOLD blocks. No V11 or earlier verdict carries forward.", "",
        "## V11 custody", "", f"- V11 remains untouched at SHA-256 `{v11_custody['sha256']}`.", "- V11 is not a V12 review target and is not superseded by this freeze until the full V12 gate decides.", "",
        "## Freeze manifest", "", f"- JSON: `{FREEZE_JSON}`", "- The JSON enumerates hashes for all exact review files plus all raw and prepared generated assets.", "",
        "## Forbidden next actions without separate approval", "", "No V12 edits, re-render, audio/caption rebuild, new generation, upload, publication, YouTube mutation, git commit/push, DB write, deploy, or restart.",
    ]
    FREEZE_MD.write_text("\n".join(lines) + "\n")
    print(json.dumps({"status": freeze["status"], "candidate_sha256": freeze["candidate"]["sha256"], "frozen_file_count": len(frozen_files), "raw_generation_attempts": len(raw_rows), "prepared_generation_regions": len(prepared_rows), "freeze_json": str(FREEZE_JSON), "freeze_json_sha256": sha(FREEZE_JSON), "freeze_md": str(FREEZE_MD), "freeze_md_sha256": sha(FREEZE_MD)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
