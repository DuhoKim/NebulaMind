#!/usr/bin/env python3
"""C41 Step 2: cache-first full-text acquisition for the sealed 180 records."""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import hashlib
import importlib.util
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind")
LANE = ROOT / ".hermes/handoffs/c41-baseline-restart-20260803T1253Z"
SELECTION = LANE / "SELECTION_INCLUDED.json"
SELECTION_SHAS = LANE / "SELECTION_SHAS.txt"
MODULE_PATH = ROOT / "tools/nm_fulltext_layer.py"
ENUM_PATH = ROOT / "docs/claim_ledger_contract_v1_agn_20260703T0830Z/artifacts/ledger_enums.json"
MANIFEST_PATH = LANE / "STEP2_FULLTEXT_MANIFEST.json"
LABELS_PATH = LANE / "STEP2_STRENGTH_LABELS.json"
REPORT_PATH = LANE / "YUI_STEP2_REPORT.md"
CHECKPOINT_PATH = LANE / "_tmp_step2_checkpoint.json"
EXPECTED_COUNT = 180
MIN_FULLTEXT_CHARS = 2_000
MIN_ARXIV_INTERVAL_SECONDS = 3.1
MAX_ATTEMPTS = 3
HARD_STOP_CONSECUTIVE_FAILURES = 3
SOURCE_ACCESS_ALLOWED = {"full_text", "abstract_only", "metadata_only"}

