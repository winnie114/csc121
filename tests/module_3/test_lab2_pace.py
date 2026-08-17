import importlib.util
from pathlib import Path

import pytest

MODULE_PATH = Path(__file__).resolve().parents[2] / "src" / "module_3" / "lab2_pace.py"


def load_module_expecting_value_error():
    # main() hardcodes get_pace(miles=26.2, minutes=0), and get_pace() itself
    # rejects minutes <= 0, so simply importing this module currently raises
    # ValueError before reaching the bottom of the file. A plain import
    # would drop the module from sys.modules once that happens, so we load it
    # via its file path directly to keep a handle on get_pace() regardless.
    spec = importlib.util.spec_from_file_location("lab2_pace_under_test", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    with pytest.raises(ValueError, match="Minutes must be greater than 0"):
        spec.loader.exec_module(module)
    return module


def test_get_pace_computes_minutes_per_mile():
    module = load_module_expecting_value_error()
    assert hasattr(module, "get_pace"), "pace.py has no get_pace() function. File may be blank"
    assert module.get_pace(miles=26.2, minutes=131) == pytest.approx(131 / 26.2)


def test_get_pace_raises_for_non_positive_minutes():
    module = load_module_expecting_value_error()
    with pytest.raises(ValueError, match="Minutes must be greater than 0"):
        module.get_pace(miles=26.2, minutes=0)
    with pytest.raises(ValueError, match="Minutes must be greater than 0"):
        module.get_pace(miles=26.2, minutes=-5)


def test_main_currently_raises_because_it_calls_get_pace_with_zero_minutes():
    # Pins down today's (buggy) behavior: main() passes minutes=0, which is
    # exactly the case get_pace() is designed to reject.
    load_module_expecting_value_error()
