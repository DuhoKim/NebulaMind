import re
from dataclasses import dataclass, field
from typing import Optional

_OPEN_RE = re.compile(r"<!--claim:([\d,\s]+)-->")
_CLOSE_RE = re.compile(r"<!--/claim:([\d,\s]+)-->")
_MARKER_STRIP_RE = re.compile(r"<!--/?claim:[\d,\s]+-->")
_TOPIC_STRIP_RE = re.compile(r"<!--topic:\d+-->")
_MIN_AMBIGUOUS_DIRECT_SPAN_CHARS = 24

def _compute_forbidden_ranges(content: str) -> list[tuple[int, int]]:
    forbidden: list[tuple[int, int]] = []
    for m in re.finditer(r"```.*?```", content, re.DOTALL): forbidden.append((m.start(), m.end()))
    for m in re.finditer(r"`[^`\n]+`", content): forbidden.append((m.start(), m.end()))
    for m in re.finditer(r"^#{1,3} .+$", content, re.MULTILINE): forbidden.append((m.start(), m.end()))
    for m in re.finditer(r"\[([^\]]+)\]\([^\)]+\)", content): forbidden.append((m.start(), m.start() + len(m.group(0))))
    for pattern in [r"\*\*[^*\n]+\*\*", r"__[^_\n]+__"]:
        for m in re.finditer(pattern, content): forbidden.append((m.start(), m.end()))
    for m in re.finditer(r"\$[^$\n]+\$", content): forbidden.append((m.start(), m.end()))
    for m in re.finditer(r"\$\$.*?\$\$", content, re.DOTALL): forbidden.append((m.start(), m.end()))
    for m in re.finditer(r"^[ \t]*(?:[-*+]|\d+\.)\s", content, re.MULTILINE): forbidden.append((m.start(), m.end()))
    for m in _MARKER_STRIP_RE.finditer(content): forbidden.append((m.start(), m.end()))
    return forbidden

def _in_forbidden(start: int, end: int, forbidden: list[tuple[int, int]]) -> bool:
    for fs, fe in forbidden:
        if start < fe and end > fs: return True
    return False

@dataclass
class InjectionCandidate:
    claim_id: int
    chosen_sentence: str
    span: str
    confidence: float
    judge_agreement: float
    match_type: str = "verbatim"
    chosen_section: str = ""

@dataclass
class InjectionResult:
    content: str
    injected_count: int
    skipped_ambiguous: int
    skipped_unsafe: int
    validation_errors: list[str]
    topical_anchor_count: int = 0

def strip_markers(content: str) -> str:
    content = _MARKER_STRIP_RE.sub("", content)
    content = _TOPIC_STRIP_RE.sub("", content)
    return content


def _expand_marker_groups(groups: list[str]) -> list[str]:
    out: list[str] = []
    for group in groups:
        for token in group.split(","):
            token = token.strip()
            if token:
                out.append(token)
    return out


def _positions(content: str, value: str) -> list[int]:
    if not value:
        return []
    return [m.start() for m in re.finditer(re.escape(value), content)]


def _loose_matches(content: str, value: str) -> list[tuple[int, int, str]]:
    """Find exact or whitespace-tolerant matches, returning actual substrings."""
    if not value or not value.strip():
        return []
    exact = [(m.start(), m.end(), m.group(0)) for m in re.finditer(re.escape(value), content)]
    if exact:
        return exact
    tokens = re.split(r"\s+", value.strip())
    if not tokens:
        return []
    pattern = r"\s+".join(re.escape(token) for token in tokens)
    return [(m.start(), m.end(), m.group(0)) for m in re.finditer(pattern, content)]


def _resolve_span(content: str, span: str, chosen_sentence: str) -> Optional[int]:
    """Return an unambiguous start index for a direct span, if possible."""
    occurrences = _positions(content, span)
    if len(occurrences) == 1:
        return occurrences[0]
    if len(occurrences) == 0:
        sent_pos = content.find(chosen_sentence)
        if sent_pos >= 0:
            sub = content[sent_pos: sent_pos + len(chosen_sentence)]
            sub_idx = sub.find(span)
            if sub_idx >= 0:
                return sent_pos + sub_idx
        return None
    # len(occurrences) > 1 — try to pin via the chosen_sentence position
    sent_pos = content.find(chosen_sentence)
    if sent_pos >= 0:
        span_in_sent = content.find(span, sent_pos)
        if 0 <= span_in_sent < sent_pos + len(chosen_sentence):
            return span_in_sent
    return None


