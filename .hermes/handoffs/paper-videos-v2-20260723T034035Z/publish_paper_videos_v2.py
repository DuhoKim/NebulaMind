#!/usr/bin/env python3
"""Idempotently publish the QA-locked five-paper V2 batch to YouTube."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import time
import urllib.request

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

BASE = Path(__file__).resolve().parent
SPEC_PATH = BASE / "paper_video_specs_v2.json"
BATCH_RECEIPT = BASE / "batch_build_receipt.json"
QA_RECEIPT = BASE / "qa" / "deterministic_qa.json"
TOKEN = Path("/Users/duhokim/HermesOps/scripts/token_manage.json")
CHANNEL_ID = "UCUHBNGk8ozEnisQRuchoS4Q"
RETRIABLE = {500, 502, 503, 504}


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def atomic_json(path: Path, value: dict) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    os.replace(tmp, path)


def service():
    creds = Credentials.from_authorized_user_file(str(TOKEN))
    if not creds.valid:
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
            TOKEN.write_text(creds.to_json())
            os.chmod(TOKEN, 0o600)
        else:
            raise RuntimeError("YouTube manage credential is invalid and cannot refresh")
    scopes = set(creds.scopes or [])
    if not any(scope.endswith("/youtube.upload") for scope in scopes):
        raise RuntimeError("manage credential lacks youtube.upload scope")
    if not any(scope.endswith("/youtube.force-ssl") for scope in scopes):
        raise RuntimeError("manage credential lacks youtube.force-ssl scope")
    return build("youtube", "v3", credentials=creds, cache_discovery=False)


def channel_uploads(youtube) -> str:
    rows = youtube.channels().list(part="snippet,contentDetails", mine=True).execute().get("items", [])
    if len(rows) != 1 or rows[0]["id"] != CHANNEL_ID:
        raise RuntimeError(f"authenticated channel mismatch: {[row.get('id') for row in rows]}")
    return rows[0]["contentDetails"]["relatedPlaylists"]["uploads"]


def inventory(youtube, uploads: str, max_items: int = 500) -> list[dict]:
    token = None
    ids: list[str] = []
    while len(ids) < max_items:
        page = youtube.playlistItems().list(
            part="contentDetails", playlistId=uploads, maxResults=50, pageToken=token,
        ).execute()
        ids.extend(row["contentDetails"]["videoId"] for row in page.get("items", []))
        token = page.get("nextPageToken")
        if not token:
            break
    rows: list[dict] = []
    for i in range(0, len(ids), 50):
        items = youtube.videos().list(
            part="snippet,status,processingDetails,contentDetails", id=",".join(ids[i:i+50]),
        ).execute().get("items", [])
        for item in items:
            rows.append({
                "id": item["id"],
                "title": item["snippet"]["title"],
                "privacy": item["status"]["privacyStatus"],
                "processing": item.get("processingDetails", {}).get("processingStatus"),
            })
    return rows


def raw_video(youtube, video_id: str) -> dict:
    rows = youtube.videos().list(
        part="snippet,status,processingDetails,contentDetails", id=video_id,
    ).execute().get("items", [])
    if len(rows) != 1:
        raise RuntimeError(f"video not found: {video_id}")
    return rows[0]


def video_state(youtube, video_id: str) -> dict:
    row = raw_video(youtube, video_id)
    return {
        "id": video_id,
        "title": row["snippet"]["title"],
        "description": row["snippet"].get("description", ""),
        "privacy": row["status"]["privacyStatus"],
        "embeddable": row["status"].get("embeddable"),
        "madeForKids": row["status"].get("madeForKids"),
        "selfDeclaredMadeForKids": row["status"].get("selfDeclaredMadeForKids"),
        "processing": row.get("processingDetails", {}).get("processingStatus"),
        "processingFailureReason": row.get("processingDetails", {}).get("processingFailureReason"),
        "duration": row.get("contentDetails", {}).get("duration"),
    }


def parse_iso_duration(value: str) -> float:
    match = re.fullmatch(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", value or "")
    if not match:
        raise RuntimeError(f"unsupported YouTube duration: {value}")
    h, m, s = (int(x or 0) for x in match.groups())
    return h*3600 + m*60 + s


def upload_once(youtube, artifact: Path, paper: dict) -> str:
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": paper["youtube_title"],
                "description": paper["description"],
                "categoryId": "28",
                "defaultLanguage": "en",
                "defaultAudioLanguage": "en",
                "tags": [
                    "NebulaMind", "astronomy", "galaxy evolution", "JWST",
                    "plain language", "scientific explainer", "autonomous research",
                ],
            },
            "status": {
                "privacyStatus": "unlisted",
                "selfDeclaredMadeForKids": False,
                "embeddable": True,
            },
        },
        media_body=MediaFileUpload(str(artifact), chunksize=8*1024*1024, resumable=True),
    )
    response = None
    failures = 0
    while response is None:
        try:
            status, response = request.next_chunk()
            if status:
                print(f"  upload {int(status.progress()*100)}%", flush=True)
        except HttpError as exc:
            if exc.resp.status not in RETRIABLE or failures >= 5:
                raise
            time.sleep(2**failures)
            failures += 1
    return response["id"]


def wait_processing(youtube, video_id: str, timeout: int = 1800) -> dict:
    deadline = time.time() + timeout
    while time.time() < deadline:
        state = video_state(youtube, video_id)
        if state["processing"] == "succeeded":
            return state
        if state["processing"] in {"failed", "terminated"}:
            raise RuntimeError(f"processing failed: {state}")
        time.sleep(10)
    raise TimeoutError(f"processing timeout for {video_id}")


def caption_rows(youtube, video_id: str) -> list[dict]:
    return youtube.captions().list(part="snippet", videoId=video_id).execute().get("items", [])


def ensure_caption(youtube, video_id: str, srt: Path, checkpoint: dict, checkpoint_path: Path) -> tuple[str, str]:
    rows = caption_rows(youtube, video_id)
    matches = [row for row in rows if row["snippet"].get("language") == "en" and row["snippet"].get("name") == "English (manual V2)"]
    if len(matches) > 1:
        raise RuntimeError(f"duplicate manual V2 captions on {video_id}")
    if matches:
        caption = matches[0]
    else:
        caption = youtube.captions().insert(
            part="snippet",
            body={"snippet": {
                "videoId": video_id,
                "language": "en",
                "name": "English (manual V2)",
                "isDraft": False,
            }},
            media_body=MediaFileUpload(str(srt), mimetype="application/x-subrip", resumable=False),
        ).execute()
        checkpoint["caption_id"] = caption["id"]
        checkpoint["caption_inserted_at"] = now()
        atomic_json(checkpoint_path, checkpoint)
    caption_id = caption["id"]
    deadline = time.time() + 300
    while time.time() < deadline:
        current = [row for row in caption_rows(youtube, video_id) if row["id"] == caption_id]
        if current:
            status = current[0]["snippet"].get("status")
            if status == "serving":
                return caption_id, status
            if status == "failed":
                raise RuntimeError(f"caption failed for {video_id}")
        time.sleep(6)
    raise TimeoutError(f"caption serving timeout for {video_id}")


def set_public(youtube, video_id: str) -> None:
    row = raw_video(youtube, video_id)
    old = row["status"]
    status = {
        "privacyStatus": "public",
        "embeddable": old.get("embeddable", True),
        "selfDeclaredMadeForKids": old.get("selfDeclaredMadeForKids", False),
    }
    for field in ("license", "publicStatsViewable"):
        if field in old:
            status[field] = old[field]
    youtube.videos().update(part="status", body={"id": video_id, "status": status}).execute()


def sustained_public(youtube, video_id: str, consecutive: int = 3) -> list[dict]:
    observations: list[dict] = []
    passed = 0
    deadline = time.time() + 180
    while time.time() < deadline:
        state = video_state(youtube, video_id)
        observations.append({"at": now(), "privacy": state["privacy"], "processing": state["processing"], "embeddable": state["embeddable"]})
        if state["privacy"] == "public" and state["processing"] == "succeeded" and state["embeddable"] is True:
            passed += 1
            if passed >= consecutive:
                return observations
        else:
            passed = 0
        time.sleep(10)
    raise TimeoutError(f"public state did not settle for {video_id}: {observations}")


def oembed(video_id: str, expected_title: str) -> dict:
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
    req = urllib.request.Request(url, headers={"User-Agent": "NebulaMind-publication-verifier/2.0"})
    with urllib.request.urlopen(req, timeout=30) as response:
        payload = json.loads(response.read().decode("utf-8"))
    if payload.get("title") != expected_title:
        raise RuntimeError(f"oEmbed title mismatch for {video_id}: {payload.get('title')!r}")
    return {"title": payload.get("title"), "author_name": payload.get("author_name"), "provider_name": payload.get("provider_name")}


def load_inputs() -> tuple[dict, list[dict]]:
    spec = json.loads(SPEC_PATH.read_text())
    batch = json.loads(BATCH_RECEIPT.read_text())
    qa = json.loads(QA_RECEIPT.read_text())
    if batch.get("marker") != "NEBULAMIND_FIVE_PAPER_VIDEO_BATCH_BUILD_COMPLETE_V2" or batch.get("paper_count") != 5:
        raise RuntimeError("V2 batch build receipt incomplete")
    if qa.get("marker") != "NEBULAMIND_FIVE_PAPER_DETERMINISTIC_QA_PASS_V2" or qa.get("paper_count") != 5:
        raise RuntimeError("V2 deterministic QA receipt incomplete")
    papers = {paper["key"]: paper for paper in spec["papers"]}
    qa_keys = {row["key"] for row in qa["rows"] if row.get("status") == "PASS"}
    rows: list[dict] = []
    for artifact in batch["artifacts"]:
        key = artifact["key"]
        if key not in papers or key not in qa_keys:
            raise RuntimeError(f"{key}: missing spec or QA pass")
        video = Path(artifact["path"])
        srt = Path(artifact["srt"])
        if sha256(video) != artifact["sha256"] or sha256(srt) != artifact["srt_sha256"]:
            raise RuntimeError(f"{key}: upload input hash drift")
        rows.append({"key": key, "paper": papers[key], "artifact": artifact, "video": video, "srt": srt, "checkpoint_path": video.parent/"publication_checkpoint.json"})
    if len(rows) != 5:
        raise RuntimeError("expected five locked upload rows")
    return spec, rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute", action="store_true", help="perform the approved unlisted→captioned→public transaction")
    args = parser.parse_args()
    _, rows = load_inputs()
    youtube = service()
    uploads = channel_uploads(youtube)
    owned = inventory(youtube, uploads)
    by_title: dict[str, list[dict]] = {}
    for item in owned:
        by_title.setdefault(item["title"], []).append(item)

    preflight: list[dict] = []
    for row in rows:
        checkpoint = json.loads(row["checkpoint_path"].read_text())
        expected_id = checkpoint.get("video_id", "")
        matches = by_title.get(row["paper"]["youtube_title"], [])
        if expected_id:
            if matches and expected_id not in [match["id"] for match in matches]:
                raise RuntimeError(f"{row['key']}: checkpoint conflicts with exact-title inventory")
        elif matches:
            raise RuntimeError(f"{row['key']}: exact-title duplicate collision: {matches}")
        preflight.append({"key": row["key"], "title": row["paper"]["youtube_title"], "checkpoint_video_id": expected_id, "exact_title_matches": matches})
    atomic_json(BASE/"youtube_publication_preflight.json", {
        "marker": "NEBULAMIND_FIVE_PAPER_V2_YOUTUBE_PREFLIGHT",
        "checked_at_utc": now(),
        "channel_id": CHANNEL_ID,
        "execute": args.execute,
        "items": preflight,
        "old_v1_mutations": False,
        "website_mutations": False,
    })
    if not args.execute:
        print(json.dumps(preflight, indent=2, ensure_ascii=False))
        return

    # Phase 1: obtain and fully process every unlisted ID.
    for row in rows:
        checkpoint = json.loads(row["checkpoint_path"].read_text())
        video_id = checkpoint.get("video_id", "")
        if not video_id:
            print(f"{row['key']}: uploading once as unlisted", flush=True)
            try:
                video_id = upload_once(youtube, row["video"], row["paper"])
            except Exception:
                refreshed = inventory(youtube, uploads)
                ambiguous = [item for item in refreshed if item["title"] == row["paper"]["youtube_title"]]
                checkpoint.update({"status": "UPLOAD_AMBIGUOUS_STOPPED", "ambiguous_candidates": ambiguous, "last_checked_at": now()})
                atomic_json(row["checkpoint_path"], checkpoint)
                raise
            checkpoint.update({
                "video_id": video_id,
                "url": f"https://youtu.be/{video_id}",
                "privacy": "unlisted",
                "processing": "uploaded_processing",
                "status": "UNLISTED_PROCESSING",
                "uploaded_at": now(),
            })
            atomic_json(row["checkpoint_path"], checkpoint)
        state = wait_processing(youtube, video_id)
        if state["title"] != row["paper"]["youtube_title"] or state["description"] != row["paper"]["description"]:
            raise RuntimeError(f"{row['key']}: server metadata mismatch")
        if state["privacy"] != "unlisted" or state["embeddable"] is not True or state["selfDeclaredMadeForKids"] is not False:
            raise RuntimeError(f"{row['key']}: unsafe unlisted state: {state}")
        if abs(parse_iso_duration(state["duration"]) - float(row["artifact"]["duration"])) > 2.0:
            raise RuntimeError(f"{row['key']}: server duration mismatch: {state['duration']}")
        checkpoint.update({"privacy": "unlisted", "processing": "succeeded", "status": "UNLISTED_PROCESSING_SUCCEEDED", "server_state": state, "verified_at": now()})
        atomic_json(row["checkpoint_path"], checkpoint)
        print(f"{row['key']}: unlisted and processed {video_id}", flush=True)

    # Phase 2: attach and settle every manual caption before any public mutation.
    for row in rows:
        checkpoint = json.loads(row["checkpoint_path"].read_text())
        video_id = checkpoint["video_id"]
        caption_id, status = ensure_caption(youtube, video_id, row["srt"], checkpoint, row["checkpoint_path"])
        checkpoint.update({"caption_id": caption_id, "caption_status": status, "status": "UNLISTED_CAPTIONS_SERVING", "caption_verified_at": now()})
        atomic_json(row["checkpoint_path"], checkpoint)
        print(f"{row['key']}: manual captions serving", flush=True)

    # Final whole-batch gate immediately before publication.
    for row in rows:
        checkpoint = json.loads(row["checkpoint_path"].read_text())
        state = video_state(youtube, checkpoint["video_id"])
        captions = caption_rows(youtube, checkpoint["video_id"])
        serving = [item for item in captions if item["id"] == checkpoint["caption_id"] and item["snippet"].get("status") == "serving"]
        if state["privacy"] != "unlisted" or state["processing"] != "succeeded" or not serving:
            raise RuntimeError(f"{row['key']}: final public gate failed")

    # Phase 3: publish every new V2 ID. Old V1 IDs are never referenced by mutation code.
    settlement: dict[str, list[dict]] = {}
    for row in rows:
        checkpoint = json.loads(row["checkpoint_path"].read_text())
        video_id = checkpoint["video_id"]
        state = video_state(youtube, video_id)
        if state["privacy"] != "public":
            set_public(youtube, video_id)
        settlement[video_id] = sustained_public(youtube, video_id)
        checkpoint.update({"privacy": "public", "status": "PUBLIC_PROCESSING_SUCCEEDED_MANUAL_CAPTIONS_SERVING", "published_at": checkpoint.get("published_at") or now(), "settlement": settlement[video_id]})
        atomic_json(row["checkpoint_path"], checkpoint)
        print(f"{row['key']}: PUBLIC {video_id}", flush=True)

    items: list[dict] = []
    for row in rows:
        checkpoint = json.loads(row["checkpoint_path"].read_text())
        state = video_state(youtube, checkpoint["video_id"])
        external = oembed(checkpoint["video_id"], row["paper"]["youtube_title"])
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
            "source_sha256": row["artifact"]["sha256"],
            "caption_sha256": row["artifact"]["srt_sha256"],
            "oembed": external,
        })
    receipt = {
        "marker": "NEBULAMIND_FIVE_PAPER_V2_YOUTUBE_PUBLICATION_COMPLETE",
        "completed_at_utc": now(),
        "channel_id": CHANNEL_ID,
        "items": items,
        "old_v1_mutations": False,
        "website_mutations": False,
        "git_mutations": False,
        "runtime_mutations": False,
        "settlement": settlement,
    }
    atomic_json(BASE/"youtube_publication_receipt.json", receipt)
    print(json.dumps(receipt, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
