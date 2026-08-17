import importlib
import random
import sys
from pathlib import Path

MODULE_NAME = "module_2.lab9_water"
MODULE_2_SRC = Path(__file__).resolve().parents[2] / "src" / "module_2"


def test_should_print_moisture_readings_until_time_to_water(monkeypatch, capsys):
    # lab9_water.py does `from soil import sample` (a bare, unqualified
    # import), so src/module_2 must also be on sys.path for that to resolve.
    # main() also runs unconditionally at import time and its readings come
    # from soil's random-based sample(), so random.randint is mocked for a
    # deterministic sequence.
    monkeypatch.syspath_prepend(str(MODULE_2_SRC))
    values_iter = iter([30, 5, 5])  # initial moisture, then two decrements
    monkeypatch.setattr(random, "randint", lambda a, b: next(values_iter))

    if MODULE_NAME in sys.modules:
        importlib.reload(sys.modules[MODULE_NAME])
    else:
        importlib.import_module(MODULE_NAME)

    assert hasattr(sys.modules[MODULE_NAME], "main"), "water.py has no main() function. File may be blank"
    captured = capsys.readouterr()
    assert captured.out == (
        "Day 0: Moisture is 25%.\n"
        "Day 1: Moisture is 20%.\n"
        "Time to water!\n"
    )
