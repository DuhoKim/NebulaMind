#!/usr/bin/env python3
"""Build the Slice-2B rebalanced stance-gold draft for Papa review.

This is gold-prep only: it reads frozen dry-run artifacts, labels a
stance-stratified sample with the same local panel used by Slice-2, and writes
review artifacts under docs/. It never writes to production tables.
"""
from __future__ import annotations

import argparse
import collections
import datetime as dt
import hashlib
import importlib.util
import json
import os
import random
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

from sqlalchemy import create_engine, text


REPO_ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = REPO_ROOT / "docs"
SLICE1_ARTIFACT = DOCS_ROOT / "page58_sentence_vote_staking_dry_run_20260622T090031Z"
SLICE2_ARTIFACT = DOCS_ROOT / "page58_slice2_calibrated_staking_20260622T111621Z"
SLICE2_SCRIPT = REPO_ROOT / "backend" / "scripts" / "page58_slice2_calibrated_staking_dry_run.py"
DSN = os.getenv("DATABASE_URL", "postgresql://nebula:nebula@localhost:5432/nebulamind")
EXPECTED_HEAD = "4ba9675"
RNG = random.Random(58202)
LABELS_V3 = ["supports", "contradicts", "related_different_facet", "unrelated"]
STAGE2_LABELS = {"supports", "contradicts", "related_different_facet"}
CLAUDE_CAP_V3 = 70


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


