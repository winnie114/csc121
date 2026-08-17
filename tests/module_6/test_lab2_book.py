import importlib
import sys

MODULE_NAME = "module_6.lab2_book"


def test_main_extracts_lines_53_through_272_into_chapter1(monkeypatch, tmp_path):
    # main() reads "alice.txt" and writes "chapter1.txt" relative to the
    # current directory and runs unconditionally at import time, so this uses
    # a small synthetic "alice.txt" (300 numbered lines) in a tmp_path rather
    # than the real book text, and (re)loads the module fresh under that
    # directory.
    monkeypatch.chdir(tmp_path)
    lines = [f"Line {i}\n" for i in range(300)]
    (tmp_path / "alice.txt").write_text("".join(lines))

    if MODULE_NAME in sys.modules:
        importlib.reload(sys.modules[MODULE_NAME])
    else:
        importlib.import_module(MODULE_NAME)

    assert hasattr(sys.modules[MODULE_NAME], "main"), "book.py has no main() function. File may be blank"

    chapter1 = (tmp_path / "chapter1.txt").read_text()
    assert chapter1 == "".join(lines[52:272])
    assert chapter1.splitlines()[0] == "Line 52"
    assert chapter1.splitlines()[-1] == "Line 271"
