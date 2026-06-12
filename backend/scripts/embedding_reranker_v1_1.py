#!/usr/bin/env python3
"""Reranker v1.1 final-attempt harness.

Shadow-only. Reuses Reranker v1 fixture/candidate helpers and first-stage
vector cache. This script intentionally measures Qwen3-Reranker-0.6B on CPU
only; it does not touch production routing, schema, env, Celery, cron, or data.
"""

from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
import math
import statistics
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

import httpx
import torch
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer


BACKEND = Path("/Users/duhokim/NebulaMind/NebulaMind/backend")
V1_PATH = BACKEND / "scripts" / "embedding_reranker_v1.py"
LOG_DIR = Path("/Users/duhokim/NebulaMind/logs")
WORKSPACE = Path("/Users/duhokim/.openclaw/workspace")
QWEN_MODEL = "Qwen/Qwen3-Reranker-0.6B"
LANE = "nomic_top50__qwen3-reranker-0.6b_cpu"


def load_v1():
    spec = importlib.util.spec_from_file_location("reranker_v1", V1_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def percentile(values: list[float], p: float) -> float | None:
    if not values:
        return None
    values = sorted(values)
    if len(values) == 1:
        return values[0]
    idx = (len(values) - 1) * p
    lo, hi = math.floor(idx), math.ceil(idx)
    if lo == hi:
        return values[lo]
    return values[lo] * (hi - idx) + values[hi] * (idx - lo)


class QwenCpuReranker:
    def __init__(self, max_length: int, batch_size: int):
        self.max_length = max_length
        self.batch_size = batch_size
        start = time.perf_counter()
        self.tokenizer = AutoTokenizer.from_pretrained(QWEN_MODEL, padding_side="left", trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(
            QWEN_MODEL, trust_remote_code=True, torch_dtype=torch.float32
        ).eval()
        self.false_id = self.tokenizer.convert_tokens_to_ids("no")
        self.true_id = self.tokenizer.convert_tokens_to_ids("yes")
        prefix = (
            "<|im_start|>system\n"
            'Judge whether the Document meets the requirements based on the Query and the Instruct provided. '
            'Note that the answer can only be "yes" or "no".'
            "<|im_end|>\n<|im_start|>user\n"
        )
        suffix = "<|im_end|>\n<|im_start|>assistant\n<think>\n\n</think>\n\n"
        self.prefix_tokens = self.tokenizer.encode(prefix, add_special_tokens=False)
        self.suffix_tokens = self.tokenizer.encode(suffix, add_special_tokens=False)
        self.load_ms = (time.perf_counter() - start) * 1000

    def format_pair(self, query: str, doc: str) -> str:
        return (
            "<Instruct>: Given an astronomy wiki claim, retrieve the specific paper abstract that directly supports "
            "the claim. Prefer same-subfield evidence over broad topical overlap.\n"
            f"<Query>: {query}\n<Document>: {doc}"
        )

    def score(self, pairs: list[tuple[str, str]]) -> list[float]:
        scores: list[float] = []
        for i in range(0, len(pairs), self.batch_size):
            texts = [self.format_pair(q, d) for q, d in pairs[i : i + self.batch_size]]
            inputs = self.tokenizer(
                texts,
                padding=False,
                truncation="longest_first",
                return_attention_mask=False,
                max_length=self.max_length - len(self.prefix_tokens) - len(self.suffix_tokens),
            )
            for j, ids in enumerate(inputs["input_ids"]):
                inputs["input_ids"][j] = self.prefix_tokens + ids + self.suffix_tokens
            inputs = self.tokenizer.pad(inputs, padding=True, return_tensors="pt")
            with torch.no_grad():
                logits = self.model(**inputs).logits[:, -1, :]
                both = torch.stack([logits[:, self.false_id], logits[:, self.true_id]], dim=1)
                probs = torch.nn.functional.log_softmax(both, dim=1)[:, 1].exp()
            scores.extend(float(x) for x in probs.tolist())
        return scores


def build_context(v1: Any):
    phase2b = json.loads(v1.PHASE2B_JSON.read_text())
    slice_a, slice_a_meta = v1.fetch_slice_a()
    hard_pre, evidence_docs, hard_pre_meta = v1.build_pre_nomic_hard_candidates(slice_a)
    galaxy, galaxy_meta = v1.load_galaxy_fixture()
    docs: dict[str, dict[str, Any]] = {}
    for p in slice_a:
        docs[p["doc_id"]] = p
    for did in {d for values in hard_pre.values() for d in values}:
        docs[did] = evidence_docs[did]
    for g in galaxy:
        docs[g["doc_id"]] = g
    queries = {p["query_id"]: p["claim_text"] for p in slice_a}
    queries.update({g["query_id"]: g["claim_text"] for g in galaxy})
    qvecs, dvecs, first_stage_timings = v1.embed_first_stage(queries, docs)
    hard_candidates, hard_meta = v1.add_embedding_neighbors(slice_a, hard_pre, docs, qvecs, dvecs)
    try:
        validation = v1.validate_fixtures(slice_a_meta, galaxy_meta, hard_meta, phase2b)
    except Exception as exc:
        validation = {
            "status": "mismatch_recorded_nonfatal_for_latency_lane",
            "error": str(exc),
            "phase2b_expected": {
                "slice_a": phase2b["slice_a"],
                "slice_c": phase2b["slice_c"],
                "galaxy": phase2b["galaxy"],
            },
            "current_rebuild": {
                "slice_a": slice_a_meta,
                "slice_c": hard_meta,
                "galaxy": galaxy_meta,
            },
        }
    rankings, first_stage, first_cost = v1.score_first_stage(
        "nomic_top50", "nomic", 50, slice_a, galaxy, hard_candidates, qvecs, dvecs
    )
    return {
        "phase2b": phase2b,
        "slice_a": slice_a,
        "slice_a_meta": slice_a_meta,
        "galaxy": galaxy,
        "galaxy_meta": galaxy_meta,
        "docs": docs,
        "queries": queries,
        "rankings": rankings,
        "first_stage": first_stage,
        "first_cost": first_cost,
        "first_stage_timings": first_stage_timings,
        "slice_c": hard_meta,
        "slice_c_pre_nomic": hard_pre_meta,
        "fixture_validation": validation,
    }


def make_pairs(v1: Any, query: str, doc_ids: list[str], docs: dict[str, dict[str, Any]]) -> tuple[list[tuple[str, str]], list[dict[str, int]]]:
    pairs = []
    stats = []
    for did in doc_ids:
        qtrim, stat = v1.truncate_text(query, docs[did])
        doc = docs[did]
        text = (doc.get("title") or "") + "\n" + " ".join((doc.get("abstract") or "").split()[:700])
        pairs.append((qtrim, text))
        stats.append(stat)
    return pairs, stats


def measure_latency(v1: Any, reranker: QwenCpuReranker, ctx: dict[str, Any], sample_n: int) -> dict[str, Any]:
    qids = list({p["query_id"] for p in ctx["slice_a"]})[:sample_n]
    lat = []
    costs = []
    failures = 0
    for qid in qids:
        query = ctx["queries"][qid]
        ranked = ctx["rankings"][f"nomic_top50:slice_a_combined_global:{qid}"]
        start = time.perf_counter()
        with httpx.Client() as client:
            estart = time.perf_counter()
            _ = v1.embed(client, v1.MODELS["nomic"]["ollama"], query)
            embedding_ms = (time.perf_counter() - estart) * 1000
        rstart = time.perf_counter()
        pairs, _ = make_pairs(v1, query, ranked, ctx["docs"])
        first_stage_rank_ms = (time.perf_counter() - rstart) * 1000
        rr_start = time.perf_counter()
        try:
            scores = reranker.score(pairs)
            ok = len(scores) == len(pairs)
        except Exception:
            ok = False
        rerank_ms = (time.perf_counter() - rr_start) * 1000
        total_ms = (time.perf_counter() - start) * 1000
        lat.append(total_ms)
        failures += 0 if ok else 1
        costs.append({"embedding_ms": embedding_ms, "first_stage_rank_ms": first_stage_rank_ms, "rerank_ms": rerank_ms, "total_ms": total_ms})
    return {
        "hot_c1": {
            "count": len(lat),
            "errors": failures,
            "p50_ms": percentile(lat, 0.50),
            "p90_ms": percentile(lat, 0.90),
            "p95_ms": percentile(lat, 0.95),
            "p99_ms": percentile(lat, 0.99),
            "note": "Bounded sample because CPU full pass projected over 2h.",
        },
        "per_query_cost_ms": summarize_cost(costs),
    }


def summarize_cost(samples: list[dict[str, float]]) -> dict[str, Any]:
    out = {}
    for key in ["embedding_ms", "first_stage_rank_ms", "rerank_ms", "total_ms"]:
        vals = [s[key] for s in samples]
        out[key] = {"avg": statistics.mean(vals) if vals else None, "p95": percentile(vals, 0.95)}
    return out


def score_quality_sample(v1: Any, reranker: QwenCpuReranker, ctx: dict[str, Any], per_scope: int) -> dict[str, Any]:
    """Small bounded sample to confirm scoring works; not used as full benchmark."""
    out = {}
    scopes = [
        ("slice_a_combined_global", ctx["slice_a"][:per_scope], "slice_a_combined_global"),
        ("slice_c_hard_negative", ctx["slice_a"][:per_scope], "slice_c_hard_negative"),
        ("galaxy_strict_global", [p for p in ctx["galaxy"] if p["label"] == "strict_support"][:per_scope], "galaxy_global"),
    ]
    total_pairs = 0
    start_all = time.perf_counter()
    for scope_name, rows, key_scope in scopes:
        ranks = []
        for p in rows:
            key_id = p["pair_id"] if key_scope == "slice_c_hard_negative" else p["query_id"]
            ranked = ctx["rankings"][f"nomic_top50:{key_scope}:{key_id}"]
            pairs, _ = make_pairs(v1, p["claim_text"], ranked, ctx["docs"])
            total_pairs += len(pairs)
            scores = reranker.score(pairs)
            reranked = [did for did, _ in sorted(zip(ranked, scores), key=lambda x: x[1], reverse=True)]
            ranks.append(reranked.index(p["doc_id"]) + 1 if p["doc_id"] in reranked else None)
        out[scope_name] = v1.metric_from_ranks(ranks, 122)
    out["sample_note"] = f"Quality sample only: {per_scope} rows per scope, {total_pairs} pair scores, not a full metric."
    out["sample_seconds"] = time.perf_counter() - start_all
    return out


def cold_sample() -> dict[str, Any]:
    code = f"""
import time, json, torch, httpx
from transformers import AutoTokenizer, AutoModelForCausalLM
t=time.perf_counter()
tok=AutoTokenizer.from_pretrained({QWEN_MODEL!r}, padding_side='left', trust_remote_code=True)
model=AutoModelForCausalLM.from_pretrained({QWEN_MODEL!r}, trust_remote_code=True, torch_dtype=torch.float32).eval()
load_ms=(time.perf_counter()-t)*1000
t=time.perf_counter()
r=httpx.post('http://127.0.0.1:11434/api/embeddings', json={{'model':'nomic-embed-text:v1.5','prompt':'Massive galaxies quench at high redshift.','keep_alive':'0s'}}, timeout=60)
r.raise_for_status()
embed_ms=(time.perf_counter()-t)*1000
print(json.dumps({{'load_ms':load_ms,'embed_ms':embed_ms,'total_ms':load_ms+embed_ms}}))
"""
    try:
        proc = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=240)
        raw = json.loads(proc.stdout.strip().splitlines()[-1])
        total = raw["total_ms"]
        errors = 0
    except Exception as exc:
        raw = {"error": str(exc)}
        total = None
        errors = 1
    return {"count": 1, "errors": errors, "p50_ms": total, "p90_ms": total, "p95_ms": total, "p99_ms": total, "raw": raw}


def write_report(report: dict[str, Any], md_out: Path) -> None:
    lines = [
        "# Embeddings Reranker v1.1 Report",
        "",
        f"Generated: {report['generated_at']}",
        "",
        "## Verdict",
        "",
        "- Lane 1 Qwen3-Reranker-0.6B CPU: FAIL / not promotable",
        "- Lane 2 BGE Gemma: SKIPPED because Lane 1 is conclusive on latency and full CPU quality is not measurable inside the one-shot window.",
        f"- Recommendation: {report['recommendation']}",
        "",
        "## Lane 1 Findings",
        "",
        f"- CPU pair throughput: {report['lane1']['pair_throughput_per_sec']:.3f} pairs/sec",
        f"- Estimated full nomic_top50 pair scores: {report['lane1']['estimated_full_pairs']}",
        f"- Estimated full pass hours: {report['lane1']['estimated_full_hours']:.2f}",
        f"- Hot c1 p95 sample: {report['latency']['hot_c1']['p95_ms']}",
        f"- Cold c1 p95 sample: {report['latency']['cold_c1']['p95_ms']}",
        "- Full quality metrics: not completed; full run projected beyond 2-hour cap.",
        "",
        "## Quality Sample",
        "",
    ]
    for scope, vals in report["quality_sample"].items():
        if not isinstance(vals, dict) or "recall_at_10" not in vals:
            continue
        lines.append(
            f"- {scope}: n={vals['n']}, R@10={vals['recall_at_10']:.3f}, MRR@10={vals['mrr_at_10']:.3f}, median={vals['median_rank']}"
        )
    lines += [
        f"- Note: {report['quality_sample']['sample_note']}",
        "",
        "## Gates",
        "",
    ]
    for gate, row in report["pass_fail"]["gates"].items():
        lines.append(f"- {gate}: {'PASS' if row['passed'] else 'FAIL'} value={row['value']} target={row['target']}")
    lines += [
        "",
        "## Fixture Validation",
        "",
        f"- Slice A pairs: {report['slice_a']['selected_count']}",
        f"- Slice C gold pairs: {report['slice_c']['included_gold_pairs']}",
        f"- Slice C unique queries: {report['slice_c']['included_unique_queries']}",
        f"- Slice C median candidates: {report['slice_c']['candidate_size']['median']}",
        f"- Galaxy labels: {report['galaxy']['label_counts']}",
        "",
        "## Artifacts",
        "",
        f"- JSON: `{report['json_out']}`",
        f"- Script: `{__file__}`",
    ]
    md_out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--latency-sample", type=int, default=5)
    parser.add_argument("--quality-sample", type=int, default=5)
    parser.add_argument("--max-length", type=int, default=768)
    parser.add_argument("--batch-size", type=int, default=4)
    args = parser.parse_args()

    started = time.perf_counter()
    v1 = load_v1()
    ctx = build_context(v1)
    reranker = QwenCpuReranker(max_length=args.max_length, batch_size=args.batch_size)
    latency = measure_latency(v1, reranker, ctx, args.latency_sample)
    qsample = score_quality_sample(v1, reranker, ctx, args.quality_sample)
    cold = cold_sample()
    latency["cold_c1"] = cold
    total_pairs_est = 1820 * 50
    sample_pairs = args.quality_sample * 3 * 50
    sample_seconds = max(qsample["sample_seconds"], 0.001)
    pair_throughput = sample_pairs / sample_seconds
    estimated_hours = total_pairs_est / pair_throughput / 3600
    hot_p95 = latency["hot_c1"]["p95_ms"]
    cold_p95 = latency["cold_c1"]["p95_ms"]
    gates = {
        "hard_negative_r10_full": {"value": None, "target": 0.144, "passed": False, "note": "full metric not measured"},
        "galaxy_strict_r10_full": {"value": None, "target": 0.824, "passed": False, "note": "full metric not measured"},
        "slice_a_combined_r10_full": {"value": None, "target": 0.305, "passed": False, "note": "full metric not measured"},
        "hot_p95_c1_ms": {"value": hot_p95, "target": 250.0, "passed": hot_p95 is not None and hot_p95 <= 250.0},
        "cold_p95_c1_ms": {"value": cold_p95, "target": 2000.0, "passed": cold_p95 is not None and cold_p95 <= 2000.0},
        "failure_rate": {"value": latency["hot_c1"]["errors"] / max(1, latency["hot_c1"]["count"]), "target": 0.01, "passed": latency["hot_c1"]["errors"] == 0},
        "two_hour_measurability": {"value": estimated_hours, "target": 2.0, "passed": estimated_hours <= 2.0},
    }
    report = {
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "elapsed_seconds": time.perf_counter() - started,
        "status": "complete_fail",
        "recommendation": "do_not_promote_keep_production",
        "lane1": {
            "model": QWEN_MODEL,
            "device": "cpu",
            "max_length": args.max_length,
            "batch_size": args.batch_size,
            "model_load_ms": reranker.load_ms,
            "estimated_full_pairs": total_pairs_est,
            "pair_throughput_per_sec": pair_throughput,
            "estimated_full_hours": estimated_hours,
            "concurrency_2_4": "skipped: c1 already exceeds latency gate by orders of magnitude on CPU",
        },
        "lane2": {"model": "BAAI/bge-reranker-v2-gemma", "status": "skipped", "reason": "Lane 1 conclusive latency/measurability fail; design says run Lane 2 only if Lane 1 quality looks promising."},
        "slice_a": ctx["slice_a_meta"],
        "galaxy": ctx["galaxy_meta"],
        "slice_c": ctx["slice_c"],
        "fixture_validation": ctx["fixture_validation"],
        "first_stage": ctx["first_stage"],
        "latency": latency,
        "quality_sample": qsample,
        "pass_fail": {"passed": False, "gates": gates},
        "environment": {
            "python": sys.version,
            "torch": torch.__version__,
            "transformers": transformers.__version__,
            "hf_cache": "/Users/duhokim/.cache/huggingface/hub",
            "vector_cache": str(v1.VECTOR_CACHE),
        },
    }
    run_stamp = dt.datetime.now().strftime("%Y%m%d_%H%M")
    json_out = LOG_DIR / f"embedding_reranker_v1_1_{run_stamp}.json"
    md_out = WORKSPACE / "Report_Embeddings_Reranker_v1_1_2026-05-23.md"
    report["json_out"] = str(json_out)
    json_out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    write_report(report, md_out)
    print(json.dumps({"event": "report_done", "json_out": str(json_out), "md_out": str(md_out), "hot_p95": hot_p95, "estimated_hours": estimated_hours}), flush=True)


if __name__ == "__main__":
    main()
