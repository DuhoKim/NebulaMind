#!/usr/bin/env python3
"""Dry-run C2 score for Page-58 sign-suppressed stance gate.

Configuration under test:
- Stage 1 remains the calibrated relatedness filter.
- Every Stage-1-related row auto-renders as related_different_facet.
- Every auto seed explicitly uses evidence stance "none" so it is trust-neutral.
- Local supports/contradicts are routed to human review, never auto-written.
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


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


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


def local_stage2(row: dict[str, Any]) -> str | None:
    label = row.get("prior_stance_label")
    if label == "neither":
        return "related_different_facet"
    if label in {"supports", "contradicts", "related_different_facet"}:
        return str(label)
    return None


def metric_for(labels: list[str], y_true: list[str], y_pred: list[str]) -> dict[str, Any]:
    matrix = {t: {p: 0 for p in labels} for t in labels}
    for truth, pred in zip(y_true, y_pred):
        matrix.setdefault(truth, {p: 0 for p in labels})
        matrix[truth].setdefault(pred, 0)
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


def score() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    containment = assert_containment()
    rows = read_jsonl(LOCKED_GOLD)
    summary = json.loads(SLICE2_SUMMARY.read_text(encoding="utf-8"))
    tau_rel = float(summary["calibration"]["relevance"]["tau_rel"])
    tau_vote = float(summary["calibration"]["stance"]["tau_vote"])

    scored = []
    seed_plan = []
    for row in rows:
        pred1 = "related" if float(row.get("max_cosine") or 0.0) >= tau_rel else "unrelated"
        local2 = local_stage2(row) if pred1 == "related" else None
        pred2 = "related_different_facet" if pred1 == "related" else None
        composite = pred2 if pred2 else "unrelated"
        human_queue_reason = None
        if local2 == "supports":
            human_queue_reason = "local_support_suppressed_for_human_review"
        elif local2 == "contradicts":
            human_queue_reason = "local_contradicts_suppressed_for_human_review"
        auto_seed = pred1 == "related"
        plan = {
            "gold_id": row["gold_id"],
            "arxiv_id": row.get("arxiv_id"),
            "sentence_index": row.get("sentence_index"),
            "base_sentence": row.get("base_sentence"),
            "intro_sentence": row.get("intro_sentence"),
            "max_cosine": row.get("max_cosine"),
            "final_label": row.get("final_label"),
            "pred_stage1_label": pred1,
            "local_stage2_label_suppressed": local2,
            "auto_seed": auto_seed,
            "auto_seed_label": "related_different_facet" if auto_seed else None,
            "evidence_stance_for_write": "none" if auto_seed else None,
            "stance_jury_run_at_for_write": "now()" if auto_seed else None,
            "create_jury_task": False if auto_seed else None,
            "abstract_for_write": None if auto_seed else None,
            "intro_excerpt_for_write": None if auto_seed else None,
            "trust_vote_effect": "neutral_non_voting" if auto_seed else "no_seed",
            "human_queue": human_queue_reason is not None,
            "human_queue_reason": human_queue_reason,
            "confirmed_contradiction_write_stance_if_later_human_approved": "challenges" if local2 == "contradicts" else None,
        }
        seed_plan.append(plan)
        scored.append({
            **row,
            "pred_stage1_label": pred1,
            "pred_stage2_label": pred2,
            "pred_composite_label": composite,
            "local_stage2_label_suppressed": local2,
            "human_queue_reason": human_queue_reason,
        })

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
        "auto_seed_stage2_label": sentinel["pred_stage2_label"],
        "local_stage2_label_suppressed": sentinel["local_stage2_label_suppressed"],
        "auto_trust_bearing_write": False,
        "human_queue": True,
        "safe_suppression": True,
        "correct_as_contradiction": False,
        "note": "The sign-suppressed auto pass intentionally renders the sentinel as neutral rdf and queues the local contradict for human review.",
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

    queue_counts = collections.Counter(plan["human_queue_reason"] or "not_queued" for plan in seed_plan)
    auto_counts = collections.Counter(plan["evidence_stance_for_write"] or "no_seed" for plan in seed_plan)
    report = {
        "phase": "page58_sign_suppressed_gate_c2_score",
        "created_at_utc": dt.datetime.now(dt.UTC).isoformat(),
        "gold_file": str(LOCKED_GOLD),
        "rows": len(scored),
        "reference_fields": ["final_label", "final_stage1_label", "final_stage2_label"],
        "configuration_under_test": {
            "stage1_relatedness_gate": {
                "name": "Slice-2 calibrated cosine relevance gate",
                "endpoint_or_source": "stored max_cosine compared with tau_rel from docs/page58_slice2_calibrated_staking_20260622T111621Z/summary.json",
                "tau_rel": tau_rel,
            },
            "stage2_sign_suppression": {
                "auto_seed_label_for_stage1_related": "related_different_facet",
                "explicit_evidence_stance_for_auto_seed": "none",
                "explicit_stance_jury_run_at_for_auto_seed": "now()",
                "create_jury_task_for_auto_seed": False,
                "abstract_for_auto_seed": None,
                "intro_excerpt_for_auto_seed": None,
                "trust_vote_effect": "neutral_non_voting",
                "local_supports": "human_queue_and_collapsed_to_rdf_for_auto_pass",
                "local_contradicts": "human_queue_and_collapsed_to_rdf_for_auto_pass",
                "confirmed_contradiction_write_stance_if_later_human_approved": "challenges",
                "tau_vote_not_tuned": tau_vote,
            },
            "local_sign_source_for_queue_only": {
                "name": "local_panel_provisional_no_claude_for_full_pass",
                "endpoint_or_source": "Ollama local chat via PAGE58_STAKING_OLLAMA_BASE default http://localhost:11434; stored prior_stance_label from classify_all_stance",
                "models": ["qwen3.6:27b-nvfp4", "gpt-oss:20b"],
                "label_mapping": {"neither": "related_different_facet"},
            },
        },
        "stage1_relatedness": s1,
        "stage2_sign_related_rows_only": s2,
        "contradicts_sentinel": sentinel_result,
        "macro_f1_excluding_contradicts_sentinel": requested_macro,
        "seed_plan_counts": {
            "auto_seed_rows": sum(1 for p in seed_plan if p["auto_seed"]),
            "no_seed_rows": sum(1 for p in seed_plan if not p["auto_seed"]),
            "evidence_stance_for_write": dict(auto_counts),
            "human_queue": dict(queue_counts),
            "auto_trust_bearing_writes": 0,
        },
        "c1_neutrality_guard": {
            "trust_model_counts_only": ["supports", "challenges"],
            "rdf_auto_seed_evidence_stance": "none",
            "rdf_auto_seed_stance_jury_run_at": "now()",
            "rdf_auto_seed_create_jury_task": False,
            "rdf_auto_seed_abstract": None,
            "rdf_auto_seed_intro_excerpt": None,
            "neutral_seed_can_move_trust_when_written_with_no_text_and_no_jury_task": False,
            "note": "This is page-58-local seed-write containment only; shared jury selectors/API are unchanged.",
            "no_hardcoded_contradicts_write_stance": True,
            "confirmed_contradiction_write_stance_if_later_human_approved": "challenges",
        },
        "containment": containment,
        "scope": {
            "draft_for_kun_only": True,
            "read_only_gold": True,
            "no_live_apply": True,
            "no_certification": True,
            "kun_independent_recert_required": True,
            "no_mine_024_066": True,
        },
        "prediction_counts": {
            "reference_final_label": dict(collections.Counter(r["final_label"] for r in scored)),
            "stage1": dict(collections.Counter(r["pred_stage1_label"] for r in scored)),
            "sign_suppressed_stage2_on_true_related": dict(collections.Counter(r["pred_stage2_label"] or "no_stage2_prediction" for r in related_rows)),
            "local_sign_queue_source_on_stage1_related": dict(collections.Counter(r["local_stage2_label_suppressed"] or "no_local_sign" for r in scored if r["pred_stage1_label"] == "related")),
        },
    }
    return report, seed_plan


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    lines = [
        "# Page 58 Sign-Suppressed Gate C2 Score",
        "",
        "Draft for Kun only. No live write, no seed apply, no pass/fail certification by implementer.",
        "",
        "## Configuration",
        "",
        f"- Stage 1: cosine relatedness gate, tau_rel={report['configuration_under_test']['stage1_relatedness_gate']['tau_rel']}.",
        "- Stage 2 auto pass: every Stage-1-related row renders as `related_different_facet` with explicit evidence stance `none`.",
        "- Local supports and contradicts are queued for human review and do not create trust-bearing writes.",
        "- Future human-confirmed contradictions must write stance `challenges`, not `contradicts`.",
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
        "## Seed Plan",
        "",
        f"- Counts: `{json.dumps(report['seed_plan_counts'], sort_keys=True)}`",
        f"- C1 guard: `{json.dumps(report['c1_neutrality_guard'], sort_keys=True)}`",
        "",
        "## Containment",
        "",
        f"- HEAD {report['containment']['nm_head']}; db_write_count={report['containment']['db_write_count']}; paid_lane_touched={str(report['containment']['paid_lane_touched']).lower()}; /api/health={report['containment']['api_health']['status_code']}.",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    report, seed_plan = score()
    stamp = utc_stamp()
    report_path = REBALANCE_DIR / f"sign_suppressed_gate_c2_score_{stamp}.json"
    md_path = REBALANCE_DIR / f"sign_suppressed_gate_c2_score_{stamp}.md"
    seed_path = REBALANCE_DIR / f"sign_suppressed_seed_plan_{stamp}.jsonl"
    write_json(report_path, report)
    write_markdown(md_path, report)
    write_jsonl(seed_path, seed_plan)
    sha256s = {
        report_path.name: sha256_file(report_path),
        md_path.name: sha256_file(md_path),
        seed_path.name: sha256_file(seed_path),
    }
    print(json.dumps({"report": str(report_path), "markdown": str(md_path), "seed_plan": str(seed_path), "sha256s": sha256s}, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
