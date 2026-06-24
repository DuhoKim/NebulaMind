#!/usr/bin/env python3
"""CCM full-audit harness (Kun, reviewer gate).

Drives the REAL production CCM functions (ADS citing query, S2 context fetch,
Pico classification) and then PROJECTS trust by calling the REAL
recalculate_trust_v2 inside a per-claim SAVEPOINT that is always rolled back.

No permanent DB writes. Emits a JSON report for the audit doc.
"""
from __future__ import annotations

import datetime as dt
import json
import sys
import time
from pathlib import Path

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from sqlalchemy import func
from app.config import settings
from app.database import SessionLocal
import app.models.jury  # noqa: F401 -- REQUIRED: resolves Evidence.consensus_scorecard_id FK -> jury_scorecards.
#   The production miner/runner FAILS to import this, so --commit crashes on first flush.
from app.models.claim import Claim, Evidence
from app.agent_loop.citation_context.miner import (
    DEFAULT_MIN_YEAR,
    build_contexts_for_mapping,
    classify_context,
    insert_supportive_evidence,
    load_enabled_maps,
)

MIN_YEAR = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_MIN_YEAR
ADS_ROWS = int(sys.argv[2]) if len(sys.argv) > 2 else 100
MAX_EV = 6  # CCM_MAX_EVIDENCE_PER_CLAIM_PER_RUN
OUT = BACKEND_ROOT / "scripts" / "ccm_audit_results.json"


def evidence_counts(db, claim_id):
    rows = db.query(Evidence).filter(Evidence.claim_id == claim_id).all()
    n_sup = sum(1 for e in rows if e.stance == "supports")
    n_chal = sum(1 for e in rows if e.stance == "challenges")
    sup_years = [e.year for e in rows if e.stance == "supports" and e.year]
    return n_sup, n_chal, (max(sup_years) if sup_years else None), len(rows)


