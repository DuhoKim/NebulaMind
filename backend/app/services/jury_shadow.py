import datetime as dt
import math
import os
import logging
from sqlalchemy.orm import Session
from app.config import settings
from app.services.jury_scorecard import JurorScorecard, PolicySpec, aggregate_scorecards
from app.models.claim import Evidence, EvidenceVote
from app.models.jury import JuryScorecard, JuryAgentProfile, PromptRevision

logger = logging.getLogger(__name__)

def get_or_create_shadow_prompt_revision(db: Session) -> int:
    import hashlib
    
    prompt_id = "stance.v2"
    policy_id = "strict_v1"
    system_text = "Shadow validation system prompt placeholder"
    user_template = "Shadow validation user template placeholder"
    aggregation = {
        "support_threshold": 0.65,
        "refute_threshold": 0.65,
        "abstain_band": [0.35, 0.65],
        "min_quoted_sentence_chars": 25
    }
    
    # Calculate SHA-256
    merged = f"{system_text}\n{user_template}"
    sha = hashlib.sha256(merged.encode("utf-8")).hexdigest()
    
    rev = db.query(PromptRevision).filter(PromptRevision.prompt_sha256 == sha).first()
    if not rev:
        rev = PromptRevision(
            prompt_id=prompt_id,
            policy_id=policy_id,
            prompt_sha256=sha,
            system_text=system_text,
            user_template=user_template,
            aggregation=aggregation
        )
        db.add(rev)
        db.flush()
    return rev.id

