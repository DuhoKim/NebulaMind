#!/usr/bin/env python3
"""Slice-2 dry-run calibration for page-58 paper-driven vote accumulation.

This consumes the Slice-1 dry-run artifacts, builds draft local-panel golds, and
reruns the in-memory rollup with calibrated relevance plus provisional pairwise
stance labels. It never writes to the production DB.
"""
from __future__ import annotations

import argparse
import collections
import datetime as dt
import hashlib
import json
import os
import random
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path
from typing import Any

from sqlalchemy import create_engine, text
from sklearn.metrics import f1_score

_SCRIPT_BACKEND_ROOT = Path(__file__).resolve().parents[1]
if str(_SCRIPT_BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_BACKEND_ROOT))

from app.services.sentence_trust import project_sentence_trust  # noqa: E402


REPO_ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = REPO_ROOT / "docs"
SLICE1_DEFAULT = DOCS_ROOT / "page58_sentence_vote_staking_dry_run_20260622T090031Z"
OLLAMA_BASE = os.getenv("PAGE58_STAKING_OLLAMA_BASE", "http://localhost:11434").rstrip("/")
DSN = os.getenv("DATABASE_URL", "postgresql://nebula:nebula@localhost:5432/nebulamind")
QWEN_PANEL = "qwen3.6:27b-nvfp4"
GPT_PANEL = "gpt-oss:20b"
CLAUDE_CAP = 15
RNG = random.Random(5802)


def utc_stamp() -> str:
    return dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def extract_json(raw: str) -> dict[str, Any]:
    raw = raw.strip()
    try:
        return json.loads(raw)
    except Exception:
        pass
    match = re.search(r"\{.*\}", raw, re.S)
    if match:
        return json.loads(match.group(0))
    raise ValueError("no parseable JSON")


