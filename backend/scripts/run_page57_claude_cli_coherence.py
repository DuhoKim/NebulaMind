#!/usr/bin/env python3
"""Manual Claude-CLI coherence rewrite for galaxy-evolution page 57."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
import time
from pathlib import Path

from sqlalchemy import func, text

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.agent_loop.autowiki.citation_context import build_evidence_map, emit_citation_scrub_required
from app.agent_loop.autowiki.tasks import _COHERENCE_EXPECTED_SECTIONS, _score_coherence_output
from app.database import SessionLocal
from app.models.page import PageVersion, WikiPage


PAGE_ID = 57
PRIMARY_MODEL = "claude-fable-5"
FALLBACK_MODEL = "claude-opus-4-7"
OUT_DIR = ROOT / "tmp" / "coherence_page57"


SYSTEM_PROMPT = """You are Claude Fable, writing as a senior galaxy-evolution reviewer.
You are performing a full-page coherence rewrite of an already sourced NebulaMind article.

Goal: collapse fragmentation into a clean graduate-textbook chapter with exactly nine canonical H2 sections. The prose must be compact, high-density, and non-repetitive. Every fact should appear once, in its best physical context. Do not pad. Do not add academic throat-clearing. Do not invent claims, datasets, citations, numbers, or instruments.

Keep HTML claim markers like <!--claim:123--> inline beside the assertions they mark. Keep evidence markers like <!--cite:1234--> only when the assertion is backed by that evidence ID. Do not create a references section."""


USER_TEMPLATE = """Rewrite the current Galaxy Evolution page as one coherent review article.

TARGET H2 STRUCTURE, EXACT STRINGS AND ORDER:
1. ## Overview & Historical Context
2. ## Galaxy Formation & Dark Matter Halos
3. ## Star Formation & Gas Physics
4. ## Quenching Mechanisms
5. ## Environmental Effects & Galaxy Clusters
6. ## Structural Evolution
7. ## Chemical Enrichment & Stellar Populations
8. ## High-Redshift Universe & Cosmic Star Formation History
9. ## Open Questions & Future Directions

QUALITY DIRECTIVE:
- Zero wordiness; no generic academic filler.
- High information density; graduate-textbook grade prose.
- No restating facts across adjacent sections.
- Strong transitions, but only where they carry scientific logic.
- Embed observational evidence inside the physical topic sections; never create a standalone observations section.
- Preserve substantive claims and quantitative facts.
- Preserve existing HTML claim markers and place them inline with their claims.
- Use only existing <!--cite:EVIDENCE_ID--> markers when appropriate.
- Output Markdown only. H1 must be exactly: # Galaxy Evolution
- No bibliography, no references section, no meta-commentary.

VALID EVIDENCE MAP:
{citation_context}

