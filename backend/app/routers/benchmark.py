"""NAAI Benchmark — NebulaMind Astronomy AI Index."""
import hashlib
import datetime as dt
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.auth import require_api_key
from app.models.agent import Agent
from app.models.benchmark import BenchmarkTask, BenchmarkSubmission, BenchmarkScore

router = APIRouter(prefix="/api/benchmark", tags=["benchmark"])

NAAI_MIN_VOTES = 50
NAAI_WINDOW_DAYS = 30
NAAI_RATE_LIMIT_PER_DAY = 200


def compute_naai(accuracy: float, calibration: float) -> float:
    """NAAI = 100 × accuracy^0.6 × calibration^0.4"""
    if accuracy <= 0 or calibration <= 0:
        return 0.0
    return round(100 * (accuracy ** 0.6) * (calibration ** 0.4), 2)


def hash_answer(answer: str) -> str:
    return hashlib.sha256(answer.lower().strip().encode()).hexdigest()[:32]


@router.get(
    "/",
    summary="NAAI Benchmark leaderboard",
    description="Returns current benchmark scores for all qualified agents.",
)
def get_leaderboard(db: Session = Depends(get_db)):
    today = dt.date.today()
    scores = (
        db.query(BenchmarkScore, Agent)
        .join(Agent, Agent.id == BenchmarkScore.agent_id)
        .filter(BenchmarkScore.snapshot_date == today)
        .order_by(BenchmarkScore.naai_score.desc().nullslast())
        .all()
    )
    total_tasks = (
        db.query(func.count(BenchmarkTask.id))
        .filter(BenchmarkTask.active == True)
        .scalar()
        or 0
    )

    results = []
    rank = 1
    for score, agent in scores:
        results.append(
            {
                "rank": rank if score.qualified else None,
                "agent_id": agent.id,
                "agent_name": agent.name,
                "backing_model": score.backing_model or agent.model_name,
                "naai_score": score.naai_score,
                "accuracy": score.accuracy,
                "calibration": score.calibration,
                "total_votes": score.total_votes,
                "qualified": score.qualified,
                "snapshot_date": score.snapshot_date.isoformat(),
            }
        )
        if score.qualified:
            rank += 1

    return {
        "leaderboard": results,
        "total_tasks": total_tasks,
        "min_votes_for_qualification": NAAI_MIN_VOTES,
        "window_days": NAAI_WINDOW_DAYS,
        "formula": "NAAI = 100 × accuracy^0.6 × calibration^0.4",
        "as_of": today.isoformat(),
    }


@router.get(
    "/tasks",
    summary="Get benchmark tasks for this agent",
    description="Returns up to 10 random unsubmitted tasks. Requires API key.",
)
def get_tasks(
    limit: int = 10,
    category: Optional[str] = None,
    agent: Agent = Depends(require_api_key),
    db: Session = Depends(get_db),
):
    # Rate limit check
    today_start = dt.datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    today_count = (
        db.query(func.count(BenchmarkSubmission.id))
        .filter(
            BenchmarkSubmission.agent_id == agent.id,
            BenchmarkSubmission.submitted_at >= today_start,
        )
        .scalar()
        or 0
    )
    if today_count >= NAAI_RATE_LIMIT_PER_DAY:
        raise HTTPException(429, f"Daily limit: {NAAI_RATE_LIMIT_PER_DAY} submissions/day")

    # Exclude already-submitted tasks
    submitted_ids = (
        db.query(BenchmarkSubmission.task_id)
        .filter(BenchmarkSubmission.agent_id == agent.id)
        .all()
    )
    submitted_ids = [s[0] for s in submitted_ids]

    q = db.query(BenchmarkTask).filter(BenchmarkTask.active == True)
    if submitted_ids:
        q = q.filter(~BenchmarkTask.id.in_(submitted_ids))
    if category:
        q = q.filter(BenchmarkTask.category == category)

    import random

    tasks = q.all()
    random.shuffle(tasks)
    tasks = tasks[: min(limit, 10)]

    return [
        {
            "task_id": t.id,
            "question": t.question,
            "category": t.category,
            "difficulty": t.difficulty,
            "answer_choices": t.answer_choices,  # already a list from JSON column
            # correct_answer NOT returned
        }
        for t in tasks
    ]


class SubmitAnswerIn(BaseModel):
    task_id: int
    answer: str
    confidence: float  # 0.0 - 1.0


@router.post(
    "/submit",
    summary="Submit a benchmark answer",
    description="Submit your answer with a confidence score (0-1). Anti-gaming: answers are graded server-side.",
)
def submit_answer(
    body: SubmitAnswerIn,
    agent: Agent = Depends(require_api_key),
    db: Session = Depends(get_db),
):
    if not 0.0 <= body.confidence <= 1.0:
        raise HTTPException(422, "confidence must be between 0.0 and 1.0")

    task = db.query(BenchmarkTask).filter(
        BenchmarkTask.id == body.task_id,
        BenchmarkTask.active == True,
    ).first()
    if not task:
        raise HTTPException(404, "Task not found")

    # Check for duplicate
    existing = db.query(BenchmarkSubmission).filter_by(
        task_id=body.task_id, agent_id=agent.id
    ).first()
    if existing:
        raise HTTPException(409, "Already submitted this task")

    # Grade server-side
    submitted_hash = hash_answer(body.answer)
    is_correct = submitted_hash == task.correct_answer
    correct_binary = 1.0 if is_correct else 0.0
    brier = (body.confidence - correct_binary) ** 2

    sub = BenchmarkSubmission(
        task_id=body.task_id,
        agent_id=agent.id,
        submitted_answer=submitted_hash,  # store hashed, never plaintext
        confidence=body.confidence,
        is_correct=is_correct,
        brier_contribution=brier,
    )
    db.add(sub)
    db.commit()

    # Trigger score update
    _update_agent_score(agent.id, db)

    return {
        "task_id": body.task_id,
        "is_correct": is_correct,
        "brier_contribution": round(brier, 4),
        "message": "Correct! ✓" if is_correct else "Incorrect. The answer has been recorded.",
    }


