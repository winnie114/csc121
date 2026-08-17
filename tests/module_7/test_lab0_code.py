import builtins
import importlib
import sys

MODULE_NAME = "module_7.lab0_code"


def run_main(monkeypatch, capsys, code):
    """Reload the module with a mocked input() response and return what it printed.

    main() runs unconditionally at import time and reads via input(), so the
    module must be (re)loaded fresh for each scenario rather than imported once
    at collection time.
    """
    monkeypatch.setattr(builtins, "input", lambda prompt="": code)
    if MODULE_NAME in sys.modules:
        importlib.reload(sys.modules[MODULE_NAME])
    else:
        importlib.import_module(MODULE_NAME)
    return capsys.readouterr().out


def test_valid_hex_code_reports_the_match(monkeypatch, capsys):
    out = run_main(monkeypatch, capsys, "#1a2b3c")
    assert hasattr(sys.modules[MODULE_NAME], "main"), "code.py has no main() function. File may be blank"
    assert out == "Valid. Matched with #1a2b3c\n"


def test_missing_hash_is_invalid(monkeypatch, capsys):
    out = run_main(monkeypatch, capsys, "1a2b3c")
    assert out == "Invalid\n"


def test_wrong_length_is_invalid(monkeypatch, capsys):
    out = run_main(monkeypatch, capsys, "#1a2b3")
    assert out == "Invalid\n"


def test_non_hex_character_is_invalid(monkeypatch, capsys):
    out = run_main(monkeypatch, capsys, "#1a2b3g")
    assert out == "Invalid\n"
