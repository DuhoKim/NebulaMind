#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import time
from pathlib import Path
from typing import Any

from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

BASE = Path(__file__).resolve().parent
BATCH = BASE / "batch"
HANDOFF = BATCH / "final_local_handoff.json"
QA = BATCH / "qa/deterministic_qa.json"
VISUAL_QA = BATCH / "qa/visual_qa.json"
V2_BASE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-videos-v2-20260723T034035Z")
V2_SPEC = V2_BASE / "paper_video_specs_v2.json"
V2_PUBLICATION = V2_BASE / "youtube_publication_receipt.json"
V2_PUBLISHER = V2_BASE / "publish_paper_videos_v2.py"
CHANNEL_ID = "UCUHBNGk8ozEnisQRuchoS4Q"
CAPTION_NAME = "English (manual V3)"
PREFLIGHT = BATCH / "youtube_v3_preflight.json"
RECEIPT = BATCH / "youtube_v3_publication_receipt.json"


def load_v2_module():
    spec = importlib.util.spec_from_file_location("v2pub", V2_PUBLISHER)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load proven V2 publisher primitives")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


v2pub = load_v2_module()


def atomic_json(path: Path, value: dict[str, Any]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    os.replace(temporary, path)


def v3_metadata(paper: dict[str, Any]) -> dict[str, Any]:
    title = paper["youtube_title"].replace("Plain-English V2", "Male Presenter V3")
    description = paper["description"]
    description = description.replace("A slower, plain-English V2 explanation", "A plain-English V3 explanation")
    description = description.replace(
        "Natural-paced Shimmer narration; manual English captions included.",
        "Natural-paced Michael narration with a fictional male presenter and exact-audio lip-sync; manual English captions included.",
    )
    if "V2" in title or "Shimmer" in description or "plain-English V2" in description:
        raise RuntimeError(f"stale V2 metadata remains: {paper['key']}")
    if len(title) > 100 or len(description) > 5000:
        raise RuntimeError(f"metadata overflow: {paper['key']}")
    return {
        "key": paper["key"],
        "youtube_title": title,
        "description": description,
    }


def load_inputs() -> list[dict[str, Any]]:
    handoff = json.loads(HANDOFF.read_text())
    qa = json.loads(QA.read_text())
    visual = json.loads(VISUAL_QA.read_text())
    papers = {paper["key"]: paper for paper in json.loads(V2_SPEC.read_text())["papers"]}
    if handoff.get("marker") != "NEBULAMIND_FIVE_PAPER_V3_LOCAL_BATCH_QA_COMPLETE" or handoff.get("paper_count") != 5:
        raise RuntimeError("V3 local handoff incomplete")
    if qa.get("marker") != "NEBULAMIND_FIVE_PAPER_V3_DETERMINISTIC_QA_PASS" or qa.get("paper_count") != 5 or qa.get("visual_qa") != "PASS":
        raise RuntimeError("V3 deterministic QA incomplete")
    if visual.get("marker") != "NEBULAMIND_FIVE_PAPER_V3_VISUAL_QA_PASS" or visual.get("paper_count") != 5:
        raise RuntimeError("V3 visual QA incomplete")
    qa_keys = {row["key"] for row in qa["rows"] if row.get("status") == "PASS"}
    visual_keys = {row["key"] for row in visual["rows"] if row.get("status") == "PASS"}
    rows: list[dict[str, Any]] = []
    for artifact in handoff["artifacts"]:
        key = artifact["key"]
        if key not in papers or key not in qa_keys or key not in visual_keys:
            raise RuntimeError(f"{key}: missing spec or QA pass")
        video = Path(artifact["artifact"])
        srt = Path(artifact["srt"])
        if v2pub.sha256(video) != artifact["artifact_sha256"] or v2pub.sha256(srt) != artifact["srt_sha256"]:
            raise RuntimeError(f"{key}: frozen upload hash drift")
        metadata = v3_metadata(papers[key])
        checkpoint_path = BATCH / key / "publication_checkpoint.json"
        if checkpoint_path.is_file():
            checkpoint = json.loads(checkpoint_path.read_text())
            if checkpoint.get("source_sha256") not in {None, "", artifact["artifact_sha256"]}:
                raise RuntimeError(f"{key}: checkpoint source hash conflicts")
            if checkpoint.get("caption_sha256") not in {None, "", artifact["srt_sha256"]}:
                raise RuntimeError(f"{key}: checkpoint caption hash conflicts")
        else:
            checkpoint = {}
        checkpoint.update({
            "key": key,
            "source": str(video),
            "source_sha256": artifact["artifact_sha256"],
            "caption": str(srt),
            "caption_sha256": artifact["srt_sha256"],
            "title": metadata["youtube_title"],
            "description": metadata["description"],
            "expected_duration": artifact["duration_seconds"],
            "old_v2_id_context_only": next(item["id"] for item in json.loads(V2_PUBLICATION.read_text())["items"] if item["key"] == key),
            "video_id": checkpoint.get("video_id", ""),
            "url": checkpoint.get("url", ""),
            "caption_id": checkpoint.get("caption_id", ""),
            "privacy": checkpoint.get("privacy", "local"),
            "processing": checkpoint.get("processing", "not_uploaded"),
            "status": checkpoint.get("status", "LOCAL_QA_COMPLETE"),
        })
        atomic_json(checkpoint_path, checkpoint)
        rows.append({
            "key": key,
            "artifact": artifact,
            "video": video,
            "srt": srt,
            "metadata": metadata,
            "checkpoint": checkpoint,
            "checkpoint_path": checkpoint_path,
        })
    if len(rows) != 5:
        raise RuntimeError("expected five V3 upload rows")
    return rows


def upload_once(youtube, row: dict[str, Any]) -> str:
    metadata = row["metadata"]
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": metadata["youtube_title"],
                "description": metadata["description"],
                "categoryId": "28",
                "defaultLanguage": "en",
                "defaultAudioLanguage": "en",
                "tags": [
                    "NebulaMind", "astronomy", "galaxy evolution", "JWST",
                    "plain language", "scientific explainer", "male presenter",
                ],
            },
            "status": {
                "privacyStatus": "unlisted",
                "selfDeclaredMadeForKids": False,
                "embeddable": True,
            },
        },
        media_body=MediaFileUpload(str(row["video"]), chunksize=8 * 1024 * 1024, resumable=True),
    )
    response = None
    failures = 0
    while response is None:
        try:
            status, response = request.next_chunk()
            if status:
                print(f"  upload {int(status.progress() * 100)}%", flush=True)
        except HttpError as exc:
            if exc.resp.status not in v2pub.RETRIABLE or failures >= 5:
                raise
            time.sleep(2**failures)
            failures += 1
    return response["id"]


