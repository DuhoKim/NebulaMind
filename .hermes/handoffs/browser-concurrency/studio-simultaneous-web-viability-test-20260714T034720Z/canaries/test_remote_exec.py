"""No-browser regression tests for stdin-fed remote execution + quoting safety.

Runs entirely local (channel_argv=[] -> local `python3 -`); proves the script is
delivered as stdin data and never reparsed by a shell, so hostile path content
cannot inject commands or break parsing. This is exactly the failure class that
STOPped XM-1 pass1 (remote `python3 -c` reparsed by zsh).
"""
import hashlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from remote_exec import preflight_empty_dir_script, run_python_stdin, sha256_script


def test_preflight_empty_dir_exit0(tmp_path):
    rc, _, err = run_python_stdin([], preflight_empty_dir_script(str(tmp_path)))
    assert rc == 0, err


def test_preflight_nonexistent_exit0(tmp_path):
    rc, _, _ = run_python_stdin([], preflight_empty_dir_script(str(tmp_path / "missing")))
    assert rc == 0


def test_preflight_nonempty_dir_exit2(tmp_path):
    (tmp_path / "x").write_text("1")
    rc, _, _ = run_python_stdin([], preflight_empty_dir_script(str(tmp_path)))
    assert rc == 2


def test_injection_path_is_literal_no_side_effect(tmp_path):
    sentinel = tmp_path / "PWNED"
    evil = f'{tmp_path}/nm x; $(touch "{sentinel}") && rm -rf * \'"`echo hi`'
    rc, _, _ = run_python_stdin([], preflight_empty_dir_script(evil))
    assert rc == 0                    # treated as a single literal (nonexistent) path
    assert not sentinel.exists()      # nothing was executed by any shell


def test_sha256_script_matches(tmp_path):
    f = tmp_path / "controller.py"
    f.write_bytes(b"print('hi')\n# path with weird name irrelevant\n")
    rc, out, err = run_python_stdin([], sha256_script(str(f)))
    assert rc == 0, err
    assert out.strip() == hashlib.sha256(f.read_bytes()).hexdigest()


def test_sha256_script_literal_path_with_metachars(tmp_path):
    weird = tmp_path / "a b;c$d"
    weird.write_bytes(b"xyz")
    rc, out, _ = run_python_stdin([], sha256_script(str(weird)))
    assert rc == 0
    assert out.strip() == hashlib.sha256(b"xyz").hexdigest()
