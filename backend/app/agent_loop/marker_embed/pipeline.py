import datetime
import json
import logging
import os
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

log = logging.getLogger(__name__)
TIMING_LOG = os.getenv("MARKER_TIMING_LOG")

COVERAGE_FLOOR = 0.0


def _timing_event(event: str, **payload) -> None:
    if not TIMING_LOG:
        return
    try:
        path = Path(TIMING_LOG)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({"stage": "pipeline", "event": event, **payload}, sort_keys=True) + "\n")
    except Exception:
        log.debug("pipeline timing log write failed", exc_info=True)

@dataclass
class RunStats:
    page_id: int
    source_version: Optional[int] = None
    total_claims: int = 0
    matched_claims: int = 0
    rejected_low_confidence: int = 0
    rejected_no_section: int = 0
    rejected_ambiguous_span: int = 0
    rejected_validation: int = 0
    confidences: list[float] = field(default_factory=list)
    judge_agreements: list[bool] = field(default_factory=list)
    status: str = "pending"
    notes: str = ""
    topical_anchor_count: int = 0
    tier_breakdown: dict = field(default_factory=lambda: {"verbatim": 0, "sentence": 0, "topic": 0})
    asserted_count: int = 0

    @property
    def coverage_pct(self) -> float:
        if self.total_claims == 0: return 0.0
        return self.matched_claims / self.total_claims

    @property
    def mean_confidence(self) -> float:
        return sum(self.confidences) / len(self.confidences) if self.confidences else 0.0

    @property
    def judge_agreement_pct(self) -> float:
        if not self.judge_agreements: return 0.0
        return sum(1 for x in self.judge_agreements if x) / len(self.judge_agreements)


