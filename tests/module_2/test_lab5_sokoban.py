import builtins
import importlib
import sys

import pytest

MODULE_NAME = "module_2.lab5_sokoban"


def run_main_until_exhausted(monkeypatch, capsys, responses):
    """Reload the module with mocked input() responses and return what it printed.

    main() runs an unconditional `while True` loop with no exit action, so it
    only ever stops when input() runs out -- here that's StopIteration from
    the mocked responses running dry, mirroring the EOFError a real terminal
    would raise once stdin closes.
    """
    responses_iter = iter(responses)
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(responses_iter))
    with pytest.raises(StopIteration):
        if MODULE_NAME in sys.modules:
            importlib.reload(sys.modules[MODULE_NAME])
        else:
            importlib.import_module(MODULE_NAME)
    return capsys.readouterr().out


def test_appends_each_action_to_history(monkeypatch, capsys):
    # main() runs unconditionally at import time and only ever stops via the
    # StopIteration above, so there's no successfully-imported module left in
    # sys.modules to hasattr-check here the way the other lab tests do.
    out = run_main_until_exhausted(monkeypatch, capsys, ["draw box", "push box"])
    assert out == "['draw box']\n['draw box', 'push box']\n"


def test_undo_removes_and_reports_the_last_action(monkeypatch, capsys):
    out = run_main_until_exhausted(monkeypatch, capsys, ["draw box", "push box", "Undo"])
    assert out == (
        "['draw box']\n"
        "['draw box', 'push box']\n"
        "Undone: 'push box'\n"
        "['draw box']\n"
    )


def test_restart_clears_history(monkeypatch, capsys):
    out = run_main_until_exhausted(monkeypatch, capsys, ["draw box", "Restart"])
    assert out == "['draw box']\n[]\n"
