#!/usr/bin/env python3
"""R3 jury calibration spike for the page-57 KEEP pile.

Read-only: reconstructs the fast-screen KEEP pile, runs the targeted ADS jury
through the subprocess-isolated juror path, and writes raw/parsed diagnostics.
"""

from __future__ import annotations

import argparse
import asyncio
import datetime as dt
import json
import logging
import random
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from app.config import settings
from app.database import SessionLocal
from scripts import targeted_ads_miner as miner

logger = logging.getLogger("jury_calibration_spike")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")


def extract_pre_downgrade(raw: str) -> dict[str, Any]:
    cleaned = miner.clean_llm_response(miner.strip_think_blocks(raw or ""))
    result: dict[str, Any] = {
        "verdict": None,
        "sentence": None,
        "confidence": None,
        "parse_mode": None,
    }

    trimmed = cleaned.strip()
    json_start = trimmed.find("{")
    json_end = trimmed.rfind("}")
    if json_start != -1 and json_end != -1 and json_end > json_start:
        try:
            parsed = json.loads(trimmed[json_start : json_end + 1])
            if "vote" in parsed:
                vote = parsed["vote"]
                result["verdict"] = "SUPPORTS" if vote == 1 else ("REFUTES" if vote == -1 else "ABSTAIN")
            elif "stance_correct" in parsed:
                result["verdict"] = "SUPPORTS" if parsed["stance_correct"] is True else "ABSTAIN"
            result["sentence"] = parsed.get("reason")
            result["confidence"] = "MEDIUM"
            result["parse_mode"] = "json"
            if result["verdict"]:
                return result
        except Exception:
            pass

    verdict_m = miner._last_match(miner.VERDICT_RE, cleaned)
    sentence_m = miner._last_match(miner.SENTENCE_RE, cleaned)
    conf_m = miner._last_match(miner.CONF_RE, cleaned)
    verdict = verdict_m.group(1).upper() if verdict_m else None
    if verdict is None:
        lowered = cleaned.lower()
        for keyword in ("refutes", "abstain", "supports"):
            if keyword in lowered:
                verdict = keyword.upper()
                break
    result["verdict"] = verdict
    result["sentence"] = sentence_m.group(1).strip() if sentence_m else None
    result["confidence"] = conf_m.group(1).upper() if conf_m else "LOW"
    result["parse_mode"] = "marker_or_keyword" if verdict else None
    return result


def sentence_in_abstract(sentence: str | None, abstract: str | None) -> bool:
    if not sentence or sentence.upper() == "NONE":
        return False
    return miner.normalize_for_substring(sentence) in miner.normalize_for_substring(abstract or "")


def make_juror_diagnostic(raw_result: dict[str, Any], abstract: str | None) -> dict[str, Any]:
    label = raw_result.get("label") or "unknown"
    raw = raw_result.get("raw") or ""
    pre = extract_pre_downgrade(raw)
    parsed = miner.parse_juror(label, raw, abstract or "")
    quoted_ok = sentence_in_abstract(pre.get("sentence"), abstract)
    bypass_verdict = pre.get("verdict")
    if bypass_verdict in {"SUPPORTS", "REFUTES"} and not pre.get("sentence"):
        bypass_verdict = "ABSTAIN"
    if isinstance(pre.get("sentence"), str) and pre["sentence"].upper() == "NONE":
        bypass_verdict = "ABSTAIN"

    return {
        "label": label,
        "raw": raw,
        "subprocess_abstain_reason": raw_result.get("subprocess_abstain_reason"),
        "pre_downgrade": pre,
        "parsed": {
            "verdict": parsed.verdict if parsed else None,
            "sentence": parsed.sentence if parsed else None,
            "confidence": parsed.confidence if parsed else None,
            "downgraded": parsed.downgraded if parsed else False,
        },
        "quote_substring_match": quoted_ok,
        "verbatim_downgrade_triggered": bool(parsed and parsed.downgraded),
        "bypass_verbatim_verdict": bypass_verdict,
    }


def select_claim_ids(page_id: int, limit: int | None) -> list[int]:
    db = SessionLocal()
    try:
        claims = miner.select_claims(db, page_id, [], limit, None)
        return [claim.id for claim in claims]
    finally:
        db.close()


def reconstruct_keep_pile(page_id: int, claim_limit: int | None, sample_size: int, seed: int) -> tuple[list[miner.Candidate], dict[str, Any]]:
    claim_ids = select_claim_ids(page_id, claim_limit)
    db = SessionLocal()
    try:
        candidates, _per_claim = miner.collect_candidates(db, claim_ids)
    finally:
        db.close()

    batches = miner.build_screen_batches(candidates, int(settings.SCREEN_BATCH))
    outcomes, fallback_batches = asyncio.run(miner.fast_screen_async(batches))
    keep: list[miner.Candidate] = []
    discard_count = 0
    for ref, candidate in enumerate(candidates):
        outcome = outcomes.get(ref, miner.ScreenOutcome(ref=ref, pre_filter="KEEP", fail_open=True))
        if outcome.pre_filter == "DISCARD":
            discard_count += 1
        else:
            keep.append(candidate)

    rng = random.Random(seed)
    sample = list(keep)
    rng.shuffle(sample)
    sample = sample[: min(sample_size, len(sample))]
    meta = {
        "page_id": page_id,
        "claim_ids": claim_ids,
        "claims": len(claim_ids),
        "candidate_count": len(candidates),
        "keep_count": len(keep),
        "discard_count": discard_count,
        "fallback_batches": fallback_batches,
        "sample_size_requested": sample_size,
        "sample_size": len(sample),
        "seed": seed,
    }
    return sample, meta