def caption_rows(youtube, video_id: str) -> list[dict[str, Any]]:
    return youtube.captions().list(part="snippet", videoId=video_id).execute().get("items", [])


def ensure_caption(youtube, row: dict[str, Any], video_id: str, checkpoint: dict[str, Any]) -> tuple[str, str]:
    matches = [
        item for item in caption_rows(youtube, video_id)
        if item["snippet"].get("language") == "en" and item["snippet"].get("name") == CAPTION_NAME
    ]
    if len(matches) > 1:
        raise RuntimeError(f"duplicate V3 captions on {video_id}")
    if matches:
        caption = matches[0]
    else:
        caption = youtube.captions().insert(
            part="snippet",
            body={"snippet": {
                "videoId": video_id,
                "language": "en",
                "name": CAPTION_NAME,
                "isDraft": False,
            }},
            media_body=MediaFileUpload(str(row["srt"]), mimetype="application/x-subrip", resumable=False),
        ).execute()
        checkpoint["caption_id"] = caption["id"]
        checkpoint["caption_inserted_at"] = v2pub.now()
        atomic_json(row["checkpoint_path"], checkpoint)
    caption_id = caption["id"]
    deadline = time.time() + 300
    while time.time() < deadline:
        current = [item for item in caption_rows(youtube, video_id) if item["id"] == caption_id]
        if current:
            status = current[0]["snippet"].get("status")
            if status == "serving":
                return caption_id, status
            if status == "failed":
                raise RuntimeError(f"caption failed for {video_id}")
        time.sleep(6)
    raise TimeoutError(f"caption serving timeout for {video_id}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute", action="store_true", help="perform approved unlisted upload, caption, and public publication")
    args = parser.parse_args()
    rows = load_inputs()
    youtube = v2pub.service()
    uploads = v2pub.channel_uploads(youtube)
    owned = v2pub.inventory(youtube, uploads)
    by_title: dict[str, list[dict[str, Any]]] = {}
    for item in owned:
        by_title.setdefault(item["title"], []).append(item)
    preflight_items = []
    for row in rows:
        checkpoint = json.loads(row["checkpoint_path"].read_text())
        video_id = checkpoint.get("video_id", "")
        matches = by_title.get(row["metadata"]["youtube_title"], [])
        if video_id:
            if matches and video_id not in [match["id"] for match in matches]:
                raise RuntimeError(f"{row['key']}: checkpoint conflicts with exact-title inventory")
        elif matches:
            raise RuntimeError(f"{row['key']}: exact-title collision {matches}")
        preflight_items.append({
            "key": row["key"],
            "title": row["metadata"]["youtube_title"],
            "source_sha256": row["artifact"]["artifact_sha256"],
            "caption_sha256": row["artifact"]["srt_sha256"],
            "checkpoint_video_id": video_id,
            "exact_title_matches": matches,
        })
    atomic_json(PREFLIGHT, {
        "marker": "NEBULAMIND_FIVE_PAPER_V3_YOUTUBE_PREFLIGHT_PASS",
        "checked_at_utc": v2pub.now(),
        "channel_id": CHANNEL_ID,
        "execute": args.execute,
        "items": preflight_items,
        "quota_basis": "Google official 2026-06-01 table: videos.insert separate 100/day bucket; captions.insert 400; videos.update 50",
        "old_v2_mutations": False,
        "website_mutations": False,
    })
    if not args.execute:
        print(json.dumps({"status": "PASS", "channel_id": CHANNEL_ID, "items": preflight_items}, indent=2, ensure_ascii=False))
        return

    # Phase 1: upload every V3 master unlisted and verify processing before captions/publication.
    for row in rows:
        checkpoint = json.loads(row["checkpoint_path"].read_text())
        video_id = checkpoint.get("video_id", "")
        if not video_id:
            print(f"{row['key']}: upload once as unlisted", flush=True)
            try:
                video_id = upload_once(youtube, row)
            except Exception:
                refreshed = v2pub.inventory(youtube, uploads)
                candidates = [item for item in refreshed if item["title"] == row["metadata"]["youtube_title"]]
                checkpoint.update({"status": "UPLOAD_AMBIGUOUS_STOPPED", "ambiguous_candidates": candidates, "last_checked_at": v2pub.now()})
                atomic_json(row["checkpoint_path"], checkpoint)
                raise
            checkpoint.update({
                "video_id": video_id,
                "url": f"https://youtu.be/{video_id}",
                "privacy": "unlisted",
                "processing": "uploaded_processing",
                "status": "UNLISTED_PROCESSING",
                "uploaded_at": v2pub.now(),
            })
            atomic_json(row["checkpoint_path"], checkpoint)
        state = v2pub.wait_processing(youtube, video_id)
        if state["title"] != row["metadata"]["youtube_title"] or state["description"] != row["metadata"]["description"]:
            raise RuntimeError(f"{row['key']}: server metadata mismatch")
        if state["privacy"] != "unlisted" or state["embeddable"] is not True or state["selfDeclaredMadeForKids"] is not False:
            raise RuntimeError(f"{row['key']}: unsafe unlisted state {state}")
        if abs(v2pub.parse_iso_duration(state["duration"]) - float(row["artifact"]["duration_seconds"])) > 2.0:
            raise RuntimeError(f"{row['key']}: server duration mismatch {state['duration']}")
        checkpoint.update({"privacy": "unlisted", "processing": "succeeded", "status": "UNLISTED_PROCESSING_SUCCEEDED", "server_state": state, "verified_at": v2pub.now()})
        atomic_json(row["checkpoint_path"], checkpoint)
        print(f"{row['key']}: unlisted processed {video_id}", flush=True)

    # Phase 2: attach and settle every manual V3 caption before any public mutation.
    for row in rows:
        checkpoint = json.loads(row["checkpoint_path"].read_text())
        caption_id, caption_status = ensure_caption(youtube, row, checkpoint["video_id"], checkpoint)
        checkpoint.update({
            "caption_id": caption_id,
            "caption_status": caption_status,
            "status": "UNLISTED_CAPTIONS_SERVING",
            "caption_verified_at": v2pub.now(),
        })
        atomic_json(row["checkpoint_path"], checkpoint)
        print(f"{row['key']}: manual V3 captions serving", flush=True)

    # Whole-batch gate: all five must remain unlisted, processed, and caption-serving.
    for row in rows:
        checkpoint = json.loads(row["checkpoint_path"].read_text())
        state = v2pub.video_state(youtube, checkpoint["video_id"])
        serving = [
            item for item in caption_rows(youtube, checkpoint["video_id"])
            if item["id"] == checkpoint["caption_id"] and item["snippet"].get("status") == "serving"
        ]
        if state["privacy"] != "unlisted" or state["processing"] != "succeeded" or not serving:
            raise RuntimeError(f"{row['key']}: public gate failed")

    # Phase 3: publish the five new V3 IDs. V2 IDs are context-only and never mutated.
    settlement: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        checkpoint = json.loads(row["checkpoint_path"].read_text())
        video_id = checkpoint["video_id"]
        if v2pub.video_state(youtube, video_id)["privacy"] != "public":
            v2pub.set_public(youtube, video_id)
        settlement[video_id] = v2pub.sustained_public(youtube, video_id)
        checkpoint.update({
            "privacy": "public",
            "processing": "succeeded",
            "caption_status": "serving",
            "status": "PUBLIC_PROCESSING_SUCCEEDED_MANUAL_CAPTIONS_SERVING",
            "published_at": checkpoint.get("published_at") or v2pub.now(),
            "settlement": settlement[video_id],
        })
        atomic_json(row["checkpoint_path"], checkpoint)
        print(f"{row['key']}: PUBLIC {video_id}", flush=True)

    items = []
    for row in rows:
        checkpoint = json.loads(row["checkpoint_path"].read_text())
        state = v2pub.video_state(youtube, checkpoint["video_id"])
        external = v2pub.oembed(checkpoint["video_id"], row["metadata"]["youtube_title"])
        items.append({
            "key": row["key"],
            "id": checkpoint["video_id"],
            "url": checkpoint["url"],
            "title": state["title"],
            "privacy": state["privacy"],
            "processing": state["processing"],
            "embeddable": state["embeddable"],
            "duration": state["duration"],
            "caption_id": checkpoint["caption_id"],
            "caption_status": checkpoint["caption_status"],
            "source_sha256": row["artifact"]["artifact_sha256"],
            "caption_sha256": row["artifact"]["srt_sha256"],
            "old_v2_id_unchanged": checkpoint["old_v2_id_context_only"],
            "oembed": external,
        })
    receipt = {
        "marker": "NEBULAMIND_FIVE_PAPER_V3_YOUTUBE_PUBLICATION_COMPLETE",
        "completed_at_utc": v2pub.now(),
        "channel_id": CHANNEL_ID,
        "items": items,
        "old_v2_mutations": False,
        "old_v1_mutations": False,
        "website_mutations": False,
        "git_mutations": False,
        "runtime_mutations": False,
        "settlement": settlement,
    }
    atomic_json(RECEIPT, receipt)
    print(json.dumps(receipt, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