def ollama_items(model: str, system: str, rows: list[dict[str, Any]], timeout: int) -> dict[str, dict[str, Any]]:
    if not rows:
        return {}
    user = "Rows JSON:\n" + json.dumps(rows, ensure_ascii=False)
    payload = {
        "model": model,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        "stream": False,
        "format": "json",
        "think": False,
        "options": {"temperature": 0},
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(f"{OLLAMA_BASE}/api/chat", data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        raw = json.loads(response.read().decode("utf-8"))
    content = ((raw.get("message") or {}).get("content") or "").strip()
    try:
        obj = extract_json(content)
    except Exception:
        return {}
    out: dict[str, dict[str, Any]] = {}
    for item in obj.get("items") or []:
        if isinstance(item, dict) and "id" in item:
            out[str(item["id"])] = item
    return out


def claude_label(task: str, row: dict[str, Any], timeout: int) -> dict[str, Any]:
    env = {k: v for k, v in os.environ.items() if "ANTHROPIC" not in k.upper() and k != "NM_ANTHROPIC_API_KEY"}
    prompt = (
        "Return strict JSON only. "
        f"Task={task}. Row={json.dumps(row, ensure_ascii=False)}. "
        "For stance labels use supports|contradicts|neither. For relevance use bears_on|not_bears_on."
    )
    result = subprocess.run(["claude", "-p", prompt], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout, env=env)
    if result.returncode != 0:
        raise RuntimeError(result.stderr[:500])
    return extract_json(result.stdout)


def check_claude(timeout: int) -> bool:
    try:
        result = subprocess.run(
            ["claude", "-p", "Return exactly: CLAUDE_PLAN_LANE_OK"],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            env={k: v for k, v in os.environ.items() if "ANTHROPIC" not in k.upper() and k != "NM_ANTHROPIC_API_KEY"},
        )
        return result.returncode == 0 and "CLAUDE_PLAN_LANE_OK" in result.stdout
    except Exception:
        return False


def batch_panel(task: str, candidates: list[dict[str, Any]], labels: list[str], timeout: int, limit: int | None = None) -> list[dict[str, Any]]:
    rows = candidates[: limit or len(candidates)]
    system = (
        "You are a strict astronomy labeling panel. Return JSON only as "
        "{\"items\":[{\"id\":\"...\",\"label\":\"LABEL\",\"confidence\":0.0,\"reason\":\"short\"}]}. "
        f"Allowed labels: {', '.join(labels)}. Task: {task}."
    )
    out: list[dict[str, Any]] = []
    for offset in range(0, len(rows), 10):
        chunk = rows[offset : offset + 10]
        payload = [
            {
                "id": row["gold_id"],
                "intro_assertion": row.get("intro_sentence"),
                "base_sentence": row.get("base_sentence"),
                "max_cosine": row.get("max_cosine"),
            }
            for row in chunk
        ]
        qwen = ollama_items(QWEN_PANEL, system, payload, timeout)
        gpt = ollama_items(GPT_PANEL, system, payload, timeout)
        for row in chunk:
            q = normalize_panel_item(qwen.get(row["gold_id"]), labels)
            g = normalize_panel_item(gpt.get(row["gold_id"]), labels)
            out.append({**row, "qwen_label": q["label"], "qwen_confidence": q["confidence"], "qwen_reason": q["reason"],
                        "gpt_label": g["label"], "gpt_confidence": g["confidence"], "gpt_reason": g["reason"]})
    return out


def normalize_panel_item(item: dict[str, Any] | None, labels: list[str]) -> dict[str, Any]:
    if not item:
        return {"label": labels[-1], "confidence": 0.0, "reason": "missing"}
    label = str(item.get("label") or labels[-1]).strip().lower()
    if label not in labels:
        label = labels[-1]
    try:
        conf = float(item.get("confidence") or 0.0)
    except (TypeError, ValueError):
        conf = 0.0
    return {"label": label, "confidence": conf, "reason": str(item.get("reason") or "")[:220]}


def finalize_stance_gold(rows: list[dict[str, Any]], timeout: int) -> tuple[list[dict[str, Any]], int]:
    claude_used = 0
    final: list[dict[str, Any]] = []
    for row in rows:
        label = row["qwen_label"]
        source = "qwen_gpt_agree" if row["qwen_label"] == row["gpt_label"] else "qwen_default"
        claude_obj = None
        if row["qwen_label"] != row["gpt_label"] and claude_used < CLAUDE_CAP:
            claude_obj = claude_label("stance", row, timeout)
            candidate = str(claude_obj.get("label") or "").strip().lower()
            if candidate in {"supports", "contradicts", "neither"}:
                label = candidate
                source = "claude_tiebreak"
            claude_used += 1
        final.append({**row, "draft_label": label, "label_source": source, "claude_tiebreak": claude_obj})
    return final, claude_used


def finalize_binary_gold(rows: list[dict[str, Any]], positive: str) -> list[dict[str, Any]]:
    final = []
    for row in rows:
        if row["qwen_label"] == row["gpt_label"]:
            label = row["qwen_label"]
            source = "qwen_gpt_agree"
        else:
            label = row["qwen_label"] if row["qwen_confidence"] >= row["gpt_confidence"] else row["gpt_label"]
            source = "higher_confidence_panel"
        final.append({**row, "draft_label": label, "label_source": source, "is_positive": label == positive})
    return final


def split_by_paper(rows: list[dict[str, Any]], tune_frac: float = 0.7) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    papers = sorted({row["arxiv_id"] for row in rows})
    RNG.shuffle(papers)
    tune_papers = set(papers[: max(1, int(len(papers) * tune_frac))])
    return [row for row in rows if row["arxiv_id"] in tune_papers], [row for row in rows if row["arxiv_id"] not in tune_papers]


def f1_binary(rows: list[dict[str, Any]], threshold: float) -> float:
    y_true = [bool(row["is_positive"]) for row in rows]
    y_pred = [float(row["max_cosine"]) >= threshold for row in rows]
    return f1_score(y_true, y_pred, zero_division=0)


def calibrate_tau_rel(rows: list[dict[str, Any]]) -> dict[str, Any]:
    tune, validate = split_by_paper(rows)
    candidates = [round(0.30 + i * 0.01, 2) for i in range(61)]
    best = max(candidates, key=lambda tau: (f1_binary(tune, tau), -abs(tau - 0.55)))
    return {"tau_rel": best, "tune_f1": round(f1_binary(tune, best), 4), "validate_f1": round(f1_binary(validate, best), 4),
            "tune_rows": len(tune), "validate_rows": len(validate)}


def calibrate_tau_vote(rows: list[dict[str, Any]]) -> dict[str, Any]:
    tune, validate = split_by_paper(rows)
    candidates = [round(0.45 + i * 0.05, 2) for i in range(10)]
    def score(subset: list[dict[str, Any]], tau: float) -> float:
        y_true = [row["draft_label"] in {"supports", "contradicts"} for row in subset]
        y_pred = [max(float(row["qwen_confidence"]), float(row["gpt_confidence"])) >= tau and row["draft_label"] in {"supports", "contradicts"} for row in subset]
        return f1_score(y_true, y_pred, zero_division=0)
    best = max(candidates, key=lambda tau: (score(tune, tau), -abs(tau - 0.70)))
    return {"tau_vote": best, "tune_f1": round(score(tune, best), 4), "validate_f1": round(score(validate, best), 4),
            "tune_rows": len(tune), "validate_rows": len(validate), "provisional": True}


def hydrate_base_rows(base_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if not base_rows:
        return base_rows
    page_version_id = int(base_rows[0]["page_version_id"])
    engine = create_engine(DSN)
    with engine.connect() as conn:
        trust = {
            int(row["sentence_index"]): dict(row)
            for row in conn.execute(
                text(
                    """
                    SELECT sentence_index, trust_level, settled_votes, contested_votes
                    FROM sentence_trust
                    WHERE page_version_id=:pv
                    """
                ),
                {"pv": page_version_id},
            ).mappings()
        }
        sources: dict[int, set[str]] = collections.defaultdict(set)
        for row in conn.execute(
            text(
                """
                SELECT sentence_index, arxiv_id
                FROM sentence_provenance
                WHERE page_version_id=:pv AND arxiv_id IS NOT NULL
                """
            ),
            {"pv": page_version_id},
        ).mappings():
            sources[int(row["sentence_index"])].add(str(row["arxiv_id"]))
    hydrated = []
    for row in base_rows:
        idx = int(row["sentence_index"])
        db_row = trust.get(idx, {})
        hydrated.append({
            **row,
            "baseline_trust_level": db_row.get("trust_level", row.get("baseline_trust_level")),
            "baseline_settled_votes": int(db_row.get("settled_votes", row.get("baseline_settled_votes") or 0)),
            "baseline_contested_votes": int(db_row.get("contested_votes", row.get("baseline_contested_votes") or 0)),
            "existing_arxiv_ids": sorted(sources[idx]),
        })
    return hydrated


def load_slice1(path: Path) -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    return (
        json.loads((path / "summary.json").read_text(encoding="utf-8")),
        read_jsonl(path / "vote_candidates.jsonl"),
        read_jsonl(path / "emergent_pool.jsonl"),
        hydrate_base_rows(read_jsonl(path / "would_be_sentence_trust.jsonl")),
    )


def sample_gold_inputs(votes: list[dict[str, Any]], emergent: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    sorted_votes = sorted(votes, key=lambda r: float(r.get("max_cosine") or 0.0), reverse=True)
    stance_pool = sorted_votes[:45] + sorted_votes[len(sorted_votes)//3:len(sorted_votes)//3 + 25] + sorted_votes[-20:]
    stance_pool = stance_pool[:90]
    rel_pool = sorted_votes[:60] + sorted(emergent, key=lambda r: float(r.get("max_cosine") or 0.0), reverse=True)[:60]
    tone_pool = (sorted_votes[:30] + emergent[:30])[:60]
    def stamp(rows: list[dict[str, Any]], prefix: str) -> list[dict[str, Any]]:
        out = []
        for i, row in enumerate(rows):
            out.append({**row, "gold_id": f"{prefix}-{i:03d}", "base_sentence": row.get("base_sentence") or row.get("nearest_base_sentence")})
        return out
    return stamp(stance_pool, "stance"), stamp(rel_pool, "rel"), stamp(tone_pool, "tone")


def classify_all_stance(votes: list[dict[str, Any]], timeout: int) -> list[dict[str, Any]]:
    rows = [{**row, "gold_id": f"all-{i:04d}"} for i, row in enumerate(votes)]
    labeled = batch_panel("Pairwise stance: does the intro assertion support, contradict, or neither the base sentence?", rows, ["supports", "contradicts", "neither"], timeout)
    final = []
    for row in labeled:
        if row["qwen_label"] == row["gpt_label"]:
            label = row["qwen_label"]
        else:
            label = row["qwen_label"] if row["qwen_confidence"] >= row["gpt_confidence"] else row["gpt_label"]
        conf = max(float(row["qwen_confidence"]), float(row["gpt_confidence"]))
        final.append({**row, "stance_label": label, "stance_confidence": conf, "stance_classifier": "local_panel_provisional_no_claude_for_full_pass"})
    return final


def reroll(base_rows: list[dict[str, Any]], stance_rows: list[dict[str, Any]], tau_rel: float, tau_vote: float, drop_con: bool = False) -> list[dict[str, Any]]:
    by_idx = {int(row["sentence_index"]): row for row in base_rows}
    grouped = {idx: {"pro": 0, "con": 0, "papers": set(), "skipped_seed_dupes": 0} for idx in by_idx}
    best: dict[tuple[int, str], dict[str, Any]] = {}
    for row in stance_rows:
        if float(row.get("max_cosine") or 0.0) < tau_rel:
            continue
        if float(row.get("stance_confidence") or 0.0) < tau_vote:
            continue
        if row["stance_label"] not in {"supports", "contradicts"}:
            continue
        idx = int(row["sentence_index"])
        key = (idx, str(row["arxiv_id"]))
        prior = best.get(key)
        if not prior or float(row["stance_confidence"]) > float(prior["stance_confidence"]):
            best[key] = row
    for (idx, arxiv_id), row in best.items():
        existing = set(by_idx[idx].get("existing_arxiv_ids") or [])
        if arxiv_id in existing:
            grouped[idx]["skipped_seed_dupes"] += 1
            continue
        if row["stance_label"] == "contradicts" and drop_con:
            continue
        grouped[idx]["papers"].add(arxiv_id)
        if row["stance_label"] == "supports":
            grouped[idx]["pro"] += 1
        elif row["stance_label"] == "contradicts":
            grouped[idx]["con"] += 1
    out = []
    for idx, base in by_idx.items():
        g = grouped[idx]
        pro = int(base["baseline_settled_votes"]) + g["pro"]
        con = int(base["baseline_contested_votes"]) + g["con"]
        sources = len(set(base.get("existing_arxiv_ids") or []) | g["papers"])
        projection = project_sentence_trust(
            settled_votes=pro,
            contested_votes=con,
            distinct_sources=sources,
        )
        out.append({**base, "slice2_new_pro_votes": g["pro"], "slice2_new_con_votes": g["con"], "seed_duplicate_stakes_skipped": g["skipped_seed_dupes"],
                    "slice2_settled_votes": pro, "slice2_contested_votes": con, "slice2_distinct_sources": sources,
                    "slice2_settled_share": projection["settled_share"], "slice2_trust_score": projection["trust_score"],
                    "slice2_trust_level": projection["trust_level"], "slice2_tone_tier": projection["tone_tier"],
                    "slice2_single_source": projection["single_source"], "slice2_contested_veto": projection["contested_veto"],
                    "slice2_tone_distribution": projection["tone_distribution"]})
    return out


def run(args: argparse.Namespace) -> dict[str, Any]:
    if not args.no_apply:
        raise SystemExit("Refusing to run without --no-apply")
    if os.getenv("NM_ANTHROPIC_API_KEY"):
        raise SystemExit("Refusing to run with NM_ANTHROPIC_API_KEY set")
    if not check_claude(args.timeout):
        raise SystemExit("claude -p unreachable; refusing metered fallback")
    args.out_dir.mkdir(parents=True, exist_ok=True)
    started = time.time()
    summary1, votes, emergent, base_rows = load_slice1(args.slice1_artifact)
    stance_in, rel_in, tone_in = sample_gold_inputs(votes, emergent)
    if args.smoke:
        stance_in, rel_in, tone_in = stance_in[:8], rel_in[:10], tone_in[:8]
        votes = votes[:30]

    stance_panel = batch_panel("Pairwise stance: supports, contradicts, or neither.", stance_in, ["supports", "contradicts", "neither"], args.timeout)
    stance_gold, claude_used = finalize_stance_gold(stance_panel, args.timeout)
    rel_panel = batch_panel("Pairwise relevance: does the intro assertion bear on the base sentence?", rel_in, ["bears_on", "not_bears_on"], args.timeout)
    rel_gold = finalize_binary_gold(rel_panel, "bears_on")
    tone_panel = batch_panel("Tone tier transfer: classify the assertion.", tone_in, ["consensus", "accepted", "debated", "challenged"], args.timeout)
    tone_gold = finalize_binary_gold(tone_panel, "accepted")
    tone_labels = ["consensus", "accepted", "debated", "challenged"]
    tone_true = [row["draft_label"] for row in tone_gold]
    tone_qwen = [row["qwen_label"] for row in tone_gold]
    tone_gpt = [row["gpt_label"] for row in tone_gold]
    tone_qwen_f1 = round(f1_score(tone_true, tone_qwen, labels=tone_labels, average="macro", zero_division=0), 4)
    tone_gpt_f1 = round(f1_score(tone_true, tone_gpt, labels=tone_labels, average="macro", zero_division=0), 4)

    rel_cal = calibrate_tau_rel(rel_gold)
    stance_cal = calibrate_tau_vote(stance_gold)
    stance_all = classify_all_stance(votes, args.timeout)
    roll = reroll(base_rows, stance_all, rel_cal["tau_rel"], stance_cal["tau_vote"])
    roll_no_con = reroll(base_rows, stance_all, rel_cal["tau_rel"], stance_cal["tau_vote"], drop_con=True)
    roll_low = reroll(base_rows, stance_all, rel_cal["tau_rel"], max(0.0, stance_cal["tau_vote"] - 0.1))
    roll_high = reroll(base_rows, stance_all, rel_cal["tau_rel"], min(1.0, stance_cal["tau_vote"] + 0.1))

    def changed(other: list[dict[str, Any]]) -> str:
        by_idx = {r["sentence_index"]: r for r in other}
        n = sum(1 for r in roll if r["slice2_trust_level"] != by_idx[r["sentence_index"]]["slice2_trust_level"])
        return f"{n}/{len(roll)}"

    staked_intros = len({row["arxiv_id"] for row in stance_all if row["stance_label"] in {"supports", "contradicts"} and row["stance_confidence"] >= stance_cal["tau_vote"] and row["max_cosine"] >= rel_cal["tau_rel"]})
    tier_counts = collections.Counter(row["slice2_trust_level"] for row in roll)
    summary = {
        "task": "page58_slice2_calibrated_staking_dry_run",
        "artifact_dir": str(args.out_dir),
        "slice1_artifact": str(args.slice1_artifact),
        "created_at": dt.datetime.now(dt.UTC).isoformat(),
        "git_head_observed": subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=REPO_ROOT, text=True).strip(),
        "git_head_required": "4ba9675",
        "db_write_count": 0,
        "no_apply": True,
        "local_only": True,
        "paid_lane_touched": False,
        "claude_p_reachable": True,
        "claude_p_invocations": claude_used,
        "stance_gold_status": "DRAFT_FOR_PAPA_SPOT_CHECK__PROVISIONAL_NOT_LOCKED",
        "calibration": {
            "relevance": rel_cal,
            "stance": stance_cal,
            "tone_transfer_gate": {
                "rows": len(tone_gold),
                "status": "draft_panel_labeled_gate_only_not_tuned",
                "macro_f1_qwen_vs_panel_draft": tone_qwen_f1,
                "macro_f1_gpt_vs_panel_draft": tone_gpt_f1,
                "gate_threshold": 0.70,
                "gate_passed_provisionally": max(tone_qwen_f1, tone_gpt_f1) >= 0.70,
                "note": "Draft local-panel transfer sample; not tuned. Uses panel-draft labels pending human review.",
            },
        },
        "ratios": {
            "intros_staked": f"{staked_intros}/{summary1['input_intros']}",
            "base_sentence_coverage": f"{sum(1 for r in roll if r['slice2_new_pro_votes'] + r['slice2_new_con_votes'] > 0)}/{len(roll)}",
            "settled_share": f"{sum(r['slice2_settled_votes'] for r in roll)}/{sum(r['slice2_settled_votes'] + r['slice2_contested_votes'] for r in roll)}",
        },
        "counts": {
            "stance_gold_rows": len(stance_gold),
            "relevance_gold_rows": len(rel_gold),
            "tone_transfer_gold_rows": len(tone_gold),
            "new_support_votes": sum(r["slice2_new_pro_votes"] for r in roll),
            "new_contradict_votes": sum(r["slice2_new_con_votes"] for r in roll),
            "seed_duplicate_stakes_skipped": sum(r["seed_duplicate_stakes_skipped"] for r in roll),
        },
        "trust_distribution": {k: {"count": tier_counts[k], "ratio": f"{tier_counts[k]}/{len(roll)}"} for k in sorted(tier_counts)},
        "sensitivity": {"drop_con_votes": changed(roll_no_con), "tau_vote_minus_0_10": changed(roll_low), "tau_vote_plus_0_10": changed(roll_high)},
        "elapsed_seconds": round(time.time() - started, 3),
    }
    write_jsonl(args.out_dir / "stance_gold_draft_for_papa.jsonl", stance_gold)
    write_jsonl(args.out_dir / "relevance_gold.jsonl", rel_gold)
    write_jsonl(args.out_dir / "tone_transfer_gold.jsonl", tone_gold)
    write_jsonl(args.out_dir / "pairwise_stance_predictions.jsonl", stance_all)
    write_jsonl(args.out_dir / "would_be_sentence_trust_slice2.jsonl", roll)
    write_json(args.out_dir / "summary.json", summary)
    write_report(args.out_dir / "REPORT.md", summary, roll)
    return summary


def pct(ratio: str) -> str:
    a, b = ratio.split("/")
    return f"{int(a) / int(b) * 100:.1f}%" if int(b) else "n/a"


def write_report(path: Path, summary: dict[str, Any], roll: list[dict[str, Any]]) -> None:
    lines = [
        "# Page-58 Slice-2 Calibrated Vote Dry Run",
        "",
        "Status: DRY-RUN ONLY. Stance gold is a draft for Papa spot-check; stance classifier is PROVISIONAL / NOT LOCKED.",
        "",
        "## Headline Ratios",
        f"- Intros staked: {summary['ratios']['intros_staked']} ({pct(summary['ratios']['intros_staked'])}).",
        f"- Base sentence coverage: {summary['ratios']['base_sentence_coverage']} ({pct(summary['ratios']['base_sentence_coverage'])}).",
        f"- Settled share: {summary['ratios']['settled_share']} ({pct(summary['ratios']['settled_share'])}).",
        "",
        "## Golds",
        f"- Stance draft rows: {summary['counts']['stance_gold_rows']} (Papa spot-check required before lock).",
        f"- Relevance gold rows: {summary['counts']['relevance_gold_rows']}; tau_rel={summary['calibration']['relevance']['tau_rel']} validate_F1={summary['calibration']['relevance']['validate_f1']}.",
        f"- Tone transfer gate rows: {summary['counts']['tone_transfer_gold_rows']}; provisional macro-F1 qwen={summary['calibration']['tone_transfer_gate']['macro_f1_qwen_vs_panel_draft']}, gpt={summary['calibration']['tone_transfer_gate']['macro_f1_gpt_vs_panel_draft']}, gate_passed={summary['calibration']['tone_transfer_gate']['gate_passed_provisionally']} (gate-only; not tuned).",
        "",
        "## Sensitivity",
        f"- Drop con votes: {summary['sensitivity']['drop_con_votes']}.",
        f"- tau_vote -0.10: {summary['sensitivity']['tau_vote_minus_0_10']}.",
        f"- tau_vote +0.10: {summary['sensitivity']['tau_vote_plus_0_10']}.",
        "",
        "## Per-Sentence Projection",
    ]
    for row in roll:
        lines.extend([
            f"### Sentence {row['sentence_index']}",
            row["sentence_text"],
            f"- New votes: +{row['slice2_new_pro_votes']} / -{row['slice2_new_con_votes']}; seed duplicate stakes skipped {row['seed_duplicate_stakes_skipped']}.",
            f"- Would-be trust: {row['slice2_trust_level']} (settled share {row['slice2_settled_share']}; "
            f"tone {row['slice2_tone_tier']}; contested_veto={row['slice2_contested_veto']}).",
            "",
        ])
    lines.extend([
        "## Containment",
        f"- db_write_count={summary['db_write_count']}",
        f"- paid_lane_touched={summary['paid_lane_touched']}",
        f"- local_only={summary['local_only']}",
        f"- claude_p_invocations={summary['claude_p_invocations']}",
    ])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-apply", action="store_true")
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument("--timeout", type=int, default=240)
    parser.add_argument("--slice1-artifact", type=Path, default=SLICE1_DEFAULT)
    parser.add_argument("--out-dir", type=Path, default=DOCS_ROOT / f"page58_slice2_calibrated_staking_{utc_stamp()}")
    args = parser.parse_args()
    summary = run(args)
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
