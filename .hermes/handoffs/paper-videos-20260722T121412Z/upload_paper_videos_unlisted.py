#!/usr/bin/env python3
"""Idempotent upload of the QA-locked five-paper batch to YouTube as unlisted."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import os
import time

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

BASE = Path(__file__).resolve().parent
SPEC_PATH = BASE / "paper_video_specs.json"
BATCH_RECEIPT = BASE / "batch_build_receipt.json"
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


def write_json(path: Path, value: dict) -> None:
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
    if not any(s.endswith("/youtube.upload") for s in scopes) or not any(s.endswith("/youtube.force-ssl") for s in scopes):
        raise RuntimeError("manage token lacks upload or force-ssl scope")
    return build("youtube", "v3", credentials=creds, cache_discovery=False)


def channel_uploads(youtube) -> str:
    rows = youtube.channels().list(part="snippet,contentDetails", mine=True).execute().get("items", [])
    if len(rows) != 1 or rows[0]["id"] != CHANNEL_ID:
        raise RuntimeError(f"authenticated channel mismatch: {[r.get('id') for r in rows]}")
    return rows[0]["contentDetails"]["relatedPlaylists"]["uploads"]


def inventory_by_title(youtube, uploads: str, title: str, max_items: int = 500) -> list[dict]:
    token = None
    ids: list[str] = []
    while len(ids) < max_items:
        page = youtube.playlistItems().list(part="contentDetails", playlistId=uploads, maxResults=50, pageToken=token).execute()
        ids += [row["contentDetails"]["videoId"] for row in page.get("items", [])]
        token = page.get("nextPageToken")
        if not token:
            break
    matches: list[dict] = []
    for i in range(0, len(ids), 50):
        rows = youtube.videos().list(part="snippet,status,processingDetails", id=",".join(ids[i:i+50])).execute().get("items", [])
        for row in rows:
            if row["snippet"]["title"] == title:
                matches.append({"id": row["id"], "title": title, "privacy": row["status"]["privacyStatus"], "processing": row.get("processingDetails", {}).get("processingStatus")})
    return matches


def video_state(youtube, video_id: str) -> dict:
    rows = youtube.videos().list(part="snippet,status,processingDetails,contentDetails", id=video_id).execute().get("items", [])
    if len(rows) != 1:
        raise RuntimeError(f"video not found: {video_id}")
    row = rows[0]
    return {"id": video_id, "title": row["snippet"]["title"], "description": row["snippet"].get("description", ""), "privacy": row["status"]["privacyStatus"], "embeddable": row["status"].get("embeddable"), "madeForKids": row["status"].get("madeForKids"), "selfDeclaredMadeForKids": row["status"].get("selfDeclaredMadeForKids"), "processing": row.get("processingDetails", {}).get("processingStatus"), "processingFailureReason": row.get("processingDetails", {}).get("processingFailureReason"), "duration": row.get("contentDetails", {}).get("duration")}


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
                "tags": ["NebulaMind", "astronomy", "galaxy evolution", "JWST", "autonomous research"],
            },
            "status": {
                "privacyStatus": "unlisted",
                "selfDeclaredMadeForKids": False,
                "embeddable": True,
            },
        },
        media_body=MediaFileUpload(str(artifact), chunksize=8 * 1024 * 1024, resumable=True),
    )
    response = None
    failures = 0
    while response is None:
        try:
            status, response = request.next_chunk()
            if status:
                print(f"  upload {int(status.progress() * 100)}%", flush=True)
        except HttpError as exc:
            if exc.resp.status not in RETRIABLE or failures >= 5:
                raise
            time.sleep(2 ** failures)
            failures += 1
    return response["id"]


def wait_processing(youtube, video_id: str, timeout: int = 1200) -> dict:
    deadline = time.time() + timeout
    while time.time() < deadline:
        state = video_state(youtube, video_id)
        if state["processing"] == "succeeded":
            return state
        if state["processing"] in {"failed", "terminated"}:
            raise RuntimeError(f"processing {state['processing']}: {state}")
        time.sleep(10)
    raise TimeoutError(f"processing timeout for {video_id}")


def caption_rows(youtube, video_id: str) -> list[dict]:
    return youtube.captions().list(part="snippet", videoId=video_id).execute().get("items", [])


def ensure_manual_caption(youtube, video_id: str, srt: Path, checkpoint: dict) -> tuple[str, str]:
    rows = caption_rows(youtube, video_id)
    matches = [r for r in rows if r["snippet"].get("language") == "en" and r["snippet"].get("name") == "English (manual)"]
    if len(matches) > 1:
        raise RuntimeError(f"duplicate manual captions on {video_id}: {[r['id'] for r in matches]}")
    if matches:
        row = matches[0]
    else:
        row = youtube.captions().insert(
            part="snippet",
            body={"snippet": {"videoId": video_id, "language": "en", "name": "English (manual)", "isDraft": False}},
            media_body=MediaFileUpload(str(srt), mimetype="application/x-subrip", resumable=False),
        ).execute()
        checkpoint["caption_id"] = row["id"]
        checkpoint["caption_inserted_at"] = now()
    caption_id = row["id"]
    deadline = time.time() + 300
    while time.time() < deadline:
        refreshed = [r for r in caption_rows(youtube, video_id) if r["id"] == caption_id]
        if refreshed:
            status = refreshed[0]["snippet"].get("status")
            if status == "serving":
                return caption_id, status
            if status == "failed":
                raise RuntimeError(f"caption failed for {video_id}")
        time.sleep(5)
    raise TimeoutError(f"caption serving timeout for {video_id}")


def load_inputs() -> tuple[dict, dict, dict[str, dict]]:
    spec = json.loads(SPEC_PATH.read_text())
    batch = json.loads(BATCH_RECEIPT.read_text())
    if batch.get("marker") != "NEBULAMIND_FIVE_PAPER_VIDEO_BATCH_BUILD_COMPLETE_V1" or batch.get("paper_count") != 5:
        raise RuntimeError("batch build receipt missing or incomplete")
    artifacts = {row["key"]: row for row in batch["artifacts"]}
    papers = {row["key"]: row for row in spec["papers"]}
    if set(artifacts) != set(papers):
        raise RuntimeError("spec/build artifact key mismatch")
    return spec, batch, {key: {"paper": papers[key], "artifact": artifacts[key]} for key in papers}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute-unlisted", action="store_true", help="perform uploads/caption inserts; default is read-only preflight")
    args = parser.parse_args()
    _, _, rows = load_inputs()
    youtube = service()
    uploads = channel_uploads(youtube)
    summary = []
    for key, row in rows.items():
        paper, artifact_row = row["paper"], row["artifact"]
        artifact, srt = Path(artifact_row["path"]), Path(artifact_row["srt"])
        if sha256(artifact) != artifact_row["sha256"] or sha256(srt) != artifact_row["srt_sha256"]:
            raise RuntimeError(f"{key}: artifact or caption hash drift")
        checkpoint_path = BASE / "videos" / key / "publication_checkpoint.json"
        checkpoint = json.loads(checkpoint_path.read_text())
        if checkpoint["source_sha256"] != artifact_row["sha256"] or checkpoint["caption_sha256"] != artifact_row["srt_sha256"]:
            raise RuntimeError(f"{key}: checkpoint hash mismatch")
        matches = inventory_by_title(youtube, uploads, paper["youtube_title"])
        video_id = checkpoint.get("video_id", "")
        if video_id:
            if matches and video_id not in [m["id"] for m in matches]:
                raise RuntimeError(f"{key}: checkpoint ID conflicts with exact-title inventory")
            state = video_state(youtube, video_id)
        else:
            if matches:
                raise RuntimeError(f"{key}: exact-title duplicate collision; refusing upload: {matches}")
            if not args.execute_unlisted:
                summary.append({"key": key, "status": "READY_NO_DUPLICATE", "title": paper["youtube_title"]})
                print(f"{key}: READY_NO_DUPLICATE", flush=True)
                continue
            print(f"{key}: uploading once as unlisted", flush=True)
            try:
                video_id = upload_once(youtube, artifact, paper)
            except Exception:
                ambiguous = inventory_by_title(youtube, uploads, paper["youtube_title"])
                checkpoint["status"] = "UPLOAD_AMBIGUOUS_STOPPED"
                checkpoint["ambiguous_candidates"] = ambiguous
                checkpoint["last_checked_at"] = now()
                write_json(checkpoint_path, checkpoint)
                raise
            checkpoint.update({"video_id": video_id, "url": f"https://youtu.be/{video_id}", "privacy": "unlisted", "processing": "uploaded_processing", "status": "UNLISTED_PROCESSING", "uploaded_at": now()})
            write_json(checkpoint_path, checkpoint)
            state = video_state(youtube, video_id)
        if not args.execute_unlisted:
            summary.append({"key": key, "status": "CHECKPOINT_VERIFY", "video_id": video_id, "state": state})
            continue
        state = wait_processing(youtube, video_id)
        if state["title"] != paper["youtube_title"] or state["description"] != paper["description"]:
            raise RuntimeError(f"{key}: server metadata mismatch")
        if state["privacy"] != "unlisted" or state["embeddable"] is not True or state["selfDeclaredMadeForKids"] is not False:
            raise RuntimeError(f"{key}: unsafe server status: {state}")
        caption_id, caption_status = ensure_manual_caption(youtube, video_id, srt, checkpoint)
        checkpoint.update({"caption_id": caption_id, "caption_status": caption_status, "privacy": "unlisted", "processing": state["processing"], "status": "UNLISTED_PROCESSING_SUCCEEDED_MANUAL_CAPTIONS_SERVING", "verified_at": now(), "server_state": state})
        write_json(checkpoint_path, checkpoint)
        summary.append({"key": key, "video_id": video_id, "url": checkpoint["url"], "privacy": "unlisted", "processing": state["processing"], "caption_id": caption_id, "caption_status": caption_status})
        print(f"{key}: UNLISTED VERIFIED {video_id}", flush=True)
    receipt = {"marker": "NEBULAMIND_FIVE_PAPER_UNLISTED_UPLOAD_PREFLIGHT_V1" if not args.execute_unlisted else "NEBULAMIND_FIVE_PAPER_UNLISTED_UPLOAD_COMPLETE_V1", "completed_at_utc": now(), "execute_unlisted": args.execute_unlisted, "channel_id": CHANNEL_ID, "items": summary, "public_visibility_changed": False, "nebula_source_changed": False, "git_changed": False, "runtime_deployed": False}
    out = BASE / ("unlisted_upload_receipt.json" if args.execute_unlisted else "unlisted_upload_preflight.json")
    write_json(out, receipt)
    print(json.dumps(receipt, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
