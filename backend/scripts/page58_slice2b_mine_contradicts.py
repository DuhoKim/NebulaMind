#!/usr/bin/env python3
"""Mine Page-58 Slice-2B for genuine denial-style contradicts.

Dry-run only. Reads frozen Slice-1/Slice-2 artifacts, casts a wide
cue-based candidate net, runs the same two-stage local panel as v3, and writes
Papa-review candidates. It never writes to production tables.
"""
from __future__ import annotations

import argparse
import collections
import datetime as dt
import hashlib
import importlib.util
import json
import os
import re
import subprocess
from pathlib import Path
from typing import Any

from sqlalchemy import create_engine, text


REPO_ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = REPO_ROOT / "docs"
SLICE1_ARTIFACT = DOCS_ROOT / "page58_sentence_vote_staking_dry_run_20260622T090031Z"
SLICE2_ARTIFACT = DOCS_ROOT / "page58_slice2_calibrated_staking_20260622T111621Z"
V3_ARTIFACT = DOCS_ROOT / "page58_slice2b_stance_gold_rebalance_20260623T043618Z"
SLICE2_SCRIPT = REPO_ROOT / "backend" / "scripts" / "page58_slice2_calibrated_staking_dry_run.py"
EXPECTED_HEAD = "4ba9675"
DSN = os.getenv("DATABASE_URL", "postgresql://nebula:nebula@localhost:5432/nebulamind")
LABELS = ["supports", "contradicts", "related_different_facet", "unrelated"]
CLAUDE_CAP = 80
MAX_PANEL_ROWS = 180


NEGATION_RE = re.compile(
    r"\b(no evidence for|no significant|not\b|unlike\b|in contrast to|contrary to|"
    r"fails? to|does not|do not|did not|cannot|can't|without|lack(?:s|ing)?|"
    r"less likely|rather than|instead of|independent of|decoupled from|not.*sufficient|"
    r"not.*primary|not.*dominant|weak(?:er)? .*dependence|only weak)\b",
    re.I,
)
MECHANISM_OFF_RE = re.compile(
    r"\b(replenish|continually accret|continual accret|inefficient|insufficient|"
    r"less likely to be sufficient|not sufficient|does not quench|continued star formation|"
    r"remain star forming|mass[- ]driven|like centrals|central velocity dispersion|"
    r"black hole mass .* predictor|environment .* weak|weak secondary dependence)\b",
    re.I,
)
KNOWN_FACET_RE = re.compile(
    r"positive AGN feedback|resolved by this work|molecular gas reservoir can be replenished|morphological quenching",
    re.I,
)


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


def load_slice2_module() -> Any:
    spec = importlib.util.spec_from_file_location("page58_slice2", SLICE2_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SLICE2_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git_head() -> str:
    return subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"],
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    ).stdout.strip()


def check_claude(timeout: int) -> bool:
    env = {k: v for k, v in os.environ.items() if "ANTHROPIC" not in k.upper() and k != "NM_ANTHROPIC_API_KEY"}
    try:
        result = subprocess.run(
            ["claude", "-p", "Return exactly: CLAUDE_PLAN_LANE_OK"],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            env=env,
        )
    except Exception:
        return False
    return result.returncode == 0 and "CLAUDE_PLAN_LANE_OK" in result.stdout


def assert_containment(no_apply: bool, claude_timeout: int) -> dict[str, Any]:
    if not no_apply:
        raise SystemExit("Refusing to run without --no-apply")
    if os.getenv("NM_ANTHROPIC_API_KEY"):
        raise SystemExit("Refusing to run with NM_ANTHROPIC_API_KEY set")
    head = git_head()
    if head != EXPECTED_HEAD:
        raise SystemExit(f"Refusing to run on git HEAD {head}; expected {EXPECTED_HEAD}")
    if not check_claude(claude_timeout):
        raise SystemExit("claude -p plan-lane is unreachable; stopping before metered fallback")
    return {
        "git_head": head,
        "db_write_count": 0,
        "paid_lane_touched": False,
        "no_apply": True,
        "claude_plan_lane_reachable": True,
    }


def production_read_checks() -> dict[str, Any]:
    engine = create_engine(DSN)
    with engine.connect() as conn:
        sentence_votes_regclass = conn.execute(text("select to_regclass('public.sentence_votes')")).scalar()
    return {"sentence_votes_table_present": bool(sentence_votes_regclass)}


def task_prompt() -> str:
    return (
        "Page-58 contradicts mining under Papa's boundary. Use two stages. "
        "Stage 1: related vs unrelated. Stage 2 if related: supports, contradicts, "
        "or related_different_facet. Final labels: supports|contradicts|"
        "related_different_facet|unrelated. Contradicts means the candidate sentence "
        "DENIES the page-58 claim's explicit assertion, even if only within a sub-regime. "
        "Related_different_facet means related/complementary/different mechanism or spatial "
        "regime with no denial. Worked boundary: positive vs negative AGN feedback in "
        "different spatial regimes is NOT contradicts; high-mass satellites behaving like "
        "centrals denies a base claim that satellite quenching is distinct from mass-driven "
        "central quenching, so it IS contradicts. Do not label contradiction from mere topic "
        "overlap, opposite direction, or coexistence."
    )


