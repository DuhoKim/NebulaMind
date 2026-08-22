#!/usr/bin/env python3
"""Match base.en backfill captions to the documents they narrate.

'The original written text was not saved' is only half-true for narration-type
readings: the narrated document survives and is authored text. This finds those
pairs by 5-word-shingle overlap, so garbled captions can be repaired against
their sources instead of guessed at.

Output is a REPORT, not edits. Coverage = fraction of a caption's shingles found
in the candidate source, so a note that merely quotes a caption scores low while
a narrated source scores high. Captions with no strong source are listed too —
absence of a source is a finding, not a silent drop.
"""
import json, re, sys, pathlib, collections

AUDIO = pathlib.Path("/Users/duhokim/HermesOps/reports/status-audio")
SRC_ROOT = pathlib.Path(__file__).resolve().parent
K = 5                      # shingle width, words
# Bands calibrated against two hand-proven pairs, not chosen a priori:
# spin-converge -> LANA assessment is a PROVEN narration and scores 0.239;
# all-verdicts -> GORU verdict is PROVEN (partial narration) and scores 0.078.
# Garbled ASR breaks shingles, so real sources score low; the first version
# labelled one proven pair WEAK and the other NO_SOURCE.
STRONG, LIKELY, CAND = 0.30, 0.12, 0.05

def toks(text):
    return [w for w in re.findall(r"[a-z']+", text.lower()) if len(w) > 2]

def shingles(text):
    t = toks(text)
    return {hash(" ".join(t[i:i+K])) for i in range(len(t) - K + 1)}

def main():
    # 1. the backfills
    caps = []
    for p in sorted(AUDIO.glob("*.asr.json")):
        d = json.loads(p.read_text())
        if d.get("model") == "base.en" and "not saved" in str(d.get("note", "")):
            stem = p.name[:-len(".asr.json")]
            txt = (AUDIO / (stem + ".txt"))
            if txt.exists():
                caps.append((stem, txt.read_text(errors="replace")))
    print(f"  {len(caps)} backfill captions", file=sys.stderr)

    # 2. index the source corpus
    index = collections.defaultdict(list)          # shingle -> [source ids]
    sources = []
    for p in sorted(SRC_ROOT.rglob("*.md")):
        try:
            if p.stat().st_size > 400_000: continue
            text = p.read_text(errors="replace")
        except OSError: continue
        sid = len(sources)
        sources.append(p.relative_to(SRC_ROOT).as_posix())
        for h in shingles(text):
            index[h].append(sid)
    print(f"  {len(sources)} sources indexed, {len(index)} shingles", file=sys.stderr)

    # 3. align
    rows = []
    for stem, text in caps:
        sh = shingles(text)
        if not sh:
            rows.append({"stem": stem, "status": "EMPTY", "n_shingles": 0}); continue
        counts = collections.Counter()
        for h in sh:
            for sid in index.get(h, ()):
                counts[sid] += 1
        best = counts.most_common(2)
        row = {"stem": stem, "n_shingles": len(sh)}
        if not best:
            row["status"] = "NO_SOURCE"
        else:
            sid, n = best[0]
            cov = n / len(sh)
            row.update({"source": sources[sid], "coverage": round(cov, 3)})
            if len(best) > 1:
                row["runner_up"] = {"source": sources[best[1][0]],
                                    "coverage": round(best[1][1] / len(sh), 3)}
            row["status"] = ("STRONG" if cov >= STRONG else
                             "LIKELY" if cov >= LIKELY else
                             "CANDIDATE" if cov >= CAND else "NO_SOURCE")
        rows.append(row)

    tally = collections.Counter(r["status"] for r in rows)
    out = {"contract": [
             "STRONG: near-verbatim narration; repair against the source, not a glossary.",
             "LIKELY: calibrated true at this band (a hand-proven pair scores 0.239); read both, then repair.",
             "CANDIDATE: calibrated true as low as 0.078 for PARTIAL narration; human judgement required.",
             "NO_SOURCE: no surviving narrated document found IN THIS TREE. Not proof none exists:",
             "the corpus is the sextet handoff dir only, and ad-hoc readings never had a source.",
           ],
           "corpus": str(SRC_ROOT), "thresholds": {"strong": STRONG, "likely": LIKELY, "candidate": CAND},
           "tally": dict(tally), "rows": rows}
    pathlib.Path(SRC_ROOT / "caption_source_alignment.json").write_text(
        json.dumps(out, indent=1))
    print(f"  tally: {dict(tally)}", file=sys.stderr)

if __name__ == "__main__":
    main()
