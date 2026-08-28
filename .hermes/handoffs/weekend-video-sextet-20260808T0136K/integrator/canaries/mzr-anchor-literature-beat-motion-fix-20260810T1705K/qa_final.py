#!/usr/bin/env python3
"""Final encoded QA and immutable freeze for one two-lane literature-beat candidate."""
from __future__ import annotations

import difflib
import hashlib
import importlib.util
import json
import math
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps

HERMES_SOURCE = Path("/Users/duhokim/.hermes/hermes-agent")
if str(HERMES_SOURCE) not in sys.path:
    sys.path.insert(0, str(HERMES_SOURCE))
from tools.managed_tool_gateway import resolve_managed_tool_gateway  # noqa: E402
from openai import OpenAI  # noqa: E402

ROOT = Path(__file__).resolve().parent
RENDERER = ROOT / "render.py"
H = ROOT.parents[2]
EXPECTED_PREDECESSOR = {
    "mzr-anchor": (H / "integrator/canaries/mzr-anchor-method-overhaul-canary-20260809T1406K/mzr-anchor-method-overhaul-canary-20260809T1406K.mp4", "c892f3faaec3049e89865673ad46e66a84fe7d24289edbbc857256bbd00e3584"),
    "brightend": (H / "integrator/canaries/brightend-method-overhaul-canary-20260809T1345K/brightend-method-overhaul-canary-20260809T1345K.mp4", "c772e6435af2298b3eac0eb772f406730c2240430a318a7f2268858f1b37cdb8"),
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, check=True, capture_output=True, text=True)


def ffprobe(path: Path) -> dict:
    return json.loads(run(["ffprobe", "-v", "error", "-count_frames", "-show_entries", "format=duration,size,bit_rate:stream=index,codec_name,codec_type,width,height,avg_frame_rate,sample_rate,channels,nb_read_frames,duration", "-of", "json", str(path)]).stdout)


def loudness(path: Path) -> dict:
    result = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-af", "loudnorm=I=-20.3:LRA=7:TP=-2.3:print_format=json", "-f", "null", "-"], check=True, capture_output=True, text=True)
    match = re.search(r"\{\s*\"input_i\".*?\}", result.stderr, re.S)
    if not match:
        raise RuntimeError("loudness parse failed")
    return json.loads(match.group(0))


def motion(path: Path) -> dict:
    width, height, rate = 160, 90, 2
    near_unchanged_threshold = 0.03
    data = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(path), "-vf", f"fps={rate},scale={width}:{height},format=gray", "-f", "rawvideo", "-pix_fmt", "gray", "-"], check=True, capture_output=True).stdout
    chunk = width * height; frames = len(data) // chunk; previous = None; diffs = []; current = 0.0; longest = 0.0
    for index in range(frames):
        array = np.frombuffer(data[index * chunk:(index + 1) * chunk], dtype=np.uint8).astype(np.int16)
        if previous is not None:
            diff = float(np.abs(array - previous).mean()); diffs.append(diff)
            if diff < near_unchanged_threshold:
                current += 1 / rate; longest = max(longest, current)
            else:
                current = 0.0
        previous = array
    return {"sample_rate_fps": rate, "sampled_frames": frames, "mean_absolute_frame_difference": float(np.mean(diffs)), "max_absolute_frame_difference": float(np.max(diffs)), "longest_near_unchanged_seconds": longest, "threshold": near_unchanged_threshold, "threshold_basis": "Low-amplitude ambient grid/star motion; values below 0.03 are treated as effectively static."}