def as_candidate(row: dict[str, Any], source: str, idx: int) -> dict[str, Any]:
    return {
        "gold_id": f"mine-{idx:03d}",
        "sample_source": source,
        "arxiv_id": row.get("arxiv_id"),
        "intro_sentence": row.get("intro_sentence"),
        "base_sentence": row.get("base_sentence", row.get("nearest_base_sentence")),
        "sentence_index": row.get("sentence_index", row.get("nearest_sentence_index")),
        "sentence_hash": row.get("sentence_hash", row.get("nearest_sentence_hash")),
        "page_version_id": row.get("page_version_id", 6189),
        "max_cosine": row.get("max_cosine"),
        "prior_stance_label": row.get("stance_label"),
        "prior_qwen_label": row.get("qwen_label"),
        "prior_gpt_label": row.get("gpt_label"),
        "pair_id": row.get("pair_id"),
    }


def denial_score(row: dict[str, Any]) -> int:
    intro = str(row.get("intro_sentence") or "")
    base = str(row.get("base_sentence", row.get("nearest_base_sentence")) or "")
    score = 0
    if NEGATION_RE.search(intro):
        score += 4
    if MECHANISM_OFF_RE.search(intro):
        score += 4
    if "satellite" in base.lower() and re.search(r"like centrals|mass[- ]driven|central velocity dispersion|weak secondary dependence|environment", intro, re.I):
        score += 5
    if "stellar mass as the primary driver" in base.lower() and re.search(r"black hole mass|environment.*primary|not.*stellar mass|more important than stellar", intro, re.I):
        score += 5
    if "gas removal" in base.lower() and re.search(r"not.*remov|less likely.*remove|insufficient.*remove|cannot.*remove|continued accretion", intro, re.I):
        score += 5
    if "agn feedback" in base.lower() and re.search(r"inefficient|below 0\\.1%|insufficient|not.*quench|positive AGN feedback", intro, re.I):
        score += 3
    try:
        score += int(float(row.get("max_cosine") or 0.0) * 10)
    except (TypeError, ValueError):
        pass
    if KNOWN_FACET_RE.search(intro):
        score -= 6
    return score


def mine_candidates(limit: int) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    pairwise = read_jsonl(SLICE2_ARTIFACT / "pairwise_stance_predictions.jsonl")
    emergent = read_jsonl(SLICE1_ARTIFACT / "emergent_pool.jsonl")
    prior_v3 = read_jsonl(V3_ARTIFACT / "stance_gold_draft_for_papa_v3.jsonl")
    seen: set[tuple[Any, Any, Any]] = set()
    scored: list[tuple[int, dict[str, Any], str]] = []
    for source, rows in (("slice2_pairwise", pairwise), ("slice1_emergent", emergent), ("v3_prior_draft", prior_v3)):
        for row in rows:
            intro = row.get("intro_sentence")
            base = row.get("base_sentence", row.get("nearest_base_sentence"))
            key = (row.get("arxiv_id"), intro, base)
            if not intro or not base or key in seen:
                continue
            seen.add(key)
            score = denial_score(row)
            if score >= 7:
                scored.append((score, row, source))
    scored.sort(key=lambda item: (item[0], float(item[1].get("max_cosine") or 0.0)), reverse=True)
    candidates = [as_candidate(row, source, idx) | {"candidate_filter_score": score} for idx, (score, row, source) in enumerate(scored[:limit])]
    return candidates, {
        "pairwise_rows": len(pairwise),
        "emergent_rows": len(emergent),
        "v3_prior_rows": len(prior_v3),
        "wide_filter_hits": len(scored),
        "panel_rows": len(candidates),
        "filter": "negation/contrast + mechanism-off + regime-flip cues; known facet exemplars downweighted",
    }


def normalize_label(value: Any) -> str | None:
    label = str(value or "").strip().lower()
    aliases = {"neither": "related_different_facet", "related": "related_different_facet"}
    label = aliases.get(label, label)
    return label if label in LABELS else None


def stage_fields(label: str | None) -> dict[str, str | None]:
    if label == "unrelated":
        return {"stage1_label": "unrelated", "stage2_label": None}
    if label in {"supports", "contradicts", "related_different_facet"}:
        return {"stage1_label": "related", "stage2_label": label}
    return {"stage1_label": None, "stage2_label": None}


def claude_tiebreak(row: dict[str, Any], timeout: int) -> dict[str, Any]:
    env = {k: v for k, v in os.environ.items() if "ANTHROPIC" not in k.upper() and k != "NM_ANTHROPIC_API_KEY"}
    prompt = (
        "Return strict JSON only with keys final_label, denied_assertion, confidence, reason. "
        f"{task_prompt()} If uncertain, prefer related_different_facet over contradicts. "
        f"Row={json.dumps(row, ensure_ascii=False)}"
    )
    result = subprocess.run(["claude", "-p", prompt], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout, env=env)
    if result.returncode != 0:
        raise RuntimeError(result.stderr[:500])
    return extract_json(result.stdout)


