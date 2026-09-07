import pathlib, shutil
stale = pathlib.Path(__file__).resolve().parent / "_review2_kimi"
if stale.is_dir() and str(stale).endswith("_review2_kimi/_review2_kimi"):
    shutil.rmtree(stale)
    print("removed stale nested dir:", stale)
else:
    print("nothing to remove:", stale)
