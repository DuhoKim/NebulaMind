#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import math
import py_compile
import shutil
import sys
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

from sqlalchemy import text

REPO = Path('/Users/duhokim/NebulaMind/NebulaMind')
BACKEND = REPO / 'backend'
PACKET_ID = 'galaxy_2929_hwao_trust_recompute_stage_packet_20260705T122901Z'
CREATED_AT = '2026-07-05T12:29:01Z'
PACKET = REPO / 'docs' / PACKET_ID
RUN = Path('/Users/duhokim/HermesOps/reports/2026-07-05') / PACKET_ID
TARGET_IDS = [2929, 2942, 2943, 2944, 2945, 2946, 2947]
MOVED_EVIDENCE_IDS = [28074,28087,28151,28155,30751,30752,30753,28091,28140,28141,28144,28148,29770,29776,29791,30754,30755,30756,30757,30758,30759,30760]
TRIGGER = 'g2929_hwao_trust_20260705T122901Z'
EXEC_PHRASE = 'APPROVE EXECUTE ' + PACKET_ID
ROLLBACK_PHRASE = 'APPROVE ROLLBACK ' + PACKET_ID
CONSUMED_DB_PACKET_ID = 'galaxy_2929_product_db_wiki_exact_diff_preflight_20260705T110725Z'
SCRATCH_PACKET_ID = 'galaxy_2929_trust_recompute_preflight_20260705T121124Z'

sys.path.insert(0, str(BACKEND))
from app.database import engine  # noqa: E402
from app.config import settings  # noqa: E402
from app.services.wikipedia_ingest import wikipedia_cross_check_score  # noqa: E402


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_path(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def jdump(obj, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True, default=str) + '\n')


def canonical(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), default=str)


def sha_obj(obj) -> str:
    return sha_bytes(canonical(obj).encode())