def execute_shadow_validation(
    db: Session,
    evidence_id: int | None,
    claim_id: int,
    claim_text: str,
    evidence_title: str,
    legacy_stance: str,
    legacy_quality: float,
    jurors_data: list[dict]  # list of {"agent_id": int, "vote": int (-1/0/1), "confidence_str": str ("LOW"/"MEDIUM"/"HIGH" or None), "reason": str, "model_name": str}
):
    """
    Executes Phase 3 Shadow Validation Mode.
    Runs the 4-axis aggregation, writes/saves scorecard and votes to DB if evidence_id is provided,
    compares stances, and logs any discrepancy.
    """
    # 1. Fetch all agent profiles to get weights
    agent_ids = [jd["agent_id"] for jd in jurors_data if jd.get("agent_id")]
    profiles = {}
    if agent_ids:
        rows = db.query(JuryAgentProfile).filter(JuryAgentProfile.agent_id.in_(agent_ids)).all()
        profiles = {r.agent_id: r for r in rows}

    # 2. Map legacy jurors to JurorScorecard
    juror_scorecards = []
    c_map = {"LOW": 0.33, "MEDIUM": 0.66, "HIGH": 1.0}
    
    for jd in jurors_data:
        aid = jd.get("agent_id")
        if not aid:
            continue
        vote = jd.get("vote", 0)
        conf_str = jd.get("confidence_str") or "MEDIUM"
        c_val = c_map.get(conf_str, 0.66)
        
        if vote == 1:
            v_str = "SUPPORTS"
            r_val, e_val, m_val = 1.0, 1.0, 1.0
        elif vote == -1:
            v_str = "REFUTES"
            r_val, e_val, m_val = 1.0, -1.0, 1.0
        else:
            v_str = "ABSTAIN"
            r_val, e_val, m_val = 0.5, 0.0, 0.5
            
        juror_scorecards.append(JurorScorecard(
            agent_id=aid,
            verdict=v_str,
            R=r_val,
            E=e_val,
            M=m_val,
            C=c_val,
            quoted_sentence=jd.get("reason"),
        ))

    # 3. Aggregate
    policy = PolicySpec()
    consensus = aggregate_scorecards(juror_scorecards, policy, profiles)

    # 4. If evidence_id exists, write to database
    scorecard_id = None
    if evidence_id is not None:
        try:
            # Get prompt revision
            prompt_rev_id = get_or_create_shadow_prompt_revision(db)
            
            # Map jurors used details
            jurors_used_json = []
            for j in juror_scorecards:
                weight_val = consensus.weights.get(j.agent_id, 0.0)
                jurors_used_json.append({
                    "agent_id": j.agent_id,
                    "weight": weight_val,
                    "scheduled_via": "local"
                })
            
            # Insert JuryScorecard
            db_scorecard = JuryScorecard(
                evidence_id=evidence_id,
                prompt_revision_id=prompt_rev_id,
                relevance=consensus.relevance,
                entailment=consensus.entailment,
                rigor=consensus.rigor,
                confidence=consensus.confidence,
                var_entailment=consensus.var_entailment,
                quality_v2=consensus.quality,
                stance=consensus.stance,
                jurors_used=jurors_used_json,
                policy_id="strict_v1"
            )
            db.add(db_scorecard)
            db.flush()
            scorecard_id = db_scorecard.id
            
            # Update Evidence
            ev = db.query(Evidence).filter(Evidence.id == evidence_id).first()
            if ev:
                ev.consensus_scorecard_id = scorecard_id
                ev.relevance = consensus.relevance
                ev.entailment = consensus.entailment
                ev.rigor = consensus.rigor
                ev.confidence = consensus.confidence
                if not settings.JURY_SHADOW_MODE:
                    ev.quality = consensus.quality
                    ev.stance = consensus.stance
                db.flush()
                
            # Update EvidenceVotes of this jury evaluation
            # Find evidence votes created in the last 1 minute for this evidence_id
            one_min_ago = dt.datetime.utcnow() - dt.timedelta(minutes=1)
            votes = db.query(EvidenceVote).filter(
                EvidenceVote.evidence_id == evidence_id,
                EvidenceVote.agent_id.in_(agent_ids),
                EvidenceVote.created_at >= one_min_ago
            ).all()
            
            for vote_row in votes:
                # Find matching juror scorecard
                j_score = next((js for js in juror_scorecards if js.agent_id == vote_row.agent_id), None)
                if j_score:
                    vote_row.prompt_revision_id = prompt_rev_id
                    vote_row.relevance = j_score.R
                    vote_row.entailment = j_score.E
                    vote_row.rigor = j_score.M
                    vote_row.confidence = j_score.C
                    vote_row.scheduled_via = "local"
            db.flush()
        except Exception as e:
            logger.error(f"Failed to save shadow scorecard to DB for evidence #{evidence_id}: {e}", exc_info=True)

    # 5. Compare stances and log discrepancy
    if legacy_stance != consensus.stance:
        log_dir = "/Users/duhokim/NebulaMind/NebulaMind/backend/logs"
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.join(log_dir, "jury_shadow_validation.log")
        
        timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = (
            f"[{timestamp}] [DISCREPANCY]\n"
            f"Claim ID: {claim_id}\n"
            f"Claim Text: {claim_text.strip()}\n"
            f"Evidence ID: {evidence_id}\n"
            f"Evidence Title: {evidence_title.strip()}\n"
            f"Legacy Stance: {legacy_stance} (Quality: {legacy_quality:.4f})\n"
            f"New Scorecard Stance: {consensus.stance} (Quality V2: {consensus.quality:.4f})\n"
            f"New Scores: Relevance={consensus.relevance:.4f}, Entailment={consensus.entailment:.4f}, Rigor={consensus.rigor:.4f}, Confidence={consensus.confidence:.4f}\n"
            f"Variance of Entailment: {consensus.var_entailment:.4f}\n"
            f"Juror Details:\n"
        )
        for jd in jurors_data:
            log_entry += f"  - Agent #{jd.get('agent_id')} ({jd.get('model_name')}): Vote={jd.get('vote')}, Conf={jd.get('confidence_str') or 'MEDIUM'}, Reason={jd.get('reason')}\n"
        log_entry += "--------------------------------------------------\n"
        
        try:
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(log_entry)
        except Exception as e:
            logger.error(f"Failed to write to jury_shadow_validation.log: {e}")
            
    return consensus
