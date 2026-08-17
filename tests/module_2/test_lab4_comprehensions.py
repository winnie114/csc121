import csv
import importlib
import sys
from pathlib import Path

MODULE_NAME = "module_2.lab4_comprehensions"
MODULE_2_SRC = Path(__file__).resolve().parents[2] / "src" / "module_2"


def test_should_write_word_counts_for_words_longer_than_four_letters(monkeypatch, capsys, tmp_path):
    # lab4_comprehensions.py does `from helpers import ...` (a bare, unqualified
    # import, matching how the script is meant to be run from inside
    # src/module_2), so that directory must also be on sys.path for the import
    # to resolve. main() also runs unconditionally at import time and reads
    # "address.txt" / writes "counts.csv" relative to the current directory.
    monkeypatch.syspath_prepend(str(MODULE_2_SRC))
    monkeypatch.chdir(tmp_path)
    (tmp_path / "address.txt").write_text(
        "Apple apple BANANA banana Cherry cherry cherry Date fig doggone doggone"
    )

    if MODULE_NAME in sys.modules:
        importlib.reload(sys.modules[MODULE_NAME])
    else:
        importlib.import_module(MODULE_NAME)

    assert hasattr(sys.modules[MODULE_NAME], "main"), "comprehensions.py has no main() function. File may be blank"

    with open(tmp_path / "counts.csv", newline="") as f:
        rows = list(csv.reader(f))

    assert rows == [
        ["Word", "Count"],
        ["cherry", "3"],
        ["apple", "2"],
        ["banana", "2"],
        ["doggone", "2"],
    ]