def finalize(rows: list[dict[str, Any]], timeout: int, cap: int) -> tuple[list[dict[str, Any]], dict[str, int]]:
    disagreements = sum(1 for row in rows if row["qwen_label"] != row["gpt_label"])
    if disagreements > cap:
        raise SystemExit(f"Refusing to run: {disagreements} disagreements exceed claude cap {cap}")
    claude_used = 0
    final = []
    for row in rows:
        q = normalize_label(row.get("qwen_label")) or "related_different_facet"
        g = normalize_label(row.get("gpt_label")) or "related_different_facet"
        label = q
        source = "qwen_gpt_agree" if q == g else "claude_tiebreak"
        claude_obj = None
        if q != g:
            claude_obj = claude_tiebreak({**row, "qwen_label": q, "gpt_label": g}, timeout)
            label = normalize_label(claude_obj.get("final_label") or claude_obj.get("label")) or "related_different_facet"
            claude_used += 1
        fields = stage_fields(label)
        final.append({
            **row,
            "qwen_label": q,
            "gpt_label": g,
            "qwen_stage1_label": stage_fields(q)["stage1_label"],
            "qwen_stage2_label": stage_fields(q)["stage2_label"],
            "gpt_stage1_label": stage_fields(g)["stage1_label"],
            "gpt_stage2_label": stage_fields(g)["stage2_label"],
            "draft_label": label,
            "draft_stage1_label": fields["stage1_label"],
            "draft_stage2_label": fields["stage2_label"],
            "label_source": source,
            "claude_tiebreak": claude_obj,
            "denies_page58_assertion": row.get("base_sentence") if label == "contradicts" else None,
            "denial_rationale": (claude_obj or {}).get("reason") or row.get("qwen_reason") or row.get("gpt_reason"),
            "papa_review": label == "contradicts",
        })
    return final, {"panel_disagreements": disagreements, "claude_tiebroken": claude_used, "qwen_default": 0}


def ratios(counts: dict[str, int], total: int) -> dict[str, str]:
    return {key: f"{value}/{total} ({(value / total * 100 if total else 0):.1f}%)" for key, value in sorted(counts.items())}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-apply", action="store_true", required=True)
    parser.add_argument("--limit", type=int, default=MAX_PANEL_ROWS)
    parser.add_argument("--timeout", type=int, default=240)
    parser.add_argument("--claude-timeout", type=int, default=240)
    parser.add_argument("--claude-cap", type=int, default=CLAUDE_CAP)
    parser.add_argument("--stamp", default=None)
    args = parser.parse_args()

    containment = assert_containment(args.no_apply, args.claude_timeout)
    slice2 = load_slice2_module()
    candidates, candidate_meta = mine_candidates(args.limit)
    labeled = slice2.batch_panel(task_prompt(), candidates, LABELS, args.timeout)
    final, disagreement_accounting = finalize(labeled, args.claude_timeout, args.claude_cap)
    contradicts = [row for row in final if row["draft_label"] == "contradicts"]

    stamp = args.stamp or utc_stamp()
    out_dir = V3_ARTIFACT / f"contradicts_mine_{stamp}"
    out_dir.mkdir(parents=True, exist_ok=True)
    jsonl_path = out_dir / "stance_gold_contradicts_mine_v1.jsonl"
    all_panel_path = out_dir / "stance_gold_contradicts_mine_panel_all_v1.jsonl"
    summary_path = out_dir / "summary.json"

    write_jsonl(jsonl_path, contradicts)
    write_jsonl(all_panel_path, final)
    label_counts = dict(collections.Counter(row["draft_label"] for row in final))
    summary = {
        "artifact": str(out_dir),
        "phase": "slice2b_contradicts_mine_v1",
        "rows": len(contradicts),
        "panel_rows": len(final),
        "draft_label_counts": label_counts,
        "draft_label_ratios": ratios(label_counts, len(final)),
        "mined_contradicts_ratio": f"{len(contradicts)}/{len(final)} ({(len(contradicts) / len(final) * 100 if final else 0):.1f}%)",
        "disagreement_accounting": disagreement_accounting,
        "claude_p_cap": args.claude_cap,
        "claude_p_invocations": disagreement_accounting["claude_tiebroken"],
        "qwen_default": 0,
        "containment": containment,
        "db_select_checks": production_read_checks(),
        "candidate_meta": candidate_meta,
        "scope": {
            "stance_lock": "not_locked_pending_papa_review",
            "accuracy_metric": "not_computed_papa_labels_required",
            "db_apply": False,
            "alembic_reconcile": False,
            "page57_swap": False,
            "tone_as_weight": False,
        },
        "sha256s": {},
    }
    write_json(summary_path, summary)
    summary["sha256s"] = {
        jsonl_path.name: sha256_file(jsonl_path),
        all_panel_path.name: sha256_file(all_panel_path),
        summary_path.name: sha256_file(summary_path),
    }
    write_json(summary_path, summary)
    summary["sha256s"][summary_path.name] = sha256_file(summary_path)
    write_json(summary_path, summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
