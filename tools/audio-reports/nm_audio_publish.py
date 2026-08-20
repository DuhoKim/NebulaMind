#!/usr/bin/env python3
"""nm_audio_publish.py — publish one rendered reading into the audio system.

Replaces the single-slot latest.mp3 latch that silently dropped readings: three
Fable reports landed 4-5 s apart while every consumer polls at 8 s, so bursts
delivered only the last one (measured 2026-08-19). Publishing now appends to a
monotonic queue (queue.json, atomic mv) that consumers drain in order.

Also owns what nm_status_say.sh used to forget:
- transcript sidecar (<stem>.txt) — its absence had silently killed alignment
  and page transcripts for every reading since 08-16;
- quiet hours (22:30-08:00 KST): render + queue with quiet=true, and do NOT
  move the legacy latest.mp3/latest.txt latch — old daemons only wake on the
  latch, so a quiet night stays a silent night by construction;
- speaker identity from voices.json, so pages can say WHO is speaking;
- background alignment spawn (needs the transcript it just wrote).

Prints a one-line JSON result {seq, quiet, file} for the shell wrapper.
"""
from __future__ import annotations
import argparse, datetime, fcntl, json, os, pathlib, subprocess, sys, tempfile

R = pathlib.Path("/Users/duhokim/HermesOps/reports/status-audio")
QUEUE = R / "queue.json"
QUEUE_SEQ = R / "queue.seq"      # durable seq floor: survives a corrupt queue.json
QUEUE_LOCK = R / ".queue.lock"   # three Fables can publish concurrently
VOICES = R / "voices.json"
QUEUE_KEEP = 50
KST = datetime.timezone(datetime.timedelta(hours=9))


def atomic_write(path: pathlib.Path, data: str) -> None:
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=f".{path.name}.")
    try:
        with os.fdopen(fd, "w") as f:
            f.write(data)
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def in_quiet_hours(now_kst: datetime.datetime) -> bool:
    if os.environ.get("NM_QUIET_OFF") == "1":
        return False
    hm = now_kst.hour * 60 + now_kst.minute
    return hm >= 22 * 60 + 30 or hm < 8 * 60


def duration_of(mp3: pathlib.Path) -> float | None:
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
             "-of", "csv=p=0", str(mp3)],
            capture_output=True, text=True, timeout=20)
        return round(float(out.stdout.strip()), 2)
    except Exception:
        return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mp3", help="rendered mp3 inside the status-audio dir")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--speaker", default="system", help="seat key in voices.json")
    ap.add_argument("--text", default=None, help="the spoken text (transcript)")
    ap.add_argument("--force-live", action="store_true",
                    help="publish as non-quiet even inside quiet hours")
    a = ap.parse_args()

    mp3 = pathlib.Path(a.mp3).resolve()
    if not mp3.exists() or mp3.parent != R:
        sys.exit(f"mp3 must exist inside {R}: {mp3}")

    try:
        voices = json.loads(VOICES.read_text())
    except Exception:
        voices = {}
    meta = voices.get(a.speaker) or {}

    now_utc = datetime.datetime.now(datetime.timezone.utc)
    now_kst = now_utc.astimezone(KST)
    quiet = in_quiet_hours(now_kst) and not a.force_live

    # transcript sidecar first — alignment and the pages depend on it.
    # The caption is the DISPLAY copy: digits, not spelled-out numbers
    # (Duho's standing rule — the spoken text leaks into the caption verbatim,
    # so "three hundred forty six" was showing up in the archive).
    transcript = None
    caption_fixes = 0
    if a.text:
        try:
            sys.path.insert(0, str(R.parent.parent / "scripts"))
            import nm_caption_norm
            caption, caption_fixes = nm_caption_norm.normalize(a.text.strip())
        except Exception:
            caption = a.text.strip()
        transcript = mp3.with_suffix(".txt")
        atomic_write(transcript, caption + "\n")
        if caption_fixes:
            print(f"[caption: {caption_fixes} spelled-out number/letter-run normalized to digits]",
                  file=sys.stderr)

    # queue update under an exclusive lock — the 08-19 Fable trio published
    # 4 s apart; unlocked read-modify-replace would hand out duplicate seqs.
    lock_fh = open(QUEUE_LOCK, "w")
    fcntl.lockf(lock_fh, fcntl.LOCK_EX)
    try:
        q = json.loads(QUEUE.read_text())
    except Exception:
        q = {"version": 1, "seq": 0, "entries": []}
    # a corrupt queue.json must not reset seq to 0 (consumers with a higher
    # state would go permanently silent) — queue.seq is the durable floor
    try:
        seq_floor = int(QUEUE_SEQ.read_text().strip())
    except Exception:
        seq_floor = 0
    q["seq"] = max(int(q.get("seq", 0)), seq_floor) + 1
    entry = {
        "seq": q["seq"],
        "file": mp3.name,
        "slug": a.slug,
        "speaker": a.speaker,
        "name": meta.get("name", a.speaker.title()),
        "voice": meta.get("voice"),
        "color": meta.get("color"),
        "stamp_utc": now_utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "stamp_kst": now_kst.strftime("%Y-%m-%d %H:%M:%S KST"),
        "quiet": quiet,
        "transcript": transcript.name if transcript else None,
        "caption_normalized": caption_fixes,
        "duration_s": duration_of(mp3),
    }
    q["entries"] = (q.get("entries", []) + [entry])[-QUEUE_KEEP:]
    q["updated_utc"] = entry["stamp_utc"]
    atomic_write(QUEUE, json.dumps(q, ensure_ascii=False, indent=1) + "\n")
    atomic_write(QUEUE_SEQ, str(q["seq"]) + "\n")

    # legacy latch — only for live readings, mp3 before txt, both atomic
    if not quiet:
        tmp = R / f".latest.mp3.{os.getpid()}"
        tmp.write_bytes(mp3.read_bytes())
        os.replace(tmp, R / "latest.mp3")
        if a.text:
            atomic_write(R / "latest_transcript.txt", (caption if transcript else a.text.strip()) + "\n")
        atomic_write(R / "latest.txt",
                     f"{entry['stamp_kst']}  {mp3.name}\n")

    fcntl.lockf(lock_fh, fcntl.LOCK_UN)
    lock_fh.close()

    # alignment in the background (harmless if faster_whisper is missing)
    if transcript:
        subprocess.Popen(
            [sys.executable, str(R.parent.parent / "scripts" / "nm_audio_align.py"), mp3.stem],
            stdout=open(R / "align.log", "a"), stderr=subprocess.STDOUT)

    print(json.dumps({"seq": entry["seq"], "quiet": quiet, "file": mp3.name}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
