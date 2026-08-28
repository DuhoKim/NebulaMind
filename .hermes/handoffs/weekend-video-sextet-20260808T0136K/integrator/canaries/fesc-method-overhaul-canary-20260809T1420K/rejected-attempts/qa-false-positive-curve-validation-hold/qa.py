#!/usr/bin/env python3
"""Full encoded QA, introduction transcription, receipts, and freeze for one sibling canary."""
from __future__ import annotations

import argparse
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
from openai import OpenAI

ROOT = Path(__file__).resolve().parent
RENDERER = ROOT / "render.py"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(cmd, **kwargs):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kwargs)


def normalize(text: str) -> str:
    return " ".join(re.sub(r"[^a-z0-9 ]+", " ", text.lower()).split())


def ffprobe(path: Path) -> dict:
    return json.loads(run(["ffprobe", "-v", "error", "-count_frames", "-show_entries", "format=duration,size,bit_rate:stream=index,codec_name,codec_type,width,height,avg_frame_rate,sample_rate,channels,nb_read_frames,duration", "-of", "json", str(path)]).stdout)


def loudness(path: Path) -> dict:
    p = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-af", "loudnorm=I=-20.3:LRA=7:TP=-2.3:print_format=json", "-f", "null", "-"], check=True, capture_output=True, text=True)
    m = re.search(r"\{\s*\"input_i\".*?\}", p.stderr, re.S)
    if not m:
        raise RuntimeError("loudness parse failed")
    return json.loads(m.group(0))


def motion(path: Path, duration: float) -> dict:
    width, height, rate = 160, 90, 2
    p = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(path), "-vf", f"fps={rate},scale={width}:{height},format=gray", "-f", "rawvideo", "-pix_fmt", "gray", "-"], check=True, capture_output=True)
    chunk = width * height; data = p.stdout; frames = len(data) // chunk
    diffs = []; longest = 0.0; current = 0.0
    previous = None
    for i in range(frames):
        arr = np.frombuffer(data[i*chunk:(i+1)*chunk], dtype=np.uint8).astype(np.int16)
        if previous is not None:
            diff = float(np.abs(arr - previous).mean()); diffs.append(diff)
            if diff < 0.08:
                current += 1/rate; longest = max(longest, current)
            else:
                current = 0.0
        previous = arr
    return {"sample_rate_fps": rate, "sampled_frames": frames, "mean_absolute_frame_difference": float(np.mean(diffs)), "max_absolute_frame_difference": float(np.max(diffs)), "longest_near_unchanged_seconds": longest, "threshold": 0.08, "expected_duration": duration}