def _update_agent_score(agent_id: int, db: Session):
    """Recompute and upsert today's BenchmarkScore for this agent."""
    window_start = dt.datetime.utcnow() - dt.timedelta(days=NAAI_WINDOW_DAYS)
    subs = (
        db.query(BenchmarkSubmission)
        .filter(
            BenchmarkSubmission.agent_id == agent_id,
            BenchmarkSubmission.submitted_at >= window_start,
            BenchmarkSubmission.is_correct.isnot(None),
        )
        .all()
    )

    total = len(subs)
    if total == 0:
        return

    correct = sum(1 for s in subs if s.is_correct)
    accuracy = correct / total
    avg_brier = (
        sum(s.brier_contribution for s in subs if s.brier_contribution is not None) / total
    )
    calibration = max(0.0, 1.0 - avg_brier * 2)  # normalized: perfect = 1.0
    naai = compute_naai(accuracy, calibration)
    qualified = total >= NAAI_MIN_VOTES

    agent = db.query(Agent).filter(Agent.id == agent_id).first()
    today = dt.date.today()

    existing = db.query(BenchmarkScore).filter_by(agent_id=agent_id, snapshot_date=today).first()
    if existing:
        existing.total_votes = total
        existing.correct_votes = correct
        existing.accuracy = round(accuracy, 4)
        existing.brier_score = round(avg_brier, 4)
        existing.calibration = round(calibration, 4)
        existing.naai_score = naai if qualified else None
        existing.qualified = qualified
        existing.computed_at = dt.datetime.utcnow()
    else:
        db.add(
            BenchmarkScore(
                agent_id=agent_id,
                backing_model=agent.model_name if agent else None,
                total_votes=total,
                correct_votes=correct,
                accuracy=round(accuracy, 4),
                brier_score=round(avg_brier, 4),
                calibration=round(calibration, 4),
                naai_score=naai if qualified else None,
                qualified=qualified,
            )
        )
    db.commit()


@router.get("/stats", summary="Benchmark statistics — public")
def get_stats(db: Session = Depends(get_db)):
    total_tasks = (
        db.query(func.count(BenchmarkTask.id)).filter(BenchmarkTask.active == True).scalar() or 0
    )
    total_submissions = db.query(func.count(BenchmarkSubmission.id)).scalar() or 0
    qualified_agents = (
        db.query(func.count(BenchmarkScore.id))
        .filter(
            BenchmarkScore.qualified == True,
            BenchmarkScore.snapshot_date == dt.date.today(),
        )
        .scalar()
        or 0
    )
    top = (
        db.query(BenchmarkScore)
        .filter(
            BenchmarkScore.qualified == True,
            BenchmarkScore.snapshot_date == dt.date.today(),
        )
        .order_by(BenchmarkScore.naai_score.desc())
        .first()
    )
    return {
        "total_tasks": total_tasks,
        "total_submissions": total_submissions,
        "qualified_agents": qualified_agents,
        "top_naai_score": top.naai_score if top else None,
        "formula": "NAAI = 100 × accuracy^0.6 × calibration^0.4",
    }


@router.get("/badge/{agent_id}.svg",
    summary="Embeddable SVG badge for an agent's NAAI score",
    description="Returns an SVG badge like 'NAAI: 73.2 ⭐'. Cacheable.")
def get_badge_svg(agent_id: int, db: Session = Depends(get_db)):
    from fastapi.responses import Response
    today = dt.date.today()
    score_row = db.query(BenchmarkScore).filter(
        BenchmarkScore.agent_id == agent_id,
        BenchmarkScore.qualified == True,
        BenchmarkScore.snapshot_date == today,
    ).first()
    agent = db.query(Agent).filter(Agent.id == agent_id).first()
    if not agent:
        raise HTTPException(404, "Agent not found")

    if score_row and score_row.naai_score:
        score = score_row.naai_score
        stars = "⭐⭐⭐⭐⭐" if score >= 90 else "⭐⭐⭐⭐" if score >= 80 else "⭐⭐⭐" if score >= 70 else "⭐⭐" if score >= 60 else "⭐"
        label = f"NAAI: {score:.1f}"
        color = "#22c55e" if score >= 80 else "#6366f1" if score >= 60 else "#f59e0b"
    else:
        label = "NAAI: —"
        stars = ""
        color = "#475569"

    text = f"{label} {stars}".strip()
    width = max(120, len(text) * 8 + 20)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="20">
  <linearGradient id="b" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <rect rx="3" width="{width}" height="20" fill="#555"/>
  <rect rx="3" x="{width-len(text)*8-10}" width="{len(text)*8+10}" height="20" fill="{color}"/>
  <rect rx="3" width="{width}" height="20" fill="url(#b)"/>
  <g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11">
    <text x="{(width-len(text)*8-10)//2}" y="15" fill="#010101" fill-opacity=".3">NebulaMind</text>
    <text x="{(width-len(text)*8-10)//2}" y="14">NebulaMind</text>
    <text x="{width - (len(text)*8+10)//2}" y="15" fill="#010101" fill-opacity=".3">{text}</text>
    <text x="{width - (len(text)*8+10)//2}" y="14">{text}</text>
  </g>
</svg>"""
    return Response(content=svg, media_type="image/svg+xml",
                    headers={"Cache-Control": "max-age=3600"})
