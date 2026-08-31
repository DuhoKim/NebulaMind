import sys
import shutil
from pathlib import Path
sys.path.insert(0, str(Path("run").resolve()))
import bs2k_stage_v2 as stage

def test_r2():
    print("Testing R2...")
    # original check
    identity = stage.archive_identity()
    print("identity:", identity)
    
    # temp copy tampering
    receipt_rel = stage.v9_literal("PINNED_PARENT_RECEIPTS_REL")
    receipt = stage.BASE.parent / receipt_rel
    temp_receipt = receipt.with_name(receipt.name + ".temp")
    shutil.copy(receipt, temp_receipt)
    
    # We must mock BASE.parent / receipt_rel to point to temp_receipt?
    # Actually, we can just modify the temp_receipt if we intercept it, or temporarily rename the real one...
    # The instruction says "test via a temp copy, never touching the real receipt". 
    # How? Maybe we can change the literal in v9_ref temp copy? No, we can just monkeypatch `receipt_rel`.
    
    print("Done R2")

test_r2()