def run_pipeline(
    page_id: int,
    content: str,
    claims: list[dict],
    source_version: Optional[int] = None,
    dry_run: bool = False,
    enable_topical_anchors: bool = False,
    section_key: Optional[str] = None,
    preserve_existing_section_markers: bool = False,
) -> tuple[Optional[str], RunStats]:
    import re

    from .section_resolver import parse_sections, resolve_section
    from .sentence_splitter import split_sentences
    from .aligner import align_claim_multipass
    from .judge import get_fallback_stats, passes_judge, reset_fallback_stats
    from .injector import InjectionCandidate, inject_markers, strip_markers
    from .embed_index import _cosine, _embed

    stats = RunStats(page_id=page_id, source_version=source_version)
    stats.total_claims = len(claims)
    reset_fallback_stats()
    chunk_started = time.perf_counter()
    _timing_event(
        "chunk_start",
        page_id=page_id,
        source_version=source_version,
        claim_count=len(claims),
        dry_run=dry_run,
        section_key=section_key,
        preserve_existing_section_markers=preserve_existing_section_markers,
    )

    if section_key:
        sections = parse_sections(content)
        target_section_block = None
        for s in sections:
            s_key = re.sub(r'_+', '_', re.sub(r'[^a-z0-9\s]', '', s.title.replace('##', '').lower()).replace(' ', '_')).strip('_')
            if s_key == section_key:
                target_section_block = s.body
                break
                
        if target_section_block is None:
            stats.status = "rolled_back"
            stats.notes = f"Section {section_key} not found"
            return None, stats
            
        sentence_source = strip_markers(target_section_block)
        clean_section = target_section_block if preserve_existing_section_markers else sentence_source
        all_sentences_with_sections = [(sent, section_key) for sent in split_sentences(sentence_source)]
        clean_content = content.replace(target_section_block, clean_section)
    else:
        clean_content = strip_markers(content)
        sections = parse_sections(clean_content)
        all_sentences_with_sections = []
        for s in sections:
            for sent in split_sentences(s.body):
                all_sentences_with_sections.append((sent, s.title))

    candidates_for_injection: list[InjectionCandidate] = []

    for claim in claims:
        claim_started = time.perf_counter()
        claim_id = claim["id"]
        claim_text = claim["text"]
        trust_level = claim.get("trust_level", "unknown")
        claim_section = claim.get("section", "")

        section_block = None
        # In Phase 3, claim_section is actually the owner_section_key.
        # We need to find the matching section block.
        for s in sections:
            sec_key = re.sub(r'_+', '_', re.sub(r'[^a-z0-9\s]', '', s.title.replace('##', '').lower()).replace(' ', '_')).strip('_')
            if sec_key == claim_section:
                section_block = s
                break
                
        if section_block is None:
            log.info("pipeline: claim_id=%d section=%r -> rejected_no_section", claim_id, claim_section)
            stats.rejected_no_section += 1
            _timing_event(
                "claim_done",
                claim_id=claim_id,
                section=claim_section,
                status="rejected_no_section",
                wall_ms=round((time.perf_counter() - claim_started) * 1000, 3),
            )
            continue

        sentences = split_sentences(strip_markers(section_block.body) if section_key else section_block.body)
        if not sentences:
            log.info("pipeline: claim_id=%d section=%r -> no sentences", claim_id, claim_section)
            stats.rejected_no_section += 1
            _timing_event(
                "claim_done",
                claim_id=claim_id,
                section=claim_section,
                status="no_sentences",
                wall_ms=round((time.perf_counter() - claim_started) * 1000, 3),
            )
            continue

        candidate_sentences = sentences[:60]

        # Tier 1 & 2
        alignment = align_claim_multipass(
            claim_id=claim_id,
            claim_text=claim_text,
            trust_level=trust_level,
            section_title=section_block.title,
            section_candidates=candidate_sentences,
            all_sentences_with_sections=all_sentences_with_sections
        )

        if alignment is None:
            # Tier 3 fallback
            if enable_topical_anchors:
                claim_vec = _embed(claim_text)
                if claim_vec:
                    best_score = 0.0
                    best_sec = ""
                    for sent, sec in all_sentences_with_sections:
                        vec = _embed(sent)
                        if vec:
                            sc = _cosine(claim_vec, vec)
                            if sc > best_score:
                                best_score = sc
                                best_sec = sec
                    if best_score >= 0.65:
                        candidates_for_injection.append(
                            InjectionCandidate(
                                claim_id=claim_id,
                                chosen_sentence="",
                                span="",
                                confidence=best_score,
                                judge_agreement=1.0,
                                match_type="topic",
                                chosen_section=best_sec
                            )
                        )
                        stats.tier_breakdown["topic"] += 1
                        _timing_event(
                            "claim_done",
                            claim_id=claim_id,
                            section=claim_section,
                            status="topic_anchor",
                            wall_ms=round((time.perf_counter() - claim_started) * 1000, 3),
                            score=best_score,
                        )
                        continue
            
            log.info("pipeline: claim_id=%d -> aligner rejected", claim_id)
            stats.rejected_low_confidence += 1
            _timing_event(
                "claim_done",
                claim_id=claim_id,
                section=claim_section,
                status="aligner_rejected",
                wall_ms=round((time.perf_counter() - claim_started) * 1000, 3),
            )
            continue

        span = alignment["span"]
        confidence = alignment["confidence"]
        stats.confidences.append(confidence)

        mtype = alignment.get("match_type", "verbatim")

        # Skip judge for Tier 1 verbatim matches
        if mtype == "verbatim":
            passed = True
            agreement_score = 1.0
            stats.judge_agreements.append(passed)
        else:
            passed, agreement_score = passes_judge(claim_text, trust_level, span)
            stats.judge_agreements.append(passed)
            if not passed:
                log.info("pipeline: claim_id=%d -> judge veto (agreement=%.2f)", claim_id, agreement_score)
                stats.rejected_validation += 1
                _timing_event(
                    "claim_done",
                    claim_id=claim_id,
                    section=claim_section,
                    status="judge_veto",
                    wall_ms=round((time.perf_counter() - claim_started) * 1000, 3),
                    agreement_score=agreement_score,
                    match_type=mtype,
                )
                continue
        candidates_for_injection.append(
            InjectionCandidate(
                claim_id=claim_id,
                chosen_sentence=alignment["chosen_sentence"],
                span=span,
                confidence=confidence,
                judge_agreement=agreement_score,
                match_type=mtype,
                chosen_section=alignment.get("chosen_section", "")
            )
        )
        stats.tier_breakdown[mtype] += 1
        stats.asserted_count += 1
        stats.matched_claims += 1
        _timing_event(
            "claim_done",
            claim_id=claim_id,
            section=claim_section,
            status="matched",
            wall_ms=round((time.perf_counter() - claim_started) * 1000, 3),
            confidence=confidence,
            agreement_score=agreement_score,
            match_type=mtype,
        )

    if stats.coverage_pct < COVERAGE_FLOOR:
        stats.status = "rolled_back"
        stats.notes = f"coverage_pct={stats.coverage_pct:.2f} < floor={COVERAGE_FLOOR}"
        return None, stats

    if dry_run or not candidates_for_injection:
        stats.status = "dry_run" if dry_run else "no_candidates"
        stats.tier_breakdown["judge_fallback"] = get_fallback_stats()
        _timing_event(
            "chunk_done",
            page_id=page_id,
            status=stats.status,
            total_claims=stats.total_claims,
            matched_claims=stats.matched_claims,
            wall_ms=round((time.perf_counter() - chunk_started) * 1000, 3),
        )
        return None, stats

    result = inject_markers(clean_content, candidates_for_injection)
    stats.rejected_ambiguous_span += result.skipped_ambiguous
    stats.rejected_validation += result.skipped_unsafe
    stats.topical_anchor_count = result.topical_anchor_count

    if result.validation_errors:
        stats.status = "rolled_back"
        stats.notes = "; ".join(result.validation_errors)
        stats.tier_breakdown["judge_fallback"] = get_fallback_stats()
        log.error("pipeline: page_id=%d validation errors: %s", page_id, stats.notes)
        _timing_event(
            "chunk_done",
            page_id=page_id,
            status=stats.status,
            total_claims=stats.total_claims,
            matched_claims=stats.matched_claims,
            wall_ms=round((time.perf_counter() - chunk_started) * 1000, 3),
            notes=stats.notes,
        )
        return None, stats

    log.info(f"pipeline: page_id={page_id} committed {stats.asserted_count}/{stats.total_claims} assertions")
    stats.tier_breakdown["judge_fallback"] = get_fallback_stats()
    stats.status = "committed"
    _timing_event(
        "chunk_done",
        page_id=page_id,
        status=stats.status,
        total_claims=stats.total_claims,
        matched_claims=stats.matched_claims,
        wall_ms=round((time.perf_counter() - chunk_started) * 1000, 3),
    )
    return result.content, stats