def extract_frames(video: Path, records: list[dict]) -> tuple[list[dict], Path]:
    out = ROOT / "encoded_qa/frames"
    if out.parent.exists():
        shutil.rmtree(out.parent)
    out.mkdir(parents=True)
    items = []
    for record in records:
        at = (record["audio_start_seconds"] + record["audio_end_seconds"]) / 2
        target = out / f"{record['id']}-{at:07.3f}.jpg"
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{at:.6f}", "-i", str(video), "-frames:v", "1", "-q:v", "2", str(target)])
        items.append({"label": record["id"], "time": at, "path": target})
    cols, tw, th, lh = 4, 480, 270, 34
    rows = math.ceil(len(items) / cols)
    sheet = Image.new("RGB", (cols * tw, rows * (th + lh)), (4, 7, 13)); draw = ImageDraw.Draw(sheet)
    fnt = ImageFont.truetype("/System/Library/Fonts/Avenir Next.ttc", 20, index=7)
    for index, item in enumerate(items):
        x = index % cols * tw; y = index // cols * (th + lh)
        image = ImageOps.fit(Image.open(item["path"]).convert("RGB"), (tw, th), Image.Resampling.LANCZOS); sheet.paste(image, (x, y))
        label = f"{item['label']} · {item['time']:06.2f}s"; box = draw.textbbox((0, 0), label, font=fnt)
        draw.text((x + (tw - (box[2] - box[0])) / 2, y + th + 5), label, font=fnt, fill=(239, 244, 251))
    contact = ROOT / "encoded-contact-sheet.jpg"; sheet.save(contact, quality=94, subsampling=0)
    return items, contact


def ocr_frames(items: list[dict]) -> dict:
    parts = []
    for item in items:
        text = run(["tesseract", str(item["path"]), "stdout", "--psm", "6"]).stdout
        parts.append(f"--- {item['label']} ---\n{text}")
    combined = "\n".join(parts); (ROOT / "encoded_qa/ocr.txt").write_text(combined)
    forbidden = ["/users/", ".json", ".md", "source_freeze", "internal path"]
    hits = [term for term in forbidden if term in combined.lower()]
    return {"engine": "tesseract", "frame_count": len(items), "forbidden_terms": forbidden, "forbidden_hits": hits, "status": "PASS" if not hits else "HOLD"}


def normalize(text: str) -> str:
    text = text.lower().replace("(y-int)", "y intercept").replace("y-int", "y intercept").replace("0.7", "zero point seven").replace("∼", " approximately ").replace("λcdm", "lambda c d m").replace("7-10", "seven to ten")
    return " ".join(re.sub(r"[^a-z0-9 ]+", " ", text).split())