def main():
    db = SessionLocal()
    maps = load_enabled_maps(db, limit=16)
    print(f"[audit] {len(maps)} enabled maps | min_year={MIN_YEAR} ads_rows={ADS_ROWS} "
          f"thresholds: CONSENSUS_MIN={settings.TRUST_CONSENSUS_MIN} "
          f"MIN_SUPPORTS={settings.TRUST_CONSENSUS_MIN_SUPPORTS} "
          f"FRESHNESS_FLOOR_YEARS={settings.FRESHNESS_FLOOR_YEARS}", flush=True)

    arxiv_budget = [5]
    results = []
    # group maps by claim so multi-bibcode claims aggregate
    from collections import defaultdict
    maps_by_claim = defaultdict(list)
    for m in maps:
        maps_by_claim[m.claim_id].append(m)

    for claim_id, claim_maps in maps_by_claim.items():
        claim = db.get(Claim, claim_id)
        before = {}
        n_sup0, n_chal0, maxy0, ntot0 = evidence_counts(db, claim_id)
        before = {"trust_level": claim.trust_level, "trust_score": round(claim.trust_score or 0.0, 4),
                  "n_supports": n_sup0, "n_challenges": n_chal0, "max_sup_year": maxy0, "n_evidence": ntot0}

        all_decisions = []
        ads_seen_total = 0
        # gather contexts from every bibcode mapped to this claim
        contexts = []
        for m in claim_maps:
            try:
                ctxs, ads_seen = build_contexts_for_mapping(
                    db, m, min_year=MIN_YEAR, ads_rows=ADS_ROWS,
                    max_candidates=20, arxiv_intro_budget=arxiv_budget,
                )
            except Exception as e:
                print(f"[audit] claim {claim_id} map {m.id} build error: {e}", flush=True)
                ctxs, ads_seen = [], 0
            ads_seen_total += ads_seen
            contexts.extend([(m, c) for c in ctxs])

        # classify each context with real Pico
        supportive = []
        rejected = held = offtopic = nonsup = 0
        for (m, ctx) in contexts:
            try:
                v = classify_context(ctx)
            except Exception as e:
                print(f"[audit] claim {claim_id} classify error: {e}", flush=True)
                continue
            dec = {
                "seminal_bibcode": ctx.seminal_bibcode,
                "citer": ctx.citing_bibcode or ctx.citing_arxiv_id or ctx.citing_doi,
                "citer_year": ctx.citing_year,
                "source": ctx.context_source,
                "intent": ctx.s2_intent,
                "hits": ctx.keyphrase_hits,
                "label": v.label,
                "confidence": v.confidence,
                "quality": v.quality,
                "sentence": ctx.context_sentence[:240],
            }
            all_decisions.append(dec)
            if v.label == "SUPPORTIVE" and v.quality is not None:
                supportive.append((ctx, v))
            elif v.label == "SUPPORTIVE":
                held += 1  # LOW confidence -> escalation hold
            elif v.label == "HOLD":
                held += 1
            elif v.label == "NONSUPPORTIVE":
                nonsup += 1; rejected += 1
            else:
                offtopic += 1; rejected += 1
            time.sleep(0.2)

        # PROJECT trust: insert capped supportive into a savepoint, recalc, rollback
        projected = None
        n_insert = min(len(supportive), MAX_EV)
        sp = db.begin_nested()
        try:
            for (ctx, v) in supportive[:n_insert]:
                insert_supportive_evidence(db, ctx, v)
            db.flush()
            from app.services.trust_calculation import recalculate_trust_v2
            new_level, ts = recalculate_trust_v2(claim_id, db, trigger="ccm_audit_dryrun")
            n_sup1, n_chal1, maxy1, ntot1 = evidence_counts(db, claim_id)
            projected = {
                "evidence_inserted": n_insert,
                "supportive_found": len(supportive),
                "trust_level": new_level, "trust_score": round(ts, 4),
                "n_supports": n_sup1, "n_challenges": n_chal1,
                "max_sup_year": maxy1, "n_evidence": ntot1,
                "gate_TS_ok": ts >= settings.TRUST_CONSENSUS_MIN,
                "gate_supports_ok": n_sup1 >= settings.TRUST_CONSENSUS_MIN_SUPPORTS,
                "gate_nochallenge_ok": n_chal1 == 0,
                "freshness_floor_risk": (maxy1 is not None and (dt.datetime.utcnow().year - maxy1) > settings.FRESHNESS_FLOOR_YEARS),
            }
        except Exception as ex:
            print(f"[audit] claim {claim_id} projection error: {type(ex).__name__}: {str(ex)[:140]}", flush=True)
        finally:
            try:
                sp.rollback()
            except Exception:
                db.rollback()

        row = {
            "claim_id": claim_id,
            "bibcodes": [m.canonical_bibcode for m in claim_maps],
            "labels": [m.canonical_label for m in claim_maps],
            "claim_text": (claim.text or "")[:160],
            "ads_citers_seen": ads_seen_total,
            "contexts_built": len(contexts),
            "supportive": len(supportive),
            "nonsupportive": nonsup,
            "offtopic": offtopic,
            "held": held,
            "before": before,
            "projected": projected,
            "decisions": all_decisions,
        }
        results.append(row)
        p = projected or {}
        print(f"[audit] claim {claim_id}: citers={ads_seen_total} ctx={len(contexts)} "
              f"SUP={len(supportive)} NONSUP={nonsup} OFF={offtopic} HELD={held} | "
              f"{before['trust_level']}(TS{before['trust_score']}) -> "
              f"{p.get('trust_level','?')}(TS{p.get('trust_score','?')})", flush=True)

    db.rollback()
    db.close()
    OUT.write_text(json.dumps(results, indent=2, default=str))
    print(f"\n[audit] wrote {OUT}")
    # summary
    greened = sum(1 for r in results if (r.get("projected") or {}).get("trust_level") == "consensus")
    print(f"[audit] claims projected to CONSENSUS: {greened}/{len(results)}")


if __name__ == "__main__":
    main()
