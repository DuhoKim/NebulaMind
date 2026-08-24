#!/usr/bin/env python3
"""Weekly watch for DESI curvature results bearing on the BHU live falsifier.

Entry 54 (Gaztanaga+ 2025, PRD 111, 103537) predicts -0.07 +/- 0.02 <= Omega_k < 0.
A confirmed flat universe kills it. DESI cosmology fits are the deciding data, so this
watches arXiv for new DESI papers constraining curvature and flags them for a human —
it never interprets a result itself.

State: seen-ids in desi_curvature_watch_state.json beside this script.
On new hits: appends one event to the autopilot feed and a row to
DESI_CURVATURE_WATCH_HITS.md. Silent when nothing is new (cron etiquette),
but always stamps last_run in the state file so a dead watch is detectable.
"""
import json, re, sys, time, urllib.request, urllib.parse, pathlib, datetime

# Absolute lane paths: the cron copy runs from ~/.hermes/scripts/, and HERE-relative
# resolution forked the state there (caught 2026-08-24: lane state stale while cron
# state showed a 429). One state, one hits file, one feed — the lane's.
LANE = pathlib.Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K")
STATE = LANE / "desi_curvature_watch_state.json"
HITS = LANE / "DESI_CURVATURE_WATCH_HITS.md"
FEED = LANE.parent / "galaxy-evolution/mastermind/autopilot-events.jsonl"
Q = ('(abs:"DESI" AND (abs:"spatial curvature" OR abs:"Omega_k" OR abs:"curvature of the universe")) '
     'OR (ti:"DESI" AND ti:"cosmological constraints")')

def main():
    state = json.loads(STATE.read_text()) if STATE.exists() else {"seen": []}
    seen = set(state["seen"])
    url = ("https://export.arxiv.org/api/query?search_query=" + urllib.parse.quote(Q) +
           "&sortBy=submittedDate&sortOrder=descending&max_results=25")
    t = None
    err = None
    for attempt in range(3):   # arXiv 429s happen on this shared IP; back off and retry
        try:
            t = urllib.request.urlopen(urllib.request.Request(
                url, headers={"User-Agent": "NebulaMind-curvature-watch/1.1 (mailto:duhokim81@gmail.com)"}),
                timeout=60).read().decode("utf-8", "replace")
            break
        except Exception as e:
            err = e
            time.sleep(40 * (attempt + 1))
    if t is None:
        state["last_run"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        state["last_error"] = str(err)[:120]
        STATE.write_text(json.dumps(state, indent=1))
        sys.exit(0)          # transient network failure: recorded (after 3 tries), not fatal
    new = []
    for e in re.findall(r"<entry>(.*?)</entry>", t, re.S):
        aid = re.sub(r"v\d+$", "", ((re.search(r"<id>(.*?)</id>", e) or [None, ""])[1]).split("/abs/")[-1])
        if not aid or aid in seen:
            continue
        ti = re.sub(r"\s+", " ", (re.search(r"<title>(.*?)</title>", e, re.S) or [None, ""])[1]).strip()
        pub = (re.search(r"<published>(.*?)</published>", e) or [None, ""])[1][:10]
        new.append((aid, pub, ti))
        seen.add(aid)
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    if new:
        with HITS.open("a") as fh:
            if HITS.stat().st_size == 0 if HITS.exists() else True:
                pass
            for aid, pub, ti in new:
                fh.write(f"- {now} · arXiv:{aid} ({pub}) — {ti}\n")
        with FEED.open("a") as fh:
            fh.write(json.dumps({"ts": now, "lane": "bhu", "actor": "tori",
                "event": "desi_curvature_candidate",
                "detail": ("Curvature watch: %d new DESI-related curvature paper(s) — a HUMAN must read "
                           "them against entry 54's window (-0.07±0.02 <= Omega_k < 0; confirmed flatness "
                           "kills it). " % len(new)) + "; ".join(
                           f"arXiv:{a} {t[:70]}" for a, _, t in new[:3])}, ensure_ascii=False) + "\n")
    state.update({"seen": sorted(seen), "last_run": now, "last_error": None, "last_new": len(new)})
    STATE.write_text(json.dumps(state, indent=1))
    if new:      # --no-agent cron: empty stdout = silent week; stdout only on news
        print(f"BHU curvature watch: {len(new)} new DESI curvature paper(s) — read against "
              f"entry 54's window (-0.07±0.02 <= Omega_k < 0):")
        for aid, pub, ti in new[:5]:
            print(f"  arXiv:{aid} ({pub}) {ti[:80]}")

if __name__ == "__main__":
    main()
