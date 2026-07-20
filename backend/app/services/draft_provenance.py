"""Draft provenance — structured revision history for Lab pipeline runs.

Each Lab run already emits a ``review_loop.md`` artifact (the automated
review-revise loop) and a ``{id}.json`` metadata record. This module distils
those into a structured ``history.json`` following the DraftHistory schema, and
provides an append-only event log so *new* provenance — human feedback, gate
verdicts, cross-run lineage — can be *captured* going forward.

Honesty contract (mirrors the frontend revision-log): the only feedback source
actually recorded today is one automated referee model. Human feedback and the
other gates are represented as explicit *absences* (``captured: false``) until
something records them via :func:`append_event` — never as empty-but-pending
slots. Stdlib-only so it runs both inside the API and as a CLI backfill.

Schema (history.json)::

    {
      "runId", "model", "converged", "createdUtc",
      "lineage": {"topicSource", "topic", "parentRunId"},
      "revisions": [{
        "cycle", "feedbackSource", "feedbackBy",
        "feedbackKind": {"verdict", "categories": [...]},
        "feedbackText", "changed": {"summary", "diffStat"}, "timestamp"
      }],
      "humanFeedback": {"captured": bool, "events": [...]},
      "gates": {"captured": bool, "note": str}
    }
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

SCHEMA_VERSION = 1
EVENTS_FILE = "provenance_events.jsonl"
HISTORY_FILE = "history.json"

# ── review_loop.md parsing (Python port of the frontend parser) ──────────────
_CYCLE_RE = re.compile(
    r"##\s*Cycle\s*(\d+)\s*[—–-]\s*VERDICT:\s*([A-Z]+)\s*\n(.*?)(?=\n##\s|\Z)",
    re.DOTALL,
)
_DETAILS_OPEN = re.compile(r"<details>\s*<summary>[^<]*</summary>", re.IGNORECASE)


def _strip_details(s: str) -> str:
    s = _DETAILS_OPEN.sub("", s)
    s = re.sub(r"</details>", "", s, flags=re.IGNORECASE)
    return s.strip()


def _strip_verdict_line(s: str) -> str:
    return re.sub(r"^\s*VERDICT:\s*[A-Z]+\s*\n", "", s, flags=re.IGNORECASE).strip()


# Coarse critique-category tags derived from the referee prose. Descriptive only.
_CATEGORY_KEYWORDS: list[tuple[str, tuple[str, ...]]] = [
    ("overclaim", ("overclaim", "overstat", "too strong", "unsupported")),
    ("caveats", ("caveat", "limitation", "missing", "acknowledg")),
    ("calibration", ("calibrat", "uncalibrated", "systematic")),
    ("selection", ("selection", "bias", "sample", "completeness")),
    ("comparison", ("literature", "compar", "prior work", "existing")),
    ("methodology", ("method", "approach", "procedure", "validation")),
    ("statistics", ("statistic", "uncertaint", "error bar", "significan")),
]


def _categories(text: str) -> list[str]:
    low = text.lower()
    out = [name for name, kws in _CATEGORY_KEYWORDS if any(k in low for k in kws)]
    return out


def parse_review_loop(md: str) -> dict[str, Any]:
    """Parse a review_loop.md into {model, convergedVerdict, cycles[], final}."""
    text = md.replace("\r\n", "\n")
    m_model = re.search(r"^Model:\s*(.+?)\.\s", text, re.MULTILINE)
    model = m_model.group(1).strip() if m_model else "automated referee"
    m_conv = re.search(r"Converged to \*\*([A-Z]+)\*\*", text)
    converged = m_conv.group(1) if m_conv else None

    parts = re.split(r"\n##\s*Final manuscript body\s*\n", text, maxsplit=1)
    body = parts[0]
    final = parts[1].strip() if len(parts) > 1 else ""

    cycles: list[dict[str, Any]] = []
    for m in _CYCLE_RE.finditer(body):
        n = int(m.group(1))
        verdict = m.group(2)
        raw = m.group(3)
        det = raw.lower().find("<details>")
        feedback = raw if det < 0 else raw[:det]
        draft = "" if det < 0 else _strip_details(raw[det:])
        cycles.append(
            {"n": n, "verdict": verdict, "feedback": _strip_verdict_line(feedback), "draft": draft}
        )
    return {"model": model, "convergedVerdict": converged, "cycles": cycles, "final": final}


def _word_counts(s: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for w in re.findall(r"[a-z0-9']+", s.lower()):
        counts[w] = counts.get(w, 0) + 1
    return counts


def _draft_delta(prev: str, nxt: str) -> dict[str, int]:
    a, b = _word_counts(prev), _word_counts(nxt)
    added = sum(max(0, c - a.get(w, 0)) for w, c in b.items())
    removed = sum(max(0, c - b.get(w, 0)) for w, c in a.items())
    return {"added": added, "removed": removed}


# ── event log (the capture primitive) ────────────────────────────────────────
def append_event(run_dir: Path, event: dict[str, Any]) -> None:
    """Append one provenance event (human feedback / gate / lineage) — the
    capture hook a worker, an API endpoint, or the CLI calls when new provenance
    occurs. Append-only JSONL so history is never rewritten in place."""
    run_dir.mkdir(parents=True, exist_ok=True)
    with (run_dir / EVENTS_FILE).open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(event, ensure_ascii=False) + "\n")


def _read_events(run_dir: Path) -> list[dict[str, Any]]:
    p = run_dir / EVENTS_FILE
    if not p.exists():
        return []
    out = []
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except Exception:
            continue
    return out


# ── history assembly ─────────────────────────────────────────────────────────
def build_history(rid: str, run_dir: Path, meta: dict[str, Any]) -> dict[str, Any]:
    """Assemble the structured DraftHistory from a run's artifacts + metadata +
    recorded events. Read-only; safe to call on demand."""
    spec = meta.get("spec") or {}
    result = meta.get("result") or {}
    model = result.get("review_model") or "automated referee"

    revisions: list[dict[str, Any]] = []
    loop_path = run_dir / "review_loop.md"
    if loop_path.exists():
        loop = parse_review_loop(loop_path.read_text(encoding="utf-8"))
        model = loop.get("model") or model
        cyc = loop["cycles"]
        for i, c in enumerate(cyc):
            if i == 0:
                changed = {"summary": "first automated pass — draft not yet revised", "diffStat": None}
            else:
                stat = _draft_delta(cyc[i - 1]["draft"], c["draft"])
                unchanged = stat["added"] == 0 and stat["removed"] == 0
                changed = {
                    "summary": "draft unchanged" if unchanged else f"+{stat['added']} / -{stat['removed']} words vs previous cycle",
                    "diffStat": stat,
                }
            revisions.append({
                "cycle": c["n"],
                "feedbackSource": "referee-model",
                "feedbackBy": model,
                "feedbackKind": {"verdict": c["verdict"], "categories": _categories(c["feedback"])},
                "feedbackText": c["feedback"],
                "changed": changed,
                "timestamp": None,
            })

    # Fold in recorded events (human feedback, gates, lineage) as extra revisions.
    events = _read_events(run_dir)
    human_events = [e for e in events if e.get("feedbackSource") == "human"]
    gate_events = [e for e in events if e.get("feedbackSource", "").endswith("-gate")]
    lineage_events = [e for e in events if e.get("type") == "lineage"]
    for e in events:
        if e.get("feedbackSource") in ("human",) or str(e.get("feedbackSource", "")).endswith("-gate"):
            revisions.append({
                "cycle": e.get("cycle"),
                "feedbackSource": e.get("feedbackSource"),
                "feedbackBy": e.get("feedbackBy", "unknown"),
                "feedbackKind": {"verdict": e.get("verdict"), "categories": e.get("categories", [])},
                "feedbackText": e.get("feedbackText", ""),
                "changed": e.get("changed", {"summary": "", "diffStat": None}),
                "timestamp": e.get("timestamp"),
            })

    parent = next((e.get("parentRunId") for e in lineage_events if e.get("parentRunId")), None)
    return {
        "schemaVersion": SCHEMA_VERSION,
        "runId": rid,
        "model": model,
        "converged": result.get("review_verdict"),
        "createdUtc": meta.get("created_utc"),
        "lineage": {
            "topicSource": spec.get("topic_source"),
            "topic": spec.get("topic"),
            "parentRunId": parent,
        },
        "revisions": revisions,
        # Explicit absences — captured only becomes true once events exist.
        "humanFeedback": {"captured": bool(human_events), "events": human_events},
        "gates": {
            "captured": bool(gate_events),
            "events": gate_events,
            "note": "novelty / expected-value / citation gates are not instrumented in this pipeline",
        },
    }


def write_history_json(rid: str, runs_dir: Path) -> Path | None:
    """(Re)build history.json for one run and write it into the run dir so the
    existing artifact endpoint serves it at /artifact/history.json."""
    meta_path = runs_dir / f"{rid}.json"
    run_dir = runs_dir / rid
    if not meta_path.exists() or not run_dir.is_dir():
        return None
    try:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    except Exception:
        return None
    hist = build_history(rid, run_dir, meta)
    out = run_dir / HISTORY_FILE
    out.write_text(json.dumps(hist, ensure_ascii=False, indent=2), encoding="utf-8")
    # mirror into the metadata artifact list so list_runs can advertise it
    arts = meta.get("artifacts") or []
    if HISTORY_FILE not in arts:
        meta["artifacts"] = arts + [HISTORY_FILE]
        meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    return out


def backfill(runs_dir: Path) -> list[str]:
    """Generate history.json for every completed run. Returns run ids written."""
    written = []
    for meta_path in runs_dir.glob("*.json"):
        rid = meta_path.stem
        if write_history_json(rid, runs_dir):
            written.append(rid)
    return written


# ── CLI ──────────────────────────────────────────────────────────────────────
def _main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(description="Draft provenance backfill / capture")
    ap.add_argument("--runs-dir", required=True, help="LAB_RUNS_DIR path")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("backfill", help="write history.json for all runs")
    rec = sub.add_parser("record", help="record a provenance event, then rebuild history")
    rec.add_argument("--run", required=True)
    rec.add_argument("--source", default="human", help="human | novelty-gate | citation-gate | expected-value-gate")
    rec.add_argument("--by", required=True, help="who gave the feedback (e.g. a person)")
    rec.add_argument("--verdict", default=None)
    rec.add_argument("--kind", default="", help="comma-separated categories")
    rec.add_argument("--text", required=True)

    args = ap.parse_args(argv)
    runs_dir = Path(args.runs_dir)
    if args.cmd == "backfill":
        ids = backfill(runs_dir)
        print(f"wrote history.json for {len(ids)} runs")
        return 0
    if args.cmd == "record":
        append_event(runs_dir / args.run, {
            "feedbackSource": args.source,
            "feedbackBy": args.by,
            "verdict": args.verdict,
            "categories": [c.strip() for c in args.kind.split(",") if c.strip()],
            "feedbackText": args.text,
            "changed": {"summary": "", "diffStat": None},
            "timestamp": None,
        })
        write_history_json(args.run, runs_dir)
        print(f"recorded {args.source} feedback on {args.run} by {args.by}")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(_main())