def write_jsonl(rows, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(''.join(json.dumps(row, sort_keys=True, default=str) + '\n' for row in rows))


class Obj:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def human_override_score(claim: dict) -> float:
    return {
        'consensus': 1.0,
        'accepted': 0.5,
        'debated': 0.0,
        'challenged': -0.5,
    }.get(claim.get('human_trust_override'), 0.0)


def apply_semantic_cap(claim: dict, candidate: str) -> tuple[str, str | None]:
    if claim.get('claim_type') == 'debate':
        return candidate, None
    cap = {
        'mixed_debated': 'debated',
        'model_bounded': 'reported',
    }.get(claim.get('debate_stance'))
    if cap and candidate in {'accepted', 'consensus'}:
        return cap, f"debate_stance:{claim.get('debate_stance')} capped {candidate}->{cap}"
    return candidate, None


def project_trust(claim: dict, evidence_rows: list[dict], vote_rows: list[dict], page: dict) -> dict:
    active = [e for e in evidence_rows if (e.get('status') or 'active') == 'active']
    if not active:
        E = 0.0
        n_supports = n_challenges = 0
    else:
        E_sup = sum(float(e.get('quality') or 0.0) for e in active if e.get('stance') == 'supports')
        E_chal = sum(float(e.get('quality') or 0.0) for e in active if e.get('stance') == 'challenges')
        E = math.tanh((E_sup - E_chal) / 1.5)
        n_supports = sum(1 for e in active if e.get('stance') == 'supports')
        n_challenges = sum(1 for e in active if e.get('stance') == 'challenges')
    active_ids = {int(e['id']) for e in active}
    relevant_votes = [v for v in vote_rows if int(v.get('evidence_id')) in active_ids]
    n_pos = sum(float(v.get('weight') or 0.0) for v in relevant_votes if int(v.get('value') or 0) > 0)
    n_neg = sum(float(v.get('weight') or 0.0) for v in relevant_votes if int(v.get('value') or 0) < 0)
    n_total = n_pos + n_neg
    if n_total > 0:
        raw = (n_pos - n_neg) / n_total
        confidence = 1.0 - math.exp(-n_total / settings.VOTE_CONFIDENCE_HALF_LIFE)
        V = raw * confidence
    else:
        V = 0.0
    V_before_wiki = V
    sup_years = [int(e['year']) for e in active if e.get('stance') == 'supports' and e.get('year')]
    if sup_years:
        years_since = datetime.utcnow().year - max(sup_years)
        T = -0.05 * max(0, years_since - settings.DECAY_FREE_YEARS) / 5.0
        T = max(T, -settings.DECAY_MAX_PENALTY)
    else:
        T = 0.0
    H = human_override_score(claim)
    wikipedia_bonus = 0.0
    # Current ORM has no wiki_summary field; this branch normally does not add a bonus.
    if settings.WIKIPEDIA_CROSSCHECK_ENABLED and page.get('wikipedia_title') and page.get('wiki_summary'):
        wikipedia_bonus = min(
            wikipedia_cross_check_score(Obj(**claim), Obj(**page)),
            settings.WIKIPEDIA_CROSSCHECK_MAX_BONUS,
        )
        if wikipedia_bonus > 0:
            V = min(1.0, V + wikipedia_bonus)
    TS = (
        settings.TRUST_W_EVIDENCE * E
        + settings.TRUST_W_VOTES * V
        + settings.TRUST_W_TEMPORAL * T
        + settings.TRUST_W_HUMAN * H
    )
    if claim.get('human_trust_override') and claim.get('human_override_locked'):
        level = claim.get('human_trust_override')
        note = None
    elif claim.get('claim_type') == 'debate':
        has_supports = any(e.get('stance') == 'supports' for e in active)
        has_challenges = any(e.get('stance') == 'challenges' for e in active)
        if has_supports and has_challenges:
            level = 'debated'
        elif has_supports:
            level = 'accepted'
        elif has_challenges:
            level = 'challenged'
        else:
            level = 'unverified'
        note = None
    elif not active and TS == 0:
        level = 'unverified'
        note = None
    elif TS >= settings.TRUST_CONSENSUS_MIN and n_supports >= settings.TRUST_CONSENSUS_MIN_SUPPORTS and n_challenges == 0:
        level = 'consensus'
        note = None
    elif TS >= settings.TRUST_ACCEPTED_MIN:
        level = 'accepted'
        note = None
    elif TS <= settings.TRUST_CHALLENGED_MAX:
        level = 'challenged'
        note = None
    elif n_supports >= 1 and n_challenges >= 1:
        level = 'debated'
        note = None
    else:
        level = 'unverified'
        note = None
    if not (claim.get('human_trust_override') and claim.get('human_override_locked')):
        level, note = apply_semantic_cap(claim, level)
    freshness_floor_applied = False
    if level == 'consensus' and sup_years and (datetime.utcnow().year - max(sup_years)) > settings.FRESHNESS_FLOOR_YEARS:
        cutoff = datetime.utcnow() - timedelta(days=settings.FRESHNESS_FLOOR_NEW_EVIDENCE_DAYS)
        recent = any(e.get('created_at') and e['created_at'] >= cutoff for e in active)
        if not recent:
            level = 'accepted'
            freshness_floor_applied = True
    return {
        'trust_level': level,
        'trust_score': TS,
        'e_component': E,
        'v_component': V,
        'v_component_before_wiki': V_before_wiki,
        'wikipedia_bonus': wikipedia_bonus,
        't_component': T,
        'h_component': H,
        'n_supports': n_supports,
        'n_challenges': n_challenges,
        'vote_positive_weight': n_pos,
        'vote_negative_weight': n_neg,
        'semantic_cap_note': note,
        'freshness_floor_applied': freshness_floor_applied,
    }


def main() -> int:
    for sub in ['artifacts', 'backups', 'diff', 'execution_results', 'lanes', 'reports', 'scripts', 'sql', 'validation']:
        (PACKET / sub).mkdir(parents=True, exist_ok=True)
    id_sql = ','.join(str(i) for i in TARGET_IDS)
    with engine.connect() as conn:
        trans = conn.begin()
        conn.execute(text('SET TRANSACTION READ ONLY'))
        claims = [dict(r) for r in conn.execute(text(f'''
            SELECT c.*, p.slug AS page_slug, p.title AS page_title
            FROM claims c JOIN wiki_pages p ON p.id=c.page_id
            WHERE c.id IN ({id_sql}) ORDER BY c.id
        ''')).mappings().all()]
        page = dict(conn.execute(text("""
            SELECT id,title,slug,content,summary,wikipedia_title,wiki_summary_revision,wiki_summary_license,
                   wiki_summary_fetched_at,category,difficulty,updated_at,length(content) AS content_len,
                   md5(coalesce(content,'')) AS content_md5
            FROM wiki_pages WHERE slug='galaxy-evolution'
        """)).mappings().first())
        page['wiki_summary'] = None
        versions = [dict(r) for r in conn.execute(text("""
            SELECT id,page_id,version_num,content,source_note,created_at,length(content) AS content_len,
                   md5(coalesce(content,'')) AS content_md5
            FROM page_versions WHERE page_id=:pid ORDER BY version_num DESC,id DESC LIMIT 8
        """), {'pid': page['id']}).mappings().all()]
        evidence = [dict(r) for r in conn.execute(text(f'''
            SELECT id,claim_id,stance,status,evidence_status,quality,year,created_at,arxiv_id,doi,url,title,authors,
                   source_channel,verified_at,stance_jury_run_at,consensus_vote,consensus_settled_at,peer_reviewed,
                   relevance,entailment,rigor,confidence
            FROM evidence WHERE claim_id IN ({id_sql}) ORDER BY claim_id,id
        ''')).mappings().all()]
        ev_ids = [int(e['id']) for e in evidence]
        ev_sql = ','.join(str(i) for i in ev_ids) if ev_ids else 'NULL'
        votes = [dict(r) for r in conn.execute(text(f'''
            SELECT id,evidence_id,value,agent_id,created_at,weight,voter_type,prompt_revision_id,relevance,entailment,
                   rigor,confidence,scheduled_via
            FROM evidence_votes WHERE evidence_id IN ({ev_sql}) ORDER BY evidence_id,id
        ''')).mappings().all()]
        jury = [dict(r) for r in conn.execute(text(f'''
            SELECT id,evidence_id,prompt_revision_id,relevance,entailment,rigor,confidence,var_entailment,quality_v2,
                   stance,policy_id,created_at
            FROM jury_scorecards WHERE evidence_id IN ({ev_sql}) ORDER BY evidence_id,id
        ''')).mappings().all()]
        audit_tail = [dict(r) for r in conn.execute(text(f'''
            SELECT id,claim_id,old_level,new_level,old_score,new_score,e_component,v_component,t_component,h_component,
                   trigger,notes,created_at
            FROM trust_audit_log WHERE claim_id IN ({id_sql}) ORDER BY id DESC LIMIT 80
        ''')).mappings().all()]
        audit_max = {int(r['claim_id']): int(r['max_id'] or 0) for r in conn.execute(text(f'''
            SELECT claim_id,max(id) AS max_id FROM trust_audit_log WHERE claim_id IN ({id_sql}) GROUP BY claim_id
        ''')).mappings().all()}
        trigger_count = int(conn.execute(text('SELECT count(*) FROM trust_audit_log WHERE trigger=:trigger'), {'trigger': TRIGGER}).scalar_one())
        moved_now = int(conn.execute(text('''
            SELECT count(*) FROM evidence
            WHERE id=ANY(:ids) AND claim_id<>2929 AND stance='supports' AND status='active'
        '''), {'ids': MOVED_EVIDENCE_IDS}).scalar_one())
        parent_none = int(conn.execute(text("""
            SELECT count(*) FROM evidence WHERE claim_id=2929 AND status='active' AND stance='none'
        """)).scalar_one())
        page_citation_links = int(conn.execute(text('SELECT count(*) FROM page_citation_links WHERE page_id=:pid'), {'pid': page['id']}).scalar_one())
        fact_sources = int(conn.execute(text('SELECT count(*) FROM fact_sources WHERE page_id=:pid AND superseded_at IS NULL'), {'pid': page['id']}).scalar_one())
        trans.rollback()
    claims_by_id = {int(c['id']): c for c in claims}
    evidence_by_claim: dict[int, list[dict]] = defaultdict(list)
    for e in evidence:
        evidence_by_claim[int(e['claim_id'])].append(e)
    votes_by_evidence: dict[int, list[dict]] = defaultdict(list)
    for v in votes:
        votes_by_evidence[int(v['evidence_id'])].append(v)
    votes_by_claim: dict[int, list[dict]] = defaultdict(list)
    for e in evidence:
        votes_by_claim[int(e['claim_id'])].extend(votes_by_evidence[int(e['id'])])
    projections = []
    exact_updates = []
    audit_insert_templates = []
    for cid in TARGET_IDS:
        claim = claims_by_id[cid]
        proj = project_trust(claim, evidence_by_claim[cid], votes_by_claim[cid], page)
        before = {
            'trust_level': claim.get('trust_level'),
            'trust_score': float(claim.get('trust_score') or 0.0),
            'trust_score_updated_at': str(claim.get('trust_score_updated_at')) if claim.get('trust_score_updated_at') else None,
        }
        after = {
            'trust_level': proj['trust_level'],
            'trust_score': proj['trust_score'],
            'trust_score_updated_at': '<execution_time_utc>',
        }
        active = [e for e in evidence_by_claim[cid] if (e.get('status') or 'active') == 'active']
        projections.append({
            'claim_id': cid,
            'claim_text': claim.get('text'),
            'rewrite_status': claim.get('rewrite_status'),
            'debate_stance': claim.get('debate_stance'),
            'before': before,
            'projected_after': after,
            'components': proj,
            'active_evidence_count': len(active),
            'active_supports': proj['n_supports'],
            'active_challenges': proj['n_challenges'],
            'active_none': sum(1 for e in active if e.get('stance') == 'none'),
        })
        exact_updates.append({
            'table': 'claims',
            'operation': 'UPDATE_AFTER_EXPLICIT_APPROVAL_ONLY',
            'primary_key': cid,
            'changed_fields': ['trust_level', 'trust_score', 'trust_score_updated_at'],
            'before': before,
            'after': after,
            'projection_components': proj,
            'claim_text': claim.get('text'),
            'rewrite_status': claim.get('rewrite_status'),
            'debate_stance': claim.get('debate_stance'),
        })
        audit_insert_templates.append({
            'table': 'trust_audit_log',
            'operation': 'INSERT_AFTER_EXPLICIT_APPROVAL_ONLY',
            'claim_id': cid,
            'old_level': before['trust_level'],
            'new_level': after['trust_level'],
            'old_score': before['trust_score'],
            'new_score': after['trust_score'],
            'e_component': proj['e_component'],
            'v_component': proj['v_component'],
            't_component': proj['t_component'],
            'h_component': proj['h_component'],
            'trigger': TRIGGER,
            'notes': proj.get('semantic_cap_note'),
        })
    backup = {
        'packet_id': PACKET_ID,
        'created_at_utc': CREATED_AT,
        'target_claim_ids': TARGET_IDS,
        'moved_evidence_ids_from_executed_db_packet': MOVED_EVIDENCE_IDS,
        'claims': claims,
        'page': {k: v for k, v in page.items() if k != 'content'},
        'page_content_sha256': sha_bytes((page.get('content') or '').encode()),
        'latest_page_versions': [{k: v for k, v in row.items() if k != 'content'} | {'content_sha256': sha_bytes((row.get('content') or '').encode())} for row in versions],
        'evidence': evidence,
        'evidence_votes': votes,
        'jury_scorecards': jury,
        'trust_audit_tail': audit_tail,
        'audit_max_by_claim': audit_max,
        'trigger_existing_count': trigger_count,
        'moved_rows_current': moved_now,
        'parent_2929_active_none_rows': parent_none,
        'page_citation_links': page_citation_links,
        'active_fact_sources': fact_sources,
    }
    jdump(backup, PACKET / 'backups/current_state_backup.json')
    write_jsonl(claims, PACKET / 'backups/claims_backup.jsonl')
    write_jsonl(evidence, PACKET / 'backups/evidence_context_backup.jsonl')
    write_jsonl(votes, PACKET / 'backups/evidence_votes_context_backup.jsonl')
    write_jsonl(audit_tail, PACKET / 'backups/trust_audit_tail_backup.jsonl')
    jdump({'status': 'PROJECTED_NOT_EXECUTED', 'projections': projections}, PACKET / 'diff/trust_recompute_projection.json')
    jdump({'status': 'PROJECTED_NOT_EXECUTED', 'claim_updates': exact_updates, 'trust_audit_inserts': audit_insert_templates}, PACKET / 'diff/exact_diff.json')
    with (PACKET / 'diff/exact_diff_summary.csv').open('w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['claim_id', 'current_level', 'projected_level', 'current_score', 'projected_score', 'active_evidence', 'supports', 'challenges', 'none', 'rewrite_status', 'debate_stance', 'note'])
        for p in projections:
            writer.writerow([p['claim_id'], p['before']['trust_level'], p['projected_after']['trust_level'], p['before']['trust_score'], p['projected_after']['trust_score'], p['active_evidence_count'], p['active_supports'], p['active_challenges'], p['active_none'], p.get('rewrite_status') or '', p.get('debate_stance') or '', p['components'].get('semantic_cap_note') or ''])
    current_values = ',\n'.join(f"({int(c['id'])}, '{c['trust_level']}', {float(c.get('trust_score') or 0.0):.17g})" for c in claims)
    after_values = ',\n'.join(f"({row['primary_key']}, '{row['after']['trust_level']}', {float(row['after']['trust_score']):.17g})" for row in exact_updates)
    (PACKET / 'sql/pre_execute_readonly_verification.sql').write_text(f"""-- Read-only pre-execute verification for {PACKET_ID}
BEGIN TRANSACTION READ ONLY;
WITH expected(id, trust_level, trust_score) AS (VALUES
{current_values}
)
SELECT 'target_claim_before_state' AS check_name, count(*) AS actual, {len(TARGET_IDS)} AS expected
FROM expected x JOIN claims c ON c.id=x.id
WHERE c.trust_level=x.trust_level AND abs(coalesce(c.trust_score,0)-x.trust_score) < 1e-9;
SELECT 'packet_trigger_absent' AS check_name, count(*) AS actual, 0 AS expected
FROM trust_audit_log WHERE trigger='{TRIGGER}';
SELECT 'moved_rows_present' AS check_name, count(*) AS actual, 22 AS expected
FROM evidence WHERE id=ANY(ARRAY[{','.join(map(str, MOVED_EVIDENCE_IDS))}]) AND claim_id<>2929 AND stance='supports' AND status='active';
SELECT 'parent_2929_none_rows' AS check_name, count(*) AS actual, 14 AS expected
FROM evidence WHERE claim_id=2929 AND status='active' AND stance='none';
SELECT 'wiki_page_content_unchanged' AS check_name, md5(coalesce(content,'')) AS actual, '{page['content_md5']}' AS expected
FROM wiki_pages WHERE id={page['id']};
ROLLBACK;
""")
    (PACKET / 'sql/post_execute_readonly_verification.sql').write_text(f"""-- Read-only post-execute verification for {PACKET_ID}
BEGIN TRANSACTION READ ONLY;
WITH expected(id, trust_level, trust_score) AS (VALUES
{after_values}
)
SELECT 'target_claim_after_state' AS check_name, count(*) AS actual, {len(TARGET_IDS)} AS expected
FROM expected x JOIN claims c ON c.id=x.id
WHERE c.trust_level=x.trust_level AND abs(coalesce(c.trust_score,0)-x.trust_score) < 1e-9 AND c.trust_score_updated_at IS NOT NULL;
SELECT 'packet_trigger_audit_rows' AS check_name, count(*) AS actual, {len(TARGET_IDS)} AS expected
FROM trust_audit_log WHERE trigger='{TRIGGER}' AND claim_id IN ({id_sql});
SELECT 'wiki_page_content_unchanged' AS check_name, md5(coalesce(content,'')) AS actual, '{page['content_md5']}' AS expected
FROM wiki_pages WHERE id={page['id']};
ROLLBACK;
""")
    (PACKET / 'sql/rollback_verification.sql').write_text(f"""-- Read-only rollback verification for {PACKET_ID}
BEGIN TRANSACTION READ ONLY;
WITH expected(id, trust_level, trust_score) AS (VALUES
{current_values}
)
SELECT 'rollback_claim_state_restored' AS check_name, count(*) AS actual, {len(TARGET_IDS)} AS expected
FROM expected x JOIN claims c ON c.id=x.id
WHERE c.trust_level=x.trust_level AND abs(coalesce(c.trust_score,0)-x.trust_score) < 1e-9;
SELECT 'packet_trigger_audit_rows_removed' AS check_name, count(*) AS actual, 0 AS expected
FROM trust_audit_log WHERE trigger='{TRIGGER}' AND claim_id IN ({id_sql});
ROLLBACK;
""")
    execute_script = f'''#!/usr/bin/env python3
from __future__ import annotations
import datetime as dt, hashlib, json, math, sys
from pathlib import Path
from sqlalchemy import text
PACKET=Path({str(PACKET)!r})
REPO=Path({str(REPO)!r})
BACKEND=REPO/'backend'
TARGET_IDS={TARGET_IDS!r}
MOVED_EVIDENCE_IDS={MOVED_EVIDENCE_IDS!r}
sys.path.insert(0,str(BACKEND))
from app.models import import_all_models
import_all_models()
from app.database import SessionLocal
from app.services.trust_calculation import recalculate_trust_v2
def sha_path(p):
    h=hashlib.sha256(); h.update(Path(p).read_bytes()); return h.hexdigest()
def approx(a,b,eps=1e-9): return math.isclose(float(a), float(b), rel_tol=0, abs_tol=eps)
def main():
    phrase=sys.argv[1] if len(sys.argv)>1 else ''
    manifest=json.loads((PACKET/'artifacts/manifest.json').read_text())
    now_tag=dt.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
    result_path=PACKET/'execution_results'/f'trust_recompute_execution_{{now_tag}}.json'
    result={{'packet_id':manifest['packet_id'],'started_utc':dt.datetime.utcnow().isoformat(timespec='microseconds')+'Z','target_claim_ids':TARGET_IDS,'status':'STARTED'}}
    if phrase != manifest['execution_phrase']:
        print('Refusing to execute: approval phrase mismatch'); return 2
    if sha_path(__file__) != manifest['checksums']['execute_script_sha256']:
        print('Refusing to execute: execute script checksum mismatch'); return 3
    src=manifest['source_fingerprints']['trust_calculation_path']
    if sha_path(src) != manifest['source_fingerprints']['trust_calculation_sha256']:
        print('Refusing to execute: trust calculation source checksum changed'); return 4
    backup=json.loads((PACKET/'backups/current_state_backup.json').read_text())
    diff={{int(row['primary_key']): row for row in json.loads((PACKET/'diff/exact_diff.json').read_text())['claim_updates']}}
    db=SessionLocal()
    try:
        db.begin()
        current=[dict(r) for r in db.execute(text('SELECT id,trust_level,trust_score,trust_score_updated_at FROM claims WHERE id=ANY(:ids) ORDER BY id'), {{'ids':TARGET_IDS}}).mappings().all()]
        if len(current)!=len(TARGET_IDS): raise RuntimeError('target claim count mismatch')
        current_by={{int(r['id']): r for r in current}}
        for b in backup['claims']:
            cid=int(b['id']); got=current_by[cid]
            if got['trust_level'] != b['trust_level'] or not approx(got['trust_score'] or 0.0, b.get('trust_score') or 0.0):
                raise RuntimeError(f'before-state drift for claim {{cid}}')
        if db.execute(text('SELECT count(*) FROM trust_audit_log WHERE trigger=:trigger'), {{'trigger':manifest['trigger']}}).scalar_one() != 0:
            raise RuntimeError('packet trigger already exists')
        moved=db.execute(text("SELECT count(*) FROM evidence WHERE id=ANY(:ids) AND claim_id<>2929 AND stance='supports' AND status='active'"), {{'ids':MOVED_EVIDENCE_IDS}}).scalar_one()
        if moved != 22: raise RuntimeError(f'moved evidence drift: {{moved}}')
        parent_none=db.execute(text("SELECT count(*) FROM evidence WHERE claim_id=2929 AND status='active' AND stance='none'")).scalar_one()
        if parent_none != 14: raise RuntimeError(f'parent 2929 held evidence drift: {{parent_none}}')
        page_md5=db.execute(text("SELECT md5(coalesce(content,'')) FROM wiki_pages WHERE id=:pid"), {{'pid':manifest['scope']['wiki_page_id']}}).scalar_one()
        if page_md5 != manifest['preconditions']['wiki_page_content_md5']:
            raise RuntimeError('wiki page content drift; prose publish is separate')
        service_returns={{}}
        for cid in TARGET_IDS:
            level,score=recalculate_trust_v2(cid, db, trigger=manifest['trigger'])
            service_returns[str(cid)]={{'level':level,'score':score}}
        db.flush()
        after=[dict(r) for r in db.execute(text('SELECT id,trust_level,trust_score,trust_score_updated_at FROM claims WHERE id=ANY(:ids) ORDER BY id'), {{'ids':TARGET_IDS}}).mappings().all()]
        after_by={{int(r['id']): r for r in after}}
        for cid in TARGET_IDS:
            exp=diff[cid]['after']; got=after_by[cid]
            if got['trust_level'] != exp['trust_level'] or not approx(got['trust_score'], exp['trust_score']):
                raise RuntimeError(f'after-state mismatch for claim {{cid}}')
            if got['trust_score_updated_at'] is None: raise RuntimeError(f'missing timestamp for claim {{cid}}')
        audits=[dict(r) for r in db.execute(text('SELECT id,claim_id,old_level,new_level,old_score,new_score,e_component,v_component,t_component,h_component,trigger,notes,created_at FROM trust_audit_log WHERE trigger=:trigger AND claim_id=ANY(:ids) ORDER BY claim_id,id'), {{'trigger':manifest['trigger'],'ids':TARGET_IDS}}).mappings().all()]
        if len(audits) != len(TARGET_IDS): raise RuntimeError(f'expected {{len(TARGET_IDS)}} audit rows, got {{len(audits)}}')
        db.commit()
        result.update({{'status':'EXECUTED_AND_VERIFIED','ended_utc':dt.datetime.utcnow().isoformat(timespec='microseconds')+'Z','service_returns':service_returns,'after_claims':[{{k:(str(v) if 'time' in k and v is not None else v) for k,v in r.items()}} for r in after],'inserted_audit_rows':[{{k:(str(v) if k=='created_at' and v is not None else v) for k,v in r.items()}} for r in audits],'inserted_audit_ids':[int(r['id']) for r in audits],'rollback_phrase':manifest['rollback_phrase']}})
        result_path.write_text(json.dumps(result,indent=2,sort_keys=True,default=str)+'\\n')
        print(json.dumps({{'status':result['status'],'result_path':str(result_path),'rollback_phrase':manifest['rollback_phrase']}},indent=2))
        return 0
    except Exception as exc:
        db.rollback(); result.update({{'status':'FAILED_ROLLED_BACK','ended_utc':dt.datetime.utcnow().isoformat(timespec='microseconds')+'Z','error':str(exc)}}); result_path.write_text(json.dumps(result,indent=2,sort_keys=True,default=str)+'\\n'); print(json.dumps({{'status':result['status'],'error':str(exc),'result_path':str(result_path)}},indent=2)); return 1
    finally:
        db.close()
if __name__ == '__main__':
    raise SystemExit(main())
'''
    rollback_script = f'''#!/usr/bin/env python3
from __future__ import annotations
import datetime as dt, hashlib, json, math, sys
from pathlib import Path
from sqlalchemy import text
PACKET=Path({str(PACKET)!r})
REPO=Path({str(REPO)!r})
BACKEND=REPO/'backend'
TARGET_IDS={TARGET_IDS!r}
sys.path.insert(0,str(BACKEND))
from app.models import import_all_models
import_all_models()
from app.database import SessionLocal
def sha_path(p): h=hashlib.sha256(); h.update(Path(p).read_bytes()); return h.hexdigest()
def approx(a,b,eps=1e-9): return math.isclose(float(a), float(b), rel_tol=0, abs_tol=eps)
def latest_exec():
    rows=sorted((PACKET/'execution_results').glob('trust_recompute_execution_*.json'))
    if not rows: raise RuntimeError('no execution result file')
    return rows[-1]
def main():
    phrase=sys.argv[1] if len(sys.argv)>1 else ''
    exec_path=Path(sys.argv[2]) if len(sys.argv)>2 else latest_exec()
    manifest=json.loads((PACKET/'artifacts/manifest.json').read_text())
    result_path=PACKET/'execution_results'/f'trust_recompute_rollback_{{dt.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")}}.json'
    result={{'packet_id':manifest['packet_id'],'started_utc':dt.datetime.utcnow().isoformat(timespec='microseconds')+'Z','execution_result':str(exec_path)}}
    if phrase != manifest['rollback_phrase']:
        print('Refusing rollback: approval phrase mismatch'); return 2
    if sha_path(__file__) != manifest['checksums']['rollback_script_sha256']:
        print('Refusing rollback: rollback script checksum mismatch'); return 3
    exec_result=json.loads(exec_path.read_text())
    if exec_result.get('status') != 'EXECUTED_AND_VERIFIED':
        print('Refusing rollback: execution result not EXECUTED_AND_VERIFIED'); return 4
    audit_ids=[int(i) for i in exec_result.get('inserted_audit_ids', [])]
    if len(audit_ids) != len(TARGET_IDS):
        print('Refusing rollback: execution result does not list exactly target audit ids'); return 5
    backup={{int(r['id']): r for r in json.loads((PACKET/'backups/current_state_backup.json').read_text())['claims']}}
    diff={{int(r['primary_key']): r for r in json.loads((PACKET/'diff/exact_diff.json').read_text())['claim_updates']}}
    db=SessionLocal()
    try:
        db.begin()
        current={{int(r['id']): r for r in db.execute(text('SELECT id,trust_level,trust_score FROM claims WHERE id=ANY(:ids)'), {{'ids':TARGET_IDS}}).mappings().all()}}
        for cid in TARGET_IDS:
            exp=diff[cid]['after']; got=current[cid]
            if got['trust_level'] != exp['trust_level'] or not approx(got['trust_score'], exp['trust_score']):
                raise RuntimeError(f'claim {{cid}} not at packet after-state')
        audits=[dict(r) for r in db.execute(text('SELECT id,claim_id,trigger FROM trust_audit_log WHERE id=ANY(:ids) ORDER BY id'), {{'ids':audit_ids}}).mappings().all()]
        if len(audits) != len(audit_ids): raise RuntimeError('some audit rows missing')
        for row in audits:
            if row['trigger'] != manifest['trigger'] or int(row['claim_id']) not in TARGET_IDS: raise RuntimeError('audit guard mismatch')
        for cid,b in backup.items():
            db.execute(text('UPDATE claims SET trust_level=:trust_level, trust_score=:trust_score, trust_score_updated_at=:trust_score_updated_at WHERE id=:id'), {{'id':cid,'trust_level':b['trust_level'],'trust_score':b['trust_score'],'trust_score_updated_at':b['trust_score_updated_at']}})
        db.execute(text('DELETE FROM trust_audit_log WHERE id=ANY(:ids)'), {{'ids':audit_ids}})
        db.commit(); result.update({{'status':'ROLLBACK_EXECUTED_AND_VERIFIED','ended_utc':dt.datetime.utcnow().isoformat(timespec='microseconds')+'Z','deleted_audit_ids':audit_ids}}); result_path.write_text(json.dumps(result,indent=2,sort_keys=True,default=str)+'\\n'); print(json.dumps({{'status':result['status'],'result_path':str(result_path)}},indent=2)); return 0
    except Exception as exc:
        db.rollback(); result.update({{'status':'ROLLBACK_FAILED_ROLLED_BACK','ended_utc':dt.datetime.utcnow().isoformat(timespec='microseconds')+'Z','error':str(exc)}}); result_path.write_text(json.dumps(result,indent=2,sort_keys=True,default=str)+'\\n'); print(json.dumps({{'status':result['status'],'error':str(exc),'result_path':str(result_path)}},indent=2)); return 1
    finally:
        db.close()
if __name__ == '__main__':
    raise SystemExit(main())
'''
    (PACKET / 'scripts/execute_trust_recompute_packet.py').write_text(execute_script)
    (PACKET / 'scripts/rollback_trust_recompute_packet.py').write_text(rollback_script)
    validation_script = f'''#!/usr/bin/env python3
from __future__ import annotations
import json, hashlib, py_compile, sys
from pathlib import Path
PACKET=Path({str(PACKET)!r})
CONSUMED={CONSUMED_DB_PACKET_ID!r}
SCRATCH={SCRATCH_PACKET_ID!r}
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
manifest=json.loads((PACKET/'artifacts/manifest.json').read_text())
fail=[]
if manifest['packet_id'] != {PACKET_ID!r}: fail.append('packet_id mismatch')
if manifest['active_execution_phrase'] != 'NO ACTIVE EXECUTION PHRASE': fail.append('active phrase not no-active')
if CONSUMED in manifest['execution_phrase']: fail.append('consumed DB phrase reused')
if SCRATCH in manifest['execution_phrase']: fail.append('scratch phrase reused')
if manifest.get('status') != 'STAGED_ONLY_AWAITING_EXPLICIT_EXECUTION_APPROVAL': fail.append('bad status')
for rel,h in manifest['checksums']['files'].items():
    if sha(PACKET/rel) != h: fail.append(f'checksum mismatch {{rel}}')
for rel in ['scripts/execute_trust_recompute_packet.py','scripts/rollback_trust_recompute_packet.py']:
    try: py_compile.compile(str(PACKET/rel), doraise=True)
    except Exception as exc: fail.append(f'py_compile failed {{rel}}: {{exc!r}}')
text='\\n'.join((PACKET/rel).read_text(errors='ignore') for rel in ['APPROVAL_PACKET.md','reports/HWAO_STAGED_TRUST_RECOMPUTE_PACKET.md','artifacts/manifest.json'])
if ('APPROVE EXECUTE '+CONSUMED) in text: fail.append('consumed execution phrase text leaked')
out={{'status':'PASS' if not fail else 'FAIL','failed_checks':fail,'marker':'VALIDATE_HWAO_2929_TRUST_RECOMPUTE_STAGE_PACKET_20260705T122901Z','db_writes_executed':0,'trust_recompute_executions':0,'wiki_prose_publish_executions':0}}
(PACKET/'validation/packet_validation.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\\n')
print(json.dumps(out,indent=2,sort_keys=True))
sys.exit(0 if not fail else 1)
'''
    (PACKET / 'scripts/validate_packet.py').write_text(validation_script)
    lane_summary = {
        'hwao_decision': 'STAGE-ONLY trust recompute packet; defer prose; hold public phrase',
        'lana_report': 'BLOCKED on apply; trust is stale relative to remap by timestamp order; stage trust-recompute packet only if Hwao elects.',
        'goru_report': 'BLOCKED for prose/wiki publish; no prose delta supplied; page 57 remains v1710 hash b97223f91897e8f8541b9c26c744ebb7.',
        'kun_report': 'PASS phrase/scratch audit; scratch may not be promoted; public surfaces remain NO ACTIVE EXECUTION PHRASE.',
        'tori_boundary': 'Tori assembled only the Hwao-directed staged packet; no DB/trust/wiki/prose execution and no cockpit update.',
    }
    jdump(lane_summary, PACKET / 'lanes/hwao_lane_receipts_summary.json')
    go_rows = [
        {'gate': 'Hwao direction', 'status': 'PASS', 'detail': 'Hwao explicitly allowed staged packet assembly only.'},
        {'gate': 'DB write execution', 'status': 'NO-GO', 'detail': 'No execution approval; no trust recompute execution.'},
        {'gate': 'Prose/wiki publish', 'status': 'NO-GO', 'detail': 'Goru blocked publish until Hwao supplies prose delta after trust.'},
        {'gate': 'Scratch promotion', 'status': 'NO-GO', 'detail': 'Kun marked Tori-solo scratch non-authoritative.'},
        {'gate': 'Public active phrase', 'status': 'PASS', 'detail': 'Keep NO ACTIVE EXECUTION PHRASE.'},
    ]
    write_jsonl(go_rows, PACKET / 'artifacts/go_no_go_checklist.jsonl')
    source_path = BACKEND / 'app/services/trust_calculation.py'
    source_sha = sha_path(source_path)
    lines = []
    for p in projections:
        lines.append(f"| {p['claim_id']} | {p['before']['trust_level']} | {p['projected_after']['trust_level']} | {p['before']['trust_score']:.12f} | {p['projected_after']['trust_score']:.12f} | {p['active_evidence_count']} | {p['active_supports']} | {p['active_challenges']} | {p['active_none']} | {p.get('rewrite_status') or ''} | {p.get('debate_stance') or ''} | {p['components'].get('semantic_cap_note') or ''} |")
    approval = f"""# Hwao-staged 2929 trust recompute packet

Packet: `{PACKET_ID}`
Created: `{CREATED_AT}`
Status: `STAGED_ONLY_AWAITING_EXPLICIT_EXECUTION_APPROVAL`
Active public execution phrase: `NO ACTIVE EXECUTION PHRASE`

## Why this packet exists

Hwao/Fable directed a correct-role redo after Tori overstepped. The lane result was:
- Lana: trust is stale relative to the executed 2929 remap because the last trust audit for 2942-2947 predates the remap.
- Goru: no wiki/prose publish packet yet; no Hwao prose delta is supplied and page 57 remains current v1710/hash `{page['content_md5']}`.
- Kun: scratch packet may not be promoted; public phrase surfaces remain `NO ACTIVE EXECUTION PHRASE`.

This packet is new and does not reuse either the consumed DB phrase or the non-authoritative scratch phrase.

## Future write scope if separately approved later

Direct writes:
- Run `recalculate_trust_v2` for claim IDs `{', '.join(map(str, TARGET_IDS))}`.
- Update only `claims.trust_level`, `claims.trust_score`, and `claims.trust_score_updated_at` for those claims.
- Insert one `trust_audit_log` row per target claim with trigger `{TRIGGER}`.

Scope rationale:
- Includes 2929 because it is the `parent_replaced` source/held parent after the remap and now has 14 active `stance='none'` evidence rows.
- Includes successors 2942-2947 because they received/support the remap blast radius.

Explicitly excluded:
- No evidence row changes.
- No `evidence_votes`, comments, element links, or jury scorecard changes.
- No `wiki_pages.content` write.
- No `page_versions` write.
- No page citation/fact-source writes.
- No prose/wiki publish.
- No runtime deploy/restart.
- No git commit/push/merge.
- No cockpit/public helper update.

## Projected trust changes (read-only projection, not execution)

| claim | current level | projected level | current score | projected score | active evidence | supports | challenges | none | rewrite_status | debate_stance | note |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|---|
{chr(10).join(lines)}

## Execution gate

This phrase is local to this packet and is not active/public. Do not execute unless the user later sends exactly the packet-specific execution approval phrase from this packet.

Future execution phrase:
`{EXEC_PHRASE}`

Anything else keeps this packet staged only.

## Rollback gate

Rollback is separate and only applies after a successful execution of this packet. Rollback phrase is in the manifest and rollback script; it is not active now.

## Artifacts

- Backup: `backups/current_state_backup.json`
- Exact diff: `diff/exact_diff.json`
- Summary CSV: `diff/exact_diff_summary.csv`
- Execute script: `scripts/execute_trust_recompute_packet.py`
- Rollback script: `scripts/rollback_trust_recompute_packet.py`
- Read-only precheck SQL: `sql/pre_execute_readonly_verification.sql`
- Read-only postcheck SQL: `sql/post_execute_readonly_verification.sql`
- Validation: `validation/packet_validation.json`

DB writes executed while preparing: 0
Trust recompute executions while preparing: 0
Wiki/prose publish executions while preparing: 0
"""
    (PACKET / 'APPROVAL_PACKET.md').write_text(approval)
    (PACKET / 'reports/HWAO_STAGED_TRUST_RECOMPUTE_PACKET.md').write_text(approval)
    read_only_check = {
        'status': 'PASS' if moved_now == 22 and parent_none == 14 and trigger_count == 0 else 'FAIL',
        'db_writes_executed': 0,
        'trust_recompute_executions': 0,
        'wiki_prose_publish_executions': 0,
        'checks': [
            {'check': 'moved_rows_present', 'actual': moved_now, 'expected': 22, 'ok': moved_now == 22},
            {'check': 'parent_2929_none_rows', 'actual': parent_none, 'expected': 14, 'ok': parent_none == 14},
            {'check': 'packet_trigger_absent', 'actual': trigger_count, 'expected': 0, 'ok': trigger_count == 0},
            {'check': 'wiki_page_content_md5_snapshot', 'actual': page['content_md5'], 'expected': page['content_md5'], 'ok': True},
        ],
        'marker': 'READONLY_NO_WRITE_HWAO_2929_TRUST_STAGE_PACKET_20260705T122901Z',
    }
    jdump(read_only_check, PACKET / 'validation/read_only_no_write_check.json')
    files = [p for p in PACKET.rglob('*') if p.is_file() and p.relative_to(PACKET).as_posix() != 'artifacts/manifest.json' and '__pycache__' not in p.parts and p.suffix != '.pyc']
    manifest = {
        'packet_id': PACKET_ID,
        'created_at_utc': CREATED_AT,
        'status': 'STAGED_ONLY_AWAITING_EXPLICIT_EXECUTION_APPROVAL',
        'active_execution_phrase': 'NO ACTIVE EXECUTION PHRASE',
        'execution_phrase': EXEC_PHRASE,
        'rollback_phrase': ROLLBACK_PHRASE,
        'trigger': TRIGGER,
        'scope': {
            'target_claim_ids': TARGET_IDS,
            'moved_evidence_ids_from_executed_db_packet': MOVED_EVIDENCE_IDS,
            'tables_direct_write_if_approved': ['claims', 'trust_audit_log'],
            'wiki_page_id': int(page['id']),
            'wiki_slug': page['slug'],
            'prose_wiki_publish': False,
        },
        'preconditions': {
            'moved_rows_current': moved_now,
            'parent_2929_active_none_rows': parent_none,
            'trigger_existing_count': trigger_count,
            'wiki_page_content_md5': page['content_md5'],
            'audit_max_by_claim': {str(k): v for k, v in audit_max.items()},
            'target_claim_before_fingerprint_sha256': sha_obj([
                {'id': c['id'], 'trust_level': c['trust_level'], 'trust_score': float(c.get('trust_score') or 0.0), 'trust_score_updated_at': str(c.get('trust_score_updated_at')) if c.get('trust_score_updated_at') else None}
                for c in claims
            ]),
        },
        'projected_levels': {str(p['claim_id']): p['projected_after']['trust_level'] for p in projections},
        'projected_scores': {str(p['claim_id']): p['projected_after']['trust_score'] for p in projections},
        'source_fingerprints': {
            'trust_calculation_path': str(source_path),
            'trust_calculation_sha256': source_sha,
        },
        'phrase_guards': {
            'consumed_db_packet_id_not_reused': CONSUMED_DB_PACKET_ID,
            'scratch_packet_id_not_promoted': SCRATCH_PACKET_ID,
            'public_phrase_must_remain': 'NO ACTIVE EXECUTION PHRASE',
        },
        'db_writes_executed': 0,
        'trust_recompute_executions': 0,
        'wiki_prose_publish_executions': 0,
        'checksums': {
            'execute_script_sha256': sha_path(PACKET / 'scripts/execute_trust_recompute_packet.py'),
            'rollback_script_sha256': sha_path(PACKET / 'scripts/rollback_trust_recompute_packet.py'),
            'files': {str(p.relative_to(PACKET)): sha_path(p) for p in sorted(files)},
        },
    }
    jdump(manifest, PACKET / 'artifacts/manifest.json')
    # Add manifest checksum to run mirror after validation updates will refresh it again.
    for script in [PACKET / 'scripts/execute_trust_recompute_packet.py', PACKET / 'scripts/rollback_trust_recompute_packet.py', PACKET / 'scripts/validate_packet.py']:
        py_compile.compile(str(script), doraise=True)
    if RUN.exists():
        shutil.rmtree(RUN)
    shutil.copytree(PACKET, RUN / 'packet')
    print(json.dumps({'packet': str(PACKET), 'run': str(RUN), 'target_claim_ids': TARGET_IDS, 'projected_levels': manifest['projected_levels'], 'db_writes_executed': 0}, indent=2, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