def load_slice2_module() -> Any:
    spec = importlib.util.spec_from_file_location("page58_slice2", SLICE2_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SLICE2_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git_head() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"],
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    return result.stdout.strip()


def assert_containment(no_apply: bool, slice2: Any, claude_timeout: int) -> dict[str, Any]:
    if not no_apply:
        raise SystemExit("Refusing to run without --no-apply")
    if os.getenv("NM_ANTHROPIC_API_KEY"):
        raise SystemExit("Refusing to run with NM_ANTHROPIC_API_KEY set")
    head = git_head()
    if head != EXPECTED_HEAD:
        raise SystemExit(f"Refusing to run on git HEAD {head}; expected {EXPECTED_HEAD}")
    if not slice2.check_claude(claude_timeout):
        raise SystemExit("claude -p plan-lane is unreachable; stopping before any metered fallback")
    return {
        "git_head": head,
        "db_write_count": 0,
        "paid_lane_touched": False,
        "local_only": True,
        "no_apply": True,
        "claude_plan_lane_reachable": True,
    }


def round3_task_prompt() -> str:
    return (
        "Page-58 stance gold, Kun round-3 taxonomy. Use a two-stage decision. "
        "Stage 1: related vs unrelated. Stage 2 only if related: supports, contradicts, "
        "or related_different_facet. Final labels are supports|contradicts|"
        "related_different_facet|unrelated. Denial test: contradicts ONLY when the "
        "intro assertion denies the base claim. If it is related but does not deny the "
        "base claim, label related_different_facet unless it directly supports the same "
        "claim. Clean exemplars: (1) Base says internal AGN feedback outflows quench star "
        "formation; intro says positive AGN feedback triggers star formation: contradicts. "
        "(2) Base says gas removal/depletion suppresses star formation by reducing cold "
        "gas supply; intro says molecular gas can be replenished by cold accretion or wet "
        "mergers: related_different_facet. (3) Same base; intro says morphological "
        "quenching works even if gas is continually accreted: related_different_facet. "
        "Do not use rows about 'resolved' vs 'unresolved' AGN questions as exemplars."
    )


def stage_fields(label: str | None) -> dict[str, str | None]:
    if label == "unrelated":
        return {"stage1_label": "unrelated", "stage2_label": None}
    if label in STAGE2_LABELS:
        return {"stage1_label": "related", "stage2_label": label}
    return {"stage1_label": None, "stage2_label": None}


def is_human_review_row(row: dict[str, Any]) -> bool:
    base = str(row.get("base_sentence") or "").lower()
    intro = str(row.get("intro_sentence") or "").lower()
    return (
        "key questions remain unresolved" in base
        and "resolved by this work" in intro
        and "integrated energy released by agn" in intro
    )


def production_read_checks() -> dict[str, Any]:
    engine = create_engine(DSN)
    with engine.connect() as conn:
        sentence_votes_regclass = conn.execute(text("select to_regclass('public.sentence_votes')")).scalar()
        page58 = conn.execute(text("select id, page_id, version_num, source_note from page_versions where id = 58")).mappings().first()
    return {
        "page58_seen_select_only": dict(page58) if page58 else None,
        "sentence_votes_table_present": bool(sentence_votes_regclass),
        "migration_applied": bool(sentence_votes_regclass),
    }


def as_gold_row(row: dict[str, Any], gold_id: str, bucket: str, source: str) -> dict[str, Any]:
    idx = row.get("sentence_index", row.get("nearest_sentence_index"))
    sentence_hash = row.get("sentence_hash", row.get("nearest_sentence_hash"))
    base_sentence = row.get("base_sentence", row.get("nearest_base_sentence"))
    return {
        "gold_id": gold_id,
        "sample_bucket": bucket,
        "sample_source": source,
        "arxiv_id": row.get("arxiv_id"),
        "intro_sentence": row.get("intro_sentence"),
        "base_sentence": base_sentence,
        "sentence_index": idx,
        "sentence_hash": sentence_hash,
        "page_version_id": row.get("page_version_id", 6189),
        "max_cosine": row.get("max_cosine"),
        "prior_stance_label": row.get("stance_label"),
        "prior_qwen_label": row.get("qwen_label"),
        "prior_gpt_label": row.get("gpt_label"),
        "pair_id": row.get("pair_id"),
    }


def dedupe_extend(out: list[dict[str, Any]], rows: list[dict[str, Any]], prefix: str, bucket: str, source: str, limit: int) -> None:
    seen = {
        (
            item.get("arxiv_id"),
            item.get("intro_sentence"),
            item.get("sentence_index"),
            item.get("base_sentence"),
        )
        for item in out
    }
    added = 0
    for row in rows:
        key = (
            row.get("arxiv_id"),
            row.get("intro_sentence"),
            row.get("sentence_index", row.get("nearest_sentence_index")),
            row.get("base_sentence", row.get("nearest_base_sentence")),
        )
        if key in seen:
            continue
        out.append(as_gold_row(row, f"{prefix}-{len(out):03d}", bucket, source))
        seen.add(key)
        added += 1
        if added >= limit:
            return


def build_rebalanced_sample(limit: int | None = None) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    stance_rows = read_jsonl(SLICE2_ARTIFACT / "pairwise_stance_predictions.jsonl")
    emergent = read_jsonl(SLICE1_ARTIFACT / "emergent_pool.jsonl")

    contradiction_like = [
        row for row in stance_rows
        if "contradicts" in {row.get("stance_label"), row.get("qwen_label"), row.get("gpt_label")}
    ]
    contradiction_like.sort(
        key=lambda row: (
            row.get("qwen_label") == row.get("gpt_label") == "contradicts",
            row.get("stance_label") == "contradicts",
            float(row.get("max_cosine") or 0.0),
        ),
        reverse=True,
    )

    support_pool = [row for row in stance_rows if row.get("stance_label") == "supports" and row not in contradiction_like]
    neither_pool = [row for row in stance_rows if row.get("stance_label") == "neither" and row not in contradiction_like]
    support_pool.sort(key=lambda row: float(row.get("max_cosine") or 0.0), reverse=True)
    neither_pool.sort(key=lambda row: float(row.get("max_cosine") or 0.0), reverse=True)

    # Sub-threshold rows expose the neither/relevance boundary missing from the
    # original cosine-survivor-only stance draft.
    sub_tau = [row for row in emergent if float(row.get("max_cosine") or 0.0) < 0.53]
    sub_tau.sort(key=lambda row: float(row.get("max_cosine") or 0.0), reverse=True)
    negative_pattern = re.compile(
        r"\b(no|not|lack|lacks|lacking|without|cannot|insufficient|inefficient|unlikely|"
        r"less likely|rather than|instead|opposite|however|although|despite|but)\b",
        re.I,
    )
    negative_probe_pool = [
        row for row in stance_rows + emergent
        if negative_pattern.search(str(row.get("intro_sentence") or ""))
    ]
    negative_probe_pool.sort(
        key=lambda row: (
            "contradicts" in {row.get("stance_label"), row.get("qwen_label"), row.get("gpt_label")},
            float(row.get("max_cosine") or 0.0),
        ),
        reverse=True,
    )

    RNG.shuffle(support_pool)
    RNG.shuffle(neither_pool)
    rows: list[dict[str, Any]] = []
    dedupe_extend(rows, contradiction_like, "stance2b", "contradict_oversample", "pairwise_stance_predictions", 27)
    dedupe_extend(rows, negative_probe_pool, "stance2b", "negative_contradiction_probe", "wider_finding_pool", 30)
    dedupe_extend(rows, sub_tau[:160], "stance2b", "sub_tau_neither_boundary", "slice1_emergent_pool", 24)
    dedupe_extend(rows, neither_pool, "stance2b", "neither_oversample", "pairwise_stance_predictions", 24)
    dedupe_extend(rows, support_pool, "stance2b", "support_control", "pairwise_stance_predictions", 24)

    if limit is not None:
        exemplar_keys = {
            (
                "2604.15438",
                "Gas can be compressed along and at the peak of these massive outflows, leading to star formation activity known as positive AGN feedback ( Cresci2015TheMUSE ; Maiolino2017StarOutflow ; Gallagher2019WidespreadOutflows ; Shin2019Positive5728 ) .",
            ),
            (
                "1706.08987v2",
                "The molecular gas reservoir can be replenished through either accretion of cold gas from the halo or wet mergers.",
            ),
            (
                "1308.5224v1",
                "Such “morphological quenching” can persist over several Gyr, and it is effective even if gas is continually accreted from external sources.",
            ),
        }
        exemplars = [row for row in rows if (row.get("arxiv_id"), row.get("intro_sentence")) in exemplar_keys]
        support_probe = next((row for row in rows if row.get("sample_bucket") == "support_control"), None)
        unrelated_probe = as_gold_row(sub_tau[-1], "stance2b-smoke-unrelated", "sub_tau_unrelated_probe", "slice1_emergent_pool") if sub_tau else None
        chosen = exemplars[:]
        for candidate in (support_probe, unrelated_probe):
            if candidate is not None and candidate not in chosen:
                chosen.append(candidate)
        extras = [row for row in rows if row not in chosen]
        rows = (chosen + extras)[:limit]
    for i, row in enumerate(rows):
        row["gold_id"] = f"stance2b-{i:03d}"
        if is_human_review_row(row):
            row["sample_bucket"] = "human_review_resolved_unresolved"
            row["human_review_required"] = True

    meta = {
        "input_rows": len(rows),
        "source_rows_pairwise": len(stance_rows),
        "source_rows_emergent": len(emergent),
        "contradiction_like_pool": len(contradiction_like),
        "negative_probe_pool": len(negative_probe_pool),
        "sub_tau_boundary_pool": len(sub_tau),
        "sample_buckets": dict(collections.Counter(row["sample_bucket"] for row in rows)),
        "source_prior_labels": dict(collections.Counter(row.get("prior_stance_label") or row["sample_bucket"] for row in rows)),
    }
    return rows, meta


def normalize_v3_label(value: Any) -> str | None:
    label = str(value or "").strip().lower()
    aliases = {
        "neither": "related_different_facet",
        "related": "related_different_facet",
        "different_facet": "related_different_facet",
        "not_related": "unrelated",
        "not_bears_on": "unrelated",
    }
    label = aliases.get(label, label)
    return label if label in LABELS_V3 else None


def normalize_v3_panel_row(row: dict[str, Any]) -> dict[str, Any]:
    for prefix in ("qwen", "gpt"):
        label = normalize_v3_label(row.get(f"{prefix}_label")) or "related_different_facet"
        row[f"{prefix}_label"] = label
        row[f"{prefix}_stage1_label"] = stage_fields(label)["stage1_label"]
        row[f"{prefix}_stage2_label"] = stage_fields(label)["stage2_label"]
    return row


def claude_label_v3(row: dict[str, Any], timeout: int) -> dict[str, Any]:
    env = {k: v for k, v in os.environ.items() if "ANTHROPIC" not in k.upper() and k != "NM_ANTHROPIC_API_KEY"}
    prompt = (
        "Return strict JSON only with keys final_label, stage1_label, stage2_label, confidence, reason. "
        f"{round3_task_prompt()} "
        "If still ambiguous after applying the denial test, prefer final_label=related_different_facet. "
        f"Row={json.dumps(row, ensure_ascii=False)}"
    )
    result = subprocess.run(["claude", "-p", prompt], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout, env=env)
    if result.returncode != 0:
        raise RuntimeError(result.stderr[:500])
    return extract_json_local(result.stdout)


def extract_json_local(raw: str) -> dict[str, Any]:
    raw = raw.strip()
    try:
        return json.loads(raw)
    except Exception:
        pass
    match = re.search(r"\{.*\}", raw, re.S)
    if match:
        return json.loads(match.group(0))
    raise ValueError("no parseable JSON")


def finalize_stance_gold_v3(rows: list[dict[str, Any]], timeout: int, cap: int) -> tuple[list[dict[str, Any]], dict[str, int]]:
    disagreements = sum(1 for row in rows if row["qwen_label"] != row["gpt_label"] and not row.get("human_review_required"))
    if disagreements > cap:
        raise SystemExit(f"Refusing to run: {disagreements} disagreements exceed claude cap {cap}")
    claude_used = 0
    ambiguous_to_facet = 0
    human_review = 0
    final: list[dict[str, Any]] = []
    for in_row in rows:
        row = normalize_v3_panel_row(dict(in_row))
        if row.get("human_review_required"):
            fields = stage_fields(None)
            final.append({
                **row,
                "draft_label": None,
                "draft_stage1_label": fields["stage1_label"],
                "draft_stage2_label": fields["stage2_label"],
                "label_source": "human_review_required",
                "claude_tiebreak": None,
            })
            human_review += 1
            continue
        label = row["qwen_label"]
        source = "qwen_gpt_agree" if row["qwen_label"] == row["gpt_label"] else "claude_tiebreak"
        claude_obj = None
        if row["qwen_label"] != row["gpt_label"]:
            claude_obj = claude_label_v3(row, timeout)
            candidate = normalize_v3_label(claude_obj.get("final_label") or claude_obj.get("label"))
            if candidate is None:
                candidate = "related_different_facet"
                ambiguous_to_facet += 1
            label = candidate
            claude_used += 1
        fields = stage_fields(label)
        final.append({
            **row,
            "draft_label": label,
            "draft_stage1_label": fields["stage1_label"],
            "draft_stage2_label": fields["stage2_label"],
            "label_source": source,
            "claude_tiebreak": claude_obj,
        })
    return final, {
        "panel_disagreements": disagreements,
        "claude_tiebroken": claude_used,
        "still_ambiguous_to_related_different_facet": ambiguous_to_facet,
        "human_review_required": human_review,
    }


def add_review_flags(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out = []
    for row in rows:
        panel_disagreement = row.get("qwen_label") != row.get("gpt_label")
        qwen_default = row.get("label_source") == "qwen_default"
        cap_exhausted = panel_disagreement and qwen_default
        papa_attention = bool(panel_disagreement or qwen_default or row.get("human_review_required") or row.get("draft_label") in {"contradicts", "related_different_facet", None})
        flags = []
        if panel_disagreement:
            flags.append("qwen_gpt_disagreement")
        if qwen_default:
            flags.append("qwen_default")
        if cap_exhausted:
            flags.append("claude_cap_exhausted_disagreement")
        if row.get("sample_bucket") == "sub_tau_neither_boundary":
            flags.append("sub_tau_relevance_boundary")
        if row.get("human_review_required"):
            flags.append("human_review_required")
        if row.get("draft_label") in {"contradicts", "related_different_facet", None}:
            flags.append("rare_or_boundary_class")
        out.append({
            **row,
            "panel_disagreement": panel_disagreement,
            "qwen_default": qwen_default,
            "claude_cap_exhausted_disagreement": cap_exhausted,
            "papa_attention": papa_attention,
            "papa_attention_flags": flags,
        })
    return out


def write_markdown(path: Path, summary: dict[str, Any]) -> None:
    lines = [
        "# Page 58 Slice-2B Stance Gold Rebalance",
        "",
        "Gold-prep only. No staking rollup was rerun.",
        "",
        "## Counts",
        "",
        f"- Rows: {summary['rows']}",
        f"- Draft labels: {summary['draft_label_ratios']}",
        f"- Stage 1: {summary['stage1_ratios']}",
        f"- Stage 2: {summary['stage2_ratios']}",
        f"- Sample buckets: {summary['sample_buckets']}",
        f"- Papa attention rows: {summary['flag_counts']['papa_attention']}",
        f"- qwen_default rows: {summary['flag_counts']['qwen_default']}",
        f"- qwen/gpt disagreement rows: {summary['flag_counts']['panel_disagreement']}",
        f"- cap-exhausted disagreement rows: {summary['flag_counts']['claude_cap_exhausted_disagreement']}",
        f"- Disagreements: {summary['disagreement_accounting']}",
        "",
        "## Containment",
        "",
        (
            f"- HEAD {summary['containment']['git_head']}; --no-apply; "
            f"db_write_count={summary['containment']['db_write_count']}; "
            f"paid_lane_touched={str(summary['containment']['paid_lane_touched']).lower()}; "
            f"local_only={str(summary['containment']['local_only']).lower()}; "
            f"claude_p_cap={summary['claude_p_cap']}; claude_p_invocations={summary['claude_p_invocations']}; "
            f"sentence_votes_table_present={str(summary['db_select_checks']['sentence_votes_table_present']).lower()}."
        ),
        "",
        "## Files",
        "",
    ]
    for name, digest in summary["sha256s"].items():
        lines.append(f"- `{name}` sha256 `{digest}`")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-apply", action="store_true", required=True)
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument("--timeout", type=int, default=240)
    parser.add_argument("--claude-timeout", type=int, default=120)
    parser.add_argument("--claude-cap", type=int, default=CLAUDE_CAP_V3)
    parser.add_argument("--stamp", default=None)
    args = parser.parse_args()

    slice2 = load_slice2_module()
    slice2.CLAUDE_CAP = args.claude_cap
    containment = assert_containment(args.no_apply, slice2, args.claude_timeout)
    limit = 5 if args.smoke else None
    sample, sample_meta = build_rebalanced_sample(limit=limit)
    labeled = slice2.batch_panel(
        round3_task_prompt(),
        sample,
        LABELS_V3,
        args.timeout,
    )
    final, disagreement_accounting = finalize_stance_gold_v3(labeled, args.claude_timeout, args.claude_cap)
    final = add_review_flags(final)

    stamp = args.stamp or utc_stamp()
    suffix = "_smoke" if args.smoke else ""
    out_dir = DOCS_ROOT / f"page58_slice2b_stance_gold_rebalance_{stamp}{suffix}"
    out_dir.mkdir(parents=True, exist_ok=True)
    jsonl_path = out_dir / "stance_gold_draft_for_papa_v3.jsonl"
    summary_path = out_dir / "summary.json"
    report_path = out_dir / "STANCE_GOLD_REBALANCE_NOTE.md"

    write_jsonl(jsonl_path, final)
    flag_counts = {
        "papa_attention": sum(1 for row in final if row["papa_attention"]),
        "qwen_default": sum(1 for row in final if row["qwen_default"]),
        "panel_disagreement": sum(1 for row in final if row["panel_disagreement"]),
        "claude_cap_exhausted_disagreement": sum(1 for row in final if row["claude_cap_exhausted_disagreement"]),
        "sub_tau_relevance_boundary": sum(1 for row in final if "sub_tau_relevance_boundary" in row["papa_attention_flags"]),
    }
    db_select_checks = production_read_checks()
    label_counts = dict(collections.Counter(str(row["draft_label"]) for row in final))
    stage1_counts = dict(collections.Counter(str(row["draft_stage1_label"]) for row in final))
    stage2_counts = dict(collections.Counter(str(row["draft_stage2_label"]) for row in final))
    def ratios(counts: dict[str, int]) -> dict[str, str]:
        total = len(final)
        return {key: f"{value}/{total} ({(value / total * 100 if total else 0):.1f}%)" for key, value in sorted(counts.items())}
    summary = {
        "artifact": str(out_dir),
        "phase": "slice2b_gold_rebalance_smoke" if args.smoke else "slice2b_gold_rebalance_complete",
        "rows": len(final),
        "draft_label_counts": label_counts,
        "draft_label_ratios": ratios(label_counts),
        "stage1_counts": stage1_counts,
        "stage1_ratios": ratios(stage1_counts),
        "stage2_counts": stage2_counts,
        "stage2_ratios": ratios(stage2_counts),
        "qwen_label_counts": dict(collections.Counter(row["qwen_label"] for row in final)),
        "gpt_label_counts": dict(collections.Counter(row["gpt_label"] for row in final)),
        "label_source_counts": dict(collections.Counter(row["label_source"] for row in final)),
        "sample_buckets": dict(collections.Counter(row["sample_bucket"] for row in final)),
        "flag_counts": flag_counts,
        "disagreement_accounting": disagreement_accounting,
        "claude_p_invocations": disagreement_accounting["claude_tiebroken"],
        "claude_p_cap": args.claude_cap,
        "no_full_staking_rollup_rerun": True,
        "stance_lock": "not_locked_pending_papa_spot_check",
        "accuracy_metric": "not_computed_papa_labels_required",
        "source_artifacts": {
            "slice1": str(SLICE1_ARTIFACT),
            "slice2": str(SLICE2_ARTIFACT),
        },
        "sample_meta": sample_meta,
        "containment": containment,
        "db_select_checks": db_select_checks,
        "sha256s": {},
    }
    write_json(summary_path, summary)
    summary["sha256s"] = {
        jsonl_path.name: sha256_file(jsonl_path),
        summary_path.name: sha256_file(summary_path),
    }
    write_json(summary_path, summary)
    summary["sha256s"][summary_path.name] = sha256_file(summary_path)
    write_markdown(report_path, summary)
    summary["sha256s"][report_path.name] = sha256_file(report_path)
    write_json(summary_path, summary)
    summary["sha256s"][summary_path.name] = sha256_file(summary_path)
    write_json(summary_path, summary)

    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
