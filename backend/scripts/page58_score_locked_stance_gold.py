#!/usr/bin/env python3
"""Score the local Page-58 stance gate against Papa-locked gold.

Read-only scoring report only. The local gate under test is the Slice-2
production dry-run gate: cosine relatedness threshold plus no-Claude local
qwen/gpt stance prediction stored on the locked rows.
"""
from __future__ import annotations

import collections
import datetime as dt
import hashlib
import json
import os
import subprocess
from pathlib import Path
from typing import Any
from urllib.request import urlopen


REPO_ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = REPO_ROOT / "docs"
REBALANCE_DIR = DOCS_ROOT / "page58_slice2b_stance_gold_rebalance_20260623T043618Z"
LOCKED_GOLD = REBALANCE_DIR / "stance_gold_LOCKED_v1.jsonl"
SLICE2_SUMMARY = DOCS_ROOT / "page58_slice2_calibrated_staking_20260622T111621Z" / "summary.json"
EXPECTED_HEAD = "4ba9675"
EXPECTED_GOLD_SHA = "de7ec421d5092e5cccb7a1b70af4fc84463aaad08164a30c8e2a2eadd0bdbe27"
HEALTH_URL = "http://localhost:8000/api/health"


def utc_stamp() -> str:
    return dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_head() -> str:
    return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=REPO_ROOT, text=True).strip()


def health_status() -> dict[str, Any]:
    with urlopen(HEALTH_URL, timeout=5) as response:
        return {"url": HEALTH_URL, "status_code": response.status, "body": json.loads(response.read().decode("utf-8"))}


def assert_containment() -> dict[str, Any]:
    if os.getenv("NM_ANTHROPIC_API_KEY"):
        raise SystemExit("Refusing to score with NM_ANTHROPIC_API_KEY set")
    head = git_head()
    if head != EXPECTED_HEAD:
        raise SystemExit(f"Refusing to score on git HEAD {head}; expected {EXPECTED_HEAD}")
    locked_sha = sha256_file(LOCKED_GOLD)
    if locked_sha != EXPECTED_GOLD_SHA:
        raise SystemExit(f"Locked gold sha mismatch: {locked_sha}; expected {EXPECTED_GOLD_SHA}")
    health = health_status()
    if health["status_code"] != 200:
        raise SystemExit(f"/api/health not 200: {health}")
    return {
        "nm_head": head,
        "api_health": health,
        "locked_gold_sha256": locked_sha,
        "db_write_count": 0,
        "paid_lane_touched": False,
        "no_db_apply": True,
        "no_alembic": True,
        "no_page57_or_page58_live_write": True,
        "no_stance_lock_write": True,
    }


def pred_stage2(row: dict[str, Any]) -> str | None:
    label = row.get("prior_stance_label")
    if label == "neither":
        return "related_different_facet"
    if label in {"supports", "contradicts", "related_different_facet"}:
        return str(label)
    return None


def metric_for(labels: list[str], y_true: list[str], y_pred: list[str]) -> dict[str, Any]:
    matrix = {t: {p: 0 for p in labels} for t in labels}
    for truth, pred in zip(y_true, y_pred):
        if truth not in matrix:
            matrix[truth] = {p: 0 for p in labels}
        if pred not in matrix[truth]:
            matrix[truth][pred] = 0
        matrix[truth][pred] += 1
    per_class: dict[str, dict[str, float | int]] = {}
    for label in labels:
        tp = matrix.get(label, {}).get(label, 0)
        fp = sum(matrix.get(other, {}).get(label, 0) for other in matrix if other != label)
        fn = sum(count for pred, count in matrix.get(label, {}).items() if pred != label)
        precision = tp / (tp + fp) if tp + fp else 0.0
        recall = tp / (tp + fn) if tp + fn else 0.0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
        per_class[label] = {
            "support": sum(matrix.get(label, {}).values()),
            "precision": round(precision, 4),
            "recall": round(recall, 4),
            "f1": round(f1, 4),
        }
    return {"per_class": per_class, "confusion_matrix": matrix}