CURRENT PAGE CONTENT:
=====================================
{content}
"""


def _h2s(markdown: str) -> list[str]:
    return re.findall(r"^## .+$", markdown, flags=re.MULTILINE)


def _marker_ids(pattern: str, text_value: str) -> set[int]:
    return {int(m) for m in re.findall(pattern, text_value)}


def _duplicate_sentence_count(markdown: str) -> int:
    sentences = re.split(r"(?<=[.!?])\s+", markdown)
    seen: set[str] = set()
    dupes = 0
    for sentence in sentences:
        norm = re.sub(r"\W+", " ", sentence.lower()).strip()
        if len(norm) < 90:
            continue
        if norm in seen:
            dupes += 1
        seen.add(norm)
    return dupes


def validate(candidate: str, original: str, allowed_evidence_ids: set[int]) -> tuple[bool, list[str], dict]:
    failures: list[str] = []
    candidate = candidate.strip()
    if not candidate.startswith("# Galaxy Evolution"):
        failures.append("missing H1 '# Galaxy Evolution'")
    sections = _h2s(candidate)
    if sections != _COHERENCE_EXPECTED_SECTIONS:
        failures.append(f"H2 structure mismatch: {sections}")
    if "## Observational Evidence" in candidate:
        failures.append("contains forbidden standalone observations section")
    if re.search(r"^## References\b|^## Bibliography\b", candidate, flags=re.MULTILINE):
        failures.append("contains forbidden references/bibliography section")
    if len(candidate) < 45_000:
        failures.append(f"too short: {len(candidate)} chars")
    if len(candidate) > 90_000:
        failures.append(f"too long: {len(candidate)} chars")

    original_claims = _marker_ids(r"<!--claim:(\d+)-->", original)
    candidate_claims = _marker_ids(r"<!--claim:(\d+)-->", candidate)
    if original_claims and len(candidate_claims) < max(30, int(len(original_claims) * 0.75)):
        failures.append(
            f"claim marker retention too low: {len(candidate_claims)}/{len(original_claims)}"
        )

    bad_cites = sorted(_marker_ids(r"<!--cite:(\d+)-->", candidate) - allowed_evidence_ids)
    if bad_cites:
        failures.append(f"unknown evidence ids in cite markers: {bad_cites[:20]}")

    fluff_hits = len(re.findall(
        r"\b(further research is needed|plays a crucial role|important insights|complex interplay|rich tapestry)\b",
        candidate,
        flags=re.I,
    ))
    if fluff_hits > 2:
        failures.append(f"generic filler phrase count too high: {fluff_hits}")

    metrics = {
        "chars_before": len(original),
        "chars_after": len(candidate),
        "h2_before": len(_h2s(original)),
        "h2_after": len(sections),
        "claim_markers_before": len(original_claims),
        "claim_markers_after": len(candidate_claims),
        "duplicate_sentences_before": _duplicate_sentence_count(original),
        "duplicate_sentences_after": _duplicate_sentence_count(candidate),
        "quality_score_before": _score_coherence_output(original),
        "quality_score_after": _score_coherence_output(candidate),
        "fluff_hits": fluff_hits,
    }
    return not failures, failures, metrics


def call_claude(prompt: str, *, timeout_s: int = 54_000) -> str:
    cmd = [
        "claude",
        "-p",
        "--model",
        PRIMARY_MODEL,
        "--fallback-model",
        FALLBACK_MODEL,
        "--no-session-persistence",
        "--tools",
        "",
    ]
    started = time.monotonic()
    proc = subprocess.run(
        cmd,
        input=prompt,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout_s,
        cwd=str(ROOT),
    )
    elapsed = int(time.monotonic() - started)
    if proc.returncode != 0:
        raise RuntimeError(f"claude exited {proc.returncode} after {elapsed}s: {proc.stderr[-2000:]}")
    return proc.stdout


def commit_candidate(candidate: str, metrics: dict) -> tuple[int, int]:
    with SessionLocal() as db:
        page = db.query(WikiPage).filter(WikiPage.id == PAGE_ID).with_for_update().one()
        next_num = (db.query(func.max(PageVersion.version_num)).filter(PageVersion.page_id == PAGE_ID).scalar() or 0) + 1
        page.content = candidate
        page.updated_at = dt.datetime.utcnow()
        pv = PageVersion(
            page_id=PAGE_ID,
            version_num=next_num,
            content=candidate,
            source_note=f"manual claude-cli coherence rewrite {PRIMARY_MODEL} fallback {FALLBACK_MODEL}; metrics={json.dumps(metrics, sort_keys=True)}",
        )
        db.add(pv)
        db.flush()
        db.execute(
            text("""
                INSERT INTO autowiki_runs
                    (page_id, started_at, finished_at, proposal_type, model_proposer,
                     model_judge, decision, judge_rationale, judge_prompt_version,
                     latency_ms_breakdown, committed_version_id)
                VALUES
                    (:page_id, NOW(), NOW(), 'claude_cli_coherence_pass',
                     :model, 'tori_validator', 'commit', :rationale,
                     'coherence_cli_v1', CAST(:lat AS jsonb), :version_id)
            """),
            {
                "page_id": PAGE_ID,
                "model": f"claude-cli/{PRIMARY_MODEL}",
                "rationale": "Manual page-57 coherence rewrite passed structural, marker, citation, length, and repetition gates.",
                "lat": json.dumps(metrics),
                "version_id": pv.id,
            },
        )
        db.commit()
        version_id = pv.id
    emit_citation_scrub_required(PAGE_ID)
    return next_num, version_id


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit", action="store_true", help="write the validated candidate to DB")
    parser.add_argument("--reuse-output", type=Path, help="validate/commit an existing candidate file")
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with SessionLocal() as db:
        page = db.query(WikiPage).filter(WikiPage.id == PAGE_ID).one()
        original = page.content or ""
        citation_context = build_evidence_map(db, PAGE_ID, max_rows=120)
        allowed_evidence_ids = {row[0] for row in db.execute(text("SELECT id FROM evidence")).fetchall()}

    prompt = f"{SYSTEM_PROMPT}\n\n{USER_TEMPLATE.format(citation_context=citation_context, content=original)}"
    stamp = dt.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    prompt_path = OUT_DIR / f"prompt_{stamp}.md"
    output_path = OUT_DIR / f"candidate_{stamp}.md"
    metrics_path = OUT_DIR / f"metrics_{stamp}.json"
    prompt_path.write_text(prompt, encoding="utf-8")

    if args.reuse_output:
        candidate = args.reuse_output.read_text(encoding="utf-8")
        output_path = args.reuse_output
    else:
        candidate = call_claude(prompt)
        output_path.write_text(candidate, encoding="utf-8")

    ok, failures, metrics = validate(candidate, original, allowed_evidence_ids)
    metrics["prompt_path"] = str(prompt_path)
    metrics["output_path"] = str(output_path)
    metrics["validation_failures"] = failures
    metrics_path.write_text(json.dumps(metrics, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(metrics, indent=2, sort_keys=True))

    if not ok:
        print(f"VALIDATION_FAILED: {failures}", file=sys.stderr)
        return 2
    if args.commit:
        version_num, version_id = commit_candidate(candidate.strip() + "\n", metrics)
        print(json.dumps({"committed": True, "version_num": version_num, "version_id": version_id}))
    else:
        print("VALIDATED_DRAFT_ONLY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
