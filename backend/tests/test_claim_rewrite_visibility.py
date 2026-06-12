import sys
from pathlib import Path

from sqlalchemy.dialects import postgresql

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.routers.claims import visible_claim_filter


def test_visible_claim_filter_hides_parent_replaced_status():
    compiled = str(
        visible_claim_filter().compile(
            dialect=postgresql.dialect(),
            compile_kwargs={"literal_binds": True},
        )
    )

    assert "rewrite_status IS NULL" in compiled
    assert "rewrite_status != 'parent_replaced'" in compiled
