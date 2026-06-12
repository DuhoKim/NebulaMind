"""preserved_elements_strict_v1

Revision ID: dfbbbacc63c2
Revises: evidence_element_links_v1
Create Date: 2026-06-01 01:21:53.293553
"""
import json
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dfbbbacc63c2'
down_revision: Union[str, None] = 'evidence_element_links_v1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Make the column nullable so that unparseable values can be set to NULL
    op.alter_column('claim_rewrite_lineage', 'preserved_elements_json', nullable=True)

    # 2. Get DB connection
    connection = op.get_bind()
    
    # Query all rows from claim_rewrite_lineage
    rows = connection.execute(
        sa.text("SELECT id, preserved_elements_json FROM claim_rewrite_lineage")
    ).fetchall()
    
    converted = 0
    already_strict = 0
    unparseable = 0
    
    for r_id, val in rows:
        if val is None:
            unparseable += 1
            continue
            
        parsed = val
        if isinstance(parsed, str):
            try:
                parsed = json.loads(parsed)
            except Exception:
                # Log to a side audit note
                with open("lineage_normalization_audit.txt", "a", encoding="utf-8") as f:
                    f.write(f"Row {r_id} has unparseable JSON string: {val}\n")
                connection.execute(
                    sa.text("UPDATE claim_rewrite_lineage SET preserved_elements_json = NULL WHERE id = :id"),
                    {"id": r_id}
                )
                unparseable += 1
                continue
                
        if isinstance(parsed, dict):
            if "supporting_evidence_ids" in parsed:
                if "element_id_map" not in parsed:
                    parsed["element_id_map"] = {}
                    connection.execute(
                        sa.text("UPDATE claim_rewrite_lineage SET preserved_elements_json = :val WHERE id = :id"),
                        {"val": json.dumps(parsed), "id": r_id}
                    )
                    converted += 1
                else:
                    already_strict += 1
            else:
                # Dict missing supporting_evidence_ids key
                with open("lineage_normalization_audit.txt", "a", encoding="utf-8") as f:
                    f.write(f"Row {r_id} has dict without supporting_evidence_ids: {val}\n")
                connection.execute(
                    sa.text("UPDATE claim_rewrite_lineage SET preserved_elements_json = NULL WHERE id = :id"),
                    {"id": r_id}
                )
                unparseable += 1
                
        elif isinstance(parsed, list):
            # List [id, ...] -> dict
            new_val = {
                "supporting_evidence_ids": parsed,
                "element_id_map": {}
            }
            connection.execute(
                sa.text("UPDATE claim_rewrite_lineage SET preserved_elements_json = :val WHERE id = :id"),
                {"val": json.dumps(new_val), "id": r_id}
            )
            converted += 1
            
        else:
            # Other types
            with open("lineage_normalization_audit.txt", "a", encoding="utf-8") as f:
                f.write(f"Row {r_id} has unexpected JSON type: {val} ({type(parsed)})\n")
            connection.execute(
                sa.text("UPDATE claim_rewrite_lineage SET preserved_elements_json = NULL WHERE id = :id"),
                {"id": r_id}
            )
            unparseable += 1

    print(f"converted={converted} already_strict={already_strict} unparseable={unparseable}")

    # Drop constraint first if it already exists to be completely idempotent even if downgrade is a no-op
    connection.execute(
        sa.text("ALTER TABLE claim_rewrite_lineage DROP CONSTRAINT IF EXISTS ck_claim_rewrite_lineage_preserved_elements_strict")
    )

    # 3. Add the CHECK constraint to enforce strict format going forward
    op.create_check_constraint(
        "ck_claim_rewrite_lineage_preserved_elements_strict",
        "claim_rewrite_lineage",
        "preserved_elements_json IS NULL OR ("
        "jsonb_typeof(preserved_elements_json) = 'object' AND "
        "jsonb_exists(preserved_elements_json, 'supporting_evidence_ids') AND "
        "jsonb_exists(preserved_elements_json, 'element_id_map')"
        ")"
    )


def downgrade() -> None:
    pass
