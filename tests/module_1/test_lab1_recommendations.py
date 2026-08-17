import builtins
import importlib
import sys

MODULE_NAME = "module_1.lab1_recommendations"


def run_main(monkeypatch, capsys, responses):
    """Reload the module with mocked input() responses and return what it printed.

    main() runs unconditionally at import time and reads via input(), so the
    module must be (re)loaded fresh for each scenario rather than imported once
    at collection time.
    """
    responses_iter = iter(responses)
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(responses_iter))
    if MODULE_NAME in sys.modules:
        importlib.reload(sys.modules[MODULE_NAME])
    else:
        importlib.import_module(MODULE_NAME)
    return capsys.readouterr().out


def test_difficult_multiplayer_recommends_poker(monkeypatch, capsys):
    out = run_main(monkeypatch, capsys, ["Difficult", "Multiplayer"])
    assert hasattr(sys.modules[MODULE_NAME], "main"), "boolean_expressions.py has no main() function. File may be blank"
    assert out == "You might like Poker\n"


def test_difficult_single_player_recommends_klondike(monkeypatch, capsys):
    out = run_main(monkeypatch, capsys, ["Difficult", "Single-player"])
    assert out == "You might like Klondike\n"


def test_casual_multiplayer_recommends_hearts(monkeypatch, capsys):
    out = run_main(monkeypatch, capsys, ["Casual", "Multiplayer"])
    assert out == "You might like Hearts\n"


def test_casual_single_player_recommends_clock(monkeypatch, capsys):
    out = run_main(monkeypatch, capsys, ["Casual", "Single-player"])
    assert out == "You might like Clock\n"


def test_invalid_difficulty_returns_before_reading_players(monkeypatch, capsys):
    # Only one response is queued: main() must return after the invalid
    # difficulty check without ever calling input() for players.
    out = run_main(monkeypatch, capsys, ["Hardcore"])
    assert out == "Enter a valid difficulty\n"


def test_invalid_players(monkeypatch, capsys):
    out = run_main(monkeypatch, capsys, ["Difficult", "Coop"])
    assert out == "Enter a valid number of players\n"
