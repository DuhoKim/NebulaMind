#!/usr/bin/env python3
"""Weekly watch for DESI curvature results bearing on the BHU live falsifier.

CONDITION CORRECTED 2026-08-28. This watch spent its whole life testing the wrong
side of zero.

It previously said: "predicts -0.07 +/- 0.02 <= Omega_k < 0. A confirmed flat
universe kills it." That was copied from the abstract's compact framing and is
wrong about what falsifies the model. Tori caught it opening phase 6; every quote
below was re-read from the pinned source
(bhu-reading-20260823/sources/2505.23877_clean.txt) rather than from our notes.

What the paper actually says (Gaztanaga+ 2025, PRD 111, 103537):

  Eq. 27:  Omega_k = -(0.07 +/- 0.02) * (chi_* / chi_k)^2
  line 306: "Recall from Eq. 8 that chi_k needs to be larger than the cloud
            boundary: chi_k > chi_*."

So the factor (chi_*/chi_k)^2 is STRICTLY less than 1. Eq. 27 is a ceiling on the
magnitude, not a predicted window — Omega_k may sit anywhere between about -0.09
and zero, approaching zero arbitrarily closely as chi_k grows.

And the authors withdraw even that ceiling, line 336:

  "The limits for Omega_k above assume that the homogeneity scale is the result
   of only chi_*. ... However, if the homogeneity scale or the low value of C_2
   has a different origin, then the value of Omega_k in the floating FLRW cloud
   could be smaller. Inflation preceded by a bounce requires Omega_k < 0."

That last clause is the model's hard content. Therefore:

  REFUTED BY      a confirmed OPEN universe (Omega_k > 0), or a confirmed
                  Omega_k < -0.09 (more closed than the +1sigma ceiling)
  NOT REFUTED BY  a flat measurement. Omega_k = -0.0001 satisfies the model
                  exactly, and no finite-precision measurement excludes it.
                  Flatness is where this model is comfortable.

The entry-54 TIER ("CALIBRATED-FALSIFIER") is a separate question and is NOT
changed here. Tori proposed a demotion and declined to self-adjudicate it: the
bibliography is a gated artifact. This file only stops the watch from testing a
condition the source does not support.

DESI cosmology fits are the deciding data, so this watches arXiv for new DESI
papers constraining curvature and flags them for a human — it never interprets a
result itself.

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
                           "them against entry 54's SIGN prediction (Omega_k < 0). Refuted by a confirmed "
                           "OPEN universe (Omega_k > 0) or Omega_k < -0.09; NOT refuted by a flat result. "
                           % len(new)) + "; ".join(
                           f"arXiv:{a} {t[:70]}" for a, _, t in new[:3])}, ensure_ascii=False) + "\n")
    state.update({"seen": sorted(seen), "last_run": now, "last_error": None, "last_new": len(new)})
    STATE.write_text(json.dumps(state, indent=1))
    if new:      # --no-agent cron: empty stdout = silent week; stdout only on news
        print(f"BHU curvature watch: {len(new)} new DESI curvature paper(s) — read against "
              f"entry 54's SIGN prediction (Omega_k < 0).")
        print("  Refuted by: confirmed OPEN (Omega_k > 0), or confirmed Omega_k < -0.09.")
        print("  NOT refuted by: a flat result — flatness is consistent with the model.")
        for aid, pub, ti in new[:5]:
            print(f"  arXiv:{aid} ({pub}) {ti[:80]}")

if __name__ == "__main__":
    main()
