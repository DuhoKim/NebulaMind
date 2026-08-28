#!/usr/bin/env python3
"""Freeze the exact V13 source, pre-render gate, render, captions, and encoded-QA lineage."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

SOURCE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-closing-video-20260812T2322K")
ROOT = Path(__file__).resolve().parent
VIDEO_DIR = Path("/Users/duhokim/HermesOps/cockpit/videos")
VIDEO = VIDEO_DIR / "bhu-closing-record-v13-local-20260813T0932Z.mp4"
SRT = VIDEO_DIR / "bhu-closing-record-v13-captions-20260813T0932Z.srt"
VTT = VIDEO_DIR / "bhu-closing-record-v13-captions-20260813T0932Z.vtt"
FREEZE_JSON = SOURCE / "V13_FREEZE_FOR_UNLISTED_RELEASE.json"
FREEZE_MD = SOURCE / "V13_FREEZE_FOR_UNLISTED_RELEASE.md"
EXPECTED_PACKET = {
    "STORYBOARD_DRAFT_V13.json": "4df53ed7d5f0e38dfe54570f7761bb9e6affe4dd3a686e66f3da852074fad817",
    "V13_VISUAL_TEXT_CONTRACT.json": "c7557b98853655355a5ce96daf27e1d385c561db5657309dfa3bbc696e551361",
    "NARRATION_DRAFT_V12.md": "178ffe4ada125668c8ff84bc156adee7820954591f9781adb7101aac562d80da",
    "V13_CONTRACT_REPAIR_RECEIPT.json": "2ae7114a45f5dd9a5aeecc45719a2c2ab25d5637df049b6f3fcc6dd30228d339",
    "V13_REPAIR_A_EXACT_AUTHORITY.md": "35e5fa1e90f8d4e5544b3aab4172e6a894b3c5a5df31d9e954a741991484056b",
    "V13_PRE_RENDER_GATE_RECEIPT.json": "bc67fc5b6c4dbe7c015cea4e6c00d2e973f42bf36dd478b84e115b288e697bea",
}
EXPECTED_SEATS = {
    "LANA_GATE_V13.md": ("LANA_V13_EXACT_HASH_PASS", "f4e1c44dc180d5c4864feaa970437b5100c0da2836ce051ad4c014bd70474892"),
    "GORU_GATE_V13.md": ("GORU_V13_EXACT_HASH_PASS", "5a2abe3fd56baab274dde4f9beb7f70481e467e8c7a92e3ead8ae2030b855623"),
    "KUN_GATE_V13.md": ("KUN_V13_EXACT_HASH_PASS", "897aa8f98d3440f0cfa488a9c12d1061f2e09c691a3f12f388c7859e87b05d85"),
}
EXPECTED_DELIVERY = {
    "video": "060764c04ba095637cb484237064d501e097b1c326d7bf8b389a22292f96d9c2",
    "srt": "8966f66a3d74c9b0e0c80c7d1aff9651bf6a5ee7267d72347f75f86d3ad7d8d5",
    "vtt": "e893244f46e9bd377defc81d4afeb37a32a211adafee776103baa32790874f13",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def item(path: Path, role: str) -> dict:
    if not path.exists():
        raise RuntimeError(f"missing freeze target {path}")
    return {"role": role, "path": str(path), "bytes": path.stat().st_size, "sha256": sha(path)}


def main() -> int:
    for name, expected in EXPECTED_PACKET.items():
        actual = sha(SOURCE / name)
        if actual != expected:
            raise RuntimeError(f"V13 frozen packet drift {name}: {actual}")
    for name, (marker, expected) in EXPECTED_SEATS.items():
        path = SOURCE / name
        if sha(path) != expected or marker not in path.read_text():
            raise RuntimeError(f"V13 seat receipt drift {name}")
    if {"video": sha(VIDEO), "srt": sha(SRT), "vtt": sha(VTT)} != EXPECTED_DELIVERY:
        raise RuntimeError("V13 delivery artifact drift")

    gate = json.loads((SOURCE / "V13_PRE_RENDER_GATE_RECEIPT.json").read_text())
    qa = json.loads((ROOT / "encoded_qa" / "V13_ENCODED_QA.json").read_text())
    manifest = json.loads((ROOT / "render_manifest.json").read_text())
    projection = json.loads((ROOT / "V13_RENDERED_TEXT_PROJECTION_AUDIT.json").read_text())
    visual = json.loads((ROOT / "V13_DECODED_FRAME_VISUAL_PREFLIGHT.json").read_text())
    ledger = json.loads((ROOT / "V12_GENERATION_SPEND_LEDGER.json").read_text())
    if gate["status"] != "PASS_V13_PRE_RENDER_THREE_SEAT_EXACT_HASH_GATE" or any(seat["verdict"] != "PASS" for seat in gate["seats"].values()):
        raise RuntimeError("pre-render three-seat exact-current gate is not all PASS")
    if qa["status"] != "PASS_V13_ENCODED_QA_READY_FOR_FREEZE" or qa["candidate_sha256"] != sha(VIDEO) or qa["checks_passed"] != qa["checks_total"]:
        raise RuntimeError("V13 encoded QA is not exact-current all-PASS")
    decoded_rows = qa["decoded_delivered_audio_wpm"]["cards"]
    if len(decoded_rows) != 11 or not all(135 <= row["decoded_audio_wpm"] <= 150 and row["inside_135_150_band"] for row in decoded_rows):
        raise RuntimeError("V13 decoded delivered-audio WPM gate failed")
    if manifest["output_sha256"] != sha(VIDEO) or not manifest["subtitle_stream_presence_asserted"]:
        raise RuntimeError("V13 manifest is not bound to the current candidate/subtitle gate")
    if projection["status"] != "PASS_EXACT_CLOSED_WORLD_RENDERED_TEXT_PROJECTION":
        raise RuntimeError("V13 rendered-text projection is not PASS")
    if visual["status"] != "PASS_V13_DECODED_FRAME_VISUAL_PREFLIGHT" or visual["candidate_sha256"] != sha(VIDEO):
        raise RuntimeError("V13 decoded-frame visual preflight is not exact-current PASS")
    if ledger["generation_call_count"] != 10 or ledger["generated_video_call_count"] != 0 or ledger["new_calls_permitted_after_ledger"]:
        raise RuntimeError("generation ledger is not closed")
    if manifest["quantitative_cards_with_generated_assets"]:
        raise RuntimeError("generated asset present in quantitative card")

    frozen_files = [
        item(SOURCE / "LANA_VISUAL_REDESIGN_SPEC.md", "redesign_authority"),
        item(SOURCE / "DETERMINISTIC_DIAGRAM_SPEC_V8.md", "no_terminus_semantic_authority"),
        item(SOURCE / "KUN_GATE_V8.md", "nine_term_enumeration_supporting_authority"),
        item(SOURCE / "V13_REPAIR_A_EXACT_AUTHORITY.md", "direct_exact_repair_authority"),
        item(SOURCE / "NARRATION_DRAFT_V11.md", "base_frozen_narration_authority"),
        item(SOURCE / "STORYBOARD_DRAFT_V11.json", "base_frozen_storyboard_authority"),
        item(SOURCE / "NARRATION_DRAFT_V12.md", "v13_exact_reused_narration"),
        item(SOURCE / "STORYBOARD_DRAFT_V12.json", "v12_predecessor_storyboard"),
        item(SOURCE / "V12_VISUAL_TEXT_CONTRACT.json", "v12_predecessor_text_contract"),
        item(SOURCE / "STORYBOARD_DRAFT_V13.json", "v13_exact_storyboard_and_render_contract"),
        item(SOURCE / "V13_VISUAL_TEXT_CONTRACT.json", "v13_closed_world_viewer_text_contract"),
        item(SOURCE / "V13_CONTRACT_REPAIR_RECEIPT.json", "v13_source_materialization_receipt"),
        item(SOURCE / "V13_PRE_RENDER_THREE_SEAT_GATE_BRIEF.md", "v13_pre_render_gate_brief"),
        item(SOURCE / "LANA_GATE_V13.md", "lana_exact_current_pre_render_pass"),
        item(SOURCE / "GORU_GATE_V13.md", "goru_exact_current_pre_render_pass"),
        item(SOURCE / "KUN_GATE_V13.md", "kun_exact_current_pre_render_pass"),
        item(SOURCE / "V13_PRE_RENDER_GATE_RECEIPT.json", "three_seat_pre_render_gate_receipt"),
        item(ROOT.parent.parent / "build_v13_contract_sources.py", "v13_source_builder"),
        item(ROOT.parent.parent / "test_v13_contract_repairs.py", "v13_contract_regression_test"),
        item(ROOT / "render_v13.py", "v13_renderer"),
        item(ROOT / "encoded_qa_v13.py", "v13_encoded_qa_program"),
        item(ROOT / "audit_v13_rendered_text_projection.py", "v13_closed_world_projection_program"),
        item(ROOT / "V13_RENDERED_TEXT_PROJECTION_AUDIT.json", "v13_closed_world_projection_result"),
        item(ROOT / "V13_DECODED_FRAME_VISUAL_PREFLIGHT.json", "v13_decoded_visual_preflight"),
        item(ROOT / "audio" / "timeline.json", "audio_timing_and_cue_authority"),
        item(ROOT / "audio" / "narration_master.wav", "audio_master"),
        item(ROOT / "captions_v12.srt", "exact_reused_source_srt"),
        item(ROOT / "captions_v12.vtt", "exact_reused_source_vtt"),
        item(ROOT / "V12_GENERATION_SPEND_LEDGER.json", "closed_generation_attempt_and_spend_ledger"),
        item(ROOT / "render_manifest.json", "v13_render_manifest"),
        item(ROOT / "encoded_qa" / "V13_ENCODED_QA.json", "v13_encoded_qa_receipt_json"),
        item(ROOT / "encoded_qa" / "V13_ENCODED_QA.md", "v13_encoded_qa_receipt_md"),
        item(ROOT / "encoded_qa" / "embedded_subtitle_extracted.srt", "subtitle_extracted_from_v13_mp4_srt"),
        item(ROOT / "encoded_qa" / "embedded_subtitle_extracted.vtt", "subtitle_extracted_from_v13_mp4_vtt"),
        item(ROOT / "encoded_qa" / "encoded_audio.wav", "audio_decoded_from_v13_mp4_pcm"),
        item(ROOT / "encoded_qa" / "encoded-contact-all11.png", "decoded_v13_reviewer_contact_sheet"),
        item(VIDEO, "exact_v13_candidate_for_unlisted_release"),
        item(SRT, "v13_delivery_srt_sidecar"),
        item(VTT, "v13_delivery_vtt_sidecar"),
    ]
    raw_rows = [item(path, "raw_generated_attempt_retained_for_audit") for path in sorted((ROOT / "generated_assets").glob("*.png"))]
    prepared_rows = [item(path, "prepared_generated_region_retained_for_audit") for path in sorted((ROOT / "assets" / "generated_prepared").glob("*.png"))]
    used_names = sorted({name for names in manifest["generated_asset_usage"].values() for name in names})
    prepared_names = sorted(path.name for path in (ROOT / "assets" / "generated_prepared").glob("*.png"))
    if not set(used_names).issubset(prepared_names):
        raise RuntimeError("manifest uses an untracked prepared generated asset")

    v11 = VIDEO_DIR / "bhu-closing-record-v11-local-20260813T1526K.mp4"
    v12 = VIDEO_DIR / "bhu-closing-record-v12-local-20260813T1657K.mp4"
    predecessor_custody = {
        "v11": item(v11, "currently_uploaded_unlisted_predecessor_to_retire_only_after_v13_upload_and_caption_serving"),
        "v12": item(v12, "local_contract_predecessor_byte_identical_to_v13_candidate"),
    }
    if predecessor_custody["v11"]["sha256"] != "8e6a4e564ddc25959ecb17c57fe19d898b9f92850b5c83da234ef3d2295f40fb":
        raise RuntimeError("V11 custody drift")
    if predecessor_custody["v12"]["sha256"] != EXPECTED_DELIVERY["video"]:
        raise RuntimeError("V12 custody drift")

    freeze = {
        "status": "FROZEN_V13_READY_FOR_GATED_UNLISTED_RELEASE",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "candidate": {
            "path": str(VIDEO), "sha256": sha(VIDEO), "bytes": VIDEO.stat().st_size,
            "duration_seconds": 402.0, "frame_count": 12060, "resolution": "1920x1080", "fps": 30,
            "streams": ["h264 video", "aac mono audio", "mov_text eng default subtitle"],
            "byte_identical_to_v12_local_candidate": sha(VIDEO) == sha(v12),
        },
        "pre_render_three_seat_gate": {
            "status": gate["status"], "receipt_sha256": sha(SOURCE / "V13_PRE_RENDER_GATE_RECEIPT.json"),
            "seats": gate["seats"], "any_hold_blocks": True, "prior_version_verdicts_carried_forward": False,
        },
        "local_qa": {
            "encoded_qa_status": qa["status"], "checks": f"{qa['checks_passed']}/{qa['checks_total']}",
            "encoded_qa_sha256": sha(ROOT / "encoded_qa" / "V13_ENCODED_QA.json"),
            "rendered_text_projection": projection["status"], "decoded_visual_preflight": visual["status"],
            "full_mp4_decode": "PASS",
        },
        "decoded_delivered_audio_wpm": {
            "method": qa["decoded_delivered_audio_wpm"]["method"],
            "per_card": decoded_rows,
            "minimum_wpm": min(row["decoded_audio_wpm"] for row in decoded_rows),
            "maximum_wpm": max(row["decoded_audio_wpm"] for row in decoded_rows),
            "all_inside_135_150": True,
        },
        "caption_gate": {
            "embedded_stream_present": True, "embedded_stream_codec": "mov_text", "embedded_stream_default_english": True,
            "embedded_stream_extracted": True, "cue_count": 64, "exact_source_payloads_and_timings": True,
            "srt_sidecar_sha256": sha(SRT), "vtt_sidecar_sha256": sha(VTT),
            "youtube_serving_state": "NOT_YET_APPLICABLE_AND_MUST_BE_VERIFIED_AFTER_CAPTIONS_INSERT",
        },
        "repair_a": {
            "exact_value": "no 95.4% endpoint, arrow, tick, bracket, marker, whisker, shaded boundary, axis-aligned glyph, or scaled terminus",
            "scaled_terminus_literal_present": True, "decoded_card_05_visual_preflight": "PASS_OPEN_FADE_NO_FORBIDDEN_95_4_TERMINUS",
        },
        "repair_b": {
            "conditional_role_exact": {"role": "illustration_tag", "text": "ILLUSTRATION", "permitted_when": "QA judges a generated asset could be read as an observation"},
            "condition_triggered": False, "judgment": "Used generated layers are stylized non-quantitative metaphor/illustration and are not mistakable for observations.",
        },
        "generation": {
            "call_count": ledger["generation_call_count"], "generated_video_calls": ledger["generated_video_call_count"],
            "monetary_cost": ledger["monetary_cost"], "final_asset_usage_by_card": manifest["generated_asset_usage"],
            "quantitative_cards_with_generated_assets": manifest["quantitative_cards_with_generated_assets"],
            "generation_closed": not ledger["new_calls_permitted_after_ledger"],
        },
        "frozen_files": frozen_files,
        "raw_generated_attempts": raw_rows,
        "prepared_generated_regions": prepared_rows,
        "prepared_regions_used_in_final": used_names,
        "prepared_regions_not_used_in_final_retained_for_audit": sorted(set(prepared_names) - set(used_names)),
        "predecessor_custody": predecessor_custody,
        "release_boundary": {
            "authorized_next_action": "unlisted upload only using the mandated uploader, exact gated title, and exact gated description, followed by captions.insert and serving verification",
            "public_visibility_authorized": False,
            "predecessor_privacy_mutation_before_v13_caption_serving": False,
            "required_post_upload": ["verify NebulaMind channel identity", "verify privacyStatus=unlisted", "captions.insert", "verify caption track serving", "update published.json full provenance", "retire V11 to private", "record supersession", "repoint bhu-video.html"],
        },
        "not_authorized": ["V13 source edit", "re-render", "audio rebuild", "caption rebuild", "new generation", "public visibility", "git commit", "git push", "DB write", "deploy", "restart"],
    }
    FREEZE_JSON.write_text(json.dumps(freeze, indent=2, ensure_ascii=False) + "\n")
    lines = [
        "# BHU V13 — exact freeze for gated unlisted release", "", f"Status: `{freeze['status']}`", "",
        f"- Candidate: `{VIDEO}`", f"- SHA-256: `{sha(VIDEO)}`", f"- {VIDEO.stat().st_size:,} bytes · 402.000 s · 12,060 frames · 1920×1080 at 30 fps", "- Streams: H.264 video, AAC mono audio, one default English mov_text subtitle stream", "",
        "## Gates", "", f"- Pre-render exact-current seats: Lana PASS · Goru PASS · Kun PASS", f"- Encoded QA: {qa['checks_passed']}/{qa['checks_total']} PASS", f"- Real decoded-AAC per-card WPM: {freeze['decoded_delivered_audio_wpm']['minimum_wpm']:.3f}–{freeze['decoded_delivered_audio_wpm']['maximum_wpm']:.3f}; all inside 135–150", "- Embedded subtitle stream extracted; 64 cue payloads and timings match source SRT/VTT and delivery sidecars.", "- Card 05 decoded-frame preflight: open fading 95.4% gradient; no forbidden endpoint or scaled terminus.", "- Conditional ILLUSTRATION tag not triggered: generated regions are stylized, non-quantitative metaphors and not observations.", "",
        "## Release boundary", "", "Unlisted upload only. Public visibility remains unauthorized. The prior unlisted V11 must remain untouched until V13 is uploaded, its caption track is inserted, and serving is verified.", "",
        f"- Freeze JSON: `{FREEZE_JSON}`", "- The JSON enumerates the exact source, gate, renderer, QA, caption, generated-asset, candidate, and predecessor hashes.",
    ]
    FREEZE_MD.write_text("\n".join(lines) + "\n")
    print(json.dumps({
        "status": freeze["status"], "candidate_sha256": sha(VIDEO), "frozen_file_count": len(frozen_files),
        "raw_generation_attempts": len(raw_rows), "prepared_generation_regions": len(prepared_rows),
        "freeze_json": str(FREEZE_JSON), "freeze_json_sha256": sha(FREEZE_JSON),
        "freeze_md": str(FREEZE_MD), "freeze_md_sha256": sha(FREEZE_MD),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