def macro_f1(per_class: dict[str, dict[str, float | int]], labels: list[str]) -> float:
    return round(sum(float(per_class[label]["f1"]) for label in labels) / len(labels), 4) if labels else 0.0


def score() -> dict[str, Any]:
    containment = assert_containment()
    rows = read_jsonl(LOCKED_GOLD)
    summary = json.loads(SLICE2_SUMMARY.read_text(encoding="utf-8"))
    tau_rel = float(summary["calibration"]["relevance"]["tau_rel"])
    tau_vote = float(summary["calibration"]["stance"]["tau_vote"])

    scored = []
    for row in rows:
        pred1 = "related" if float(row.get("max_cosine") or 0.0) >= tau_rel else "unrelated"
        pred2 = pred_stage2(row) if pred1 == "related" else None
        composite = pred2 if pred1 == "related" and pred2 else "unrelated"
        scored.append({**row, "pred_stage1_label": pred1, "pred_stage2_label": pred2, "pred_composite_label": composite})

    stage1_labels = ["related", "unrelated"]
    s1 = metric_for(stage1_labels, [r["final_stage1_label"] for r in scored], [r["pred_stage1_label"] for r in scored])
    s1["macro_f1"] = macro_f1(s1["per_class"], stage1_labels)

    related_rows = [r for r in scored if r["final_stage1_label"] == "related"]
    stage2_matrix_labels = ["supports", "contradicts", "related_different_facet", "no_stage2_prediction"]
    stage2_true = [r["final_stage2_label"] for r in related_rows]
    stage2_pred = [r["pred_stage2_label"] or "no_stage2_prediction" for r in related_rows]
    s2_all = metric_for(stage2_matrix_labels, stage2_true, stage2_pred)
    stage2_scored_classes = ["supports", "related_different_facet"]
    s2_per_class = {label: s2_all["per_class"][label] for label in stage2_scored_classes}
    s2 = {
        "rows": len(related_rows),
        "per_class_excluding_contradicts_sentinel": s2_per_class,
        "macro_f1_excluding_contradicts_sentinel": macro_f1(s2_per_class, stage2_scored_classes),
        "confusion_matrix": s2_all["confusion_matrix"],
        "contradicts_p_r_f1": "not_computed_n_equals_1_sentinel_only",
    }

    sentinel = next(r for r in scored if r["gold_id"] == "stance2b-001")
    sentinel_result = {
        "gold_id": sentinel["gold_id"],
        "true_stage1_label": sentinel["final_stage1_label"],
        "true_stage2_label": sentinel["final_stage2_label"],
        "pred_stage1_label": sentinel["pred_stage1_label"],
        "pred_stage2_label": sentinel["pred_stage2_label"],
        "correct": sentinel["final_stage1_label"] == sentinel["pred_stage1_label"] and sentinel["final_stage2_label"] == sentinel["pred_stage2_label"],
        "intro_sentence": sentinel["intro_sentence"],
        "base_sentence": sentinel["base_sentence"],
    }

    macro_rows = [r for r in scored if r["final_label"] != "contradicts"]
    macro_labels = ["supports", "related_different_facet", "unrelated"]
    macro_metric = metric_for(macro_labels, [r["final_label"] for r in macro_rows], [r["pred_composite_label"] for r in macro_rows])
    requested_macro = {
        "labels": macro_labels,
        "rows": len(macro_rows),
        "macro_f1": macro_f1(macro_metric["per_class"], macro_labels),
        "per_class": macro_metric["per_class"],
        "confusion_matrix": macro_metric["confusion_matrix"],
        "note": "Two-stage composite summary excluding the n=1 contradicts sentinel; stage-1 and stage-2 primary metrics remain separate.",
    }

    return {
        "phase": "page58_locked_stance_gold_local_gate_score",
        "created_at_utc": dt.datetime.now(dt.UTC).isoformat(),
        "gold_file": str(LOCKED_GOLD),
        "rows": len(scored),
        "reference_fields": ["final_label", "final_stage1_label", "final_stage2_label"],
        "scored_model_endpoint": {
            "stage1_relatedness_gate": {
                "name": "Slice-2 calibrated cosine relevance gate",
                "endpoint_or_source": "stored max_cosine compared with tau_rel from docs/page58_slice2_calibrated_staking_20260622T111621Z/summary.json",
                "tau_rel": tau_rel,
            },
            "stage2_stance_gate": {
                "name": "local_panel_provisional_no_claude_for_full_pass",
                "endpoint_or_source": "Ollama local chat via PAGE58_STAKING_OLLAMA_BASE default http://localhost:11434; stored prior_stance_label from classify_all_stance",
                "models": ["qwen3.6:27b-nvfp4", "gpt-oss:20b"],
                "tau_vote": tau_vote,
                "label_mapping": {"neither": "related_different_facet"},
            },
        },
        "stage1_relatedness": s1,
        "stage2_sign_related_rows_only": s2,
        "contradicts_sentinel": sentinel_result,
        "macro_f1_excluding_contradicts_sentinel": requested_macro,
        "containment": containment,
        "scope": {
            "read_only_gold": True,
            "no_certification": True,
            "kun_independent_exit_gate_required": True,
            "no_mine_024_066": True,
        },
        "prediction_counts": {
            "stage1": dict(collections.Counter(r["pred_stage1_label"] for r in scored)),
            "stage2_on_true_related": dict(collections.Counter(r["pred_stage2_label"] or "no_stage2_prediction" for r in related_rows)),
            "reference_final_label": dict(collections.Counter(r["final_label"] for r in scored)),
        },
    }


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    lines = [
        "# Page 58 Locked Stance Gold Local Gate Score",
        "",
        "Dry-run report only. Papa locked the gold; this report does not certify pass/fail.",
        "",
        "## Scored Gate",
        "",
        f"- Stage 1: cosine relatedness gate, tau_rel={report['scored_model_endpoint']['stage1_relatedness_gate']['tau_rel']}.",
        "- Stage 2: local_panel_provisional_no_claude_for_full_pass via local Ollama models qwen3.6:27b-nvfp4 + gpt-oss:20b; no Claude or paid lane.",
        "",
        "## Stage 1",
        "",
        f"- Macro-F1: {report['stage1_relatedness']['macro_f1']}",
        f"- Per-class: `{json.dumps(report['stage1_relatedness']['per_class'], sort_keys=True)}`",
        f"- Confusion matrix: `{json.dumps(report['stage1_relatedness']['confusion_matrix'], sort_keys=True)}`",
        "",
        "## Stage 2",
        "",
        f"- Rows: {report['stage2_sign_related_rows_only']['rows']}",
        f"- Macro-F1 excluding contradicts sentinel: {report['stage2_sign_related_rows_only']['macro_f1_excluding_contradicts_sentinel']}",
        f"- Per-class: `{json.dumps(report['stage2_sign_related_rows_only']['per_class_excluding_contradicts_sentinel'], sort_keys=True)}`",
        f"- Confusion matrix: `{json.dumps(report['stage2_sign_related_rows_only']['confusion_matrix'], sort_keys=True)}`",
        f"- Contradicts sentinel: `{json.dumps(report['contradicts_sentinel'], ensure_ascii=False, sort_keys=True)}`",
        "",
        "## Containment",
        "",
        f"- HEAD {report['containment']['nm_head']}; db_write_count={report['containment']['db_write_count']}; paid_lane_touched={str(report['containment']['paid_lane_touched']).lower()}; /api/health={report['containment']['api_health']['status_code']}.",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    report = score()
    stamp = utc_stamp()
    report_path = REBALANCE_DIR / f"local_stance_classifier_score_{stamp}.json"
    md_path = REBALANCE_DIR / f"local_stance_classifier_score_{stamp}.md"
    write_json(report_path, report)
    write_markdown(md_path, report)
    sha256s = {report_path.name: sha256_file(report_path), md_path.name: sha256_file(md_path)}
    print(json.dumps({"report": str(report_path), "markdown": str(md_path), "sha256s": sha256s}, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
