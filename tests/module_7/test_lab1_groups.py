import builtins
import importlib
import sys

import pytest

MODULE_NAME = "module_7.lab1_groups"


def run_main(monkeypatch, capsys, number):
    """Reload the module with a mocked input() response and return what it printed.

    main() runs unconditionally at import time and reads via input(), so the
    module must be (re)loaded fresh for each scenario rather than imported once
    at collection time.
    """
    monkeypatch.setattr(builtins, "input", lambda prompt="": number)
    if MODULE_NAME in sys.modules:
        importlib.reload(sys.modules[MODULE_NAME])
    else:
        importlib.import_module(MODULE_NAME)
    return capsys.readouterr().out


def test_us_number_reports_united_states_and_canada(monkeypatch, capsys):
    out = run_main(monkeypatch, capsys, "+1 617-495-1000")
    assert hasattr(sys.modules[MODULE_NAME], "main"), "groups.py has no main() function. File may be blank"
    assert out == "United States and Canada\n"


def test_indonesia_number_reports_indonesia(monkeypatch, capsys):
    out = run_main(monkeypatch, capsys, "+62 617-495-1000")
    assert out == "Indonesia\n"


def test_nicaragua_number_reports_nicaragua(monkeypatch, capsys):
    out = run_main(monkeypatch, capsys, "+505 617-495-1000")
    assert out == "Nicaragua\n"


def test_unrecognized_format_reports_unknown(monkeypatch, capsys):
    out = run_main(monkeypatch, capsys, "not a number")
    assert out == "Unknown\n"


def test_valid_format_with_uncovered_country_code_currently_raises_key_error(monkeypatch, capsys):
    # The regex accepts any 1-3 digit country code, but `locations` only has
    # entries for +1, +62, and +505 -- a well-formed number like a UK one
    # (+44) matches the pattern yet isn't in the dict, so main() currently
    # crashes with an uncaught KeyError instead of printing "Unknown".
    monkeypatch.setattr(builtins, "input", lambda prompt="": "+44 617-495-1000")
    with pytest.raises(KeyError):
        if MODULE_NAME in sys.modules:
            importlib.reload(sys.modules[MODULE_NAME])
        else:
            importlib.import_module(MODULE_NAME)
