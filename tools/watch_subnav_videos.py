#!/usr/bin/env python3
"""Watch the crew video-delivery file; when Yui drops UNLISTED YouTube IDs, patch the Lab's
subnavVideos.ts, rebuild + redeploy the frontend, so each sub-nav explainer auto-embeds. Idempotent."""
import json, os, re, subprocess, time
DELIVERY = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/video-briefs/subnav-explainers-delivery.json"
FRONTEND = "/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend"
VIDEOS_TS = os.path.join(FRONTEND, "src/app/lab/subnavVideos.ts")
LOG = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/video-briefs/embed_watch.log"
RECEIPTS = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/video-briefs/receipts"
STEPS = ["corpus", "embedding", "clustering", "overlay", "ranking"]
YT = re.compile(r"^[A-Za-z0-9_-]{11}$")

def log(m):
    line = f"[{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}] {m}"
    print(line, flush=True); open(LOG, "a").write(line + "\n")

def norm_id(v):
    if not v: return ""
    v = str(v).strip()
    m = re.search(r"(?:v=|youtu\.be/|embed/)([A-Za-z0-9_-]{11})", v)
    if m: return m.group(1)
    return v if YT.match(v) else ""

def read_delivery():
    try:
        d = json.load(open(DELIVERY))
        return {s: norm_id(d.get(s)) for s in STEPS}
    except Exception:
        return {s: "" for s in STEPS}

def read_current():
    try:
        t = open(VIDEOS_TS).read()
        return {s: (re.search(rf'{s}:\s*"([^"]*)"', t) or [None, ""])[-1] for s in STEPS}
    except Exception:
        return {s: "" for s in STEPS}

def write_videos(ids):
    body = "\n".join(f'  {s}: "{ids[s]}",' for s in STEPS)
    open(VIDEOS_TS, "w").write(
        "// Auto-updated by tools/watch_subnav_videos.py from the crew video delivery file.\n"
        "export const SUBNAV_VIDEOS: Record<string, string> = {\n" + body + "\n};\n")

def deploy():
    r = subprocess.run(["npm", "run", "build"], cwd=FRONTEND, capture_output=True, text=True, timeout=420)
    ok = "Compiled successfully" in (r.stdout + r.stderr) or r.returncode == 0
    if ok:
        subprocess.run(["launchctl", "kickstart", "-k", f"gui/{os.getuid()}/com.nebulamind.frontend"], capture_output=True)
    return ok


def write_receipt(changed, before, merged, deployed):
    """Governance (Kun audit R3): every live-tree mutation leaves a tracked receipt."""
    os.makedirs(RECEIPTS, exist_ok=True)
    ts = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    try:
        build_id = open(os.path.join(FRONTEND, ".next/BUILD_ID")).read().strip()
    except Exception:
        build_id = None
    receipt = {
        "lane": "subnav_video_embed",
        "actor": "tools/watch_subnav_videos.py (autonomous watcher)",
        "generated_at": ts,
        "changed": changed,
        "before": before,
        "after": merged,
        "deployed": deployed,
        "build_id": build_id,
        "target": VIDEOS_TS,
        "governance": ".hermes/agents/subnav-watcher-governance.md",
    }
    path = os.path.join(RECEIPTS, f"subnav_embed_{ts}.json")
    open(path, "w").write(json.dumps(receipt, indent=1, sort_keys=True) + "\n")
    return path

def main():
    log("watching delivery file for sub-nav video IDs...")
    while True:
        delivered, current = read_delivery(), read_current()
        changed = {s: delivered[s] for s in STEPS if delivered[s] and delivered[s] != current.get(s, "")}
        if changed:
            merged = {s: (delivered[s] or current.get(s, "")) for s in STEPS}
            log(f"new IDs {changed} -> writing subnavVideos.ts + rebuilding")
            write_videos(merged)
            ok = deploy()
            receipt = write_receipt(changed, current, merged, ok)
            if ok:
                log(f"embedded {[s for s in STEPS if merged[s]]} and redeployed; receipt {receipt}")
            else:
                log(f"build failed; will retry next tick; receipt {receipt}")
        time.sleep(60)

if __name__ == "__main__":
    main()