def transcribe_opening(video: Path, records: list[dict]) -> dict:
    opening = [record for record in records if record["section"] in {"motivation", "literature"}]
    start = max(0.0, opening[0]["audio_start_seconds"] - 0.25); end = opening[-1]["audio_end_seconds"] + 0.35
    wav = ROOT / "encoded_qa/encoded-opening.wav"
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{start:.6f}", "-to", f"{end:.6f}", "-i", str(video), "-vn", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le", str(wav)])
    gateway = resolve_managed_tool_gateway("openai-audio")
    if gateway is None:
        raise RuntimeError("managed audio gateway unavailable")
    client = OpenAI(api_key=gateway.nous_user_token, base_url=gateway.gateway_origin.rstrip("/") + "/v1")
    with wav.open("rb") as stream:
        transcript = client.audio.transcriptions.create(model="whisper-1", file=stream).text.strip()
    expected = " ".join(record["text"] for record in opening)
    similarity = difflib.SequenceMatcher(None, normalize(expected), normalize(transcript)).ratio()
    normalized_transcript = normalize(transcript)
    if any(record["id"] == "i05q" for record in opening):
        semantic_terms = ["metallicity", "calibration", "zero point seven", "dex", "disputed", "no answer", "finding"]
    else:
        semantic_terms = ["jwst", "high redshift", "stellar masses", "massive galaxy candidates", "unresolved", "observations", "lambda c d m", "no answer", "finding"]
    semantic_guard = all(term in normalized_transcript for term in semantic_terms)
    # The exact raw sentence clips are independently ASR-gated. This encoded
    # combined-clip check protects channel survival and safety semantics while
    # tolerating a proper-name homophone such as Kewley/Cooley from Whisper.
    report = {"status": "PASS" if similarity >= 0.75 and semantic_guard else "HOLD", "provider_route": "Hermes managed OpenAI audio gateway", "model": "whisper-1", "start_seconds": start, "end_seconds": end, "expected": expected, "transcript": transcript, "similarity": similarity, "semantic_terms": semantic_terms, "semantic_guard": semantic_guard, "audio_sha256": sha256(wav)}
    (ROOT / "encoded_qa/encoded-opening-transcription.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    return report


def current_tree(root: Path) -> dict:
    rows = []
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        rows.append({"path": str(path.relative_to(root)), "bytes": path.stat().st_size, "sha256": sha256(path)})
    payload = "".join(f"{row['sha256']}  {row['path']}\n" for row in rows).encode()
    return {"file_count": len(rows), "tree_sha256": hashlib.sha256(payload).hexdigest(), "files": rows}


def custody_checks() -> tuple[dict, dict]:
    baseline = json.loads((ROOT / "PROTECTED_CUSTODY_BASELINE.json").read_text())
    canaries = H / "integrator/canaries"
    comparisons = []
    for expected in baseline["fesc_and_mzr_census_canary_trees"]:
        current = current_tree(Path(expected["root"]))
        comparisons.append({"root": expected["root"], "expected_file_count": expected["file_count"], "current_file_count": current["file_count"], "expected_tree_sha256": expected["tree_sha256"], "current_tree_sha256": current["tree_sha256"], "unchanged": current["file_count"] == expected["file_count"] and current["tree_sha256"] == expected["tree_sha256"]})
    cockpit_root = Path(baseline["cockpit_mp4_manifest"]["root"])
    rows = []
    for path in sorted(cockpit_root.rglob("*.mp4")):
        rows.append({"path": str(path.relative_to(cockpit_root)), "bytes": path.stat().st_size, "sha256": sha256(path)})
    payload = "".join(f"{row['sha256']}  {row['path']}\n" for row in rows).encode()
    cockpit_tree = hashlib.sha256(payload).hexdigest()
    result = {"fesc_and_mzr_census": comparisons, "cockpit": {"expected_file_count": baseline["cockpit_mp4_manifest"]["file_count"], "current_file_count": len(rows), "expected_tree_sha256": baseline["cockpit_mp4_manifest"]["tree_sha256"], "current_tree_sha256": cockpit_tree, "unchanged": len(rows) == baseline["cockpit_mp4_manifest"]["file_count"] and cockpit_tree == baseline["cockpit_mp4_manifest"]["tree_sha256"]}}
    checks = {"all_fesc_and_mzr_census_trees_unchanged": all(item["unchanged"] for item in comparisons), "all_cockpit_mp4s_unchanged": result["cockpit"]["unchanged"]}
    return result, checks


def manifest() -> dict:
    excluded = {"FILE_MANIFEST.json", "CANDIDATE_AUTHORITY.json", "RECEIPT.json", "POST_ENCODE_FREEZE.json"}
    rows = []
    for path in sorted(item for item in ROOT.rglob("*") if item.is_file() and item.name not in excluded):
        rows.append({"path": str(path.relative_to(ROOT)), "bytes": path.stat().st_size, "sha256": sha256(path)})
    return {"files": rows, "count": len(rows)}


def main() -> int:
    provenance = ROOT / "provenance"; provenance.mkdir(exist_ok=True); shutil.copy2(Path(__file__).resolve(), provenance / "qa_final.py")
    spec = json.loads((ROOT / "spec.json").read_text()); timeline = json.loads((ROOT / "audio/timeline.json").read_text()); build = json.loads((ROOT / "build_receipt.json").read_text())
    video = ROOT / spec["candidate_filename"]; probe = ffprobe(video); streams = {stream["codec_type"]: stream for stream in probe["streams"]}; duration = float(probe["format"]["duration"])
    subprocess.run(["ffmpeg", "-hide_banner", "-v", "error", "-i", str(video), "-map", "0:v:0", "-map", "0:a:0", "-f", "null", "-"], check=True)
    items, contact = extract_frames(video, timeline["records"]); ocr = ocr_frames(items); intro = transcribe_opening(video, timeline["records"]); mot = motion(video); loud = loudness(video)
    renderer_spec = importlib.util.spec_from_file_location("renderer", RENDERER); renderer = importlib.util.module_from_spec(renderer_spec); renderer_spec.loader.exec_module(renderer)
    dummy = Image.new("RGB", (1920, 1080)); draw = ImageDraw.Draw(dummy)
    caption_lines = {}
    for record in timeline["records"]:
        size = 18 if record["section"] == "literature" and len(record["text"]) > 190 else 24 if record["section"] == "literature" else 31
        fnt = renderer.font(size, bold=record["section"] != "literature", serif=record["section"] == "literature")
        caption_lines[record["id"]] = len(renderer.wrap_lines(draw, record["text"], fnt, 1510))
    contract = json.loads((ROOT / "CONTRACT_QA.json").read_text()); asr = json.loads((ROOT / "audio/literature_asr.json").read_text()); numeric = json.loads((ROOT / "numeric_guard.json").read_text())
    custody, custody_flags = custody_checks(); predecessor_path, predecessor_hash = EXPECTED_PREDECESSOR[spec["slug"]]
    encoded_frames = int(streams["video"]["nb_read_frames"]); raw_frames = int(build["raw_frames_submitted"])
    checks = {
        "video_stream_h264": streams["video"]["codec_name"] == "h264", "audio_stream_aac": streams["audio"]["codec_name"] == "aac",
        "resolution_1920x1080": [streams["video"]["width"], streams["video"]["height"]] == [1920, 1080], "fps_30": streams["video"]["avg_frame_rate"] == "30/1",
        "duration_tail_within_one_frame": abs(duration - timeline["master_duration_seconds"]) <= 1 / 30 + 0.002, "delivered_wpm_exact_target": abs(timeline["delivered_wpm"] - 115.0) < 0.001,
        "av_alignment_under_one_frame": timeline["max_abs_audio_visual_start_delta_seconds"] < 1 / 30, "all_sentence_states_extracted": len(items) == len(timeline["records"]),
        "encoded_opening_transcription_pass": intro["status"] == "PASS", "literature_raw_asr_pass": asr["status"] == "PASS", "contract_qa_pass": contract["status"] == "PASS",
        "numeric_guard_pass": numeric["status"] == "PASS", "no_eight_second_freeze": mot["longest_near_unchanged_seconds"] < 8, "positive_motion": mot["mean_absolute_frame_difference"] > 0.05,
        "loudness_in_target_band": -21.8 <= float(loud["input_i"]) <= -19.0, "true_peak_safe": float(loud["input_tp"]) <= -2.0,
        "spec_hash_matches_build": build["spec_sha256"] == sha256(ROOT / "spec.json"), "timeline_hash_matches_build": build["timeline_sha256"] == sha256(ROOT / "audio/timeline.json"),
        "audio_hash_matches_build": build["audio_master_sha256"] == sha256(ROOT / "audio/narration_master.wav"), "encoded_hash_matches_build": build["output_sha256"] == sha256(video),
        "renderer_snapshot_matches_build": build["renderer_sha256"] == sha256(ROOT / build["renderer_path"]), "raw_frame_receipt_matches_ceil": raw_frames == math.ceil(timeline["master_duration_seconds"] * 30),
        "encoded_frame_receipt_matches_probe": encoded_frames == int(build["encoded_video_frames"]), "frame_delta_at_most_one": abs(raw_frames - encoded_frames) <= 1,
        "ocr_internal_terms_clean": ocr["status"] == "PASS", "captions_at_most_two_lines": max(caption_lines.values()) <= 2,
        "source_grounded_runtime_at_least_75_percent": build["source_grounded_runtime_percent"] >= 75, "video_reportable_now_false": spec["video_reportable_now"] is False,
        "source_freeze_absent": spec["source_freeze_status"] == "ABSENT_FAIL_CLOSED" and not (ROOT / "sources/SOURCE_FREEZE.json").exists(),
        "predecessor_unchanged": predecessor_path.is_file() and sha256(predecessor_path) == predecessor_hash,
        **custody_flags, "full_decode_pass": True,
    }
    report = {"status": "PASS" if all(checks.values()) else "HOLD", "candidate": ROOT.name, "video": video.name, "video_sha256": sha256(video), "probe": probe, "timeline_summary": {key: timeline[key] for key in ("sentence_count", "word_count", "delivered_wpm", "master_duration_seconds", "max_abs_audio_visual_start_delta_seconds", "section_intervals_seconds")}, "loudness": loud, "motion": mot, "encoded_opening_transcription": intro, "literature_asr": asr, "ocr": ocr, "caption_lines": caption_lines, "numeric_guard": numeric, "frame_custody": {"raw_frames_submitted": raw_frames, "encoded_video_frames": encoded_frames}, "protected_custody": custody, "contact_sheet": contact.name, "checks": checks, "passed": sum(checks.values()), "total": len(checks)}
    (ROOT / "encoded_qa.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    if report["status"] != "PASS":
        raise RuntimeError("encoded QA HOLD: " + str([key for key, value in checks.items() if not value]))
    now = datetime.now(timezone.utc).astimezone().isoformat()
    authority = {"authority_id": f"{spec['slug'].upper().replace('-', '_')}_LITERATURE_BEAT_CANARY_AUTHORITY_20260810T1640K", "created_at": now, "state": "PROVISIONAL_FROZEN_AWAITING_KUN_GUARDRAILS_THEN_TORI_EXACT_HASH_REGATE_THEN_DUHO_WATCH", "lane": spec["slug"], "candidate": ROOT.name, "video": video.name, "video_sha256": sha256(video), "source_freeze": "ABSENT", "video_reportable_now": False, "accepted_by_duho": False, "gates": {"upload": False, "cockpit_copy": False, "public": False, "git": False}}
    (ROOT / "CANDIDATE_AUTHORITY.json").write_text(json.dumps(authority, indent=2) + "\n")
    file_manifest = manifest(); (ROOT / "FILE_MANIFEST.json").write_text(json.dumps(file_manifest, indent=2) + "\n")
    receipt = {"created_at": now, "status": "LOCAL_SELF_QA_PASS_PROVISIONAL_NOT_ACCEPTED", "candidate": ROOT.name, "video": video.name, "video_sha256": sha256(video), "spec_sha256": sha256(ROOT / "spec.json"), "timeline_sha256": sha256(ROOT / "audio/timeline.json"), "audio_master_sha256": sha256(ROOT / "audio/narration_master.wav"), "synthesis_receipt_sha256": sha256(ROOT / "audio/synthesis_receipt.json"), "literature_asr_sha256": sha256(ROOT / "audio/literature_asr.json"), "build_receipt_sha256": sha256(ROOT / "build_receipt.json"), "encoded_qa_sha256": sha256(ROOT / "encoded_qa.json"), "contract_qa_sha256": sha256(ROOT / "CONTRACT_QA.json"), "candidate_authority_sha256": sha256(ROOT / "CANDIDATE_AUTHORITY.json"), "file_manifest_sha256": sha256(ROOT / "FILE_MANIFEST.json"), "contact_sheet_sha256": sha256(contact), "predecessor_sha256": predecessor_hash, "gates": {"upload": False, "cockpit_or_video_root_copy": False, "git": False, "video_reportable_now": False, "accepted_by_duho": False}}
    (ROOT / "RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n")
    freeze = {"frozen_at": now, "status": "PROVISIONAL_LOCAL_SELF_QA_PASS_FROZEN_AWAITING_KUN_TORI_DUHO", "candidate": ROOT.name, "video_sha256": sha256(video), "receipt_sha256": sha256(ROOT / "RECEIPT.json"), "candidate_authority_sha256": sha256(ROOT / "CANDIDATE_AUTHORITY.json"), "file_manifest_sha256": sha256(ROOT / "FILE_MANIFEST.json"), "replacement_policy": "Never rewrite this candidate; corrections require a new versioned directory.", "gates": receipt["gates"]}
    (ROOT / "POST_ENCODE_FREEZE.json").write_text(json.dumps(freeze, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "passed": report["passed"], "total": report["total"], "video_sha256": report["video_sha256"], "duration": duration, "wpm": timeline["delivered_wpm"], "opening_similarity": intro["similarity"], "raw_frames": raw_frames, "encoded_frames": encoded_frames}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