def extract_frames(candidate: Path, video: Path, records: list[dict], peak_section: str) -> tuple[list[dict], Path]:
    out = candidate / "encoded_qa" / "frames"
    if out.parent.exists(): shutil.rmtree(out.parent)
    out.mkdir(parents=True)
    items=[]
    for r in records:
        t=(r["audio_start_seconds"]+r["audio_end_seconds"])/2
        target=out/f"{r['id']}-{t:07.3f}.jpg"
        run(["ffmpeg","-hide_banner","-loglevel","error","-y","-ss",f"{t:.6f}","-i",str(video),"-frames:v","1","-q:v","2",str(target)])
        items.append({"label":r["id"],"time":t,"path":target})
    peak=[r for r in records if r["section"]==peak_section]
    center=peak[len(peak)//2]
    for i,q in enumerate((.05,.25,.5,.75,.95),1):
        t=center["audio_start_seconds"]+(center["audio_end_seconds"]-center["audio_start_seconds"])*q
        target=out/f"peak-{i}-{t:07.3f}.jpg"
        run(["ffmpeg","-hide_banner","-loglevel","error","-y","-ss",f"{t:.6f}","-i",str(video),"-frames:v","1","-q:v","2",str(target)])
        items.append({"label":f"peak-{i}","time":t,"path":target})
    cols=4; tw,th,lh=480,270,34; rows=math.ceil(len(items)/cols)
    sheet=Image.new("RGB",(cols*tw,rows*(th+lh)),(4,7,13)); draw=ImageDraw.Draw(sheet); fnt=ImageFont.truetype("/System/Library/Fonts/Avenir Next.ttc",20,index=7)
    for idx,item in enumerate(items):
        x=(idx%cols)*tw; y=(idx//cols)*(th+lh); im=ImageOps.fit(Image.open(item["path"]).convert("RGB"),(tw,th),Image.Resampling.LANCZOS); sheet.paste(im,(x,y))
        label=f"{item['label']} · {item['time']:06.2f}s"; box=draw.textbbox((0,0),label,font=fnt); draw.text((x+(tw-(box[2]-box[0]))/2,y+th+5),label,font=fnt,fill=(239,244,251))
    contact=candidate/"encoded-contact-sheet.jpg"; sheet.save(contact,quality=94,subsampling=0)
    return items,contact


def ocr_frames(items: list[dict], candidate: Path) -> dict:
    parts=[]
    for item in items:
        p=run(["tesseract",str(item["path"]),"stdout","--psm","6"])
        parts.append(f"--- {item['label']} ---\n{p.stdout}")
    text="\n".join(parts); (candidate/"encoded_qa/ocr.txt").write_text(text)
    lower=text.lower(); forbidden=["/users/",".json",".md","source_freeze","status.json","t1_","t2_","t3_","internal path"]
    hits=[x for x in forbidden if x in lower]
    return {"engine":"tesseract", "frame_count":len(items), "forbidden_terms":forbidden, "forbidden_hits":hits, "status":"PASS" if not hits else "HOLD"}


def transcribe_intro(candidate: Path, video: Path, records: list[dict]) -> dict:
    start=max(0.0,records[0]["audio_start_seconds"]-0.25); end=records[3]["audio_end_seconds"]+0.35
    wav=candidate/"encoded_qa/encoded-introduction.wav"
    run(["ffmpeg","-hide_banner","-loglevel","error","-y","-ss",f"{start:.6f}","-to",f"{end:.6f}","-i",str(video),"-vn","-ac","1","-ar","16000","-c:a","pcm_s16le",str(wav)])
    gateway=resolve_managed_tool_gateway("openai-audio")
    if gateway is None: raise RuntimeError("managed audio gateway unavailable for encoded transcription")
    client=OpenAI(api_key=gateway.nous_user_token,base_url=gateway.gateway_origin.rstrip("/")+"/v1")
    with wav.open("rb") as stream:
        response=client.audio.transcriptions.create(model="whisper-1",file=stream)
    transcript=response.text.strip(); expected=" ".join(r["text"] for r in records[:4])
    n_expected=normalize(expected); n_actual=normalize(transcript); similarity=difflib.SequenceMatcher(None,n_expected,n_actual).ratio()
    report={"status":"PASS" if similarity>=.94 else "HOLD","provider_route":"Hermes managed OpenAI audio gateway","model":"whisper-1","start_seconds":start,"end_seconds":end,"expected":expected,"transcript":transcript,"normalized_expected":n_expected,"normalized_transcript":n_actual,"similarity":similarity,"audio_sha256":sha256(wav)}
    (candidate/"encoded_qa/encoded-introduction-transcription.json").write_text(json.dumps(report,indent=2)+"\n")
    return report


def source_manifest(candidate: Path) -> dict:
    files=[]
    for path in sorted((candidate/"sources").iterdir()):
        if path.is_file(): files.append({"path":str(path.relative_to(candidate)),"sha256":sha256(path),"bytes":path.stat().st_size})
    return {"files":files,"count":len(files)}


def provenance_manifest(candidate: Path) -> dict:
    files=[]
    for path in sorted((candidate/"provenance").rglob("*")):
        if path.is_file(): files.append({"path":str(path.relative_to(candidate)),"sha256":sha256(path),"bytes":path.stat().st_size})
    return {"files":files,"count":len(files)}


def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("candidate_dir"); args=ap.parse_args(); candidate=Path(args.candidate_dir).resolve()
    provenance=candidate/"provenance"; provenance.mkdir(parents=True,exist_ok=True); qa_snapshot=provenance/"qa.py"; shutil.copy2(Path(__file__).resolve(),qa_snapshot)
    spec=json.loads((candidate/"spec.json").read_text()); timeline=json.loads((candidate/"audio/timeline.json").read_text()); build=json.loads((candidate/"build_receipt.json").read_text())
    video=candidate/spec["candidate_filename"]
    probe=ffprobe(video); streams={s["codec_type"]:s for s in probe["streams"]}; duration=float(probe["format"]["duration"])
    subprocess.run(["ffmpeg","-hide_banner","-v","error","-i",str(video),"-map","0:v:0","-map","0:a:0","-f","null","-"],check=True)
    items,contact=extract_frames(candidate,video,timeline["records"],spec["peak_section"])
    ocr=ocr_frames(items,candidate); intro=transcribe_intro(candidate,video,timeline["records"]); mot=motion(video,duration); loud=loudness(video)
    peak_hashes=[sha256(x["path"]) for x in items if x["label"].startswith("peak-")]
    renderer_spec=importlib.util.spec_from_file_location("renderer",RENDERER); renderer=importlib.util.module_from_spec(renderer_spec); renderer_spec.loader.exec_module(renderer)
    dummy=Image.new("RGB",(1920,1080)); draw=ImageDraw.Draw(dummy); fnt=renderer.font(31,bold=True)
    caption_lines={r["id"]:len(renderer.wrap_lines(draw,r["text"],fnt,1510)) for r in timeline["records"]}
    numeric=json.loads((candidate/"numeric_guard.json").read_text())
    icon_kinds=[r.get("params",{}).get("icon") for r in timeline["records"] if r.get("params",{}).get("icon")]
    renderer_source=(candidate/build["renderer_path"]).read_text()
    checks={
        "video_stream_h264":streams["video"]["codec_name"]=="h264",
        "audio_stream_aac":streams["audio"]["codec_name"]=="aac",
        "resolution_1920x1080":[streams["video"]["width"],streams["video"]["height"]]==[1920,1080],
        "fps_30":streams["video"]["avg_frame_rate"]=="30/1",
        "duration_within_one_frame":abs(duration-timeline["master_duration_seconds"])<=1/30+0.001,
        "delivered_wpm_in_range":105<=timeline["delivered_wpm"]<=125,
        "av_alignment_under_one_frame":timeline["max_abs_audio_visual_start_delta_seconds"]<1/30,
        "all_sentence_states_extracted":len([x for x in items if not x["label"].startswith("peak-")])==len(timeline["records"]),
        "encoded_intro_transcription_pass":intro["status"]=="PASS",
        "motivation_first_four":all(r["section"]=="motivation" for r in timeline["records"][:4]),
        "peak_is_longest_section":timeline["section_intervals_seconds"][spec["peak_section"]]==max(timeline["section_intervals_seconds"].values()),
        "five_distinct_peak_frames":len(set(peak_hashes))==5,
        "no_eight_second_freeze":mot["longest_near_unchanged_seconds"]<8,
        "positive_motion":mot["mean_absolute_frame_difference"]>0.05,
        "loudness_in_target_band":-21.8<=float(loud["input_i"])<=-19.0,
        "true_peak_safe":float(loud["input_tp"])<=-2.0,
        "spec_hash_matches_build":build["spec_sha256"]==sha256(candidate/"spec.json"),
        "timeline_hash_matches_build":build["timeline_sha256"]==sha256(candidate/"audio/timeline.json"),
        "audio_hash_matches_build":build["audio_master_sha256"]==sha256(candidate/"audio/narration_master.wav"),
        "encoded_hash_matches_build":build["output_sha256"]==sha256(video),
        "renderer_snapshot_matches_build":(candidate/build["renderer_path"]).is_file() and build["renderer_sha256"]==sha256(candidate/build["renderer_path"]),
        "numeric_guard_pass":numeric["status"]=="PASS",
        "curve_icon_parameter_absent":"curve" not in icon_kinds,
        "curve_icon_primitive_unavailable":'kind=="curve"' not in renderer_source,
        "source_grounded_runtime_at_least_75_percent":build["source_grounded_runtime_percent"]>=75,
        "ocr_internal_terms_clean":ocr["status"]=="PASS",
        "captions_at_most_two_lines":max(caption_lines.values())<=2,
        "method_only_gate_closed":spec["video_reportable_now"] is False,
        "no_source_freeze_in_candidate":not (candidate/"sources/SOURCE_FREEZE.json").exists(),
        "full_decode_pass":True
    }
    report={"status":"PASS" if all(checks.values()) else "HOLD","candidate":candidate.name,"video":video.name,"video_sha256":sha256(video),"probe":probe,"timeline_summary":{k:timeline[k] for k in ("sentence_count","word_count","delivered_wpm","master_duration_seconds","max_abs_audio_visual_start_delta_seconds","section_intervals_seconds")},"loudness":loud,"motion":mot,"introduction_transcription":intro,"ocr":ocr,"caption_lines":caption_lines,"numeric_guard":numeric,"contact_sheet":contact.name,"checks":checks,"passed":sum(checks.values()),"total":len(checks)}
    (candidate/"encoded_qa.json").write_text(json.dumps(report,indent=2)+"\n")
    if report["status"]!="PASS": raise RuntimeError("encoded QA HOLD: "+str([k for k,v in checks.items() if not v]))
    now=datetime.now(timezone.utc).astimezone().isoformat(); manifest=source_manifest(candidate); (candidate/"source_manifest.json").write_text(json.dumps(manifest,indent=2)+"\n"); provenance_data=provenance_manifest(candidate); (candidate/"provenance_manifest.json").write_text(json.dumps(provenance_data,indent=2)+"\n")
    pred=json.loads((candidate/"PREDECESSOR.json").read_text()) if (candidate/"PREDECESSOR.json").exists() else None
    qa=f"""# Self-QA — {candidate.name}\n\nTimestamp: {now}\nStatus: `LOCAL_SELF_QA_PASS`\nCandidate SHA-256: `{sha256(video)}`\n\n- Encoded machine checks: **{report['passed']}/{report['total']} PASS**.\n- Full H.264/AAC decode: PASS.\n- Media: 1920×1080, 30 fps, {duration:.3f} seconds.\n- Narration: {timeline['word_count']} words, {timeline['delivered_wpm']:.3f} WPM, Alloy at speed 1.18, no music.\n- Audio: {float(loud['input_i']):.2f} LUFS, {float(loud['input_tp']):.2f} dBTP.\n- Maximum A/V action-start delta: {timeline['max_abs_audio_visual_start_delta_seconds']:.6f} seconds.\n- Introduction transcription similarity: {intro['similarity']:.6f}; conditional motivation precedes all technical content.\n- Peak section: `{spec['peak_section']}` at {timeline['section_intervals_seconds'][spec['peak_section']]:.3f} seconds, the longest narrated move.\n- Source-grounded runtime: {build['source_grounded_runtime_percent']:.2f}%.\n- Numeric guard: PASS; every rendered numeral has lane-local evidence.\n- Encoded OCR: no internal path or artifact filename exposure.\n- Captions: maximum {max(caption_lines.values())} lines.\n- Method-only boundary: no source freeze; no result value, direction, or interpretation authorized.\n\nDisposition: `LOCAL_ONLY_ACCEPTANCE_CANDIDATE`. Independent review remains separate. No upload, cockpit/videos copy, Git action, deployment, or publication occurred.\n"""
    (candidate/"QA.md").write_text(qa)
    receipt={"created_at":now,"status":"LOCAL_SELF_QA_PASS","candidate":candidate.name,"video":video.name,"video_sha256":sha256(video),"spec_sha256":sha256(candidate/"spec.json"),"timeline_sha256":sha256(candidate/"audio/timeline.json"),"audio_master_sha256":sha256(candidate/"audio/narration_master.wav"),"synthesis_receipt_sha256":sha256(candidate/"audio/synthesis_receipt.json"),"build_receipt_sha256":sha256(candidate/"build_receipt.json"),"encoded_qa_sha256":sha256(candidate/"encoded_qa.json"),"source_manifest_sha256":sha256(candidate/"source_manifest.json"),"provenance_manifest_sha256":sha256(candidate/"provenance_manifest.json"),"contact_sheet_sha256":sha256(contact),"predecessor":pred,"gates":{"upload":False,"cockpit_or_video_root_copy":False,"git":False,"video_reportable_now":False}}
    (candidate/"RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
    freeze={"frozen_at":now,"status":"LOCAL_SELF_QA_PASS_FROZEN","candidate":candidate.name,"video_sha256":sha256(video),"receipt_sha256":sha256(candidate/"RECEIPT.json"),"replacement_policy":"Never rewrite this candidate; corrections require a new versioned directory.","gates":receipt["gates"]}
    (candidate/"POST_ENCODE_FREEZE.json").write_text(json.dumps(freeze,indent=2)+"\n")
    print(json.dumps({"status":report["status"],"passed":report["passed"],"total":report["total"],"video_sha256":report["video_sha256"],"duration":duration,"wpm":timeline["delivered_wpm"],"intro_similarity":intro["similarity"]},indent=2))
    return 0


if __name__=="__main__": raise SystemExit(main())
