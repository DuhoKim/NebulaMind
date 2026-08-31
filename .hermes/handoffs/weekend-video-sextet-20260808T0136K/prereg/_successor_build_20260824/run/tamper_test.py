import bs2k_stage_v2 as stage
import shutil
import json

# R2 tampered copy test
def r2_tamper():
    receipt_rel = stage.v9_literal("PINNED_PARENT_RECEIPTS_REL")
    real = stage.BASE.parent / receipt_rel
    temp = real.with_name(real.name + ".temp")
    shutil.copy(real, temp)
    with temp.open("a") as f:
        f.write(" ")
    
    # monkeypatch to use temp
    orig = stage.BASE
    stage.BASE = temp.parent.parent
    # wait, receipt = BASE.parent / receipt_rel
    # If BASE = temp.parent.parent, BASE.parent = temp.parent.parent.parent
    # Let's monkeypatch v9_literal to return the temp path relative to BASE.parent
    orig_v9 = stage.v9_literal
    def mock_v9(name):
        if name == "PINNED_PARENT_RECEIPTS_REL":
            return receipt_rel.replace(real.name, temp.name)
        return orig_v9(name)
    stage.v9_literal = mock_v9

    try:
        stage.archive_identity()
        print("R2 TAMPER FAILED: Did not refuse")
    except stage.Refusal as e:
        print(f"R2 TAMPER SUCCESS: Refused with {e.code}")
    finally:
        stage.v9_literal = orig_v9
        temp.unlink()

r2_tamper()

# R3 tampered copy test
def r3_tamper():
    real = stage.X2_COMMIT
    temp = real.with_name(real.name + ".temp")
    content = real.read_text().replace("COMMITTEE-READ", "COMMITTEE-READX")
    temp.write_text(content)
    
    orig_x2 = stage.X2_COMMIT
    stage.X2_COMMIT = temp
    try:
        stage.x2_material()
        print("R3 TAMPER FAILED: Did not refuse")
    except stage.Refusal as e:
        print(f"R3 TAMPER SUCCESS: Refused with {e.code}")
    finally:
        stage.X2_COMMIT = orig_x2
        temp.unlink()

r3_tamper()