def _group_span_choices(
    content: str,
    sentence: str,
    group: list[InjectionCandidate],
) -> list[tuple[str, int, bool]]:
    """Return candidate wrapper spans as (span, position, used_sentence_fallback).

    Multi-claim groups prefer the whole chosen sentence so every co-located
    claim visibly anchors to the same assertion. Single-claim ambiguous spans
    fall back to the whole sentence instead of being dropped.
    """
    choices: list[tuple[str, int, bool]] = []
    seen: set[tuple[int, str]] = set()

    def add(span: str, pos: Optional[int], fallback: bool) -> None:
        if pos is None or not span:
            return
        key = (pos, span)
        if key not in seen:
            seen.add(key)
            choices.append((span, pos, fallback))

    sentence_matches = _loose_matches(content, sentence)
    sentence_pos = sentence_matches[0][0] if len(sentence_matches) == 1 else None
    sentence_span = sentence_matches[0][2] if len(sentence_matches) == 1 else sentence

    # Biggest unlock: all claims on the same sentence can share one full-sentence
    # span instead of collapsing to a single highest-confidence claim.
    if len(group) > 1:
        add(sentence_span, sentence_pos, True)

    ranked = sorted(
        group,
        key=lambda c: (
            len(_loose_matches(content, c.span)) == 1,
            len((c.span or "").strip()),
            c.confidence,
        ),
        reverse=True,
    )

    for cand in ranked:
        span = (cand.span or "").strip()
        span_matches = _loose_matches(content, span)
        if len(span_matches) == 1:
            add(span_matches[0][2], span_matches[0][0], False)
            continue

        # Ambiguous or missing direct spans: prefer the full sentence when it is
        # unique, especially for short generic spans such as "AGN feedback".
        if len(span) < _MIN_AMBIGUOUS_DIRECT_SPAN_CHARS or len(span_matches) != 1:
            add(sentence_span, sentence_pos, True)
            continue

        # Last resort for repeated long spans: pin within the chosen sentence.
        add(span, _resolve_span(content, span, cand.chosen_sentence), False)

    if not choices:
        add(sentence_span, sentence_pos, True)

    return choices


def inject_markers(content: str, candidates: list[InjectionCandidate]) -> InjectionResult:
    existing_claim_ids = set(_expand_marker_groups(_OPEN_RE.findall(content)))
    existing_candidate_ids = {
        cand.claim_id for cand in candidates if str(cand.claim_id) in existing_claim_ids
    }

    # Group non-topic candidates by chosen_sentence so that multiple co-located
    # claims can share one wrap (multi-claim stacking — recovers drops that the
    # old highest-confidence dedup silently discarded).
    sentence_groups: dict[str, list[InjectionCandidate]] = {}
    topical_cands: list[InjectionCandidate] = []
    for cand in candidates:
        if cand.claim_id in existing_candidate_ids:
            continue
        if cand.match_type == "topic":
            topical_cands.append(cand)
            continue
        sentence_groups.setdefault(cand.chosen_sentence, []).append(cand)

    with open("/tmp/injector_debug.log", "w") as f:
        f.write(f"1. candidates_in (after judge gate): {len(candidates)}\n")
        f.write(f"   already_visible_candidate_ids: {len(existing_candidate_ids)}\n")
        nontopic = len(candidates) - len(topical_cands)
        f.write(f"   non-topic: {nontopic}, topic: {len(topical_cands)}\n")
        f.write(f"2. sentence_groups: {len(sentence_groups)}\n")
        top_groups = sorted(sentence_groups.items(), key=lambda x: len(x[1]), reverse=True)[:5]
        f.write("Top 5 sentences absorbing claims:\n")
        for sent, cands in top_groups:
            f.write(f"--- ({len(cands)}) {sent[:140]}\n")
            for c in cands:
                f.write(f"    claim_id={c.claim_id} conf={c.confidence} match_type={c.match_type}\n")

    forbidden = _compute_forbidden_ranges(content)

    @dataclass
    class PlacedInjection:
        claim_ids: list[int]
        span: str
        content_pos: int
        is_topic: bool = False
        fallback_used: bool = False  # span->sentence fallback

    placed: list[PlacedInjection] = []
    skipped_ambiguous = 0
    skipped_unsafe = 0
    sentence_fallback_count = 0

    for sent, group in sentence_groups.items():
        choices = _group_span_choices(content, sent, group)
        if not choices:
            skipped_ambiguous += len(group)
            continue

        chosen_span: Optional[str] = None
        chosen_pos: Optional[int] = None
        used_fallback = False
        for span, pos, fallback in choices:
            if not _in_forbidden(pos, pos + len(span), forbidden):
                chosen_span = span
                chosen_pos = pos
                used_fallback = fallback
                break

        if chosen_span is None or chosen_pos is None:
            skipped_unsafe += len(group)
            continue
        if used_fallback:
            sentence_fallback_count += 1

        claim_ids = sorted({c.claim_id for c in group})
        placed.append(PlacedInjection(
            claim_ids=claim_ids,
            span=chosen_span,
            content_pos=chosen_pos,
            fallback_used=used_fallback,
        ))

    with open("/tmp/injector_debug.log", "a") as f:
        f.write(f"\n3. after_resolution: groups_placed={len(placed)} skipped_ambiguous_claims={skipped_ambiguous}\n")
        f.write(f"   sentence_fallback_used: {sentence_fallback_count} group(s)\n")
        f.write(f"4. after_forbidden_check (dropped {skipped_unsafe} claims): groups_placed={len(placed)}\n")
        total_ids_placed = sum(len(p.claim_ids) for p in placed)
        f.write(f"5. final_injected_claim_ids: {total_ids_placed} across {len(placed)} wrap(s)\n")

    # Topical anchors — emit at section head, untouched by stacking change.
    topic_claims_by_section: dict[str, set[int]] = {}
    for cand in topical_cands:
        topic_claims_by_section.setdefault(cand.chosen_section, set()).add(cand.claim_id)

    for sec_title, cids in topic_claims_by_section.items():
        m = re.search(r"^(#{1,3})\s+" + re.escape(sec_title) + r"\s*$", content, re.MULTILINE)
        if m:
            insert_pos = m.end() + 1
            for cid in sorted(cids):
                placed.append(PlacedInjection(claim_ids=[cid], span="", content_pos=insert_pos, is_topic=True))

    # Insert from the end so positions stay valid.
    placed.sort(key=lambda x: x.content_pos, reverse=True)

    result = content
    topical_count = 0
    new_injected_count = 0
    placed_groups: list[list[int]] = []
    for inj in placed:
        pos = inj.content_pos
        if inj.is_topic:
            tag = f"<!--topic:{inj.claim_ids[0]}-->"
            result = result[:pos] + tag + result[pos:]
            topical_count += 1
            continue
        ids_str = ",".join(str(cid) for cid in inj.claim_ids)
        open_tag = f"<!--claim:{ids_str}-->"
        close_tag = f"<!--/claim:{ids_str}-->"
        span_len = len(inj.span)
        result = result[:pos] + open_tag + inj.span + close_tag + result[pos + span_len:]
        new_injected_count += len(inj.claim_ids)
        placed_groups.append(list(inj.claim_ids))

    validation_errors = _validate(result, new_injected_count, placed_groups=placed_groups)

    return InjectionResult(
        content=result,
        injected_count=len(existing_candidate_ids) + new_injected_count,
        skipped_ambiguous=skipped_ambiguous,
        skipped_unsafe=skipped_unsafe,
        validation_errors=validation_errors,
        topical_anchor_count=topical_count,
    )


