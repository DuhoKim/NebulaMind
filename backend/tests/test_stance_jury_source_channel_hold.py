import sys
from pathlib import Path
from types import SimpleNamespace

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.agent_loop import tasks
from app.database import Base
from app.models import (
    agent, arxiv, autowiki, benchmark, claim, claim_rewrite_lineage, comment,
    council, edit, evidence_element_link, external, facility, feedback, graph,
    jury, page, qa, reference, research_idea, social, spotlight, subscriber,
    survey, visitor, vote,
)
from app.models.claim import Claim, Evidence
from app.models.page import WikiPage


def test_overnight_packet_source_channel_is_held_from_stance_jury(monkeypatch):
    monkeypatch.setattr(
        tasks,
        "settings",
        SimpleNamespace(
            STANCE_JURY_HELD_PAGE_IDS="",
            STANCE_JURY_HELD_CLAIM_IDS="",
            STANCE_JURY_HELD_EVIDENCE_IDS="",
            STANCE_JURY_HELD_SOURCE_CHANNELS="overnight_paper_harness_v1",
        ),
    )
    evidence = SimpleNamespace(
        id=29757,
        claim_id=2929,
        source_channel="overnight_paper_harness_v1",
    )

    assert tasks._stance_jury_is_held(ev=evidence) is True


def test_drain_stance_jury_backlog_skips_held_source_channel_but_keeps_manual_queueable(
    monkeypatch,
    tmp_path,
):
    engine = create_engine(
        f"sqlite:///{tmp_path / 'stance_jury.db'}",
        connect_args={"check_same_thread": False},
    )
    Base.metadata.create_all(bind=engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    db = TestingSessionLocal()
    try:
        page = WikiPage(id=58, slug="galaxy-v2", title="Galaxy V2")
        packet_claim = Claim(id=2929, page_id=58, text="Packet claim", trust_level="accepted")
        manual_claim = Claim(id=2930, page_id=58, text="Manual claim", trust_level="accepted")
        packet_evidence = Evidence(
            id=29757,
            claim_id=2929,
            title="Packet evidence",
            stance="supports",
            quality=1.0,
            abstract="x" * 200,
            source_channel="overnight_paper_harness_v1",
        )
        manual_evidence = Evidence(
            id=40001,
            claim_id=2930,
            title="Manual evidence",
            stance="supports",
            quality=1.0,
            abstract="x" * 200,
            source_channel="manual",
        )
        db.add_all([page, packet_claim, manual_claim, packet_evidence, manual_evidence])
        db.commit()
    finally:
        db.close()

    settings = SimpleNamespace(
        STANCE_JURY_ENABLED=True,
        STANCE_JURY_MAX_PER_HOUR=100,
        STANCE_JURY_MAX_ENQUEUE_PER_HOUR=10,
        STANCE_JURY_MIN_ABSTRACT_CHARS=100,
        INTRO_EXCERPT_MIN_CHARS=100,
        STANCE_JURY_ENQUEUE_SPACING_SECONDS=90,
        STANCE_JURY_HELD_PAGE_IDS="",
        STANCE_JURY_HELD_CLAIM_IDS="",
        STANCE_JURY_HELD_EVIDENCE_IDS="",
        STANCE_JURY_HELD_SOURCE_CHANNELS="overnight_paper_harness_v1",
    )
    enqueued = []

    monkeypatch.setattr(tasks, "settings", settings)
    monkeypatch.setattr(tasks, "SessionLocal", TestingSessionLocal)
    monkeypatch.setattr(tasks, "_notify", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(
        tasks,
        "_enqueue_stance_jury_task",
        lambda _task, evidence_id, countdown: enqueued.append((evidence_id, countdown)) or True,
    )

    tasks.drain_stance_jury_backlog.run()

    assert [evidence_id for evidence_id, _countdown in enqueued] == [40001]