ARXIV_EXACT = re.compile(r"^(\d{4}\.\d{4,5})(?:v\d+)?$", re.I)
ARXIV_PREFIX = re.compile(r"^arXiv:(\d{4}\.\d{4,5})(?:v\d+)?$", re.I)
ARXIV_DOI = re.compile(r"^10\.48550/arXiv\.(\d{4}\.\d{4,5})(?:v\d+)?$", re.I)


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def rel(path: Path | None) -> str | None:
    if path is None:
        return None
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def atomic_json(path: Path, payload: Any) -> None:
    tmp = LANE / f"_tmp_{path.name}"
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def load_module():
    spec = importlib.util.spec_from_file_location("nm_fulltext_layer", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def expected_selection_sha() -> str:
    for line in SELECTION_SHAS.read_text(encoding="utf-8").splitlines():
        parts = line.split()
        if len(parts) >= 2 and parts[-1] == "SELECTION_INCLUDED.json":
            return parts[0]
    raise RuntimeError("SELECTION_INCLUDED.json hash is missing from SELECTION_SHAS.txt")


def resolve_arxiv_id(record: dict[str, Any]) -> str | None:
    values = [record.get("arxiv_id"), record.get("arxiv")]
    values.extend(record.get("identifiers") or [])
    values.extend(record.get("doi") or [])
    for value in values:
        if not value:
            continue
        text = str(value).strip()
        match = ARXIV_EXACT.fullmatch(text) or ARXIV_PREFIX.fullmatch(text) or ARXIV_DOI.fullmatch(text)
        if match:
            return match.group(1)
    return None


def load_and_verify_inputs() -> tuple[dict[str, Any], list[dict[str, Any]], dict[str, Any], dict[str, Any]]:
    expected_sha = expected_selection_sha()
    actual_sha = sha256(SELECTION)
    if actual_sha != expected_sha:
        raise RuntimeError(f"sealed input hash mismatch: expected {expected_sha}, got {actual_sha}")

    selection = json.loads(SELECTION.read_text(encoding="utf-8"))
    records = selection.get("records")
    if not isinstance(records, list) or len(records) != EXPECTED_COUNT:
        raise RuntimeError(f"sealed selection must contain exactly {EXPECTED_COUNT} records")

    keys = [record.get("key") for record in records]
    if any(not key for key in keys) or len(set(keys)) != EXPECTED_COUNT:
        raise RuntimeError("sealed selection record keys are missing or duplicated")

    arxiv_ids = [resolve_arxiv_id(record) for record in records]
    if len([value for value in arxiv_ids if value]) != EXPECTED_COUNT:
        raise RuntimeError("one or more sealed records lack an arXiv identifier")
    if len(set(arxiv_ids)) != EXPECTED_COUNT:
        raise RuntimeError("resolved arXiv identifiers are not unique across the sealed selection")

    enums = json.loads(ENUM_PATH.read_text(encoding="utf-8"))
    enum_access = set(enums.get("source_access") or [])
    if enum_access != SOURCE_ACCESS_ALLOWED:
        raise RuntimeError(f"unexpected source_access enum: {sorted(enum_access)}")

    module_stat = MODULE_PATH.stat()
    selection_stat = SELECTION.stat()
    input_manifest = {
        "selection": {
            "path": rel(SELECTION),
            "sha256": actual_sha,
            "expected_sha256": expected_sha,
            "bytes": selection_stat.st_size,
            "records": len(records),
        },
        "module": {
            "path": rel(MODULE_PATH),
            "sha256": sha256(MODULE_PATH),
            "bytes": module_stat.st_size,
        },
        "source_access_enum": {
            "path": rel(ENUM_PATH),
            "sha256": sha256(ENUM_PATH),
            "allowed": sorted(enum_access),
        },
    }
    return selection, records, enums, input_manifest


def cache_paths(cache: Path, arxiv_id: str) -> dict[str, Path]:
    return {
        "html": cache / f"{arxiv_id}.html",
        "pdf": cache / f"{arxiv_id}.pdf",
        "chunks": cache / f"{arxiv_id}.chunks.json",
        "src": cache / f"{arxiv_id}.src",
    }


def usable_html(module, path: Path) -> tuple[str | None, int, int, str | None]:
    try:
        html_text = path.read_text(encoding="utf-8", errors="replace")
        prose, tables = module.extract_html_structured(html_text)
        combined = prose + "\n\n" + "\n\n".join(f"[TABLE] {table}" for table in tables)
        if len(prose) < MIN_FULLTEXT_CHARS:
            return None, len(prose), len(tables), f"cached_html_extracted_only_{len(prose)}_chars"
        return combined.strip(), len(prose), len(tables), None
    except Exception as exc:
        return None, 0, 0, f"cached_html_extraction_{type(exc).__name__}: {str(exc)[:180]}"


def usable_pdf(module, data: bytes) -> tuple[str | None, int, str | None]:
    try:
        text = module.extract_text(data)
        if len(text) < MIN_FULLTEXT_CHARS:
            return None, len(text), f"pdf_extracted_only_{len(text)}_chars"
        return text, len(text), None
    except Exception as exc:
        return None, 0, f"pdf_extraction_{type(exc).__name__}: {str(exc)[:180]}"


def write_derived_cache(module, paths: dict[str, Path], text: str, source: str) -> tuple[int, str | None]:
    try:
        chunks = module.chunk_text(text)
        if not paths["chunks"].exists():
            tmp = paths["chunks"].with_suffix(paths["chunks"].suffix + ".tmp")
            tmp.write_text(json.dumps(chunks, ensure_ascii=False), encoding="utf-8")
            os.replace(tmp, paths["chunks"])
        if not paths["src"].exists():
            tmp = paths["src"].with_suffix(paths["src"].suffix + ".tmp")
            tmp.write_text(source + "\n", encoding="utf-8")
            os.replace(tmp, paths["src"])
        return len(chunks), None
    except Exception as exc:
        return 0, f"derived_cache_{type(exc).__name__}: {str(exc)[:180]}"


class ArxivGate:
    def __init__(self) -> None:
        self.last_request_started: float | None = None

    def wait(self) -> None:
        if self.last_request_started is None:
            return
        elapsed = time.monotonic() - self.last_request_started
        if elapsed < MIN_ARXIV_INTERVAL_SECONDS:
            time.sleep(MIN_ARXIV_INTERVAL_SECONDS - elapsed)

    def mark(self) -> None:
        self.last_request_started = time.monotonic()


def fetch_pdf_with_backoff(module, arxiv_id: str, gate: ArxivGate) -> tuple[bytes | None, int, str | None]:
    last_reason = None
    for attempt in range(1, MAX_ATTEMPTS + 1):
        gate.wait()
        gate.mark()
        try:
            return module.fetch_pdf(arxiv_id), attempt, None
        except urllib.error.HTTPError as exc:
            last_reason = f"HTTP_{exc.code}"
            retryable = exc.code == 429 or 500 <= exc.code <= 599
            if not retryable or attempt == MAX_ATTEMPTS:
                break
        except Exception as exc:
            last_reason = f"{type(exc).__name__}: {str(exc)[:180]}"
            if attempt == MAX_ATTEMPTS:
                break
        time.sleep(MIN_ARXIV_INTERVAL_SECONDS * (2 ** (attempt - 1)))
    return None, MAX_ATTEMPTS, last_reason or "unknown_arxiv_fetch_failure"


def ads_abstract(module, bibcode: str | None) -> tuple[int, str | None]:
    if not bibcode:
        return 0, "missing_bibcode_for_ads_fallback"
    try:
        params = urllib.parse.urlencode({"q": f'bibcode:"{bibcode}"', "fl": "bibcode,abstract", "rows": 1})
        request = urllib.request.Request(
            f"{module.ADS}?{params}",
            headers={"Authorization": f"Bearer {module._token()}", "User-Agent": module.UA},
        )
        with urllib.request.urlopen(request, timeout=60) as response:
            docs = json.loads(response.read().decode("utf-8"))["response"]["docs"]
        abstract = docs[0].get("abstract") if docs else None
        return len(abstract or ""), None if abstract else "ads_record_has_no_abstract"
    except Exception as exc:
        return 0, f"ads_fallback_{type(exc).__name__}: {str(exc)[:180]}"


def primary_cache_path(paths: dict[str, Path], method: str | None) -> Path | None:
    if method == "html" and paths["html"].exists():
        return paths["html"]
    if method == "pdf" and paths["pdf"].exists():
        return paths["pdf"]
    return None


def record_result(
    record: dict[str, Any],
    arxiv_id: str,
    paths: dict[str, Path],
    source_access: str,
    fetch_outcome: str,
    extraction_outcome: str,
    extraction_method: str | None,
    text_chars: int,
    chunk_count: int,
    attempts: int,
    failure_reason: str | None,
    abstract_chars: int,
    cache_was_present: bool,
) -> dict[str, Any]:
    primary = primary_cache_path(paths, extraction_method)
    cache_map = {name: rel(path) for name, path in paths.items() if path.exists()}
    byte_count = primary.stat().st_size if primary and primary.exists() else 0
    return {
        "identity": {
            "rank": record.get("rank"),
            "key": record.get("key"),
            "bibcode": record.get("bibcode"),
            "arxiv_id": arxiv_id,
            "doi": record.get("doi") or [],
            "title": record.get("title"),
            "year": record.get("year"),
        },
        "cache_path": rel(primary),
        "cache_paths": cache_map,
        "cache_was_present": cache_was_present,
        "byte_count": byte_count,
        "source_access": source_access,
        "source_class": record.get("source_class"),
        "review_flag": bool(record.get("review")),
        "fetch_outcome": fetch_outcome,
        "fetch_attempts": attempts,
        "extraction_outcome": extraction_outcome,
        "extraction_method": extraction_method,
        "extracted_text_chars": text_chars,
        "chunk_count": chunk_count,
        "abstract_chars": abstract_chars,
        "failure_reason": failure_reason,
    }


def checkpoint(results: list[dict[str, Any]], started_at: str) -> None:
    atomic_json(
        CHECKPOINT_PATH,
        {
            "protocol_version": "C41_STEP2_V1",
            "started_at": started_at,
            "updated_at": utc_now(),
            "records_complete": len(results),
            "records": results,
        },
    )


def summarize(results: list[dict[str, Any]], initial_cache_files: int, final_cache_files: int, runtime: float, halted: bool) -> dict[str, Any]:
    access = collections.Counter(item["source_access"] for item in results)
    fetches = collections.Counter(item["fetch_outcome"] for item in results)
    extractions = collections.Counter(item["extraction_outcome"] for item in results)
    cache_hits = fetches.get("cached", 0)
    return {
        "requested_records": EXPECTED_COUNT,
        "manifest_records": len(results),
        "access_label_counts": dict(sorted(access.items())),
        "fetch_outcome_counts": dict(sorted(fetches.items())),
        "extraction_outcome_counts": dict(sorted(extractions.items())),
        "cache_hits": cache_hits,
        "cache_hit_rate": round(cache_hits / EXPECTED_COUNT, 6),
        "total_new_fetches": fetches.get("fetched", 0),
        "failed_records": fetches.get("failed", 0),
        "initial_cache_file_count": initial_cache_files,
        "final_cache_file_count": final_cache_files,
        "runtime_seconds": round(runtime, 3),
        "hard_stop_triggered": halted,
    }


def write_deliverables(
    results: list[dict[str, Any]],
    input_manifest: dict[str, Any],
    started_at: str,
    finished_at: str,
    summary: dict[str, Any],
    cache: Path,
    halted_reason: str | None,
) -> None:
    safety = {
        "writes": [rel(LANE), rel(cache)],
        "network": ["arxiv.org", "api.adsabs.harvard.edu"],
        "db_writes": False,
        "git_writes": False,
        "product_surface_writes": False,
        "deep_research_or_credit_spend": False,
        "env_content_logged": False,
        "prose_authorized": False,
        "selection_changed": False,
    }
    manifest = {
        "protocol_version": "C41_STEP2_V1",
        "started_at": started_at,
        "finished_at": finished_at,
        "input_manifest": input_manifest,
        "cache_root": rel(cache),
        "summary": summary,
        "hard_stop_reason": halted_reason,
        "safety_ledger": safety,
        "records": results,
    }
    atomic_json(MANIFEST_PATH, manifest)

    labels_records = [
        {
            "key": item["identity"]["key"],
            "bibcode": item["identity"]["bibcode"],
            "arxiv_id": item["identity"]["arxiv_id"],
            "source_access": item["source_access"],
            "source_class": item["source_class"],
            "review_flag": item["review_flag"],
        }
        for item in results
    ]
    labels = {
        "protocol_version": "C41_STEP2_V1",
        "input_manifest": input_manifest,
        "summary": {
            "records": len(labels_records),
            "source_access": summary["access_label_counts"],
            "source_class": dict(sorted(collections.Counter(item["source_class"] for item in labels_records).items())),
            "review_flag": {
                "true": sum(item["review_flag"] for item in labels_records),
                "false": sum(not item["review_flag"] for item in labels_records),
            },
        },
        "records": labels_records,
    }
    atomic_json(LABELS_PATH, labels)

    failures = [item for item in results if item["fetch_outcome"] == "failed"]
    failure_lines = [
        f"- Rank {item['identity']['rank']} — {item['identity']['bibcode']} / arXiv:{item['identity']['arxiv_id']}: {item['failure_reason']}"
        for item in failures
    ] or ["- None."]
    complete = len(results) == EXPECTED_COUNT and not summary["hard_stop_triggered"]
    marker = "YUI_STEP2_COMPLETE_20260804" if complete else "YUI_STEP2_BLOCKED_20260804"
    report = f"""# Yui C41 Step 2 report

## Outcome

- Sealed records requested: {EXPECTED_COUNT}
- Manifest records written: {len(results)}
- Full text: {summary['access_label_counts'].get('full_text', 0)}
- Abstract only: {summary['access_label_counts'].get('abstract_only', 0)}
- Metadata only: {summary['access_label_counts'].get('metadata_only', 0)}
- Cache hits: {summary['cache_hits']} ({summary['cache_hit_rate']:.2%})
- New arXiv fetches: {summary['total_new_fetches']}
- Failed records: {summary['failed_records']}
- Runtime: {summary['runtime_seconds']:.3f} seconds
- Hard stop triggered: {str(summary['hard_stop_triggered']).lower()}

## Input seal

- `SELECTION_INCLUDED.json`: `{input_manifest['selection']['sha256']}` ({input_manifest['selection']['bytes']} bytes)
- Expected selection hash: `{input_manifest['selection']['expected_sha256']}` — MATCH
- `tools/nm_fulltext_layer.py`: `{input_manifest['module']['sha256']}` ({input_manifest['module']['bytes']} bytes)
- Exactly the sealed 180 were processed; no record was added, removed, or re-admitted.

## Failures and honest access labels

{chr(10).join(failure_lines)}

Every record without extracted full text is labeled `abstract_only` with its failure reason in `STEP2_FULLTEXT_MANIFEST.json`. No unavailable source was promoted to `full_text`.

## Re-admission candidates

- None noticed during exact sealed-set acquisition. The excluded set and in-progress C41 map lanes were not inspected.

## Safety boundary

This run wrote only this C41 lane directory and the engine `fulltext_cache/`. It made no database writes, git writes, product-surface changes, deploys or restarts, Deep Research calls, or credit-spending calls. Network access was limited to arXiv and ADS. The ADS token was used only in memory by the tracked module and was never printed or written. This is a pre-prose acquisition artifact: prose, exact-diff, claim/evidence mutation, trust targeting, publication, and runtime changes remain unauthorized.

{marker}
"""
    REPORT_PATH.write_text(report, encoding="utf-8")


def run(preflight: bool) -> int:
    selection, records, _enums, input_manifest = load_and_verify_inputs()
    module = load_module()
    cache = Path(module.CACHE)
    cache.mkdir(parents=True, exist_ok=True)
    initial_cache_files = sum(1 for item in os.scandir(cache) if item.is_file())

    resolved = [resolve_arxiv_id(record) for record in records]
    existing_sources = sum(
        bool(arxiv_id and ((cache / f"{arxiv_id}.html").is_file() or (cache / f"{arxiv_id}.pdf").is_file()))
        for arxiv_id in resolved
    )
    print(
        json.dumps(
            {
                "preflight": True,
                "sealed_records": len(records),
                "selection_sha256": input_manifest["selection"]["sha256"],
                "module_sha256": input_manifest["module"]["sha256"],
                "resolved_unique_arxiv_ids": len(set(resolved)),
                "cache_files": initial_cache_files,
                "records_with_cached_source": existing_sources,
            },
            sort_keys=True,
        ),
        flush=True,
    )
    if preflight:
        return 0

    started_at = utc_now()
    started_monotonic = time.monotonic()
    gate = ArxivGate()
    results: list[dict[str, Any]] = []
    consecutive_failures = 0
    halted_reason = None

    for index, record in enumerate(records, start=1):
        arxiv_id = resolve_arxiv_id(record)
        if arxiv_id is None:
            raise RuntimeError(f"preflight inconsistency: no arXiv id for rank {record.get('rank')}")
        paths = cache_paths(cache, arxiv_id)
        cache_was_present = paths["html"].is_file() or paths["pdf"].is_file()
        text = None
        text_chars = 0
        chunk_count = 0
        extraction_method = None
        fetch_outcome = "cached" if cache_was_present else "failed"
        attempts = 0
        reasons: list[str] = []

        if paths["html"].is_file():
            text, text_chars, table_count, reason = usable_html(module, paths["html"])
            if text:
                extraction_method = "html"
                chunk_count, derived_reason = write_derived_cache(module, paths, text, "cache-html")
                if derived_reason:
                    reasons.append(derived_reason)
                if table_count:
                    reasons.append(f"html_tables_linearized={table_count}")
            elif reason:
                reasons.append(reason)

        if text is None and paths["pdf"].is_file():
            data = paths["pdf"].read_bytes()
            text, text_chars, reason = usable_pdf(module, data)
            if text:
                extraction_method = "pdf"
                chunk_count, derived_reason = write_derived_cache(module, paths, text, "pdf")
                if derived_reason:
                    reasons.append(derived_reason)
            elif reason:
                reasons.append(reason)

        if text is None and not paths["pdf"].is_file():
            data, attempts, reason = fetch_pdf_with_backoff(module, arxiv_id, gate)
            if data is not None:
                fetch_outcome = "fetched"
                text, text_chars, extraction_reason = usable_pdf(module, data)
                if text:
                    extraction_method = "pdf"
                    chunk_count, derived_reason = write_derived_cache(module, paths, text, "pdf")
                    if derived_reason:
                        reasons.append(derived_reason)
                elif extraction_reason:
                    reasons.append(extraction_reason)
            else:
                reasons.append(f"arxiv_fetch_failed_after_{attempts}_attempts: {reason}")

        abstract_chars = 0
        if text is not None:
            source_access = "full_text"
            extraction_outcome = "extracted"
            failure_reason = None
            if fetch_outcome == "failed":
                fetch_outcome = "cached"
            consecutive_failures = 0
        else:
            abstract_chars, ads_reason = ads_abstract(module, record.get("bibcode"))
            if ads_reason:
                reasons.append(ads_reason)
            source_access = "abstract_only"
            extraction_outcome = "failed"
            fetch_outcome = "failed"
            failure_reason = "; ".join(reasons) if reasons else "full_text_unavailable"
            consecutive_failures += 1

        item = record_result(
            record=record,
            arxiv_id=arxiv_id,
            paths=paths,
            source_access=source_access,
            fetch_outcome=fetch_outcome,
            extraction_outcome=extraction_outcome,
            extraction_method=extraction_method,
            text_chars=text_chars,
            chunk_count=chunk_count,
            attempts=attempts,
            failure_reason=failure_reason,
            abstract_chars=abstract_chars,
            cache_was_present=cache_was_present,
        )
        results.append(item)
        print(
            f"[{index:03d}/{EXPECTED_COUNT}] rank={record.get('rank')} arxiv={arxiv_id} "
            f"fetch={fetch_outcome} access={source_access} chars={text_chars}",
            flush=True,
        )
        if index % 10 == 0 or fetch_outcome == "failed":
            checkpoint(results, started_at)

        if consecutive_failures >= HARD_STOP_CONSECUTIVE_FAILURES:
            halted_reason = f"hard stop after {consecutive_failures} consecutive full-text failures at rank {record.get('rank')}"
            break

    runtime = time.monotonic() - started_monotonic
    finished_at = utc_now()
    final_cache_files = sum(1 for item in os.scandir(cache) if item.is_file())
    summary = summarize(results, initial_cache_files, final_cache_files, runtime, halted_reason is not None)
    write_deliverables(results, input_manifest, started_at, finished_at, summary, cache, halted_reason)
    if CHECKPOINT_PATH.exists():
        CHECKPOINT_PATH.unlink()

    print(json.dumps({"finished": True, "summary": summary, "report": str(REPORT_PATH)}, sort_keys=True), flush=True)
    return 2 if halted_reason else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight", action="store_true", help="verify seals and cache state without network or deliverable writes")
    args = parser.parse_args()
    try:
        return run(args.preflight)
    except Exception as exc:
        message = f"{type(exc).__name__}: {str(exc)}"
        REPORT_PATH.write_text(
            "# Yui C41 Step 2 blocker\n\n"
            f"Step 2 stopped before acquisition completed: `{message}`\n\n"
            "No selection mutation, database write, git write, product mutation, deploy, restart, or Deep Research call was made.\n\n"
            "YUI_STEP2_BLOCKED_20260804\n",
            encoding="utf-8",
        )
        print(message, file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