def _validate(content: str, expected_injected: int, placed_groups: Optional[list[list[int]]] = None) -> list[str]:
    errors: list[str] = []
    all_open_groups = _OPEN_RE.findall(content)
    all_close_groups = _CLOSE_RE.findall(content)

    if placed_groups is not None:
        # Scope validation to ids this run placed; legacy/junk markers in untouched
        # sections must not cause rollback (preserves the prior section-scoped fix).
        scoped_ids: set[str] = {str(cid) for g in placed_groups for cid in g}
        opens = [t for t in _expand_marker_groups(all_open_groups) if t in scoped_ids]
        closes = [t for t in _expand_marker_groups(all_close_groups) if t in scoped_ids]
        scoped_group_strs = {",".join(str(cid) for cid in g) for g in placed_groups}
    else:
        opens = _expand_marker_groups(all_open_groups)
        closes = _expand_marker_groups(all_close_groups)
        scoped_group_strs = set(all_open_groups)

    if sorted(opens) != sorted(closes):
        errors.append(f"unmatched_markers: opens={len(opens)} closes={len(closes)}")
    if len(opens) != expected_injected:
        errors.append(f"marker_count_mismatch: found={len(opens)} expected={expected_injected}")
    if len(opens) != len(set(opens)):
        dupes = [x for x in opens if opens.count(x) > 1]
        errors.append(f"duplicate_marker_ids: {set(dupes)}")

    # Frontend smoke: each emitted group string must have a matched open/close pair
    # (with identical id-list) somewhere in the content. Verifies the regex the UI
    # uses (`<!--claim:(\d+(?:,\d+)*)-->...<!--/claim:\1-->`) will actually wrap.
    frontend_matched_ids = 0
    for gstr in scoped_group_strs:
        pattern = rf"<!--claim:{re.escape(gstr)}-->.*?<!--/claim:{re.escape(gstr)}-->"
        if re.search(pattern, content, re.DOTALL):
            frontend_matched_ids += len(gstr.split(","))
    if frontend_matched_ids != expected_injected:
        errors.append(f"frontend_smoke_fail: matched={frontend_matched_ids} expected={expected_injected}")

    return errors