def calibrate(candidates: list[miner.Candidate]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    per_model: dict[str, dict[str, Any]] = defaultdict(
        lambda: {
            "parsed": Counter(),
            "pre_downgrade": Counter(),
            "bypass_verbatim": Counter(),
            "verbatim_downgrades": 0,
            "subprocess_timeouts": 0,
            "subprocess_abstains": Counter(),
            "latency_s_total": 0.0,
            "calls": 0,
        }
    )

    models = miner.jury_models()
    for index, candidate in enumerate(candidates, start=1):
        logger.info(
            "calibration_candidate_start index=%s/%s claim_id=%s title=%r",
            index,
            len(candidates),
            candidate.claim.id,
            (candidate.record.title or "")[:120],
        )
        prompt = miner.user_prompt(candidate.claim, candidate.record)
        jurors = []
        for model in models:
            started = time.monotonic()
            raw_result = miner._call_juror_subprocess(model, prompt)
            latency_s = time.monotonic() - started
            diag = make_juror_diagnostic(raw_result, candidate.record.abstract)
            diag["latency_s"] = round(latency_s, 3)
            jurors.append(diag)

            label = diag["label"]
            stats = per_model[label]
            stats["calls"] += 1
            stats["latency_s_total"] += latency_s
            stats["parsed"][diag["parsed"]["verdict"] or "UNPARSED"] += 1
            stats["pre_downgrade"][diag["pre_downgrade"]["verdict"] or "UNPARSED"] += 1
            stats["bypass_verbatim"][diag["bypass_verbatim_verdict"] or "UNPARSED"] += 1
            if diag["verbatim_downgrade_triggered"]:
                stats["verbatim_downgrades"] += 1
            reason = diag.get("subprocess_abstain_reason")
            if reason:
                stats["subprocess_abstains"][reason] += 1
                if reason == "timeout":
                    stats["subprocess_timeouts"] += 1

        rows.append(
            {
                "index": index,
                "claim": {
                    "id": candidate.claim.id,
                    "text": candidate.claim.text,
                    "section": candidate.claim.section,
                },
                "paper": {
                    "title": candidate.record.title,
                    "year": candidate.record.year,
                    "bibcode": candidate.record.bibcode,
                    "arxiv_id": candidate.record.arxiv_id,
                    "doi": candidate.record.doi,
                    "abstract": candidate.record.abstract,
                },
                "query": candidate.query,
                "jurors": jurors,
            }
        )
        logger.info("calibration_candidate_done index=%s/%s claim_id=%s", index, len(candidates), candidate.claim.id)

    summary_models = {}
    for label, stats in per_model.items():
        calls = stats["calls"] or 1
        summary_models[label] = {
            "calls": stats["calls"],
            "parsed_distribution": dict(stats["parsed"]),
            "pre_downgrade_distribution": dict(stats["pre_downgrade"]),
            "bypass_verbatim_distribution": dict(stats["bypass_verbatim"]),
            "verbatim_downgrades": stats["verbatim_downgrades"],
            "subprocess_timeouts": stats["subprocess_timeouts"],
            "subprocess_abstain_reasons": dict(stats["subprocess_abstains"]),
            "avg_latency_s": round(stats["latency_s_total"] / calls, 3),
        }

    return rows, {"per_model": summary_models}


def main() -> int:
    parser = argparse.ArgumentParser(description="R3 jury calibration spike")
    parser.add_argument("--page-id", type=int, default=57)
    parser.add_argument("--sample-size", type=int, default=30)
    parser.add_argument("--claim-limit", type=int, default=None)
    parser.add_argument("--seed", type=int, default=57)
    parser.add_argument(
        "--output",
        default=str(BACKEND_ROOT / "logs" / "jury_calibration_r3_results.json"),
    )
    args = parser.parse_args()

    started = dt.datetime.now(dt.timezone.utc)
    candidates, keep_meta = reconstruct_keep_pile(args.page_id, args.claim_limit, args.sample_size, args.seed)
    rows, summary = calibrate(candidates)
    finished = dt.datetime.now(dt.timezone.utc)
    result = {
        "task": "jury_calibration_r3",
        "started_at": started.isoformat(),
        "finished_at": finished.isoformat(),
        "elapsed_s": round((finished - started).total_seconds(), 3),
        "keep_pile": keep_meta,
        "subprocess_timeout_s": miner.JUROR_SUBPROCESS_TIMEOUT_SECONDS,
        "summary": summary,
        "rows": rows,
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"output": str(output), **keep_meta, **summary}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
